#!/usr/bin/env bash
# run_deterministic.sh — Orchestrator for all deterministic audit scripts
#
# Runs 4 independent checkers in parallel and emits a combined JSON blob:
#   1. bots_eye_view.sh        — Bot's Eye View (per-bot UA fetches + SSR classification)
#   2. deterministic_checks.py — 9 targeted checks (FAQ, H1 nesting, TTFB, etc.)
#   3. check_robots_txt.py     — Per-bot allow/deny for 10+ AI crawlers
#   4. check_sitemap.py        — Target URL presence + sample URL validity
#   5. check_schema_completeness.py — Per-@type required/recommended field validation
#
# Usage:
#   bash scripts/run_deterministic.sh <URL>              # emits combined JSON
#   bash scripts/run_deterministic.sh <URL> human        # emits human-readable summary

set -euo pipefail

if [ "${1:-}" = "" ]; then
  echo '{"error":"missing URL","usage":"bash run_deterministic.sh <URL> [human]"}'
  exit 1
fi

URL="$1"
MODE="${2:-json}"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Create temp files for parallel execution
BEV_FILE=$(mktemp)
DET_FILE=$(mktemp)
ROBOTS_FILE=$(mktemp)
SITEMAP_FILE=$(mktemp)
SCHEMA_FILE=$(mktemp)

# Run all 5 in parallel
bash "${SCRIPT_DIR}/bots_eye_view.sh" "$URL" > "$BEV_FILE" 2>/dev/null &
P1=$!

python3 "${SCRIPT_DIR}/deterministic_checks.py" "$URL" > "$DET_FILE" 2>/dev/null &
P2=$!

python3 "${SCRIPT_DIR}/check_robots_txt.py" "$URL" > "$ROBOTS_FILE" 2>/dev/null &
P3=$!

python3 "${SCRIPT_DIR}/check_sitemap.py" "$URL" > "$SITEMAP_FILE" 2>/dev/null &
P4=$!

python3 "${SCRIPT_DIR}/check_schema_completeness.py" "$URL" > "$SCHEMA_FILE" 2>/dev/null &
P5=$!

wait $P1 $P2 $P3 $P4 $P5

# Combine all into single JSON
python3 -c "
import json

def safe_load(path):
    try:
        with open(path) as f:
            return json.load(f)
    except Exception as e:
        return {'error': f'script output unparseable: {e}'}

bev = safe_load('$BEV_FILE')
det = safe_load('$DET_FILE')
robots = safe_load('$ROBOTS_FILE')
sitemap = safe_load('$SITEMAP_FILE')
schema = safe_load('$SCHEMA_FILE')

# Aggregate check results across all 5 scripts
all_checks = {}
def collect(src_name, src_dict):
    if not isinstance(src_dict, dict):
        return
    checks = src_dict.get('checks', {})
    for cid, result in checks.items():
        all_checks[f'{src_name}:{cid}'] = result

collect('det_checks', det)
collect('robots', robots)
collect('sitemap', sitemap)
collect('schema', schema)

# Count by status
pass_count = sum(1 for c in all_checks.values() if c.get('status') == 'pass')
fail_count = sum(1 for c in all_checks.values() if c.get('status') == 'fail')
warn_count = sum(1 for c in all_checks.values() if c.get('status') == 'warn')
na_count = sum(1 for c in all_checks.values() if c.get('status') == 'na')

# Collect all critical issues
critical_issues = []
critical_issues.extend(bev.get('summary', {}).get('critical_issues', []))
for cid, result in all_checks.items():
    if result.get('status') == 'fail':
        critical_issues.append(f'[{cid}] {result.get(\"evidence\", \"\")[:200]}')

combined = {
    'url': '$URL',
    'bots_eye_view': bev,
    'deterministic_checks': det,
    'robots_txt_analysis': robots,
    'sitemap_analysis': sitemap,
    'schema_completeness': schema,
    'overall_summary': {
        'classification': bev.get('classification'),
        'total_checks_run': len(all_checks),
        'pass': pass_count,
        'fail': fail_count,
        'warn': warn_count,
        'na': na_count,
        'all_critical_issues': critical_issues,
    },
    'all_checks': all_checks,
}

