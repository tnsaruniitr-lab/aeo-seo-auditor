#!/usr/bin/env python3
"""
bev_analyze_v2.py — Fixed Bot's Eye View analyzer.

Replaces the original scripts/_bev_analyze.py. Fixes:

1. FAQ false-positive gate in `faq_visible_count`.
   Original Pattern 1 counted every <details>/<summary> as an FAQ pair.
   Country expanders, menu items, disclosure toggles all counted as FAQs.
   Fix: require the summary text to look like a question — contain '?',
   start with a question word (how/what/when/where/why/which/who/can/do/
   does/is/are/will/should), or include "FAQ" / "Q:" label.

2. New 'ssr_shell_js_hidden_content' classification.
   Catches the pattern where a thin SSR modal/gate is served by the
   server while the real landing page lives in a JS bundle that bots
   cannot execute. Heuristic signals: <200 visible words + UI-action H1
   (e.g. "Select Language") + rich JS bundle (>40KB with Next.js
   streaming markers).

3. Uses html.parser (stdlib) for visible text extraction instead of
   regex-based tag stripping. More accurate for malformed HTML,
   <style>/<script>/<noscript> handling, CDATA.

Interface preserved: same function names and return signatures as
the original _bev_analyze.py for drop-in replacement.

Dependencies: python3 (3.8+). stdlib only.
"""

import html as html_lib
import html.parser
import json
import re
import sys
from typing import Dict, List, Optional, Tuple


# ----------------------------------------------------------------------
# HTML → visible text (stdlib html.parser, not regex)
# ----------------------------------------------------------------------

class _VisibleTextExtractor(html.parser.HTMLParser):
    """Collects text from an HTML doc, skipping script/style/noscript/template."""
    SKIP_TAGS = {'script', 'style', 'noscript', 'template', 'head'}

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self._parts: List[str] = []
        self._skip_depth = 0

    def handle_starttag(self, tag, attrs):
        if tag.lower() in self.SKIP_TAGS:
            self._skip_depth += 1

    def handle_endtag(self, tag):
        if tag.lower() in self.SKIP_TAGS and self._skip_depth > 0:
            self._skip_depth -= 1

    def handle_data(self, data):
        if self._skip_depth == 0:
            self._parts.append(data)

    def get_text(self) -> str:
        return ' '.join(self._parts)


def visible_text(html_str: str, max_chars: int = 50_000) -> str:
    """Extract visible text via stdlib html.parser."""
    if not html_str:
        return ''
    ex = _VisibleTextExtractor()
    try:
        ex.feed(html_str)
    except Exception:
        # If parser chokes, fall back to brute-force tag strip so we never
        # crash the whole audit.
        stripped = re.sub(r'<script[^>]*>.*?</script>', ' ', html_str, flags=re.DOTALL | re.IGNORECASE)
        stripped = re.sub(r'<style[^>]*>.*?</style>', ' ', stripped, flags=re.DOTALL | re.IGNORECASE)
        stripped = re.sub(r'<[^>]+>', ' ', stripped)
        stripped = html_lib.unescape(stripped)
        return re.sub(r'\s+', ' ', stripped).strip()[:max_chars]
    text = ex.get_text()
    text = re.sub(r'\s+', ' ', text).strip()
    return text[:max_chars]


def visible_word_count(html_str: str) -> int:
    """Count visible (human-readable) words in an HTML document."""
    text = visible_text(html_str)
    return len([w for w in text.split() if w.strip()])


# ----------------------------------------------------------------------
# FAQ detection with question-intent gate
# ----------------------------------------------------------------------

_QUESTION_WORDS = (
    'how ', 'what ', 'when ', 'where ', 'why ', 'which ', 'who ',
    'can ', 'could ', 'do ', 'does ', 'did ',
    'is ', 'are ', 'was ', 'were ',
    'will ', 'would ', 'should ', 'shall ', 'may ', 'might ',
    'have ', 'has ', 'had ',
)


