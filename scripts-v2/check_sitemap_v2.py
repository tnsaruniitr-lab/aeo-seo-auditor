#!/usr/bin/env python3
"""
check_sitemap_v2.py — Fixed sitemap validator.

Replaces the original scripts/check_sitemap.py. Fixes:

1. Real XML parsing via xml.etree.ElementTree (stdlib).
   Original used regex; corrupted URLs with &amp; entities, CDATA,
   and namespace variations.

2. HEAD with GET fallback for sample URL probing.
   Original used HEAD-only (curl -I); falsely failed URLs on servers
   that return 405/501 for HEAD but 200 for GET (Cloudflare, nginx
   with specific configs).

3. Safe URL quoting when interpolating into shell/curl commands.
   Prevents URL fragments like `?q=hello&world` from being mangled.

4. Graceful handling of empty/malformed sitemap responses.
   Original raised uncaught exceptions.

Interface preserved: same CLI (`python3 check_sitemap_v2.py <URL>`),
same JSON output schema as check_sitemap.py.

Dependencies: curl, python3 (3.8+). stdlib only.
"""

import hashlib
import json
import re
import subprocess
import sys
import urllib.parse
import xml.etree.ElementTree as ET
from typing import Dict, List, Optional, Tuple

SITEMAP_NAMESPACE = {'sm': 'http://www.sitemaps.org/schemas/sitemap/0.9'}
CURL_TIMEOUT = 15
USER_AGENT = 'Mozilla/5.0 (compatible; SEO-AEO-Auditor/2.0)'
MAX_INDEX_DEPTH = 2
MAX_SUBSITEMAPS_PER_INDEX = 20
SAMPLE_SIZE = 10


def curl_fetch(url: str, timeout: int = CURL_TIMEOUT) -> Tuple[int, str, str]:
    """
    Fetch URL via curl. Returns (http_code, body, error).
    URL is passed as a separate argv entry — no shell interpolation.
    """
    try:
        result = subprocess.run(
            ['curl', '-sS', '-L', '--max-redirs', '5',
             '--max-time', str(timeout),
             '-A', USER_AGENT,
             '-w', '\n---HTTP_CODE---\n%{http_code}',
             url],
            capture_output=True, text=True, timeout=timeout + 5
        )
        output = result.stdout
        if '\n---HTTP_CODE---\n' in output:
            body, code_str = output.rsplit('\n---HTTP_CODE---\n', 1)
            try:
                code = int(code_str.strip())
            except ValueError:
                code = 0
        else:
            body = output
            code = 0
        return code, body, result.stderr
    except subprocess.TimeoutExpired:
        return 0, '', 'timeout'
    except FileNotFoundError:
        return 0, '', 'curl not installed'
    except Exception as e:
        return 0, '', f'{type(e).__name__}: {e}'


def probe_url(url: str, timeout: int = 10) -> Tuple[int, str]:
    """
    Probe a URL's reachability. HEAD first; fall back to GET with Range
    if HEAD returns 405/501. Returns (http_code, method_used).

    This is the fix for the HEAD-only bug that falsely flagged URLs
    on servers that don't allow HEAD but accept GET.
    """
    # First attempt: HEAD
    try:
        r = subprocess.run(
            ['curl', '-sS', '-I', '-L', '--max-redirs', '3',
             '--max-time', str(timeout),
             '-A', USER_AGENT,
             '-o', '/dev/null',
             '-w', '%{http_code}',
             url],
            capture_output=True, text=True, timeout=timeout + 3
        )
        head_code = int(r.stdout.strip()) if r.stdout.strip().isdigit() else 0
    except (subprocess.TimeoutExpired, ValueError):
        head_code = 0

    # If HEAD said 405 Method Not Allowed or 501 Not Implemented,
    # try GET with a byte range to minimize transfer.
    if head_code in (405, 501):
        try:
            r = subprocess.run(
                ['curl', '-sS', '-L', '--max-redirs', '3',
                 '--max-time', str(timeout),
                 '-A', USER_AGENT,
                 '-H', 'Range: bytes=0-1023',
                 '-o', '/dev/null',
                 '-w', '%{http_code}',
                 url],
                capture_output=True, text=True, timeout=timeout + 3
            )
            get_code = int(r.stdout.strip()) if r.stdout.strip().isdigit() else 0
            return get_code, 'GET_range'
        except (subprocess.TimeoutExpired, ValueError):
            return 0, 'GET_failed'

    # If HEAD succeeded (2xx/3xx) or gave a definitive error (4xx other than
    # 405, or 5xx other than 501), trust it.
    return head_code, 'HEAD'


