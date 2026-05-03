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

import os
import sys
import threading
import uuid
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, Optional

# Load .env if present (graceful fallback if python-dotenv not installed)
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

THIS_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(THIS_DIR))

from fastapi import FastAPI, HTTPException, BackgroundTasks
from fastapi.responses import FileResponse, JSONResponse, PlainTextResponse, HTMLResponse
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


def run_audit(url: str, output_dir: str):
    """Dispatch to the chosen audit pipeline.

    Modes:
        - 'agent'         : full 15-phase parity loop (matches chat skill)
        - 'deterministic' : legacy fast path (scripts + 1 Sonnet call)
        - 'auto'          : agent if available, else deterministic
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
        return run_audit_agent(url, output_dir=output_dir, verbose=False)
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


# ----------------------------------------------------------------------
# FASTAPI APP
# ----------------------------------------------------------------------

app = FastAPI(
    title='AEO/SEO/GEO Auditor',
    description='Standalone deterministic website audit service. '
                'Powered by 12,764-entry Sieve brain + Anthropic Sonnet 4.6.',
    version='4.0',
)


INDEX_HTML = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>AEO/SEO/GEO Auditor</title>
<style>
  :root { --bg:#0b0d10; --panel:#14181d; --border:#262c33; --fg:#e7ecf2; --muted:#8a95a3; --accent:#6ea8ff; --good:#3ecf8e; --warn:#f5b14b; --bad:#ef6464; }
  * { box-sizing: border-box; }
  body { margin:0; background:var(--bg); color:var(--fg); font:15px/1.5 -apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif; }
  .wrap { max-width: 880px; margin: 0 auto; padding: 48px 20px; }
  h1 { font-size: 28px; margin: 0 0 6px; letter-spacing:-0.01em; }
  .sub { color: var(--muted); margin-bottom: 32px; }
  form { display:flex; gap:8px; margin-bottom:24px; }
  input[type=url] { flex:1; background:var(--panel); border:1px solid var(--border); color:var(--fg); padding:14px 16px; border-radius:8px; font-size:15px; outline:none; }
  input[type=url]:focus { border-color: var(--accent); }
  button { background:var(--accent); color:#0b0d10; border:0; padding:14px 22px; border-radius:8px; font-weight:600; cursor:pointer; font-size:15px; }
  button:disabled { opacity:0.5; cursor:not-allowed; }
  .panel { background:var(--panel); border:1px solid var(--border); border-radius:10px; padding:20px; margin-top:16px; }
  .row { display:flex; justify-content:space-between; align-items:baseline; gap:12px; flex-wrap:wrap; }
  .score { font-size: 48px; font-weight:700; letter-spacing:-0.02em; }
  .grade { font-size: 28px; font-weight:600; padding:4px 14px; border-radius:8px; background:#222; }
  .grade.A { background:#13402c; color:var(--good); }
  .grade.B { background:#13402c; color:var(--good); }
  .grade.C { background:#403213; color:var(--warn); }
  .grade.D, .grade.F { background:#401818; color:var(--bad); }
  .meta { color:var(--muted); font-size:13px; }
  .sections { display:grid; grid-template-columns:repeat(auto-fit,minmax(140px,1fr)); gap:8px; margin-top:16px; }
  .sec { background:#0b0d10; border:1px solid var(--border); padding:10px 12px; border-radius:6px; }
  .sec .k { color:var(--muted); font-size:11px; text-transform:uppercase; letter-spacing:0.04em; }
  .sec .v { font-size:18px; font-weight:600; margin-top:2px; }
  .diag { white-space:pre-wrap; line-height:1.65; }
  .links { display:flex; gap:8px; margin-top:18px; flex-wrap:wrap; }
  .links a { background:#0b0d10; border:1px solid var(--border); color:var(--fg); text-decoration:none; padding:10px 14px; border-radius:6px; font-size:13px; }
  .links a:hover { border-color: var(--accent); color:var(--accent); }
  .status { display:inline-block; padding:3px 10px; border-radius:999px; font-size:12px; background:#1d2530; color:var(--accent); }
  .status.error { background:#401818; color:var(--bad); }
  .err { color:var(--bad); white-space:pre-wrap; font-family:ui-monospace,monospace; font-size:13px; }
  .spinner { display:inline-block; width:12px; height:12px; border:2px solid var(--border); border-top-color:var(--accent); border-radius:50%; animation:spin 0.8s linear infinite; vertical-align:middle; margin-right:6px; }
  @keyframes spin { to { transform:rotate(360deg); } }
  footer { color:var(--muted); font-size:12px; margin-top:40px; text-align:center; }
  footer a { color:var(--muted); }
</style>
</head>
<body>
<div class="wrap">
  <h1>AEO / SEO / GEO Auditor</h1>
  <div class="sub">Deterministic 97-check audit · Sieve brain (12,764 entries) · Claude Sonnet 4.6</div>

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
  out.innerHTML = '<div class="panel"><span class="status"><span class="spinner"></span>Submitting…</span></div>';

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
    out.innerHTML = '<div class="panel"><div class="status error">Error</div><div class="err" style="margin-top:10px">' + escapeHtml(err.message) + '</div></div>';
  } finally {
    $('go').disabled = false;
  }
});

async function poll(id) {
  const started = Date.now();
  while (true) {
    const r = await fetch('/audit/' + id);
    const data = await r.json();
    const elapsed = Math.round((Date.now() - started) / 1000);

    if (data.status === 'completed') { render(data); return; }
    if (data.status === 'error') {
      out.innerHTML = '<div class="panel"><div class="status error">Audit failed</div><div class="err" style="margin-top:10px">' + escapeHtml(data.error || 'unknown error') + '</div></div>';
      return;
    }
    out.innerHTML = '<div class="panel"><span class="status"><span class="spinner"></span>' +
      (data.status === 'queued' ? 'Queued' : 'Running') + ' · ' + elapsed + 's elapsed</span>' +
      '<div class="meta" style="margin-top:8px">Typical completion: 60–120 seconds. Running 97 checks across Technical, Performance, On-Page, Schema, AEO, GEO, Entity.</div></div>';
    await new Promise(r => setTimeout(r, 3000));
  }
}

function render(data) {
  const s = data.result_summary || {};
  const sec = s.section_scores || {};
  const grade = (s.overall_grade || '').charAt(0).toUpperCase();
  const a = data.artifacts || {};
  const id = data.audit_id;

  let secHtml = '';
  for (const [k, v] of Object.entries(sec)) {
    secHtml += '<div class="sec"><div class="k">' + escapeHtml(k) + '</div><div class="v">' + escapeHtml(String(v ?? '—')) + '</div></div>';
  }

  out.innerHTML =
    '<div class="panel">' +
      '<div class="row">' +
        '<div>' +
          '<div class="meta">' + escapeHtml(s.url || '') + '</div>' +
          '<div class="meta">' + escapeHtml(s.page_type || '—') + ' · ' + escapeHtml(s.industry || '—') + ' · ' + (data.duration_seconds || '?') + 's · ' + (s.findings_count || 0) + ' findings</div>' +
        '</div>' +
        '<div style="display:flex;align-items:center;gap:12px">' +
          '<div class="score">' + (s.overall_score ?? '—') + '</div>' +
          '<div class="grade ' + escapeHtml(grade) + '">' + escapeHtml(s.overall_grade || '—') + '</div>' +
        '</div>' +
      '</div>' +
      (secHtml ? '<div class="sections">' + secHtml + '</div>' : '') +
    '</div>' +

    (s.executive_diagnosis ? '<div class="panel"><h3 style="margin:0 0 12px;font-size:15px;color:var(--muted);text-transform:uppercase;letter-spacing:0.05em">Executive diagnosis</h3><div class="diag">' + escapeHtml(s.executive_diagnosis) + '</div></div>' : '') +

    '<div class="panel"><h3 style="margin:0 0 12px;font-size:15px;color:var(--muted);text-transform:uppercase;letter-spacing:0.05em">Download artifacts</h3>' +
      '<div class="links">' +
        '<a href="' + (a.json || '/audit/'+id+'/json') + '" target="_blank">Full JSON</a>' +
        '<a href="' + (a.markdown || '/audit/'+id+'/md') + '" target="_blank">Markdown report</a>' +
        '<a href="' + (a.pdf || '/audit/'+id+'/pdf') + '" target="_blank">PDF summary</a>' +
      '</div>' +
    '</div>';
}

function escapeHtml(s) {
  return String(s).replace(/[&<>"']/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
}
</script>
</body>
</html>
"""


