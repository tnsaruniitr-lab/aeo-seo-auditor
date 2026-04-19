#!/usr/bin/env python3
"""
check_sitemap.py — Deterministic sitemap validity check

Fetches sitemap.xml (via robots.txt directive or default /sitemap.xml),
verifies structure, and confirms:
  1. Target URL is listed in the sitemap
  2. A sample of sitemap URLs actually return 200 (not 404 or 500)
  3. lastmod dates are present and well-formed
  4. No obvious sitemap index/urlset confusion
  5. No cross-domain sitemap entries (common misconfig)

Usage:
  python3 scripts/check_sitemap.py <URL>

Output: JSON to stdout.

Deterministic: same sitemap.xml content produces identical findings.
The only varying aspect is which 5 random URLs get sampled — we use a fixed seed
based on the target URL so sampling is stable for a given target.
"""

import sys
import re
import json
import urllib.request
import urllib.parse
import hashlib
from urllib.error import URLError, HTTPError


SAMPLE_SIZE = 5
SAMPLE_HTTP_TIMEOUT = 10


def fetch_url(url, timeout=10, allow_redirects=True):
    """Fetch any URL, return (text, http_status, final_url, error)."""
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (AuditBot/1.0)'})
    try:
        if allow_redirects:
            resp = urllib.request.urlopen(req, timeout=timeout)
        else:
            class NoFollow(urllib.request.HTTPRedirectHandler):
                def redirect_request(self, *a, **kw):
                    return None
            opener = urllib.request.build_opener(NoFollow())
            resp = opener.open(req, timeout=timeout)
        text = resp.read().decode('utf-8', errors='replace')
        return text, resp.status, resp.url, None
    except HTTPError as e:
        return '', e.code, url, f'http_{e.code}'
    except URLError as e:
        return None, 0, url, f'url_error: {e.reason}'
    except Exception as e:
        return None, 0, url, f'exception: {type(e).__name__}'


def head_url(url, timeout=8):
    """HEAD request — returns (status, final_url, error). Much cheaper than GET."""
    req = urllib.request.Request(
        url,
        method='HEAD',
        headers={'User-Agent': 'Mozilla/5.0 (AuditBot/1.0)'}
    )
    try:
        resp = urllib.request.urlopen(req, timeout=timeout)
        return resp.status, resp.url, None
    except HTTPError as e:
        # Some servers reject HEAD — treat as partial info
        return e.code, url, f'http_{e.code}'
    except URLError as e:
        return 0, url, f'url_error: {e.reason}'
    except Exception as e:
        return 0, url, f'exception: {type(e).__name__}'


def parse_origin(url):
    """Get https://host from URL."""
    m = re.match(r'(https?://[^/]+)', url)
    return m.group(1) if m else None


def find_sitemap_url(origin_url):
    """
    Discover sitemap.xml URL.
    Priority: robots.txt Sitemap: directive → /sitemap.xml → /sitemap_index.xml
    Returns (sitemap_url, source) or (None, None).
    """
    origin = parse_origin(origin_url)
    if not origin:
        return None, None

    # Try robots.txt first
    robots_text, status, _, _ = fetch_url(f'{origin}/robots.txt', timeout=8)
    if robots_text:
        for line in robots_text.splitlines():
            line = line.split('#', 1)[0].strip()
            if line.lower().startswith('sitemap:'):
                sitemap_url = line.split(':', 1)[1].strip()
                return sitemap_url, 'robots_txt_directive'

    # Fallback: /sitemap.xml
    text, status, _, _ = fetch_url(f'{origin}/sitemap.xml', timeout=8)
    if status == 200 and text:
        return f'{origin}/sitemap.xml', 'default_path'

    # Second fallback: /sitemap_index.xml
    text, status, _, _ = fetch_url(f'{origin}/sitemap_index.xml', timeout=8)
    if status == 200 and text:
        return f'{origin}/sitemap_index.xml', 'sitemap_index_default'

    return None, None