def looks_like_question(text: str) -> bool:
    """Heuristic: does this text look like a user-facing question?"""
    if not text:
        return False
    t = text.strip().lower()
    if '?' in t:
        return True
    # "FAQ" or "Q:" labels
    if t.startswith(('faq', 'q:', 'question')):
        return True
    # Starts with a question word
    if any(t.startswith(kw) for kw in _QUESTION_WORDS):
        return True
    return False


def faq_visible_count(html_str: str) -> Tuple[int, str]:
    """
    Count visible FAQ pairs using multiple detection patterns with
    question-intent gating.

    Returns (count, detection_method).
    """
    if not html_str:
        return 0, 'empty_html'

    # Pattern 1: <details><summary> WITH question-like summary text
    summaries = re.findall(
        r'<summary[^>]*>(.*?)</summary>', html_str, re.IGNORECASE | re.DOTALL
    )
    q_summaries = []
    for s in summaries:
        text = re.sub(r'<[^>]+>', ' ', s).strip()
        text = html_lib.unescape(text)
        if looks_like_question(text):
            q_summaries.append(s)
    if q_summaries:
        return len(q_summaries), 'details_summary_question'

    # Pattern 2: <dl><dt><dd> — require at least 3 pairs to look FAQ-like,
    # AND at least half of the <dt> texts must be questions.
    dts = re.findall(r'<dt[^>]*>(.*?)</dt>', html_str, re.IGNORECASE | re.DOTALL)
    dds = re.findall(r'<dd[^>]*>', html_str, re.IGNORECASE)
    if len(dts) >= 3 and len(dds) >= 3:
        q_dts = [dt for dt in dts if looks_like_question(
            re.sub(r'<[^>]+>', ' ', html_lib.unescape(dt))
        )]
        if len(q_dts) >= len(dts) / 2:
            return min(len(q_dts), len(dds)), 'dl_dt_dd_question'

    # Pattern 3: data-slot="accordion-item" (shadcn/ui) — treat as FAQ
    # since explicit accordion semantic
    accordion = re.findall(
        r'data-slot=["\']accordion-item["\']', html_str, re.IGNORECASE
    )
    if accordion:
        return len(accordion), 'data_slot_accordion'

    # Pattern 4: class="*accordion-item*" or "*faq-item*" / "*faq-entry*"
    class_items = re.findall(
        r'class=["\'][^"\']*(?:accordion-item|faq-item|faq-entry|faq-question)',
        html_str, re.IGNORECASE
    )
    if class_items:
        return len(class_items), 'class_accordion_item'

    # Pattern 5: H3 tags ending in ? — strong signal of FAQ headings
    h3_qs = re.findall(
        r'<h3[^>]*>\s*[^<]*\?\s*</h3>', html_str, re.IGNORECASE
    )
    if h3_qs and len(h3_qs) >= 3:
        return len(h3_qs), 'h3_question_headings'

    # Pattern 6: aria-expanded attributes — only if 3+ AND the labels
    # adjacent look like questions (too noisy otherwise, disabled for now)

    return 0, 'none_detected'


# ----------------------------------------------------------------------
# FAQ schema count (unchanged logic; safe)
# ----------------------------------------------------------------------

def faq_schema_count(html_str: str) -> int:
    """Count FAQ pairs in FAQPage JSON-LD, if present."""
    blocks = re.findall(
        r'<script[^>]*type=["\']application/ld\+json["\'][^>]*>(.*?)</script>',
        html_str, re.IGNORECASE | re.DOTALL
    )
    for b in blocks:
        try:
            data = json.loads(b.strip())
        except json.JSONDecodeError:
            continue
        items = data if isinstance(data, list) else [data]
        for item in items:
            if not isinstance(item, dict):
                continue
            if item.get('@type') == 'FAQPage':
                me = item.get('mainEntity', [])
                if isinstance(me, list):
                    return len(me)
            graph = item.get('@graph', [])
            if isinstance(graph, list):
                for g in graph:
                    if isinstance(g, dict) and g.get('@type') == 'FAQPage':
                        me = g.get('mainEntity', [])
                        if isinstance(me, list):
                            return len(me)
    return 0


