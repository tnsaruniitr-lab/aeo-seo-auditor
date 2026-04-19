#!/usr/bin/env python3
"""
check_robots_txt.py — Deterministic robots.txt analysis

Fetches robots.txt, parses User-agent groups with correct precedence semantics,
and emits per-bot allow/deny status for 10 major AI crawlers + Google + Bing.

Usage:
  python3 scripts/check_robots_txt.py <URL>

Output: JSON to stdout.

Deterministic: same robots.txt input produces identical JSON across runs.

What it catches that prose reading might miss:
  - Multi-agent grouped blocks (User-agent: GPTBot \\n User-agent: ChatGPT-User \\n Allow: /)
  - Path-specific Disallows that target the audit URL
  - Precedence rules (more-specific agent match wins over wildcard)
  - Grouped bot-specific Disallow rules amid overall permissive wildcard
"""

import sys
import re
import json
import urllib.request
from urllib.error import URLError, HTTPError


# The 10 AI crawlers + Google/Bing primary bots we check for explicit allow/deny
# Plus wildcard-handled bots that may fall through
BOTS_TO_CHECK = [
    'Googlebot',
    'Bingbot',
    'BingPreview',
    'GPTBot',
    'ChatGPT-User',
    'ClaudeBot',
    'Claude-Web',
    'anthropic-ai',
    'PerplexityBot',
    'Google-Extended',
    'OAI-SearchBot',
    'CCBot',
    'Applebot',
    'Applebot-Extended',
    'DuckDuckBot',
    'Bytespider',
]


def fetch_robots(origin_url, timeout=10):
    """Fetch robots.txt from the origin. Returns (text, http_status, error)."""
    # Parse origin from URL
    m = re.match(r'(https?://[^/]+)', origin_url)
    if not m:
        return None, 0, 'could_not_parse_origin'
    origin = m.group(1)
    robots_url = f'{origin}/robots.txt'

    req = urllib.request.Request(
        robots_url,
        headers={'User-Agent': 'Mozilla/5.0 (AuditBot/1.0)'}
    )
    try:
        resp = urllib.request.urlopen(req, timeout=timeout)
        text = resp.read().decode('utf-8', errors='replace')
        return text, resp.status, None
    except HTTPError as e:
        return '', e.code, f'http_{e.code}'
    except URLError as e:
        return None, 0, f'url_error: {e.reason}'
    except Exception as e:
        return None, 0, f'exception: {e}'


def parse_robots_txt(text):
    """
    Parse robots.txt into a list of agent groups.

    Returns list of {agents: [...], allow: [...], disallow: [...], crawl_delay: N or None}.

    Handles multi-agent groups (consecutive User-agent lines before rules).
    """
    if not text:
        return []

    groups = []
    current_agents = []
    current_rules = {'allow': [], 'disallow': [], 'crawl_delay': None}
    expecting_rules = False

    sitemaps = []

    for raw_line in text.splitlines():
        # Strip comments and whitespace
        line = raw_line.split('#', 1)[0].strip()
        if not line:
            continue

        if ':' not in line:
            continue

        directive, _, value = line.partition(':')
        directive = directive.strip().lower()
        value = value.strip()

        if directive == 'sitemap':
            sitemaps.append(value)
            continue

        if directive == 'user-agent':
            if expecting_rules:
                # We've started seeing rules — this User-agent starts a new group
                groups.append({
                    'agents': current_agents[:],
                    'allow': current_rules['allow'][:],
                    'disallow': current_rules['disallow'][:],
                    'crawl_delay': current_rules['crawl_delay'],
                })
                current_agents = []
                current_rules = {'allow': [], 'disallow': [], 'crawl_delay': None}
                expecting_rules = False
            current_agents.append(value)
            continue

        # Any rule directive means we're now in the "rules" phase of the current group
        if directive in ('allow', 'disallow', 'crawl-delay'):
            expecting_rules = True
            if directive == 'allow':
                current_rules['allow'].append(value)
            elif directive == 'disallow':
                current_rules['disallow'].append(value)
            elif directive == 'crawl-delay':
                try:
                    current_rules['crawl_delay'] = float(value)
                except ValueError:
                    pass

    # Flush final group
    if current_agents:
        groups.append({
            'agents': current_agents[:],
            'allow': current_rules['allow'][:],
            'disallow': current_rules['disallow'][:],
            'crawl_delay': current_rules['crawl_delay'],
        })

    return groups, sitemaps


def find_matching_groups(groups, bot_name):
    """
    Find groups that apply to a given bot.

    Google/robots.txt precedence rules:
      - Bot name match is case-insensitive and prefix-based (Googlebot matches Googlebot-Image)
      - BUT for our purposes, we treat exact case-insensitive match first, then wildcard (*) as fallback
      - If a specific group matches, wildcard group is IGNORED for that bot
    """
    specific_matches = []
    wildcard_matches = []

    for g in groups:
        for agent in g['agents']:
            if agent == '*':
                wildcard_matches.append(g)
                break
            if agent.lower() == bot_name.lower():
                specific_matches.append(g)
                break
            # Google treats Googlebot as matching Googlebot, Googlebot-Image, etc.
            # For our purposes we do exact case-insensitive match to avoid false positives

    # If any specific group matched, use those only
    if specific_matches:
        return specific_matches, 'explicit'
    return wildcard_matches, 'wildcard'


