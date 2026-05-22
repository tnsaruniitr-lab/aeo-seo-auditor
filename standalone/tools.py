"""
tools.py — Tool implementations for the audit agent.

Exposes 5 client-side tools the agent calls via Anthropic tool-use, plus
declares 2 Anthropic SERVER-side tools (web_search, web_fetch) that run
inside Anthropic's infrastructure with byte-for-byte parity to the chat
WebSearch / WebFetch tools.

Client-side tools (we dispatch in dispatch_tool):
    1. render_page_js(url)                        — Playwright: post-JS HTML + perf metrics
    2. run_deterministic_scripts(url)             — subprocess to skill-unified/scripts/run_deterministic.sh
    3. query_brain(check_id, page_type, industry) — wraps ranker.select_citations
    4. read_reference(name)                       — read skill-unified/references/{name}.md
    5. persist_audit(audit_data)                  — Supabase INSERT (best-effort) + always local

Server-side tools (Anthropic handles execution; we only declare in TOOLS_SPEC):
    6. web_search                                 — Anthropic native ($10 / 1k searches)
    7. web_fetch                                  — Anthropic native (free, only token costs)

Design rules:
    - Client tools never raise. They catch all exceptions and return {"error": str}.
    - Output payloads are bounded (truncate long fields) — keeps agent context small.
    - No tool depends on agent state — they're pure functions of their args + env.
    - Server tools are dispatched by Anthropic itself; agent.py skips them in its
      dispatch loop (they appear as web_search_tool_use / web_fetch_tool_use blocks
      in the assistant message, with results inlined as *_tool_result blocks).

ENV VARS
    ANTHROPIC_API_KEY        (required — also pays for web_search/web_fetch usage)
    SUPABASE_URL             (optional, for persist_audit)
    SUPABASE_SERVICE_KEY     (optional, for persist_audit)
"""

from __future__ import annotations

import json
import logging
import os
import re
import subprocess
import sys
import time
from pathlib import Path
from typing import Any, Dict, List, Optional

log = logging.getLogger('audit.tools')

# Paths
THIS_DIR = Path(__file__).resolve().parent
RULESET_DIR = THIS_DIR.parent / 'auditor-ruleset-export'
SCRIPTS_DIR = THIS_DIR.parent / 'skill-unified' / 'scripts'
REFERENCES_DIR = THIS_DIR.parent / 'skill-unified' / 'references'

sys.path.insert(0, str(RULESET_DIR))


# ============================================================================
# NOTE: web_fetch and web_search are Anthropic SERVER-side tools.
# They are NOT implemented here — Anthropic executes them. We only declare
# them in TOOLS_SPEC at the bottom of this file. See:
#   https://platform.claude.com/docs/en/agents-and-tools/tool-use/web-search-tool
#   https://platform.claude.com/docs/en/agents-and-tools/tool-use/web-fetch-tool
# ============================================================================


# ============================================================================
# TOOL: render_page_js (Playwright)
# ============================================================================

