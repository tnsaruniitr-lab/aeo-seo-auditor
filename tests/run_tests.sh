#!/usr/bin/env bash
# run_tests.sh — stdlib-only test runner for the auditor fixtures.
#
# Executes each fixture against the relevant v2 script and asserts
# the expected outcome. No pytest, no external deps.
#
# Usage: bash tests/run_tests.sh
#
# Exit code: 0 if all tests pass, non-zero if any fail.

set -uo pipefail  # note: NOT -e so we can count failures

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
FIX_DIR="${SCRIPT_DIR}/fixtures"
V2_DIR="${SCRIPT_DIR}/../scripts-v2"

PASS=0
FAIL=0
FAILURES=()

assert_contains() {
    local label="$1"
    local haystack="$2"
    local needle="$3"
    if [[ "$haystack" == *"$needle"* ]]; then
        PASS=$((PASS+1))
        echo "  ✓ ${label}"
    else
        FAIL=$((FAIL+1))
        FAILURES+=("${label} — expected '${needle}' in output")
        echo "  ✗ ${label}"
        echo "    Expected substring: ${needle}"
        echo "    Actual (first 200 chars): ${haystack:0:200}"
    fi
}

assert_equals() {
    local label="$1"
    local actual="$2"
    local expected="$3"
    if [[ "$actual" == "$expected" ]]; then
        PASS=$((PASS+1))
        echo "  ✓ ${label}"
    else
        FAIL=$((FAIL+1))
        FAILURES+=("${label} — expected '${expected}', got '${actual}'")
        echo "  ✗ ${label}"
        echo "    Expected: ${expected}"
        echo "    Actual:   ${actual}"
    fi
}

python_fn() {
    # Run inline Python that imports from scripts-v2
    PYTHONPATH="${V2_DIR}" python3 -c "$1" 2>&1
}

echo "=============================================="
echo "Auditor fixture tests"
echo "=============================================="
echo ""