def evaluate_path_access(matching_groups, path):
    """
    For a given set of groups that apply to this bot, decide if path is allowed.

    robots.txt semantics:
      - If no rules exist, path is allowed by default
      - Most-specific (longest matching) rule wins
      - Allow and Disallow are combined — longest match across both wins
      - If Allow and Disallow are equally specific, Allow wins (Google's rule)
    """
    all_rules = []
    for g in matching_groups:
        for a in g['allow']:
            all_rules.append(('allow', a))
        for d in g['disallow']:
            all_rules.append(('disallow', d))

    if not all_rules:
        return {'allowed': True, 'matching_rule': None, 'reason': 'no_rules'}

    # Check if any rule matches the path
    def matches_path(pattern, path):
        if pattern == '':
            # Empty Disallow means allow everything
            return False
        # Simplified matching: prefix match, with * and $ wildcards
        # Full googlebot semantics are more complex but this covers 95% of real robots.txt
        pattern_regex = re.escape(pattern).replace('\\*', '.*')
        if pattern.endswith('$'):
            pattern_regex = pattern_regex[:-2] + '$'  # $ at end means exact suffix
        else:
            pattern_regex = pattern_regex
        return bool(re.match(pattern_regex, path))

    matching = []
    for rule_type, pattern in all_rules:
        if matches_path(pattern, path):
            matching.append((rule_type, pattern))

    if not matching:
        return {'allowed': True, 'matching_rule': None, 'reason': 'no_matching_rule'}

    # Sort by length of pattern descending — longest match wins
    matching.sort(key=lambda x: len(x[1]), reverse=True)
    longest_len = len(matching[0][1])
    most_specific = [m for m in matching if len(m[1]) == longest_len]

    # If allow and disallow tie at same specificity, allow wins (Google rule)
    has_allow = any(m[0] == 'allow' for m in most_specific)
    has_disallow = any(m[0] == 'disallow' for m in most_specific)

    if has_allow:
        allow_rule = [m for m in most_specific if m[0] == 'allow'][0]
        return {'allowed': True, 'matching_rule': f'Allow: {allow_rule[1]}', 'reason': 'allow_wins'}
    if has_disallow:
        disallow_rule = [m for m in most_specific if m[0] == 'disallow'][0]
        # Empty disallow means allow all
        if disallow_rule[1] == '':
            return {'allowed': True, 'matching_rule': 'Disallow: (empty)', 'reason': 'empty_disallow_allows_all'}
        return {'allowed': False, 'matching_rule': f'Disallow: {disallow_rule[1]}', 'reason': 'disallow_wins'}

    return {'allowed': True, 'matching_rule': None, 'reason': 'fallthrough'}


def extract_path(url):
    """Extract path portion from a URL."""
    m = re.match(r'https?://[^/]+(/.*)?', url)
    if m:
        return m.group(1) or '/'
    return '/'