def render_page_js(url: str) -> Dict[str, Any]:
    """Render a page with a real browser (Playwright + Chromium).

    Returns post-JS HTML and performance metrics:
        {
          "url": str,
          "post_js_html_size": int,
          "title": str,
          "h1_first": str,
          "ttfb_ms": float,
          "lcp_ms": float | None,
          "cls": float | None,
          "load_time_ms": float,
          "request_count": int,
          "console_errors": [str],
          "spa_signals": [str],   # detected frameworks (Next.js, React, etc.)
        }
    """
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        return {"error": "playwright not installed. pip install playwright && playwright install chromium"}

    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True, args=["--no-sandbox"])
            ctx = browser.new_context(
                user_agent="Mozilla/5.0 (compatible; AEO-Auditor/1.0; +Playwright)"
            )
            page = ctx.new_page()

            console_errors: List[str] = []
            page.on("console", lambda msg: console_errors.append(msg.text)
                    if msg.type == "error" else None)
            request_count = [0]
            page.on("request", lambda _: request_count.__setitem__(0, request_count[0] + 1))

            t0 = time.time()
            response = page.goto(url, wait_until="networkidle", timeout=30000)
            load_time_ms = (time.time() - t0) * 1000

            # TTFB from response timing
            ttfb_ms = None
            try:
                timing = response.request.timing if response else None
                if timing:
                    ttfb_ms = timing.get("responseStart")
            except Exception:
                pass

            # LCP via PerformanceObserver — best-effort
            try:
                lcp = page.evaluate("""
                    () => new Promise((resolve) => {
                        let lcp = null;
                        try {
                            new PerformanceObserver((list) => {
                                const entries = list.getEntries();
                                if (entries.length) lcp = entries[entries.length - 1].startTime;
                            }).observe({type: 'largest-contentful-paint', buffered: true});
                        } catch(e) {}
                        setTimeout(() => resolve(lcp), 2000);
                    })
                """)
            except Exception:
                lcp = None

            # CLS — also best-effort
            try:
                cls = page.evaluate("""
                    () => new Promise((resolve) => {
                        let cls = 0;
                        try {
                            new PerformanceObserver((list) => {
                                for (const entry of list.getEntries()) {
                                    if (!entry.hadRecentInput) cls += entry.value;
                                }
                            }).observe({type: 'layout-shift', buffered: true});
                        } catch(e) {}
                        setTimeout(() => resolve(cls), 1500);
                    })
                """)
            except Exception:
                cls = None

            # SPA framework detection
            spa = page.evaluate("""
                () => {
                    const out = [];
                    if (window.__NEXT_DATA__) out.push('Next.js');
                    if (window.__NUXT__) out.push('Nuxt');
                    if (window.React || document.querySelector('[data-reactroot]')) out.push('React');
                    if (window.Vue) out.push('Vue');
                    if (window.ng) out.push('Angular');
                    return out;
                }
            """) or []

            html = page.content()
            title = page.title()
            h1 = ""
            try:
                h1_node = page.query_selector("h1")
                if h1_node:
                    h1 = (h1_node.inner_text() or "").strip()[:300]
            except Exception:
                pass

            browser.close()

            return {
                "url": url,
                "post_js_html_size": len(html),
                "title": title[:300],
                "h1_first": h1,
                "ttfb_ms": ttfb_ms,
                "lcp_ms": lcp,
                "cls": cls,
                "load_time_ms": round(load_time_ms, 1),
                "request_count": request_count[0],
                "console_errors": console_errors[:20],
                "spa_signals": spa,
            }
    except Exception as e:
        return {"error": f"{type(e).__name__}: {e}", "url": url}


# ============================================================================
# TOOL: run_deterministic_scripts
# ============================================================================

DETERMINISTIC_SCRIPT = SCRIPTS_DIR / "run_deterministic.sh"


def run_deterministic_scripts(url: str, timeout: int = 180) -> Dict[str, Any]:
    """Invoke skill-unified/scripts/run_deterministic.sh and parse JSON output.

    Returns the orchestrator JSON: bots_eye_view, all_checks, overall_summary,
    sitemap_analysis, robots_txt_analysis, schema_completeness.
    """
    if not DETERMINISTIC_SCRIPT.exists():
        return {"error": f"Script not found: {DETERMINISTIC_SCRIPT}"}

    try:
        proc = subprocess.run(
            ["bash", str(DETERMINISTIC_SCRIPT), url],
            capture_output=True, text=True, timeout=timeout,
        )
    except subprocess.TimeoutExpired:
        return {"error": f"timed out after {timeout}s"}
    except Exception as e:
        return {"error": f"{type(e).__name__}: {e}"}

    try:
        return json.loads(proc.stdout)
    except json.JSONDecodeError as e:
        return {
            "error": f"JSON parse: {e}",
            "stdout_first_2000": proc.stdout[:2000],
            "stderr_first_2000": proc.stderr[:2000],
        }


# ============================================================================
# TOOL 5: query_brain
# ============================================================================

_BRAIN_CACHE = None


def _get_brain():
    global _BRAIN_CACHE
    if _BRAIN_CACHE is None:
        from ranker import BrainIndex
        _BRAIN_CACHE = BrainIndex.from_export_dir(str(RULESET_DIR))
    return _BRAIN_CACHE


