"""
agent.py — Audit agent harness.

Runs the 15-phase playbook in `system_prompt.py` as a Claude tool-use loop.
The agent calls tools defined in tools.py until it emits a final
`<audit>...</audit>` JSON payload.

This is the parity layer: same model (claude-sonnet-4-6), same playbook
(skill-unified/SKILL.md adaptation), same tools (web_fetch, web_search,
Playwright render, deterministic scripts, brain ranker, references) as the
chat skill — just headless.

USAGE
    from agent import run_audit_agent
    result = run_audit_agent("https://example.com", output_dir="./audits/")

ENV
    ANTHROPIC_API_KEY     required
    TAVILY_API_KEY        required for web_search
    SUPABASE_URL/KEY      optional for persist_audit
"""

from __future__ import annotations

import json
import logging
import os
import re
import sys
import time
import traceback
import uuid
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional

THIS_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(THIS_DIR))

from tools import TOOLS_SPEC, dispatch_tool, SERVER_TOOL_NAMES
from system_prompt import SYSTEM_PROMPT

log = logging.getLogger('audit.agent')


# -----------------------------------------------------------------------------
# CONFIG
# -----------------------------------------------------------------------------

MODEL = "claude-sonnet-4-6"
# Output token cap per turn. The final audit JSON is ~26KB (~7-8K tokens)
# and intermediate turns are tiny (~200 tokens), so a generous ceiling
# avoids the "max_tokens cut off the final JSON mid-object" failure mode.
# Sonnet 4.6 supports up to 64K output tokens.
MAX_TOKENS_PER_TURN = 32768
MAX_AGENT_TURNS = 80              # hard cap on tool-use iterations
MAX_TOOL_RESULT_BYTES = 50_000     # truncate big tool outputs (e.g. raw scripts JSON)
TOTAL_BUDGET_SECONDS = 480         # 8-minute hard ceiling per audit


# -----------------------------------------------------------------------------
# CORE LOOP
# -----------------------------------------------------------------------------

