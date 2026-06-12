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

---

# 2026-06-12 — Robustness pass (skill-unified + live skill)

Trigger: the somana.com audit false positive. The site was audited as
`http://somana.com`; the server answers http with a 308 (empty body) and the
probe didn't follow redirects, so the report claimed "JS-only SPA, 0 visible
words" about a fully pre-rendered Framer site. A full code audit of
`skill-unified/scripts/` followed; 40+ verified findings fixed. The live copy
at `.claude/skills/website-seo-aeo-auditor/scripts/` is synced. `skill/scripts/`
and `scripts-v2/` are LEGACY lineages — do not edit them; `skill-unified/` is
canonical.

## bots_eye_view.sh + _bev_analyze.py (the false-positive chain)
- curl now uses `-L --max-redirs 5 --compressed`; `-w` adds `%{num_redirects}`
  and `%{url_effective}` (parser is back-compatible with 3-field strings).
- `classify_ssr()` gates on http_code FIRST: new transport classes
  `unresolved_redirect`, `bot_blocked` (401/403/429), `http_error`,
  `fetch_failed` — an empty redirect/error body can never again classify as
  "SPA / minimal content".
- Bot blocking (browser UA 2xx, bot UA 4xx) is now its own finding and is
  excluded from the cloaking word-count comparison. Per-UA divergent final
  URLs are reported (`divergent_final_urls`).
- FAQ ground truth: schema questions are text-matched against visible HTML
  (`faq_schema_questions_visible`, integrity classes `ok_text_match` /
  `partial_text_match`) — fixes the false "FAQ markup disqualified" claim on
  Framer/custom-markup sites. FAQPage parsing handles `@type` arrays,
  single-dict `mainEntity`, multiple blocks, HTML-escaped JSON-LD.
- `looks_like_question()` knows German question words.
- `summary` now actually contains the keys the orchestrator reads
  (`critical_issues`, `same_html_as_404_url`, `cloaking_detected`, …) — they
  were silently absent before. Scheme-less URLs normalized to https. Temp
  files cleaned via trap; dead `PY_EXIT` logic removed.

## deterministic_checks.py (+ extras)
- Per-check crash isolation in `run_all_checks` (one bad check → `na`, not a
  dead process); J2 TypeError on non-string JSON-LD names fixed.
- HTTP status gating: non-2xx page → all checks `na` with accurate evidence,
  `content_checks_skipped: true`.