# ----------------------------------------------------------------------
# SPA signal + classification
# ----------------------------------------------------------------------

def detect_spa_signals(html_str: str) -> List[str]:
    """Return list of SPA framework hints detected in raw HTML."""
    signals = []
    if re.search(r'<app-root', html_str, re.IGNORECASE):
        signals.append('angular_app_root')
    if re.search(r'<div[^>]*id=["\']__next["\']', html_str, re.IGNORECASE) \
            or '__NEXT_DATA__' in html_str \
            or 'self.__next_f' in html_str:
        signals.append('nextjs')
    if re.search(r'<div[^>]*id=["\']root["\']', html_str, re.IGNORECASE) \
            and 'react' in html_str.lower():
        signals.append('react_root')
    if ('id="app"' in html_str or "id='app'" in html_str) \
            and 'vue' in html_str.lower():
        signals.append('vue_app')
    if re.search(r'<div[^>]*id=["\']__nuxt["\']', html_str, re.IGNORECASE):
        signals.append('nuxt')
    return signals


_UI_ACTION_H1_KEYWORDS = (
    'select', 'choose', 'pick', 'continue', 'enter your',
    'get started', 'sign in', 'log in', 'welcome',
)


def classify_ssr(
    visible_words: int,
    same_as_404: bool,
    spa_signals: List[str],
    h1_first: Optional[str] = None,
    html_snippet: Optional[str] = None,
) -> str:
    """
    Deterministic classification based on signals.

    Returns one of:
      - 'spa_no_ssr'                 — Identical shell for every URL. Dark to AI.
      - 'ssr_shell_js_hidden_content' — SSR works but only a modal/gate is rendered;
                                         real content is in the JS bundle. (NEW)
      - 'js_dependent'               — Content exists but <200 words. AI sees little.
      - 'minimal_content'            — <200 words, genuinely thin page.
      - 'partial_ssr'                — 200-500 words.
      - 'fully_accessible'           — >500 words of real content in raw HTML.
    """
    if same_as_404:
        return 'spa_no_ssr'

    # NEW: detect SSR-shell-with-JS-hidden-content
    ui_action_h1 = False
    if h1_first:
        h1_lower = h1_first.lower()
        ui_action_h1 = any(kw in h1_lower for kw in _UI_ACTION_H1_KEYWORDS)

    has_next_streaming = bool(
        html_snippet and 'self.__next_f.push' in html_snippet
    )
    rich_bundle = has_next_streaming and html_snippet and len(html_snippet) > 40_000
    if visible_words < 200 and ui_action_h1 and rich_bundle:
        return 'ssr_shell_js_hidden_content'

    if visible_words < 200:
        if spa_signals:
            return 'js_dependent'
        return 'minimal_content'
    if visible_words < 500:
        return 'partial_ssr'
    return 'fully_accessible'


# ----------------------------------------------------------------------
# Helpers exposed for testing (and backwards-compatibility with the
# existing bots_eye_view.sh wrapper)
# ----------------------------------------------------------------------

def safe_read(path: str) -> str:
    """Read file, return '' if missing/unreadable. Never raises."""
    try:
        with open(path, encoding='utf-8', errors='replace') as f:
            return f.read()
    except (FileNotFoundError, PermissionError, OSError):
        return ''


def parse_curl_result(result_str: str) -> Dict:
    """Parse 'HTTP_CODE SIZE TTFB' string from curl -w output."""
    parts = result_str.strip().split()
    try:
        return {
            'http_code': int(parts[0]) if len(parts) > 0 else 0,
            'size_bytes': int(parts[1]) if len(parts) > 1 else 0,
            'ttfb_seconds': float(parts[2]) if len(parts) > 2 else 0.0,
        }
    except (ValueError, IndexError):
        return {'http_code': 0, 'size_bytes': 0, 'ttfb_seconds': 0.0}


