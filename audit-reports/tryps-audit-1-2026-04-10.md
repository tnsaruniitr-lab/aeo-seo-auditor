# TRYPS Audit Report #1

**Audit ID:** fbf9bc19-9fe8-4cea-a348-28027289709a
**URL:** https://trypsagent.com
**Domain:** jointryps.com
**Page Type:** Landing page
**Company:** TRYPS — A group trip planning app for friends — choose dates, shared itinerary, split expenses
**Industry:** Travel Tech
**Date:** 2026-04-10 10:28 UTC
**Audit Version:** 2.0 (WebFetch-based — pre curl-first fix)
**Duration:** ~180 seconds

---

## Scores

**Overall Score: 52% (F)**

| Section | Score |
|---|---|
| Technical SEO (A) | 72% |
| Performance (B) | 65% |
| On-Page SEO (C) | 68% |
| Schema (D) | 75% |
| AEO: Discovery (E) | 70% |
| AEO: Extraction (F) | 42% |
| AEO: Trust (G) | 19% |
| AEO: Selection (H) | 25% |
| GEO (I) | 15% |
| Entity (J) | 50% |

---

## Check Summary

| Metric | Count |
|---|---|
| Total checks run | 89 |
| Passed | 42 |
| Failed | 30 |
| Warnings | 17 |
| N/A | 8 |

---

## Executive Diagnosis

TRYPS is invisible to AI answer engines. Zero E-E-A-T signals. Content opens with marketing, not answers.

---

## Competitors Analyzed

| Name | Domain |
|---|---|
| SquadTrip | squadtrip.com |
| Wanderlog | wanderlog.com |
| Troupe | troupe.com |

---

## Target Queries

1. group trip planning app
2. best group trip planner
3. plan a trip with friends app

---

## Top 5 Fixes (Priority Order)

### Fix #1: Add Direct-Answer First Paragraph
**Impact:** Critical | **Effort:** Easy

The opening is a marketing tagline ("A group trip planning app your friends actually use"). AI engines need "TRYPS is a [category] that [function]" in sentence 1. The definition sentence exists on the page but is buried after the tagline.

### Fix #2: Add datePublished/dateModified
**Impact:** High | **Effort:** Trivial

No dates anywhere — not in schema, not visible on page. Perplexity gives 3.2x citation boost for content < 30 days. Without any date signal, AI engines cannot assess freshness.

### Fix #3: Create Comparison Content
**Impact:** High | **Effort:** Moderate

"Why not just use WhatsApp, Google Sheets, or Wanderlog?" section exists as heading with narrative content. Convert to structured comparison table. SquadTrip has a comparison table and ranks #1-2.

### Fix #4: Fix Canonical + Domain Split
**Impact:** Critical | **Effort:** Trivial

trypsagent.com redirects to jointryps.com. No canonical tag detected. Domain signal is split. Add `<link rel="canonical" href="https://jointryps.com/">`.

### Fix #5: Add Author Entity + E-E-A-T Signals
**Impact:** High | **Effort:** Easy

Person schema exists for Jake Stein as founder, but no visible author byline on page, no credentials, no sameAs links to external profiles.

---

## Key Findings by Section

### Technical SEO (72%)
- HTTPS: PASS
- Title tag: WARN (not extractable from WebFetch)
- Meta description: FAIL (not detected by WebFetch — **may be false failure due to WebFetch limitation**)
- Canonical tag: FAIL (not detected — **may be false failure**)
- Robots meta: PASS (no noindex)
- H1: PASS (single H1)
- robots.txt: PASS (allows all via wildcard)
- Sitemap: PASS (4 URLs)

### Schema (75%)
- 8 JSON-LD blocks: Organization, Person, WebSite, SoftwareApplication, HowTo, FAQPage (7 Q&A), MobileApplication x2, BreadcrumbList
- Organization: basic (name, url, logo) — missing sameAs, foundingDate
- Person (Jake Stein): name only — missing jobTitle, sameAs, credentials
- SoftwareApplication: name, version, rating 4.8/500, offers (free)
- FAQPage: 7 Q&A pairs — properly structured
- Missing: datePublished, dateModified in all schema blocks
- Missing: speakable property

### AEO Discovery (70%)
- PerplexityBot: PASS (allowed via wildcard)
- BingPreview: PASS
- Googlebot: PASS
- No nosnippet: PASS
- Content in raw HTML: PASS (WebFetch extracted substantial content)
- Page in sitemap: FAIL (only 4 URLs, many pages missing)

### AEO Extraction (42%)
- First paragraph: FAIL — opens with tagline, not entity definition
- FAQ section: PASS — 7 Q&A pairs
- FAQ semantic markup: PASS — details/summary
- Named entities: FAIL — "your friends", "your group" instead of "TRYPS"
- Specific facts: FAIL — very few numbers beyond "500+ groups"
- Definition-first: FAIL — tagline first, definition second
- Summary/TL;DR: FAIL — no recap section

### AEO Trust (19%)
- Author byline: FAIL
- Author schema credentials: FAIL (Person exists but no sameAs)
- Outbound citations: FAIL (zero)
- Publication date: FAIL (none)
- dateModified: FAIL (none)
- Organization sameAs: FAIL (none)
- Privacy/terms: PASS
- HTTPS: PASS (partial — no HSTS confirmed)

### AEO Selection (25%)
- Content depth vs competitors: FAIL (1,500 words vs SquadTrip 4,500)
- Schema completeness vs competitors: PASS (8 types — TRYPS strongest asset)
- Fresher than competitors: FAIL (no dateModified)
- Appears in AI results: FAIL (not in any AI results)

### GEO (15%)
- Brand in category queries: FAIL (TRYPS not in "best group trip planning app" results)
- Knowledge panel: FAIL
- Brand sentiment: N/A (no presence to assess)

### Entity Consistency (50%)
- Brand name consistent: PASS ("TRYPS" across schema and content)
- Domain split: FAIL (trypsagent.com → jointryps.com without canonical)

---

## Data Reliability Note

**This audit used WebFetch (v2 process).** WebFetch is an AI summarization layer that may miss HTML `<head>` elements unpredictably. Some FAIL results (meta description, canonical, OG tags) may be false failures — these elements may exist in the actual HTML but WebFetch didn't extract them.

The v3.1 curl-first audit (conducted later the same day) found a higher score of 68% after confirming meta description, canonical, OG tags, and Twitter cards all existed in the raw HTML.

**Treat this 52% score as a lower-bound estimate, not a precise measurement.**
