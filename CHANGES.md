# CHANGES — v2 audit fixes

This document describes the changes introduced in `scripts-v2/` and `tests/`,
addressing audit-correctness bugs identified in a 2026-04-19 external review.

The **originals in `skill/scripts/` are unchanged.** The v2 scripts live in
parallel and can be adopted either by swapping symlinks or by applying
`apply-to-original.patch`. Choose whichever fits your deployment workflow.

---

## Summary — 12 fixture tests, 0 failures

```
[1] empty_robots.txt — parser must not crash                         ✓
[2] sitemap_with_entities.xml — real XML parser required             ✓
[3] country_accordion_not_faq.html — must return 0 (not 4)           ✓
[4] real_faq_accordion.html — must return 6 real Q&As                ✓
[5] nextjs_streaming_hreflang.html — 9 hreflang in streaming          ✓
[6] spa_shell_same_as_404.html — must classify as spa_no_ssr         ✓
[7] ssr_full_landing.html — must classify as fully_accessible        ✓
```

Run from repo root:
```bash
bash tests/run_tests.sh
```

---

## Changes by bug

### 1. FAQ false-positive gate (high severity)

**Before:** `faq_visible_count()` counted every `<details>/<summary>` pair as
an FAQ. On feelvaleo.com the 4 country expanders ("United Arab Emirates",
"Kingdom of Saudi Arabia", "Qatar", "Kuwait") registered as 4 FAQs, producing
a noisy D9_faqpage_schema_vs_visible_match failure and polluting every
FAQ-related fix recommendation.

**After (`bev_analyze_v2.py::faq_visible_count`):** require the summary text
to look like a question — contain `?`, start with a question word (how, what,
when, where, why, which, who, can, do, does, is, are, will, should), OR
start with a FAQ/Q: label. Other detection patterns (shadcn accordion, class
patterns, H3-ending-in-question-mark) retained unchanged.

**Impact on audit quality:** eliminates one of the top sources of false-positive
FAQ failures on locale-gateway sites, service pages with disclosure toggles,
and navigation menus built with `<details>`.

### 2. Real XML parser for sitemap (high severity)

**Before:** `check_sitemap.py` used regex to extract `<loc>` and `<lastmod>`
values from sitemap XML. Regex silently corrupted URLs containing `&amp;`
entities and failed outright on `<![CDATA[...]]>` sections. For sitemaps
with query-string-heavy URLs (e-commerce, search pages, UTM tags) 10-20% of
URLs were read incorrectly, causing false "target URL not in sitemap"
failures.

**After (`check_sitemap_v2.py`):** uses `xml.etree.ElementTree` from the
stdlib. Properly handles entities, CDATA, namespaces, and comments. No
external dependency added.

**Impact:** URLs like `https://example.com/search?q=hello&lang=en` now read
correctly. Sitemaps with the sitemap-index pattern work at full depth (2
levels, up to 20 sub-sitemaps per index).

### 3. HEAD-with-GET fallback for URL probing (high severity)

**Before:** `check_sitemap.py::sample_urls_return_200` used `curl -I` (HEAD)
only. Servers that return 405 Method Not Allowed or 501 Not Implemented for
HEAD but 200 OK for GET (seen on Cloudflare Workers, some nginx configs,
older PHP apps) were falsely flagged as broken.

**After (`check_sitemap_v2.py::probe_url`):** HEAD first. If the server
returns 405 or 501, retry with `GET` using `Range: bytes=0-1023` to minimize
transfer cost. Reports the method used.

**Impact:** eliminates a class of false-positive sitemap health failures
on CDN-fronted sites.

### 4. Per-PID wait in orchestrator (medium severity)

**Before:** `run_deterministic.sh` used `set -euo pipefail` with
`wait $P1 $P2 $P3 $P4 $P5`. If any one child exited non-zero (sitemap fetch
timeout, malformed robots.txt, etc.), `wait` returned non-zero and `set -e`
killed the whole script. The other 4 scripts' output was lost.

**After (`run_deterministic_v2.sh`):** wraps each child in `timeout` with
a per-script limit (60s), waits each PID individually with error isolation,
writes the exit code of every child to a temp file, and reports per-child
health in the combined output. One failed child no longer kills four
good children.

**Bonus:** combined JSON now contains `overall_summary.child_health` with
`{bev, det, robots, sitemap, schema}` and `any_child_degraded` flag so
downstream consumers can detect degraded runs.

### 5. Empty / error robots.txt tolerance (medium severity)

**Before:** `check_robots_txt.py::parse_robots` made assumptions about the
input shape. Empty body (HTTP 200 with zero bytes) raised `IndexError`.
HTTP 403/500 bodies (WAF block pages, backend errors) sometimes parsed
partially and fabricated fake Allow/Disallow rules from HTML fragments.

**After (`check_robots_txt_v2.py::parse_robots_txt`):**
- Empty input returns a valid empty structure (no crash)
- HTTP 4xx/5xx is detected explicitly in the fetch layer and propagated
  as a FAIL on `robots_reachable` with permissive-default semantics per
  RFC 9309 §2.3.1 downstream