def check_robots_for_url(url):
    """Main entry point — runs the full analysis for a given URL."""
    text, status, error = fetch_robots(url)

    if error == 'could_not_parse_origin':
        return {
            'url': url,
            'robots_txt': {
                'reachable': False,
                'http_status': 0,
                'error': 'could_not_parse_origin_from_url',
            },
            'checks': {}
        }

    if text is None:
        return {
            'url': url,
            'robots_txt': {
                'reachable': False,
                'http_status': status,
                'error': error,
            },
            'checks': {
                'robots_reachable': {
                    'status': 'fail',
                    'evidence': f'robots.txt fetch failed: {error}',
                    'detail': {}
                }
            }
        }

    if status == 404:
        return {
            'url': url,
            'robots_txt': {
                'reachable': True,
                'http_status': 404,
                'text': '',
                'raw_length': 0,
            },
            'checks': {
                'robots_reachable': {
                    'status': 'warn',
                    'evidence': 'robots.txt returns 404 — defaults to permissive (all bots allowed).',
                    'detail': {}
                }
            }
        }

    groups, sitemaps = parse_robots_txt(text)
    target_path = extract_path(url)

    # Per-bot evaluation
    bot_results = {}
    for bot in BOTS_TO_CHECK:
        matching_groups, match_type = find_matching_groups(groups, bot)
        access = evaluate_path_access(matching_groups, target_path)

        # Determine "explicit allow" vs "wildcard inferred"
        explicit_match = match_type == 'explicit'

        bot_results[bot] = {
            'explicitly_listed': explicit_match,
            'match_type': match_type,
            'allowed_for_path': access['allowed'],
            'matching_rule': access['matching_rule'],
            'reason': access['reason'],
            'path_checked': target_path,
        }

    # Build checks dict
    checks = {}

    # Check 1: reachable
    checks['robots_reachable'] = {
        'status': 'pass',
        'evidence': f'robots.txt reachable, HTTP {status}, {len(text)} bytes.',
        'detail': {'http_status': status, 'bytes': len(text)}
    }

    # Check 2: sitemap declared
    if sitemaps:
        checks['robots_declares_sitemap'] = {
            'status': 'pass',
            'evidence': f'robots.txt declares {len(sitemaps)} sitemap(s): {sitemaps}',
            'detail': {'sitemaps': sitemaps}
        }
    else:
        checks['robots_declares_sitemap'] = {
            'status': 'warn',
            'evidence': 'robots.txt does not declare a Sitemap directive.',
            'detail': {'sitemaps': []}
        }

    # Check 3: Googlebot access (critical — if not allowed, page won't rank)
    gbot = bot_results['Googlebot']
    if gbot['allowed_for_path']:
        if gbot['explicitly_listed']:
            checks['googlebot_allowed'] = {
                'status': 'pass',
                'evidence': f'Googlebot explicitly listed and allowed for {target_path}.',
                'detail': gbot
            }
        else:
            checks['googlebot_allowed'] = {
                'status': 'pass',
                'evidence': f'Googlebot allowed for {target_path} via wildcard (not explicitly listed).',
                'detail': gbot
            }
    else:
        checks['googlebot_allowed'] = {
            'status': 'fail',
            'evidence': f'Googlebot BLOCKED from {target_path}. Matching rule: {gbot["matching_rule"]}.',
            'detail': gbot
        }

    # Check 4: AI crawler coverage — explicit listings
    ai_crawlers = ['GPTBot', 'ChatGPT-User', 'ClaudeBot', 'PerplexityBot', 'Google-Extended',
                   'OAI-SearchBot', 'CCBot', 'Applebot-Extended', 'anthropic-ai', 'BingPreview']
    explicitly_listed = [b for b in ai_crawlers if bot_results[b]['explicitly_listed']]
    allowed_via_wildcard = [b for b in ai_crawlers if not bot_results[b]['explicitly_listed'] and bot_results[b]['allowed_for_path']]
    blocked = [b for b in ai_crawlers if not bot_results[b]['allowed_for_path']]

    if blocked:
        checks['ai_crawlers_all_allowed'] = {
            'status': 'fail',
            'evidence': f'{len(blocked)} AI crawler(s) BLOCKED: {blocked}',
            'detail': {
                'blocked': blocked,
                'explicitly_listed_and_allowed': explicitly_listed,
                'allowed_via_wildcard_only': allowed_via_wildcard,
            }
        }
    elif len(explicitly_listed) == 0:
        checks['ai_crawlers_all_allowed'] = {
            'status': 'warn',
            'evidence': f'All {len(ai_crawlers)} AI crawlers allowed via wildcard only. None explicitly listed. Explicit entries are more reliable.',
            'detail': {
                'blocked': [],
                'explicitly_listed_and_allowed': [],
                'allowed_via_wildcard_only': allowed_via_wildcard,
            }
        }
    elif len(explicitly_listed) < len(ai_crawlers):
        checks['ai_crawlers_all_allowed'] = {
            'status': 'warn',
            'evidence': f'{len(explicitly_listed)} of {len(ai_crawlers)} AI crawlers explicitly listed: {explicitly_listed}. Others ({allowed_via_wildcard}) only allowed via wildcard.',
            'detail': {
                'blocked': [],
                'explicitly_listed_and_allowed': explicitly_listed,
                'allowed_via_wildcard_only': allowed_via_wildcard,
            }
        }
    else:
        checks['ai_crawlers_all_allowed'] = {
            'status': 'pass',
            'evidence': f'All {len(ai_crawlers)} AI crawlers explicitly listed and allowed.',
            'detail': {
                'blocked': [],
                'explicitly_listed_and_allowed': explicitly_listed,
                'allowed_via_wildcard_only': [],
            }
        }

    # Check 5: target path not in any Disallow
    # Already covered by googlebot_allowed effectively, but explicit
    any_disallow = [b for b, r in bot_results.items() if not r['allowed_for_path']]
    if any_disallow:
        checks['target_path_not_disallowed'] = {
            'status': 'fail',
            'evidence': f'Target path {target_path} disallowed for: {any_disallow}',
            'detail': {'bots_blocked_from_path': any_disallow}
        }
    else:
        checks['target_path_not_disallowed'] = {
            'status': 'pass',
            'evidence': f'Target path {target_path} is allowed for all {len(BOTS_TO_CHECK)} checked bots.',
            'detail': {'target_path': target_path}
        }

    return {
        'url': url,
        'robots_txt': {
            'reachable': True,
            'http_status': status,
            'text_length_bytes': len(text),
            'group_count': len(groups),
            'sitemap_directives': sitemaps,
            'target_path': target_path,
        },
        'per_bot_analysis': bot_results,
        'checks': checks,
    }


def main():
    if len(sys.argv) < 2:
        print(json.dumps({'error': 'Usage: python3 check_robots_txt.py <URL>'}))
        sys.exit(1)
    url = sys.argv[1]
    result = check_robots_for_url(url)
    print(json.dumps(result, indent=2, ensure_ascii=False))


if __name__ == '__main__':
    main()
