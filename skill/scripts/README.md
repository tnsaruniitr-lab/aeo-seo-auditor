# Deterministic Audit Scripts

Standalone bash+Python tools that deliver repeatable outputs for the most
failure-prone audit checks. Designed to be run directly OR via the
`website-seo-aeo-auditor` skill.

## Quick Start

```bash
# Full 5-script orchestrator (human-readable)
bash scripts/run_deterministic.sh https://example.com human

# Full 5-script orchestrator (JSON, for programmatic diffing)
bash scripts/run_deterministic.sh https://example.com > audit.json

# Individual scripts (all emit JSON)
bash scripts/bots_eye_view.sh https://example.com        # Phase 1
python3 scripts/deterministic_checks.py https://example.com  # Phase 2
python3 scripts/check_robots_txt.py https://example.com      # Phase 3
python3 scripts/check_sitemap.py https://example.com         # Phase 4
python3 scripts/check_schema_completeness.py https://example.com  # Phase 5
```

## What each script does

### Phase 1 — `bots_eye_view.sh` + `_bev_analyze.py`

Fetches the URL 5 times with different User-Agents (default, Googlebot, GPTBot,
PerplexityBot, ClaudeBot) + once for a guaranteed-404 URL.

Outputs JSON with:
- **Classification**: `fully_accessible` | `partial_ssr` | `js_dependent` | `minimal_content` | `spa_no_ssr`
- Byte-level comparison across all UAs (cloaking detection, 5% tolerance)
- Byte-level comparison with 404 response (SPA-no-SSR detection)
- Title, H1, canonical, meta, schema counts from raw HTML
- FAQ pair count using 6 different detection patterns

**Key signal:** If `same_html_as_404_url: true`, the site is a client-side SPA with
no server-side rendering. AI crawlers see nothing.

### Phase 2 — `deterministic_checks.py`

Runs 9 targeted checks, each a pure function of the HTML input. These are the
checks where the auditor skill has historically produced wrong answers:

| Check ID | Catches |
|---|---|
| D9_faqpage_schema_vs_visible_match | FAQ schema count ≠ visible count (handles React accordions, shadcn, semantic HTML) |
| A7b_h1_nested_in_heading | H1 inside H2/H3/etc (invalid HTML) |
| J2_brand_name_consistency | Character substitution (Weg0vy vs Wegovy) |
| A4b_canonical_redirect_chain | Canonical points to a 3xx-redirected URL (loop detection) |
| B1_ttfb_median_5_samples | TTFB variance (5 samples, reports median+p95) |
| D4_schema_id_coverage | Every schema entity has @id |
| C12b_datemodified_staleness | Cosmetic Date.now() pattern AND stale >13-weeks detection |
| D12_person_schema_with_credentials | Person schema with hasCredential for YMYL |
| A2b_title_uniqueness_sample | Fetches 3 URLs, flags same-title-everywhere (SPA shell) |

### Phase 3 — `check_robots_txt.py`

Parses `robots.txt` into User-agent groups and evaluates per-bot access with
correct precedence rules:
- Multi-agent group handling (multiple `User-agent:` lines before `Allow/Disallow`)
- **Specific match wins over wildcard** (`Googlebot` rules override `*`)
- **Longest path match + allow-wins-on-tie** for Allow/Disallow evaluation

Checks access for 16 bots: Googlebot, Bingbot, BingPreview, GPTBot, ChatGPT-User,
ClaudeBot, Claude-Web, anthropic-ai, PerplexityBot, Google-Extended, OAI-SearchBot,
CCBot, Applebot, Applebot-Extended, DuckDuckBot, Bytespider.

Outputs 5 checks:
- `robots_reachable` — fetches without 4xx/5xx
- `robots_declares_sitemap` — one or more `Sitemap:` directives present
- `googlebot_allowed` — target URL path not blocked for Googlebot
- `ai_crawlers_all_allowed` — GPTBot, ClaudeBot, PerplexityBot, etc. all allowed
- `target_path_not_disallowed` — the specific URL being audited is crawlable

### Phase 4 — `check_sitemap.py`

Discovers sitemap via 3 paths in order:
1. `robots.txt` Sitemap directive
2. `/sitemap.xml`
3. `/sitemap_index.xml`

Recursively follows sitemap indexes (max depth 2, capped at 20 sub-sitemaps) to
enumerate all URLs. Uses `HEAD` requests for cheap validity probing.

**Deterministic sampling:** Uses `MD5(target_url + seed)` to select the same 10
sample URLs every run (no random seeding).

Outputs 6 checks:
- `sitemap_reachable` — sitemap URL returns 200 and parses as XML
- `target_url_in_sitemap` — the audited URL appears in the sitemap (or sub-sitemap)
- `no_cross_domain_entries` — sitemap only references URLs on same domain
- `sampled_urls_return_200` — 10 deterministically-sampled URLs all return 2xx
- `lastmod_coverage` — ≥80% of URLs have `<lastmod>` present
- `sitemap_size_compliance` — ≤50,000 URLs and ≤50MB per Google spec