if '$MODE' == 'human':
    print('=' * 75)
    print(f'DETERMINISTIC AUDIT — {combined[\"url\"]}')
    print('=' * 75)
    print()

    print('PHASE 1 — Bot\\'s Eye View')
    print('-' * 75)
    if 'page_identity' in bev:
        print(f'Classification: {bev[\"classification\"]}')
        print(f'Title: {bev[\"page_identity\"][\"title\"]}')
        print(f'H1 count: {bev[\"page_identity\"][\"h1_count\"]} — first: {bev[\"page_identity\"][\"h1_first\"]}')
        print(f'Visible words (raw HTML): {bev[\"content_visible_to_bots\"][\"visible_word_count\"]}')
        print(f'FAQ visible: {bev[\"content_visible_to_bots\"][\"faq_visible_pairs\"]} pairs (via {bev[\"content_visible_to_bots\"][\"faq_visible_detection_method\"]})')
        print(f'FAQ in schema: {bev[\"content_visible_to_bots\"][\"faq_schema_pairs\"]} pairs')
        print(f'Same HTML as 404: {bev[\"summary\"][\"same_html_as_404_url\"]}')
        print(f'Cloaking: {bev[\"summary\"][\"cloaking_detected\"]}')
        print()
        print('Bytes served per bot UA:')
        for bot, data in bev['response_per_bot'].items():
            print(f'  {bot:15s}: {data[\"http_code\"]} / {data[\"size_bytes\"]:>7d} bytes / {data[\"ttfb_seconds\"]:.3f}s')
    print()

    print('PHASE 2 — Targeted Deterministic Checks')
    print('-' * 75)
    summary = det.get('summary', {})
    print(f'Summary: {summary.get(\"pass\",0)} pass, {summary.get(\"fail\",0)} fail, {summary.get(\"warn\",0)} warn, {summary.get(\"na\",0)} N/A')
    for cid, result in det.get('checks', {}).items():
        icons = {'pass':'✓','fail':'✗','warn':'⚠','na':'—'}
        ic = icons.get(result['status'], '?')
        print(f'  {ic} {cid}: {result[\"evidence\"][:180]}')
    print()

    print('PHASE 3 — robots.txt Analysis')
    print('-' * 75)
    for cid, result in robots.get('checks', {}).items():
        icons = {'pass':'✓','fail':'✗','warn':'⚠','na':'—'}
        ic = icons.get(result['status'], '?')
        print(f'  {ic} {cid}: {result[\"evidence\"][:180]}')
    print()

    print('PHASE 4 — Sitemap Validity')
    print('-' * 75)
    sm_info = sitemap.get('sitemap', {})
    if sm_info.get('found'):
        print(f'Sitemap URL: {sm_info.get(\"sitemap_url\")}')
        print(f'Total URLs: {sm_info.get(\"total_urls_indexed\")}')
    for cid, result in sitemap.get('checks', {}).items():
        icons = {'pass':'✓','fail':'✗','warn':'⚠','na':'—'}
        ic = icons.get(result['status'], '?')
        print(f'  {ic} {cid}: {result[\"evidence\"][:180]}')
    print()

    print('PHASE 5 — Schema Completeness (per-@type)')
    print('-' * 75)
    ss = schema.get('schema_summary', {})
    print(f'Entities: {ss.get(\"total_entities\",0)} total | {ss.get(\"valid\",0)} valid | {ss.get(\"incomplete\",0)} incomplete | {ss.get(\"invalid\",0)} invalid | {ss.get(\"unknown_types\",0)} unknown')
    print(f'Types found: {ss.get(\"entity_types_found\",[])}')
    for cid, result in schema.get('checks', {}).items():
        icons = {'pass':'✓','fail':'✗','warn':'⚠','na':'—'}
        ic = icons.get(result['status'], '?')
        print(f'  {ic} {cid}: {result[\"evidence\"][:180]}')
    print()

    print('OVERALL SUMMARY')
    print('-' * 75)
    os_dict = combined['overall_summary']
    print(f'Classification: {os_dict[\"classification\"]}')
    print(f'Total deterministic checks: {os_dict[\"total_checks_run\"]}')
    print(f'  ✓ Pass: {os_dict[\"pass\"]}')
    print(f'  ✗ Fail: {os_dict[\"fail\"]}')
    print(f'  ⚠ Warn: {os_dict[\"warn\"]}')
    print(f'  — N/A:  {os_dict[\"na\"]}')
    print()

    critical = os_dict['all_critical_issues']
    if critical:
        print(f'CRITICAL ISSUES ({len(critical)}):')
        for i, issue in enumerate(critical[:15], 1):
            print(f'  {i}. {issue[:200]}')
    else:
        print('No critical issues detected.')

else:
    print(json.dumps(combined, indent=2, ensure_ascii=False))
"

rm -f "$BEV_FILE" "$DET_FILE" "$ROBOTS_FILE" "$SITEMAP_FILE" "$SCHEMA_FILE"
