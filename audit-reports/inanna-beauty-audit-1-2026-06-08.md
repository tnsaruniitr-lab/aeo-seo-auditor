# SEO + AEO + GEO Audit Report
**URL:** https://inanna.beauty/en/
**Domain:** inanna.beauty
**Page Type:** Local business / Medical day spa — homepage (HIGH confidence)
**Company:** Inanna Wellness Berlin (Inanna GmbH) — award-winning medical day spa in Berlin-Mitte (facials, anti-aging, Biologique Recherche flagship)
**Date:** 2026-06-08
**Audit version:** 3.0 (SKILL.md 15-phase protocol)
**Audit duration:** ~6 min (recon only — technical fetch blocked)
**Competitors analyzed:** profaceberlin.de, susannekaufmann.com (KaDeWe), meridianspa.de — *SERP-derived only, not crawled*
**Target queries:**
  - Primary: `medical spa Berlin facial`
  - Variant: `anti-aging facial Berlin Mitte`
  - Category: `best spa Berlin 2026`
  - Branded: `Inanna Wellness Berlin`

---

## ⚠ BLOCKING ISSUE DETECTED — DATA-COLLECTION GATE FAILURE (audit-environment, not the site)

**This audit could not fetch the target page.** Every outbound request to `inanna.beauty`
from this execution environment was rejected by the environment's egress network policy:

```
HTTP/2 403
x-deny-reason: host_not_allowed
Host not in allowlist
```

This is **NOT** a fault of inanna.beauty. It is this Claude-Code-on-the-web environment's
**GitHub-only network policy**. Confirmed by cross-host probing:

| Host | Result |
|---|---|
| github.com | 200 (allowed) |
| inanna.beauty | 403 `host_not_allowed` |
| example.com | 403 `host_not_allowed` |
| google.com | 403 `host_not_allowed` |

**Consequence for this report:** The curl-grounded technical core of the auditor
(Phases 1, 1.5, 1.6, 5–8, schema parsing, robots.txt, sitemap, Bot's Eye View byte
analysis) **could not run against real data.** The deterministic scripts executed but
only measured the proxy's 21-byte 403 responses — so their raw output
(`classification: spa_no_ssr`, `no title`, `no schema`, `same as 404`) is an **artifact
of the block and is NOT a finding about the site.** Those checks are marked
**N/A — egress blocked** throughout, never pass/fail.