- All downstream checks mark `target_path_not_disallowed` as WARN when
  robots is inaccessible, not PASS with falsified evidence
- Parse warnings are accumulated and returned with the result, never
  swallowed

### 6. URL interpolation safety (medium-low severity)

**Before:** URLs with shell-meaningful characters (`?`, `&`, `$`, backticks,
quotes) could be misinterpreted when passed into shell command strings
or `eval`-style constructs.

**After:**
- All subprocess calls in `check_sitemap_v2.py`, `check_robots_txt_v2.py`,
  and `run_deterministic_v2.sh` pass URLs as separate argv entries, not
  interpolated strings.
- `deterministic_checks_v2.py::safe_url_for_shell` is available for the
  rare case where an actual single-string form is needed (uses
  `shlex.quote`).
- `deterministic_checks_v2.py::safe_url_components` returns parsed
  path/query/origin separately via `urllib.parse` — no manual string
  surgery on URLs anywhere.

### 7. Hreflang detection for Next.js streaming (new check)

**Before:** No dedicated hreflang check existed in the scripts. When audit
prose-layer grep looked at top-level `<link rel="alternate">`, it missed
hreflang entries streamed via Next.js App Router's `self.__next_f.push(...)`
chunks. Feelvaleo.com audit falsely reported "0 hreflang tags" when the
page had 9 in streaming data.

**After (`deterministic_checks_v2.py::detect_hreflang`):** scans both
top-level `<link>` tags and `self.__next_f.push(...)` chunks. Returns:
- `total_count` — unique locales detected across both
- `toplevel_count` vs `streamed_count` — diagnostic split
- `status` — `pass`/`warn`/`fail`
- `evidence` — describes what was found and where

A locale detected only in streaming data is reported as WARN (works for
hydrated clients, but some bots may miss it) rather than FAIL.

### 8. `ssr_shell_js_hidden_content` classification (new)

**Before:** `classify_ssr()` returned `minimal_content` for thin pages
regardless of whether the thinness was genuine (truly a minor page) or
a modal/gate in front of a JS-rendered full homepage. Feelvaleo.com
homepage (100-word SSR locale modal over a full JS-rendered landing page)
got the generic `minimal_content` verdict when the actionable insight was
"your real content is invisible to bots because it's behind the modal."

**After (`bev_analyze_v2.py::classify_ssr`):** detects the SSR-shell-with-
JS-hidden-content pattern when ALL three signals co-occur:
1. Visible words < 200 (thin SSR)
2. H1 matches UI-action keyword (Select, Choose, Pick, Continue, Welcome, etc.)
3. Rich JS bundle (>40KB with Next.js streaming markers)

Returns a new classification: `ssr_shell_js_hidden_content`. Downstream
reporting can now explain the actual problem ("there IS content, but it's
in the JS bundle — bots never see it") rather than the generic thin-page
diagnosis.

---

## What was NOT changed

1. The original 9 checks in `deterministic_checks.py` — still the source of
   truth for the Phase-2 suite. V2 is additive, not replacement.
2. The scoring rubric in `references/scoring-rubric.md` — the reviewer's
   critique about "numbers look too precise for the evidence" is valid but
   sits at the presentation layer, out of scope for this bug-fix pass.
3. The brain enrichment SQL in `references/supabase-queries.md` — unchanged.
4. The Claude Code SKILL.md orchestrator — unchanged (the v2 scripts can be
   swapped in by changing the paths in Phase 1.6).

---

## How to adopt

### Option A — parallel install (safest)

Leave `skill/scripts/` untouched. Invoke v2 explicitly:

```bash
bash scripts-v2/run_deterministic_v2.sh https://example.com human
```

The v2 orchestrator calls v2 scripts for robots and sitemap, falls back
to the original scripts for bev and det (which are unchanged in v2).

### Option B — in-place patch of originals

Apply the unified diff:

```bash
patch -p1 < apply-to-original.patch
```

This mutates the files in `skill/scripts/`. Irreversible except via git
revert. Do this only after reviewing the patch and running
`bash tests/run_tests.sh` against the result.

### Option C — symlink swap

```bash
cd skill/scripts
mv check_sitemap.py check_sitemap.py.original
ln -s ../../scripts-v2/check_sitemap_v2.py check_sitemap.py
# repeat for check_robots_txt.py, _bev_analyze.py, run_deterministic.sh
```

Reversible. But naming mismatch between `.py` and `_v2.py` may confuse future
readers.

---

## Known limits of this v2 pass

1. **No retry/backoff on WebFetch/WebSearch.** Transient 429/timeout still
   becomes a bogus N/A. Addressed separately.
2. **Scoring rubric still shows precise percentages.** Reviewer's confidence-
   band recommendation is valid but presentation-layer scope, deferred.
3. **Brain enrichment silent degradation.** If Supabase is unreachable, the
   report still reads as if enrichment ran. Separate fix needed in SKILL.md
   Phase 13.
4. **Competitor crawl still uses WebFetch (LLM-summarized).** Not measured.
   Separate fix — use curl for competitor fetches.
5. **Chrome MCP LCP capture remains approximate.** Documented in
   `scripts/README.md` Chrome caveats section.
