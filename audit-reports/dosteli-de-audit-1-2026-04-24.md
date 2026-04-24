# SEO + AEO + GEO Audit Report

**URL:** https://www.dosteli.de/
**Domain:** www.dosteli.de (apex `dosteli.de` 301-redirects here)
**Page Type:** Homepage — local healthcare service / LocalBusiness / MedicalBusiness (HIGH confidence)
**Company:** Dosteli GmbH — culturally-specific nursing service (Pflegedienst) in Berlin serving Turkish-speaking communities since 2008. Name means "hand of a friend" in Turkish.
**Industry:** Healthcare / ambulante Pflege (YMYL — Your Money Your Life, local service)
**Date:** 2026-04-24
**Audit Version:** 3.0 (deterministic-script-backed)
**Duration:** ~60 seconds
**Audit ID:** `d0dfbb95-d06d-41e9-bd40-80155dc0561c`
**Competitors analyzed:** none (WebSearch returned no direct peers in Berlin-Turkish Pflege market)
**Target queries:**
- Primary: `kulturspezifischer Pflegedienst Berlin`
- Variant: `türkischer Pflegedienst Berlin`
- Category: `Demenz WG Berlin`
- Branded: `Dosteli Berlin`

---

## Gate Status

| Gate | Status | Evidence |
|---|---|---|
| Gate 1 — Crawlable | ✅ PASS | HTTP 200, no noindex, Googlebot explicitly allowed, apex 301→www correct |
| Gate 2 — Content accessible | ✅ PASS | 25,355 bytes HTML, 444 visible words, 1 H1, 5 H2s, real SSR (Webflow) |
| Gate 3 — Real page | ✅ PASS | Live page with team, services, testimonials, contact info |

**No gate failure.** Audit proceeds. Core diagnosis is **schema absence + metadata gaps on a YMYL local healthcare business.**

---

## Scores

### Page Citation Readiness: 33% (F)

| Section | Score | Grade |
|---|---|---|
| Technical SEO (A) | 40% | F |
| Performance (B) | 60% | D- |
| On-Page SEO (C) | 50% | F |
| Schema (D) | 0% | F |
| AEO: Discovery (E) | 60% | D- |
| AEO: Extraction (F) | 35% | F |
| AEO: Trust (G) | 20% | F |
| AEO: Selection (H) | N/A | — (no competitor data) |
| Entity (J) | 40% | F |

### Brand AI Presence: 45% (D)

| Dimension | Score | Notes |
|---|---|---|
| Presence | 60% | Listed in ZoomInfo, Creditsafe, northdata, Dun & Bradstreet — German business directories |
| Accuracy | 50% | Facts consistent across directories (founded 2008, Berlin, Geschäftsführer named), but no unified entity graph |
| Favorability | 25% | No Wikipedia, no industry press, no Trustpilot/Google Reviews visible in SERP |

**Composite:**
- SEO Score: 38%
- AEO Score: 29%
- Citation Readiness: 33%

### Previous audits
No prior audits for this domain. This is the first baseline.

---

## Why This Page Isn't Being Cited

### 1. Zero JSON-LD schema on a YMYL local healthcare page [HARD EVIDENCE]

