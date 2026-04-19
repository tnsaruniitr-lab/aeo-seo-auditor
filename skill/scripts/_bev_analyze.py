#!/usr/bin/env python3
"""
_bev_analyze.py — Deterministic HTML analysis for bots_eye_view.sh

Reads 5 fetched HTML files (default UA + 4 bot UAs + 404 probe) and emits
a single JSON object describing what AI crawlers see.

Invoked by bots_eye_view.sh. Not intended to be called directly.

Determinism guarantees:
  - Same input HTML → identical output JSON
  - Only network-related fields (TTFB) vary across runs
  - All content-derived fields (title, H1, counts, classification) are stable
"""

import sys
import re
import json
import os
from pathlib import Path


def safe_read(path):
    """Read a file; return empty string if missing or empty."""
    try:
        p = Path(path)
        if p.exists() and p.stat().st_size > 0:
            return p.read_text(encoding='utf-8', errors='replace')
    except Exception:
        pass
    return ''


def extract_title(html):
    m = re.search(r'<title[^>]*>([^<]*)</title>', html, re.IGNORECASE)
    if m:
        return re.sub(r'\s+', ' ', m.group(1)).strip()
    return None


def extract_h1_texts(html):
    """Return list of H1 text contents (stripped)."""
    results = []
    for m in re.finditer(r'<h1[^>]*>(.*?)</h1>', html, re.IGNORECASE | re.DOTALL):
        inner = re.sub(r'<[^>]*>', ' ', m.group(1))
        inner = re.sub(r'&[a-zA-Z#0-9]+;', ' ', inner)
        inner = re.sub(r'\s+', ' ', inner).strip()
        if inner:
            results.append(inner)
    return results


def count_tag(html, tag):
    """Count opening occurrences of a specific tag."""
    return len(re.findall(rf'<{tag}(?:\s|>)', html, re.IGNORECASE))


def extract_meta(html, name):
    """Extract <meta name="X" content="Y"> or <meta property="X" content="Y">"""
    m = re.search(
        rf'<meta[^>]*(?:name|property)=["\']{re.escape(name)}["\'][^>]*content=["\']([^"\']*)',
        html, re.IGNORECASE
    )
    return m.group(1) if m else None


def extract_canonical(html):
    m = re.search(
        r'<link[^>]*rel=["\']canonical["\'][^>]*href=["\']([^"\']*)',
        html, re.IGNORECASE
    )
    return m.group(1) if m else None


def count_schema_blocks(html):
    """Count JSON-LD script blocks."""
    return len(re.findall(
        r'<script[^>]*type=["\']application/ld\+json["\']',
        html, re.IGNORECASE
    ))


def visible_word_count(html):
    """Strip scripts, styles, and tags, then count words."""
    if not html:
        return 0
    c = re.sub(r'<script[^>]*>.*?</script>', ' ', html, flags=re.DOTALL | re.IGNORECASE)
    c = re.sub(r'<style[^>]*>.*?</style>', ' ', c, flags=re.DOTALL | re.IGNORECASE)
    c = re.sub(r'<!--.*?-->', ' ', c, flags=re.DOTALL)
    t = re.sub(r'<[^>]+>', ' ', c)
    t = re.sub(r'&[a-zA-Z#0-9]+;', ' ', t)
    t = re.sub(r'\s+', ' ', t).strip()
    return len(t.split())


def visible_text_preview(html, max_chars=400):
    """First N chars of visible text."""
    if not html:
        return ''
    c = re.sub(r'<script[^>]*>.*?</script>', ' ', html, flags=re.DOTALL | re.IGNORECASE)
    c = re.sub(r'<style[^>]*>.*?</style>', ' ', c, flags=re.DOTALL | re.IGNORECASE)
    c = re.sub(r'<!--.*?-->', ' ', c, flags=re.DOTALL)
    t = re.sub(r'<[^>]+>', ' ', c)
    t = re.sub(r'&[a-zA-Z#0-9]+;', ' ', t)
    t = re.sub(r'\s+', ' ', t).strip()
    return t[:max_chars]