# ----------------------------------------------------------------------
# TEST 1: Empty robots.txt must not crash
# ----------------------------------------------------------------------
echo "[1] empty_robots.txt — parser must not crash"
OUT=$(python_fn "
import sys
sys.path.insert(0, '${V2_DIR}')
try:
    from check_robots_txt_v2 import parse_robots_txt
    result = parse_robots_txt('')
    print('GROUPS_COUNT=' + str(len(result.get('groups', []))))
    print('STATUS=ok')
except ImportError as e:
    print('SKIP_MISSING_MODULE=' + str(e))
except Exception as e:
    print('CRASH=' + type(e).__name__ + ':' + str(e))
")
if [[ "$OUT" == *"SKIP_MISSING_MODULE"* ]]; then
    echo "  — SKIPPED (scripts-v2/check_robots_txt_v2.py not yet implemented)"
elif [[ "$OUT" == *"CRASH"* ]]; then
    FAIL=$((FAIL+1))
    FAILURES+=("empty robots.txt crashed parser: $OUT")
    echo "  ✗ parser crashed on empty input"
    echo "    $OUT"
else
    assert_contains "empty robots returns groups structure" "$OUT" "GROUPS_COUNT="
    assert_contains "empty robots parsed without error" "$OUT" "STATUS=ok"
fi

# ----------------------------------------------------------------------
# TEST 2: Sitemap with entities and CDATA — regex would corrupt
# ----------------------------------------------------------------------
echo ""
echo "[2] sitemap_with_entities.xml — real XML parser required"
OUT=$(python_fn "
import xml.etree.ElementTree as ET
tree = ET.parse('${FIX_DIR}/sitemap_with_entities.xml')
ns = {'sm': 'http://www.sitemaps.org/schemas/sitemap/0.9'}
urls = [u.find('sm:loc', ns).text.strip() for u in tree.getroot().findall('sm:url', ns)]
print('COUNT=' + str(len(urls)))
for u in urls:
    print('URL=' + u)
")
assert_contains "URL count correct" "$OUT" "COUNT=4"
assert_contains "entity-encoded ampersand preserved in full URL" "$OUT" "URL=https://example.com/search?q=hello&lang=en"
assert_contains "CDATA URL extracted correctly" "$OUT" "URL=https://example.com/articles/what-is-seo&aeo"
assert_contains "second entity URL preserved" "$OUT" "URL=https://example.com/products/widget?id=123&utm=email"

# ----------------------------------------------------------------------
# TEST 3: Country accordion must NOT count as FAQ
# ----------------------------------------------------------------------
echo ""
echo "[3] country_accordion_not_faq.html — current code returns 4, patch returns 0"
OUT=$(python_fn "
import sys
sys.path.insert(0, '${V2_DIR}')
try:
    from bev_analyze_v2 import faq_visible_count
    with open('${FIX_DIR}/country_accordion_not_faq.html') as f:
        html = f.read()
    count, method = faq_visible_count(html)
    print('COUNT=' + str(count))
    print('METHOD=' + method)
except ImportError as e:
    print('SKIP_MISSING_MODULE=' + str(e))
")
if [[ "$OUT" == *"SKIP_MISSING_MODULE"* ]]; then
    echo "  — SKIPPED (scripts-v2/bev_analyze_v2.py not yet implemented)"
else
    assert_contains "country accordion does not register as FAQ" "$OUT" "COUNT=0"
fi

# ----------------------------------------------------------------------
# TEST 4: Real FAQ accordion must count as 6
# ----------------------------------------------------------------------
echo ""
echo "[4] real_faq_accordion.html — 6 real Q&As must count"
OUT=$(python_fn "
import sys
sys.path.insert(0, '${V2_DIR}')
try:
    from bev_analyze_v2 import faq_visible_count
    with open('${FIX_DIR}/real_faq_accordion.html') as f:
        html = f.read()
    count, method = faq_visible_count(html)
    print('COUNT=' + str(count))
    print('METHOD=' + method)
except ImportError as e:
    print('SKIP_MISSING_MODULE=' + str(e))
")
if [[ "$OUT" == *"SKIP_MISSING_MODULE"* ]]; then
    echo "  — SKIPPED"
else
    assert_contains "real FAQ accordion counts all 6" "$OUT" "COUNT=6"
fi

# ----------------------------------------------------------------------
# TEST 5: Next.js streaming hreflang must be detected
# ----------------------------------------------------------------------
echo ""
echo "[5] nextjs_streaming_hreflang.html — 9 hreflang in streaming data"
OUT=$(python_fn "
import sys
sys.path.insert(0, '${V2_DIR}')
try:
    from deterministic_checks_v2 import detect_hreflang
    with open('${FIX_DIR}/nextjs_streaming_hreflang.html') as f:
        html = f.read()
    result = detect_hreflang(html)
    print('TOTAL=' + str(result.get('total_count', 0)))
    print('TOPLEVEL=' + str(result.get('toplevel_count', 0)))
    print('STREAMED=' + str(result.get('streamed_count', 0)))
except ImportError as e:
    print('SKIP_MISSING_MODULE=' + str(e))
")
if [[ "$OUT" == *"SKIP_MISSING_MODULE"* ]]; then
    echo "  — SKIPPED"
else
    assert_contains "Next.js streaming hreflang count" "$OUT" "STREAMED=9"
    assert_contains "top-level hreflang is zero (encoded in streaming)" "$OUT" "TOPLEVEL=0"
fi

# ----------------------------------------------------------------------
# TEST 6: SPA shell same-as-404 classification
# ----------------------------------------------------------------------
echo ""
echo "[6] spa_shell_same_as_404.html — must classify as spa_no_ssr"
OUT=$(python_fn "
import sys
sys.path.insert(0, '${V2_DIR}')
try:
    from bev_analyze_v2 import classify_ssr
    # When real URL and 404 URL return identical HTML
    result = classify_ssr(
        visible_words=8,
        same_as_404=True,
        spa_signals=['angular_app_root'],
        h1_first=None,
        html_snippet='<app-root></app-root>'
    )
    print('CLASS=' + result)
except ImportError as e:
    print('SKIP_MISSING_MODULE=' + str(e))
")
if [[ "$OUT" == *"SKIP_MISSING_MODULE"* ]]; then
    echo "  — SKIPPED"
else
    assert_contains "SPA shell classified as spa_no_ssr" "$OUT" "CLASS=spa_no_ssr"
fi

# ----------------------------------------------------------------------
# TEST 7: Full SSR landing must classify as fully_accessible
# ----------------------------------------------------------------------
echo ""
echo "[7] ssr_full_landing.html — must classify as fully_accessible"
OUT=$(python_fn "
import sys
sys.path.insert(0, '${V2_DIR}')
try:
    from bev_analyze_v2 import classify_ssr, visible_word_count
    with open('${FIX_DIR}/ssr_full_landing.html') as f:
        html = f.read()
    wc = visible_word_count(html)
    result = classify_ssr(
        visible_words=wc,
        same_as_404=False,
        spa_signals=[],
        h1_first='At-Home Healthcare Across UAE, KSA, Qatar, and Kuwait',
        html_snippet=html
    )
    print('WORDS=' + str(wc))
    print('CLASS=' + result)
except ImportError as e:
    print('SKIP_MISSING_MODULE=' + str(e))
")
if [[ "$OUT" == *"SKIP_MISSING_MODULE"* ]]; then
    echo "  — SKIPPED"
else
    assert_contains "full SSR landing classified as fully_accessible" "$OUT" "CLASS=fully_accessible"
fi

# ----------------------------------------------------------------------
# TEST 8: Unified orchestrator smoke test (canonical audit path)
# ----------------------------------------------------------------------
# Why this exists: previous regressions slipped through because every test
# above this one imports library helpers directly. Nothing exercised
# skill-unified/scripts/run_deterministic.sh, so the broken BEV CLI and the
# missing macOS `timeout` both passed CI silently. This test stubs each of
# the 5 children with a tiny script that emits fixed JSON, runs the
# canonical orchestrator, and asserts the integration contract:
#   * orchestrator emits valid JSON
#   * every child's _child_status is "ok"
#   * bots_eye_view.classification is present in the output
#   * overall_summary.any_child_degraded is false
echo ""
echo "[8] unified orchestrator — canonical audit path smoke test"
ORCH="${SCRIPT_DIR}/../skill-unified/scripts/run_deterministic.sh"
if [ ! -f "$ORCH" ]; then
    echo "  — SKIPPED (skill-unified orchestrator not present)"
else
    STUB_DIR=$(mktemp -d "${TMPDIR:-/tmp}/auditor-smoke-XXXXXX")
    trap 'rm -rf "'"$STUB_DIR"'"' EXIT

    # Stub for BEV — the orchestrator invokes this via `bash <script> <url>`
    cat > "${STUB_DIR}/bev.sh" <<'SH'
#!/usr/bin/env bash
cat <<'JSON'
{"classification":"fully_accessible","summary":{"visible_words_default":620,"faq_integrity":"ok","critical_issues":[]},"probes":{}}
JSON
SH
    chmod +x "${STUB_DIR}/bev.sh"

    # Stub Python children — orchestrator invokes `python3 <script> <url>`.
    # All four use the same body for brevity.
    for name in det robots sitemap schema; do
        cat > "${STUB_DIR}/${name}.py" <<PY
import json
print(json.dumps({"checks": {"${name}_smoke_check": {"status": "pass", "evidence": "stub ok"}}}))
PY
    done

    SMOKE_OUT=$(BEV_SCRIPT_OVERRIDE="${STUB_DIR}/bev.sh" \
        DET_SCRIPT_OVERRIDE="${STUB_DIR}/det.py" \
        ROBOTS_SCRIPT_OVERRIDE="${STUB_DIR}/robots.py" \
        SITEMAP_SCRIPT_OVERRIDE="${STUB_DIR}/sitemap.py" \
        SCHEMA_SCRIPT_OVERRIDE="${STUB_DIR}/schema.py" \
        bash "$ORCH" "https://smoke.example.com/" 2>&1)

    # Parse via python on stdin (avoids any heredoc quoting hazards) so
    # assertions key off real JSON paths, not fragile greps.
    SMOKE_PARSED=$(printf '%s' "$SMOKE_OUT" | python3 -c "
import json, sys
raw = sys.stdin.read()
try:
    o = json.loads(raw)
except Exception as e:
    print(f'PARSE_FAIL={e}')
    sys.exit(0)
ch = (o.get('overall_summary') or {}).get('child_health') or {}
print('DEGRADED=' + str((o.get('overall_summary') or {}).get('any_child_degraded')))
print('CLASS=' + str((o.get('bots_eye_view') or {}).get('classification')))
for name in ('bev', 'det', 'robots', 'sitemap', 'schema'):
    print(f'CHILD_{name}=' + str((ch.get(name) or {}).get('status')))
")

    if [[ "$SMOKE_PARSED" == *"PARSE_FAIL"* ]]; then
        FAIL=$((FAIL+1))
        FAILURES+=("orchestrator output not valid JSON: $SMOKE_PARSED")
        echo "  ✗ orchestrator did not produce valid JSON"
        echo "    $SMOKE_PARSED"
        echo "    First 200 chars of raw: ${SMOKE_OUT:0:200}"
    else
        assert_contains "orchestrator: bots_eye_view.classification present" "$SMOKE_PARSED" "CLASS=fully_accessible"
        assert_contains "orchestrator: any_child_degraded is False" "$SMOKE_PARSED" "DEGRADED=False"
        for name in bev det robots sitemap schema; do
            assert_contains "orchestrator: child '${name}' health=ok" "$SMOKE_PARSED" "CHILD_${name}=ok"
        done
    fi
fi

# ----------------------------------------------------------------------
# Summary
# ----------------------------------------------------------------------
echo ""
echo "=============================================="
echo "Results: ${PASS} passed, ${FAIL} failed"
echo "=============================================="
if (( FAIL > 0 )); then
    echo ""
    echo "Failures:"
    for f in "${FAILURES[@]}"; do
        echo "  - $f"
    done
    exit 1
fi
exit 0
