# TRYPS Audit Report #2

**Audit ID:** 801fce2e-4663-43c1-ae58-a280207540fa
**URL:** https://trypsagent.com
**Domain:** jointryps.com
**Page Type:** Landing page
**Company:** TRYPS — Group trip planning app for friends — choose dates, shared itinerary, split expenses
**Industry:** Travel Tech
**Date:** 2026-04-10 12:44 UTC
**Audit Version:** 2.0 (WebFetch-based — pre curl-first fix)
**Duration:** ~90 seconds

---

## Scores

**Overall Score: 58% (F)**

| Section | Score | Change from Audit #1 |
|---|---|---|
| Technical SEO (A) | 65% | -7% |
| Performance (B) | 55% | -10% |
| On-Page SEO (C) | 60% | -8% |
| Schema (D) | 88% | **+13%** |
| AEO: Discovery (E) | 73% | +3% |
| AEO: Extraction (F) | 42% | 0% |
| AEO: Trust (G) | 33% | **+14%** |
| AEO: Selection (H) | 25% | 0% |
| GEO (I) | 15% | 0% |
| Entity (J) | 65% | **+15%** |

---

## Check Summary

| Metric | Count |
|---|---|
| Total checks run | 93 |
| Passed | 52 |
| Failed | 28 |
| Warnings | 13 |
| N/A | 8 |

---

## Executive Diagnosis

Schema significantly improved since last audit (+13%). Opening still doesn't answer query. No dates. Brand still invisible in category searches.

---

## What Changed Between Audit #1 and #2

### Schema Improvements (75% → 88%)

| Previous Gap | Status in Audit #2 |
|---|---|
| No Organization sameAs | **FIXED** — Instagram, LinkedIn, X (3 profiles) |
| No Person sameAs/credentials | **FIXED** — LinkedIn URL, jobTitle: "Founder" |
| No founder link in Organization | **FIXED** — founder object with Person reference |
| No featureList in SoftwareApp | **FIXED** — 5 features listed |
| No screenshots | **FIXED** — 3 screenshot URLs |
| No foundingDate | **FIXED** — 2025-01-01 |
| No contactPoint | **FIXED** — customer support email + URL |
| No knowsAbout | **FIXED** — 5 topic keywords |

### Trust Improvements (19% → 33%)

| Change | Impact |
|---|---|
| Organization sameAs added (3 profiles) | G6 moved from FAIL to PASS |
| Person schema enriched (jobTitle, sameAs, worksFor) | G2 partially improved |

### Entity Improvements (50% → 65%)

| Change | Impact |
|---|---|
| sameAs URLs added | J4 partially improved |
| Domain consistency improved | J3 improved |

### What Did NOT Improve

| Section | Score | Why |
|---|---|---|
| AEO Extraction (F) | 42% (unchanged) | Content structure unchanged — still opens with tagline |
| AEO Selection (H) | 25% (unchanged) | Not in SERP, no comparison table, below competitors |
| GEO (I) | 15% (unchanged) | Brand still not in category search results |
| Performance (B) | 55% (dropped) | Stricter assessment in this run |

---

## Competitors Analyzed

| Name | Domain |
|---|---|
| SquadTrip | squadtrip.com |
| Wanderlog | wanderlog.com |

---

## Target Queries (Multi-Query — 4 types)

| Type | Query |
|---|---|
| Primary | group trip planning app |
| Variant | plan a trip with friends online |
| Category | best group trip planning app 2026 |
| Branded | TRYPS app |

---

## Top 5 Fixes (Priority Order)

### Fix #1: Move Entity Definition to First Sentence
**Impact:** Critical | **Effort:** Easy | **Type:** CONTENT RESTRUCTURE

The definition sentence ("TRYPS is a group trip planning app for friends that helps you choose dates...") already exists on the page — it just needs to be the FIRST text, not the second. Currently the marketing tagline comes first.

### Fix #2: Add datePublished/dateModified
**Impact:** High | **Effort:** Trivial | **Type:** PAGE HTML + SCHEMA

Despite schema enrichment, dates are still completely absent. No visible date on page, no datePublished/dateModified in any schema block. 50% of AI citations from content < 13 weeks old.

### Fix #3: Add Canonical + Meta Description
**Impact:** High | **Effort:** Trivial | **Type:** PAGE HTML

Domain split (trypsagent.com → jointryps.com) without canonical fragments siteAuthority. Meta description may exist but was not detected by WebFetch.

### Fix #4: Fix Duplicate H1
**Impact:** Medium | **Effort:** Trivial | **Type:** PAGE HTML

Two H1 tags detected: "A group trip planning app your friends actually use" and "Group trip planning app." Consolidate to single H1 containing entity name + primary keyword.

### Fix #5: Add Comparison Table
**Impact:** High | **Effort:** Moderate | **Type:** CONTENT RESTRUCTURE

"Why not just use WhatsApp, Google Sheets, or Wanderlog?" section exists but uses narrative format. Convert to structured HTML table comparing features across TRYPS, WhatsApp, Google Sheets, Wanderlog.

---

## Key Findings by Section