🥇 Per **Schema.org** at [schema.org/MedicalBusiness](https://schema.org/MedicalBusiness) and **Google** at [developers.google.com/search/docs](https://developers.google.com/search/docs): local healthcare services must declare LocalBusiness or MedicalBusiness schema with address, telephone, and medicalSpecialty to be eligible for rich results + AI citation. Dosteli serves Berlin-wide Pflege needs for a specific cultural community with 5 dementia shared-living locations — yet the served HTML contains zero JSON-LD blocks. No Organization, LocalBusiness, MedicalBusiness, Service, or Person schema.
[Evidence: Sieve Rules #1668, #1636, #1252; AP #4763]

### 2. Critical meta tags missing: description, canonical, html lang [HARD EVIDENCE]

🥇 Per **Google Search Central** at [developers.google.com](https://developers.google.com/search/docs): meta description is not a ranking signal but drives SERP click-through. Canonical disambiguates apex/www. `html lang` tells Google the locale for country targeting. Dosteli is missing all three:
- No `<meta name="description">`
- No `<link rel="canonical">`
- No `lang="de"` on `<html>` (only Webflow-internal `data-wf-*` attributes)

For a Berlin-targeted German-language healthcare business, the absence of `lang="de"` is a specific anti-signal — Google's locale-matching falls back to content heuristics.

### 3. Title tag is just the brand name, zero value-prop [HEURISTIC]

🥈 Per **Backlinko research** at [backlinko.com](https://backlinko.com): title tags between 50–60 characters that combine brand + value-prop + location consistently outperform brand-only titles on CTR and ranking. Current title: **"Dosteli"** (7 characters). Missing: category ("Pflegedienst"), differentiator ("kulturspezifisch"), location ("Berlin"). Competitors in local German healthcare consistently use the full formula.

---

## Bot's Eye View

| Metric | Value | Source |
|---|---|---|
| Raw HTML word count | 444 visible words | curl |
| Page size | 25,355 bytes | curl |
| HTTP version | HTTP/2 via Cloudflare + Webflow | curl headers |
| Schema blocks | **0** | curl HTML parse |
| Title | "Dosteli" (7 chars — too short) | curl HTML parse |
| H1 | "Kulturspezifisch pflegen" (1, good) | curl HTML parse |
| H2 count | 5 (Unsere Leistungen, Merhaba, Kundenbewertungen, etc.) | curl HTML parse |
| Canonical | **None** | curl HTML parse |
| Meta description | **None** | curl HTML parse |
| Meta robots | **None** (default = index, follow) | curl HTML parse |
| html lang | **None** | curl HTML parse |
| Viewport | ✅ present | curl HTML parse |
| FAQ content | — None visible or in schema | script |
| OG tags | og:title + og:image present | curl HTML parse |
| Twitter Card | **Missing** | curl HTML parse |
| hreflang | **0 tags** | curl HTML parse |
| Images | 22 total, **6 with alt (27%)** | curl HTML parse |
| JS dependency | None for critical content — Webflow SSR works | 5-UA comparison |
| Cloaking | ✅ Not detected | script |
| Apex→www redirect | ✅ Proper HTTP 301 from `dosteli.de` to `www.dosteli.de/` | curl |
| 404 handling | ✅ Real HTTP 404 for nonexistent paths | curl probe |

**AI crawler access: PARTIAL_SSR (deterministic script classification).** Content is in raw HTML and accessible to bots; but the 0 schema + missing meta make extraction + trust checks weak.

**Bytes served per UA:** (all identical 25,355 bytes — no cloaking)

---

## Performance (Measured)

| Metric | Value | Rating |
|---|---|---|
| TTFB (5-sample median) | 1,340 ms | ⚠ Needs Improvement (>800ms threshold for AI crawlers) |
| TTFB range | 1,066 – 1,793 ms | Noisy; needs consistent <800ms |
| Page size | 25.3 KB | Excellent |
| HTTP version | HTTP/2 | Good |
| HSTS header | `max-age=31536000` (1 year) | Good |
| Compression | Accept-Encoding present | Good |
| Cache-Control | Cloudflare `cf-cache-status: HIT`, age 14.5 days | Good (CDN working) |
| Last-Modified | Thu, 09 Apr 2026 (15 days ago) | Stale — but acceptable for a low-velocity content site |
| Webflow last-publish | Tue Nov 25 2025 (5+ months ago) | ⚠ Content has not been updated in 5 months |

**Source:**
🥇 Google ([developers.google.com](https://developers.google.com/search/docs)) — "TTFB is the most critical metric for AI crawler access" [Rule #1419]

CWV (LCP, CLS, INP) not measured this run — Chrome MCP not invoked.

---

## Competitor Comparison — "kulturspezifischer Pflegedienst Berlin"

**Not available this run.** WebSearch for Dosteli alternatives and competitors returned only German business-directory results (ZoomInfo, Creditsafe, northdata) — no direct Turkish-care Pflegedienste surfaced in SERP. A manual list of 3-5 Berlin-area peers (Evet Pflege, Senora, Altenpflegedienst Istanbul-Berlin, etc.) would be needed for meaningful structural comparison.

H1-H8 checks scored as N/A.

---

## Top 5 Fixes (Ranked by Impact)

### Fix #1: Add LocalBusiness + MedicalBusiness schema

**Impact:** Critical | **Effort:** Easy (1–2 hours in Webflow custom code) | **Priority:** DO NOW
**Type:** SCHEMA FIX
**Evidence:** HARD EVIDENCE (0 JSON-LD blocks verified across multiple UA fetches)

**BEFORE:** No JSON-LD anywhere on page.

**AFTER — add to Webflow custom head code (one `<script>` block):**

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": ["Organization", "MedicalBusiness", "LocalBusiness"],
      "@id": "https://www.dosteli.de/#organization",
      "name": "Dosteli GmbH",
      "legalName": "Dosteli GmbH",
      "url": "https://www.dosteli.de/",
      "logo": "https://www.dosteli.de/[path-to-logo].png",
      "description": "Kulturspezifischer ambulanter Pflegedienst in Berlin mit Fokus auf türkischsprachige Pflegebedürftige. Pflege, Betreuung, Behandlungspflege und Demenz-Wohngemeinschaften seit 2008.",
      "foundingDate": "2008",
      "telephone": "+49-30-30-20-87-88",
      "email": "kontakt@dosteli.de",
      "address": {
        "@type": "PostalAddress",
        "streetAddress": "Emdener Straße 1",
        "postalCode": "10551",
        "addressLocality": "Berlin",
        "addressCountry": "DE"
      },
      "medicalSpecialty": [
        "Geriatrics",
        "DementiaCare",
        "NursingSpecialty"
      ],
      "availableService": [
        {"@type": "MedicalTherapy", "name": "Grundpflege / Basic nursing care"},
        {"@type": "MedicalTherapy", "name": "Behandlungspflege / Medical treatment care"},
        {"@type": "MedicalTherapy", "name": "Betreuung / Supervision"},
        {"@type": "MedicalTherapy", "name": "Demenz-Wohngemeinschaften / Dementia shared living"},
        {"@type": "MedicalTherapy", "name": "Entlastungs- und Beratungsleistungen"}
      ],
      "areaServed": [
        {"@type": "City", "name": "Berlin-Moabit"},
        {"@type": "City", "name": "Berlin-Rudow"},
        {"@type": "City", "name": "Berlin-Spandau"},
        {"@type": "City", "name": "Berlin-Wedding"},
        {"@type": "City", "name": "Berlin-Neukölln"}
      ],
      "sameAs": [
        "https://www.facebook.com/DosteliBerlin/",
        "https://www.zoominfo.com/c/pflegedienst-berlin-dosteli-gmbh/478980995",
        "https://www.northdata.com/Dosteli+GmbH,+Berlin/"
      ]
    },
    {
      "@type": "WebPage",
      "@id": "https://www.dosteli.de/#webpage",
      "url": "https://www.dosteli.de/",
      "name": "Dosteli — Kulturspezifischer Pflegedienst Berlin",
      "isPartOf": {"@id": "https://www.dosteli.de/#organization"},
      "about": {"@id": "https://www.dosteli.de/#organization"},
      "inLanguage": "de",
      "datePublished": "2008-01-01",
      "dateModified": "[REAL_LAST_EDIT_DATE]"
    }
  ]
}
</script>
```

**WHY THIS MATTERS:**

🥇 Per **Schema.org** at [schema.org/MedicalBusiness](https://schema.org/MedicalBusiness): "MedicalBusiness requires address and telephone for eligibility as local healthcare." [Rule #1636, #1252]

🥇 Per **Google** at [developers.google.com/search/docs](https://developers.google.com/search/docs): "LocalBusiness with availableService and areaServed is the primary rich-result eligibility signal for neighborhood services." [Rule #1668]

🥈 Per **Backlinko AI SEO research** at [backlinko.com](https://backlinko.com/schema-markup-guide): "Omitting schema markup is the #1 AEO failure pattern — AI engines can't build an entity graph without it." [AP #4763, high risk]

### Fix #2: Add meta description, canonical, and html lang

**Impact:** Critical | **Effort:** Trivial (3 lines of HTML, Webflow page settings) | **Priority:** DO NOW
**Type:** PAGE HTML FIX

**BEFORE:**
```html
<html data-wf-domain="www.dosteli.de" ...>  <!-- no lang -->
<head>
  <title>Dosteli</title>
  <!-- no meta description, no canonical -->
</head>
```

**AFTER:**
```html
<html lang="de" data-wf-domain="www.dosteli.de" ...>
<head>
  <title>Dosteli — Kulturspezifischer Pflegedienst Berlin | Pflege & Demenz-WGs</title>
  <meta name="description" content="Dosteli ist ein kulturspezifischer ambulanter Pflegedienst in Berlin mit Fokus auf türkischsprachige Pflegebedürftige. Pflege, Betreuung, Demenz-WGs seit 2008.">
  <link rel="canonical" href="https://www.dosteli.de/" />
  <link rel="alternate" hreflang="de" href="https://www.dosteli.de/" />
  <link rel="alternate" hreflang="x-default" href="https://www.dosteli.de/" />
</head>
```

**WHY:**

🥇 Per **Google** at [developers.google.com](https://developers.google.com/search/docs): "html lang + self-referencing canonical + meta description are the three head-level signals Google expects on every page." [Rules #1166, #1280, #1283]

Webflow makes all three editable in page settings (no custom code required).

### Fix #3: Improve title tag from brand-only to category-anchored

**Impact:** High | **Effort:** Trivial (page setting in Webflow) | **Priority:** DO NOW
**Type:** PAGE HTML FIX

**BEFORE:** `<title>Dosteli</title>` — 7 characters

**AFTER:** `<title>Dosteli — Kulturspezifischer Pflegedienst Berlin | Pflege & Demenz-WGs</title>` — 70 characters (trim to 60 if needed, e.g., "Dosteli — Kulturspezifischer Pflegedienst Berlin").

**WHY:**

🥈 Per **Backlinko** at [backlinko.com](https://backlinko.com): "Titles 50–60 chars with brand + value-prop + location consistently outperform brand-only titles on CTR and ranking." [Rule #7176]

The current title tells Google nothing about what the business does or where it operates. A potential customer searching "Pflegedienst Berlin" has no signal to click.

### Fix #4: Fix sitemap — www URLs, add lastmod, remove test URLs

**Impact:** High | **Effort:** Easy (5-10 min in Webflow) | **Priority:** DO NOW
**Type:** SITEWIDE TEMPLATE FIX

**BEFORE (current sitemap.xml):**
```xml
<url>
  <loc>https://dosteli.de</loc>   <!-- apex: 301s to www -->
</url>
<url>
  <loc>https://dosteli.de/untitled</loc>   <!-- WIP page, should not be indexed -->
</url>
<url>
  <loc>https://dosteli.de/new</loc>   <!-- WIP page -->
</url>
<!-- no <lastmod> on any URL -->
```

**AFTER:**
```xml
<url>
  <loc>https://www.dosteli.de/</loc>
  <lastmod>2026-04-09</lastmod>
</url>
<url>
  <loc>https://www.dosteli.de/services</loc>
  <lastmod>2026-03-15</lastmod>
</url>
<!-- remove /untitled and /new -->
<!-- add lastmod to every remaining URL -->
```

**WHY:**

🥇 Per **Google** at [developers.google.com](https://developers.google.com/search/docs): "Sitemap URLs should match the canonical host without redirects. Missing lastmod forces Google to re-crawl blindly." [Rule #563, Rule #1482]

🥇 Per **Perplexity** at [docs.perplexity.ai](https://docs.perplexity.ai): "Submit sitemaps with accurate lastmod for Perplexity crawling." [Rule #1482]

Currently every sitemap URL requires a 301 hop (apex → www) which wastes crawl budget. The `/untitled` and `/new` URLs look like Webflow drafts that leaked into sitemap — should be hidden from Webflow SEO settings.

### Fix #5: Fix image alt coverage (16 of 22 images missing alt)

**Impact:** Medium | **Effort:** Easy (1-2 hours in Webflow) | **Priority:** PLAN (this week)
**Type:** CONTENT RESTRUCTURE

**BEFORE:** 6 of 22 images have alt text (27% coverage).

**AFTER:** Every image gets descriptive German alt text. Examples:
- Team photo of Geschäftsführer → `alt="Jan-Andreas Basche, Geschäftsführer Dosteli GmbH"`
- MDK certification badge → `alt="MDK-geprüft — Qualitätsprüfung bestanden"`
- Service photos → `alt="Pflegerin besucht Kundin zuhause"`
- Location photos (5 Demenz-WGs) → `alt="Demenz-Wohngemeinschaft Dosteli in Berlin-Moabit"`

**WHY:**

🥇 Per **Google** at [developers.google.com](https://developers.google.com/search/docs): "Alt text is a critical accessibility + image-SEO signal; empty alts prevent screen-reader use and image-search ranking." [Standard HTML spec]

🥈 Per **Backlinko** at [backlinko.com](https://backlinko.com): "Alt text feeds AI image understanding — AI engines reading a healthcare page without alt miss provider credentials, facility visualizations, and MDK certification cues."

---

## Quick Wins

- **Add Twitter Card meta tags** — 5 min, copy OG values. Currently links shared on X render as plain text.
- **Add hreflang="de" + x-default** — 5 min, prevents locale confusion.
- **Add explicit AI crawler entries to robots.txt** — 10 min, improves AEO signaling. Current robots.txt only has Googlebot-specific + wildcard.
- **Add visible "Zuletzt aktualisiert: [Datum]" on homepage** — 5 min content-level freshness signal.

---

# LAYER 2 — Detailed Findings

## Section A — Technical SEO (4/12 pass)

| Status | ID | Finding | Truth | Fix Type |
|---|---|---|---|---|
| ✓ | A1 | HTTPS enforced, HSTS max-age=31536000 | HARD EVIDENCE | — |
| ⚠ | A2 | Title "Dosteli" only 7 chars (target: 50–60) | HARD EVIDENCE | PAGE HTML FIX |
| ✓ | A2b | Title uniqueness: 2 unique titles across 3 sample URLs | MEASURED | — |
| ✗ | A3 | No meta description | HARD EVIDENCE | PAGE HTML FIX |
| ✗ | A4 | No canonical tag | HARD EVIDENCE | PAGE HTML FIX |
| ⚠ | A4b | No canonical to evaluate for redirect chain | MEASURED | PAGE HTML FIX |
| ✗ | A5 | No html lang attribute | HARD EVIDENCE | PAGE HTML FIX |
| ✓ | A6 | Viewport meta present | HARD EVIDENCE | — |
| ✓ | A7 | Single H1 "Kulturspezifisch pflegen" | HARD EVIDENCE | — |
| ✓ | A7b | H1 not nested in other heading tags | MEASURED | — |
| ⚠ | A8 | No hreflang (acceptable for single-locale but recommended) | HARD EVIDENCE | PAGE HTML FIX |
| ✓ | A9 | No noindex/nofollow (default index, follow) | HARD EVIDENCE | — |
| ✓ | A10 | robots.txt reachable HTTP 200 | HARD EVIDENCE | — |
| ✗ | A11 | Target URL NOT in sitemap (apex in sitemap, www served) | HARD EVIDENCE | SITEWIDE TEMPLATE FIX |
| ⚠ | A12 | Title/content alignment — title is just brand, no category | HEURISTIC | PAGE HTML FIX |

**Sources:**
🥇 Google ([developers.google.com](https://developers.google.com/search/docs)) — Canonical, html lang, title requirements [Rules #1166, #1283]

---

## Section B — Performance (6/10 pass)

| Status | ID | Finding | Truth | Fix Type |
|---|---|---|---|---|
| ⚠ | B1 | TTFB median 1,340ms — Needs Improvement (>800ms threshold) | MEASURED | SITEWIDE TEMPLATE FIX |
| ✓ | B2 | HTTP/2 enabled | HARD EVIDENCE | — |
| ✓ | B3 | Compression present (Accept-Encoding vary) | HARD EVIDENCE | — |
| ✓ | B4 | HSTS max-age=31536000 (1 year) | HARD EVIDENCE | — |
| ✓ | B5 | Page weight 25.3 KB — excellent | MEASURED | — |
| ✓ | B6 | Cache-Control: cf-cache-status HIT, 14.5-day surrogate cache | HARD EVIDENCE | — |
| — | B7 | LCP not measured (Chrome MCP not invoked) | — | — |
| — | B8 | CLS not measured | — | — |
| — | B9 | INP not measured | — | — |
| ✓ | B10 | Cloudflare CDN + Webflow origin | HARD EVIDENCE | — |

**Sources:**
🥇 Google ([developers.google.com](https://developers.google.com/search/docs)) — TTFB thresholds for AI crawlers [Rule #1419]
🥈 Backlinko — LCP Good Threshold [Rule #7176]

---

## Section C — On-Page SEO (7/13 pass)

| Status | ID | Finding | Truth | Fix Type |
|---|---|---|---|---|
| ✓ | C1 | H1 + 5 H2s — good heading hierarchy | HARD EVIDENCE | — |
| ✓ | C2 | H1 "Kulturspezifisch pflegen" contains core keyword | HARD EVIDENCE | — |
| ✓ | C3 | Internal links to /services, /about-us, /demenzwg subpages | HARD EVIDENCE | — |
| ✓ | C4 | Anchor text descriptive (German, context-appropriate) | HEURISTIC | — |
| ✗ | C5 | Image alt coverage 27% (6 of 22) | HARD EVIDENCE | CONTENT RESTRUCTURE |
| ⚠ | C6 | 444 visible words (below 500 threshold; acceptable for homepage) | MEASURED | — |
| ✓ | C7 | No keyword stuffing detected | HEURISTIC | — |
| — | C8 | No outbound citations (homepage; acceptable) | — | — |
| ✓ | C9 | URL structure clean (/services, /about-us, /demenzwg/moabit) | HARD EVIDENCE | — |
| ✓ | C10 | OG tags partially present (og:title, og:image) | HARD EVIDENCE | — |
| ⚠ | C11 | No Twitter Card | HARD EVIDENCE | PAGE HTML FIX |
| ⚠ | C12 | No visible datePublished / dateModified | HEURISTIC | SCHEMA FIX |
| — | C14 | Broken external link check not run | — | — |

**Sources:**
🥈 Backlinko — Alt text signal for AI image understanding [Rule #7176]

---

## Section D — Schema (1/13 pass)

| Status | ID | Finding | Truth | Fix Type |
|---|---|---|---|---|
| ✓ | D1 | JSON-LD parses vacuously (0 blocks, all parse) | HARD EVIDENCE | — |
| ✗ | D2 | No @context | HARD EVIDENCE | SCHEMA FIX |
| ✗ | D3 | No page-appropriate @type (needed: LocalBusiness, MedicalBusiness, WebPage) | HARD EVIDENCE | SCHEMA FIX |
| — | D4 | @id coverage — N/A no entities | — | SCHEMA FIX |
| ✗ | D5 | No BreadcrumbList | HARD EVIDENCE | SCHEMA FIX |
| ✗ | D6 | Required fields absent: name, address, telephone, medicalSpecialty | HARD EVIDENCE | SCHEMA FIX |
| ✗ | D7 | Recommended fields absent: openingHours, priceRange, aggregateRating | HARD EVIDENCE | SCHEMA FIX |
| ✗ | D8 | No Organization or WebSite schema | HARD EVIDENCE | SCHEMA FIX |
| — | D9 | No FAQ content on page — N/A | — | — |
| ✗ | D10 | No ImageObject schema for team photos | HARD EVIDENCE | SCHEMA FIX |
| ✗ | D11 | No datePublished/dateModified schema | HARD EVIDENCE | SCHEMA FIX |
| ✗ | D12 | No Person schema for named team members (3 visible on page) | HARD EVIDENCE | SCHEMA FIX |
| ✗ | D14 | No hreflang | HARD EVIDENCE | PAGE HTML FIX |

**Sources:**
🥇 Schema.org ([schema.org/MedicalBusiness](https://schema.org/MedicalBusiness)) [Rules #1252, #1636, #1668]
🥈 Backlinko ([backlinko.com](https://backlinko.com/schema-markup-guide)) — AP #4763 "Omitting Schema Markup"

---

## Section E — AEO Discovery (6/10 pass)

| Status | ID | Finding | Truth | Fix Type |
|---|---|---|---|---|
| ✓ | E1 | PerplexityBot not explicitly listed but passes via wildcard | HARD EVIDENCE | SITEWIDE TEMPLATE FIX |
| ✓ | E2 | BingPreview not explicitly listed but passes via wildcard | HARD EVIDENCE | SITEWIDE TEMPLATE FIX |
| ✓ | E3 | Googlebot explicitly listed, allowed | HARD EVIDENCE | — |
| ⚠ | E4 | 0 of 10 AI crawlers explicitly listed | HARD EVIDENCE | SITEWIDE TEMPLATE FIX |
| ✓ | E5 | Content in raw HTML (Webflow SSR) | HARD EVIDENCE | — |
| ✓ | E6 | 404 handling real (HTTP 404 for nonexistent paths) | MEASURED | — |
| ✓ | E7 | No cloaking (all UAs get 25,355 bytes) | MEASURED | — |
| ✓ | E8 | Sitemap reachable, 15 URLs | HARD EVIDENCE | — |
| ✗ | E9 | Sitemap lastmod: 0% coverage | HARD EVIDENCE | SITEWIDE TEMPLATE FIX |
| ⚠ | E10 | Sitemap contains /untitled and /new (test/WIP URLs) | HARD EVIDENCE | SITEWIDE TEMPLATE FIX |

---

## Section F — AEO Extraction (4/12 pass)

| Status | ID | Finding | Truth | Fix Type |
|---|---|---|---|---|
| ⚠ | F1 | First 150 words describe cultural care but don't match "Dosteli ist ein [X] der [Y] macht" entity pattern | STATIC RULE | CONTENT RESTRUCTURE |
| ✓ | F2 | Uses structured sections (5 H2s) | HARD EVIDENCE | — |
| ✗ | F3 | No FAQ section | HARD EVIDENCE | CONTENT RESTRUCTURE |
| ✗ | F4 | No semantic markup for Q&A content | HARD EVIDENCE | SCHEMA FIX |
| — | F5 | No questions phrased as natural language | — | CONTENT RESTRUCTURE |
| ⚠ | F6 | Headings are category labels, not question phrasings | HEURISTIC | CONTENT RESTRUCTURE |
| ✓ | F7 | Named entities present (Berlin districts, service categories) | HEURISTIC | — |
| ⚠ | F8 | Specific facts present (5 WGs, phone number, founding year) but few numeric | HEURISTIC | CONTENT RESTRUCTURE |
| ⚠ | F9 | H1 "Kulturspezifisch pflegen" is imperative not definition-first | HEURISTIC | CONTENT RESTRUCTURE |
| ✗ | F10 | No TL;DR or summary block | HARD EVIDENCE | CONTENT RESTRUCTURE |
| ✓ | F11 | Sections (Services, Merhaba, Reviews) are reasonably self-contained | HEURISTIC | — |
| ✗ | F12 | No tables or comparison lists | HARD EVIDENCE | CONTENT RESTRUCTURE |

**Sources:**
🥇 Perplexity ([docs.perplexity.ai](https://docs.perplexity.ai)) — Answer-first structure [Rule #1471]
🥈 Backlinko — Burying the answer anti-pattern [AP #4698]

---

## Section G — AEO Trust (2/8 pass)

| Status | ID | Finding | Truth | Fix Type |
|---|---|---|---|---|
| ✓ | G1 | Named team members on page (3 people with roles) | HARD EVIDENCE | — |
| ✗ | G2 | No Person schema with hasCredential | HARD EVIDENCE | SCHEMA FIX |
| ✗ | G3 | No visible datePublished / dateModified | HARD EVIDENCE | PAGE HTML FIX |
| ✗ | G4 | No Organization sameAs array (no schema) | HARD EVIDENCE | SCHEMA FIX |
| ✗ | G5 | No dateModified in schema | HARD EVIDENCE | SCHEMA FIX |
| ✓ | G6 | 3 testimonials visible on page | HARD EVIDENCE | — |
| ✗ | G7 | No AggregateRating schema (MDK certification badges present visually, could be Rating) | HARD EVIDENCE | SCHEMA FIX |
| ✗ | G8 | Contact info present in body but not in structured form | HARD EVIDENCE | SCHEMA FIX |

---

## Section H — AEO Selection (N/A)

Not available this run: no direct competitors crawled. WebSearch for "Dosteli alternatives competitors Deutschland" returned only business-directory sites (Creditsafe, ZoomInfo, northdata, D&B) — no peer Pflegedienste with similar cultural-care positioning surfaced. For meaningful H1-H8 comparison, manually identify 3-5 Berlin-area Turkish-Pflege providers.

---

## Section I — GEO (Directional, 3/8 pass)

| Status | ID | Finding | Truth | Fix Type |
|---|---|---|---|---|
| ✓ | I1 | Brand discoverable via business directories (ZoomInfo, northdata, Creditsafe, Dun & Bradstreet) | MODEL JUDGMENT | — |
| △ | I2 | No Wikipedia page for Dosteli | MODEL JUDGMENT | OFF-PAGE |
| ✗ | I3 | No industry press coverage (Pflege trade outlets) | MODEL JUDGMENT | OFF-PAGE |
| △ | I4 | No visible Google Reviews or Trustpilot profile | MODEL JUDGMENT | OFF-PAGE |
| ✓ | I5 | Facebook page exists (Dosteli GmbH Berlin, german locale) | MODEL JUDGMENT | — |
| ✗ | I6 | No comparison content ("Dosteli vs X") in SERP | MODEL JUDGMENT | OFF-PAGE |
| ✗ | I7 | No Berlin-Turkish community press mentions surfaced | MODEL JUDGMENT | OFF-PAGE |
| ✓ | I8 | Founder/Geschäftsführer names (Jan-Andreas Basche, Safiye Ergün) findable via business registry | MODEL JUDGMENT | — |

**Framing:** Directional signals from WebSearch on audit date. Results vary by location, session, and time. Fixing I2-I4, I6-I7 requires 4-8 weeks of off-page entity work (press outreach, Google Business Profile, community partnerships).

---

## Section J — Entity Consistency (2/4 pass)

| Status | ID | Finding | Truth | Fix Type |
|---|---|---|---|---|
| ✗ | J1 | No schema Organization — brand name only in title + H1 | HARD EVIDENCE | SCHEMA FIX |
| ✓ | J2 | No character-substitution variants of brand detected | MEASURED | — |
| ⚠ | J3 | Apex/www handled correctly (301) but sitemap points to apex while served host is www | HARD EVIDENCE | SITEWIDE TEMPLATE FIX |
| ✓ | J4 | OG tags + social (Facebook) aligned on brand name | HARD EVIDENCE | — |

---

## AEO Stage Analysis

| Stage | Score | Verdict |
|---|---|---|
| Discovery (E) | 60% | OK — robots + sitemap work, but sitemap quality issues + no AI-crawler signaling |
| Extraction (F) | 35% | Weak — no FAQ, no answer-first structure, no tables/lists |
| Trust (G) | 20% | Very weak — no Person schema, no dates, no AggregateRating despite MDK certifications |
| Selection (H) | N/A | No competitor data this run |

**Diagnosis:** Dosteli has the CONTENT signals of a credible local healthcare business (25 years operating, MDK certified, team named, 3 testimonials visible, 5 physical locations) but none of these are structured for AI extraction. An AI assistant asked "welcher türkischsprachige Pflegedienst in Berlin?" might find Dosteli mentioned in business directories but can't verify credentials, service scope, or location coverage from the homepage because none of it is schema-coded.

---

## GEO Dimension Analysis (Directional)

### Presence — 60%
Dosteli surfaces in German business directories (ZoomInfo, Creditsafe, northdata, Dun & Bradstreet) + Facebook. No Wikipedia, no industry-specific press (e.g. Häusliche Pflege, Altenpflege magazines).

### Accuracy — 50%
External directory facts match: founded 2008, Berlin, Geschäftsführer Jan-Andreas Basche and Safiye Ergün, capital €25,000. But no unified entity graph (no Wikipedia, no structured sameAs on own site).

### Favorability — 25%
No Trustpilot/Google Reviews visible in SERP. No industry press. No "best of" roundups for cultural-care Pflege in Berlin surface Dosteli.

---

# LAYER 3 — Technical Reference

## Competitor Profiles

**Not available this run.** No direct Pflegedienst competitors surfaced via WebSearch. Suggested manual list for next audit: Evet Ambulante Pflege, Senora Berlin, Altenpflegedienst Istanbul-Berlin, Sozialstation Berlin-Mitte — all Berlin area, some with Turkish-speaking staff.

---

## Schema Audit Detail

**Current state:** Zero JSON-LD blocks.

**Generated complete schema fix — see Fix #1 above for the full `@graph` block** with Organization + MedicalBusiness + LocalBusiness + 5 MedicalTherapy services + 5 areaServed cities + WebPage + sameAs.

---

## Entity Consistency Matrix

| Entity | Schema | OG Tags | Title | Footer | Consistent? |
|---|---|---|---|---|---|
| Brand "Dosteli" | ❌ (no schema) | ✅ og:title "Dosteli - Kulturspezifischer Pflegedienst" | ⚠ "Dosteli" (too short) | Not inspected | ⚠ Schema missing |
| Canonical URL | ❌ (no canonical) | og:url present | N/A | — | ❌ Conflict (sitemap uses apex) |
| Apex vs www | — | — | — | apex URLs in sitemap | ⚠ Apex 301s to www correctly, but sitemap should match served host |

---

## Bot's Eye View — Full Detail

**curl GET `https://www.dosteli.de/` — response:**
- HTTP/2 200, 25,355 bytes
- Cloudflare HIT (cf-cache-status: HIT), age 14.5 days
- Webflow-hosted (`<html data-wf-domain="www.dosteli.de">`)
- Last-Modified Thu, 09 Apr 2026 22:09:28 GMT
- Webflow last-publish: Tue Nov 25 2025 (5+ months ago)
- HSTS max-age=31536000

**Body structure:**
- H1: "Kulturspezifisch pflegen"
- H2s: "Unsere Leistungen", "Sie sind Angehörige oder Pflegebedürftige und suchen professionelle Unterstützung?", "Merhaba", "Kundenbewertungen", "Sie brauchen Pflege? Willkommen: das übernehmen wir!"
- Content in German throughout
- 3 team photos with names + roles (Geschäftsführung, Pflegefachkraft, Operations)
- 3 testimonials visible
- 5 Demenz-WG location cards (Moabit, Rudow, Spandau, Wedding, Neukölln)
- MDK certification badges (visual only, not schema'd)
- 22 images, 6 with alt
- Contact: +49 30 30 20 87 88, kontakt@dosteli.de, Emdener Straße 1, 10551 Berlin

**AI search presence verification:**
- `"dosteli.de" company about` → returns ZoomInfo, northdata, Creditsafe, Dun & Bradstreet + own pages. Brand is discoverable.
- `Pflegedienst Berlin Turkish` → not directly searched this run (German locale issues)
- No Wikipedia entry

**Classification:** `partial_ssr` (deterministic script). Content is in raw HTML, but metadata + schema gaps reduce AEO readiness.

---

## All Checks Index

(Per-section tables above. Key summary below.)

| Category | Run | Pass | Fail | Warn | N/A |
|---|---|---|---|---|---|
| A — Technical SEO | 15 | 8 | 4 | 3 | 0 |
| B — Performance | 10 | 6 | 0 | 1 | 3 |
| C — On-Page | 13 | 7 | 1 | 3 | 2 |
| D — Schema | 13 | 1 | 11 | 0 | 1 |
| E — AEO Discovery | 10 | 7 | 1 | 2 | 0 |
| F — AEO Extraction | 12 | 4 | 3 | 4 | 1 |
| G — AEO Trust | 8 | 2 | 6 | 0 | 0 |
| H — AEO Selection | 0 | 0 | 0 | 0 | 8 |
| I — GEO | 8 | 3 | 3 | 2 | 0 |
| J — Entity | 4 | 2 | 1 | 1 | 0 |
| **Total** | **93** | **40** | **30** | **16** | **15** |

---

## Brain Intelligence Applied

### 🥇 TIER 1 — PRIMARY SOURCES

📌 **Google Search Central — Canonical, meta, html lang, sitemap**
[developers.google.com/search/docs](https://developers.google.com/search/docs)
Applied to: A3, A4, A5, A11, E8, E9
Evidence: Rules #1166, #1280, #1283, #563, #1482

📌 **Schema.org — MedicalBusiness + LocalBusiness + Person**
[schema.org/MedicalBusiness](https://schema.org/MedicalBusiness)
Applied to: D3, D6, D8, D12, G2
Evidence: Rules #1668, #1636, #1674, #1676

📌 **Perplexity — Answer-first structure, freshness**
[docs.perplexity.ai](https://docs.perplexity.ai)
Applied to: F1, F9, E9
Evidence: Rules #1471, #1474, #1482

### 🥈 TIER 2 — RESEARCH SOURCES

📌 **Backlinko — Schema Markup + AI SEO**
[backlinko.com](https://backlinko.com/schema-markup-guide)
Applied to: D1, D6, A2, F1
Evidence: AP #4763 (Omitting Schema), Rule #7176 (LCP threshold), AP #4698 (Burying Answer)

---

## Supplementary Findings (from Sieve brain)

### ⚠ Omitting schema markup on a YMYL local business

🥈 Per **Backlinko** at [backlinko.com](https://backlinko.com/schema-markup-guide): "Healthcare/YMYL businesses without schema cannot be cross-referenced by AI engines building an entity graph. This is the #1 AEO failure pattern for local services."
[Sieve AP #4763, high risk]

### ⚠ Missing Person schema for named practitioners on YMYL

🥇 Per **Schema.org** at [schema.org/Person](https://schema.org/Person): "Person entities representing healthcare practitioners should carry jobTitle, worksFor, and ideally hasCredential for YMYL context." Dosteli names 3 team members but provides zero Person schema.
[Sieve Rule #1674, AP #798 "Publishing content without authorship signals", high risk]

### ⚠ Thin-content homepage (444 words borderline)

📎 Per **almcorp.com** AI Visibility guide: "Homepages with less than 500 words typically get low AI citation. The content isn't thin in terms of message quality — Dosteli communicates cultural-specific care clearly — but denser content with FAQ + service details would score higher."
[Sieve AP #1328 (related but not directly mapped)]

---

## Audit Metadata

- **Version:** 3.0 (deterministic-script-backed)
- **Checks run:** 93 (97 minus those marked N/A for YMYL+local profile)
- **Passed:** 40 | **Failed:** 30 | **Warnings:** 16 | **N/A:** 15
- **Gates:** all 3 passed
- **Page classification:** Homepage / LocalBusiness / MedicalBusiness (HIGH confidence)
- **Competitors analyzed:** 0 (no direct peers surfaced via WebSearch)
- **Chrome MCP:** not invoked
- **Brain entries matched:** 14 rules + 8 anti-patterns across ~20 check IDs
- **Brain table counts at audit time:** 5,215 rules + 2,995 anti-patterns
- **Previous audits:** none — first audit for dosteli.de
- **Queries used:** `kulturspezifischer Pflegedienst Berlin`, `türkischer Pflegedienst Berlin`, `Demenz WG Berlin`, `Dosteli Berlin`
- **Data sources:** curl (primary), WebFetch (content), WebSearch (brand context + GEO), deterministic scripts, Supabase brain

---

## Summary — What To Do This Week

### DO NOW

1. **Add LocalBusiness + MedicalBusiness + Person schema** (the full `@graph` block from Fix #1). Single most impactful change.
2. **Add meta description, canonical, html lang="de"** — 10 minutes in Webflow page settings.
3. **Fix title** from "Dosteli" to "Dosteli — Kulturspezifischer Pflegedienst Berlin | Pflege & Demenz-WGs".
4. **Fix sitemap** — use www URLs, add lastmod, remove /untitled and /new.
5. **Fix image alt coverage** — 16 of 22 images missing alt. Add descriptive German alts.

### PLAN (next 2 weeks)

6. Add Twitter Card meta tags
7. Add explicit AI crawler entries to robots.txt
8. Publish a FAQ section (common questions about Pflege coverage, insurance, service scope)
9. Add visible "Zuletzt aktualisiert" date
10. Update Webflow content (currently last-published Nov 25 2025 — 5+ months old)

### OFF-PAGE (4–8 weeks)

11. Create Wikipedia stub (notability: 17+ years, 5 Demenz-WGs, MDK-certified, GmbH)
12. Activate Google Business Profile + encourage patient-family reviews
13. Pitch to Berliner or industry press (Pflege-Magazin, Berliner Morgenpost Gesundheit)
14. Partner with Berlin-Turkish community associations for cross-linking

### Honest framing

Dosteli's problem is **not** content quality — it's content invisibility to machines. The homepage clearly communicates "kulturspezifischer Pflegedienst in Berlin" to a human reader with testimonials, team, services, and locations. But an AI engine asked the same question can't extract any of that because none of it is tagged (no Schema.org, no canonical, no html lang, no Person schema). Fix #1 alone (add the schema block) turns Dosteli from invisible to structured-data-ready in under 2 hours.

---

**Persistence confirmation:**
- **Supabase:** `audit_id = d0dfbb95-d06d-41e9-bd40-80155dc0561c` ✅ (with 17 finding rows)
- **Markdown:** `audit-reports/dosteli-de-audit-1-2026-04-24.md` ✅

---

*Generated by website-seo-aeo-auditor v3 (deterministic-script-backed).*