- urllib 308 support (Python < 3.11 doesn't follow 308): RecordingHandler /
  _Redirect308Handler alias 308→307 in both this file and
  check_schema_completeness.py.
- A4b canonical: attribute order/quoting agnostic, `urljoin` for relative
  hrefs, fragment stripped, scheme/host lowercased.
- D9: `@type` arrays, dict `mainEntity`, accumulation across blocks, and the
  same schema-question text-match fallback as the BEV analyzer (pass/warn
  instead of false fail when the text is visible without a widget pattern).
- D12: author/founder as lists of Person; `@type` arrays.
- C12b: unparseable/future-only dates → `warn` (was silent `pass` with
  contradictory evidence); date-only stamps exempt from the 60s cosmetic
  window.
- B1 TTFB: no more cache-busting query param (measures CDN reality), `-L`,
  non-2xx samples discarded and counted; invalid `%{header_...}` removed.
- A2b: status-aware (non-2xx → na; soft-404 wording vs SPA-shell claim);
  fixed probe slug (deterministic output). A7b: heading auto-close semantics
  (no false "nested H1" on unclosed h2). Charset-aware body decoding.
  Shared `extract_jsonld_blocks()`. hreflang: zero declarations → `na` (was
  fail for every monolingual site); streamed-hreflang scan no longer
  truncates at the first `)` and is case-insensitive.

## check_robots_txt.py
- UA-group matching per RFC 9309/Google parser: prefix match, longest token
  wins (was bidirectional substring — selected `Googlebot-Image` groups for
  Googlebot). `*`/`$` wildcards in Allow/Disallow translated to regex,
  longest-match precedence, Allow wins ties (were treated as literals).
  Groups with only Crawl-delay etc. are kept (allow-all), not dropped.
- 5xx robots.txt = assume complete disallow (was claimed "permissive").
  Decoding errors='replace'. Query string included in path evaluation.
  Sitemap-directive check is `na` when robots.txt unreachable.

## check_sitemap.py
- Gzipped sitemaps (.gz bodies) gunzipped instead of crashing the UTF-8
  decode into "fetch failed". URL comparison normalized both ways
  (scheme/www/trailing slash). 50k limit applied per FILE not aggregate.
  Truncated traversals flagged (`truncated: true`) and demote "not in
  sitemap" to warn. ALL robots `Sitemap:` directives traversed. 403s on
  sampled URLs reported as "blocked", not dead; evidence matches predicate.

## check_schema_completeness.py
- `@graph` reachable inside list-wrapped blocks (was "No schema entities
  found" for valid markup). Multi-type `@type` arrays validated against the
  first type with a spec; non-string types no longer crash. Single-dict
  `mainEntity` and `@type: ["Question"]` accepted. HTTPError keeps its real
  code (403 reads "blocked", not "could not fetch"). Deterministic ordering
  (`sorted`). String breadcrumb positions coerced.

## run_deterministic.sh + SKILL.md + tests
- Orchestrator normalizes scheme-less URLs; human mode reads the analyzer's
  real keys (`page_identity` / `content_visible_to_bots` never existed).
- SKILL.md Phase 1.6 contract rewritten to the analyzer's actual output,
  including how to interpret transport classes ("probe inconclusive — write
  zero content findings").
- tests/run_tests.sh: +13 assertions (tests 9–11) covering transport gating,
  curl -w parsing (new + legacy), FAQ @type arrays / dict mainEntity /
  text-match, German question detection. 32 passed, 0 failed.

End-to-end verification: `run_deterministic.sh http://somana.com` now yields
classification `fully_accessible`, 27/27 checks run, and only genuine
findings (1 of 6 FAQ questions not visible, FAQPage missing @id, no Person
schema, 0/90 sitemap lastmod). reddit.com correctly reports bot blocking
(gbot/gpt 403, claude 429) instead of "cloaking".

---

# 2026-06-12 — Production-service hardening (standalone/)

First audit of the FastAPI service itself (standalone/main.py + agent/pipeline
layers). Security + report-integrity fixes; deploys via the same Railway build.

## Security (standalone/main.py + new standalone/safety.py)
- SSRF guard (`safety.check_url_safe`): submission and webhook URLs are now
  rejected when they target loopback/RFC1918/link-local/reserved/multicast
  addresses, cloud-metadata IPs (169.254.169.254 etc.), `localhost`, embedded
  credentials, or non-http(s) schemes — resolving DNS and checking every
  returned address. Blocks the "audit http://169.254.169.254/ and read it back
  from the public audit JSON" exfiltration.
- Fail-closed auth: in production (Railway env detected, or AUDITOR_FAIL_CLOSED=1)
  a missing AUDIT_USERNAME/PASSWORD or AUDIT_API_KEY now returns 503 on the
  paid submission endpoints instead of silently serving them to everyone.
- Concurrency cap (MAX_CONCURRENT_AUDITS, default 3): submissions past the cap
  get 429 instead of spawning unbounded chromium/agent loops. JOBS is bounded
  (MAX_TRACKED_JOBS) with oldest-finished eviction, and hung 'running' jobs are
  reaped to 'error' after MAX_AUDIT_SECONDS so they can't hold a slot forever.
- /healthz no longer leaks auth/config posture (was an "auth_enabled:false"
  beacon); detailed readiness moved to an auth-gated /readyz. git_sha kept on
  /healthz for deploy verification.
- `javascript:`/`data:` scheme XSS in the report renderer's citation links
  fixed with a client-side `safeHref()` (http/https only).
- Added the missing `import re` that silently NameError'd the Supabase
  idempotency path (every retry was re-running/re-billing the audit).

## Report integrity (audit_pipeline.py, agent.py, system_prompt.py, tools.py)
- Transport gate: a probe classified `unresolved_redirect` / `bot_blocked` /
  `http_error` / `fetch_failed`, or with no applicable checks, now scores
  `INCONCLUSIVE` (overall_score null) instead of the old 0/100 Grade F — the
  redirect-incident failure mode at the scoring layer. The narrative for such
  pages is a fixed honest statement (no LLM call), not three fabricated
  "why not cited" reasons; the "exactly 3" instruction is now "up to 3, only
  when findings support it". system_prompt.py gains GATE 0 teaching the agent
  the same rule.
- Phantom-key fixes via a single `bev_summary()` reader: classification,
  narrative context, and the markdown Bot's-Eye-View table now read the
  analyzer's REAL keys (summary.visible_words_default, summary.faq_*, probes.
  default.h1_first) instead of `page_identity`/`content_visible_to_bots`,
  which never existed and made every report print "FAQ visible: 0" and 'n/a'
  word counts. FAQ integrity legend (ok_text_match/schema_missing) documented.
- agent.py: `pause_turn` from server tools now continues the loop instead of
  aborting the audit; a budget/turn-cap exit no longer promotes intermediate
  chatter to a "completed" audit (only an explicit <audit> tag on a clean
  end_turn is accepted, and a missing scoring/findings fails to the error
  envelope); oversize tool results are structure-trimmed before a last-resort
  byte-slice.
- tools.py: run_deterministic_scripts runs the script subtree in its own
  process group and killpg's it on timeout (no more orphaned curl children
  hanging past the deadline); findings persist is insert-then-delete so a
  failed insert can't leave 0 findings behind a non-zero findings_count.
- Scoring tolerates unknown check statuses instead of KeyError-ing the audit;
  PDF/markdown renderers html.escape page-derived strings and handle a null
  (INCONCLUSIVE) score.

Verified: SSRF/fail-closed/concurrency/401 all fire via FastAPI TestClient;
transport gate + phantom-key + narrative-gate unit tests pass; full
deterministic pipeline on http://somana.com renders grade C/72 with a correct
Bot's-Eye-View table (was Grade F with "FAQ visible: 0"). 37/37 script tests
still green.