# ----------------------------------------------------------------------
# Self-test when run directly
# ----------------------------------------------------------------------

def extract_first_h1(html_str: str) -> Optional[str]:
    """Return the text inside the first <h1>, or None."""
    if not html_str:
        return None
    m = re.search(r'<h1[^>]*>(.*?)</h1>', html_str, re.IGNORECASE | re.DOTALL)
    if not m:
        return None
    text = re.sub(r'<[^>]+>', ' ', m.group(1))
    text = html_lib.unescape(text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text or None


def _normalize_for_equality(html_str: str) -> str:
    """Strip volatile tokens (nonces, timestamps) for content-equality comparison."""
    if not html_str:
        return ''
    s = re.sub(r'nonce=["\'][^"\']+["\']', '', html_str, flags=re.IGNORECASE)
    s = re.sub(r'csrf[_-]?token["\']?\s*[:=]\s*["\'][^"\']+["\']', '', s, flags=re.IGNORECASE)
    s = re.sub(r'\d{10,}', '', s)  # long numeric IDs / unix timestamps
    s = re.sub(r'\s+', ' ', s).strip()
    return s


def analyze_probe(html_str: str, curl_result: str) -> Dict:
    """Analyze a single UA probe. Returns dict of all derived signals."""
    curl = parse_curl_result(curl_result)
    visible = visible_text(html_str)
    wc = len([w for w in visible.split() if w.strip()])
    faq_vc, faq_method = faq_visible_count(html_str)
    return {
        'http_code': curl['http_code'],
        'size_bytes': curl['size_bytes'],
        'ttfb_seconds': round(curl['ttfb_seconds'], 3),
        'visible_words': wc,
        'faq_visible': {'count': faq_vc, 'method': faq_method},
        'faq_schema': faq_schema_count(html_str),
        'spa_signals': detect_spa_signals(html_str),
        'h1_first': extract_first_h1(html_str),
    }


def _run_cli(payload: Dict) -> Dict:
    """
    Deterministic orchestrator consumed by bots_eye_view.sh.

    Expected payload shape:
      {
        "url": "...",
        "probe_url": "...",
        "probes": {
          "default":   {"html_file": "...", "curl_result": "CODE SIZE TTFB"},
          "gbot":      {...},
          "gpt":       {...},
          "perp":      {...},
          "claude":    {...},
          "not_found": {...}
        }
      }
    """
    url = payload.get('url') or ''
    probe_url = payload.get('probe_url') or ''
    probes_in = payload.get('probes') or {}

    per_probe: Dict[str, Dict] = {}
    html_by_probe: Dict[str, str] = {}
    for name, entry in probes_in.items():
        if not isinstance(entry, dict):
            continue
        html_str = safe_read(entry.get('html_file') or '')
        html_by_probe[name] = html_str
        per_probe[name] = analyze_probe(html_str, entry.get('curl_result') or '')

    default_html = html_by_probe.get('default', '')
    nf_html = html_by_probe.get('not_found', '')

    # same-as-404: default page body indistinguishable from a guaranteed 404.
    same_as_404 = False
    if default_html and nf_html:
        same_as_404 = (
            _normalize_for_equality(default_html) == _normalize_for_equality(nf_html)
            or (
                visible_word_count(default_html) == visible_word_count(nf_html) > 0
                and visible_text(default_html) == visible_text(nf_html)
            )
        )

    # Cloaking: flag if any bot UA's visible-word count differs from default
    # by > 20% and > 50 words. Conservative threshold to avoid noise.
    default_wc = per_probe.get('default', {}).get('visible_words', 0)
    cloaking_deltas: List[Dict] = []
    cloaking_detected = False
    for name in ('gbot', 'gpt', 'perp', 'claude'):
        probe_wc = per_probe.get(name, {}).get('visible_words', 0)
        if default_wc == 0 and probe_wc == 0:
            continue
        delta = probe_wc - default_wc
        rel = (abs(delta) / default_wc) if default_wc else 1.0
        entry = {'probe': name, 'visible_words': probe_wc, 'delta_vs_default': delta}
        if abs(delta) > 50 and rel > 0.20:
            entry['flagged'] = True
            cloaking_detected = True
        cloaking_deltas.append(entry)

    classification = classify_ssr(
        visible_words=default_wc,
        same_as_404=same_as_404,
        spa_signals=per_probe.get('default', {}).get('spa_signals', []),
        h1_first=per_probe.get('default', {}).get('h1_first'),
        html_snippet=default_html,
    )

    d = per_probe.get('default', {})
    visible_faq = d.get('faq_visible', {}).get('count', 0)
    schema_faq = d.get('faq_schema', 0)
    if visible_faq == 0 and schema_faq == 0:
        faq_integrity = 'na'
    elif visible_faq == schema_faq:
        faq_integrity = 'ok'
    else:
        faq_integrity = 'mismatch'

    return {
        'url': url,
        'probe_url': probe_url,
        'probes': per_probe,
        'same_as_404': same_as_404,
        'cloaking_detected': cloaking_detected,
        'cloaking_deltas': cloaking_deltas,
        'classification': classification,
        'summary': {
            'visible_words_default': default_wc,
            'spa_signals': per_probe.get('default', {}).get('spa_signals', []),
            'faq_visible': visible_faq,
            'faq_schema': schema_faq,
            'faq_integrity': faq_integrity,
        },
    }


def _selftest():
    """Quick self-check: run against the bundled fixture files."""
    import os
    here = os.path.dirname(os.path.abspath(__file__))
    fix_dir = None
    for candidate in (
        os.path.join(here, '..', 'tests', 'fixtures'),
        os.path.join(here, '..', '..', 'tests', 'fixtures'),
    ):
        if os.path.isdir(candidate):
            fix_dir = candidate
            break
    if fix_dir is None:
        print('SKIP selftest — fixtures directory not found')
        sys.exit(0)

    tests = [
        ('country_accordion_not_faq.html', 0, 'details_summary_question or none_detected'),
        ('real_faq_accordion.html', 6, 'details_summary_question'),
        ('ssr_full_landing.html', None, 'details_summary_question'),
    ]

    all_ok = True
    for fname, expected_count, _ in tests:
        path = os.path.join(fix_dir, fname)
        if not os.path.exists(path):
            print(f'SKIP {fname} — fixture not found')
            continue
        with open(path) as f:
            html = f.read()
        count, method = faq_visible_count(html)
        wc = visible_word_count(html)
        print(f'{fname}: faq_count={count} method={method} visible_words={wc}')
        if expected_count is not None and count != expected_count:
            print(f'  ✗ expected {expected_count}, got {count}')
            all_ok = False
        else:
            print(f'  ✓ ok')

    sys.exit(0 if all_ok else 1)


def main():
    """
    CLI entrypoint used by bots_eye_view.sh.

    Reads a JSON payload from stdin describing the probes and emits a JSON
    result on stdout. See `_run_cli` for payload shape.
    """
    if len(sys.argv) > 1 and sys.argv[1] == '--selftest':
        _selftest()
        return
    if len(sys.argv) > 1 and sys.argv[1] == '--help':
        print('bev_analyze: pipe a JSON payload on stdin, receive JSON on stdout.')
        print('  --selftest   run fixture-based self-check')
        return

    raw = sys.stdin.read()
    if not raw.strip():
        print(json.dumps({'error': 'empty stdin; expected JSON payload'}))
        sys.exit(2)
    try:
        payload = json.loads(raw)
    except json.JSONDecodeError as e:
        print(json.dumps({'error': f'invalid JSON on stdin: {e}'}))
        sys.exit(2)

    result = _run_cli(payload)
    print(json.dumps(result, indent=2, ensure_ascii=False))


if __name__ == '__main__':
    main()
