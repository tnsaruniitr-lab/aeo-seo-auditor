"""
tools.py — Tool implementations for the audit agent.

Exposes 7 tools that mirror the capabilities the chat-based skill uses:

    1. web_fetch(url, extract_prompt=None)        — fetch HTML, return structured digest
    2. web_search(query, n=10)                    — Tavily API
    3. render_page_js(url)                        — Playwright: post-JS HTML + perf metrics
    4. run_deterministic_scripts(url)             — subprocess to skill-unified/scripts/run_deterministic.sh
    5. query_brain(check_id, page_type, industry) — wraps ranker.select_citations
    6. read_reference(name)                       — read skill-unified/references/{name}.md
    7. persist_audit(audit_data)                  — Supabase INSERT (best-effort) + always local

Each tool is a plain Python function returning JSON-serializable dicts.
TOOLS_SPEC at the bottom is the JSONSchema list passed to Anthropic messages.create
so the agent can call them via tool-use.

Design rules:
    - Tools never raise. They catch all exceptions and return {"error": str}.
    - Output payloads are bounded (truncate long fields) — keeps agent context small.
    - No tool depends on agent state — they're pure functions of their args + env.

ENV VARS
    ANTHROPIC_API_KEY        (required by agent, not by these tools directly)
    TAVILY_API_KEY           (required for web_search)
    SUPABASE_URL             (optional, for persist_audit)
    SUPABASE_SERVICE_KEY     (optional, for persist_audit)
"""

from __future__ import annotations

import json
import os
import re
import subprocess
import sys
import time
from pathlib import Path
from typing import Any, Dict, List, Optional
from urllib.parse import urlparse

# Paths
THIS_DIR = Path(__file__).resolve().parent
RULESET_DIR = THIS_DIR.parent / 'auditor-ruleset-export'
SCRIPTS_DIR = THIS_DIR.parent / 'skill-unified' / 'scripts'
REFERENCES_DIR = THIS_DIR.parent / 'skill-unified' / 'references'

sys.path.insert(0, str(RULESET_DIR))


# ============================================================================
# TOOL 1: web_fetch
# ============================================================================

def web_fetch(url: str, extract_prompt: Optional[str] = None) -> Dict[str, Any]:
    """Fetch a URL and return a structured digest of its content.

    Returns:
        {
          "url": str,                    # final URL after redirects
          "http_status": int,
          "content_type": str,
          "title": str,
          "meta_description": str,
          "canonical": str | None,
          "meta_robots": str | None,
          "h1": list[str],
          "h2": list[str],
          "h3": list[str],
          "schema_blocks": list[dict],   # parsed JSON-LD
          "open_graph": dict,
          "visible_text_excerpt": str,   # first ~3000 words of body text
          "word_count": int,
          "internal_link_count": int,
          "external_link_count": int,
          "html_size_bytes": int,
          "extracted": str | None,       # if extract_prompt given, Haiku extraction result
        }

    The structured digest is what the chat WebFetch tool effectively returns —
    a parseable summary, not raw HTML. extract_prompt is optional: if given,
    a cheap Haiku call answers the specific question against the cleaned text.
    """
    try:
        import httpx
        from selectolax.parser import HTMLParser
    except ImportError as e:
        return {"error": f"Missing dep: {e}. Install httpx + selectolax."}

    try:
        with httpx.Client(
            follow_redirects=True,
            timeout=30.0,
            headers={"User-Agent": "Mozilla/5.0 (compatible; AEO-Auditor/1.0)"},
        ) as client:
            r = client.get(url)
        final_url = str(r.url)
        html = r.text
        status = r.status_code
        ctype = r.headers.get("content-type", "")
    except Exception as e:
        return {"error": f"fetch failed: {type(e).__name__}: {e}"}

    if not html or "html" not in ctype.lower():
        return {
            "url": final_url, "http_status": status, "content_type": ctype,
            "error": "non-HTML or empty response",
            "html_size_bytes": len(html or ""),
        }

    try:
        tree = HTMLParser(html)
    except Exception as e:
        return {"error": f"HTML parse: {e}", "url": final_url, "http_status": status}

    def text_or_none(node):
        return node.text(strip=True) if node else None

    def attr_or_none(node, name):
        return node.attributes.get(name) if node else None

    title = text_or_none(tree.css_first("title")) or ""
    meta_desc_node = tree.css_first('meta[name="description"]')
    meta_desc = attr_or_none(meta_desc_node, "content") or ""
    canonical_node = tree.css_first('link[rel="canonical"]')
    canonical = attr_or_none(canonical_node, "href")
    meta_robots_node = tree.css_first('meta[name="robots"]')
    meta_robots = attr_or_none(meta_robots_node, "content")

    h1 = [n.text(strip=True) for n in tree.css("h1") if n.text(strip=True)]
    h2 = [n.text(strip=True) for n in tree.css("h2") if n.text(strip=True)]
    h3 = [n.text(strip=True) for n in tree.css("h3") if n.text(strip=True)]

    # JSON-LD blocks
    schema_blocks: List[Dict] = []
    for node in tree.css('script[type="application/ld+json"]'):
        raw = node.text(strip=False) or ""
        try:
            parsed = json.loads(raw)
            if isinstance(parsed, list):
                schema_blocks.extend(p for p in parsed if isinstance(p, dict))
            elif isinstance(parsed, dict):
                schema_blocks.append(parsed)
        except json.JSONDecodeError:
            pass

    # Open Graph
    og: Dict[str, str] = {}
    for node in tree.css('meta[property^="og:"]'):
        prop = node.attributes.get("property", "")
        content = node.attributes.get("content", "")
        if prop and content:
            og[prop[3:]] = content  # strip "og:"

    # Visible body text
    body = tree.css_first("body")
    body_text = ""
    if body:
        # Strip script/style/nav/footer for cleaner excerpt
        for sel in ("script", "style", "nav", "footer", "noscript", "svg"):
            for n in body.css(sel):
                n.decompose()
        body_text = body.text(separator=" ", strip=True)
        body_text = re.sub(r"\s+", " ", body_text)
    word_count = len(body_text.split())
    excerpt = " ".join(body_text.split()[:3000])

    # Link counts
    domain = urlparse(final_url).netloc
    internal = external = 0
    for a in tree.css("a[href]"):
        href = a.attributes.get("href", "")
        if not href or href.startswith(("#", "mailto:", "tel:", "javascript:")):
            continue
        if href.startswith("/"):
            internal += 1
        elif domain in href:
            internal += 1
        else:
            external += 1

    result = {
        "url": final_url,
        "http_status": status,
        "content_type": ctype,
        "title": title[:300],
        "meta_description": meta_desc[:500],
        "canonical": canonical,
        "meta_robots": meta_robots,
        "h1": h1[:10],
        "h2": h2[:30],
        "h3": h3[:50],
        "schema_blocks": schema_blocks[:20],
        "open_graph": og,
        "visible_text_excerpt": excerpt,
        "word_count": word_count,
        "internal_link_count": internal,
        "external_link_count": external,
        "html_size_bytes": len(html),
        "extracted": None,
    }

    # Optional Haiku extraction against the prompt
    if extract_prompt and excerpt:
        result["extracted"] = _haiku_extract(excerpt, extract_prompt)

    return result