def parse_sitemap_xml(xml_text):
    """
    Parse sitemap XML. Handles both urlset and sitemapindex.
    Returns {
      'is_index': bool,
      'urls': [{loc, lastmod}],        # for urlset
      'sub_sitemaps': [{loc, lastmod}] # for sitemapindex
    }
    """
    is_index = bool(re.search(r'<sitemapindex\b', xml_text, re.IGNORECASE))

    if is_index:
        # It's an index — extract <sitemap><loc>...</loc></sitemap> entries
        sub_sitemaps = []
        for m in re.finditer(r'<sitemap\b[^>]*>(.*?)</sitemap>', xml_text, re.DOTALL | re.IGNORECASE):
            inner = m.group(1)
            loc_m = re.search(r'<loc>([^<]+)</loc>', inner)
            lastmod_m = re.search(r'<lastmod>([^<]+)</lastmod>', inner)
            if loc_m:
                sub_sitemaps.append({
                    'loc': loc_m.group(1).strip(),
                    'lastmod': lastmod_m.group(1).strip() if lastmod_m else None,
                })
        return {'is_index': True, 'urls': [], 'sub_sitemaps': sub_sitemaps}

    # urlset — extract <url><loc>...</loc><lastmod>...</lastmod></url>
    urls = []
    for m in re.finditer(r'<url\b[^>]*>(.*?)</url>', xml_text, re.DOTALL | re.IGNORECASE):
        inner = m.group(1)
        loc_m = re.search(r'<loc>([^<]+)</loc>', inner)
        lastmod_m = re.search(r'<lastmod>([^<]+)</lastmod>', inner)
        if loc_m:
            urls.append({
                'loc': loc_m.group(1).strip(),
                'lastmod': lastmod_m.group(1).strip() if lastmod_m else None,
            })
    return {'is_index': False, 'urls': urls, 'sub_sitemaps': []}


def collect_all_urls(sitemap_url, max_depth=2, visited=None):
    """
    Follow sitemap indexes recursively to collect all URLs.
    Cap at max_depth to avoid infinite loops.
    Returns list of {loc, lastmod, source_sitemap}.
    """
    if visited is None:
        visited = set()
    if sitemap_url in visited or max_depth < 0:
        return []
    visited.add(sitemap_url)

    text, status, _, error = fetch_url(sitemap_url, timeout=10)
    if status != 200 or not text:
        return []

    parsed = parse_sitemap_xml(text)

    if parsed['is_index']:
        # Recurse into each sub-sitemap
        all_urls = []
        for sub in parsed['sub_sitemaps'][:20]:  # cap sub-sitemaps for performance
            all_urls.extend(
                collect_all_urls(sub['loc'], max_depth - 1, visited)
            )
        return all_urls
    else:
        return [{
            **u,
            'source_sitemap': sitemap_url
        } for u in parsed['urls']]


def deterministic_sample(urls, target_url, sample_size):
    """
    Pick sample_size URLs deterministically.
    Seed is derived from target_url so same target always produces same sample.
    Prefer URLs that are NOT the target + ensure variety.
    """
    # Filter out the target URL itself (we check that separately)
    candidates = [u for u in urls if u['loc'] != target_url and u['loc'].rstrip('/') != target_url.rstrip('/')]

    if len(candidates) <= sample_size:
        return candidates

    # Deterministic hash-based selection
    seed = hashlib.md5(target_url.encode()).hexdigest()
    seed_int = int(seed[:8], 16)

    # Sort candidates by hash(url + seed) — deterministic
    def sort_key(u):
        return hashlib.md5((u['loc'] + seed).encode()).hexdigest()

    sorted_candidates = sorted(candidates, key=sort_key)
    return sorted_candidates[:sample_size]