def faq_visible_count(html):
    """
    Count visible FAQ pairs using MULTIPLE detection patterns.
    This is the fix for the Valeo miss: custom React accordions
    don't use <details>/<summary>, so we check several patterns.

    Returns (count, detection_method).
    """
    # Pattern 1: <details><summary> (semantic HTML5 disclosure)
    details = re.findall(r'<details[^>]*>', html, re.IGNORECASE)
    summaries = re.findall(r'<summary[^>]*>', html, re.IGNORECASE)
    if details and summaries and min(len(details), len(summaries)) > 0:
        return min(len(details), len(summaries)), 'details_summary'

    # Pattern 2: <dl><dt><dd> (definition list — common for FAQ on older sites)
    dts = re.findall(r'<dt[^>]*>', html, re.IGNORECASE)
    dds = re.findall(r'<dd[^>]*>', html, re.IGNORECASE)
    if dts and dds and min(len(dts), len(dds)) >= 3:
        return min(len(dts), len(dds)), 'dl_dt_dd'

    # Pattern 3: data-slot="accordion-item" (shadcn/ui + similar)
    accordion_items = re.findall(
        r'data-slot=["\']accordion-item["\']', html, re.IGNORECASE
    )
    if accordion_items:
        return len(accordion_items), 'data_slot_accordion'

    # Pattern 4: class name contains "accordion-item" or "faq-item"
    class_items = re.findall(
        r'class=["\'][^"\']*(?:accordion-item|faq-item|faq-entry)', html, re.IGNORECASE
    )
    if class_items:
        return len(class_items), 'class_accordion_item'

    # Pattern 5: aria-expanded attributes (sometimes one per FAQ toggle)
    aria_exp = re.findall(r'aria-expanded=', html, re.IGNORECASE)
    # Need at least 3 to look like a FAQ list rather than a menu
    if len(aria_exp) >= 3:
        return len(aria_exp), 'aria_expanded_heuristic'

    # Pattern 6: H3 tags ending in ? (question headings, no accordion markup)
    h3_qs = re.findall(r'<h3[^>]*>\s*[^<]*\?\s*</h3>', html, re.IGNORECASE)
    if h3_qs and len(h3_qs) >= 3:
        return len(h3_qs), 'h3_question_headings'

    return 0, 'none_detected'


def faq_schema_count(html):
    """Count FAQ pairs in FAQPage JSON-LD, if present."""
    blocks = re.findall(
        r'<script[^>]*type=["\']application/ld\+json["\'][^>]*>(.*?)</script>',
        html, re.IGNORECASE | re.DOTALL
    )
    for b in blocks:
        try:
            data = json.loads(b.strip())
        except json.JSONDecodeError:
            continue
        # Could be a dict or array
        items = data if isinstance(data, list) else [data]
        for item in items:
            if not isinstance(item, dict):
                continue
            if item.get('@type') == 'FAQPage':
                me = item.get('mainEntity', [])
                if isinstance(me, list):
                    return len(me)
            # Also check @graph
            graph = item.get('@graph', [])
            if isinstance(graph, list):
                for g in graph:
                    if isinstance(g, dict) and g.get('@type') == 'FAQPage':
                        me = g.get('mainEntity', [])
                        if isinstance(me, list):
                            return len(me)
    return 0


def detect_spa_signals(html):
    """Return list of SPA framework hints detected."""
    signals = []
    if re.search(r'<app-root', html, re.IGNORECASE):
        signals.append('angular_app_root')
    if re.search(r'<div[^>]*id=["\']__next["\']', html, re.IGNORECASE) or '__NEXT_DATA__' in html:
        signals.append('nextjs')
    if re.search(r'<div[^>]*id=["\']root["\']', html, re.IGNORECASE) and 'react' in html.lower():
        signals.append('react_root')
    if 'id="app"' in html or "id='app'" in html:
        if 'vue' in html.lower():
            signals.append('vue_app')
    return signals