def _haiku_extract(text: str, prompt: str) -> Optional[str]:
    """Cheap targeted extraction via Haiku. ~$0.001 per call."""
    try:
        from anthropic import Anthropic
    except ImportError:
        return None
    api_key = os.getenv("ANTHROPIC_API_KEY")
    if not api_key:
        return None
    try:
        client = Anthropic(api_key=api_key)
        msg = client.messages.create(
            model="claude-haiku-4-5",
            max_tokens=1500,
            system="You extract structured information from web page text. "
                   "Be concise and faithful to the source. Do not invent facts.",
            messages=[{
                "role": "user",
                "content": f"Page text:\n\n{text[:15000]}\n\n---\n\nTask: {prompt}",
            }],
        )
        return msg.content[0].text.strip()
    except Exception as e:
        return f"(extract failed: {type(e).__name__}: {e})"


# ============================================================================
# TOOL 2: web_search (Tavily)
# ============================================================================

def web_search(query: str, n: int = 10) -> Dict[str, Any]:
    """Search the web via Tavily API. Returns top-N organic results.

    Returns:
        {
          "query": str,
          "results": [
            {"title": str, "url": str, "snippet": str, "score": float},
            ...
          ],
          "answer": str | None,   # Tavily's own LLM-synthesized direct answer
        }
    """
    api_key = os.getenv("TAVILY_API_KEY")
    if not api_key:
        return {"error": "TAVILY_API_KEY not set", "query": query, "results": []}

    try:
        import httpx
    except ImportError:
        return {"error": "httpx not installed", "query": query, "results": []}

    try:
        with httpx.Client(timeout=20.0) as client:
            r = client.post(
                "https://api.tavily.com/search",
                json={
                    "api_key": api_key,
                    "query": query,
                    "search_depth": "basic",
                    "max_results": min(n, 20),
                    "include_answer": True,
                },
            )
        r.raise_for_status()
        data = r.json()
    except Exception as e:
        return {"error": f"{type(e).__name__}: {e}", "query": query, "results": []}

    results = []
    for item in data.get("results", [])[:n]:
        results.append({
            "title": item.get("title", "")[:300],
            "url": item.get("url", ""),
            "snippet": (item.get("content") or "")[:500],
            "score": item.get("score"),
        })

    return {
        "query": query,
        "results": results,
        "answer": data.get("answer"),
    }