### Technical SEO (65%)
- HTTPS: PASS
- Title tag: WARN (not fully extractable via WebFetch)
- Meta description: not confirmed (WebFetch limitation)
- Canonical: not confirmed (WebFetch limitation)
- H1: FAIL — 2 H1 tags detected (was 1 in Audit #1 — page changed)
- robots.txt: PASS
- Sitemap: PASS (but only 4 URLs)

### Schema (88%) — IMPROVED
- 9 schema blocks (was 8): Organization **enriched**, Person **enriched**, WebSite, SoftwareApplication **enriched**, HowTo, FAQPage (7 Q&A), MobileApplication x2, BreadcrumbList
- Organization now has: sameAs (Instagram, LinkedIn, X), foundingDate, contactPoint, founder with jobTitle, knowsAbout
- Person now has: sameAs (LinkedIn), jobTitle ("Founder"), worksFor
- SoftwareApplication now has: featureList (5 features), screenshots (3), aggregateRating (4.8/500)
- **Still missing:** datePublished, dateModified in all blocks. No speakable property.

### AEO Discovery (73%)
- All AI crawlers allowed via wildcard
- No nosnippet directives
- Content in raw HTML (SSR)
- Sitemap exists but only 4 URLs — many destination pages NOT in sitemap
- No IndexNow mechanism

### AEO Extraction (42%) — UNCHANGED
- Opening: still a tagline, not entity definition
- FAQ: 7 Q&A pairs — good
- FAQ markup: details/summary — good
- Named entities: still dominated by "your", "you" instead of "TRYPS"
- Specific facts: still few — "500+ groups" is main number
- No summary/TL;DR section
- No comparison table

### AEO Trust (33%) — IMPROVED
- Organization sameAs: **PASS** (3 profiles — was FAIL)
- Person schema: **improved** (jobTitle, sameAs — was basic)
- Outbound citations: still FAIL (zero)
- Publication date: still FAIL (none)
- dateModified: still FAIL (none)
- Privacy/terms: PASS

### AEO Selection (25%) — UNCHANGED
- Content depth: 1,500 words vs SquadTrip 4,500 — below median
- FAQ: 7 pairs vs SquadTrip 8 — near median
- Schema: 9 types vs SquadTrip 4 — ABOVE median (TRYPS strength)
- Freshness: no dateModified — all competitors weak here too
- Not in AI results for any target query

### GEO (15%) — UNCHANGED
- Brand not in "best group trip planning app" results
- No knowledge panel
- Brand not recommended in any category query

### Entity (65%) — IMPROVED
- Brand name "TRYPS" consistent across schema and content: PASS
- Organization sameAs present (3 profiles): improved
- Domain: canonical added? — not confirmed via WebFetch

---

## Brain Intelligence Applied

| Brain Entry | Check | Status |
|---|---|---|
| Rule #1487 (0.99): Allow PerplexityBot | E1 | PASS |
| Rule #1481 (0.99): Serve raw HTML | E5 | PASS |
| Rule #1448 (0.95): Answer-first structure | F1 | FAIL |
| Rule #1474 (0.95): Signal freshness | G5, G9 | FAIL |
| Rule #1478 (0.92): Cite authoritative sources | G3 | FAIL |
| AP#3 (high): AI Answer Evasion | F1 | PARTIAL — page has definition but leads with marketing |
| AP#797 (high): Vague Marketing Language | F8 | PARTIAL — "500+ groups" is specific, but most claims qualitative |

---

## Competitor Comparison — "group trip planning app"

| Signal | TRYPS | SquadTrip | Wanderlog |
|---|---|---|---|
| In SERP | No | Yes (#1-2) | Yes (#3-5) |
| Word Count | ~1,500 | ~4,500 | ~8,500 |
| FAQ Pairs | 7 | 8 | 0 |
| Schema Types | 9 | 4 | ~1 |
| Comparison Table | No | Yes | No |
| dateModified | None | None | None |
| Author | None | None | None |
| Social Proof | "500+ groups" | "2,000+ organizers" | "60+ testimonials" |

---

## Data Reliability Note

**This audit used WebFetch (v2 process).** Some technical check results (meta description, canonical, OG tags, lang, viewport) may be unreliable due to WebFetch's inconsistent extraction of `<head>` elements.

A subsequent v3.1 curl-first audit (same day, not persisted due to Supabase timeout) confirmed:
- Meta description EXISTS (137 chars)
- Canonical EXISTS (self-referencing to jointryps.com)
- OG tags EXIST (complete suite with image + dimensions)
- Twitter Card EXISTS (summary_large_image)
- `<html lang="en">` EXISTS
- Viewport EXISTS
- **True curl-measured score: approximately 68% PCR (D+)**

The 58% score stored in Supabase is a lower-bound estimate due to WebFetch false failures. The curl-first process (v3.1+) eliminates this class of measurement error.

---

## Trend Summary

| Metric | Audit #1 (10:28) | Audit #2 (12:44) | Change |
|---|---|---|---|
| Overall | 52% (F) | 58% (F) | +6% |
| Schema | 75% | 88% | **+13%** |
| Trust | 19% | 33% | **+14%** |
| Entity | 50% | 65% | **+15%** |
| Extraction | 42% | 42% | 0% |
| Selection | 25% | 25% | 0% |
| GEO | 15% | 15% | 0% |
| Checks passed | 42/89 | 52/93 | +10 |

**Schema enrichment worked.** D, G, and J all improved significantly. But content structure (F), competitive position (H), and brand presence (I) didn't change — those require content restructuring and off-page work, not metadata fixes.