def classify_ssr(visible_words, same_as_404, spa_signals):
    """
    Deterministic classification based on facts.

    Returns one of:
      - 'spa_no_ssr'         — Site serves identical shell for every URL. Dark to AI.
      - 'js_dependent'       — Content exists but <200 words in raw HTML. AI sees almost nothing.
      - 'partial_ssr'        — 200-500 words. Some content visible, some behind JS.
      - 'fully_accessible'   — >500 words of real content in raw HTML.
    """
    if same_as_404:
        return 'spa_no_ssr'
    if visible_words < 200:
        if spa_signals:
            return 'js_dependent'
        return 'minimal_content'  # Not necessarily SPA, just thin
    if visible_words < 500:
        return 'partial_ssr'
    return 'fully_accessible'


def parse_curl_result(result_str):
    """Parse 'HTTP_CODE SIZE TTFB' string from curl -w."""
    parts = result_str.strip().split()
    try:
        return {
            'http_code': int(parts[0]) if len(parts) > 0 else 0,
            'size_bytes': int(parts[1]) if len(parts) > 1 else 0,
            'ttfb_seconds': float(parts[2]) if len(parts) > 2 else 0.0,
        }
    except (ValueError, IndexError):
        return {'http_code': 0, 'size_bytes': 0, 'ttfb_seconds': 0.0}