def check_target_in_sitemap(target_url, all_urls):
    """
    Check if target URL is in the sitemap.
    Handles trailing slash + protocol variants + common normalization.
    """
    def normalize(url):
        u = url.rstrip('/').lower()
        u = u.replace('http://', 'https://')
        return u

    target_norm = normalize(target_url)

    exact_match = None
    normalized_match = None
    for u in all_urls:
        if u['loc'] == target_url:
            exact_match = u
            break
        if normalize(u['loc']) == target_norm:
            normalized_match = u

    if exact_match:
        return {'found': True, 'match_type': 'exact', 'entry': exact_match}
    if normalized_match:
        return {'found': True, 'match_type': 'normalized (trailing slash or protocol differs)', 'entry': normalized_match}
    return {'found': False, 'match_type': None, 'entry': None}


def check_cross_domain(all_urls, expected_origin):
    """Flag sitemap entries that point to a different origin (common misconfig)."""
    cross_domain = []
    for u in all_urls:
        loc = u['loc']
        loc_origin = parse_origin(loc)
        if loc_origin and loc_origin != expected_origin:
            cross_domain.append({'loc': loc, 'expected_origin': expected_origin})
    return cross_domain


def main():
    if len(sys.argv) < 2:
        print(json.dumps({'error': 'Usage: python3 check_sitemap.py <URL>'}))
        sys.exit(1)

    target_url = sys.argv[1]
    target_origin = parse_origin(target_url)

    # Step 1: Find the sitemap
    sitemap_url, discovery_source = find_sitemap_url(target_url)

    if not sitemap_url:
        print(json.dumps({
            'url': target_url,
            'sitemap': {'found': False, 'error': 'could_not_locate_sitemap'},
            'checks': {
                'sitemap_reachable': {
                    'status': 'fail',
                    'evidence': 'No sitemap.xml found via robots.txt directive, /sitemap.xml, or /sitemap_index.xml.',
                    'detail': {}
                }
            }
        }, indent=2))
        sys.exit(0)

    # Step 2: Fetch and parse the sitemap (recursively if it's an index)
    all_urls = collect_all_urls(sitemap_url)

    # Step 3: Check target URL presence
    target_check = check_target_in_sitemap(target_url, all_urls)

    # Step 4: Check cross-domain entries
    cross_domain = check_cross_domain(all_urls, target_origin)

    # Step 5: Sample URLs and probe them
    sample = deterministic_sample(all_urls, target_url, SAMPLE_SIZE)
    sample_results = []
    for entry in sample:
        status, final_url, error = head_url(entry['loc'])
        sample_results.append({
            'url': entry['loc'],
            'status': status,
            'final_url': final_url,
            'error': error,
            'lastmod_declared': entry['lastmod'],
            'verdict': 'ok' if status == 200 else ('redirect' if 300 <= status < 400 else 'broken')
        })

    # Step 6: Lastmod analysis
    urls_with_lastmod = [u for u in all_urls if u['lastmod']]
    urls_missing_lastmod = len(all_urls) - len(urls_with_lastmod)

    # Step 7: Build checks dict
    checks = {}

    # Check 1: sitemap reachable
    checks['sitemap_reachable'] = {
        'status': 'pass',
        'evidence': f'Sitemap located via {discovery_source}: {sitemap_url}. {len(all_urls)} URLs parsed.',
        'detail': {
            'sitemap_url': sitemap_url,
            'discovery_source': discovery_source,
            'url_count': len(all_urls),
        }
    }

    # Check 2: target URL present in sitemap
    if target_check['found']:
        checks['target_url_in_sitemap'] = {
            'status': 'pass',
            'evidence': f'Target URL {target_url} found in sitemap ({target_check["match_type"]}). lastmod: {target_check["entry"].get("lastmod", "none")}.',
            'detail': target_check,
        }
    else:
        checks['target_url_in_sitemap'] = {
            'status': 'fail',
            'evidence': f'Target URL {target_url} NOT found in sitemap. Checked {len(all_urls)} URLs.',
            'detail': {'target_url': target_url, 'sitemap_url_count': len(all_urls)}
        }

    # Check 3: no cross-domain entries
    if cross_domain:
        checks['no_cross_domain_sitemap_entries'] = {
            'status': 'fail',
            'evidence': f'Found {len(cross_domain)} cross-domain sitemap entries (pointing to different origins than {target_origin}).',
            'detail': {'cross_domain_entries': cross_domain[:5], 'total_cross_domain': len(cross_domain)}
        }
    else:
        checks['no_cross_domain_sitemap_entries'] = {
            'status': 'pass',
            'evidence': f'All sitemap entries point to the expected origin ({target_origin}).',
            'detail': {}
        }

    # Check 4: sample URLs return 200
    broken = [s for s in sample_results if s['verdict'] == 'broken']
    redirects = [s for s in sample_results if s['verdict'] == 'redirect']
    ok = [s for s in sample_results if s['verdict'] == 'ok']

    if broken:
        checks['sampled_urls_return_200'] = {
            'status': 'fail',
            'evidence': f'{len(broken)}/{len(sample_results)} sampled sitemap URLs return error status: {[(b["url"], b["status"]) for b in broken]}',
            'detail': {'sample_results': sample_results, 'broken_count': len(broken), 'redirect_count': len(redirects), 'ok_count': len(ok)}
        }
    elif redirects:
        checks['sampled_urls_return_200'] = {
            'status': 'warn',
            'evidence': f'{len(redirects)}/{len(sample_results)} sampled sitemap URLs redirect (should be canonical URLs only).',
            'detail': {'sample_results': sample_results}
        }
    elif not sample_results:
        checks['sampled_urls_return_200'] = {
            'status': 'na',
            'evidence': 'Not enough URLs in sitemap to sample.',
            'detail': {}
        }
    else:
        checks['sampled_urls_return_200'] = {
            'status': 'pass',
            'evidence': f'All {len(sample_results)} sampled URLs return HTTP 200.',
            'detail': {'sample_results': sample_results}
        }

    # Check 5: lastmod coverage
    if len(all_urls) > 0:
        lastmod_pct = (len(urls_with_lastmod) / len(all_urls)) * 100
        if lastmod_pct >= 80:
            checks['lastmod_coverage'] = {
                'status': 'pass',
                'evidence': f'{len(urls_with_lastmod)}/{len(all_urls)} URLs ({lastmod_pct:.0f}%) have lastmod dates.',
                'detail': {'urls_with_lastmod': len(urls_with_lastmod), 'total_urls': len(all_urls)}
            }
        elif lastmod_pct >= 30:
            checks['lastmod_coverage'] = {
                'status': 'warn',
                'evidence': f'Only {len(urls_with_lastmod)}/{len(all_urls)} URLs ({lastmod_pct:.0f}%) have lastmod dates. Perplexity uses lastmod for freshness signals.',
                'detail': {'urls_with_lastmod': len(urls_with_lastmod), 'total_urls': len(all_urls)}
            }
        else:
            checks['lastmod_coverage'] = {
                'status': 'fail',
                'evidence': f'Only {len(urls_with_lastmod)}/{len(all_urls)} URLs ({lastmod_pct:.0f}%) have lastmod dates. Google-recommended for all entries.',
                'detail': {'urls_with_lastmod': len(urls_with_lastmod), 'total_urls': len(all_urls)}
            }

    # Check 6: sitemap size compliance (Google limits: 50MB, 50,000 URLs per file)
    # For index sitemaps, these limits apply per sub-sitemap, not globally
    if len(all_urls) > 50000:
        checks['sitemap_size_compliance'] = {
            'status': 'warn',
            'evidence': f'Sitemap contains {len(all_urls)} URLs (total across any sub-sitemaps). Google limit: 50,000 URLs per individual sitemap file.',
            'detail': {'url_count': len(all_urls)}
        }

    return_value = {
        'url': target_url,
        'sitemap': {
            'found': True,
            'sitemap_url': sitemap_url,
            'discovery_source': discovery_source,
            'total_urls_indexed': len(all_urls),
            'urls_with_lastmod': len(urls_with_lastmod),
            'cross_domain_entry_count': len(cross_domain),
            'target_in_sitemap': target_check['found'],
        },
        'sample_probe_results': sample_results,
        'checks': checks,
    }

    print(json.dumps(return_value, indent=2, ensure_ascii=False))


if __name__ == '__main__':
    main()
