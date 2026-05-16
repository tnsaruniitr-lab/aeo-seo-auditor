"""
main.py — FastAPI service exposing the standalone auditor.

Three endpoints:
    POST /audit          — kick off an audit (async, returns audit_id)
    GET  /audit/{id}     — fetch status + result (poll until completed)
    GET  /healthz        — service health check

Plus convenience routes:
    GET /audit/{id}.json — raw JSON
    GET /audit/{id}.md   — Markdown report
    GET /audit/{id}.pdf  — PDF summary
    GET /audit/{id}.html — preview-friendly HTML render

USAGE
    pip install fastapi uvicorn anthropic python-dotenv
    export ANTHROPIC_API_KEY="sk-ant-..."
    uvicorn main:app --host 0.0.0.0 --port 8000

ENVIRONMENT VARIABLES
    ANTHROPIC_API_KEY  — required for audit narrative generation
    AUDIT_OUTPUT_DIR   — where to write audit artifacts (default: ./audits/)
    PORT               — port to bind (default: 8000)
"""

from __future__ import annotations

import logging
import os
import sys
import threading
import time
import traceback
import uuid
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, Optional


# ----------------------------------------------------------------------
# LOGGING — configured early so all modules picking up loggers inherit it
# ----------------------------------------------------------------------

LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO').upper()

logging.basicConfig(
    level=LOG_LEVEL,
    format='%(asctime)s %(levelname)s %(name)s: %(message)s',
    datefmt='%H:%M:%S',
    stream=sys.stdout,
    force=True,
)
log = logging.getLogger('audit')

# Quiet down noisy third-party loggers unless we asked for DEBUG
if LOG_LEVEL != 'DEBUG':
    logging.getLogger('httpx').setLevel(logging.WARNING)
    logging.getLogger('anthropic').setLevel(logging.WARNING)
    logging.getLogger('httpcore').setLevel(logging.WARNING)

# Load .env if present (graceful fallback if python-dotenv not installed)
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

THIS_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(THIS_DIR))

import secrets

from fastapi import FastAPI, HTTPException, BackgroundTasks, Depends, status
from fastapi.responses import FileResponse, JSONResponse, PlainTextResponse, HTMLResponse
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from pydantic import BaseModel, HttpUrl

from audit_pipeline import run_audit as run_audit_deterministic

# Agent-mode (full parity with the chat skill) is opt-in via AUDIT_MODE env var.
# Default is "agent" once the parity layer is deployed; falls back automatically
# if dependencies (Playwright, Tavily key, etc.) aren't ready.
AUDIT_MODE = os.getenv('AUDIT_MODE', 'agent').lower().strip()

try:
    from agent import run_audit_agent
    AGENT_AVAILABLE = True
except Exception as _agent_import_err:
    AGENT_AVAILABLE = False
    _AGENT_IMPORT_ERROR = str(_agent_import_err)


def run_audit(url: str, output_dir: str, progress_callback=None):
    """Dispatch to the chosen audit pipeline.

    Modes:
        - 'agent'         : full 15-phase parity loop (matches chat skill)
        - 'deterministic' : legacy fast path (scripts + 1 Sonnet call)
        - 'auto'          : agent if available, else deterministic

    progress_callback (optional): called with a dict {phase, tool, turn,
    tool_count, elapsed_seconds, last_tool_ms} after each tool call when
    running in agent mode. Ignored by the deterministic path.
    """
    mode = AUDIT_MODE
    if mode == 'agent' and not AGENT_AVAILABLE:
        # Hard-fail if the user explicitly asked for agent and it's broken
        raise RuntimeError(
            f"AUDIT_MODE=agent requested but agent module failed to import: "
            f"{_AGENT_IMPORT_ERROR}"
        )
    if mode == 'auto':
        mode = 'agent' if AGENT_AVAILABLE else 'deterministic'
    if mode == 'agent':
        return run_audit_agent(url, output_dir=output_dir, verbose=False,
                                progress_callback=progress_callback)
    return run_audit_deterministic(url, output_dir=output_dir)


# ----------------------------------------------------------------------
# CONFIG
# ----------------------------------------------------------------------

OUTPUT_DIR = Path(os.getenv('AUDIT_OUTPUT_DIR', './audits/')).expanduser().resolve()
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# In-memory job tracker (sufficient for single-instance v1).
# For multi-instance scale, swap for Redis or DB.
JOBS: Dict[str, Dict] = {}
JOBS_LOCK = threading.Lock()


# ----------------------------------------------------------------------
# REQUEST / RESPONSE MODELS
# ----------------------------------------------------------------------

class AuditRequest(BaseModel):
    url: HttpUrl


class AuditResponse(BaseModel):
    audit_id: str
    status: str  # 'queued' | 'running' | 'completed' | 'error'
    message: str
    poll_url: str


class AuditStatusResponse(BaseModel):
    audit_id: str
    status: str
    started_at: Optional[str] = None
    completed_at: Optional[str] = None
    duration_seconds: Optional[float] = None
    error: Optional[str] = None
    result_summary: Optional[dict] = None
    artifacts: Optional[dict] = None
    # Live progress (populated while status == 'running'):
    # {phase, tool, turn, tool_count, elapsed_seconds, last_tool_ms}
    progress: Optional[dict] = None
    # Agent diagnostic fields — populated when status == 'error' and the
    # failure originated in the agent loop (vs an exception at orchestration).
    agent_errors: Optional[list] = None
    raw_final_text_preview: Optional[str] = None
    agent_turns: Optional[int] = None
    tool_call_count: Optional[int] = None
    input_tokens: Optional[int] = None
    output_tokens: Optional[int] = None


# ----------------------------------------------------------------------
# FASTAPI APP
# ----------------------------------------------------------------------

app = FastAPI(
    title='AEO/SEO/GEO Auditor',
    description='Standalone deterministic website audit service. '
                'Powered by 12,764-entry Sieve brain + Anthropic Sonnet 4.6.',
    version='4.0',
)


# ----------------------------------------------------------------------
# AUTH — HTTP Basic, credentials from env vars (never in code)
# ----------------------------------------------------------------------
# Set in Railway: AUDIT_USERNAME and AUDIT_PASSWORD env vars.
# If either is unset, AUTH IS DISABLED (service is fully public).
# Always set both in production.

AUDIT_USERNAME = os.getenv('AUDIT_USERNAME', '')
AUDIT_PASSWORD = os.getenv('AUDIT_PASSWORD', '')
AUTH_ENABLED = bool(AUDIT_USERNAME and AUDIT_PASSWORD)

if not AUTH_ENABLED:
    log.warning('AUTH DISABLED — AUDIT_USERNAME / AUDIT_PASSWORD env vars not set. '
                'Service is publicly accessible. Set both in Railway to enable auth.')
else:
    log.info('AUTH enabled for user=%s', AUDIT_USERNAME)

_basic = HTTPBasic(auto_error=False)