@app.get('/', response_class=HTMLResponse)
def root():
    return HTMLResponse(INDEX_HTML)


@app.get('/api')
def api_info():
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
async def submit_audit(req: AuditRequest, background_tasks: BackgroundTasks):
    """Submit a URL for audit. Returns audit_id immediately; audit runs async.

    Poll GET /audit/{id} for status. Typical completion: 60-120 seconds.
    """
    audit_id = str(uuid.uuid4())
    url_str = str(req.url)

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
    with JOBS_LOCK:
        JOBS[audit_id]['status'] = 'running'
        JOBS[audit_id]['started_at'] = datetime.now(timezone.utc).isoformat()

    try:
        result = run_audit(url, output_dir=str(OUTPUT_DIR))
        with JOBS_LOCK:
            JOBS[audit_id]['status'] = 'completed'
            JOBS[audit_id]['completed_at'] = datetime.now(timezone.utc).isoformat()
            JOBS[audit_id]['result'] = result
    except Exception as e:
        with JOBS_LOCK:
            JOBS[audit_id]['status'] = 'error'
            JOBS[audit_id]['error'] = f'{type(e).__name__}: {e}'
            JOBS[audit_id]['completed_at'] = datetime.now(timezone.utc).isoformat()


@app.get('/audit/{audit_id}', response_model=AuditStatusResponse)
def get_audit(audit_id: str):
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

    if job['status'] == 'error':
        response['error'] = job.get('error')
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
def get_audit_json(audit_id: str):
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
def get_audit_markdown(audit_id: str):
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
def get_audit_pdf(audit_id: str):
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
def list_audits():
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