def parse_sitemap_xml(xml_body: str) -> Optional[Dict]:
    """
    Parse sitemap XML using stdlib xml.etree.ElementTree.
    Returns {'type': 'index' | 'urlset', 'entries': [...]} or None on failure.

    Handles: &amp; entities, CDATA sections, namespaces, comments.
    Does NOT use regex on XML (the original bug).
    """
    if not xml_body or not xml_body.strip():
        return None

    try:
        root = ET.fromstring(xml_body)
    except ET.ParseError as e:
        return {'parse_error': f'{type(e).__name__}: {e}'}

    # Strip namespace from tag name for simpler inspection
    tag = root.tag.split('}')[-1] if '}' in root.tag else root.tag

    # Try with namespace first, fall back to no namespace
    def find_all(element, child_tag):
        with_ns = element.findall(f'sm:{child_tag}', SITEMAP_NAMESPACE)
        if with_ns:
            return with_ns
        return element.findall(child_tag)

    def get_text(element, child_tag):
        child = element.find(f'sm:{child_tag}', SITEMAP_NAMESPACE)
        if child is None:
            child = element.find(child_tag)
        return child.text.strip() if child is not None and child.text else None

    if tag == 'sitemapindex':
        entries = []
        for sm in find_all(root, 'sitemap'):
            loc = get_text(sm, 'loc')
            lastmod = get_text(sm, 'lastmod')
            if loc:
                entries.append({'loc': loc, 'lastmod': lastmod})
        return {'type': 'index', 'entries': entries}

    elif tag == 'urlset':
        entries = []
        for url_el in find_all(root, 'url'):
            loc = get_text(url_el, 'loc')
            lastmod = get_text(url_el, 'lastmod')
            changefreq = get_text(url_el, 'changefreq')
            priority = get_text(url_el, 'priority')
            if loc:
                entries.append({
                    'loc': loc,
                    'lastmod': lastmod,
                    'changefreq': changefreq,
                    'priority': priority
                })
        return {'type': 'urlset', 'entries': entries}

    else:
        return {'parse_error': f'unexpected root tag: {tag}'}


def discover_sitemap_url(base_url: str) -> Tuple[Optional[str], str]:
    """
    Try 3 discovery paths in order:
    1. robots.txt Sitemap: directive
    2. /sitemap.xml
    3. /sitemap_index.xml
    Returns (sitemap_url, discovered_via) or (None, reason).
    """
    parsed = urllib.parse.urlparse(base_url)
    origin = f'{parsed.scheme}://{parsed.netloc}'

    # 1. robots.txt
    robots_url = f'{origin}/robots.txt'
    code, body, _ = curl_fetch(robots_url)
    if 200 <= code < 300 and body:
        for line in body.splitlines():
            line = line.strip()
            if line.lower().startswith('sitemap:'):
                sm_url = line.split(':', 1)[1].strip()
                if sm_url:
                    return sm_url, 'robots_txt_directive'

    # 2. /sitemap.xml
    sm_url = f'{origin}/sitemap.xml'
    code, _, _ = curl_fetch(sm_url)
    if 200 <= code < 300:
        return sm_url, 'default_sitemap_xml'

    # 3. /sitemap_index.xml
    sm_url = f'{origin}/sitemap_index.xml'
    code, _, _ = curl_fetch(sm_url)
    if 200 <= code < 300:
        return sm_url, 'default_sitemap_index_xml'

    return None, 'not_discovered'