def run_agent_loop(url: str, verbose: bool = False,
                    log_prefix: str = '') -> Dict[str, Any]:
    """Drive the Claude tool-use loop until the agent emits <audit>...</audit>.

    Returns:
        {
          "audit": dict | None,        # parsed audit JSON
          "raw_final_text": str,       # last assistant text (for debugging)
          "tool_calls": [...],         # log of (name, input_summary, ms)
          "turns": int,
          "stop_reason": str,
          "input_tokens": int,
          "output_tokens": int,
          "errors": [str],
        }
    """
    try:
        from anthropic import Anthropic
    except ImportError:
        return _fail("anthropic SDK not installed")

    api_key = os.getenv("ANTHROPIC_API_KEY")
    if not api_key:
        return _fail("ANTHROPIC_API_KEY not set")

    client = Anthropic(api_key=api_key)

    messages: List[Dict[str, Any]] = [{
        "role": "user",
        "content": (
            f"Audit this URL: {url}\n\n"
            "Execute all 15 phases in order. Use the tools as specified. "
            "When finished, your FINAL message must be ONLY a single JSON "
            "object wrapped in <audit>...</audit> tags."
        ),
    }]

    tool_call_log: List[Dict[str, Any]] = []
    errors: List[str] = []
    input_tokens_total = 0
    output_tokens_total = 0
    raw_final_text = ""
    stop_reason = "unknown"
    turns = 0

    started = time.time()
    pfx = log_prefix or ''
    log.info('%sloop start url=%s', pfx, url)

    for turn in range(MAX_AGENT_TURNS):
        turns = turn + 1

        if time.time() - started > TOTAL_BUDGET_SECONDS:
            msg = f"hit total budget {TOTAL_BUDGET_SECONDS}s at turn {turns}"
            errors.append(msg)
            log.warning('%s%s', pfx, msg)
            break

        try:
            # Use streaming so we're not bound by the SDK's non-streaming
            # 10-minute upper-bound heuristic. With MAX_TOKENS_PER_TURN at
            # 32768 the SDK refuses non-streaming requests because
            # 32768 / conservative_token_rate could exceed 600s. Streaming
            # bypasses this — same response shape, same cost.
            with client.messages.stream(
                model=MODEL,
                max_tokens=MAX_TOKENS_PER_TURN,
                system=SYSTEM_PROMPT,
                tools=TOOLS_SPEC,
                messages=messages,
            ) as stream:
                response = stream.get_final_message()
        except Exception as e:
            errors.append(f"messages.stream failed turn {turns}: "
                          f"{type(e).__name__}: {e}")
            log.error('%smessages.stream failed turn=%d: %s: %s',
                      pfx, turns, type(e).__name__, e)
            log.error('%s%s', pfx, traceback.format_exc())
            break

        input_tokens_total += response.usage.input_tokens
        output_tokens_total += response.usage.output_tokens
        stop_reason = response.stop_reason

        log.info('%sturn=%d stop=%s in=%d out=%d',
                 pfx, turns, stop_reason,
                 response.usage.input_tokens, response.usage.output_tokens)
        if verbose:
            print(f"[turn {turns}] stop={stop_reason} "
                  f"in={response.usage.input_tokens} "
                  f"out={response.usage.output_tokens}", flush=True)

        # Append assistant turn (includes text + tool_use blocks)
        messages.append({"role": "assistant", "content": response.content})

        # Capture latest assistant text + log a preview of reasoning,
        # log server-tool invocations (which Anthropic dispatched itself).
        for block in response.content:
            btype = getattr(block, "type", None)
            if btype == "text":
                txt = (block.text or "").strip()
                if txt:
                    raw_final_text = block.text
                    preview = txt[:240].replace("\n", " ")
                    log.info('%s  text: %s%s', pfx, preview,
                             '...' if len(txt) > 240 else '')
            elif btype in ("server_tool_use", "web_search_tool_use", "web_fetch_tool_use"):
                # Anthropic-dispatched server tool. Log so we know it ran.
                tname = getattr(block, "name", "server_tool")
                tin = getattr(block, "input", None) or {}
                log.info('%s  → [server] %s(%s)', pfx, tname, _short(tin))
            elif btype in ("web_search_tool_result", "web_fetch_tool_result"):
                # Result of a server tool — Anthropic already executed it.
                # Log size if we can.
                content = getattr(block, "content", None)
                csize = (len(json.dumps(content, default=str))
                         if content is not None else 0)
                log.info('%s  ← [server] result %dB', pfx, csize)

        if stop_reason == "end_turn":
            log.info('%send_turn at turn=%d', pfx, turns)
            break

        if stop_reason != "tool_use":
            msg = f"unexpected stop_reason '{stop_reason}' at turn {turns}"
            errors.append(msg)
            log.warning('%s%s', pfx, msg)
            break

        # Run all CLIENT tool_use blocks. Server tools (web_search, web_fetch)
        # are dispatched by Anthropic itself; their results appear inline as
        # *_tool_result blocks in the same assistant turn — we don't process
        # them here and the SDK handles serializing them in the next turn.
        tool_result_blocks: List[Dict[str, Any]] = []
        for block in response.content:
            if getattr(block, "type", None) != "tool_use":
                continue
            name = block.name
            if name in SERVER_TOOL_NAMES:
                continue
            tinput = block.input or {}

            t0 = time.time()
            try:
                result = dispatch_tool(name, tinput)
            except Exception as e:
                result = {"error": f"dispatch crash {type(e).__name__}: {e}"}
                log.error('%s  dispatch crash %s: %s\n%s', pfx, name, e,
                          traceback.format_exc())
            elapsed_ms = int((time.time() - t0) * 1000)

            # Truncate huge results to keep context tractable
            result_str = json.dumps(result, default=str, ensure_ascii=False)
            if len(result_str) > MAX_TOOL_RESULT_BYTES:
                result_str = (
                    result_str[:MAX_TOOL_RESULT_BYTES]
                    + f'... [truncated {len(result_str) - MAX_TOOL_RESULT_BYTES} bytes]'
                )

            had_error = "error" in (result if isinstance(result, dict) else {})
            tool_call_log.append({
                "turn": turns, "name": name,
                "input_keys": list(tinput.keys()),
                "input_preview": _short(tinput),
                "ms": elapsed_ms,
                "result_size": len(result_str),
                "had_error": had_error,
            })

            log_method = log.error if had_error else log.info
            log_method('%s  → %s(%s) %dms %dB%s',
                       pfx, name, _short(tinput), elapsed_ms, len(result_str),
                       ' ERROR' if had_error else '')
            if had_error:
                err_msg = (result.get("error") if isinstance(result, dict) else "?")
                log.error('%s    error: %s', pfx, err_msg)
            if verbose:
                print(f"  → {name}({_short(tinput)}) "
                      f"[{elapsed_ms}ms, {len(result_str)}B]", flush=True)

            tool_result_blocks.append({
                "type": "tool_result",
                "tool_use_id": block.id,
                "content": result_str,
            })

        if not tool_result_blocks:
            msg = f"stop_reason=tool_use but no client tool_use blocks turn {turns}"
            errors.append(msg)
            log.warning('%s%s', pfx, msg)
            break

        messages.append({"role": "user", "content": tool_result_blocks})

    else:
        msg = f"hit MAX_AGENT_TURNS={MAX_AGENT_TURNS}"
        errors.append(msg)
        log.warning('%s%s', pfx, msg)

    audit = _extract_audit_json(raw_final_text, errors)
    if audit is not None:
        log.info('%sextracted audit JSON (%d top-level keys, %dB raw)',
                 pfx, len(audit), len(json.dumps(audit, default=str)))
    else:
        log.error('%sfailed to extract audit JSON. raw_final_text len=%d preview=%s',
                  pfx, len(raw_final_text), raw_final_text[:300].replace('\n', ' \\n '))

    log.info('%sloop done turns=%d stop=%s tokens=%d+%d errors=%d',
             pfx, turns, stop_reason, input_tokens_total, output_tokens_total,
             len(errors))

    return {
        "audit": audit,
        "raw_final_text": raw_final_text[:5000],
        "tool_calls": tool_call_log,
        "turns": turns,
        "stop_reason": stop_reason,
        "input_tokens": input_tokens_total,
        "output_tokens": output_tokens_total,
        "errors": errors,
        "duration_seconds": round(time.time() - started, 1),
    }