### Phase 5 — `check_schema_completeness.py`

Parses every `<script type="application/ld+json">` block, flattens `@graph` and
nested entities (founder, author, medicalSpecialist — max depth 5), then validates
each entity against a per-@type field registry (`FIELD_SPECS`) covering 28 types
(Article, BlogPosting, Product, LocalBusiness, FAQPage, HowTo, Organization,
WebSite, BreadcrumbList, Person, ImageObject, etc.).

For each @type, checks:
- **required** — Schema.org spec requirements
- **google_required** — Google Search structured data requirements (tighter)
- **recommended** — best-practice fields (surface as `warn`)

Custom validations beyond field presence:
- **FAQPage** — `mainEntity` must be array of `Question` objects, each with `name`
  and `acceptedAnswer.text`
- **BreadcrumbList** — `itemListElement` positions must be sequential from 1

Outputs 6 checks:
- `all_schema_blocks_parse` — all JSON-LD blocks parse without error
- `schema_entities_present` — at least one entity parsed
- `no_invalid_entities` — no entity missing Google-required fields
- `schema_id_coverage` — every entity has `@id`
- `recommended_fields_coverage` — ≥70% of recommended fields populated
- `known_schema_types` — no entities using unknown `@type` values

### Orchestrator — `run_deterministic.sh`

Runs all 5 scripts in parallel (background PIDs, `wait` on all), combines outputs
into a single JSON with:
- Top-level `bots_eye_view`, `deterministic_checks`, `robots_txt_analysis`,
  `sitemap_analysis`, `schema_completeness`
- `overall_summary` with aggregated pass/fail/warn/na counts across all ~25 checks
- `all_critical_issues` — flat list of every `fail` finding prefixed with source
- `all_checks` — flat map keyed as `<source>:<check_id>` for ranking/diffing

Supports `human` mode for a readable 5-phase report with ✓/✗/⚠/— icons.

## Determinism Guarantees

**Verified:** 3 consecutive runs on `trypsagent.com` produced identical output
(MD5 `5cbf7d17f10fc02c0249f11b20981f96`) across all content-derived fields.

The following fields are intentionally non-deterministic and excluded from
determinism checks:

| Field | Why it varies | Mitigation |
|---|---|---|
| `ttfb_seconds`, `samples_ms`, `median_ms` | Physical network timing | 5-sample median smooths variance |
| `probe_404_url` cache-busters | Timestamp appended to avoid CDN cache | Intentional; see `_bev_analyze.py` |
| `size_bytes` per UA response | CDN edge variance (±tens of bytes via ETag/Set-Cookie) | 5% tolerance in cloaking check |
| Schema type list iteration order | Python dict/set ordering on identical entity sets | Sort for display in reports |

All content-derived fields — classifications, counts, verdicts, evidence
substance, URLs detected, entities parsed, fields validated — are stable across
runs on the same HTML.

## Tested Against

- `trypsagent.com` — SSR'd Next.js, 9 schema blocks, FAQ 7-vs-6 mismatch, 42 entities — all caught correctly
- `fiatrepublic.com` — Angular SPA without SSR — classification `spa_no_ssr` correct
- `feelvaleo.com/en-ae/journey/weightloss` — H1 nesting + drug name substitution — both caught

## Requirements

- `curl` (any version)
- `python3` (3.8+)
- Standard Unix tools (`grep`, `wc`, `mktemp`)
- No external Python packages needed — uses stdlib only

## Exit Codes

- `0` — success, JSON emitted
- `1` — missing URL argument or unrecoverable error

## File Layout

```
scripts/
├── README.md                        (this file)
├── bots_eye_view.sh                 (Phase 1 entry: bash wrapper)
├── _bev_analyze.py                  (Phase 1 logic: HTML parser + classifier)
├── deterministic_checks.py          (Phase 2: 9 targeted checks)
├── check_robots_txt.py              (Phase 3: per-bot allow/deny)
├── check_sitemap.py                 (Phase 4: sitemap validity + URL sampling)
├── check_schema_completeness.py     (Phase 5: per-@type field validation)
└── run_deterministic.sh             (orchestrator: runs all 5 in parallel)
```

## Output Shape (orchestrator)

```json
{
  "url": "https://example.com",
  "bots_eye_view": { "classification": "...", "response_per_bot": {...}, ... },
  "deterministic_checks": { "checks": { "D9_faqpage_...": {...}, ... }, "summary": {...} },
  "robots_txt_analysis": { "checks": {...}, "summary": {...} },
  "sitemap_analysis": { "sitemap": {...}, "checks": {...} },
  "schema_completeness": { "schema_summary": {...}, "entities": [...], "checks": {...} },
  "overall_summary": {
    "classification": "fully_accessible",
    "total_checks_run": 25,
    "pass": 15, "fail": 5, "warn": 5, "na": 0,
    "all_critical_issues": ["[det_checks:D9...] evidence", ...]
  },
  "all_checks": {
    "det_checks:D9_faqpage_schema_vs_visible_match": {...},
    "robots:ai_crawlers_all_allowed": {...},
    ...
  }
}
```
