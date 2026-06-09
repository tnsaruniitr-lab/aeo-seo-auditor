# SEO + AEO + GEO Audit Report
**URL:** https://www.mmedien.net/
**Domain:** mmedien.net
**Page Type:** Agency homepage / professional-services local business (HIGH confidence)
**Company:** mmedien GmbH — Berlin communications agency (Content · Design · Marketing); founded 2009, ~10–25 staff, Google Partner, AGD member; niche strength in medical-practice (Arzt/Zahnarzt) and real-estate marketing
**Date:** 2026-06-08
**Audit version:** 3.0 (SKILL.md 15-phase protocol)
**Audit duration:** ~6 min (recon only — technical fetch blocked)
**Competitors analyzed:** prodoc.design, designery.health, digitalgrafik24.de, fjellfras.com, praxismarketingberlin.de — *SERP-derived only, not crawled*
**Target queries:**
  - Primary: `Werbeagentur Arztpraxis Berlin`
  - Variant: `Praxismarketing Berlin Ärzte Zahnärzte`
  - Category: `Online-Marketing-Agentur Berlin 2026`
  - Branded: `mmedien GmbH`

---

## ⚠ BLOCKING ISSUE DETECTED — DATA-COLLECTION GATE FAILURE (audit-environment, not the site)

**This audit could not fetch the target page.** Every outbound request to `mmedien.net` from
this execution environment was rejected by the environment's egress network policy:

```
HTTP/2 403
x-deny-reason: host_not_allowed
Host not in allowlist
```

This is **NOT** a fault of mmedien.net (curl + WebFetch both confirmed blocked). It is this
Claude-Code-on-the-web environment's **GitHub-only network policy** — every host except
github.com returns `host_not_allowed`.