**What IS grounded in this report:** `WebSearch` routes outside the egress proxy and works.
Page identity (from Google's index / SERP), company context, competitor discovery, and the
entire **GEO / Brand-AI-Presence** layer are backed by real search data and are reported
with their normal truth badges.

**To get the full byte-accurate audit:** re-run in an environment with open egress (or
allowlist `inanna.beauty`), or paste the page HTML + robots.txt + sitemap.xml for
pasted-HTML mode. See the SKILL.md run commands in the report footer.

Everything below frames technical scores as **not computable this run**; GEO is reported
in full.

---

## Scores

### Page Citation Readiness: NOT COMPUTABLE THIS RUN
Can this page be found, extracted, trusted, and selected by AI answer engines?
Requires curl ground-truth (HTML, headers, robots.txt, schema) — blocked by egress policy.

| Section | Score | Grade | Note |
|---|---|---|---|
| Technical SEO (A) | NM | — | Needs raw HTML + headers — egress blocked |
| Performance (B) | NM | — | Needs curl timing + headers — egress blocked |
| On-Page SEO (C) | Partial | — | Title/architecture inferred from SERP only |
| Schema (D) | NM | — | Needs raw JSON-LD parse — egress blocked |
| AEO: Discovery (E) | NM | — | Needs robots.txt — egress blocked |
| AEO: Extraction (F) | NM | — | Needs body content — egress blocked |
| AEO: Trust (G) | Partial | — | Author/date needs HTML; off-page trust grounded |
| AEO: Selection (H) | Partial | — | Competitors not crawlable; SERP signals only |
| Entity (J) | Partial | — | Cross-source name consistency grounded; schema NM |

`NM` = not measured (data collection blocked). `Partial` = only SERP-derivable portion assessed.

### Brand AI Presence: ~70% (B−) — DIRECTIONAL, fully assessed
Does this brand exist in AI's understanding of the category?

| Dimension | Score | Basis |
|---|---|---|
| Presence | 75% | Strong branded presence + press + awards; weak in category aggregator lists |
| Accuracy | 85% | AI/SERP descriptions match site positioning precisely |
| Favorability | 65% | Positive sentiment, but not surfaced as a top "best spa Berlin" pick in lists |

Note: Brand presence is a directional assessment based on web search signals.
Page edits alone cannot fix brand presence — this requires content strategy and
entity-building work over months.

**Composite:**
- SEO Score: Not computable (technical core blocked)
- AEO Score: Not computable (technical core blocked)
- Citation Readiness: Not computable (technical core blocked)
- Brand AI Presence: ~70% (directional)

---

## Why This Page Isn't Being Cited

*Three findings limited to what is grounded without page fetch. Technical citation
blockers (schema, robots.txt, SSR) could not be assessed this run.*

- **Duplicated brand name in the homepage `<title>` tag** [HARD EVIDENCE — from Google's index].
  Google indexes the homepage title as `Inanna Wellness Berlin | Inanna Wellness Berlin |
  Award-Winning Spa` — the brand is repeated twice, wasting pixel width and diluting the
  keyword portion an AI extractor reads as the page's primary label. A4/A2 title hygiene.

- **Weak presence in category "best spa Berlin" answer sets** [MODEL JUDGMENT — directional].
  Per category WebSearch, the spas surfaced for "best spa Berlin / best facial Berlin 2026"
  are PROFACE, Susanne Kaufmann (KaDeWe), Meridian, and Yelp/Berlin10 aggregators — Inanna
  does **not** appear in those list-style sources, despite holding "Germany's Best Day Spa
  2024 & 2025." AI answer engines lean on those aggregator lists, so the brand is
  under-represented in non-branded category answers. Off-page / entity work.

- **Technical extraction readiness is UNVERIFIED this run** [N/A — egress blocked].
  Whether AI crawlers (GPTBot/PerplexityBot/ClaudeBot) actually receive the content in raw
  HTML (SSR vs JS-rendered), whether robots.txt permits them, and whether LocalBusiness/FAQ
  schema is present — all UNKNOWN because the page could not be fetched. These are the usual
  top citation blockers and MUST be re-checked with open egress before drawing conclusions.

---

## Bot's Eye View — What AI Crawlers See

**NOT AVAILABLE THIS RUN: egress blocked (`host_not_allowed`).** The page could not be
fetched with any User-Agent from this environment, so byte-level Bot's Eye View could not
be measured.

| Metric | Value | Source |
|---|---|---|
| Raw HTML word count | UNKNOWN | curl blocked |
| Page size | UNKNOWN | curl blocked |
| Schema blocks | UNKNOWN | curl blocked |
| FAQ in initial HTML | UNKNOWN | curl blocked |
| Images in HTML | UNKNOWN | curl blocked |
| JS dependency / SSR | UNKNOWN | curl blocked |

**Important:** The deterministic script returned `classification: spa_no_ssr` and
`same_html_as_404: true`. **Disregard these** — they reflect the egress proxy returning an
identical 21-byte `Host not in allowlist` 403 to every User-Agent and to the 404 probe, not
the real site. SERP evidence (10+ distinct indexed `inanna.beauty/en/...` pages with unique
titles, blog posts, team/press pages) indicates the site is live and indexable — contradicting
the script's blocked-environment artifact.

AI crawler access: **UNDETERMINED THIS RUN** (re-run with open egress to classify).

---

## Performance (Measured)

**NOT AVAILABLE THIS RUN: egress blocked.** TTFB, total load, page size, HTTP version, HSTS,
compression, and Cache-Control all require an actual response from the origin. The 47ms
"TTFB" the script reported is the *proxy's* rejection latency, not inanna.beauty's. Chrome
MCP was also not connected, so Core Web Vitals (LCP/CLS/INP) were not measured either.

| Metric | Value | Rating | AI Impact |
|---|---|---|---|
| TTFB | UNKNOWN | — | Re-run with open egress |
| LCP / CLS / INP | UNKNOWN | — | Chrome MCP not connected |
| Page Weight | UNKNOWN | — | — |
| Compression / HSTS / Cache | UNKNOWN | — | — |

---

## Competitor Comparison — "medical spa Berlin facial"

**Partial — competitors identified via SERP but NOT crawled (egress blocked).** Structural
signal columns (word count, schema, dates, links) require fetching each competitor page and
are marked N/A. Positioning is SERP-derived.

| Signal | Your Page (Inanna) | PROFACE Berlin | Susanne Kaufmann @ KaDeWe | Meridian Spa |
|---|---|---|---|---|
| Word count | N/A (not crawled) | N/A | N/A | N/A |
| FAQ pairs | N/A | N/A | N/A | N/A |
| Schema types | N/A | N/A | N/A | N/A |
| dateModified | N/A | N/A | N/A | N/A |
| Author/expert | Team page exists (SERP) | Single named esthetician | Brand house | Chain |
| Category positioning | Award-winning medical spa, Biologique Recherche flagship | "Leading esthetician Berlin Mitte", bespoke custom facials | Alpine-inspired brand treatments | Large day-spa chain |
| Appears in "best Berlin" lists | **Not in aggregator lists** | Yes (Berlin10, Yelp) | Yes | Yes (Meridian network) |

Note: Based on SERP results for the query family on 2026-06-08. Results vary by location/time.

**Key Gaps:**
1. **Aggregator-list absence** — competitors appear in Yelp / Berlin10 / threebestrated
   "best facial Berlin" lists; Inanna does not surface there despite stronger awards.
2. **Structural gaps unmeasured** — word count, FAQ, schema depth vs competitors could not
   be compared (no crawl). Re-run required for H1–H6.
3. **Single-expert vs house positioning** — PROFACE leans on one named expert (strong E-E-A-T
   author signal); Inanna's expertise is institutional (team/awards) — verify Person schema
   coverage once HTML is fetchable.

---

## Top Fixes (Ranked by Impact)

*Limited to fixes grounded without a page fetch. A full top-5 with BEFORE/AFTER code requires
the raw HTML — re-run with open egress.*

### Fix #1: Remove the duplicated brand name from the homepage `<title>`
**Impact:** High | **Effort:** Trivial | **Priority:** DO NOW
**Type:** PAGE HTML FIX
**Evidence:** HARD EVIDENCE (from Google's indexed title)

**BEFORE:**
```html
<title>Inanna Wellness Berlin | Inanna Wellness Berlin | Award-Winning Spa</title>
```

**AFTER:**
```html
<title>Inanna Wellness Berlin — Award-Winning Medical Day Spa, Mitte</title>
```

**WHY:** The brand token is repeated, pushing descriptive/keyword terms past the ~60-char
SERP cutoff and giving AI extractors a redundant page label. A clean, unique title improves
both SERP CTR and the entity label AI engines attach to the page.

### Fix #2: Get listed in Berlin "best spa / best facial" aggregators
**Impact:** High | **Effort:** Moderate (off-page) | **Priority:** PLAN
**Type:** OFF-PAGE / ENTITY WORK
**Evidence:** MODEL JUDGMENT (directional, from category WebSearch)

**BEFORE:** Inanna is absent from Yelp Berlin facials, Berlin10, and threebestrated "best spa"
lists that AI answer engines cite for "best spa Berlin."

**AFTER:** Active, complete profiles + outreach for inclusion on Yelp, Berlin10,
threebestrated, and Top10 Berlin (already partially present) with the "Germany's Best Day
Spa 2024/2025" award prominently cited.

**WHY:** AI category answers ("best spa in Berlin") are assembled largely from list/aggregator
sources. Strong awards don't help category citation if the brand isn't in the lists the
models read.

### Fix #3 (CONDITIONAL — verify first): Add/confirm LocalBusiness + FAQPage schema
**Impact:** High (if missing) | **Effort:** Easy | **Priority:** DO NOW *after verification*
**Type:** SCHEMA FIX
**Evidence:** N/A this run — schema presence UNVERIFIED (egress blocked)

**BEFORE:** Unknown — could not parse JSON-LD.

**AFTER (template if missing):**
```json
{
  "@context": "https://schema.org",
  "@type": ["MedicalBusiness","DaySpa","HealthAndBeautyBusiness"],
  "@id": "https://inanna.beauty/#org",
  "name": "Inanna Wellness Berlin",
  "url": "https://inanna.beauty/en/",
  "telephone": "0800 0808 800",
  "email": "keepshining@inanna.beauty",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "Charlottenstrasse 19",
    "postalCode": "10117",
    "addressLocality": "Berlin",
    "addressCountry": "DE"
  },
  "award": ["World Spa Awards — Germany's Best Day Spa 2024","World Spa Awards — Germany's Best Day Spa 2025","Gloria Award 2025","Ambiente SPA Star Award 2025"],
  "sameAs": [
    "https://www.linkedin.com/company/inanna-beauty/",
    "https://www.facebook.com/inannabeautygoddess/"
  ]
}
```

**WHY:** A local medical spa's single biggest structured-data win is complete
LocalBusiness/MedicalBusiness schema with address, awards, and `sameAs` — it powers map
packs, knowledge panels, and entity grounding in AI answers. **Confirm current state before
applying** — the page may already include this.

---

## Quick Wins
- Fix duplicated brand in `<title>` (Fix #1) — trivial.
- Audit SERP-truncated titles (`Skincare &…`, `FACIAL…`, `OncoSp…`, `KOBIDO®…`) — these
  Google-truncated titles suggest over-length or template-prefixed titles on inner pages;
  trim to <60 chars with the unique term first.
- Ensure `award` + `sameAs` present on Organization schema to leverage the World Spa Awards
  wins for entity authority *(verify after fetch)*.

---

## All Findings by Section

*Legend: ✓ pass · ✗ fail · △ warn · — N/A. Where a check requires fetching the page,
status is `— N/A` with reason "egress blocked" — NOT a fail. Re-run with open egress to
populate.*

### Section A — Technical SEO (0/12 measurable this run)

| Status | ID | Finding | Truth | Fix Type |
|---|---|---|---|---|
| — | A1 | HTTPS + HSTS — site is HTTPS (SERP URLs https), HSTS header unverified | HARD EVIDENCE | sitewide_template |
| △ | A2 | Title present but homepage title duplicates brand; inner titles SERP-truncated | HARD EVIDENCE | page_html |
| — | A3 | Meta description length — not fetchable | HARD EVIDENCE | page_html |
| — | A4 | Canonical self-referencing — egress blocked | HARD EVIDENCE | page_html |
| — | A5 | Robots meta indexable — egress blocked (pages ARE indexed, per SERP → likely OK) | HARD EVIDENCE | page_html |
| — | A6 | Exactly one H1 — egress blocked | HARD EVIDENCE | page_html |
| — | A7 | H1 contains primary keyword — egress blocked | HEURISTIC | content_restructure |
| — | A8 | HTML lang attribute (`/en/` + likely `/de/`) — egress blocked | HARD EVIDENCE | page_html |
| — | A9 | Viewport meta — egress blocked | HARD EVIDENCE | page_html |
| — | A10 | robots.txt allows crawling — egress blocked | HARD EVIDENCE | sitewide_template |
| — | A11 | Sitemap referenced — egress blocked | HARD EVIDENCE | sitewide_template |
| — | A12 | Renders without JS — egress blocked (script artifact unreliable) | MEASURED | cms_constraint |

### Section B — Performance (0/11 measurable this run)

| Status | ID | Finding | Truth | Fix Type |
|---|---|---|---|---|
| — | B1 | TTFB — egress blocked (47ms reading is proxy latency, invalid) | MEASURED | sitewide_template |
| — | B2–B5 | Render-blocking / image formats / lazy-load / minification — egress blocked | HARD EVIDENCE | page_html |
| — | B6 | DOM depth — Chrome MCP not connected | MEASURED | cms_constraint |
| — | B7 | Gzip/Brotli — egress blocked | HARD EVIDENCE | sitewide_template |
| — | B8 | Cache-Control — egress blocked | HARD EVIDENCE | sitewide_template |
| — | B9 | No mixed content — egress blocked | HARD EVIDENCE | page_html |
| — | B10 | Core Web Vitals — Chrome MCP not connected | MEASURED | sitewide_template |
| — | B11 | Image dimensions — egress blocked | HARD EVIDENCE | page_html |

### Section C — On-Page SEO (1 partial / 13)

| Status | ID | Finding | Truth | Fix Type |
|---|---|---|---|---|
| △ | C9 | URL clean & descriptive — `/en/medical-cosmetics/facials/` etc. are clean, hyphenated, descriptive (SERP) | HARD EVIDENCE | sitewide_template |
| — | C1 | Heading hierarchy — egress blocked | HARD EVIDENCE | content_restructure |
| — | C2 | Keyword in first 100 words — egress blocked | HEURISTIC | content_restructure |
| — | C3 | ≥3 internal links — egress blocked (deep architecture suggests good linking) | HARD EVIDENCE | content_restructure |
| — | C4 | Descriptive anchor text — egress blocked | HEURISTIC | content_restructure |
| — | C5 | Image alt text — egress blocked | HARD EVIDENCE | page_html |
| — | C6 | Word count vs competitors — egress blocked | COMPARATIVE | content_restructure |
| — | C7 | Keyword stuffing — egress blocked | HEURISTIC | content_restructure |
| — | C8 | Outbound authoritative links — egress blocked | HARD EVIDENCE | content_restructure |
| — | C10 | Open Graph tags — egress blocked | HARD EVIDENCE | page_html |
| — | C11 | Twitter Card — egress blocked | HARD EVIDENCE | page_html |
| — | C12 | Visible publication/update date — egress blocked (blog posts exist) | HEURISTIC | page_html |
| — | C14 | Broken external links — egress blocked | MEASURED | content_restructure |

### Section D — Schema / Structured Data (0/13 measurable)

| Status | ID | Finding | Truth | Fix Type |
|---|---|---|---|---|
| — | D1–D13 | All schema checks require raw JSON-LD parse — **egress blocked**. Script "0 entities" is a blocked-fetch artifact, NOT evidence of missing schema. | HARD EVIDENCE / STATIC RULE | schema |

### Section E — AEO Discovery (0/13 measurable)

| Status | ID | Finding | Truth | Fix Type |
|---|---|---|---|---|
| — | E1–E13 | robots.txt + meta-robots checks (Perplexity/Bing/Google/GPTBot/ClaudeBot/CCBot, sitemap, IndexNow, paywall) — **egress blocked**. Pages ARE in Google's index (SERP), so Googlebot access is likely fine, but unverified. | HARD EVIDENCE | sitewide_template |

### Section F — AEO Extraction (0/12 measurable)

| Status | ID | Finding | Truth | Fix Type |
|---|---|---|---|---|
| — | F1–F12 | First-paragraph answer, quick-answer block, FAQ pairs, named entities, facts, definition-first, tables/lists — all require body content — **egress blocked**. | STATIC RULE / HEURISTIC | content_restructure |

### Section G — AEO Trust (1 partial / 9)

| Status | ID | Finding | Truth | Fix Type |
|---|---|---|---|---|
| ✓ | G6 | Organization off-page trust — strong: World Spa Awards 2024/2025, Gloria 2025, Ambiente SPA Star 2025, CIDESCO-certified, press (Handelsblatt, Presseportal) | HARD EVIDENCE (off-page) | schema |
| — | G1 | Author byline visible — egress blocked | HEURISTIC | content_restructure |
| — | G2 | Author schema w/ credentials — egress blocked (Person/team page exists) | HARD EVIDENCE | schema |
| — | G3 | Outbound citations — egress blocked | HARD EVIDENCE | content_restructure |
| — | G4 | Publication date visible + schema — egress blocked | HARD EVIDENCE | page_html |
| — | G5 | dateModified visible + schema — egress blocked | HARD EVIDENCE | page_html |
| — | G7 | Privacy/terms accessible — egress blocked | HARD EVIDENCE | page_html |
| ✓ | G8 | HTTPS valid — indexed https URLs | HARD EVIDENCE | sitewide_template |
| — | G9 | Content freshness recency — egress blocked (active blog: Winter-Glow, Discovering the Best) | HARD EVIDENCE + MODEL JUDGMENT | content_restructure |

### Section H — AEO Selection (Competitor-Relative — partial)

| Status | ID | Finding | Truth | Fix Type |
|---|---|---|---|---|
| △ | H7 | AI Overview / answer presence — appears for branded queries; **absent** from category "best spa Berlin" answer sets | MEASURED | cannot_fix_from_page |
| — | H1 | Content depth vs competitors — competitors not crawled | COMPARATIVE | content_restructure |
| — | H2 | Unique data/research — not crawled | MODEL JUDGMENT | content_restructure |
| — | H3 | FAQ coverage vs competitors — not crawled | COMPARATIVE | content_restructure |
| — | H4 | Schema completeness vs competitors — not crawled | COMPARATIVE | schema |
| — | H5 | Fresher than competitors — not crawled | COMPARATIVE | page_html |
| △ | H6 | E-E-A-T vs competitors — strong awards/press; competitors lean on named experts (PROFACE) | COMPARATIVE | offpage_entity |
| — | H8 | Content matches query intent — not crawled | MODEL JUDGMENT | content_restructure |

### Section I — GEO (FULLY ASSESSED — directional / MODEL JUDGMENT)

| Status | ID | Finding | Truth | Fix Type |
|---|---|---|---|---|
| ✓ | I1 | Brand in category queries — **partial**: dominates branded queries, weak in "best spa Berlin" lists | MODEL JUDGMENT | offpage_entity |
| △ | I2 | Knowledge panel / entity card — likely present (awards, press, GMB signals) but unverified | MEASURED | offpage_entity |
| ✓ | I3 | AI description matches positioning — accurate ("award-winning Berlin medical spa, Biologique Recherche") | MODEL JUDGMENT | offpage_entity |
| ✓ | I4 | No outdated/incorrect AI info — current awards (2024/2025) reflected | MODEL JUDGMENT | offpage_entity |
| ✓ | I5 | Brand sentiment positive/neutral — positive (awards, favorable reviews) | MODEL JUDGMENT | offpage_entity |
| △ | I6 | Recommended over competitors — not surfaced as top pick in category lists vs PROFACE/Susanne Kaufmann | MODEL JUDGMENT | offpage_entity |
| ✓ | I7 | Consistent entity across sources — name/address/positioning consistent across press + directories | MODEL JUDGMENT | offpage_entity |
| — | I8 | sameAs links to authoritative profiles — schema sameAs unverified (LinkedIn/Facebook exist) | HARD EVIDENCE | schema |

### Section J — Entity Consistency (partial)

| Status | ID | Finding | Truth | Fix Type |
|---|---|---|---|---|
| ✓ | J1 | Organization name consistent — "Inanna Wellness Berlin" / "Inanna GmbH" consistent across SERP, press, directories | HARD EVIDENCE | sitewide_template |
| — | J2 | Logo consistent (schema/OG/favicon) — egress blocked | HARD EVIDENCE | sitewide_template |
| — | J3 | URL/domain consistent — egress blocked (canonical/@id/OG unverified) | HARD EVIDENCE | page_html |
| △ | J4 | sameAs URLs resolve — LinkedIn + Facebook profiles exist (SERP); schema linkage unverified | MEASURED | schema |

---

## AEO Stage Analysis

| Stage | Score | Verdict |
|---|---|---|
| Discovery (E) | NM | robots.txt unverified; site IS indexed by Google (positive signal) |
| Extraction (F) | NM | body content not fetchable |
| Trust (G) | Partial — strong off-page | Awards + press + HTTPS solid; on-page author/date unverified |
| Selection (H) | Partial — weak category | Wins branded, loses category answer presence vs aggregator-listed rivals |

**Diagnosis:** The brand's *trust* foundation is exceptionally strong (multi-year World Spa
Awards, CIDESCO certification, national press). The likely AEO weakness is **Selection in
non-branded category answers** — and possibly extraction/schema, which could not be verified.
The decisive unknown is technical extraction readiness (SSR + schema + robots), which gates
everything and must be measured with open egress.

---

## GEO Dimension Analysis (Directional Assessment)

All GEO findings are MODEL JUDGMENT based on web search proxies. Results vary by location,
session, and time.

### Presence — 75%
Strong for branded ("Inanna Wellness Berlin"): own pages, press portals, Top10 Berlin, Creme
Guides, inspiredcitizen. **Gap:** absent from Yelp/Berlin10/threebestrated "best facial Berlin"
list pages that feed category AI answers.

### Accuracy — 85%
AI/SERP descriptions accurately reflect positioning: award-winning Berlin-Mitte medical day
spa, Inanna Method®, Biologique Recherche flagship, CIDESCO-certified. Current 2024/2025
awards correctly attributed.

### Favorability — 65%
Sentiment positive (award framing, favorable reviews quoted). Not yet positioned as the
default "best spa in Berlin" recommendation in category lists, where competitors lead.

---

## Competitor Profiles

*SERP-derived; pages not crawled (egress blocked).*

- **PROFACE Berlin (profaceberlin.de):** "Leading esthetician in Berlin Mitte." Bespoke 60/90-min
  custom facials with deep-tissue sculpting massage; modalities incl. microcurrent, chemical
  peels, Gua Sha, Dermadrop. Strong single-named-expert E-E-A-T. Appears in Berlin10/Yelp lists.
- **Susanne Kaufmann @ KaDeWe (susannekaufmann.com):** Alpine-inspired brand-house facials
  (e.g., Barrier Boosting Ectoin Facial, 45 min, €99). Strong retail brand + flagship location.
- **Meridian Spa (meridianspa.de):** Large Berlin day-spa chain; broad face/body cosmetic menu;
  multiple locations (e.g., Spandau Arcaden).
- **Aggregators feeding category answers:** Yelp Berlin (Facials/Skin Care), Berlin10
  ("16 Best Facial Treatments in Berlin"), threebestrated.de, walk-this-way, Top10 Berlin.

Full structural comparison (word count, schema, FAQ, dates, links) requires crawling — re-run
with open egress.

---

## Schema Audit Detail

**NOT AVAILABLE THIS RUN: egress blocked.** JSON-LD blocks could not be fetched or parsed.
The script's "0 entities / types: []" is a blocked-fetch artifact and must not be read as
"no schema present." Recommended target schema (apply only after verifying current state)
is the LocalBusiness/MedicalBusiness + award + sameAs block in **Fix #3** above; a
`Service` schema per treatment page and `FAQPage` per FAQ-bearing page are likely high-value
additions for a multi-treatment medical spa.

---

## Entity Consistency Matrix

| Entity | Schema | OG Tags | Title | Footer | Consistent? |
|---|---|---|---|---|---|
| Org name (Inanna Wellness Berlin / Inanna GmbH) | NM | NM | ✓ (SERP) | NM | ✓ across external sources |
| Logo | NM | NM | — | NM | UNKNOWN |
| URL/domain (inanna.beauty) | NM | NM | ✓ | NM | ✓ canonical domain consistent in index |
| sameAs (LinkedIn, Facebook) | NM | NM | — | NM | Profiles exist; schema linkage UNKNOWN |

NM = not measured (egress blocked).

---

## Bot's Eye View — Full Detail

**NOT AVAILABLE THIS RUN: egress blocked (`host_not_allowed`).**
- curl response details: every UA (default, Googlebot, GPTBot, PerplexityBot, ClaudeBot) +
  404 probe returned identical `HTTP/2 403 / 21 bytes / x-deny-reason: host_not_allowed` —
  the environment proxy, not inanna.beauty.
- Content verification: not possible.
- AI search presence verification: **branded** queries return the brand's own pages + press +
  directories (strong); **category** queries ("best spa Berlin facial 2026") return PROFACE,
  Susanne Kaufmann, Meridian, Yelp, Berlin10 — Inanna not surfaced.
- Classification statement: **UNDETERMINED** — must be re-measured with open egress. Do not
  rely on the script's `spa_no_ssr`.

---

## All Checks Index

| Category | Checks | Measured | Pass | Fail | Warn | N/A (egress) |
|---|---|---|---|---|---|---|
| A — Technical SEO | 12 | 1 | 0 | 0 | 1 | 11 |
| B — Performance | 11 | 0 | 0 | 0 | 0 | 11 |
| C — On-Page SEO | 13 | 1 | 0 | 0 | 1 | 12 |
| D — Schema | 13 | 0 | 0 | 0 | 0 | 13 |
| E — AEO Discovery | 13 | 0 | 0 | 0 | 0 | 13 |
| F — AEO Extraction | 12 | 0 | 0 | 0 | 0 | 12 |
| G — AEO Trust | 9 | 3 | 2 | 0 | 1 | 6 |
| H — AEO Selection | 8 | 2 | 0 | 0 | 2 | 6 |
| I — GEO | 8 | 7 | 5 | 0 | 2 | 1 |
| J — Entity | 4 | 2 | 1 | 0 | 1 | 2 |
| **Total** | **103** | **16** | **8** | **0** | **8** | **87** |

**16 of 103 checks were measurable** from outside the page fetch. The remaining 87 require
open egress (or pasted HTML) and are N/A — not failures.

---

## Brain Intelligence Applied

**Sieve / Supabase brain not queried this run** (Supabase project `aldraxqsqeywluohskhs`
requires MCP credentials not present in this environment). Source attribution below is from
live web sources gathered during recon.

🥇 TIER 1 — PRIMARY
- Google Search index — confirmed 10+ indexed `inanna.beauty/en/...` pages, homepage title
  string, clean URL structure. Applied to: A2, C9, E (indexability signal), J1.

🥈 TIER 2 — RESEARCH / PRESS
- Handelsblatt / Presseportal / finanznachrichten — "Inanna Wellness gewinnt Germany's Best
  Day Spa 2025 (World Spa Awards)." Applied to: G6, H6, I3, I4.

🥉 TIER 3 — INDUSTRY / DIRECTORIES
- Top10 Berlin, Creme Guides, inspiredcitizen, Berlin10, threebestrated, Yelp Berlin.
  Applied to: I1, I2, I6, H7.

---

## Supplementary Findings

- **Multilingual structure (`/en/` paths)** — confirms at least EN + likely DE; verify
  `hreflang` reciprocity once HTML is fetchable (common Next.js-streaming hreflang miss is a
  known issue in this auditor — see README pending patch #2).
- **Treatment-page breadth** (Sculptural Face Lifting™, MamiSpa®, OncoSpa®, Kobido®,
  Dermalux® LED, mesotherapy, laser) is a strong topical-authority asset — each is a candidate
  for dedicated `Service`/`MedicalProcedure` schema and a quick-answer intro paragraph (F1/F2).

---

## Audit Metadata
- Version: 3.0
- Checks run: 16/103 measurable | Passed: 8 | Failed: 0 | Warnings: 8 | N/A (egress): 87
- Gates: **DATA-COLLECTION GATE FAILURE** — target unreachable from this environment
  (`host_not_allowed`); site itself appears healthy and indexed
- Page classification: Local business / medical day spa — homepage (HIGH confidence)
- Competitors analyzed: 3 (SERP-derived, not crawled)
- Chrome MCP: unavailable — CWV not measured
- Brain entries matched: 0 (Supabase not connected)
- Previous audit: none — first audit
- Queries used: primary, variant, category, branded
- Data sources: WebSearch (working) · curl/WebFetch (BLOCKED by egress policy) · Supabase (not connected) · Chrome MCP (not connected)

---

## Summary — "What to do this week"

**DO NOW (grounded):**
1. Fix the duplicated brand name in the homepage `<title>` (Fix #1) — trivial, real.
2. Trim/standardize SERP-truncated inner-page titles (`Skincare &…`, `FACIAL…`, `OncoSp…`).

**PLAN (off-page, grounded):**
3. Pursue inclusion in Yelp / Berlin10 / threebestrated "best spa/facial Berlin" lists,
   leading with the World Spa Awards wins (Fix #2) — this is the clearest lever for category
   AI-answer presence.

**BLOCKED — must re-run with open egress before acting:**
4. Verify SSR vs JS rendering, robots.txt AI-crawler rules, and LocalBusiness/FAQ/Service
   schema. These gate AEO citation and could not be measured. Re-run:
   `bash skill/scripts/run_deterministic.sh https://inanna.beauty/en/ human`

**Honest framing:** Inanna has a *premium trust profile* (awards, press, certification) that
most spas would envy — the brand is real, healthy, and indexed. The two grounded wins are
small/off-page. The substantive technical AEO verdict (schema, SSR, robots, performance)
is genuinely **unknown** from this environment and should not be guessed. Re-run with network
access for the complete byte-accurate report.

---
**Persistence confirmation:**
- Supabase: unreachable — not persisted (project `aldraxqsqeywluohskhs` requires MCP
  credentials not present in this environment)
- Markdown: audit-reports/inanna-beauty-audit-1-2026-06-08.md ✓ saved
- ⚠ Technical core (curl/WebFetch) blocked by environment egress policy (`host_not_allowed`).
  This report is **recon-grade**, not a complete byte-accurate audit. Re-run with open egress.