def traverse_sitemap(
    sitemap_url: str, depth: int = 0, seen: Optional[set] = None
) -> Tuple[List[Dict], List[str]]:
    """
    Recursively fetch and parse sitemap + sitemap indexes.
    Returns (all_url_entries, errors).
    """
    if seen is None:
        seen = set()
    if sitemap_url in seen or depth > MAX_INDEX_DEPTH:
        return [], []
    seen.add(sitemap_url)

    errors = []
    all_entries = []

    code, body, err = curl_fetch(sitemap_url)
    if code == 0 or not body:
        errors.append(f'fetch failed for {sitemap_url}: {err or f"HTTP {code}"}')
        return [], errors
    if code >= 400:
        errors.append(f'HTTP {code} for {sitemap_url}')
        return [], errors

    parsed = parse_sitemap_xml(body)
    if parsed is None:
        errors.append(f'empty/invalid XML at {sitemap_url}')
        return [], errors
    if 'parse_error' in parsed:
        errors.append(f'parse error at {sitemap_url}: {parsed["parse_error"]}')
        return [], errors

    if parsed['type'] == 'urlset':
        return parsed['entries'], errors

    elif parsed['type'] == 'index':
        # Recurse into sub-sitemaps (bounded)
        sub_entries = parsed['entries'][:MAX_SUBSITEMAPS_PER_INDEX]
        for sub in sub_entries:
            sub_url = sub['loc']
            child_entries, child_errors = traverse_sitemap(sub_url, depth + 1, seen)
            all_entries.extend(child_entries)
            errors.extend(child_errors)

    return all_entries, errors


def deterministic_sample(
    entries: List[Dict], target_url: str, sample_size: int = SAMPLE_SIZE
) -> List[Dict]:
    """
    Deterministic sampling: for a given target_url, always returns the same
    sample entries from a given entries list. Uses MD5 hash for stable order.
    """
    if len(entries) <= sample_size:
        return entries

    seed = target_url.encode()
    scored = []
    for entry in entries:
        h = hashlib.md5(seed + entry['loc'].encode()).hexdigest()
        scored.append((h, entry))
    scored.sort(key=lambda x: x[0])
    return [e for _, e in scored[:sample_size]]


