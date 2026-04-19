#!/usr/bin/env python3
"""
deterministic_checks.py — Phase 2 targeted deterministic checks

The 8 checks below are the ones where Claude produced wrong answers in past audits.
Each is a pure function: same HTML input → same output. No LLM in the loop.

Usage:
  bash scripts/run_all.sh <URL>     (invoked via the orchestrator)
  python3 scripts/deterministic_checks.py <URL>    (standalone)

Output: JSON to stdout with results for all 8 checks.

Checks implemented:
  D9.  faqpage_schema_vs_visible_match    — Catches the Valeo-style mismatch (Claude missed this with bad grep)
  A7b. h1_nested_in_heading_invalid       — Catches H1 inside H2 (Valeo weight loss)
  J2.  brand_name_consistency             — Flags mixed casing / character substitution (Weg0vy vs Wegovy)
  A4b. canonical_redirect_chain           — Flags canonical pointing to a redirected URL (Valeo trailing slash)
  B1.  ttfb_median_5_samples              — 5-sample TTFB instead of 1 (Valeo variance problem)
  D4.  schema_id_coverage                 — Every schema entity should have @id
  C12b. date_modified_is_stale            — Flags dateModified that hasn't changed despite other edits (AnswerMonk stale stamp)
  A2b. title_uniqueness_sample            — Samples 3 URLs from sitemap, checks titles differ (catches SPA placeholder titles)

Each check returns:
  {
    "status": "pass" | "fail" | "warn" | "na",
    "evidence": "<exact bytes or measurement>",
    "detail": { ... structured data for the narrative report ... }
  }
"""

import sys
import re
import json
import os
import subprocess
import time
import urllib.request
import urllib.parse
from urllib.error import URLError, HTTPError

# Share the question-intent-gated FAQ detector with the BEV layer so Phase 2
# counts the same thing Phase 1 does. Prior code had a duplicate pattern list
# that counted every <details>/<summary> pair, including country accordions.
_HERE = os.path.dirname(os.path.abspath(__file__))
if _HERE not in sys.path:
    sys.path.insert(0, _HERE)
from _bev_analyze import faq_visible_count as _faq_visible_count  # noqa: E402
# Hreflang detector that also walks Next.js streaming chunks (RSC payloads).
# Prior to wiring this in, App Router sites with locales declared inside
# self.__next_f.push(...) chunks reported zero hreflang in the audit output.
from deterministic_checks_extras import detect_hreflang as _detect_hreflang  # noqa: E402


# ──────────────────────────────────────────────────────────────────────────
# Utilities
# ──────────────────────────────────────────────────────────────────────────

USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (AuditBot)'


def fetch(url, timeout=15, allow_redirects=True, user_agent=USER_AGENT):
    """Fetch URL with controlled behavior. Returns (html, final_url, status, headers, redirect_chain)."""
    req = urllib.request.Request(url, headers={'User-Agent': user_agent})
    redirect_chain = []
    try:
        # Build opener that records redirects
        class RecordingHandler(urllib.request.HTTPRedirectHandler):
            def redirect_request(self, req, fp, code, msg, headers, newurl):
                redirect_chain.append({'from': req.full_url, 'to': newurl, 'status': code})
                return super().redirect_request(req, fp, code, msg, headers, newurl)

        if allow_redirects:
            opener = urllib.request.build_opener(RecordingHandler())
        else:
            # No redirects — catch the redirect response
            class NoFollowHandler(urllib.request.HTTPRedirectHandler):
                def redirect_request(self, req, fp, code, msg, headers, newurl):
                    return None
            opener = urllib.request.build_opener(NoFollowHandler())

        resp = opener.open(req, timeout=timeout)
        html = resp.read().decode('utf-8', errors='replace')
        return html, resp.url, resp.status, dict(resp.headers), redirect_chain
    except HTTPError as e:
        try:
            body = e.read().decode('utf-8', errors='replace')
        except Exception:
            body = ''
        return body, url, e.code, dict(e.headers) if e.headers else {}, redirect_chain
    except Exception as e:
        return '', url, 0, {}, redirect_chain