def require_auth(credentials: Optional[HTTPBasicCredentials] = Depends(_basic)):
    """Verify HTTP Basic credentials against env-var-defined username/password.

    If AUTH_ENABLED is False (env vars unset), allows all requests.
    Uses constant-time comparison to prevent timing attacks.
    Raises 401 with WWW-Authenticate header so browsers auto-prompt.
    """
    if not AUTH_ENABLED:
        return True

    if credentials is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Authentication required',
            headers={'WWW-Authenticate': 'Basic realm="AEO Auditor"'},
        )

    user_ok = secrets.compare_digest(credentials.username, AUDIT_USERNAME)
    pass_ok = secrets.compare_digest(credentials.password, AUDIT_PASSWORD)
    if not (user_ok and pass_ok):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Invalid credentials',
            headers={'WWW-Authenticate': 'Basic realm="AEO Auditor"'},
        )
    return True


@app.middleware('http')
async def request_logging_middleware(request, call_next):
    """Log slow or non-2xx HTTP responses. Skips the normal 2xx/<1s noise
    that uvicorn already prints, but always surfaces server errors and
    audit-related calls (which can be slow)."""
    t0 = time.time()
    try:
        response = await call_next(request)
    except Exception as e:
        elapsed_ms = int((time.time() - t0) * 1000)
        log.exception('request crashed: %s %s in %dms: %s',
                      request.method, request.url.path, elapsed_ms, e)
        raise
    elapsed_ms = int((time.time() - t0) * 1000)
    code = response.status_code
    is_audit_path = request.url.path.startswith('/audit')
    # Log conditions: server error, slow (>2s), or audit-related anomaly (>=400)
    if code >= 500:
        log.error('%s %s → %d in %dms', request.method, request.url.path, code, elapsed_ms)
    elif code >= 400 and is_audit_path:
        log.warning('%s %s → %d in %dms', request.method, request.url.path, code, elapsed_ms)
    elif elapsed_ms > 2000:
        log.info('SLOW %s %s → %d in %dms', request.method, request.url.path, code, elapsed_ms)
    return response