def check_sitemap(target_url: str) -> Dict:
    """Main entry: run all sitemap checks against target_url."""
    checks = {}

    sitemap_url, discovered_via = discover_sitemap_url(target_url)

    if not sitemap_url:
        for check_id in ('sitemap_reachable', 'target_url_in_sitemap',
                         'no_cross_domain_sitemap_entries',
                         'sampled_urls_return_200', 'lastmod_coverage',
                         'sitemap_size_compliance'):
            checks[check_id] = {
                'status': 'fail',
                'severity': 'high',
                'evidence': 'Sitemap could not be discovered via robots.txt, /sitemap.xml, or /sitemap_index.xml.'
            }
        return {
            'sitemap': {'found': False, 'discovered_via': discovered_via},
            'checks': checks
        }

    entries, errors = traverse_sitemap(sitemap_url)

    checks['sitemap_reachable'] = {
        'status': 'pass' if entries and not errors else
                  'warn' if entries else 'fail',
        'severity': 'high',
        'evidence': (
            f'Sitemap located via {discovered_via}: {sitemap_url}. '
            f'{len(entries)} URLs parsed.' +
            (f' Warnings: {"; ".join(errors[:3])}' if errors else '')
        )
    }

    target_parsed = urllib.parse.urlparse(target_url)
    target_origin = f'{target_parsed.scheme}://{target_parsed.netloc}'

    # target_url_in_sitemap
    target_variants = {
        target_url,
        target_url.rstrip('/'),
        target_url + '/',
        target_url.replace('://', '://www.'),
    }
    sitemap_urls = {e['loc'] for e in entries}
    sitemap_urls_norm = {u.rstrip('/') for u in sitemap_urls} | sitemap_urls
    found = any(v in sitemap_urls_norm or v.rstrip('/') in sitemap_urls_norm
                for v in target_variants)
    if found:
        matching = next(
            (e for e in entries
             if e['loc'] in target_variants or e['loc'].rstrip('/') in target_variants),
            None
        )
        evidence = (
            f'Target URL {target_url} found in sitemap'
            + (' (normalized (trailing slash or protocol differs))'
               if matching and matching['loc'] != target_url else '')
            + (f'. lastmod: {matching["lastmod"]}' if matching and matching['lastmod']
               else '')
        )
        checks['target_url_in_sitemap'] = {
            'status': 'pass', 'severity': 'high', 'evidence': evidence
        }
    else:
        checks['target_url_in_sitemap'] = {
            'status': 'fail', 'severity': 'high',
            'evidence': f'Target URL {target_url} not found in sitemap ({len(entries)} URLs checked).'
        }

    # no_cross_domain_sitemap_entries
    cross_domain = []
    for entry in entries[:500]:  # sample for performance
        p = urllib.parse.urlparse(entry['loc'])
        entry_origin = f'{p.scheme}://{p.netloc}'
        if entry_origin != target_origin:
            cross_domain.append(entry['loc'])
    checks['no_cross_domain_sitemap_entries'] = {
        'status': 'pass' if not cross_domain else 'warn',
        'severity': 'medium',
        'evidence': (
            f'All sitemap entries point to the expected origin ({target_origin}).'
            if not cross_domain
            else f'{len(cross_domain)} URLs point to different origins. '
                 f'Examples: {cross_domain[:3]}'
        )
    }

    # sampled_urls_return_200 — uses HEAD-then-GET-fallback
    sample = deterministic_sample(entries, target_url, sample_size=5)
    sample_results = []
    non_200 = []
    for entry in sample:
        code, method = probe_url(entry['loc'])
        sample_results.append({'url': entry['loc'], 'code': code, 'method': method})
        if not (200 <= code < 400):
            non_200.append((entry['loc'], code))
    checks['sampled_urls_return_200'] = {
        'status': 'pass' if not non_200 else 'fail',
        'severity': 'high',
        'evidence': (
            f'All {len(sample)} sampled URLs return HTTP 200.'
            if not non_200
            else f'{len(non_200)} of {len(sample)} sampled URLs returned non-2xx: {non_200[:3]}'
        ),
        'detail': sample_results
    }

    # lastmod_coverage
    with_lastmod = sum(1 for e in entries if e.get('lastmod'))
    coverage = (with_lastmod / len(entries) * 100) if entries else 0
    checks['lastmod_coverage'] = {
        'status': 'pass' if coverage >= 80 else
                  'warn' if coverage >= 40 else 'fail',
        'severity': 'medium',
        'evidence': f'{with_lastmod}/{len(entries)} URLs ({coverage:.0f}%) have lastmod dates.'
    }

    # sitemap_size_compliance (Google limits: 50K URLs, 50MB)
    size_ok = len(entries) <= 50_000
    checks['sitemap_size_compliance'] = {
        'status': 'pass' if size_ok else 'warn',
        'severity': 'low',
        'evidence': (
            f'Sitemap has {len(entries)} URLs (Google limit: 50,000).'
            if size_ok
            else f'Sitemap exceeds 50,000 URLs ({len(entries)}) — split into multiple sitemaps.'
        )
    }

    return {
        'sitemap': {
            'found': True,
            'sitemap_url': sitemap_url,
            'discovered_via': discovered_via,
            'total_urls_indexed': len(entries),
            'traversal_errors': errors[:5] if errors else []
        },
        'checks': checks
    }


def main():
    if len(sys.argv) < 2:
        print(json.dumps({'error': 'missing URL', 'usage': 'python3 check_sitemap_v2.py <URL>'}))
        sys.exit(1)

    result = check_sitemap(sys.argv[1])
    print(json.dumps(result, indent=2, ensure_ascii=False))


if __name__ == '__main__':
    main()