def query_brain(check_id: str, page_type: str = "homepage",
                industry: str = "other", max_citations: int = 3) -> Dict[str, Any]:
    """Query the Sieve brain for citations relevant to a given check_id.

    Returns top-N rules + anti-patterns ranked by tier ASC, confidence DESC.

    Resolution order for the check_id:
        1. Exact match  ('A2b_title_uniqueness_sample' → exact key)
        2. Strip trailing letter from the numeric prefix
           ('A2b_title_uniqueness_sample' → 'A2_*' prefix scan)
        3. Bare-section prefix scan
           ('A2b_anything' → first key starting with 'A2_')

    This handles the case where the deterministic scripts emit sub-check IDs
    like 'A2b_title_uniqueness_sample' (a sub-check of the parent A2) but
    the brain mapping was authored against the parent 'A2_title_tag'. Falling
    back to the parent gives reasonable citations for sub-checks.
    """
    try:
        from ranker import select_citations
        brain = _get_brain()
    except Exception as e:
        return {"error": f"brain load: {type(e).__name__}: {e}", "citations": []}

    resolved_id = _resolve_check_id(check_id, brain.check_to_rules)

    try:
        citations = select_citations(
            brain=brain, check_id=resolved_id,
            page_type=page_type, industry=industry,
            max_citations=max_citations,
        )
        # Trim verbose fields
        for c in citations:
            for k in ("if_condition", "then_action", "description"):
                if k in c and isinstance(c[k], str):
                    c[k] = c[k][:500]
        return {
            "check_id": check_id,
            "resolved_to": resolved_id if resolved_id != check_id else None,
            "citations": citations,
        }
    except Exception as e:
        return {"error": f"{type(e).__name__}: {e}", "citations": []}


def _resolve_check_id(check_id: str, mappings: Dict[str, Any]) -> str:
    """Resolve a (possibly sub-check) ID to a key present in brain-mappings.

    Examples:
        'A2_title_tag'                 → 'A2_title_tag'                 (exact)
        'A2b_title_uniqueness_sample'  → 'A2_title_tag'                 (strip 'b')
        'D14_hreflang_coverage'        → 'D14_hreflang_coverage'        (exact)
        'C12b_datemodified_staleness'  → 'C12_visible_date_staleness'   (parent prefix)
        'unknown_check_id'             → 'unknown_check_id'             (no resolution)
    """
    if check_id in mappings:
        return check_id

    # Extract the section prefix (e.g. "A2b" → "A2", "C12b" → "C12")
    import re
    m = re.match(r"^([A-J])(\d+)([a-z])?(_.*)?$", check_id)
    if not m:
        return check_id  # not a section-style ID, return as-is

    section, num, letter, suffix = m.groups()
    bare_prefix = f"{section}{num}"

    # Try the bare prefix as a key starter (e.g. "A2_")
    candidates = [k for k in mappings if k.startswith(bare_prefix + "_")]
    if candidates:
        # If the original had a sub-letter (A2b), prefer non-sub-lettered keys
        # If multiple, take the shortest/most generic name
        return sorted(candidates, key=len)[0]

    return check_id


# ============================================================================
# TOOL 6: read_reference
# ============================================================================

# Whitelist — only these reference files are loadable
ALLOWED_REFERENCES = {
    "static-rules", "check-definitions", "schema-validation",
    "knowledge-seo", "knowledge-performance", "knowledge-aeo",
    "knowledge-geo", "aeo-framework", "geo-framework",
    "scoring-rubric", "brain-mappings", "competitor-gap-template",
    "supabase-queries",
}


def read_reference(name: str) -> Dict[str, Any]:
    """Read a reference markdown file from skill-unified/references/.

    Args:
        name: file basename without .md (e.g. "static-rules", "schema-validation")
    """
    if name not in ALLOWED_REFERENCES:
        return {
            "error": f"unknown reference: {name}",
            "allowed": sorted(ALLOWED_REFERENCES),
        }
    path = REFERENCES_DIR / f"{name}.md"
    if not path.exists():
        return {"error": f"file missing: {path}"}
    try:
        content = path.read_text(encoding="utf-8")
    except Exception as e:
        return {"error": f"{type(e).__name__}: {e}"}
    return {"name": name, "size_bytes": len(content), "content": content}