INDEX_HTML = r"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>AEO / SEO / GEO Auditor</title>
<style>
  :root {
    --bg:#0a0c0f; --bg-2:#0f1216; --panel:#14181d; --panel-2:#191e25;
    --border:#262c33; --border-2:#2f3640;
    --fg:#e7ecf2; --fg-2:#c5cdd9; --muted:#8a95a3; --muted-2:#5a6573;
    --accent:#6ea8ff; --accent-2:#3d6fd9;
    --good:#3ecf8e; --good-bg:#0f3a2a;
    --warn:#f5b14b; --warn-bg:#3a2c10;
    --bad:#ef6464; --bad-bg:#3a1414;
    --crit:#ff4d4d; --crit-bg:#3d0d0d;
    --code-bg:#0a0d11;
  }
  * { box-sizing:border-box; }
  html,body { margin:0; padding:0; background:var(--bg); color:var(--fg);
    font:15px/1.55 -apple-system,BlinkMacSystemFont,"Segoe UI",Inter,sans-serif;
    -webkit-font-smoothing:antialiased; }
  .wrap { max-width: 1080px; margin: 0 auto; padding: 56px 24px 80px; }
  h1 { font-size: 30px; margin: 0 0 6px; letter-spacing:-0.015em; font-weight:600; }
  h2 { font-size: 13px; margin: 0 0 14px; text-transform:uppercase;
       letter-spacing:0.08em; color:var(--muted); font-weight:600; }
  h3 { font-size: 17px; margin: 0; font-weight:600; letter-spacing:-0.005em; }
  h4 { font-size: 11px; margin: 0 0 6px; text-transform:uppercase;
       letter-spacing:0.08em; color:var(--muted-2); font-weight:600; }
  p { margin: 0 0 8px; }
  a { color:var(--accent); text-decoration:none; }
  a:hover { text-decoration:underline; }

  /* Header / form */
  .tagline { color: var(--muted); margin-bottom: 28px; font-size: 14px; }
  form { display:flex; gap:10px; margin-bottom:28px; }
  input[type=url] { flex:1; background:var(--panel); border:1px solid var(--border);
    color:var(--fg); padding:14px 16px; border-radius:10px; font-size:15px; outline:none;
    transition: border-color 0.15s; }
  input[type=url]:focus { border-color: var(--accent); }
  button { background:var(--accent); color:#0a0c0f; border:0; padding:14px 24px;
    border-radius:10px; font-weight:600; cursor:pointer; font-size:15px;
    transition: background 0.15s; }
  button:hover:not(:disabled) { background:#7fb3ff; }
  button:disabled { opacity:0.5; cursor:not-allowed; }

  /* Status / spinner */
  .status-card { background:var(--panel); border:1px solid var(--border);
    border-radius:12px; padding:20px; }
  .status { display:inline-flex; align-items:center; gap:8px; padding:5px 12px;
    border-radius:999px; font-size:12px; background:#1b2330; color:var(--accent);
    font-weight:500; }
  .status.error { background:var(--bad-bg); color:var(--bad); }
  .spinner { display:inline-block; width:10px; height:10px; border:2px solid var(--border);
    border-top-color:var(--accent); border-radius:50%; animation:spin 0.8s linear infinite; }
  @keyframes spin { to { transform:rotate(360deg); } }
  .err { color:var(--bad); white-space:pre-wrap; font-family:ui-monospace,Menlo,monospace;
    font-size:12px; margin-top:10px; }

  /* Section card */
  section { margin-top: 24px; }
  .card { background:var(--panel); border:1px solid var(--border); border-radius:12px;
    padding:22px 24px; }
  .card.tight { padding:16px 18px; }

  /* Hero */
  .hero { background:linear-gradient(180deg, #131820, #0f1318);
    border:1px solid var(--border); border-radius:14px; padding:24px 26px;
    display:grid; grid-template-columns: 1fr auto; gap:18px 24px; align-items:start; }
  .hero-meta-url { font-size:14px; color:var(--fg-2); font-weight:500;
    word-break:break-all; }
  .hero-meta-tags { color:var(--muted); font-size:13px; margin-top:4px; }
  .hero-score { display:flex; align-items:center; gap:14px; }
  .score-num { font-size:48px; font-weight:700; letter-spacing:-0.025em;
    line-height:1; font-variant-numeric:tabular-nums; }
  .grade { font-size:24px; font-weight:700; padding:6px 16px; border-radius:10px;
    background:#222; line-height:1; }
  .grade.A { background:var(--good-bg); color:var(--good); }
  .grade.B { background:var(--good-bg); color:var(--good); }
  .grade.C { background:var(--warn-bg); color:var(--warn); }
  .grade.D, .grade.F { background:var(--bad-bg); color:var(--bad); }
  .hero-diag { grid-column: 1 / -1; color:var(--fg-2); font-size:15.5px;
    line-height:1.6; padding-top:16px; border-top:1px solid var(--border); }

  /* Top fixes — the marquee section */
  .fixes h2 { font-size:14px; color:var(--fg); }
  .fix { background:var(--panel); border:1px solid var(--border); border-radius:12px;
    padding:20px 22px; margin-bottom:14px; }
  .fix-header { display:flex; flex-wrap:wrap; gap:10px; align-items:center;
    margin-bottom:14px; }
  .fix-rank { font-size:13px; font-weight:700; color:var(--muted-2);
    background:var(--bg-2); padding:3px 9px; border-radius:6px;
    font-variant-numeric:tabular-nums; }
  .fix-title { flex:1; font-size:17px; font-weight:600; min-width:200px; }
  .fix-body { display:grid; grid-template-columns: 1fr; gap:12px; }
  @media (min-width: 720px) {
    .fix-body { grid-template-columns: 1fr 1fr; }
    .fix-body .why { grid-column: 1 / -1; }
  }
  .fix-block { background:var(--bg-2); border:1px solid var(--border);
    border-radius:8px; padding:12px 14px; }
  .fix-block.why { background:transparent; border-color:transparent; padding:6px 0; }
  .fix-block p, .fix-block pre { margin:0; font-size:14px; line-height:1.55;
    color:var(--fg-2); }
  pre { white-space:pre-wrap; word-break:break-word; font-family:ui-monospace,Menlo,monospace;
    font-size:12.5px; background:var(--code-bg); border:1px solid var(--border);
    padding:10px 12px; border-radius:6px; margin:6px 0; overflow-x:auto; }
  code { font-family:ui-monospace,Menlo,monospace; font-size:12.5px;
    background:var(--code-bg); padding:1px 5px; border-radius:4px; }

  /* Badges */
  .badge { display:inline-flex; align-items:center; font-size:11px; font-weight:600;
    text-transform:uppercase; letter-spacing:0.04em; padding:3px 9px;
    border-radius:5px; background:var(--bg-2); color:var(--fg-2);
    border:1px solid var(--border); }
  .badge.impact-critical { background:var(--crit-bg); color:var(--crit); border-color:#5a1a1a; }
  .badge.impact-high { background:var(--bad-bg); color:var(--bad); border-color:#5a1f1f; }
  .badge.impact-medium { background:var(--warn-bg); color:var(--warn); border-color:#5a3f15; }
  .badge.impact-low { background:var(--bg-2); color:var(--muted); }
  .badge.effort-trivial, .badge.effort-easy { background:var(--good-bg); color:var(--good); border-color:#1a4f3a; }
  .badge.effort-moderate { background:var(--warn-bg); color:var(--warn); border-color:#5a3f15; }
  .badge.effort-heavy { background:var(--bad-bg); color:var(--bad); border-color:#5a1f1f; }
  .badge.truth { background:#1a2335; color:var(--accent); border-color:#2a3a55; }
  .badge.type { background:var(--bg-2); color:var(--muted); }

  /* Why not cited cards */
  .wnc-grid { display:grid; gap:14px; }
  @media (min-width:720px) { .wnc-grid { grid-template-columns: repeat(3, 1fr); } }
  .wnc { background:var(--panel); border:1px solid var(--border); border-radius:12px;
    padding:18px 20px; }
  .wnc h3 { font-size:15px; margin:8px 0 10px; }
  .wnc p { color:var(--fg-2); font-size:14px; line-height:1.55; }

  /* Score breakdown */
  .scorebars { display:grid; gap:8px; }
  .sb-row { display:grid; grid-template-columns: 180px 1fr 50px; gap:12px;
    align-items:center; }
  .sb-label { font-size:13px; color:var(--fg-2); }
  .sb-bar { background:var(--bg-2); height:8px; border-radius:999px; overflow:hidden;
    border:1px solid var(--border); }
  .sb-fill { height:100%; background:var(--accent); border-radius:999px;
    transition: width 0.4s; }
  .sb-fill.bad { background:var(--bad); }
  .sb-fill.warn { background:var(--warn); }
  .sb-fill.good { background:var(--good); }
  .sb-val { font-size:13px; text-align:right; font-variant-numeric:tabular-nums;
    color:var(--fg-2); }
  .sb-val.na { color:var(--muted-2); }

  /* Two-column diagnostic (bots eye + perf) */
  .twocol { display:grid; gap:14px; }
  @media (min-width:720px) { .twocol { grid-template-columns: 1fr 1fr; } }
  .stat-table { width:100%; border-collapse:collapse; font-size:13px; }
  .stat-table td { padding:7px 0; border-bottom:1px solid var(--border); vertical-align:top; }
  .stat-table tr:last-child td { border-bottom:0; }
  .stat-table td:first-child { color:var(--muted); width:50%; }
  .stat-table td:last-child { color:var(--fg-2); text-align:right;
    font-variant-numeric:tabular-nums; word-break:break-word; }

  /* Competitor table */
  .comp-table { width:100%; border-collapse:collapse; font-size:13px; }
  .comp-table th, .comp-table td { padding:9px 10px; border-bottom:1px solid var(--border);
    text-align:left; vertical-align:top; }
  .comp-table th { color:var(--muted); font-weight:600; font-size:11px;
    text-transform:uppercase; letter-spacing:0.04em; background:var(--bg-2); }
  .comp-table tr.target td { background:#162030; }
  .comp-table td { font-variant-numeric:tabular-nums; }
  .comp-table td:first-child { font-weight:500; color:var(--fg); }

  /* Findings table (Layer 2) */
  details { background:var(--panel); border:1px solid var(--border);
    border-radius:12px; padding:14px 18px; }
  details > summary { cursor:pointer; user-select:none; color:var(--fg-2);
    font-size:14px; font-weight:500; padding:4px 0; }
  details[open] > summary { margin-bottom:12px; }
  .findings-table { width:100%; border-collapse:collapse; font-size:13px; }
  .findings-table th, .findings-table td { padding:8px 10px;
    border-bottom:1px solid var(--border); text-align:left; vertical-align:top; }
  .findings-table th { color:var(--muted); font-weight:600; font-size:11px;
    text-transform:uppercase; letter-spacing:0.04em; }
  .status-icon { display:inline-block; width:18px; text-align:center; font-weight:700; }
  .status-icon.fail { color:var(--bad); }
  .status-icon.warn { color:var(--warn); }
  .status-icon.pass { color:var(--good); }
  .check-id { font-family:ui-monospace,Menlo,monospace; font-size:12px;
    color:var(--muted); }

  /* Quick wins */
  .qw-list { padding-left:0; list-style:none; }
  .qw-list li { padding:8px 0; padding-left:24px; position:relative;
    border-bottom:1px solid var(--border); color:var(--fg-2); font-size:14px; }
  .qw-list li:last-child { border-bottom:0; }
  .qw-list li:before { content:'✓'; position:absolute; left:0; color:var(--good);
    font-weight:700; }

  /* Citations / brain */
  .tier { margin-bottom:16px; }
  .tier h3 { font-size:13px; color:var(--muted); margin-bottom:8px;
    text-transform:uppercase; letter-spacing:0.05em; font-weight:600; }
  .citation { font-size:13px; color:var(--fg-2); padding:5px 0;
    border-bottom:1px solid var(--border); }
  .citation:last-child { border-bottom:0; }
  .citation .src { color:var(--accent); font-weight:500; }
  .citation .nm { color:var(--fg-2); }

  /* Downloads */
  .links { display:flex; gap:10px; flex-wrap:wrap; }
  .links a { background:var(--bg-2); border:1px solid var(--border); color:var(--fg);
    padding:10px 16px; border-radius:8px; font-size:13px; font-weight:500;
    transition: border-color 0.15s, color 0.15s; }
  .links a:hover { border-color: var(--accent); color:var(--accent);
    text-decoration:none; }

  /* Footer */
  footer { color:var(--muted); font-size:12px; margin-top:48px;
    text-align:center; padding-top:20px; border-top:1px solid var(--border); }
  footer a { color:var(--muted); }

  /* Misc */
  .err-block { background:var(--bad-bg); border:1px solid #5a1f1f;
    border-radius:8px; padding:12px 14px; }
</style>
</head>
<body>
<div class="wrap">
  <h1>AEO / SEO / GEO Auditor</h1>
  <div class="tagline">Full 97-check audit · Sieve brain (12,764 entries) · Claude Sonnet 4.6</div>

  <form id="f">
    <input id="url" type="url" placeholder="https://example.com" required autofocus>
    <button id="go" type="submit">Run audit</button>
  </form>

  <div id="out"></div>

  <footer>
    JSON API: <a href="/api">/api</a> · Health: <a href="/healthz">/healthz</a> · Docs: <a href="/docs">/docs</a>
  </footer>
</div>

<script>
const $ = (id) => document.getElementById(id);
const out = $('out');

$('f').addEventListener('submit', async (e) => {
  e.preventDefault();
  const url = $('url').value.trim();
  if (!url) return;
  $('go').disabled = true;
  out.innerHTML = '<div class="status-card"><span class="status"><span class="spinner"></span>Submitting…</span></div>';

  try {
    const r = await fetch('/audit', {
      method: 'POST',
      headers: {'Content-Type':'application/json'},
      body: JSON.stringify({url})
    });
    if (!r.ok) throw new Error('Submit failed: ' + r.status + ' ' + (await r.text()));
    const {audit_id} = await r.json();
    await poll(audit_id);
  } catch (err) {
    out.innerHTML = renderError(err.message);
  } finally {
    $('go').disabled = false;
  }
});

async function poll(id) {
  const started = Date.now();
  let consecutive404 = 0;
  while (true) {
    const r = await fetch('/audit/' + id);
    const elapsed = Math.round((Date.now() - started) / 1000);

    // 404 = audit not in server's JOBS dict. Either it was never created,
    // or the server restarted (Railway redeploy) and the in-memory state
    // was wiped. Tolerate 2 consecutive 404s in case of a race; bail on 3rd.
    if (r.status === 404) {
      consecutive404 += 1;
      if (consecutive404 >= 3) {
        out.innerHTML = renderError(
          'Audit ' + id.slice(0,8) + '… not found on the server.\n\n' +
          'Most likely cause: the service redeployed mid-audit (Railway in-memory ' +
          'job state is wiped on every container restart). Please resubmit the URL.'
        );
        return;
      }
      await new Promise(r => setTimeout(r, 3000));
      continue;
    }
    consecutive404 = 0;

    if (!r.ok) {
      const body = await r.text().catch(() => '');
      out.innerHTML = renderError('Status check failed: HTTP ' + r.status +
        (body ? '\n\n' + body.slice(0, 500) : ''));
      return;
    }

    const data = await r.json();

    if (data.status === 'completed') {
      // Fetch full audit JSON for rich render
      try {
        const rJson = await fetch('/audit/' + id + '/json');
        if (rJson.ok) {
          const fullAudit = await rJson.json();
          renderFull(fullAudit, data, id);
          return;
        }
      } catch(e) { /* fall through to summary render */ }
      renderSummary(data, id);
      return;
    }
    if (data.status === 'error') {
      let msg = data.error || 'unknown error';
      if (data.agent_errors && data.agent_errors.length) {
        msg += '\n\nAgent errors:\n  - ' + data.agent_errors.join('\n  - ');
      }
      if (data.raw_final_text_preview) {
        msg += '\n\nLast assistant text (preview):\n' + data.raw_final_text_preview.slice(0, 800);
      }
      const stats = [];
      if (data.agent_turns != null) stats.push(data.agent_turns + ' turns');
      if (data.tool_call_count != null) stats.push(data.tool_call_count + ' tool calls');
      if (data.input_tokens != null) stats.push((data.input_tokens + (data.output_tokens||0)) + ' tokens');
      if (stats.length) msg += '\n\nAgent stats: ' + stats.join(' · ');
      out.innerHTML = renderError(msg);
      return;
    }

    const prog = data.progress || {};
    const phaseLine = prog.phase || (data.status === 'queued' ? 'Queued' : 'Starting up...');
    const statsLine = [];
    if (prog.turn) statsLine.push('turn ' + prog.turn);
    if (prog.tool_count) statsLine.push(prog.tool_count + ' tool calls');
    if (prog.last_tool_ms) statsLine.push('last ' + prog.last_tool_ms + 'ms');
    const statsStr = statsLine.length ? ' · ' + statsLine.join(' · ') : '';

    out.innerHTML =
      '<div class="status-card">' +
        '<span class="status"><span class="spinner"></span>' +
          escapeHtml(phaseLine) + ' · ' + elapsed + 's' +
        '</span>' +
        (statsStr ? '<div style="color:var(--muted-2);font-size:12px;margin-top:6px;font-variant-numeric:tabular-nums">' + escapeHtml(statsStr.slice(3)) + '</div>' : '') +
        '<div style="color:var(--muted);font-size:13px;margin-top:12px;line-height:1.55">' +
          'Typical completion: 90–300 seconds depending on site complexity. The agent is running 95+ checks across Technical, Performance, On-Page, Schema, AEO Discovery/Extraction/Trust/Selection, GEO, and Entity Consistency — including a 5-competitor crawl and Sieve brain citation enrichment.' +
        '</div>' +
      '</div>';
    await new Promise(r => setTimeout(r, 3000));
  }
}

function renderError(msg) {
  return '<div class="status-card"><span class="status error">Error</span>' +
    '<div class="err">' + escapeHtml(msg) + '</div></div>';
}

function renderSummary(data, id) {
  // Fallback render when full JSON unavailable
  const s = data.result_summary || {};
  out.innerHTML = renderHero(s, data.duration_seconds, s.findings_count || 0) +
    renderDownloads(id, data.artifacts || {});
}

function renderFull(audit, status, id) {
  const cls = audit.classification || {};
  const sc = audit.scoring || {};
  const narr = audit.narrative || {};
  const findings = audit.findings || [];
  const competitors = audit.competitor_comparison || [];
  const bev = audit.bots_eye_view || (audit.scripts_output && audit.scripts_output.bots_eye_view) || {};
  const perf = audit.performance || {};

  const heroData = {
    url: audit.url,
    page_type: cls.page_type,
    industry: cls.industry,
    company_name: cls.company_name,
    overall_score: sc.overall_score ?? sc.page_citation_readiness,
    overall_grade: sc.overall_grade,
    executive_diagnosis: narr.executive_diagnosis,
  };

  const html = [
    renderHero(heroData, audit.duration_seconds, findings.length),
    renderTopFixes(narr.top_5_fixes || []),
    renderWhyNotCited(narr.why_not_cited || [], (narr.top_5_fixes || []).length ? null : (findings.find(f => f.citations && f.citations.length))),
    renderScoreBreakdown(sc),
    renderTwoCol(bev, perf, audit),
    renderCompetitors(competitors, audit.domain),
    renderQuickWins(narr.quick_wins || []),
    renderSummary_text(narr.summary_what_to_do),
    renderAllFindings(findings),
    renderBrainSources(findings),
    renderDownloads(id, status.artifacts || {}),
  ];
  out.innerHTML = html.filter(Boolean).join('');
}

function renderHero(s, duration, findingsCount) {
  const grade = (s.overall_grade || '').charAt(0).toUpperCase();
  const meta = [s.page_type, s.industry, s.company_name].filter(Boolean).join(' · ');
  return (
    '<div class="hero">' +
      '<div>' +
        '<div class="hero-meta-url">' + escapeHtml(s.url || '') + '</div>' +
        '<div class="hero-meta-tags">' + escapeHtml(meta || '—') +
          ' · ' + (duration || '?') + 's · ' + findingsCount + ' findings' +
        '</div>' +
      '</div>' +
      '<div class="hero-score">' +
        '<div class="score-num">' + (s.overall_score ?? '—') + '</div>' +
        '<div class="grade ' + escapeHtml(grade) + '">' + escapeHtml(s.overall_grade || '—') + '</div>' +
      '</div>' +
      (s.executive_diagnosis ? '<div class="hero-diag">' + escapeHtml(s.executive_diagnosis) + '</div>' : '') +
    '</div>'
  );
}

function renderTopFixes(fixes) {
  if (!fixes || !fixes.length) return '';
  let html = '<section class="fixes"><h2>Top fixes that matter</h2>';
  for (const f of fixes) {
    const impact = String(f.impact || '').toLowerCase();
    const effort = String(f.effort || '').toLowerCase();
    html +=
      '<div class="fix">' +
        '<div class="fix-header">' +
          '<span class="fix-rank">#' + (f.rank || '?') + '</span>' +
          '<span class="fix-title">' + escapeHtml(f.title || '') + '</span>' +
          (f.impact ? '<span class="badge impact-' + escapeHtml(impact) + '">' + escapeHtml(f.impact) + ' impact</span>' : '') +
          (f.effort ? '<span class="badge effort-' + escapeHtml(effort) + '">' + escapeHtml(f.effort) + ' effort</span>' : '') +
          (f.type ? '<span class="badge type">' + escapeHtml(f.type) + '</span>' : '') +
          (f.truth_badge ? '<span class="badge truth">' + escapeHtml(f.truth_badge) + '</span>' : '') +
        '</div>' +
        '<div class="fix-body">' +
          (f.before ? '<div class="fix-block"><h4>Currently</h4>' + formatBlock(f.before) + '</div>' : '') +
          (f.after ? '<div class="fix-block"><h4>Recommended</h4>' + formatBlock(f.after) + '</div>' : '') +
          (f.why ? '<div class="fix-block why"><h4>Why this matters</h4><p>' + escapeHtml(f.why) + '</p></div>' : '') +
        '</div>' +
      '</div>';
  }
  html += '</section>';
  return html;
}

function renderWhyNotCited(items) {
  if (!items || !items.length) return '';
  let html = '<section><h2>Why this page isn\'t being cited</h2><div class="wnc-grid">';
  for (const it of items) {
    html +=
      '<div class="wnc">' +
        (it.badge ? '<span class="badge truth">' + escapeHtml(it.badge) + '</span>' : '') +
        '<h3>' + escapeHtml(it.title || '') + '</h3>' +
        '<p>' + escapeHtml(it.body || '') + '</p>' +
      '</div>';
  }
  html += '</div></section>';
  return html;
}

function renderScoreBreakdown(sc) {
  const sec = sc.section_scores || {};
  const order = ['A_technical','B_performance','C_onpage','D_schema',
    'E_aeo_discovery','F_aeo_extraction','G_aeo_trust','H_aeo_selection',
    'I_geo','J_entity'];
  const labels = {
    'A_technical': 'A · Technical SEO',
    'B_performance': 'B · Performance',
    'C_onpage': 'C · On-Page SEO',
    'D_schema': 'D · Schema',
    'E_aeo_discovery': 'E · AEO Discovery',
    'F_aeo_extraction': 'F · AEO Extraction',
    'G_aeo_trust': 'G · AEO Trust',
    'H_aeo_selection': 'H · AEO Selection',
    'I_geo': 'I · GEO',
    'J_entity': 'J · Entity Consistency',
  };
  let rows = '';
  for (const k of order) {
    if (!(k in sec)) continue;
    const v = sec[k];
    if (v === null || v === undefined) {
      rows += '<div class="sb-row"><div class="sb-label">' + escapeHtml(labels[k] || k) +
        '</div><div class="sb-bar"></div><div class="sb-val na">N/A</div></div>';
    } else {
      const cls = v >= 75 ? 'good' : v >= 50 ? 'warn' : 'bad';
      rows += '<div class="sb-row">' +
        '<div class="sb-label">' + escapeHtml(labels[k] || k) + '</div>' +
        '<div class="sb-bar"><div class="sb-fill ' + cls + '" style="width:' + v + '%"></div></div>' +
        '<div class="sb-val">' + v + '</div>' +
      '</div>';
    }
  }
  let extras = '';
  if (sc.brand_ai_presence != null) {
    extras += '<div style="margin-top:14px;padding-top:14px;border-top:1px solid var(--border);font-size:13px;color:var(--muted)">' +
      'Brand AI Presence (BAP): <strong style="color:var(--fg)">' + sc.brand_ai_presence + '</strong>' +
      (sc.seo_score != null ? ' · SEO: <strong style="color:var(--fg)">' + sc.seo_score + '</strong>' : '') +
      (sc.aeo_score != null ? ' · AEO: <strong style="color:var(--fg)">' + sc.aeo_score + '</strong>' : '') +
      (sc.citation_readiness != null ? ' · Citation readiness: <strong style="color:var(--fg)">' + sc.citation_readiness + '</strong>' : '') +
      '</div>';
  }
  return '<section><h2>Score breakdown</h2><div class="card"><div class="scorebars">' +
    rows + '</div>' + extras + '</div></section>';
}

function renderTwoCol(bev, perf, audit) {
  const cvb = bev.content_visible_to_bots || {};
  const pid = bev.page_identity || {};
  const summary = bev.summary || {};

  // Handle multiple possible field-name conventions across agent vs script outputs
  const faqVisible = cvb.faq_visible_pairs ?? cvb.faq_visible ?? summary.faq_visible ?? bev.faq_visible_pairs;
  const faqSchema = cvb.faq_schema_pairs ?? cvb.faq_schema ?? summary.faq_schema ?? bev.faq_schema_pairs;
  const faqStr = (faqVisible !== undefined && faqSchema !== undefined)
    ? faqVisible + ' / ' + faqSchema
    : null;
  const wordCount = cvb.visible_word_count ?? summary.visible_words_default ?? cvb.visible_words ?? bev.visible_word_count;

  const bevRows = [
    ['Visible word count', wordCount],
    ['Schema blocks', cvb.schema_block_count ?? summary.schema_blocks ?? bev.schema_block_count],
    ['FAQ visible / in schema', faqStr],
    ['Title', pid.title || bev.title],
    ['H1', pid.h1_first || bev.h1_first],
    ['Canonical', pid.canonical_tag || bev.canonical || 'none'],
    ['Meta robots', pid.meta_robots || bev.meta_robots || 'none'],
    ['Classification', bev.classification],
  ];
  const perfRows = [
    ['TTFB', perf.ttfb_ms != null ? perf.ttfb_ms + ' ms' : null],
    ['LCP', perf.lcp_ms != null ? perf.lcp_ms + ' ms' : null],
    ['CLS', perf.cls != null ? perf.cls.toFixed ? perf.cls.toFixed(3) : perf.cls : null],
    ['Load time', perf.load_time_ms != null ? perf.load_time_ms + ' ms' : null],
    ['Request count', perf.request_count],
    ['SPA framework', (perf.spa_signals || []).join(', ') || 'none detected'],
    ['Console errors', perf.console_errors ? perf.console_errors.length : null],
  ];

  function tableRows(rows) {
    return rows.filter(r => r[1] !== null && r[1] !== undefined && r[1] !== '')
      .map(r => '<tr><td>' + escapeHtml(r[0]) + '</td><td>' + escapeHtml(String(r[1])) + '</td></tr>')
      .join('');
  }

  const bevHtml = tableRows(bevRows);
  const perfHtml = tableRows(perfRows);

  if (!bevHtml && !perfHtml) return '';

  return '<section><h2>How crawlers see this page</h2><div class="twocol">' +
    (bevHtml ? '<div class="card"><h3 style="font-size:14px;margin-bottom:10px">Bot\'s eye view</h3><table class="stat-table"><tbody>' + bevHtml + '</tbody></table></div>' : '') +
    (perfHtml ? '<div class="card"><h3 style="font-size:14px;margin-bottom:10px">Performance</h3><table class="stat-table"><tbody>' + perfHtml + '</tbody></table></div>' : '') +
    '</div></section>';
}

function renderCompetitors(comps, ourDomain) {
  if (!comps || !comps.length) return '';
  let rows = '';
  for (const c of comps) {
    const isUs = c.domain === ourDomain;
    rows +=
      '<tr' + (isUs ? ' class="target"' : '') + '>' +
        '<td>' + escapeHtml(c.domain || '') + (isUs ? ' (you)' : '') + '</td>' +
        '<td>' + (c.word_count ?? '—') + '</td>' +
        '<td>' + (c.faq_pairs ?? '—') + '</td>' +
        '<td>' + escapeHtml(((c.schema_types || [])).join(', ') || '—') + '</td>' +
        '<td>' + escapeHtml(c.dateModified || '—') + '</td>' +
        '<td>' + escapeHtml(c.author || '—') + '</td>' +
        '<td>' + (c.outbound_links ?? '—') + '</td>' +
      '</tr>';
  }
  return '<section><h2>How you compare to competitors</h2><div class="card tight">' +
    '<table class="comp-table"><thead><tr>' +
      '<th>Domain</th><th>Words</th><th>FAQ</th><th>Schema types</th>' +
      '<th>Modified</th><th>Author</th><th>Outbound</th>' +
    '</tr></thead><tbody>' + rows + '</tbody></table></div></section>';
}

function renderQuickWins(items) {
  if (!items || !items.length) return '';
  let lis = '';
  for (const it of items) lis += '<li>' + escapeHtml(it) + '</li>';
  return '<section><h2>Quick wins (under 5 min each)</h2><div class="card"><ul class="qw-list">' +
    lis + '</ul></div></section>';
}

function renderSummary_text(s) {
  if (!s) return '';
  return '<section><h2>What to do this week</h2><div class="card" style="line-height:1.65;color:var(--fg-2)">' +
    escapeHtml(s) + '</div></section>';
}

function renderAllFindings(findings) {
  if (!findings || !findings.length) return '';
  // Group: failures first, then warnings, then passes
  const sortKey = f => (f.status === 'fail' ? 0 : f.status === 'warn' ? 1 : 2);
  const sorted = [...findings].sort((a,b) => sortKey(a) - sortKey(b));
  let rows = '';
  for (const f of sorted.slice(0, 120)) {
    const icon = f.status === 'fail' ? '✗' : f.status === 'warn' ? '⚠' : f.status === 'pass' ? '✓' : '·';
    rows +=
      '<tr>' +
        '<td><span class="status-icon ' + escapeHtml(f.status || '') + '">' + icon + '</span></td>' +
        '<td><span class="check-id">' + escapeHtml(f.check_id || '') + '</span></td>' +
        '<td>' + escapeHtml(f.severity || '—') + '</td>' +
        '<td>' + escapeHtml((f.evidence || '').slice(0, 220)) + '</td>' +
        '<td>' + (f.truth_badge ? '<span class="badge truth">' + escapeHtml(f.truth_badge) + '</span>' : '') + '</td>' +
      '</tr>';
  }
  return '<section><details><summary>All findings (' + findings.length + ' checks · click to expand)</summary>' +
    '<table class="findings-table"><thead><tr>' +
      '<th></th><th>Check</th><th>Severity</th><th>Evidence</th><th>Truth</th>' +
    '</tr></thead><tbody>' + rows + '</tbody></table></details></section>';
}

function renderBrainSources(findings) {
  // Collect unique citations grouped by tier. Skip citations that have no
  // usable content (no name AND no source_org AND no source_url) — those
  // are the agent emitting partial/reshaped objects.
  const seen = new Set();
  const byTier = {1:[], 2:[], 3:[], 4:[], 5:[]};
  for (const f of findings) {
    for (const c of (f.citations || [])) {
      const name = c.name || c.title;
      const hasContent = name || c.source_org || c.source_url;
      if (!hasContent) continue;  // skip empty/malformed
      const dedupKey = (c.id ?? name) + ':' + (c.kind || '?');
      if (seen.has(dedupKey)) continue;
      seen.add(dedupKey);
      const tier = c.tier || 5;
      (byTier[tier] = byTier[tier] || []).push(c);
    }
  }
  const totalCites = seen.size;
  if (!totalCites) return '';
  const tierLabels = {1:'🥇 Tier 1 — Authoritative', 2:'🥈 Tier 2 — Reputable',
                       3:'🥉 Tier 3 — Industry', 4:'📎 Tier 4 — Specialized', 5:'Other'};
  let html = '<section><h2>Sources cited (' + totalCites + ' from Sieve brain)</h2><div class="card">';
  for (const t of [1,2,3,4,5]) {
    if (!byTier[t] || !byTier[t].length) continue;
    html += '<div class="tier"><h3>' + tierLabels[t] + '</h3>';
    for (const c of byTier[t].slice(0, 12)) {
      const kind = c.kind === 'rule' ? 'Rule' : c.kind === 'anti_pattern' ? 'AP' : 'Item';
      const name = c.name || c.title || '(no name)';
      // Confidence/risk badges where available
      const conf = (c.confidence_score != null) ? ' (conf ' + c.confidence_score + ')' : '';
      const risk = c.risk_level ? ' [' + escapeHtml(c.risk_level) + ' risk]' : '';
      // Only show [#id] if id is actually a usable number
      const idTag = (c.id != null && c.id !== '' && !isNaN(c.id))
        ? ' <code style="font-size:11px">[Sieve ' + kind + ' #' + escapeHtml(String(c.id)) + ']</code>'
        : '';
      html += '<div class="citation">' +
        '<span class="src">' + escapeHtml(c.source_org || 'unknown') + '</span> — ' +
        (c.source_url ? '<a href="' + escapeHtml(c.source_url) + '" target="_blank" rel="noopener">' : '') +
        '<span class="nm">' + escapeHtml(name) + '</span>' +
        (c.source_url ? '</a>' : '') +
        conf + risk + idTag +
        '</div>';
    }
    html += '</div>';
  }
  html += '</div></section>';
  return html;
}

function renderDownloads(id, artifacts) {
  return '<section><h2>Download artifacts</h2><div class="card tight">' +
    '<div class="links">' +
      '<a href="' + (artifacts.json || '/audit/'+id+'/json') + '" target="_blank">Full JSON</a>' +
      '<a href="' + (artifacts.markdown || '/audit/'+id+'/md') + '" target="_blank">Markdown report</a>' +
      '<a href="' + (artifacts.pdf || '/audit/'+id+'/pdf') + '" target="_blank">PDF summary</a>' +
    '</div></div></section>';
}

function formatBlock(text) {
  // Detect code-like content (JSON, HTML, multiline indented blocks) vs prose.
  if (!text) return '';
  const t = String(text);
  const looksCode = /^(\s*[<{]|<\w|<!|```)/m.test(t.trim()) || /\n\s{2,}/.test(t);
  if (looksCode) {
    // Strip ```lang fences if present
    const stripped = t.replace(/^```\w*\n?|\n?```$/g, '').trim();
    return '<pre>' + escapeHtml(stripped) + '</pre>';
  }
  return '<p>' + escapeHtml(t).replace(/\n/g, '<br>') + '</p>';
}

function escapeHtml(s) {
  return String(s == null ? '' : s).replace(/[&<>"']/g, c =>
    ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
}
</script>
</body>
</html>
"""


@app.get('/', response_class=HTMLResponse)
def root(_: bool = Depends(require_auth)):
    return HTMLResponse(INDEX_HTML)


@app.get('/api')
def api_info(_: bool = Depends(require_auth)):
    return {
        'service': 'aeo-seo-auditor',
        'version': '4.0',
        'endpoints': {
            'POST /audit': 'Submit a URL for audit',
            'GET /audit/{id}': 'Fetch status + result',
            'GET /audit/{id}/{json,md,pdf}': 'Fetch specific artifact',
            'GET /healthz': 'Health check',
        },
        'docs': '/docs',
    }


@app.get('/healthz')
def healthz():
    """Liveness/readiness check. Verifies brain snapshots load."""
    try:
        sys.path.insert(0, str(THIS_DIR.parent / 'auditor-ruleset-export'))
        from ranker import BrainIndex
        brain = BrainIndex.from_export_dir(
            str(THIS_DIR.parent / 'auditor-ruleset-export')
        )
        stats = brain.stats()
        api_key_set = bool(os.getenv('ANTHROPIC_API_KEY'))
        return {
            'status': 'ok',
            'brain_loaded': True,
            'brain_stats': stats,
            'anthropic_key_set': api_key_set,
            'audit_mode': AUDIT_MODE,
            'agent_available': AGENT_AVAILABLE,
            'agent_import_error': None if AGENT_AVAILABLE else _AGENT_IMPORT_ERROR,
            'web_tools': 'anthropic_native_server_tools',
            'auth_enabled': AUTH_ENABLED,
            'output_dir': str(OUTPUT_DIR),
        }
    except Exception as e:
        return JSONResponse(
            status_code=503,
            content={
                'status': 'degraded',
                'error': f'{type(e).__name__}: {e}',
            },
        )


@app.post('/audit', response_model=AuditResponse)
async def submit_audit(req: AuditRequest, background_tasks: BackgroundTasks,
                        _: bool = Depends(require_auth)):
    """Submit a URL for audit. Returns audit_id immediately; audit runs async.

    Poll GET /audit/{id} for status. Typical completion: 60-120 seconds.
    """
    audit_id = str(uuid.uuid4())
    url_str = str(req.url)
    log.info('[%s] submitted url=%s mode=%s', audit_id[:8], url_str, AUDIT_MODE)

    with JOBS_LOCK:
        JOBS[audit_id] = {
            'audit_id': audit_id,
            'status': 'queued',
            'url': url_str,
            'started_at': None,
            'completed_at': None,
            'result': None,
            'error': None,
        }

    background_tasks.add_task(_run_audit_background, audit_id, url_str)

    return AuditResponse(
        audit_id=audit_id,
        status='queued',
        message='Audit queued. Poll the audit endpoint for status.',
        poll_url=f'/audit/{audit_id}',
    )


def _run_audit_background(audit_id: str, url: str):
    """Background runner — invoked via FastAPI background_tasks."""
    sid = audit_id[:8]
    started = time.time()
    log.info('[%s] mode=%s dispatching url=%s', sid, AUDIT_MODE, url)

    with JOBS_LOCK:
        JOBS[audit_id]['status'] = 'running'
        JOBS[audit_id]['started_at'] = datetime.now(timezone.utc).isoformat()

    def _update_progress(info: Dict):
        """Bound to this audit_id. Receives {phase, tool, turn, tool_count,
        elapsed_seconds, last_tool_ms} from the agent loop after each tool
        call. Writes into JOBS so the /audit/{id} endpoint can surface it."""
        with JOBS_LOCK:
            if audit_id in JOBS:
                JOBS[audit_id]['progress'] = info

    try:
        result = run_audit(url, output_dir=str(OUTPUT_DIR),
                            progress_callback=_update_progress)
        elapsed = round(time.time() - started, 1)

        # Agent path returns an error envelope (no exception) when it can't
        # produce a valid audit JSON. Detect that and mark as error so the
        # homepage doesn't think the audit succeeded.
        if isinstance(result, dict) and result.get('error'):
            log.error('[%s] failed in %ss: %s', sid, elapsed, result['error'])
            for ae in (result.get('agent_errors') or [])[:5]:
                log.error('[%s]   agent_error: %s', sid, ae)
            preview = (result.get('raw_final_text_preview') or '')[:300]
            if preview:
                log.error('[%s]   last_text_preview: %s', sid, preview.replace('\n', ' \\n '))
            with JOBS_LOCK:
                JOBS[audit_id]['status'] = 'error'
                JOBS[audit_id]['error'] = result['error']
                JOBS[audit_id]['agent_errors'] = result.get('agent_errors', [])
                JOBS[audit_id]['raw_final_text_preview'] = result.get('raw_final_text_preview', '')
                JOBS[audit_id]['agent_turns'] = result.get('agent_turns')
                JOBS[audit_id]['tool_call_count'] = result.get('tool_call_count')
                JOBS[audit_id]['input_tokens'] = result.get('input_tokens')
                JOBS[audit_id]['output_tokens'] = result.get('output_tokens')
                JOBS[audit_id]['completed_at'] = datetime.now(timezone.utc).isoformat()
            return

        score = (result.get('scoring') or {}).get('overall_score') if isinstance(result, dict) else None
        grade = (result.get('scoring') or {}).get('overall_grade') if isinstance(result, dict) else None
        log.info('[%s] completed in %ss score=%s grade=%s', sid, elapsed, score, grade)
        with JOBS_LOCK:
            JOBS[audit_id]['status'] = 'completed'
            JOBS[audit_id]['completed_at'] = datetime.now(timezone.utc).isoformat()
            JOBS[audit_id]['result'] = result
    except Exception as e:
        elapsed = round(time.time() - started, 1)
        # Full traceback to stdout — Railway captures it in the log viewer.
        log.error('[%s] background task crashed in %ss: %s: %s',
                  sid, elapsed, type(e).__name__, e)
        log.error('[%s] traceback:\n%s', sid, traceback.format_exc())
        with JOBS_LOCK:
            JOBS[audit_id]['status'] = 'error'
            JOBS[audit_id]['error'] = f'{type(e).__name__}: {e}'
            JOBS[audit_id]['traceback'] = traceback.format_exc()
            JOBS[audit_id]['completed_at'] = datetime.now(timezone.utc).isoformat()


@app.get('/audit/{audit_id}', response_model=AuditStatusResponse)
def get_audit(audit_id: str, _: bool = Depends(require_auth)):
    """Fetch audit status + summary. Poll until status == 'completed'."""
    with JOBS_LOCK:
        job = JOBS.get(audit_id)
    if not job:
        raise HTTPException(status_code=404, detail='audit not found')

    response = {
        'audit_id': audit_id,
        'status': job['status'],
        'started_at': job.get('started_at'),
        'completed_at': job.get('completed_at'),
    }

    # Live progress info (only meaningful while status == 'running')
    if job.get('progress'):
        response['progress'] = job['progress']

    if job['status'] == 'error':
        response['error'] = job.get('error')
        # Surface agent diagnostic fields if present (set by _run_audit_background
        # when the agent returned an error envelope). These are critical for
        # debugging why the agent failed to produce valid output.
        for k in ('agent_errors', 'raw_final_text_preview', 'agent_turns',
                  'tool_call_count', 'input_tokens', 'output_tokens'):
            if k in job:
                response[k] = job[k]
        return response

    if job['status'] == 'completed' and job.get('result'):
        result = job['result']
        response['duration_seconds'] = result.get('duration_seconds')

        # Compact summary — full data via .json artifact
        response['result_summary'] = {
            'url': result.get('url'),
            'domain': result.get('domain'),
            'page_type': result.get('classification', {}).get('page_type'),
            'industry': result.get('classification', {}).get('industry'),
            'overall_score': result.get('scoring', {}).get('overall_score'),
            'overall_grade': result.get('scoring', {}).get('overall_grade'),
            'section_scores': result.get('scoring', {}).get('section_scores'),
            'findings_count': len(result.get('findings', [])),
            'executive_diagnosis': result.get('narrative', {}).get('executive_diagnosis'),
        }

        response['artifacts'] = {
            'json': f'/audit/{audit_id}/json',
            'markdown': f'/audit/{audit_id}/md',
            'pdf': f'/audit/{audit_id}/pdf',
        }

    return response


# Artifact endpoints use /audit/{id}/{format} (slash separator) to avoid
# greedy-matching with the bare /audit/{id} route.
@app.get('/audit/{audit_id}/json')
def get_audit_json(audit_id: str, _: bool = Depends(require_auth)):
    """Full audit JSON."""
    with JOBS_LOCK:
        job = JOBS.get(audit_id)
    if not job or job['status'] != 'completed':
        raise HTTPException(status_code=404, detail='audit not ready or not found')
    json_path = job['result'].get('json_path')
    if not json_path or not Path(json_path).exists():
        raise HTTPException(status_code=404, detail='json artifact not found')
    return FileResponse(json_path, media_type='application/json',
                         filename=f'{audit_id}.json')


@app.get('/audit/{audit_id}/md')
def get_audit_markdown(audit_id: str, _: bool = Depends(require_auth)):
    """Markdown audit report."""
    with JOBS_LOCK:
        job = JOBS.get(audit_id)
    if not job or job['status'] != 'completed':
        raise HTTPException(status_code=404, detail='audit not ready')
    md_path = job['result'].get('md_path')
    if not md_path or not Path(md_path).exists():
        raise HTTPException(status_code=404, detail='markdown artifact not found')
    return FileResponse(md_path, media_type='text/markdown',
                         filename=f'{audit_id}.md')


@app.get('/audit/{audit_id}/pdf')
def get_audit_pdf(audit_id: str, _: bool = Depends(require_auth)):
    """1-page PDF summary."""
    with JOBS_LOCK:
        job = JOBS.get(audit_id)
    if not job or job['status'] != 'completed':
        raise HTTPException(status_code=404, detail='audit not ready')
    pdf_path = job['result'].get('pdf_path')
    if not pdf_path or not Path(pdf_path).exists():
        raise HTTPException(
            status_code=404,
            detail='PDF not available (Chrome may not be installed on this host)'
        )
    return FileResponse(pdf_path, media_type='application/pdf',
                         filename=f'{audit_id}.pdf')


@app.get('/audits')
def list_audits(_: bool = Depends(require_auth)):
    """List all audits in this service instance (in-memory only, lost on restart)."""
    with JOBS_LOCK:
        return {
            'count': len(JOBS),
            'audits': [
                {
                    'audit_id': a['audit_id'],
                    'url': a['url'],
                    'status': a['status'],
                    'started_at': a.get('started_at'),
                    'completed_at': a.get('completed_at'),
                }
                for a in JOBS.values()
            ],
        }


if __name__ == '__main__':
    import uvicorn
    port = int(os.getenv('PORT', 8000))
    uvicorn.run(app, host='0.0.0.0', port=port)