def main():
    args = sys.argv[1:]
    # Expected: url ne_url default_html default_result gbot_html gbot_result ...
    if len(args) < 14:
        print(json.dumps({'error': 'invalid argument count', 'argc': len(args)}))
        sys.exit(1)

    url = args[0]
    ne_url = args[1]
    default_html = safe_read(args[2])
    default_res = parse_curl_result(args[3])
    gbot_html = safe_read(args[4])
    gbot_res = parse_curl_result(args[5])
    gpt_html = safe_read(args[6])
    gpt_res = parse_curl_result(args[7])
    perp_html = safe_read(args[8])
    perp_res = parse_curl_result(args[9])
    claude_html = safe_read(args[10])
    claude_res = parse_curl_result(args[11])
    ne_html = safe_read(args[12])
    ne_res = parse_curl_result(args[13])

    # Parse default (normal UA) response for content analysis
    title = extract_title(default_html)
    h1_texts = extract_h1_texts(default_html)
    canonical = extract_canonical(default_html)
    meta_desc = extract_meta(default_html, 'description')
    meta_robots = extract_meta(default_html, 'robots')
    og_title = extract_meta(default_html, 'og:title')
    og_type = extract_meta(default_html, 'og:type')

    visible_words = visible_word_count(default_html)
    preview = visible_text_preview(default_html, 300)
    schema_blocks = count_schema_blocks(default_html)
    faq_visible, faq_method = faq_visible_count(default_html)
    faq_schema = faq_schema_count(default_html)
    spa_signals = detect_spa_signals(default_html)

    h1_count = count_tag(default_html, 'h1')
    h2_count = count_tag(default_html, 'h2')
    h3_count = count_tag(default_html, 'h3')

    # Cloaking / bot-shell detection
    default_size = default_res['size_bytes']
    gbot_size = gbot_res['size_bytes']
    gpt_size = gpt_res['size_bytes']
    perp_size = perp_res['size_bytes']
    claude_size = claude_res['size_bytes']
    ne_size = ne_res['size_bytes']

    # Same bytes for 404 test (critical SPA-no-SSR detector)
    same_as_404 = (
        default_html != ''
        and ne_html != ''
        and default_html == ne_html
    )

    # Cloaking detection: is any bot UA getting materially different bytes?
    # Use a 5% tolerance since dynamic insertions (timestamps, random IDs) are common
    sizes = [default_size, gbot_size, gpt_size, perp_size, claude_size]
    sizes_nonzero = [s for s in sizes if s > 0]
    cloaking_detected = False
    cloaking_detail = None
    if len(sizes_nonzero) >= 2:
        min_size = min(sizes_nonzero)
        max_size = max(sizes_nonzero)
        if min_size > 0 and (max_size - min_size) / min_size > 0.05:
            cloaking_detected = True
            cloaking_detail = f'default={default_size} gbot={gbot_size} gpt={gpt_size} perp={perp_size} claude={claude_size}'

    # Classification
    classification = classify_ssr(visible_words, same_as_404, spa_signals)

    # FAQ integrity
    faq_integrity = 'no_faq'
    if faq_visible == 0 and faq_schema == 0:
        faq_integrity = 'no_faq'
    elif faq_visible == faq_schema:
        faq_integrity = 'match'
    elif faq_visible > faq_schema:
        faq_integrity = f'visible_exceeds_schema ({faq_visible} visible vs {faq_schema} in schema)'
    else:
        faq_integrity = f'schema_exceeds_visible_orphan ({faq_schema} in schema vs {faq_visible} visible)'

    # Assemble output
    out = {
        'url': url,
        'probe_404_url': ne_url,
        'classification': classification,
        'summary': {
            'can_ai_crawlers_extract_content': classification in ('partial_ssr', 'fully_accessible'),
            'same_html_as_404_url': same_as_404,
            'cloaking_detected': cloaking_detected,
            'spa_framework_signals': spa_signals,
            'critical_issues': []  # populated below
        },
        'page_identity': {
            'title': title,
            'h1_first': h1_texts[0] if h1_texts else None,
            'h1_count': h1_count,
            'h1_all_texts': h1_texts,
            'h2_count': h2_count,
            'h3_count': h3_count,
            'canonical_tag': canonical,
            'meta_description': meta_desc,
            'meta_robots': meta_robots,
            'og_title': og_title,
            'og_type': og_type,
        },
        'content_visible_to_bots': {
            'visible_word_count': visible_words,
            'visible_text_preview': preview,
            'schema_block_count': schema_blocks,
            'faq_visible_pairs': faq_visible,
            'faq_visible_detection_method': faq_method,
            'faq_schema_pairs': faq_schema,
            'faq_integrity': faq_integrity,
        },
        'response_per_bot': {
            'default_ua': {'http_code': default_res['http_code'], 'size_bytes': default_size, 'ttfb_seconds': default_res['ttfb_seconds']},
            'googlebot': {'http_code': gbot_res['http_code'], 'size_bytes': gbot_size, 'ttfb_seconds': gbot_res['ttfb_seconds']},
            'gptbot': {'http_code': gpt_res['http_code'], 'size_bytes': gpt_size, 'ttfb_seconds': gpt_res['ttfb_seconds']},
            'perplexitybot': {'http_code': perp_res['http_code'], 'size_bytes': perp_size, 'ttfb_seconds': perp_res['ttfb_seconds']},
            'claudebot': {'http_code': claude_res['http_code'], 'size_bytes': claude_size, 'ttfb_seconds': claude_res['ttfb_seconds']},
            'probe_404': {'http_code': ne_res['http_code'], 'size_bytes': ne_size, 'ttfb_seconds': ne_res['ttfb_seconds']},
        },
        'cloaking_detail': cloaking_detail,
    }

    # Populate critical_issues
    ci = out['summary']['critical_issues']
    if same_as_404:
        ci.append('SAME_HTML_AS_404 — server returns identical bytes for this URL and a nonexistent URL. Site is likely a client-side-rendered SPA with no SSR. AI crawlers receive zero unique content.')
    if visible_words < 200 and not same_as_404:
        ci.append(f'LOW_VISIBLE_CONTENT — only {visible_words} words in raw HTML (threshold: 200). AI crawlers see minimal content.')
    if cloaking_detected:
        ci.append(f'POSSIBLE_CLOAKING — response sizes differ across user-agents: {cloaking_detail}')
    if not title or title.strip() == '':
        ci.append('NO_TITLE — <title> tag missing or empty.')
    if h1_count == 0:
        ci.append('NO_H1 — zero <h1> tags in raw HTML.')
    elif h1_count > 1:
        ci.append(f'MULTIPLE_H1 — {h1_count} <h1> tags found.')
    if schema_blocks == 0:
        ci.append('NO_SCHEMA — zero JSON-LD schema blocks.')
    if faq_integrity.startswith('schema_exceeds_visible') or faq_integrity.startswith('visible_exceeds_schema'):
        ci.append(f'FAQ_MISMATCH — {faq_integrity}')

    print(json.dumps(out, indent=2, ensure_ascii=False))


if __name__ == '__main__':
    main()