# ============================================================================
# TOOL 7: persist_audit
# ============================================================================

def persist_audit(audit_data: Dict[str, Any]) -> Dict[str, Any]:
    """Persist a completed audit to Supabase — both the audit summary row
    and one row per finding.

    Writes to project htowtfnbfmjmbeftfhis (set via SUPABASE_URL env var):
        - public.website_audits          (1 row, 30-column schema)
        - public.website_audit_findings  (N rows, FK on audit_id)

    Uses the service_role key (SUPABASE_SERVICE_KEY) which bypasses RLS.
    If either env var is unset, returns a local-only no-op success.

    Returns:
        {
          "persisted": bool,
          "supabase_row_id": str | None,   # the table's gen_random_uuid() id
          "audit_id": str,                  # the agent's own audit uuid
          "findings_persisted": int,
          "error": str | None,
        }
    """
    supabase_url = os.getenv("SUPABASE_URL")
    supabase_key = os.getenv("SUPABASE_SERVICE_KEY")
    audit_id = audit_data.get("audit_id")

    if not (supabase_url and supabase_key):
        return {"persisted": False, "supabase_row_id": None,
                "audit_id": audit_id, "findings_persisted": 0,
                "note": "Supabase env vars not set — local-only persistence."}

    try:
        import httpx
    except ImportError:
        return {"persisted": False, "error": "httpx not installed",
                "audit_id": audit_id, "findings_persisted": 0}

    base = supabase_url.rstrip("/")
    headers = {
        "apikey": supabase_key,
        "Authorization": f"Bearer {supabase_key}",
        "Content-Type": "application/json",
    }

    classification = audit_data.get("classification", {}) or {}
    context = audit_data.get("context", {}) or {}
    scoring = audit_data.get("scoring", {}) or {}
    findings = audit_data.get("findings", []) or []

    # ---- Audit summary row — matches the 30-column website_audits schema ----
    audit_row = {
        "audit_id": audit_id,
        "url": audit_data.get("url"),
        "domain": audit_data.get("domain"),
        "audit_date": audit_data.get("date"),
        "page_type": classification.get("page_type"),
        "industry": classification.get("industry"),
        "company_name": classification.get("company_name"),
        "confidence": classification.get("confidence"),
        "competitors": context.get("competitors"),
        "test_queries": context.get("test_queries"),
        "gates": audit_data.get("gates"),
        "section_scores": scoring.get("section_scores"),
        "page_citation_readiness": scoring.get("page_citation_readiness"),
        "brand_ai_presence": scoring.get("brand_ai_presence"),
        "seo_score": scoring.get("seo_score"),
        "aeo_score": scoring.get("aeo_score"),
        "citation_readiness": scoring.get("citation_readiness"),
        "overall_score": scoring.get("overall_score"),
        "overall_grade": scoring.get("overall_grade"),
        "narrative": audit_data.get("narrative"),
        "competitor_comparison": audit_data.get("competitor_comparison"),
        "bots_eye_view": audit_data.get("bots_eye_view"),
        "performance": audit_data.get("performance"),
        "supplementary_findings": audit_data.get("supplementary_findings"),
        "metadata": audit_data.get("metadata"),
        "findings_count": len(findings),
        "duration_seconds": audit_data.get("duration_seconds"),
        "audit_mode": (audit_data.get("metadata", {}) or {}).get("version", "agent"),
    }

    try:
        with httpx.Client(timeout=20.0) as client:
            # 1. Insert the audit summary row. resolution=merge-duplicates makes
            #    a re-persist of the same audit_id idempotent (upsert on the
            #    unique audit_id column).
            r = client.post(
                f"{base}/rest/v1/website_audits",
                headers={**headers,
                         "Prefer": "return=representation,resolution=merge-duplicates"},
                json=audit_row,
            )
            if r.status_code not in (200, 201):
                return {"persisted": False,
                        "error": f"website_audits insert status {r.status_code}: "
                                 f"{r.text[:400]}",
                        "audit_id": audit_id, "findings_persisted": 0}
            inserted = r.json()
            row_id = inserted[0].get("id") if inserted else None

            # 2. Insert findings (batch). Replace any existing rows for this
            #    audit_id first so a re-persist doesn't duplicate.
            findings_persisted = 0
            if findings:
                client.delete(
                    f"{base}/rest/v1/website_audit_findings",
                    headers=headers,
                    params={"audit_id": f"eq.{audit_id}"},
                )
                findings_rows = [
                    {
                        "audit_id": audit_id,
                        "check_id": f.get("check_id"),
                        "section": f.get("section"),
                        "status": f.get("status"),
                        "severity": f.get("severity"),
                        "evidence": (f.get("evidence") or "")[:4000],
                        "truth_badge": f.get("truth_badge"),
                        "fix_type": f.get("fix_type"),
                        "citations": f.get("citations"),
                    }
                    for f in findings
                ]
                fr = client.post(
                    f"{base}/rest/v1/website_audit_findings",
                    headers={**headers, "Prefer": "return=minimal"},
                    json=findings_rows,
                )
                if fr.status_code in (200, 201):
                    findings_persisted = len(findings_rows)
                else:
                    # Audit row saved; findings failed — report partial success
                    return {"persisted": True, "supabase_row_id": row_id,
                            "audit_id": audit_id, "findings_persisted": 0,
                            "error": f"findings insert status {fr.status_code}: "
                                     f"{fr.text[:300]}"}

        return {"persisted": True, "supabase_row_id": row_id,
                "audit_id": audit_id, "findings_persisted": findings_persisted}
    except Exception as e:
        return {"persisted": False, "error": f"{type(e).__name__}: {e}",
                "audit_id": audit_id, "findings_persisted": 0}