# ============================================================================
# TOOL 3: render_page_js (Playwright)
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
# TOOL 4: run_deterministic_scripts
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
    """
    try:
        from ranker import select_citations
        brain = _get_brain()
    except Exception as e:
        return {"error": f"brain load: {type(e).__name__}: {e}", "citations": []}

    try:
        citations = select_citations(
            brain=brain, check_id=check_id,
            page_type=page_type, industry=industry,
            max_citations=max_citations,
        )
        # Trim verbose fields
        for c in citations:
            for k in ("if_condition", "then_action", "description"):
                if k in c and isinstance(c[k], str):
                    c[k] = c[k][:500]
        return {"check_id": check_id, "citations": citations}
    except Exception as e:
        return {"error": f"{type(e).__name__}: {e}", "citations": []}


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
    """Persist a completed audit. Tries Supabase if configured, always returns
    a deterministic local-only success.

    Returns: {"persisted": bool, "supabase_audit_id": str|None, "error": str|None}
    """
    supabase_url = os.getenv("SUPABASE_URL")
    supabase_key = os.getenv("SUPABASE_SERVICE_KEY")
    if not (supabase_url and supabase_key):
        return {"persisted": False, "supabase_audit_id": None,
                "note": "Supabase env vars not set — local-only persistence."}

    try:
        import httpx
    except ImportError:
        return {"persisted": False, "error": "httpx not installed"}

    headers = {
        "apikey": supabase_key,
        "Authorization": f"Bearer {supabase_key}",
        "Content-Type": "application/json",
        "Prefer": "return=representation",
    }
    audit_row = {
        "audit_id": audit_data.get("audit_id"),
        "url": audit_data.get("url"),
        "domain": audit_data.get("domain"),
        "page_type": audit_data.get("classification", {}).get("page_type"),
        "industry": audit_data.get("classification", {}).get("industry"),
        "overall_score": audit_data.get("scoring", {}).get("overall_score"),
        "overall_grade": audit_data.get("scoring", {}).get("overall_grade"),
        "section_scores": audit_data.get("scoring", {}).get("section_scores"),
        "narrative": audit_data.get("narrative"),
        "duration_seconds": audit_data.get("duration_seconds"),
        "created_at": audit_data.get("date"),
    }
    try:
        with httpx.Client(timeout=15.0) as client:
            r = client.post(
                f"{supabase_url}/rest/v1/website_audits",
                headers=headers, json=audit_row,
            )
        if r.status_code in (200, 201):
            return {"persisted": True,
                    "supabase_audit_id": audit_data.get("audit_id")}
        return {"persisted": False,
                "error": f"status {r.status_code}: {r.text[:300]}"}
    except Exception as e:
        return {"persisted": False, "error": f"{type(e).__name__}: {e}"}


# ============================================================================
# TOOL DISPATCH TABLE — used by agent.py
# ============================================================================

TOOLS_IMPL = {
    "web_fetch": web_fetch,
    "web_search": web_search,
    "render_page_js": render_page_js,
    "run_deterministic_scripts": run_deterministic_scripts,
    "query_brain": query_brain,
    "read_reference": read_reference,
    "persist_audit": persist_audit,
}


# ============================================================================
# JSONSCHEMA SPEC FOR ANTHROPIC TOOL-USE API
# ============================================================================

TOOLS_SPEC = [
    {
        "name": "web_fetch",
        "description": (
            "Fetch a URL and return a structured digest: title, meta tags, "
            "headings, JSON-LD schema blocks, OG tags, visible text excerpt "
            "(first 3000 words), word count, link counts, HTML size. "
            "Use this for the target page (Phase 1 content fetch) and "
            "competitor crawl (Phase 8). Optionally pass extract_prompt to "
            "get a Haiku-extracted answer to a specific question."
        ),
        "input_schema": {
            "type": "object",
            "properties": {
                "url": {"type": "string", "description": "Absolute URL to fetch"},
                "extract_prompt": {
                    "type": "string",
                    "description": "Optional. If provided, runs Haiku against the cleaned page text to answer this specific question. Example: 'List the author name, publication date, and any credentials shown.'",
                },
            },
            "required": ["url"],
        },
    },
    {
        "name": "web_search",
        "description": (
            "Search the web via Tavily. Returns up to N organic results "
            "(title, URL, snippet, relevance score) plus an LLM-synthesized "
            "direct answer. Use for company context (Phase 3a), competitor "
            "discovery (Phase 3b), and GEO brand presence (Phase 9)."
        ),
        "input_schema": {
            "type": "object",
            "properties": {
                "query": {"type": "string"},
                "n": {"type": "integer", "default": 10,
                      "description": "Number of results, max 20."},
            },
            "required": ["query"],
        },
    },
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
    {
        "name": "persist_audit",
        "description": (
            "Persist a completed audit. Best-effort Supabase INSERT to "
            "website_audits if SUPABASE_URL + SUPABASE_SERVICE_KEY are set; "
            "otherwise no-op success. Always call once at the end of Phase 14a "
            "with the full audit dict."
        ),
        "input_schema": {
            "type": "object",
            "properties": {"audit_data": {"type": "object"}},
            "required": ["audit_data"],
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