# -----------------------------------------------------------------------------
# HELPERS
# -----------------------------------------------------------------------------

def _fail(msg: str) -> Dict[str, Any]:
    return {
        "audit": None, "raw_final_text": "", "tool_calls": [],
        "turns": 0, "stop_reason": "error",
        "input_tokens": 0, "output_tokens": 0,
        "errors": [msg], "duration_seconds": 0,
    }


def _short(d: Dict[str, Any], max_len: int = 80) -> str:
    s = json.dumps(d, default=str, ensure_ascii=False)
    return s[:max_len] + ("..." if len(s) > max_len else "")


_AUDIT_TAG_RE = re.compile(r"<audit>\s*(\{.*?\})\s*</audit>", re.DOTALL)


def _extract_audit_json(text: str, errors: List[str]) -> Optional[Dict[str, Any]]:
    """Pull the JSON object from the final assistant text. Robust to:
       - <audit>{...}</audit> tags (preferred)
       - bare {...} JSON if tags missing
       - markdown ```json fences
    """
    if not text:
        errors.append("no final text to parse")
        return None

    m = _AUDIT_TAG_RE.search(text)
    candidate = m.group(1) if m else None

    if candidate is None:
        # Fallback 1: strip ```json fences
        stripped = re.sub(r"^```(?:json)?\s*", "", text.strip())
        stripped = re.sub(r"\s*```\s*$", "", stripped)
        if stripped.startswith("{") and stripped.endswith("}"):
            candidate = stripped

    if candidate is None:
        # Fallback 2: first {...} block in text
        brace_match = re.search(r"\{[\s\S]*\}", text)
        if brace_match:
            candidate = brace_match.group(0)

    if candidate is None:
        errors.append("no JSON object found in final text")
        return None

    try:
        return json.loads(candidate)
    except json.JSONDecodeError as e:
        errors.append(f"final JSON parse failed: {e}")
        return None


# -----------------------------------------------------------------------------
# PUBLIC ENTRYPOINT — analog of audit_pipeline.run_audit()
# -----------------------------------------------------------------------------