# ============================================================================
# TOOL DISPATCH TABLE — used by agent.py
# ============================================================================

# Only CLIENT-side tools are dispatched in this table.
# Server-side tools (web_search, web_fetch) are executed by Anthropic itself.
# NOTE: persist_audit is intentionally NOT here — it is a post-loop step
# called directly by run_audit_agent() with the real audit_id + complete
# audit dict, not a tool the agent invokes mid-loop.
TOOLS_IMPL = {
    "render_page_js": render_page_js,
    "run_deterministic_scripts": run_deterministic_scripts,
    "query_brain": query_brain,
    "read_reference": read_reference,
}

# Names of Anthropic server-side tools — agent.py skips these in dispatch
# (their tool_use blocks are handled by Anthropic's servers, with results
# returned inline as *_tool_result blocks in the same assistant turn).
SERVER_TOOL_NAMES = {"web_search", "web_fetch"}


# ============================================================================
# JSONSCHEMA SPEC FOR ANTHROPIC TOOL-USE API
# ============================================================================

TOOLS_SPEC = [
    # ----- Anthropic SERVER-side tools -------------------------------------
    # These are executed by Anthropic infrastructure (same backend the chat
    # WebSearch / WebFetch tools use). We do not implement them in TOOLS_IMPL.
    # Pricing: web_search = $10 per 1,000 searches; web_fetch = free (token
    # costs only). Both work on claude-sonnet-4-6 with no beta header.
    {
        "type": "web_search_20250305",
        "name": "web_search",
        "max_uses": 8,  # cap per audit — covers Phase 3a/3b/3c (4 queries) + Phase 9 (2) + headroom
    },
    {
        "type": "web_fetch_20250910",
        "name": "web_fetch",
        "max_uses": 8,  # cap per audit — Phase 1 target + Phase 8 (5 competitors) + headroom
        "citations": {"enabled": True},
        "max_content_tokens": 100_000,
    },
    # ----- Client-side tools (we dispatch these in agent.py) ----------------
    {
        "name": "render_page_js",
        "description": (
            "Render a URL with a real headless Chromium browser via Playwright. "
            "Returns post-JS HTML size, title, first H1, performance metrics "
            "(TTFB, LCP, CLS, load time, request count), console errors, and "
            "detected SPA framework signals. Use for Phase 1.5 performance "
            "measurement and to detect SPA-without-SSR cases. Slower than "
            "web_fetch (~5–10s) — only use when JS rendering or perf metrics "
            "are needed."
        ),
        "input_schema": {
            "type": "object",
            "properties": {"url": {"type": "string"}},
            "required": ["url"],
        },
    },
    {
        "name": "run_deterministic_scripts",
        "description": (
            "Invoke the skill's deterministic bash + Python script suite. "
            "Returns the full orchestrator JSON: bots_eye_view (5 UA probes "
            "+ classification), all_checks (D9, A7b, J2, A4b, B1, D4, C12b, "
            "A2b, D14, D12), overall_summary, sitemap_analysis (parsed XML, "
            "URL count, target_url presence), robots_txt_analysis (per-UA "
            "allowlist), schema_completeness (entities + missing fields). "
            "Call this once early in Phase 1.6 — it's the foundation of "
            "Phase 5–7 deterministic checks."
        ),
        "input_schema": {
            "type": "object",
            "properties": {"url": {"type": "string"}},
            "required": ["url"],
        },
    },
    {
        "name": "query_brain",
        "description": (
            "Query the Sieve brain (12,764 entries) for citations supporting "
            "a specific check. Returns top-3 rules + anti-patterns ranked by "
            "tier (1=Google/Schema.org, 2=Backlinko/Vercel, 3=SEL, 4=specialized) "
            "and confidence. Use during Phase 13 (citation enrichment) for "
            "every failed/warned check. check_id should match the static-rules "
            "namespace (e.g. 'D14_hreflang_coverage', 'A2b_title_uniqueness_sample')."
        ),
        "input_schema": {
            "type": "object",
            "properties": {
                "check_id": {"type": "string"},
                "page_type": {"type": "string", "default": "homepage"},
                "industry": {"type": "string", "default": "other"},
                "max_citations": {"type": "integer", "default": 3},
            },
            "required": ["check_id"],
        },
    },
    {
        "name": "read_reference",
        "description": (
            "Read a reference markdown file from skill-unified/references/. "
            "Use this to load detailed criteria when needed. Available files: "
            "static-rules (all 103 check criteria), check-definitions (truth "
            "badges + fix types), schema-validation (per-entity required "
            "fields), knowledge-seo / knowledge-performance / knowledge-aeo / "
            "knowledge-geo (research thresholds), aeo-framework (4-stage "
            "model), geo-framework (3-dimension model), scoring-rubric "
            "(weights + grades + DO NOW/PLAN/LATER matrix), brain-mappings "
            "(check_id → rule mappings), competitor-gap-template (Phase 8 "
            "comparison shape), supabase-queries (persistence SQL). "
            "Reference files are large — only load what you need for the "
            "current phase."
        ),
        "input_schema": {
            "type": "object",
            "properties": {
                "name": {
                    "type": "string",
                    "enum": sorted(ALLOWED_REFERENCES),
                },
            },
            "required": ["name"],
        },
    },
]


# ============================================================================
# DISPATCH
# ============================================================================

def dispatch_tool(name: str, tool_input: Dict[str, Any]) -> Dict[str, Any]:
    """Run a tool by name with the given input dict. Returns the tool's output
    or {"error": ...} if the tool is unknown or raises."""
    impl = TOOLS_IMPL.get(name)
    if impl is None:
        return {"error": f"unknown tool: {name}"}
    try:
        return impl(**tool_input)
    except TypeError as e:
        return {"error": f"bad arguments to {name}: {e}"}
    except Exception as e:
        return {"error": f"{type(e).__name__}: {e}"}


if __name__ == "__main__":
    # Smoke test from CLI: python tools.py <tool> <json_args>
    if len(sys.argv) < 2:
        print("Usage: python tools.py <tool_name> [json_args]")
        print("Tools:", ", ".join(TOOLS_IMPL.keys()))
        sys.exit(1)
    tool_name = sys.argv[1]
    args = json.loads(sys.argv[2]) if len(sys.argv) > 2 else {}
    result = dispatch_tool(tool_name, args)
    print(json.dumps(result, indent=2, ensure_ascii=False, default=str)[:5000])
