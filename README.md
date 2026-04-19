# AEO + SEO + GEO Website Auditor

A deterministic, script-backed website auditor for SEO, AEO (Answer Engine Optimization), and GEO (Generative Engine Optimization). Produces reproducible, byte-identical output across runs on the same HTML input.

Originally built as a Claude Code skill. The `skill/` directory is a drop-in skill for Claude Code; the `scripts/` subdirectory is fully standalone (Python + bash, stdlib only) and can be run without Claude.

## What it does

Runs 5 deterministic inspectors against any URL, in parallel, and emits a combined JSON or human-readable report:

| Inspector | Checks |
|---|---|
| **Bot's Eye View** (`bots_eye_view.sh` + `_bev_analyze.py`) | Fetches target with 5 different User-Agents (default, Googlebot, GPTBot, PerplexityBot, ClaudeBot) + a 404 probe. Classifies as `fully_accessible`, `partial_ssr`, `js_dependent`, `minimal_content`, or `spa_no_ssr`. Detects cloaking (cross-UA byte comparison) and SPA shells (404-comparison). |
| **9 targeted checks** (`deterministic_checks.py`) | FAQ schema vs visible pair match, H1 nesting validity, brand-name character substitution (e.g., `Weg0vy` vs `Wegovy`), canonical-to-redirect loops, TTFB 5-sample median, schema `@id` coverage, `dateModified` staleness detection, `Person` schema + credentials for YMYL pages, title-uniqueness sampling across sitemap URLs. |
| **robots.txt analysis** (`check_robots_txt.py`) | Evaluates access for 16 bots (Googlebot, GPTBot, ClaudeBot, PerplexityBot, Bingbot, etc.) using correct User-agent precedence (specific > wildcard) + longest-path matching. |
| **Sitemap validation** (`check_sitemap.py`) | Discovers sitemap via 3 paths, recursively follows indexes, deterministic 10-URL sampling via `MD5(url+seed)` for stable re-runs, 200-OK probing via HEAD, `<lastmod>` coverage, 50K URL / 50MB compliance. |
| **Schema completeness** (`check_schema_completeness.py`) | Parses every JSON-LD block, flattens `@graph` and nested entities (max depth 5), validates each against per-@type field registry covering 28 types with custom checks for `FAQPage` and `BreadcrumbList`. |

## Quick start (standalone, no Claude)

```bash
# Requirements: curl, python3 (3.8+). No external pip packages.
cd skill/scripts

# Full 5-inspector orchestrator (human-readable)
bash run_deterministic.sh https://example.com human

# Full orchestrator (JSON, for programmatic diffing)
bash run_deterministic.sh https://example.com > audit.json

# Individual inspectors
bash bots_eye_view.sh https://example.com
python3 deterministic_checks.py https://example.com
python3 check_robots_txt.py https://example.com
python3 check_sitemap.py https://example.com
python3 check_schema_completeness.py https://example.com
```

## Determinism

Verified: 3 consecutive runs on `trypsagent.com` produce identical output (MD5 `5cbf7d17f10fc02c0249f11b20981f96`) across all content-derived fields.

Non-deterministic fields (intentionally — physical network timing + cache-busters):
- TTFB measurements
- Cache-buster timestamps in 404 probe URLs
- Schema type list iteration order (Python dict/set ordering)

All content-derived fields (classifications, counts, verdicts, evidence substance, URLs detected, entities parsed, fields validated) are stable.

## Repository layout

```
.
├── skill/
│   ├── SKILL.md                      # Claude Code skill orchestrator (15 phases)
│   ├── scripts/                      # The deterministic core (what an auditor should review)
│   │   ├── README.md                 # Full script docs
│   │   ├── bots_eye_view.sh          # Phase 1 entry (bash wrapper)
│   │   ├── _bev_analyze.py           # Phase 1 logic (HTML parser + classifier)
│   │   ├── deterministic_checks.py   # Phase 2 (9 targeted checks)
│   │   ├── check_robots_txt.py       # Phase 3 (16-bot access evaluation)
│   │   ├── check_sitemap.py          # Phase 4 (sitemap validity + sampling)
│   │   ├── check_schema_completeness.py  # Phase 5 (28 @type field validation)
│   │   └── run_deterministic.sh      # Orchestrator (all 5 in parallel)
│   └── references/                   # Static rules, frameworks, knowledge models
│       ├── static-rules.md           # 101 checks with pass/fail criteria
│       ├── check-definitions.md      # Check catalog (IDs, weights, truth badges)
│       ├── aeo-framework.md          # 4-stage AEO model (Discovery/Extraction/Trust/Selection)
│       ├── geo-framework.md          # 3-dimension GEO model (Presence/Accuracy/Favorability)
│       ├── schema-validation.md      # Required/recommended fields per @type
│       ├── scoring-rubric.md         # Weights, formulas, grade thresholds
│       ├── competitor-gap-template.md
│       ├── supabase-queries.md       # Persistence + brain-lookup SQL
│       ├── brain-mappings.md         # Check-ID → Sieve rule/AP mappings
│       ├── knowledge-seo.md
│       ├── knowledge-aeo.md
│       ├── knowledge-geo.md
│       └── knowledge-performance.md
└── audit-reports/                    # Example audits run against real sites
    ├── answermonk-audit-1-2026-04-14.md
    ├── feelvaleo-com-audit-1-2026-04-19.md
    ├── feelvaleo-com-SEO.AEO-1-2026-04-14.md
    ├── jointryps-com-audit-3-2026-04-14.md
    ├── trypsagent-com-audit-1-2026-04-14.md
    ├── trypsagent-com-audit-2-2026-04-14.md
    ├── tryps-audit-1-2026-04-10.md
    └── tryps-audit-2-2026-04-10.md
```

## Known issues / pending patches

Four issues were identified in the 2026-04-19 feelvaleo.com audit run and are **not yet patched**:

1. **FAQ false-positive** (`_bev_analyze.py` lines 117–121) — `<details>/<summary>` detection counts country-expander UI as FAQ pairs. Needs a question-keyword gate.
2. **Hreflang detection misses Next.js streaming data** — top-level `<link rel="alternate">` check doesn't see hreflang encoded inside `self.__next_f.push` chunks.
3. **Classification gap** — sites that SSR only a modal/gate over a JS-rendered body get classified as `minimal_content` when they should get `ssr_shell_js_hidden_content`.
4. **Chrome MCP LCP capture is unreliable** — observers registered via CDP `Runtime.evaluate` miss LCP entries that fire before observer setup. Workaround: approximate from largest image `responseEnd`.

Full patch text and line-level diffs are in `audit-reports/feelvaleo-com-audit-1-2026-04-19.md`.

## External dependencies

Core scripts: **zero** — pure Python stdlib + bash + curl.

Claude skill wrapper (`SKILL.md`): uses Claude Code MCP tools (WebFetch, WebSearch, Supabase) for the narrative layer + persistence. Scripts stand alone without any MCP.

## License

No license selected yet — add one before reuse. Consider MIT or Apache-2.0.

## Provenance

Built iteratively across ~4 Claude Code sessions. Key design decisions:

- **curl as ground truth, WebFetch as supporting layer** — WebFetch summarizes and drops tags unpredictably; curl returns verbatim HTML.
- **Deterministic scripts replaced prose interpretation** — earlier prose-based audits produced wrong answers on FAQ counts, H1 nesting, drug name obfuscation, and dateModified staleness. Scripts fix this.
- **5-sample TTFB median** instead of single-sample — reduces false alarms from network jitter.
- **MD5-based URL sampling** for sitemap probing — same URL → same sample every run.