def strip_tags(html):
    if not html:
        return ''
    c = re.sub(r'<script[^>]*>.*?</script>', ' ', html, flags=re.DOTALL | re.IGNORECASE)
    c = re.sub(r'<style[^>]*>.*?</style>', ' ', c, flags=re.DOTALL | re.IGNORECASE)
    c = re.sub(r'<!--.*?-->', ' ', c, flags=re.DOTALL)
    t = re.sub(r'<[^>]+>', ' ', c)
    t = re.sub(r'&[a-zA-Z#0-9]+;', ' ', t)
    return re.sub(r'\s+', ' ', t).strip()


# ──────────────────────────────────────────────────────────────────────────
# CHECK D9: FAQPage schema vs visible match
# ──────────────────────────────────────────────────────────────────────────

def check_d9_faq_schema_match(html):
    """
    Count visible FAQ pairs using ALL detection patterns (not just <details>/<summary>).
    Compare to FAQPage schema mainEntity count.
    Returns pass only if they match, fail if there's a mismatch.
    """
    # Use the shared, question-intent-gated detector. Counts only
    # <details>/<summary> pairs whose summary text actually looks like a
    # question, plus the other accordion/FAQ-class signals. Returns
    # ('none_detected' | 'empty_html' | <pattern_name>).
    visible_count, detection_method = _faq_visible_count(html)

    # FAQPage schema count
    faq_schema_count = 0
    schema_questions = []
    blocks = re.findall(
        r'<script[^>]*type=["\']application/ld\+json["\'][^>]*>(.*?)</script>',
        html, re.IGNORECASE | re.DOTALL
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
            candidates = [item]
            if isinstance(item.get('@graph'), list):
                candidates.extend(item['@graph'])
            for c in candidates:
                if isinstance(c, dict) and c.get('@type') == 'FAQPage':
                    me = c.get('mainEntity', [])
                    if isinstance(me, list):
                        faq_schema_count = len(me)
                        schema_questions = [q.get('name', '') for q in me if isinstance(q, dict)]

    # Determine status
    if visible_count == 0 and faq_schema_count == 0:
        return {
            'status': 'na',
            'evidence': 'No FAQ content detected on the page in schema or visible HTML.',
            'detail': {
                'visible_count': 0,
                'schema_count': 0,
                'detection_method': 'none',
            }
        }

    if visible_count == faq_schema_count and visible_count > 0:
        return {
            'status': 'pass',
            'evidence': f'{visible_count} visible FAQ pairs match {faq_schema_count} in FAQPage schema.',
            'detail': {
                'visible_count': visible_count,
                'schema_count': faq_schema_count,
                'detection_method': detection_method,
                'schema_questions': schema_questions,
            }
        }

    # Mismatch
    direction = 'schema has more than visible' if faq_schema_count > visible_count else 'visible has more than schema'
    return {
        'status': 'fail',
        'evidence': f'FAQPage schema claims {faq_schema_count} Q&A pairs; visible HTML has {visible_count} (detected via {detection_method}). {direction}.',
        'detail': {
            'visible_count': visible_count,
            'schema_count': faq_schema_count,
            'detection_method': detection_method,
            'mismatch_direction': direction,
            'schema_questions': schema_questions,
        }
    }


# ──────────────────────────────────────────────────────────────────────────
# CHECK A7b: H1 nested inside another heading (invalid HTML)
# ──────────────────────────────────────────────────────────────────────────

def check_a7b_h1_nesting(html):
    """
    Detect H1 tags nested inside H2/H3/H4 elements.
    This is invalid HTML per W3C.
    Catches the Valeo "Frequently asked questions" case.
    """
    violations = []
    for parent_tag in ['h2', 'h3', 'h4', 'h5', 'h6']:
        # Find <hN>...</hN> blocks and check for <h1> inside
        for m in re.finditer(
            rf'<{parent_tag}[^>]*>(.*?)</{parent_tag}>',
            html, re.IGNORECASE | re.DOTALL
        ):
            inner = m.group(1)
            if re.search(r'<h1[^>]*>', inner, re.IGNORECASE):
                # Extract the H1 content for evidence
                h1_match = re.search(r'<h1[^>]*>(.*?)</h1>', inner, re.IGNORECASE | re.DOTALL)
                h1_text = ''
                if h1_match:
                    h1_text = re.sub(r'<[^>]*>', ' ', h1_match.group(1))
                    h1_text = re.sub(r'\s+', ' ', h1_text).strip()[:80]
                violations.append({
                    'parent_tag': parent_tag,
                    'parent_position': m.start(),
                    'h1_text': h1_text,
                })

    if not violations:
        return {
            'status': 'pass',
            'evidence': 'No H1 tags nested inside other heading elements.',
            'detail': {'violations': []}
        }

    parent_tags_list = ", ".join([f"h1 in {v['parent_tag']}" for v in violations])
    return {
        'status': 'fail',
        'evidence': f'Found {len(violations)} H1 tag(s) invalidly nested inside heading elements: {parent_tags_list}.',
        'detail': {'violations': violations}
    }


# ──────────────────────────────────────────────────────────────────────────
# CHECK J2: Brand name consistency (catches character substitution / mixed casing)
# ──────────────────────────────────────────────────────────────────────────

def check_j2_brand_name_consistency(html, brand_name=None):
    """
    Detect when the same brand name has mixed variants on the page.
    Catches Weg0vy vs Wegovy (zero substituted for o).

    If brand_name is None, auto-detect from <title> or Organization schema.
    Scans for common character substitutions: o→0, l→1, i→1/l, e→3, a→4, s→5, b→6, z→2.
    """
    # Auto-detect brand name from Organization schema
    candidates = set()
    if brand_name:
        candidates.add(brand_name)
    else:
        for m in re.finditer(
            r'<script[^>]*application/ld\+json[^>]*>(.*?)</script>',
            html, re.IGNORECASE | re.DOTALL
        ):
            try:
                data = json.loads(m.group(1).strip())
            except json.JSONDecodeError:
                continue
            items = data if isinstance(data, list) else [data]
            for item in items:
                if isinstance(item, dict) and item.get('@type') in ('Organization', 'MedicalBusiness', 'LocalBusiness', 'SoftwareApplication'):
                    n = item.get('name')
                    if n and len(n) >= 4:
                        candidates.add(n)

    # Also look for common product/drug names that get obfuscated in this industry
    # These are well-known GLP-1 weight-loss drugs and other medical products commonly obfuscated
    known_terms = ['Wegovy', 'Mounjaro', 'Ozempic', 'Rybelsus', 'Saxenda', 'Trulicity']

    # Substitution map (lowercase)
    subst_map = {'o': '0', 'l': '1', 'i': '1', 'e': '3', 'a': '4', 's': '5', 'b': '6', 'z': '2'}

    mixed_variants = []
    for term in list(candidates) + known_terms:
        if not term or len(term) < 4:
            continue
        # Real count
        real_count = len(re.findall(r'\b' + re.escape(term) + r'\b', html, re.IGNORECASE))
        # Generate substituted variants and count them
        for idx, ch in enumerate(term.lower()):
            if ch in subst_map:
                substituted = term[:idx] + subst_map[ch] + term[idx+1:]
                sub_count = len(re.findall(r'\b' + re.escape(substituted) + r'\b', html, re.IGNORECASE))
                if sub_count > 0:
                    mixed_variants.append({
                        'real': term,
                        'real_count': real_count,
                        'substituted': substituted,
                        'substituted_count': sub_count,
                    })

    if not mixed_variants:
        return {
            'status': 'pass',
            'evidence': 'No character-substitution variants of brand/product names detected.',
            'detail': {'variants_found': []}
        }

    # Each variant found is an issue
    return {
        'status': 'fail',
        'evidence': f'Found {len(mixed_variants)} brand/product name with mixed spelling: ' +
                    '; '.join([f'{v["real"]} ({v["real_count"]}x) vs {v["substituted"]} ({v["substituted_count"]}x)' for v in mixed_variants]),
        'detail': {'variants_found': mixed_variants}
    }


# ──────────────────────────────────────────────────────────────────────────
# CHECK A4b: Canonical URL redirect chain
# ──────────────────────────────────────────────────────────────────────────

def check_a4b_canonical_redirect_chain(html, current_url):
    """
    Extract the canonical URL from the HTML. If it differs from current_url,
    fetch the canonical URL without following redirects and see if it 3xx's.

    Flags the Valeo-style case: page at /foo, canonical says /foo/, which 308s to /foo.
    """
    # Extract canonical
    m = re.search(
        r'<link[^>]*rel=["\']canonical["\'][^>]*href=["\']([^"\']*)',
        html, re.IGNORECASE
    )
    if not m:
        return {
            'status': 'warn',
            'evidence': 'No canonical tag found on the page.',
            'detail': {}
        }

    canonical = m.group(1)

    # Normalize URLs for comparison (strip query + fragment but keep path/slash)
    def normalize(u):
        # Add scheme if missing
        if u.startswith('//'):
            u = 'https:' + u
        elif not u.startswith('http'):
            u = 'https://' + u.lstrip('/')
        return u

    canonical_norm = normalize(canonical)
    current_norm = normalize(current_url)

    # Case 1: Self-referencing (strictly equal including trailing slash)
    if canonical_norm == current_norm:
        return {
            'status': 'pass',
            'evidence': f'Canonical ({canonical}) exactly matches served URL.',
            'detail': {
                'canonical_url': canonical,
                'current_url': current_url,
                'identical': True,
            }
        }

    # Case 2: Canonical differs. Probe the canonical URL to see if it 3xx's.
    # Test without following redirects
    _, _, status, headers, redirects = fetch(canonical_norm, allow_redirects=False, timeout=10)

    # Also test with redirects to get final URL
    _, final_url, final_status, _, full_chain = fetch(canonical_norm, allow_redirects=True, timeout=10)

    is_redirect = status in (301, 302, 303, 307, 308)
    redirect_target = headers.get('Location') or headers.get('location') if is_redirect else None

    # Worst case: canonical points somewhere that redirects back to current URL
    if is_redirect and final_url and normalize(final_url) == current_norm:
        return {
            'status': 'fail',
            'evidence': f'Canonical points to {canonical} which {status}-redirects back to current URL {current_url}. This is a canonical loop.',
            'detail': {
                'canonical_url': canonical,
                'current_url': current_url,
                'canonical_status': status,
                'canonical_redirect_target': redirect_target,
                'final_url_after_redirects': final_url,
                'loop_detected': True,
            }
        }

    if is_redirect:
        return {
            'status': 'fail',
            'evidence': f'Canonical ({canonical}) returns {status} redirect to {redirect_target}. Canonical should point to a 200 page.',
            'detail': {
                'canonical_url': canonical,
                'canonical_status': status,
                'canonical_redirect_target': redirect_target,
                'final_url_after_redirects': final_url,
            }
        }

    # Canonical differs from current but resolves to a 200 — could be intentional
    # (e.g., filter variants canonicalizing to a main page)
    return {
        'status': 'warn',
        'evidence': f'Canonical ({canonical}) differs from served URL ({current_url}) but resolves to status {status}. Verify this is intentional.',
        'detail': {
            'canonical_url': canonical,
            'current_url': current_url,
            'canonical_status': status,
        }
    }


# ──────────────────────────────────────────────────────────────────────────
# CHECK B1: TTFB 5-sample median
# ──────────────────────────────────────────────────────────────────────────

def check_b1_ttfb_median(url, samples=5):
    """
    Sample TTFB 5 times and report median + p95.
    Fixes the single-sample variance problem I hit on Valeo weight loss.
    """
    ttfbs = []
    origin_times = []
    for i in range(samples):
        try:
            # Use curl for accurate TTFB measurement
            result = subprocess.run(
                ['curl', '-sS', '-o', '/dev/null', '-w',
                 '%{time_starttransfer} %{header_x-envoy-upstream-service-time}',
                 '--max-time', '15',
                 '-H', 'Cache-Control: no-cache',
                 f'{url}?_ttfb_sample={i}'],
                capture_output=True, text=True, timeout=20
            )
            parts = result.stdout.strip().split()
            if parts:
                ttfb_sec = float(parts[0])
                ttfbs.append(ttfb_sec * 1000)  # convert to ms
                if len(parts) > 1 and parts[1]:
                    try:
                        origin_times.append(float(parts[1]))
                    except ValueError:
                        pass
            time.sleep(0.5)
        except Exception:
            continue

    if not ttfbs:
        return {
            'status': 'na',
            'evidence': 'Could not collect TTFB samples (network or tool failure).',
            'detail': {}
        }

    ttfbs.sort()
    median_ttfb = ttfbs[len(ttfbs) // 2]
    p95_ttfb = ttfbs[min(int(len(ttfbs) * 0.95), len(ttfbs) - 1)]
    max_ttfb = max(ttfbs)
    min_ttfb = min(ttfbs)

    # Google Core Web Vitals thresholds
    if median_ttfb < 800:
        status = 'pass'
        verdict = 'Good (<800ms)'
    elif median_ttfb < 1800:
        status = 'warn'
        verdict = 'Needs Improvement (800-1800ms)'
    else:
        status = 'fail'
        verdict = 'Poor (>1800ms)'

    return {
        'status': status,
        'evidence': f'TTFB median: {median_ttfb:.0f}ms ({verdict}). Samples: {[int(t) for t in ttfbs]}',
        'detail': {
            'samples_ms': [round(t, 0) for t in ttfbs],
            'median_ms': round(median_ttfb, 0),
            'p95_ms': round(p95_ttfb, 0),
            'min_ms': round(min_ttfb, 0),
            'max_ms': round(max_ttfb, 0),
            'origin_times_ms': origin_times,
            'verdict': verdict,
            'sample_count': len(ttfbs),
        }
    }


# ──────────────────────────────────────────────────────────────────────────
# CHECK D4: Schema @id coverage
# ──────────────────────────────────────────────────────────────────────────

def check_d4_schema_id_coverage(html):
    """
    Every schema entity on a production page should have @id for cross-referencing.
    Flags the TRYPS/AnswerMonk pattern of entities without @id.
    """
    entities = []
    for m in re.finditer(
        r'<script[^>]*application/ld\+json[^>]*>(.*?)</script>',
        html, re.IGNORECASE | re.DOTALL
    ):
        try:
            data = json.loads(m.group(1).strip())
        except json.JSONDecodeError:
            continue

        # Handle @graph, arrays, and single objects
        items_to_check = []
        if isinstance(data, dict):
            if isinstance(data.get('@graph'), list):
                items_to_check.extend(data['@graph'])
            else:
                items_to_check.append(data)
        elif isinstance(data, list):
            items_to_check.extend(data)

        for item in items_to_check:
            if not isinstance(item, dict):
                continue
            t = item.get('@type')
            if t:
                entities.append({
                    'type': t if isinstance(t, str) else str(t),
                    'has_id': bool(item.get('@id')),
                    'id': item.get('@id'),
                    'name': item.get('name', '')[:80] if isinstance(item.get('name'), str) else '',
                })

    if not entities:
        return {
            'status': 'na',
            'evidence': 'No schema entities found on the page.',
            'detail': {'entities': []}
        }

    missing_id = [e for e in entities if not e['has_id']]
    total = len(entities)
    with_id = total - len(missing_id)

    if len(missing_id) == 0:
        return {
            'status': 'pass',
            'evidence': f'All {total} schema entities have @id fragments.',
            'detail': {'entities': entities, 'with_id': with_id, 'total': total}
        }

    return {
        'status': 'fail' if len(missing_id) >= total / 2 else 'warn',
        'evidence': f'{len(missing_id)} of {total} schema entities lack @id. Missing on: {", ".join([e["type"] for e in missing_id])}.',
        'detail': {
            'entities': entities,
            'entities_missing_id': missing_id,
            'with_id': with_id,
            'total': total,
        }
    }


# ──────────────────────────────────────────────────────────────────────────
# CHECK C12b: dateModified staleness detection
# ──────────────────────────────────────────────────────────────────────────

def check_c12b_datemodified_staleness(html):
    """
    Extract dateModified from schema. Check if it's:
    (a) Missing — warn
    (b) Present and > 13 weeks old — flag as stale
    (c) Present and exactly matches the current timestamp — flag as cosmetic (Date.now() pattern)
    (d) Present and reasonable
    """
    import datetime

    dates_found = []
    for m in re.finditer(
        r'<script[^>]*application/ld\+json[^>]*>(.*?)</script>',
        html, re.IGNORECASE | re.DOTALL
    ):
        try:
            data = json.loads(m.group(1).strip())
        except json.JSONDecodeError:
            continue
        items = data if isinstance(data, list) else [data]
        if isinstance(data, dict) and isinstance(data.get('@graph'), list):
            items.extend(data['@graph'])
        for item in items:
            if not isinstance(item, dict):
                continue
            dm = item.get('dateModified')
            if dm and isinstance(dm, str):
                dates_found.append({
                    'type': item.get('@type'),
                    'dateModified': dm,
                })

    if not dates_found:
        return {
            'status': 'warn',
            'evidence': 'No dateModified found in any schema entity.',
            'detail': {'dates_found': []}
        }

    now = datetime.datetime.now(datetime.timezone.utc)
    analyses = []
    for d in dates_found:
        dm_str = d['dateModified']
        try:
            # Try ISO format with various endings
            parsed = None
            for fmt_input in [dm_str, dm_str.replace('Z', '+00:00')]:
                try:
                    parsed = datetime.datetime.fromisoformat(fmt_input)
                    break
                except ValueError:
                    continue
            if parsed and parsed.tzinfo is None:
                parsed = parsed.replace(tzinfo=datetime.timezone.utc)
            if not parsed:
                analyses.append({**d, 'analysis': 'unparseable'})
                continue

            age = now - parsed
            age_seconds = age.total_seconds()
            age_days = age_seconds / 86400

            # Detect cosmetic pattern: dateModified within 60s of fetch time
            if 0 <= age_seconds < 60:
                analyses.append({**d, 'analysis': 'cosmetic_near_now', 'age_days': round(age_days, 3)})
            elif age_seconds < 0:
                analyses.append({**d, 'analysis': 'future_date', 'age_days': round(age_days, 3)})
            elif age_days > 91:  # ~13 weeks
                analyses.append({**d, 'analysis': 'stale_over_13_weeks', 'age_days': round(age_days, 1)})
            else:
                analyses.append({**d, 'analysis': 'fresh', 'age_days': round(age_days, 1)})
        except Exception:
            analyses.append({**d, 'analysis': 'unparseable'})

    # Determine overall status
    # If any date is cosmetic (== now), fail
    # If all dates are stale (>13 weeks), warn
    # Otherwise pass
    cosmetic = [a for a in analyses if a['analysis'] == 'cosmetic_near_now']
    stale = [a for a in analyses if a['analysis'] == 'stale_over_13_weeks']
    fresh = [a for a in analyses if a['analysis'] == 'fresh']

    if cosmetic:
        return {
            'status': 'fail',
            'evidence': f'{len(cosmetic)} dateModified field(s) match the current timestamp to within 60s — likely cosmetic/dynamic rendering. AP #799.',
            'detail': {'analyses': analyses}
        }

    if stale and not fresh:
        ages = [a['age_days'] for a in stale]
        return {
            'status': 'warn',
            'evidence': f'All dateModified fields are stale (>13 weeks old): ages {ages} days. 50% of AI-cited content is <13 weeks old.',
            'detail': {'analyses': analyses}
        }

    return {
        'status': 'pass',
        'evidence': f'{len(fresh)} dateModified field(s) are fresh (<13 weeks old).',
        'detail': {'analyses': analyses}
    }


# ──────────────────────────────────────────────────────────────────────────
# CHECK A2b: Title uniqueness sample (catches SPA placeholder titles)
# ──────────────────────────────────────────────────────────────────────────

def check_a2b_title_uniqueness(url, sample_size=3):
    """
    Fetch the page + a 404 URL + another sitemap URL. Compare titles.
    If all 3 have the same title, site has a global placeholder title (SPA pattern).
    """
    origin = re.match(r'(https?://[^/]+)', url).group(1) if re.match(r'(https?://[^/]+)', url) else None
    if not origin:
        return {'status': 'na', 'evidence': 'Could not parse origin from URL.', 'detail': {}}

    # Fetch current page
    html1, _, _, _, _ = fetch(url)
    title1 = extract_title_from_html(html1)

    # Fetch a guaranteed-404 URL
    ne_url = f'{origin}/nonexistent-probe-{int(time.time())}'
    html2, _, _, _, _ = fetch(ne_url)
    title2 = extract_title_from_html(html2)

    # Try to fetch another URL from sitemap.xml
    sitemap_url = f'{origin}/sitemap.xml'
    sitemap_html, _, sitemap_status, _, _ = fetch(sitemap_url)
    other_title = None
    other_url = None
    if sitemap_status == 200 and sitemap_html:
        # Pick a URL that's different from the current one
        locs = re.findall(r'<loc>([^<]+)</loc>', sitemap_html)
        for loc in locs:
            if loc != url and not loc.endswith('/sitemap.xml'):
                other_url = loc
                html3, _, _, _, _ = fetch(loc)
                other_title = extract_title_from_html(html3)
                break

    # Compare
    titles_collected = {
        url: title1,
        ne_url: title2,
    }
    if other_url and other_title:
        titles_collected[other_url] = other_title

    unique_titles = set(t for t in titles_collected.values() if t)
    if len(titles_collected) < 2:
        return {
            'status': 'na',
            'evidence': 'Could not collect enough titles to compare.',
            'detail': {'titles': titles_collected}
        }

    # If 2+ URLs return the same title → SPA placeholder pattern
    if len(unique_titles) == 1:
        return {
            'status': 'fail',
            'evidence': f'All {len(titles_collected)} tested URLs return the same title: "{list(unique_titles)[0]}". This indicates a client-side SPA without per-page SSR.',
            'detail': {'titles': titles_collected, 'unique_count': 1}
        }

    # If the 404 title matches the real page title → still a red flag
    if title2 and title1 and title2 == title1:
        return {
            'status': 'fail',
            'evidence': f'404 URL and real URL return same title "{title1}". Indicates SPA shell without per-URL rendering.',
            'detail': {'titles': titles_collected, 'unique_count': len(unique_titles)}
        }

    return {
        'status': 'pass',
        'evidence': f'{len(titles_collected)} URLs tested, {len(unique_titles)} unique titles. Per-page titles appear to be rendered.',
        'detail': {'titles': titles_collected, 'unique_count': len(unique_titles)}
    }


def extract_title_from_html(html):
    m = re.search(r'<title[^>]*>([^<]*)</title>', html, re.IGNORECASE)
    if m:
        return re.sub(r'\s+', ' ', m.group(1)).strip()
    return None


# ──────────────────────────────────────────────────────────────────────────
# CHECK D12: Person/author schema presence
# ──────────────────────────────────────────────────────────────────────────

def check_d12_person_schema(html):
    """
    Check if any Person schema exists with credentials.
    For YMYL pages (medical, financial), this is a required E-E-A-T signal.
    """
    persons = []
    for m in re.finditer(
        r'<script[^>]*application/ld\+json[^>]*>(.*?)</script>',
        html, re.IGNORECASE | re.DOTALL
    ):
        try:
            data = json.loads(m.group(1).strip())
        except json.JSONDecodeError:
            continue
        items = data if isinstance(data, list) else [data]
        if isinstance(data, dict) and isinstance(data.get('@graph'), list):
            items.extend(data['@graph'])
        # Also check nested Person in founder/author fields
        for item in items:
            if not isinstance(item, dict):
                continue
            if item.get('@type') == 'Person':
                persons.append({
                    'name': item.get('name'),
                    'jobTitle': item.get('jobTitle'),
                    'hasCredential': bool(item.get('hasCredential')),
                    'sameAs_count': len(item.get('sameAs', [])) if isinstance(item.get('sameAs'), list) else 0,
                })
            # Nested as founder
            for field in ['founder', 'author', 'medicalSpecialist']:
                nested = item.get(field)
                if isinstance(nested, dict) and nested.get('@type') == 'Person':
                    persons.append({
                        'name': nested.get('name'),
                        'jobTitle': nested.get('jobTitle'),
                        'hasCredential': bool(nested.get('hasCredential')),
                        'sameAs_count': len(nested.get('sameAs', [])) if isinstance(nested.get('sameAs'), list) else 0,
                        'found_via': field,
                    })

    if not persons:
        return {
            'status': 'fail',
            'evidence': 'No Person schema found in any JSON-LD block.',
            'detail': {'persons_found': []}
        }

    with_creds = [p for p in persons if p.get('hasCredential')]

    if with_creds:
        return {
            'status': 'pass',
            'evidence': f'{len(persons)} Person entities found, {len(with_creds)} with hasCredential.',
            'detail': {'persons_found': persons, 'with_credentials': with_creds}
        }

    return {
        'status': 'warn',
        'evidence': f'{len(persons)} Person entities found but none have hasCredential. Add for E-E-A-T (especially YMYL).',
        'detail': {'persons_found': persons}
    }


# ──────────────────────────────────────────────────────────────────────────
# CHECK D14: hreflang coverage (incl. Next.js streaming chunks)
# ──────────────────────────────────────────────────────────────────────────

def check_d14_hreflang_coverage(html):
    """
    Detect hreflang tags in the <head> AND inside Next.js streaming chunks
    (self.__next_f.push). Catches the App Router false-negative where
    locales declared in RSC payloads were invisible to the audit.

    Wraps `_detect_hreflang` (in deterministic_checks_extras.py) so that
    Phase 2 output carries an `hreflang_coverage` check entry like every
    other deterministic check.
    """
    r = _detect_hreflang(html)
    return {
        'status': r.get('status', 'na'),
        'evidence': r.get('evidence', ''),
        'detail': {
            'total_count': r.get('total_count', 0),
            'toplevel_count': r.get('toplevel_count', 0),
            'streamed_count': r.get('streamed_count', 0),
            'locales': r.get('locales', []),
        },
    }


# ──────────────────────────────────────────────────────────────────────────
# Main orchestrator
# ──────────────────────────────────────────────────────────────────────────

def run_all_checks(url):
    """Run all 8 deterministic checks and return consolidated JSON."""
    # Fetch the page once
    html, final_url, status_code, _, _ = fetch(url)

    if not html:
        return {
            'url': url,
            'error': 'Could not fetch page',
            'checks': {}
        }

    results = {
        'url': url,
        'final_url_after_redirects': final_url,
        'http_status': status_code,
        'checks': {}
    }

    # Run checks that only need HTML
    results['checks']['D9_faqpage_schema_vs_visible_match'] = check_d9_faq_schema_match(html)
    results['checks']['A7b_h1_nested_in_heading'] = check_a7b_h1_nesting(html)
    results['checks']['J2_brand_name_consistency'] = check_j2_brand_name_consistency(html)
    results['checks']['D4_schema_id_coverage'] = check_d4_schema_id_coverage(html)
    results['checks']['C12b_datemodified_staleness'] = check_c12b_datemodified_staleness(html)
    results['checks']['D12_person_schema_with_credentials'] = check_d12_person_schema(html)
    results['checks']['D14_hreflang_coverage'] = check_d14_hreflang_coverage(html)

    # Run checks that need network
    results['checks']['A4b_canonical_redirect_chain'] = check_a4b_canonical_redirect_chain(html, final_url)
    results['checks']['B1_ttfb_median_5_samples'] = check_b1_ttfb_median(url)
    results['checks']['A2b_title_uniqueness_sample'] = check_a2b_title_uniqueness(url)

    # Summary counts
    statuses = [c['status'] for c in results['checks'].values()]
    results['summary'] = {
        'total_checks': len(statuses),
        'pass': statuses.count('pass'),
        'fail': statuses.count('fail'),
        'warn': statuses.count('warn'),
        'na': statuses.count('na'),
    }

    return results


def main():
    if len(sys.argv) < 2:
        print(json.dumps({'error': 'Usage: python3 deterministic_checks.py <URL>'}))
        sys.exit(1)

    url = sys.argv[1]
    out = run_all_checks(url)
    print(json.dumps(out, indent=2, ensure_ascii=False))


if __name__ == '__main__':
    main()
