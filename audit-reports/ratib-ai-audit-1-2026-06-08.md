# SEO + AEO + GEO Audit Report
**URL:** https://ratib.ai/
**Domain:** ratib.ai
**Page Type:** SaaS homepage / product landing (HIGH confidence)
**Company:** Ratib — payroll automation software for MENA & South Asia (UAE, Saudi Arabia, Egypt, Kuwait, Qatar, Jordan, Iraq, Pakistan); claims 500+ companies
**Date:** 2026-06-08
**Audit version:** 3.0 (SKILL.md 15-phase protocol)
**Audit duration:** ~6 min (recon only — technical fetch blocked)
**Competitors analyzed:** bayzat.com, zenhr.com, jisr.net, neuralhr.ai, darwinbox.com, yomly.com — *SERP-derived only, not crawled*
**Target queries:**
  - Primary: `payroll software UAE WPS compliant`
  - Variant: `multi-country payroll software MENA`
  - Category: `best payroll software UAE Saudi 2026`
  - Branded: `Ratib payroll`

---

## ⚠ BLOCKING ISSUE DETECTED — DATA-COLLECTION GATE FAILURE (audit-environment, not the site)

**This audit could not fetch the target page.** Every outbound request to `ratib.ai` from
this execution environment was rejected by the environment's egress network policy:

```
HTTP/2 403
x-deny-reason: host_not_allowed
Host not in allowlist
```

