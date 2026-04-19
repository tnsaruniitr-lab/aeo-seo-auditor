# scripts-v2/ — Fixed implementations

Drop-in-compatible v2 versions of the original `skill/scripts/` files.
Originals remain unchanged; v2 sits alongside them.

## Files

| File | Replaces | What's fixed |
|---|---|---|
| `check_sitemap_v2.py` | `skill/scripts/check_sitemap.py` | Real XML parser (xml.etree.ElementTree), HEAD-with-GET-fallback probing, safe URL handling |
| `check_robots_txt_v2.py` | `skill/scripts/check_robots_txt.py` | Empty-body tolerance, explicit HTTP 4xx/5xx handling, structured parse output |
| `bev_analyze_v2.py` | `skill/scripts/_bev_analyze.py` | FAQ question-intent gate, `ssr_shell_js_hidden_content` classification, html.parser-based text extraction |
| `deterministic_checks_v2.py` | (additive) | New `detect_hreflang` helper that sees Next.js streaming data; safe URL helpers |
| `run_deterministic_v2.sh` | `skill/scripts/run_deterministic.sh` | Per-PID wait with failure isolation, per-child timeout, child-health reporting |

## Usage

```bash
# Run v2 orchestrator (falls back to originals for bev + det)
bash scripts-v2/run_deterministic_v2.sh https://example.com human

# Run v2 self-tests
python3 scripts-v2/bev_analyze_v2.py --selftest
python3 scripts-v2/deterministic_checks_v2.py --selftest

# Run the full fixture test suite
bash tests/run_tests.sh
```

## Interface compatibility

- **JSON output schema:** identical to original scripts where possible;
  new fields added under `overall_summary.child_health` (non-breaking).
- **CLI signature:** identical (`python3 scriptname.py <URL>`).
- **Environment:** stdlib only. No pip dependencies added.

## Environment variables for overrides

The v2 orchestrator respects these overrides (useful for testing):

```bash
BEV_SCRIPT_OVERRIDE=/path/to/alt/bev.sh
DET_SCRIPT_OVERRIDE=/path/to/alt/det.py
ROBOTS_SCRIPT_OVERRIDE=/path/to/alt/robots.py
SITEMAP_SCRIPT_OVERRIDE=/path/to/alt/sitemap.py
SCHEMA_SCRIPT_OVERRIDE=/path/to/alt/schema.py
```

## See also

- `../CHANGES.md` — bug-by-bug description of what's different
- `../tests/fixtures/` — reproducible local inputs that trigger each bug
- `../tests/run_tests.sh` — assertions that verify v2 behavior