def run_audit_agent(url: str, output_dir: str = "./audits/",
                     verbose: bool = False) -> Dict[str, Any]:
    """Run the agent loop, attach metadata, render artifacts, return result.

    Output shape matches the existing `run_audit()` from audit_pipeline.py so
    main.py and the rest of the FastAPI service work without changes.
    """
    audit_id = str(uuid.uuid4())
    started = time.time()
    out_dir = Path(output_dir).expanduser().resolve()
    out_dir.mkdir(parents=True, exist_ok=True)

    if verbose:
        print(f"[agent] starting audit {audit_id} for {url}", flush=True)

    loop_result = run_agent_loop(url, verbose=verbose,
                                  log_prefix=f'[{audit_id[:8]}] ')

    audit = loop_result.get("audit")

    domain = re.sub(r"^https?://", "", url).rstrip("/").split("/")[0]
    duration = round(time.time() - started, 1)

    # Build the wrapped result regardless of agent success
    if audit is None:
        # Agent failed to produce parseable output. Return error envelope.
        return {
            "audit_id": audit_id,
            "url": url,
            "domain": domain,
            "duration_seconds": duration,
            "error": "agent did not return valid audit JSON",
            "agent_errors": loop_result.get("errors", []),
            "agent_turns": loop_result.get("turns"),
            "agent_stop_reason": loop_result.get("stop_reason"),
            "raw_final_text_preview": loop_result.get("raw_final_text", "")[:1500],
            "tool_call_count": len(loop_result.get("tool_calls", [])),
            "input_tokens": loop_result.get("input_tokens"),
            "output_tokens": loop_result.get("output_tokens"),
        }

    # Inject our authoritative metadata into the agent's audit
    audit["audit_id"] = audit_id
    audit["url"] = url
    audit["domain"] = domain
    audit["date"] = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    audit["duration_seconds"] = duration

    md = audit.setdefault("metadata", {})
    md["version"] = md.get("version", "5.0-agent")
    md["model"] = MODEL
    md["tool_call_count"] = len(loop_result.get("tool_calls", []))
    md["agent_turns"] = loop_result.get("turns")
    md["agent_stop_reason"] = loop_result.get("stop_reason")
    md["input_tokens"] = loop_result.get("input_tokens")
    md["output_tokens"] = loop_result.get("output_tokens")
    md["agent_errors"] = loop_result.get("errors", [])

    # Render artifacts using the existing renderers from audit_pipeline.py
    # (they consume the same shape we produce).
    try:
        from audit_pipeline import render_markdown_report, render_pdf_summary
    except ImportError as e:
        audit["render_warning"] = f"renderers unavailable: {e}"
        render_markdown_report = None
        render_pdf_summary = None

    slug = domain.replace(".", "-")
    base_path = out_dir / f"{slug}-{audit_id[:8]}"

    json_path = base_path.with_suffix(".json")
    json_path.write_text(json.dumps(audit, indent=2, ensure_ascii=False, default=str))
    audit["json_path"] = str(json_path)

    if render_markdown_report:
        try:
            md_text = render_markdown_report(_render_compat(audit))
            md_path = base_path.with_suffix(".md")
            md_path.write_text(md_text)
            audit["md_path"] = str(md_path)
        except Exception as e:
            audit["md_render_error"] = f"{type(e).__name__}: {e}"
            audit["md_path"] = None
    else:
        audit["md_path"] = None

    if render_pdf_summary:
        try:
            pdf_path = render_pdf_summary(_render_compat(audit), base_path)
            audit["pdf_path"] = str(pdf_path) if pdf_path else None
        except Exception as e:
            audit["pdf_render_error"] = f"{type(e).__name__}: {e}"
            audit["pdf_path"] = None
    else:
        audit["pdf_path"] = None

    if verbose:
        print(f"[agent] complete in {duration}s, "
              f"{md['tool_call_count']} tool calls, "
              f"{md['input_tokens']}+{md['output_tokens']} tokens",
              flush=True)

    return audit


def _render_compat(audit: Dict[str, Any]) -> Dict[str, Any]:
    """Adapt the agent's audit shape to what render_markdown_report expects.

    The legacy renderer wants: scripts_output, brain_stats, classification,
    scoring, narrative, findings. The agent produces the same fields, but
    'scripts_output' is nested under bots_eye_view differently. Stitch them.
    """
    return {
        "audit_id": audit.get("audit_id"),
        "url": audit.get("url"),
        "domain": audit.get("domain"),
        "date": audit.get("date"),
        "duration_seconds": audit.get("duration_seconds"),
        "classification": audit.get("classification", {}),
        "scoring": audit.get("scoring", {}),
        "findings": audit.get("findings", []),
        "narrative": audit.get("narrative", {}),
        "scripts_output": {
            "bots_eye_view": audit.get("bots_eye_view", {}),
            "all_checks": {f["check_id"]: f for f in audit.get("findings", [])},
        },
        "brain_stats": audit.get("metadata", {}).get("brain_stats", {}),
    }


# -----------------------------------------------------------------------------
# CLI
# -----------------------------------------------------------------------------

if __name__ == "__main__":
    import argparse
    p = argparse.ArgumentParser(description="Run the agent-mode audit pipeline.")
    p.add_argument("url")
    p.add_argument("--output", "-o", default="./audits/")
    p.add_argument("--verbose", "-v", action="store_true")
    args = p.parse_args()

    result = run_audit_agent(args.url, args.output, verbose=args.verbose)
    print(json.dumps({k: v for k, v in result.items()
                      if k not in ("findings", "scripts_output", "bots_eye_view")},
                     indent=2, ensure_ascii=False, default=str)[:5000])
    if result.get("error"):
        sys.exit(1)