This is **NOT** a fault of ratib.ai. It is this Claude-Code-on-the-web environment's
**GitHub-only network policy**. `curl` and `WebFetch` (the auditor's ground-truth sources)
both route through this proxy and are walled off from all hosts except github.com.

**Consequence for this report:** The curl-grounded technical core (Phases 1, 1.5, 1.6, 5–8,
schema, robots.txt, sitemap, Bot's Eye View byte analysis) **could not run against real
data.** Those checks are marked **N/A — egress blocked** throughout, never pass/fail.

**What IS grounded:** `WebSearch` routes outside the egress proxy and works. Page identity
(from Google's index), index footprint, company context, competitor discovery, and the entire
**GEO / Brand-AI-Presence** layer are real and reported with normal truth badges.

**To get the full byte-accurate audit:** re-run with open egress (or allowlist `ratib.ai`),
or paste the page HTML + robots.txt + sitemap.xml for pasted-HTML mode.

---

## Scores

### Page Citation Readiness: NOT COMPUTABLE THIS RUN
Requires curl ground-truth (HTML, headers, robots.txt, schema) — blocked by egress policy.

| Section | Score | Grade | Note |
|---|---|---|---|
| Technical SEO (A) | NM | — | Needs raw HTML + headers — egress blocked |
| Performance (B) | NM | — | Needs curl timing + headers — egress blocked |
| On-Page SEO (C) | Partial | — | Title inferred from SERP only |
| Schema (D) | NM | — | Needs raw JSON-LD parse — egress blocked |
| AEO: Discovery (E) | Partial | — | robots.txt NM; **index footprint near-zero (grounded)** |
| AEO: Extraction (F) | NM | — | Needs body content — egress blocked |
| AEO: Trust (G) | Partial | — | HTTPS grounded; author/date/off-page trust thin |
| AEO: Selection (H) | Partial | — | Competitors not crawlable; **absent from category answers (grounded)** |
| Entity (J) | Partial | — | Name consistent; schema NM |

`NM` = not measured (data collection blocked). `Partial` = only SERP-derivable portion assessed.

### Brand AI Presence: ~30% (D) — DIRECTIONAL, fully assessed
Does this brand exist in AI's understanding of the category?

| Dimension | Score | Basis |
|---|---|---|
| Presence | 20% | Only the homepage is indexed; absent from every category buyer-guide list AI cites |
| Accuracy | 50% | "MENA payroll" positioning consistent, but the on-site "#1" claim is uncorroborated anywhere |
| Favorability | 20% | No third-party reviews, rankings, or recommendations found in category sources |

Note: Brand presence is a directional assessment based on web search signals. Page edits
alone cannot fix it — this requires content + entity-building work over months.

**Composite:**
- SEO Score: Not computable (technical core blocked)
- AEO Score: Not computable (technical core blocked)
- Citation Readiness: Not computable (technical core blocked)
- Brand AI Presence: ~30% (directional)

---

## Why This Page Isn't Being Cited

*Three findings limited to what is grounded without page fetch.*

- **Near-zero indexed footprint** [HARD EVIDENCE — from Google's index].
  `site:ratib.ai` returns **only the homepage** — no treatment of features, pricing, WPS/GOSI/
  Mudad compliance, country pages, blog, or docs surfaces in the index. AI answer engines
  retrieve and cite *pages*; a single indexed page gives them almost nothing to extract. This
  is the single biggest visibility limiter and it's verifiable today.

- **Absent from every "best payroll software MENA/UAE/Saudi" answer set** [MODEL JUDGMENT — directional].
  Category WebSearch returns Bayzat, ZenHR, Jisr, NeuralHR, Darwinbox, Yomly, Keka, ZingHR
  buyer-guides — Ratib appears in **none** of their recommendation bodies. The exact questions
  Ratib's buyers ask AI engines ("best WPS-compliant payroll UAE 2026") return competitors,
  not Ratib. Off-page / entity work.

- **The on-site "#1 Payroll Software for MENA & South Asia" claim is uncorroborated** [MODEL JUDGMENT].
  No third-party source — review site, buyer guide, directory, press — ranks or even lists
  Ratib in the category. Unbacked superlative claims are a known E-E-A-T/trust risk and AI
  engines discount them; the gap between self-claim and external corroboration is large.

*Technical citation blockers (SSR, robots.txt AI-crawler rules, schema) are UNVERIFIED this
run — egress blocked — and must be re-checked.*

---

## Bot's Eye View — What AI Crawlers See

**NOT AVAILABLE THIS RUN: egress blocked (`host_not_allowed`).** The page could not be fetched
with any User-Agent, so byte-level Bot's Eye View could not be measured.

| Metric | Value | Source |
|---|---|---|
| Raw HTML word count | UNKNOWN | curl blocked |
| Page size | UNKNOWN | curl blocked |
| Schema blocks | UNKNOWN | curl blocked |
| FAQ in initial HTML | UNKNOWN | curl blocked |
| Images in HTML | UNKNOWN | curl blocked |
| JS dependency / SSR | UNKNOWN | curl blocked |

**Note:** Any deterministic-script `classification` value this run reflects the egress proxy's
identical 21-byte 403 to every UA, not the real site — disregard it. SERP shows the homepage
is indexed, so it is reachable by Googlebot, but raw-HTML content visibility to GPTBot/
PerplexityBot/ClaudeBot is **undetermined**.

AI crawler access: **UNDETERMINED THIS RUN** (re-run with open egress to classify).

---

## Performance (Measured)

**NOT AVAILABLE THIS RUN: egress blocked.** TTFB, total load, page size, HTTP version, HSTS,
compression, and Cache-Control require an actual origin response. Chrome MCP was not connected,
so Core Web Vitals (LCP/CLS/INP) were not measured.

| Metric | Value | Rating | AI Impact |
|---|---|---|---|
| TTFB | UNKNOWN | — | Re-run with open egress |
| LCP / CLS / INP | UNKNOWN | — | Chrome MCP not connected |
| Compression / HSTS / Cache | UNKNOWN | — | — |

---

## Competitor Comparison — "payroll software UAE / MENA"

**Partial — competitors identified via SERP but NOT crawled (egress blocked).** Structural
columns require fetching each page and are N/A. Positioning + category-answer presence are
SERP-derived.

| Signal | Your Page (Ratib) | Bayzat | ZenHR | Jisr | Darwinbox |
|---|---|---|---|---|---|
| Word count / schema / FAQ | N/A (not crawled) | N/A | N/A | N/A | N/A |
| Indexed footprint (`site:`) | **~1 page (homepage only)** | Large (blog + product) | Large (blog + guides) | Large | Large |
| Category positioning | MENA + South Asia payroll, "#1" (self-claimed) | UEA-simplicity, WPS, insurance/benefits | MENA HRMS — GOSI/Mudad/WPS native | KSA-native payroll | Enterprise GCC payroll/HRMS |
| Appears in "best payroll" lists | **No (zero category lists)** | Yes | Yes | Yes | Yes |
| Third-party reviews/press | **None found** | Many | Many | Many | Many (Gartner-adjacent) |

Note: Based on SERP results for the query family on 2026-06-08. Results vary by location/time.

**Key Gaps:**
1. **Indexed-footprint gap** — competitors publish large, indexed content libraries (WPS/GOSI/
   Mudad guides, country pages, blogs); Ratib exposes essentially one indexed page.
2. **Category-answer absence** — every competitor is recommended in buyer-guide lists; Ratib
   is in none, so it never enters AI category answers.
3. **Third-party corroboration gap** — competitors have reviews/press/directory listings;
   Ratib has no external review or ranking footprint found.

---

## Top Fixes (Ranked by Impact)

*Limited to fixes grounded without a page fetch. A full top-5 with BEFORE/AFTER code requires
the raw HTML — re-run with open egress.*

### Fix #1: Publish & index real content pages (kill the single-page footprint)
**Impact:** Critical | **Effort:** Moderate–High | **Priority:** DO NOW
**Type:** CONTENT RESTRUCTURE + SITEWIDE TEMPLATE FIX
**Evidence:** HARD EVIDENCE (`site:ratib.ai` → homepage only)

**BEFORE:** Only `https://ratib.ai/` is indexed. No feature, pricing, compliance, country, or
blog page surfaces in Google.

**AFTER:** Indexable, server-rendered pages for: per-country compliance (UAE WPS, KSA
GOSI/Mudad/Saudization, Egypt, Qatar, Kuwait, Jordan, Iraq, Pakistan), pricing, product/
features, integrations, and a comparison/guide blog — each in the XML sitemap and internally
linked from the homepage.

**WHY:** AI answer engines (and Google) cite pages, not domains. A one-page index means there
is almost nothing for GPTBot/Perplexity/Google AI to retrieve for the dozens of specific
queries Ratib's buyers ask. This is the foundational lever — everything else depends on it.

### Fix #2: Build category presence — get into the "best payroll MENA" lists
**Impact:** Critical | **Effort:** Moderate (off-page) | **Priority:** PLAN
**Type:** OFF-PAGE / ENTITY WORK
**Evidence:** MODEL JUDGMENT (directional, from category WebSearch)

**BEFORE:** Ratib appears in zero buyer-guide / review lists (Bayzat, ZenHR, Jisr, NeuralHR,
Darwinbox, Yomly, Keka dominate). No G2/Capterra/SoftwareSuggest presence found.

**AFTER:** Complete, reviewed profiles on G2, Capterra, SoftwareSuggest (UAE), and outreach
for inclusion in the 2026 UAE/Saudi/MENA payroll buyer guides, with WPS/GOSI/Mudad coverage
stated explicitly.

**WHY:** Category AI answers are assembled from list/review sources. Until Ratib is in those
lists with real reviews, it cannot surface for "best payroll software UAE/Saudi 2026" no
matter how good the product is.

### Fix #3: Substantiate or reframe the "#1" claim
**Impact:** High | **Effort:** Easy | **Priority:** DO NOW
**Type:** CONTENT RESTRUCTURE
**Evidence:** MODEL JUDGMENT (no third-party corroboration found)

**BEFORE:** Homepage title/positioning: "Ratib | #1 Payroll Software for MENA & South Asia" —
no external source supports the ranking.

**AFTER:** Either (a) attribute the claim to a verifiable basis ("500+ companies across 8
countries"), or (b) replace the superlative with a specific, checkable differentiator
("Multi-country WPS/GOSI/Mudad payroll across MENA & South Asia"). Pair with logos, case
studies, and review-site ratings as proof.

**WHY:** Unbacked superlatives erode E-E-A-T and are discounted by AI engines; concrete,
verifiable claims are extracted and cited.

---

## Quick Wins
- Add an XML sitemap + ensure inner pages are server-rendered and indexable (precondition for Fix #1).
- Create G2/Capterra/SoftwareSuggest listings (precondition for Fix #2).
- Replace the "#1" superlative with a concrete proof point (Fix #3).
- Verify robots.txt allows GPTBot/PerplexityBot/ClaudeBot *(after fetch)*.

---

## All Findings by Section

*Legend: ✓ pass · ✗ fail · △ warn · — N/A. Checks requiring page fetch are `— N/A
(egress blocked)`, NOT failures. Re-run with open egress to populate.*

### Section A — Technical SEO (1 partial / 12)

| Status | ID | Finding | Truth | Fix Type |
|---|---|---|---|---|
| △ | A2 | Title present: "Ratib \| #1 Payroll Software for MENA & South Asia" — keyword-rich but leads with unverified "#1" superlative | HARD EVIDENCE | page_html |
| — | A1 | HTTPS + HSTS (site is https; HSTS unverified) | HARD EVIDENCE | sitewide_template |
| — | A3–A9 | Meta desc / canonical / robots-meta / H1 / lang / viewport — egress blocked | HARD EVIDENCE | page_html |
| — | A10 | robots.txt allows crawling — egress blocked | HARD EVIDENCE | sitewide_template |
| △ | A11 | Sitemap referenced — unverified, but `site:` footprint suggests sitemap/indexing is thin | HARD EVIDENCE | sitewide_template |
| — | A12 | Renders without JS — egress blocked | MEASURED | cms_constraint |

### Section B — Performance (0/11 measurable)

| Status | ID | Finding | Truth | Fix Type |
|---|---|---|---|---|
| — | B1–B11 | TTFB, render-blocking, image formats, compression, cache, CWV — all require origin response — **egress blocked** (Chrome MCP also not connected) | MEASURED / HARD EVIDENCE | sitewide_template |

### Section C — On-Page SEO (1 partial / 13)

| Status | ID | Finding | Truth | Fix Type |
|---|---|---|---|---|
| △ | C12 | Visible date / freshness — no indexed blog or dated content found (single-page footprint) | HEURISTIC | page_html |
| — | C1–C11, C14 | Heading hierarchy, keyword placement, internal links, alt text, OG/Twitter, word count, outbound links — egress blocked | HARD EVIDENCE / HEURISTIC | content_restructure |

### Section D — Schema / Structured Data (0/13 measurable)

| Status | ID | Finding | Truth | Fix Type |
|---|---|---|---|---|
| — | D1–D13 | All schema checks require raw JSON-LD parse — **egress blocked**. Recommended targets once verified: `SoftwareApplication` + `Organization` (sameAs, logo) + `FAQPage` + `Product/Offer`. | HARD EVIDENCE / STATIC RULE | schema |

### Section E — AEO Discovery (1 partial / 13)

| Status | ID | Finding | Truth | Fix Type |
|---|---|---|---|---|
| ✗ | E8 | Page-in-sitemap / index coverage — **`site:ratib.ai` returns only the homepage**; inner pages effectively not indexed | HARD EVIDENCE | sitewide_template |
| — | E1–E7, E9–E13 | Perplexity/Bing/Google/GPTBot/ClaudeBot/CCBot robots rules, IndexNow, paywall, noarchive — egress blocked | HARD EVIDENCE | sitewide_template |

### Section F — AEO Extraction (0/12 measurable)

| Status | ID | Finding | Truth | Fix Type |
|---|---|---|---|---|
| — | F1–F12 | First-paragraph answer, quick-answer block, FAQ pairs, named entities, facts, tables/lists — require body content — **egress blocked** | STATIC RULE / HEURISTIC | content_restructure |

### Section G — AEO Trust (1 partial / 9)

| Status | ID | Finding | Truth | Fix Type |
|---|---|---|---|---|
| ✓ | G8 | HTTPS valid — homepage indexed over https | HARD EVIDENCE | sitewide_template |
| △ | G6 | Organization off-page trust — **thin**: no press, reviews, or directory listings found | HARD EVIDENCE (off-page) | schema |
| — | G1–G5, G7, G9 | Author byline, author schema, outbound citations, dates, privacy/terms, freshness — egress blocked | HARD EVIDENCE | content_restructure |

### Section H — AEO Selection (Competitor-Relative — partial)

| Status | ID | Finding | Truth | Fix Type |
|---|---|---|---|---|
| ✗ | H7 | AI Overview / answer presence — **absent** from category "best payroll software MENA/UAE/Saudi" answer sets | MEASURED | cannot_fix_from_page |
| △ | H6 | E-E-A-T vs competitors — competitors have reviews/press/guides; Ratib has none found | COMPARATIVE | offpage_entity |
| — | H1–H5, H8 | Content depth, unique data, FAQ, schema, freshness, intent vs competitors — competitors not crawled | COMPARATIVE / MODEL JUDGMENT | content_restructure |

### Section I — GEO (FULLY ASSESSED — directional / MODEL JUDGMENT)

| Status | ID | Finding | Truth | Fix Type |
|---|---|---|---|---|
| ✗ | I1 | Brand in category queries — **absent** from all "best payroll MENA/UAE/Saudi 2026" lists | MODEL JUDGMENT | offpage_entity |
| △ | I2 | Knowledge panel / entity card — none found; no Crunchbase/press entity surfaced | MEASURED | offpage_entity |
| △ | I3 | AI description matches positioning — "MENA payroll" is consistent, but "#1" is uncorroborated | MODEL JUDGMENT | offpage_entity |
| ✓ | I4 | No outdated/incorrect AI info — what little exists is current (no stale misinfo) | MODEL JUDGMENT | offpage_entity |
| △ | I5 | Brand sentiment — neutral; no reviews to establish positive sentiment | MODEL JUDGMENT | offpage_entity |
| ✗ | I6 | Recommended over competitors — never; competitors own the category answers | MODEL JUDGMENT | offpage_entity |
| △ | I7 | Consistent entity across sources — consistent but extremely sparse (few sources exist) | MODEL JUDGMENT | offpage_entity |
| — | I8 | sameAs to authoritative profiles — schema unverified; no strong external profiles found | HARD EVIDENCE | schema |

### Section J — Entity Consistency (partial)

| Status | ID | Finding | Truth | Fix Type |
|---|---|---|---|---|
| ✓ | J1 | Organization name consistent — "Ratib" consistent on the few sources that mention it | HARD EVIDENCE | sitewide_template |
| — | J2, J3 | Logo / URL-domain consistency (schema/OG/canonical) — egress blocked | HARD EVIDENCE | sitewide_template |
| △ | J4 | sameAs URLs resolve — no authoritative external profiles found to link | MEASURED | schema |

---

## AEO Stage Analysis

| Stage | Score | Verdict |
|---|---|---|
| Discovery (E) | Weak (grounded) | Homepage indexed, but **inner pages effectively absent from index** — retrieval surface ≈ 1 page |
| Extraction (F) | NM | body content not fetchable |
| Trust (G) | Partial — thin | HTTPS OK; no off-page trust signals (reviews/press/citations) found |
| Selection (H) | Weak (grounded) | Loses every category answer to Bayzat/ZenHR/Jisr/Darwinbox |

**Diagnosis:** Ratib's AEO problem starts at **Discovery** — with essentially one indexed
page, there is almost nothing for AI engines to find, extract, or select, regardless of product
quality. Layered on top is a **category-presence vacuum**: zero third-party reviews, lists, or
press. The decisive technical unknowns (SSR, robots.txt AI rules, schema) could not be measured
and must be re-checked, but the grounded signals already point to a content/indexing + entity
problem as the primary blocker.

---

## GEO Dimension Analysis (Directional Assessment)

All GEO findings are MODEL JUDGMENT based on web search proxies. Results vary by location,
session, and time.

### Presence — 20%
Only `ratib.ai` homepage indexed; no knowledge panel, Crunchbase, or directory entity found;
absent from all category buyer-guides. AI engines have almost no Ratib data to surface.

### Accuracy — 50%
The "MENA & South Asia payroll, 500+ companies, 8 countries" positioning is internally
consistent. The "#1" superlative has no external corroboration — neither confirmed nor refuted
by third parties.

### Favorability — 20%
No reviews, ratings, or recommendations found. Competitors are actively recommended in category
answers; Ratib is not mentioned, so there is no favorability signal to build on yet.

---

## Competitor Profiles

*SERP-derived; pages not crawled (egress blocked).*

- **Bayzat (bayzat.com):** UAE-focused, WPS-compliant payroll + integrated insurance/benefits;
  positioned on simplicity for SMBs. Strong content + review footprint.
- **ZenHR (zenhr.com):** MENA HRMS + payroll with native GOSI/Mudad/WPS; deep localization
  across KSA/UAE/Jordan/Egypt/Iraq/Kuwait; large guide/blog library.
- **Jisr (jisr.net):** KSA-native payroll/HR, strong where local Saudi hosting is required.
- **NeuralHR (neuralhr.ai):** Saudi SMB pick — native Mudad/GOSI exports, AI anomaly detection,
  Saudization dashboard.
- **Darwinbox / Yomly / Keka:** Enterprise/multi-country GCC payroll & HRMS; broad footprints.

Full structural comparison (word count, schema, FAQ, dates, links) requires crawling — re-run
with open egress.

---

## Schema Audit Detail

**NOT AVAILABLE THIS RUN: egress blocked.** JSON-LD could not be fetched/parsed. For a
multi-country payroll SaaS, the high-value targets to verify/add are: `SoftwareApplication`
(with `applicationCategory: BusinessApplication`, `offers`), `Organization` (logo, `sameAs`
to LinkedIn/Crunchbase/G2), `FAQPage` for common WPS/GOSI questions, and `BreadcrumbList` on
inner pages once they exist. Confirm current state after a successful fetch before applying.

---

## Entity Consistency Matrix

| Entity | Schema | OG Tags | Title | Footer | Consistent? |
|---|---|---|---|---|---|
| Org name (Ratib) | NM | NM | ✓ (SERP) | NM | ✓ on the few sources that mention it |
| Logo | NM | NM | — | NM | UNKNOWN |
| URL/domain (ratib.ai) | NM | NM | ✓ | NM | ✓ |
| sameAs (LinkedIn/G2/Crunchbase) | NM | NM | — | NM | No strong external profiles found |

NM = not measured (egress blocked).

---

## Bot's Eye View — Full Detail

**NOT AVAILABLE THIS RUN: egress blocked (`host_not_allowed`).**
- curl response details: every UA + 404 probe returned identical `HTTP/2 403 / 21 bytes /
  x-deny-reason: host_not_allowed` — the environment proxy, not ratib.ai.
- Content verification: not possible.
- AI search presence verification: **branded** ("Ratib payroll") returns the homepage + a few
  ambiguous near-name results (RapidAI, RatibPal, Ratib Al Haddad) → weak entity disambiguation;
  **category** ("best payroll software UAE/Saudi/MENA 2026") returns competitors only.
- Classification statement: **UNDETERMINED** — re-measure with open egress.

---

## All Checks Index

| Category | Checks | Measured | Pass | Fail | Warn | N/A (egress) |
|---|---|---|---|---|---|---|
| A — Technical SEO | 12 | 2 | 0 | 0 | 2 | 10 |
| B — Performance | 11 | 0 | 0 | 0 | 0 | 11 |
| C — On-Page SEO | 13 | 1 | 0 | 0 | 1 | 12 |
| D — Schema | 13 | 0 | 0 | 0 | 0 | 13 |
| E — AEO Discovery | 13 | 1 | 0 | 1 | 0 | 12 |
| F — AEO Extraction | 12 | 0 | 0 | 0 | 0 | 12 |
| G — AEO Trust | 9 | 2 | 1 | 0 | 1 | 6 |
| H — AEO Selection | 8 | 2 | 0 | 1 | 1 | 6 |
| I — GEO | 8 | 7 | 1 | 3 | 3 | 1 |
| J — Entity | 4 | 2 | 1 | 0 | 1 | 2 |
| **Total** | **103** | **17** | **3** | **6** | **9** | **86** |

**17 of 103 checks were measurable** from outside the page fetch. The remaining 86 require
open egress (or pasted HTML) and are N/A — not failures.

---

## Brain Intelligence Applied

**Sieve / Supabase brain not queried this run** (project `aldraxqsqeywluohskhs` requires MCP
credentials not present). Attribution below is from live web sources gathered during recon.

🥇 TIER 1 — PRIMARY
- Google Search index — `site:ratib.ai` → homepage only; homepage title string. Applied to:
  A2, E8, H7, I1.

🥉 TIER 3 — INDUSTRY / DIRECTORIES
- Category buyer guides (Bayzat, ZenHR, NeuralHR, Iceipts, ZingHR, Keka, Yomly, SoftwareSuggest,
  Bolto). Used to establish competitor set and Ratib's absence. Applied to: H6, H7, I1, I6.

---

## Supplementary Findings

- **Name-collision / entity-disambiguation risk** — "Ratib" collides with RapidAI, RatibPal
  Services (India), and "Ratib Al Haddad" (a dhikr app). Weak entity authority means AI engines
  may conflate or fail to surface the payroll brand. Strengthen with `Organization` schema +
  `sameAs` to LinkedIn/Crunchbase/G2 and a clear entity homepage definition.
- **Single-page SaaS pattern** — common for early-stage products; the fastest compounding win
  is publishing indexable compliance/country/comparison content (Fix #1), which simultaneously
  helps Discovery (E), Extraction (F), and Selection (H).

---

## Audit Metadata
- Version: 3.0
- Checks run: 17/103 measurable | Passed: 3 | Failed: 6 | Warnings: 9 | N/A (egress): 86
- Gates: **DATA-COLLECTION GATE FAILURE** — target unreachable from this environment
  (`host_not_allowed`); homepage itself is live and indexed
- Page classification: SaaS homepage / product landing (HIGH confidence)
- Competitors analyzed: 5–6 (SERP-derived, not crawled)
- Chrome MCP: unavailable — CWV not measured
- Brain entries matched: 0 (Supabase not connected)
- Previous audit: none — first audit
- Queries used: primary, variant, category, branded
- Data sources: WebSearch (working) · curl/WebFetch (BLOCKED by egress policy) · Supabase (not connected) · Chrome MCP (not connected)

---

## Summary — "What to do this week"

**DO NOW (grounded):**
1. Publish and index real content pages — per-country WPS/GOSI/Mudad compliance, pricing,
   features — and add an XML sitemap (Fix #1). The single-page index is the #1 limiter.
2. Replace the unbacked "#1" claim with a concrete, verifiable proof point (Fix #3).

**PLAN (off-page, grounded):**
3. Create G2 / Capterra / SoftwareSuggest profiles and pursue inclusion in 2026 MENA/UAE/Saudi
   payroll buyer guides (Fix #2) — the route into category AI answers.

**BLOCKED — must re-run with open egress before acting:**
4. Verify SSR vs JS rendering, robots.txt AI-crawler rules, schema, and performance. Re-run:
   `bash skill/scripts/run_deterministic.sh https://ratib.ai/ human`

**Honest framing:** Unlike a mature brand, Ratib's grounded signals point to an **early-stage
visibility problem**: one indexed page, no category presence, no third-party corroboration of
its "#1" claim. These are fixable and high-leverage — content/indexing + entity-building — but
they are months of work, not page tweaks. The technical AEO verdict (schema, SSR, robots,
performance) is genuinely **unknown** from this environment and should be measured before
drawing further conclusions.

---
**Persistence confirmation:**
- Supabase: unreachable — not persisted (project `aldraxqsqeywluohskhs` requires MCP
  credentials not present in this environment)
- Markdown: audit-reports/ratib-ai-audit-1-2026-06-08.md ✓ saved
- ⚠ Technical core (curl/WebFetch) blocked by environment egress policy (`host_not_allowed`).
  This report is **recon-grade**, not a complete byte-accurate audit. Re-run with open egress.