**Consequence:** the curl-grounded technical core (raw HTML, headers, robots.txt, sitemap,
schema parse, Bot's Eye View bytes, performance) **could not run.** Those checks are marked
**N/A — egress blocked**, never pass/fail.

**What IS grounded:** `WebSearch` works. Page identity (from Google's index), index footprint,
company context, competitor set, and the full **GEO / Brand-AI-Presence** layer are real and
carry their normal truth badges.

**To get the full byte-accurate audit:** re-run with open egress (or allowlist `mmedien.net`),
or run `bash scripts-v2/run_local_batch.sh mmedien.net` from an open-network machine.

---

## Scores

### Page Citation Readiness: NOT COMPUTABLE THIS RUN
Requires curl ground-truth (HTML, headers, robots.txt, schema) — blocked by egress policy.

| Section | Score | Grade | Note |
|---|---|---|---|
| Technical SEO (A) | Partial | — | Title visible in index (over-optimized); rest egress-blocked |
| Performance (B) | NM | — | Needs curl timing + headers — egress blocked |
| On-Page SEO (C) | Partial | — | Title/URL structure from SERP only |
| Schema (D) | NM | — | Needs raw JSON-LD parse — egress blocked |
| AEO: Discovery (E) | Partial | — | robots.txt NM; **multi-page index footprint confirmed (grounded)** |
| AEO: Extraction (F) | NM | — | Needs body content — egress blocked |
| AEO: Trust (G) | Partial | — | HTTPS + reviews + memberships grounded; on-page author/date NM |
| AEO: Selection (H) | Partial | — | Competitors not crawled; niche-category presence grounded |
| Entity (J) | Partial | — | Name consistent across sources; schema NM |

`NM` = not measured (data collection blocked). `Partial` = only SERP-derivable portion assessed.

### Brand AI Presence: ~60% (C+) — DIRECTIONAL, fully assessed
Does this brand exist in AI's understanding of the category?

| Dimension | Score | Basis |
|---|---|---|
| Presence | 55% | Multi-page indexed site + Sortlist/agenturtipp profiles + appears in niche "Praxismarketing Berlin" answers; minor in the broad "Online-Marketing-Agentur Berlin" field |
| Accuracy | 75% | AI/SERP descriptions match positioning (content/design/marketing, Berlin, medical & real-estate niche) |
| Favorability | 55% | Positive reviews (Sortlist ~4, agenturtipp), but thin volume; not a dominant category recommendation |

Note: Brand presence is a directional assessment based on web search signals; page edits alone
cannot fix it — it needs content + entity-building work over months.

**Composite:**
- SEO / AEO / Citation Readiness: Not computable (technical core blocked)
- Brand AI Presence: ~60% (directional)

---

## Why This Page Isn't Being Cited (as strongly as it could be)

*Limited to what is grounded without page fetch.*

- **Severely keyword-stuffed homepage `<title>`** [HARD EVIDENCE — from Google's index].
  Google indexes the homepage title as:
  `mmedien GmbH | ᐅ CONTENT ᐅ DESIGN ᐅ MARKETING | Werbeagentur in Berlin,
  Online-Marketing-Agentur, Werbeagentur Arztpraxis, Werbeagentur Zahnarztpraxis,
  Werbeagentur Arzt, Werbeagentur Immobilienunternehmen, Werbeagentur Immobilienmakler`.
  That's ~200 characters, decorative ᐅ glyphs, and "Werbeagentur" repeated 6×. Google truncates
  it, and AI extractors get a noisy, diluted page label instead of one clear entity definition.
  The `/werbeagentur-arzt-zahnarzt/` page title is stuffed the same way.

- **Crowded niche, no clear lead signal** [MODEL JUDGMENT — directional].
  For "Praxismarketing / Werbeagentur Arzt Berlin," mmedien *does* appear — but alongside
  ProDoc.Design (since 2007), Designery (apoBank partner), Praxisdesign Dr. Peiler (30 yrs,
  450 clients), digitalgrafik24, STUDIO FJELLFRAS. Competitors carry stronger trust hooks
  (official partnerships, longevity, client counts); mmedien has none surfaced. Off-page work.

- **Thin third-party review volume** [HARD EVIDENCE — off-page].
  Reviews are positive but sparse (~4 on Sortlist; agenturtipp profile). AI favorability and
  category ranking lean on review density across G2/Google/Sortlist/agenturtipp — more
  corroborated reviews would lift Selection and Favorability.

*Technical citation blockers (schema, robots.txt AI-crawler rules, SSR) are UNVERIFIED this
run — egress blocked.*

---

## Bot's Eye View — What AI Crawlers See

**NOT AVAILABLE THIS RUN: egress blocked (`host_not_allowed`).** Byte-level Bot's Eye View
could not be measured (no UA could fetch the page).

| Metric | Value | Source |
|---|---|---|
| Raw HTML word count | UNKNOWN | curl blocked |
| Page size / schema blocks / FAQ / images / JS-dependency | UNKNOWN | curl blocked |

**Positive grounded signal:** `site:mmedien.net` returns a healthy multi-page index — homepage,
`/agentur/`, `/projekte/`, `/kontakt/`, `/nachhaltigkeit/`, `/partner/`, a dated `/blog/`
(posts 2023 & 2025), `/werbeagentur-arzt-zahnarzt/`, plus tag/category archives (WordPress-style).
So the site is reachable and indexable by Googlebot. Raw-HTML visibility to GPTBot/Perplexity/
ClaudeBot (SSR vs JS) remains **undetermined** this run.

AI crawler access: **UNDETERMINED THIS RUN** (re-run with open egress to classify).

---

## Performance (Measured)

**NOT AVAILABLE THIS RUN: egress blocked.** TTFB, total load, page size, HTTP version, HSTS,
compression, Cache-Control all require an origin response. Chrome MCP not connected → no CWV.

| Metric | Value | Rating | AI Impact |
|---|---|---|---|
| TTFB / LCP / CLS / INP / compression / cache | UNKNOWN | — | Re-run with open egress |

---

## Competitor Comparison — "Werbeagentur Arztpraxis / Praxismarketing Berlin"

**Partial — competitors identified via SERP but NOT crawled (egress blocked).** Structural
columns require fetching each page and are N/A. Positioning + trust hooks are SERP-derived.

| Signal | Your Page (mmedien) | ProDoc.Design | Designery | Praxisdesign Dr. Peiler |
|---|---|---|---|---|
| Word count / schema / FAQ | N/A (not crawled) | N/A | N/A | N/A |
| Niche focus | Medical + real estate + services | Medical (Arzt/Zahnarzt/MVZ) since 2007 | Medical practices | Medical, 30+ yrs |
| Standout trust hook | Google Partner, AGD member, 75% EV fleet | Specialist longevity (2007) | **apoBank official partner**, Web Award | **450+ clients, 30 yrs** |
| Appears in niche category answers | Yes (`/werbeagentur-arzt-zahnarzt/`) | Yes | Yes | Yes |
| Third-party reviews | Sortlist (~4), agenturtipp | Present | Present | Present |

Note: Based on SERP results for the query family on 2026-06-08. Results vary by location/time.
*(ProDoc.Design is also a target in this batch — useful head-to-head once both are crawled.)*

**Key Gaps:**
1. **Weaker headline trust hook** — rivals lead with apoBank partnership / 450 clients / 30 yrs;
   mmedien's strongest external signals (Google Partner, AGD) are less category-specific.
2. **Structural depth unmeasured** — word count, FAQ, schema vs competitors needs a crawl (H1–H6).
3. **Review density** — thin review count vs the corroboration AI engines reward in this niche.

---

## Top Fixes (Ranked by Impact)

*Limited to fixes grounded without a page fetch.*

### Fix #1: Rewrite the keyword-stuffed homepage `<title>`
**Impact:** High | **Effort:** Trivial | **Priority:** DO NOW
**Type:** PAGE HTML FIX
**Evidence:** HARD EVIDENCE (from Google's indexed title)

**BEFORE:**
```html
<title>mmedien GmbH | ᐅ CONTENT ᐅ DESIGN ᐅ MARKETING | Werbeagentur in Berlin,
Online-Marketing-Agentur, Werbeagentur Arztpraxis, Werbeagentur Zahnarztpraxis,
Werbeagentur Arzt, Werbeagentur Immobilienunternehmen, Werbeagentur Immobilienmakler</title>
```

**AFTER:**
```html
<title>mmedien GmbH – Werbeagentur für Praxis- & Content-Marketing in Berlin</title>
```

**WHY:** ~200 chars, repeated keywords, and ᐅ glyphs get truncated by Google and read as noise
by AI extractors. One clear ≤60-char title with the entity + core service + city gives a clean
page label and better SERP CTR. Move the long-tail keywords (Arzt, Zahnarzt, Immobilien) onto
their own dedicated, well-titled pages instead.

### Fix #2: Add a category-specific trust hook above the fold
**Impact:** High | **Effort:** Easy | **Priority:** PLAN
**Type:** CONTENT RESTRUCTURE
**Evidence:** MODEL JUDGMENT (competitor-relative)

**BEFORE:** Competitors lead with apoBank partner / "450 clients" / "since 2007"; mmedien's page
doesn't surface an equivalent category proof point in SERP snippets.

**AFTER:** Surface concrete proof — number of medical-practice clients served, years in
practice marketing, named certifications/partnerships — as a visible, schema-marked claim.

**WHY:** In a crowded niche, AI Selection and human CTR favor the agency with the strongest
*specific, verifiable* credibility signal. mmedien has the substance (since 2009, Google Partner,
AGD) — it just needs to be stated as a category-specific hook.

### Fix #3 (CONDITIONAL — verify first): Confirm LocalBusiness + Organization schema
**Impact:** High (if missing) | **Effort:** Easy | **Priority:** DO NOW *after verification*
**Type:** SCHEMA FIX
**Evidence:** N/A this run — schema presence UNVERIFIED (egress blocked)

**AFTER (template if missing):**
```json
{
  "@context": "https://schema.org",
  "@type": ["Organization","ProfessionalService"],
  "@id": "https://www.mmedien.net/#org",
  "name": "mmedien GmbH",
  "url": "https://www.mmedien.net/",
  "telephone": "+49 30 3642840-60",
  "email": "kontakt@mmedien.net",
  "foundingDate": "2009",
  "areaServed": "Berlin-Brandenburg & DE",
  "knowsAbout": ["Praxismarketing","Content Marketing","Webdesign","SEO","SEA"],
  "sameAs": ["https://www.linkedin.com/company/mmedien","https://www.sortlist.de/agency/mmedien-gmbh-agentur-fur-kommunikation"]
}
```

**WHY:** Organization/ProfessionalService schema with `sameAs` + `knowsAbout` strengthens entity
grounding and category association for AI answers. **Confirm current state before applying** —
a 2009-era WordPress agency site may already include this.

---

## Quick Wins
- Fix the homepage title (Fix #1) — trivial, high-value.
- Audit other stuffed titles (e.g. `/werbeagentur-arzt-zahnarzt/` carries the same pattern).
- Encourage more reviews on Google/Sortlist/agenturtipp to lift Favorability density.
- Confirm `sameAs` links to LinkedIn + Sortlist are present in Organization schema *(after fetch)*.

---

## All Findings by Section

*Legend: ✓ pass · ✗ fail · △ warn · — N/A. Checks needing a page fetch are `— N/A (egress
blocked)`, NOT failures.*

### Section A — Technical SEO (1 partial / 12)

| Status | ID | Finding | Truth | Fix Type |
|---|---|---|---|---|
| ✗ | A2 | Title present but **massively over-length & keyword-stuffed** (~200 chars, ᐅ glyphs, "Werbeagentur" ×6) | HARD EVIDENCE | page_html |
| — | A1 | HTTPS + HSTS — site is https (indexed); HSTS unverified | HARD EVIDENCE | sitewide_template |
| — | A3–A9 | Meta desc / canonical / robots-meta / H1 / lang / viewport — egress blocked | HARD EVIDENCE | page_html |
| — | A10 | robots.txt allows crawling — egress blocked (site is indexed → likely OK) | HARD EVIDENCE | sitewide_template |
| △ | A11 | Sitemap referenced — unverified, but multi-page index suggests sitemap present | HARD EVIDENCE | sitewide_template |
| — | A12 | Renders without JS — egress blocked | MEASURED | cms_constraint |

### Section B — Performance (0/11 measurable)

| Status | ID | Finding | Truth | Fix Type |
|---|---|---|---|---|
| — | B1–B11 | TTFB, render-blocking, image formats, compression, cache, CWV — origin response required — **egress blocked** | MEASURED / HARD EVIDENCE | sitewide_template |

### Section C — On-Page SEO (2 partial / 13)

| Status | ID | Finding | Truth | Fix Type |
|---|---|---|---|---|
| ✗ | C7 | Keyword stuffing — homepage title repeats "Werbeagentur" 6× with decorative glyphs | HEURISTIC | content_restructure |
| ✓ | C9 | URL clean & descriptive — `/agentur/`, `/projekte/`, `/werbeagentur-arzt-zahnarzt/` are clean, hyphenated (SERP) | HARD EVIDENCE | sitewide_template |
| △ | C12 | Visible date / freshness — dated blog posts (2023, 2025) indexed | HEURISTIC | page_html |
| — | C1–C6, C8, C10–C11, C14 | Heading hierarchy, keyword placement, internal links, alt text, OG/Twitter, word count, outbound links — egress blocked | HARD EVIDENCE / HEURISTIC | content_restructure |

### Section D — Schema / Structured Data (0/13 measurable)

| Status | ID | Finding | Truth | Fix Type |
|---|---|---|---|---|
| — | D1–D13 | All require raw JSON-LD parse — **egress blocked**. Targets to verify: `Organization`/`ProfessionalService` + `sameAs`, `BreadcrumbList` on inner pages, `BlogPosting` on blog, `FAQPage` if present. | HARD EVIDENCE / STATIC RULE | schema |

### Section E — AEO Discovery (1 partial / 13)

| Status | ID | Finding | Truth | Fix Type |
|---|---|---|---|---|
| ✓ | E8 | Index coverage — **healthy multi-page index** (agentur, projekte, blog, kontakt, niche pages) | HARD EVIDENCE | sitewide_template |
| — | E1–E7, E9–E13 | Perplexity/Bing/Google/GPTBot/ClaudeBot/CCBot robots rules, IndexNow, paywall, noarchive — egress blocked | HARD EVIDENCE | sitewide_template |

### Section F — AEO Extraction (0/12 measurable)

| Status | ID | Finding | Truth | Fix Type |
|---|---|---|---|---|
| — | F1–F12 | First-paragraph answer, quick-answer block, FAQ pairs, entities, facts, tables/lists — body content required — **egress blocked** | STATIC RULE / HEURISTIC | content_restructure |

### Section G — AEO Trust (3 partial / 9)

| Status | ID | Finding | Truth | Fix Type |
|---|---|---|---|---|
| ✓ | G6 | Organization off-page trust — Google Partner, AGD member (since 2021), Sortlist-verified, sustainability profile | HARD EVIDENCE (off-page) | schema |
| ✓ | G8 | HTTPS valid — indexed https URLs | HARD EVIDENCE | sitewide_template |
| △ | G9 | Content freshness — active blog (2025 posts) signals maintenance; per-page dateModified unverified | HARD EVIDENCE + MODEL JUDGMENT | content_restructure |
| — | G1–G5, G7 | Author byline/schema, outbound citations, dates in schema, privacy/terms — egress blocked | HARD EVIDENCE | content_restructure |

### Section H — AEO Selection (Competitor-Relative — partial)

| Status | ID | Finding | Truth | Fix Type |
|---|---|---|---|---|
| ✓ | H7 | AI answer presence — **appears** in niche "Praxismarketing/Werbeagentur Arzt Berlin" answer sets | MEASURED | cannot_fix_from_page |
| △ | H6 | E-E-A-T vs competitors — solid (Google Partner/AGD) but rivals lead with apoBank/longevity/client-count hooks | COMPARATIVE | offpage_entity |
| — | H1–H5, H8 | Content depth, unique data, FAQ, schema, freshness, intent vs competitors — competitors not crawled | COMPARATIVE / MODEL JUDGMENT | content_restructure |

### Section I — GEO (FULLY ASSESSED — directional / MODEL JUDGMENT)

| Status | ID | Finding | Truth | Fix Type |
|---|---|---|---|---|
| △ | I1 | Brand in category queries — **present in the medical-marketing niche**; minor in broad "Online-Marketing-Agentur Berlin" | MODEL JUDGMENT | offpage_entity |
| △ | I2 | Knowledge panel / entity card — GMB/CB Insights/ZoomInfo entries exist; rich panel unverified | MEASURED | offpage_entity |
| ✓ | I3 | AI description matches positioning — accurate (content/design/marketing, Berlin, medical & real-estate niche) | MODEL JUDGMENT | offpage_entity |
| ✓ | I4 | No outdated/incorrect AI info — current (2025 blog, AGD 2021) | MODEL JUDGMENT | offpage_entity |
| ✓ | I5 | Brand sentiment positive — favorable reviews (Sortlist, agenturtipp) | MODEL JUDGMENT | offpage_entity |
| △ | I6 | Recommended over competitors — one of several; not the default pick vs ProDoc/Designery/Peiler | MODEL JUDGMENT | offpage_entity |
| ✓ | I7 | Consistent entity across sources — name/positioning consistent (site, Sortlist, LinkedIn, CB Insights, ZoomInfo) | MODEL JUDGMENT | offpage_entity |
| — | I8 | sameAs to authoritative profiles — LinkedIn/Sortlist exist; schema linkage unverified | HARD EVIDENCE | schema |

### Section J — Entity Consistency (partial)

| Status | ID | Finding | Truth | Fix Type |
|---|---|---|---|---|
| ✓ | J1 | Organization name consistent — "mmedien GmbH" consistent across site + directories | HARD EVIDENCE | sitewide_template |
| — | J2, J3 | Logo / URL-domain consistency (schema/OG/canonical) — egress blocked | HARD EVIDENCE | sitewide_template |
| △ | J4 | sameAs URLs resolve — LinkedIn + Sortlist profiles exist; schema linkage unverified | MEASURED | schema |

---

## AEO Stage Analysis

| Stage | Score | Verdict |
|---|---|---|
| Discovery (E) | Good (grounded) | Healthy multi-page index; robots.txt AI rules unverified |
| Extraction (F) | NM | body content not fetchable |
| Trust (G) | Partial — solid off-page | Google Partner/AGD/HTTPS/active blog; on-page author/date NM |
| Selection (H) | Partial — competitive | Present in niche answers but not the lead; rivals have stronger hooks |

**Diagnosis:** mmedien's foundations are sound — real indexed footprint, active blog, legitimate
memberships, positive reviews, and genuine presence in its medical-marketing niche. The grounded
weaknesses are **on-page over-optimization** (stuffed titles diluting the entity label) and a
**comparatively soft trust hook** in a crowded niche. The technical AEO core (schema, SSR,
robots, performance) is unverified and should be measured before final scoring.

---

## GEO Dimension Analysis (Directional Assessment)

All GEO findings are MODEL JUDGMENT based on web search proxies. Results vary by location,
session, and time.

### Presence — 55%
Multi-page indexed site + Sortlist/agenturtipp/CB Insights/ZoomInfo/LinkedIn profiles + appears
in niche "Praxismarketing Berlin" answers. Minor presence in the very broad "Online-Marketing-
Agentur Berlin" field (huge competitive set).

### Accuracy — 75%
Descriptions across sources match positioning precisely: Berlin content/design/marketing agency,
founded 2009, medical & real-estate specialization, sustainability angle.

### Favorability — 55%
Positive but thin review volume (~4 Sortlist). Recommended in niche lists but not the default
pick versus ProDoc.Design, Designery (apoBank), or Praxisdesign Dr. Peiler (450 clients).

---

## Competitor Profiles

*SERP-derived; pages not crawled (egress blocked).*

- **ProDoc.Design® (prodoc.design):** Berlin practice-marketing agency since 2007 — websites,
  corporate design, marketing for Ärzte/Zahnärzte/Kliniken/MVZ. *(Also a target in this batch.)*
- **Designery (designery.health):** Official apoBank partner, Web Award winner — strong verified
  trust signals in the medical niche.
- **Praxisdesign Dr. Peiler (praxisdesign.de):** 30+ years, 450+ clients — longevity/scale hook.
- **digitalgrafik24 (digitalgrafik24.de):** Berlin dental marketing — practice sites + Zahnarzt SEO.
- **STUDIO FJELLFRAS (fjellfras.com):** Since 2009, practice marketing Berlin/Brandenburg + DE.

Full structural comparison (word count, schema, FAQ, dates, links) requires crawling — re-run
with open egress.

---

## Schema Audit Detail

**NOT AVAILABLE THIS RUN: egress blocked.** JSON-LD could not be fetched/parsed. High-value
targets to verify/add for an agency site: `Organization`/`ProfessionalService` (with `sameAs`,
`areaServed`, `knowsAbout`, telephone/email), `BreadcrumbList` on inner pages, `BlogPosting`
(author + datePublished/dateModified) on blog posts, and `FAQPage` where Q&A exists. Confirm
current state after a successful fetch before applying the Fix #3 template.

---

## Entity Consistency Matrix

| Entity | Schema | OG Tags | Title | Footer | Consistent? |
|---|---|---|---|---|---|
| Org name (mmedien GmbH) | NM | NM | ✓ (SERP) | NM | ✓ across site + directories |
| Logo | NM | NM | — | NM | UNKNOWN |
| URL/domain (mmedien.net) | NM | NM | ✓ | NM | ✓ |
| sameAs (LinkedIn, Sortlist) | NM | NM | — | NM | Profiles exist; schema linkage UNKNOWN |

NM = not measured (egress blocked).

---

## Bot's Eye View — Full Detail

**NOT AVAILABLE THIS RUN: egress blocked (`host_not_allowed`).**
- curl + WebFetch both returned `403 / host_not_allowed` — the environment proxy, not mmedien.net.
- Content verification: not possible.
- AI search presence: **branded** ("mmedien GmbH") → own multi-page site + Sortlist/LinkedIn/
  CB Insights/ZoomInfo (strong); **niche category** ("Werbeagentur Arzt Berlin") → present among
  several specialists; **broad category** ("Online-Marketing-Agentur Berlin") → minor.
- Classification: **UNDETERMINED** — re-measure with open egress.

---

## All Checks Index

| Category | Checks | Measured | Pass | Fail | Warn | N/A (egress) |
|---|---|---|---|---|---|---|
| A — Technical SEO | 12 | 2 | 0 | 1 | 1 | 10 |
| B — Performance | 11 | 0 | 0 | 0 | 0 | 11 |
| C — On-Page SEO | 13 | 3 | 1 | 1 | 1 | 10 |
| D — Schema | 13 | 0 | 0 | 0 | 0 | 13 |
| E — AEO Discovery | 13 | 1 | 1 | 0 | 0 | 12 |
| F — AEO Extraction | 12 | 0 | 0 | 0 | 0 | 12 |
| G — AEO Trust | 9 | 3 | 2 | 0 | 1 | 6 |
| H — AEO Selection | 8 | 2 | 1 | 0 | 1 | 6 |
| I — GEO | 8 | 7 | 4 | 0 | 3 | 1 |
| J — Entity | 4 | 2 | 1 | 0 | 1 | 2 |
| **Total** | **103** | **20** | **10** | **2** | **8** | **83** |

**20 of 103 checks were measurable** from outside the page fetch. The remaining 83 require open
egress (or pasted HTML) and are N/A — not failures.

---

## Brain Intelligence Applied

**Sieve / Supabase brain not queried this run** (credentials not present). Attribution below is
from live web sources gathered during recon.

🥇 TIER 1 — PRIMARY
- Google Search index — multi-page `site:mmedien.net` footprint; homepage title string; clean
  URL structure. Applied to: A2, C7, C9, E8, J1.

🥉 TIER 3 — INDUSTRY / DIRECTORIES
- Sortlist, agenturtipp.de, werbeagentur.de, feedbax, CB Insights, ZoomInfo, LinkedIn. Used for
  trust, reviews, and entity consistency. Applied to: G6, I2, I5, I7, J4.

---

## Supplementary Findings

- **Title-stuffing pattern is sitewide-risk** — both the homepage and `/werbeagentur-arzt-zahnarzt/`
  titles repeat keywords with ᐅ glyphs; check whether the WordPress SEO template applies this
  pattern across all pages (a sitewide_template fix, not a one-page fix).
- **Strong topical asset** — a dated blog (Content Marketing, Instagram-in-Google-Search 2025,
  Dienstleistungsmarketing 2023) is good freshness/topical-authority signal; ensure each post
  has `BlogPosting` schema with author + dates to convert it into AEO Trust value.
- **Sustainability angle (75% EV fleet, AGD)** is a differentiator that could be turned into
  citable, schema-marked credibility content.

---

## Audit Metadata
- Version: 3.0
- Checks run: 20/103 measurable | Passed: 10 | Failed: 2 | Warnings: 8 | N/A (egress): 83
- Gates: **DATA-COLLECTION GATE FAILURE** — target unreachable from this environment
  (`host_not_allowed`); site itself is live, healthy, and well-indexed
- Page classification: agency homepage / professional-services local business (HIGH confidence)
- Competitors analyzed: 5 (SERP-derived, not crawled)
- Chrome MCP: unavailable — CWV not measured
- Brain entries matched: 0 (Supabase not connected)
- Previous audit: none — first audit
- Queries used: primary, variant, category, branded
- Data sources: WebSearch (working) · curl/WebFetch (BLOCKED by egress policy) · Supabase (not connected) · Chrome MCP (not connected)

---

## Summary — "What to do this week"

**DO NOW (grounded):**
1. Rewrite the homepage `<title>` to one clear ≤60-char entity+service+city label; move long-tail
   keywords to dedicated pages (Fix #1). Check whether the stuffed pattern is sitewide.

**PLAN (grounded):**
2. Add a category-specific, verifiable trust hook above the fold (client count / years / named
   partnerships) to compete with apoBank/longevity signals in the niche (Fix #2).
3. Grow review density on Google/Sortlist/agenturtipp to lift Favorability and Selection.

**BLOCKED — must re-run with open egress before acting:**
4. Verify SSR, robots.txt AI-crawler rules, Organization/BlogPosting schema, and performance.
   Re-run: `bash scripts-v2/run_local_batch.sh mmedien.net` (open network) or
   `bash skill/scripts/run_deterministic.sh https://www.mmedien.net/ human`.

**Honest framing:** mmedien is a legitimately healthy small-agency site — real index footprint,
active blog, genuine memberships, positive reviews, real niche presence. This is *not* a "bad
website." The grounded opportunities are on-page (de-stuff the titles) and off-page (stronger
trust hook + more reviews). The full technical AEO verdict (schema/SSR/robots/perf) is genuinely
unknown from this environment and should be measured before final scoring.

---
**Persistence confirmation:**
- Supabase: unreachable — not persisted (credentials not present in this environment)
- Markdown: audit-reports/mmedien-net-audit-1-2026-06-08.md ✓ saved
- ⚠ Technical core (curl/WebFetch) blocked by environment egress policy (`host_not_allowed`).
  This report is **recon-grade**, not a complete byte-accurate audit. Re-run with open egress.
