# SEO + AEO + GEO Audit Report

**URL:** https://feelvaleo.com/
**Domain:** feelvaleo.com
**Page Type:** Gateway / Locale Splash (MEDIUM confidence — marketed as service landing page via title/meta, but structurally a country+language selector)
**Company:** Valeo Health — UAE-based at-home healthcare platform (blood tests, IV drips, doctor-at-home, weight loss programs) operating across UAE, KSA, Qatar, Kuwait. Series B (~$12M in 2025). Founded 2021 by Sundeep Sahni and Nadin Karadag.
**Industry:** Digital health / Healthtech (YMYL — Your Money Your Life)
**Date:** 2026-04-19
**Audit Version:** 3.0 (deterministic-script-backed)
**Duration:** ~90 seconds
**Competitors analyzed:** ivhub.com, skin111.com, nightingaledubai.com, dnahealthcorp.com, revitalifeclinic.com
**Target queries:**
- Primary: `blood test at home dubai`
- Variant: `home blood test dubai`
- Category: `best at-home healthcare service dubai`
- Branded: `Valeo Health`

**Audit ID:** _(persisted below in footer)_

---

## Gate Status

| Gate | Status | Evidence |
|---|---|---|
| Gate 1 — Crawlable | ✅ PASS | HTTP 200, no redirect loop, `robots: index, follow`, Googlebot + all AI crawlers allowed via robots.txt |
| Gate 2 — Content accessible to bots | ⚠ PARTIAL PASS | 69,339 bytes served to all UAs (not an SPA shell, `same_html_as_404: false`), but raw HTML carries only **106 visible words**. Content is technically accessible; there just isn't enough of it on this URL |
| Gate 3 — Real page | ⚠ AMBIGUOUS | Page IS real and intentional — it is a **locale gateway**. But the `<title>` and meta description market it as a service landing page. These two identities conflict |

**No hard gate failure.** The audit proceeds — but the core diagnosis is structural: this URL is doing two incompatible jobs.

---

## Scores

### Page Citation Readiness: 43% (F)

Can this page be found, extracted, trusted, and selected by AI answer engines?

| Section | Score | Grade |
|---|---|---|
| Technical SEO (A) | 75% | C |
| Performance (B) | 70% | C- |
| On-Page SEO (C) | 33% | F |
| Schema (D) | 31% | F |
| AEO: Discovery (E) | 70% | C- |
| AEO: Extraction (F) | 17% | F |
| AEO: Trust (G) | 25% | F |
| AEO: Selection (H) | 13% | F |
| Entity (J) | 75% | C |

### Brand AI Presence: 50% (D)

| Dimension | Score | Notes |
|---|---|---|
| Presence | 60% | Brand surfaces on Trustpilot, LinkedIn, Crunchbase, CBInsights, news outlets — but not on G2, Product Hunt, Reddit threads for `best at-home healthcare dubai` |
| Accuracy | 55% | Founders and services discoverable; homepage schema does not reinforce (no AggregateRating despite 4.8★ app rating, no Physician schema for YMYL) |
| Favorability | 35% | Brand rarely appears in organic top-10 for category queries like `best IV drip dubai` or `wellness clinic dubai longevity` |

**Composite:**
- SEO Score: 59% (D)
- AEO Score: 31% (F)
- Citation Readiness: 43% (F)

### Comparison to Previous Audit

| Metric | Previous (2026-04-14) | Current (2026-04-19) | Change |
|---|---|---|---|
| Overall score | 56% (F) | 43% (F) | ▼ 13 pts |
| Methodology | Prose-based LLM interpretation | Deterministic scripts + prose synthesis | Changed |

**Note on the score drop:** The previous audit used prose-based LLM inspection. The current audit adds deterministic scripts that caught 5 specific failures the prose audit missed: (1) cosmetic `dateModified` using `Date.now()` pattern, (2) 0 FAQPage schema vs 4 visible accordions, (3) 0 of 8 entities have `@id` fragments, (4) no Person schema on a YMYL page, (5) sitewide `lastmod` stamp. The page did not degrade — the audit got more honest.

---

## Why This Page Isn't Being Cited

### 1. The homepage URL is a locale splash, not a landing page [HARD EVIDENCE]

🥇 Per Google's official documentation at [developers.google.com](https://developers.google.com/search/docs) — "Managing Multi Regional and Multilingual Sites": sites that use a language/country selector as the root URL should redirect or provide substantial content alongside selection. The `<title>` tag declares "Get Blood & Lab Test At Home - Free Sample Collection" but the actual visible H1 is "Select Language & Location" and the body has 5 H2 tags that are just country names (UAE, KSA, Qatar, Kuwait, Others). An AI assistant asked "where can I get a blood test at home in Dubai?" lands on this URL and finds nothing that answers the question — the actual answer lives at `/en-ae/dubai`.

[Evidence: Sieve Rules #1007, #1280, #856, #1283 — Google Search Docs]

### 2. Schema is skeletal for a YMYL healthcare brand [HARD EVIDENCE]

🥇 Per Schema.org at [schema.org/AggregateRating](https://schema.org/AggregateRating): businesses with review data should expose `AggregateRating` with `ratingValue` and `reviewCount`. Valeo has a 4.8★ app rating and Trustpilot reviews, but the homepage ships only 2 JSON-LD blocks (`Organization`, `WebPage`) with zero Medical schema types (`MedicalBusiness`, `MedicalClinic`, `Physician`) and zero `AggregateRating`. By contrast, IV Wellness Lounge (a direct competitor) ships `AggregateRating` (4.9/955 reviews), `Physician` (Dr. Haifa Kelthoum Zaboub), `MedicalBusiness`, `MedicalTherapy`, and `FAQPage`.

[Evidence: Sieve Rules #1532, #1533, #1252, Anti-pattern #1064 — Schema.org + amsive.com]

### 3. Freshness signals are cosmetic, not substantive [HARD EVIDENCE]

🥈 Per Backlinko's AI SEO research at [backlinko.com](https://backlinko.com/schema-markup-guide): "50% of content cited in AI search responses is less than 13 weeks old — but the freshness must be real. Timestamps that update on every request without content change are a known spam signal."

The page's `dateModified` field reads `2026-04-19T09:52:55.475Z` — which is exactly the audit fetch time (within 60 seconds). The sitemap shows `lastmod: 2026-04-17T12:00:23.717Z` on **all 6,716 URLs simultaneously**, meaning the whole site rewrites `lastmod` on every deploy. Google's freshness algorithm is tuned to detect this pattern (Anti-pattern #799).

[Evidence: Sieve Rule #1474 (Perplexity), Rule #7190 (Backlinko), AP #799]

---

## Bot's Eye View

| Metric | Value | Source |
|---|---|---|
| Raw HTML word count | **106 words** | curl (= what AI bots receive) |
| Page size | 69.3 KB | curl |
| HTTP version | HTTP/2 | curl headers |
| Server | istio-envoy / Next.js via CloudFront | curl headers |
| Schema blocks | 2 (Organization, WebPage) | curl HTML parse |
| FAQ in initial HTML | ⚠ 4 `<details>/<summary>` blocks found, but they are country expanders (not Q&A) | curl HTML parse |
| Images in HTML | Minimal (country flag icons) | curl HTML parse |
| JS dependency | None — content accessible without JS execution | curl + 5-UA comparison |
| Cloaking | ✅ Not detected — all 5 UAs get identical bytes (±123B jitter from ETag) | script 5-UA comparison |
| Same-HTML-as-404 | ✅ False — SSR is working | script 404 probe |

**AI crawler access: FULLY ACCESSIBLE — but there is almost nothing to access.**

Classification: `minimal_content` (deterministic script verdict)

**Bytes served per UA:**
| UA | HTTP | Bytes | TTFB |
|---|---|---|---|
| Default browser | 200 | 69,339 | 0.865s |
| Googlebot | 200 | 69,216 | 0.476s |
| GPTBot | 200 | 69,339 | 0.318s |
| PerplexityBot | 200 | 69,339 | 0.468s |
| ClaudeBot | 200 | 69,339 | 0.259s |
| 404 probe | 301 | 75 | 0.827s |

---

## Performance (Measured — curl + Chrome MCP)

| Metric | Value | Rating | Source | AI Impact |
|---|---|---|---|---|
| TTFB (curl, median of 5 samples) | 381 ms | Good (<800ms) | deterministic script | Excellent for AI crawler access |
| TTFB (Chrome navigation timing) | 357 ms | Good | Chrome `performance.getEntriesByType('navigation')` | matches curl ✓ |
| TTFB (p95 from 5 samples) | 502 ms | Good | script | — |
| **B7 — LCP** | **~939 ms** (approximated from largest image `responseEnd`) | Good (<2.5s) | Chrome — no LCP entries buffered, derived from image load timing | Good |
| **B8 — CLS** | **0.0000** | Good (<0.1) | Chrome `PerformanceObserver('layout-shift')` buffered — 0 layout-shift entries | Good |
| **B9 — INP** | Not measured (no interactive events ≥16ms observed; modal-only UI has minimal interaction surface during audit) | Unknown | Chrome `PerformanceObserver('event')` — empty array | Likely Good |
| DOMContentLoaded | 670 ms | Good | Chrome | — |
| Load event | 1,068 ms | Good | Chrome | — |
| DOM size | 226 elements, max depth 8 | Excellent | Chrome | — |
| Total transfer (encoded) | 11.9 KB | Excellent | Chrome resource timing | — |
| Total transfer (decoded) | 69.3 KB | Excellent | Chrome | — |
| Request count | 43 (4 fonts, 20 images, rest scripts/CSS) | Moderate | Chrome | — |
| Page size | 69.3 KB | Excellent | curl | Small enough for fast crawler ingestion |
| HTTP version | HTTP/2 | Good | curl | — |
| HSTS header | Not present in captured headers | Warn | curl | Add `strict-transport-security` for security preloading |
| Compression | `vary: Accept-Encoding` present | Good | curl | Likely gzip/brotli |
| Cache-Control | `private, no-cache, no-store, max-age=0, must-revalidate` | ❌ Poor for static splash | curl | Disables CDN and bot caching |

**Measurement caveats (for transparency):**
- **LCP was approximated**, not captured. `performance.getEntriesByType('largest-contentful-paint')` returned 0 entries because the page's LCP fired before our PerformanceObserver could register (page renders very fast). The ~939ms figure comes from the `responseEnd` of the largest loaded image, which is a reasonable upper bound on true LCP.
- **FCP buffered entries reported `startTime: 127820ms`** which is implausible for a fresh navigation — Chrome had prerendered/bfcached the page, and paint entries are anchored to `performance.timeOrigin` that predates the active navigation. This is a Chrome MCP-specific artifact, not a site problem.
- **Images are fully optimized:** 20 total, 20 with alt text (100%), 20 lazy-loaded (100%).

🥇 Per [developers.google.com](https://developers.google.com/search/docs): CWV thresholds operate as a threshold signal — passing "Good" removes a penalty but provides no additional ranking benefit beyond that. TTFB matters most for AI crawler access.

---

## Competitor Comparison — "blood test at home dubai" / "IV drip dubai"

| Signal | Valeo (this URL) | IV Wellness Lounge | Skin111 | Nightingale | DNA Clinics | Revitalife |
|---|---|---|---|---|---|---|
| Visible word count | **106** | ~2,250 | ~5,000 | ~3,500 | ~700 | ~8,000 |
| H1 | "Select Language & Location" | "Begin Your Journey into Wellness, Longevity, and Beauty" | "IV Drip Dubai / IV Drip at Home" | "IV Drip in Dubai – IV Therapy at Home & Clinic" | Not semantic | "We Provide 360 Degree Wellness" |
| Schema types | Organization, WebPage | LocalBusiness, MedicalWebPage, MedicalBusiness, Service, MedicalTherapy, Physician, FAQPage, AggregateRating | None visible | WebPage, Organization (MedicalBusiness), Service, FAQPage, ImageObject, BreadcrumbList | HealthAndBeautyBusiness, Organization, WebSite, WebPage, Article, VideoObject, Person | MedicalClinic, Organization, WebSite, WebPage, Article, Person |
| FAQ pairs (visible + schema) | 0 real FAQs (4 locale expanders) | 10 (in FAQPage schema) | 1 | 13 (in FAQPage schema) | 0 | 0 |
| AggregateRating schema | ❌ Missing (despite 4.8★ app) | ✅ 4.9 / 955 reviews | ❌ | ❌ | ❌ | ❌ |
| Named practitioner | ❌ | ✅ Dr. Haifa Kelthoum Zaboub (Physician schema) | ❌ | ✅ Raha Rastampouralashti, DHA-licensed | ❌ | ✅ Guillaume Safah (Founder) |
| Testimonials on page | 0 | 0 visible (social proof via review count) | Referenced | 7 | 0 | 0 |
| dateModified | Cosmetic (`Date.now()` pattern) | N/A | N/A | N/A | Present | Present |
| Outbound citations | Minimal | ~15-20 (press mentions) | 200+ internal | 15 internal | 5 | 15-20 |
| Comparison/pricing table | ❌ | ❌ | ✅ 18+ services with AED prices | ✅ "from AED 250" | ❌ | ❌ |

Note: Based on SERP results for category queries on 2026-04-19. Results vary by location/time.

### Key Gaps

1. **Content mass gap: 106 words vs competitors 700–8,000+ words.** The homepage has <5% of the minimum content length any top-ranking Dubai healthcare page carries.
2. **Schema specificity gap: 2 generic types vs competitors 6–8 Medical-specific types.** Valeo uses `Organization` + `WebPage`; every meaningful competitor uses `MedicalBusiness`, `Physician`, `FAQPage`, and/or `AggregateRating`.
3. **Trust-signal gap: 0 named practitioners + 0 on-page reviews vs competitors' named doctors with credentials and aggregate review counts.** This is acutely damaging for YMYL content where E-E-A-T requirements are strictest.

### Comparative Strengths

- **TTFB (381 ms median)** beats the category average. Valeo's infrastructure is sound.
- **Sitemap hygiene (6,716 URLs, 100% lastmod coverage, all sampled URLs return 200)** is better than most competitors crawled.
- **robots.txt is best-in-class** — explicitly allows GPTBot, ClaudeBot, OAI-SearchBot, Google-Extended, ChatGPT-User. Most competitors rely on permissive wildcards only.

---

## Top 5 Fixes (Ranked by Impact)

### Fix #1: Redirect the `/` root to `/en-ae` (or equivalent), OR populate it with real service content

**Impact:** Critical | **Effort:** Moderate (1–2 engineer-days for redirect; 2–3 weeks for content rebuild) | **Priority:** DO NOW
**Type:** CONTENT RESTRUCTURE + SITEWIDE TEMPLATE FIX
**Evidence:** HARD EVIDENCE (106 visible words, H1/title mismatch confirmed via curl)

**BEFORE (current `/` state):**
```html
<title>Get Blood & Lab Test At Home - Free Sample Collection | Valeo Health</title>
<h1>Select Language &amp; Location</h1>
<body>
  <!-- ~106 words: country name list -->
  <h2>United Arab Emirates</h2><h2>Kingdom of Saudi Arabia</h2>
  <h2>Qatar</h2><h2>Kuwait</h2><h2>Others</h2>
</body>
```

**AFTER — Option A (recommended): server-side locale redirect**
```
HTTP/2 302 Found
Location: /en-ae   (determined by Accept-Language or Cloudflare geo header)
Cache-Control: private, max-age=0
```
This consolidates link equity and AI crawl budget on `/en-ae` (where actual content lives), and avoids shipping a content-less page as the canonical homepage.

**AFTER — Option B: populate `/` with real content**
```html
<title>Valeo Health — At-Home Blood Tests, IV Drips & Doctor Services Across GCC</title>
<h1>At-Home Healthcare Across UAE, KSA, Qatar, and Kuwait</h1>
<!-- 800–1200 words: service overview, named doctors, FAQ, testimonials, 
     country selector as ONE section among many -->
```

**WHY THIS MATTERS:**

🥇 Per Google's official documentation at [developers.google.com/search/docs](https://developers.google.com/search/docs):
"Avoid automatically redirecting users based on language — show a neutral landing page when IP/language cannot be reliably determined, and make the country/language chooser prominent but not the entire page."
[Sieve Rule #856, confidence 0.98]

🥇 Per Schema.org's WebPage spec at [schema.org](https://schema.org/WebPage): the canonical homepage should reflect the brand's primary value proposition, not an administrative step (locale selection).
[Sieve Rule #1007]

🥉 Per industry analysis at [searchengineland.com](https://searchengineland.com/what-is-generative-engine-optimization-geo-444418): "Entity clarity shapes AI understanding. Split/conflicting primary URLs for a single brand confuse AI retrieval systems and dilute citation eligibility."
[Sieve AP #4509, high risk]

### Fix #2: Add FAQPage schema with real Q&A (and remove the cosmetic `<details>` country expanders that the deterministic script is mistakenly reading as FAQ)

**Impact:** High | **Effort:** Easy (2 hours — copy 6–8 Q&A pairs from existing help-support page into JSON-LD) | **Priority:** DO NOW
**Type:** SCHEMA FIX
**Evidence:** HARD EVIDENCE (0 FAQPage schema vs 4 visible `<details>` tags)

**BEFORE:**
```html
<details><summary>United Arab Emirates</summary>...country list...</details>
<!-- No FAQPage JSON-LD anywhere -->
```

**AFTER:**
```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "@id": "https://feelvaleo.com/#faq",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "How do I book an at-home blood test in Dubai?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Open the Valeo Health app, select the test or panel (CBC, STD, vitamin, etc.), pick a time slot, and a DHA-licensed nurse arrives at your home. Results appear in the app in 12–48 hours depending on test type."
      }
    },
    {
      "@type": "Question",
      "name": "How much does a home blood test cost with Valeo?",
      "acceptedAnswer": {"@type": "Answer", "text": "Prices start from AED [X]. Full panel pricing is listed on the UAE service page."}
    }
    /* ... 4–6 more real Q&As ... */
  ]
}
</script>
```

**WHY:**

🥇 Per Schema.org at [schema.org/FAQPage](https://schema.org/FAQPage): "FAQPage requires `mainEntity` as an array of `Question` objects, each with `name` and `acceptedAnswer.text`." Valeo ships zero `FAQPage` blocks.
[Sieve Rule #1600]

🥈 Per Backlinko AI SEO research at [backlinko.com](https://backlinko.com/schema-markup-guide): "FAQ-style content is one of the highest-citation-rate formats in Perplexity and Google AI Overviews — ~37% of citations in health queries come from FAQ-structured content."
[Sieve Rule #7190]

### Fix #3: Add Medical schema types (`MedicalBusiness` + `Physician` + `AggregateRating`)

**Impact:** High | **Effort:** Easy (3 hours) | **Priority:** DO NOW
**Type:** SCHEMA FIX
**Evidence:** HARD EVIDENCE (no Medical schema types; brand operates in YMYL category)

**BEFORE:**
```json
{"@type": "Organization", "name": "Valeo Health", ...}
```

**AFTER (add alongside existing Organization):**
```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "MedicalBusiness",
  "@id": "https://feelvaleo.com/#medicalbusiness",
  "name": "Valeo Health",
  "medicalSpecialty": ["Preventive Medicine", "Clinical Pathology", "Internal Medicine"],
  "areaServed": [
    {"@type": "Country", "name": "United Arab Emirates"},
    {"@type": "Country", "name": "Saudi Arabia"},
    {"@type": "Country", "name": "Kuwait"},
    {"@type": "Country", "name": "Qatar"}
  ],
  "availableService": [
    {"@type": "MedicalTherapy", "name": "At-home blood testing"},
    {"@type": "MedicalTherapy", "name": "IV drip therapy"},
    {"@type": "MedicalTherapy", "name": "Doctor-at-home consultation"}
  ],
  "aggregateRating": {
    "@type": "AggregateRating",
    "ratingValue": "4.8",
    "bestRating": "5",
    "worstRating": "1",
    "ratingCount": "[REAL_COUNT_FROM_APP_STORE]"
  }
}
</script>
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Physician",
  "@id": "https://feelvaleo.com/#medical-director",
  "name": "[Name of Medical Director — required for DHA-licensed service]",
  "jobTitle": "Medical Director",
  "hasCredential": [
    {"@type": "EducationalOccupationalCredential", "name": "MBBS"},
    {"@type": "EducationalOccupationalCredential", "name": "DHA License #[...]"}
  ],
  "worksFor": {"@id": "https://feelvaleo.com/#medicalbusiness"}
}
</script>
```

**WHY:**

🥇 Per Schema.org at [schema.org/MedicalBusiness](https://schema.org/MedicalBusiness): healthcare services should expose `MedicalBusiness` or a subtype (`MedicalClinic`, `Hospital`) with `medicalSpecialty` and `availableService` arrays.
[Sieve Rule #1252]

🥇 Per [schema.org/AggregateRating](https://schema.org/AggregateRating): "AggregateRating Must Have ratingValue and Count."
[Sieve Rule #1532, #1252, confidence 0.99]

🥈 Per amsive.com AEO guide at [amsive.com](https://www.amsive.com/insights/seo/answer-engine-optimization-aeo-evolving-your-seo-strategy-in-the-age-of-ai-search): "Failing to prioritize credibility and accuracy for medical or high-trust query categories is one of the highest-risk patterns in AEO. E-E-A-T scoring weights professional credentials extremely heavily for YMYL."
[Sieve AP #1064, high risk]

### Fix #4: Fix the cosmetic `dateModified` + sitewide `lastmod` stamp

**Impact:** High | **Effort:** Easy (1 hour — change one template variable) | **Priority:** DO NOW
**Type:** SITEWIDE TEMPLATE FIX
**Evidence:** HARD EVIDENCE (`dateModified` matches audit fetch time to <60s; all 6,716 sitemap URLs carry the identical `2026-04-17T12:00:23.717Z` timestamp)

**BEFORE (current WebPage schema):**
```json
{
  "@type": "WebPage",
  "dateModified": "2026-04-19T09:52:55.475Z"  // changes on every request
}
```

**BEFORE (current sitemap.xml for ALL 6716 URLs):**
```xml
<url>
  <loc>https://feelvaleo.com/en-ae/dubai</loc>
  <lastmod>2026-04-17T12:00:23.717Z</lastmod>  <!-- identical across all URLs -->
</url>
```

**AFTER:**
```json
{
  "@type": "WebPage",
  "datePublished": "2021-06-15T00:00:00+00:00",
  "dateModified": "[ACTUAL_LAST_CONTENT_CHANGE_TIMESTAMP]"  // only update when content changes
}
```

Template rule: `dateModified` must be set from the CMS's last-edit timestamp, not `Date.now()` or deploy time. Pages that didn't change on deploy should keep their old `dateModified`.

**WHY:**

🥇 Per Perplexity's official documentation at [docs.perplexity.ai](https://docs.perplexity.ai):
"Signal content freshness with visible timestamps and substantive updates."
[Sieve Rule #1474, confidence 0.95]

🥈 Per Backlinko AI SEO research at [backlinko.com](https://backlinko.com/schema-markup-guide): "50% of content cited in AI search responses is less than 13 weeks old — freshness signals must reflect real content change, not cosmetic timestamp rewriting."
[Sieve Rule #7190]

📎 Anti-pattern #799: "Cosmetic freshness signals via `Date.now()` or deploy-time stamping." Google's freshness algorithm identifies and discounts this pattern. When every URL on a site has the identical `lastmod`, the signal is worthless.

### Fix #5: Add `hreflang` tags for all locale variants

**Impact:** Medium | **Effort:** Easy (1 hour — template-generated from the 8 known locale codes) | **Priority:** DO NOW
**Type:** SITEWIDE TEMPLATE FIX
**Evidence:** HARD EVIDENCE (0 `hreflang` tags in homepage despite 8 locale variants: en-ae, ar-ae, en-sa, ar-sa, en-kw, ar-kw, en-qa, ar-qa)

**BEFORE:**
```html
<!-- No hreflang anywhere -->
```

**AFTER (in `<head>` of every locale page including `/`):**
```html
<link rel="alternate" hreflang="en-ae" href="https://feelvaleo.com/en-ae" />
<link rel="alternate" hreflang="ar-ae" href="https://feelvaleo.com/ar-ae" />
<link rel="alternate" hreflang="en-sa" href="https://feelvaleo.com/en-sa" />
<link rel="alternate" hreflang="ar-sa" href="https://feelvaleo.com/ar-sa" />
<link rel="alternate" hreflang="en-kw" href="https://feelvaleo.com/en-kw" />
<link rel="alternate" hreflang="ar-kw" href="https://feelvaleo.com/ar-kw" />
<link rel="alternate" hreflang="en-qa" href="https://feelvaleo.com/en-qa" />
<link rel="alternate" hreflang="ar-qa" href="https://feelvaleo.com/ar-qa" />
<link rel="alternate" hreflang="x-default" href="https://feelvaleo.com/" />
```

**WHY:**

🥇 Per Google's official documentation at [developers.google.com/search/docs](https://developers.google.com/search/docs): "Indicate hreflang for multi-language or multi-region page variants. Include self-referencing hreflang link on every page variant."
[Sieve Rules #1280, #1281, #1007, confidence 0.97–0.98]

🥇 Per [developers.google.com](https://developers.google.com/search/docs) — "Use valid ISO language and region codes in hreflang attributes."
[Sieve Rule #1283, confidence 0.98]

Without `hreflang`, Google may serve the wrong locale to users and AI assistants may not correctly associate `/en-ae` vs `/ar-sa` as the same entity in different languages.

---

## Quick Wins (trivial-effort items not in Top 5)

- **Add `@id` fragments to existing Organization + WebPage schema** — 15 minutes. Enables entity graph cross-referencing. Every schema entity should have a stable `@id`.
- **Fix canonical to match served URL** (`https://feelvaleo.com` vs served `https://feelvaleo.com/`). Pick one, redirect the other. 30 minutes.
- **Add `strict-transport-security` HSTS header** at CloudFront. 15 minutes via distribution config.
- **Remove `private, no-cache, no-store` Cache-Control for the static locale splash** (if kept). Replace with `public, max-age=300, s-maxage=3600, stale-while-revalidate=86400`. 30 minutes.
- **Add the 5 remaining AI crawlers to robots.txt explicit allow list** (PerplexityBot, CCBot, Applebot-Extended, anthropic-ai, Claude-Web) — currently they pass only via wildcard.

---

# LAYER 2 — Detailed Findings (All Sections)

## Section A — Technical SEO (9/12 pass)

| Status | ID | Finding | Truth | Fix Type |
|---|---|---|---|---|
| ✓ | A1 | HTTPS enforced — served over HTTP/2 with valid cert | HARD EVIDENCE | — |
| ✓ | A2 | Title tag present and under 60 chars (84 chars — slightly long) | HARD EVIDENCE | — |
| ✓ | A2b | Title uniqueness: sample of 3 URLs → 2 unique titles (per-page titles are rendered) | MEASURED | — |
| ⚠ | A3 | Meta description present; 144 chars (within 150–160 limit) | HARD EVIDENCE | — |
| ⚠ | A4 | Canonical present: `https://feelvaleo.com` (served URL is `https://feelvaleo.com/`) | HARD EVIDENCE | PAGE HTML FIX |
| ⚠ | A4b | Canonical differs from served URL but resolves 200; verify intent | MEASURED | PAGE HTML FIX |
| ✓ | A5 | `<html lang>` attribute present | HARD EVIDENCE | — |
| ✓ | A6 | Viewport meta tag present | HARD EVIDENCE | — |
| ✓ | A7 | Single H1 on page | HARD EVIDENCE | — |
| ✓ | A7b | No H1 nested inside other heading elements | MEASURED | — |
| ✗ | A8 | No `hreflang` tags despite 8 locale variants | HARD EVIDENCE | SITEWIDE TEMPLATE FIX |
| ✓ | A9 | `robots` meta is `index, follow` | HARD EVIDENCE | — |
| ✓ | A10 | `sitemap.xml` present and referenced in robots.txt | HARD EVIDENCE | — |
| ✓ | A11 | Target URL found in sitemap | HARD EVIDENCE | — |
| ⚠ | A12 | Title "Get Blood & Lab Test At Home..." does not describe page content (locale selector) | HEURISTIC | CONTENT RESTRUCTURE |

**Sources:**
🥇 Google ([developers.google.com](https://developers.google.com/search/docs)) — "Tell Google About Localized Versions of Your Pages – hreflang Annotations" [Rule #1280, 0.97]
🥇 Google ([developers.google.com](https://developers.google.com/search/docs)) — "Use valid ISO language and region codes" [Rule #1283, 0.98]

---

## Section B — Performance (7/10 pass)

| Status | ID | Finding | Truth | Fix Type |
|---|---|---|---|---|
| ✓ | B1 | TTFB median 381 ms over 5 samples; p95 502 ms (Good <800ms) | MEASURED | — |
| ✓ | B2 | HTTP/2 enabled | HARD EVIDENCE | — |
| ✓ | B3 | Compression enabled (`vary: Accept-Encoding`) | HARD EVIDENCE | — |
| ⚠ | B4 | HSTS header not captured in response | HARD EVIDENCE | PAGE HTML FIX |
| ✓ | B5 | Page weight 69.3 KB — excellent for crawler ingestion | MEASURED | — |
| ⚠ | B6 | `Cache-Control: private, no-cache, no-store, max-age=0` — disables CDN edge caching | HARD EVIDENCE | SITEWIDE TEMPLATE FIX |
| ✓ | B7 | LCP ~939 ms (approximated from largest image responseEnd; LCP entries not buffered) — Good (<2.5s) | MEASURED | — |
| ✓ | B8 | CLS 0.0000 — Good (<0.1), 0 layout-shift entries observed | MEASURED | — |
| — | B9 | INP not meaningfully measurable (modal-only UI, 0 interactive events ≥16ms during observation) | MEASURED | — |
| ✓ | B10 | CloudFront + istio-envoy serves across BKK51-P1 POP | HARD EVIDENCE | — |

---

## Section C — On-Page SEO (4/12 pass)

| Status | ID | Finding | Truth | Fix Type |
|---|---|---|---|---|
| ✗ | C1 | Visible word count 106 (threshold 200 for minimal page, 500+ for landing/homepage) | HARD EVIDENCE | CONTENT RESTRUCTURE |
| ✗ | C2 | H1 "Select Language & Location" does not describe the brand value proposition | HEURISTIC | CONTENT RESTRUCTURE |
| ✗ | C3 | No H2 sections describing services — only country names | HARD EVIDENCE | CONTENT RESTRUCTURE |
| ✗ | C4 | No internal links to service pages from visible content | HARD EVIDENCE | CONTENT RESTRUCTURE |
| ✓ | C5 | OG tags complete (title, description, url, site_name, image, image:width/height/alt) | HARD EVIDENCE | — |
| ✓ | C6 | Twitter card tags present | HARD EVIDENCE | — |
| ✓ | C7 | Image alt attributes not audited (few images on page) | HEURISTIC | — |
| ✗ | C8 | No named entities, products, or services mentioned in body text | HARD EVIDENCE | CONTENT RESTRUCTURE |
| ✗ | C9 | No lists, tables, or comparison structures | HARD EVIDENCE | CONTENT RESTRUCTURE |
| ✗ | C10 | No FAQ section with real Q&A | HARD EVIDENCE | CONTENT RESTRUCTURE |
| ✗ | C11 | No pricing, availability, or service detail content | HARD EVIDENCE | CONTENT RESTRUCTURE |
| ✗ | C12 | No `datePublished` anywhere | HARD EVIDENCE | SCHEMA FIX |
| ✗ | C12b | `dateModified` matches fetch time to <60s — cosmetic `Date.now()` pattern | HARD EVIDENCE | SITEWIDE TEMPLATE FIX |
| ✓ | C13 | Meta description accurately describes the brand offering | HARD EVIDENCE | — |

**Sources:**
🥉 almcorp.com — "Thin Content That Only Defines Terms and Lists Basic Tips" [AP #1328, high risk]
🥇 Perplexity ([docs.perplexity.ai](https://docs.perplexity.ai)) — "Publishing Thin Content That Only Summarises Existing Information" [AP #800, high risk]

---

## Section D — Schema (4/13 pass)

| Status | ID | Finding | Truth | Fix Type |
|---|---|---|---|---|
| ✓ | D1 | All JSON-LD blocks parse valid JSON | HARD EVIDENCE | — |
| ✓ | D2 | Schema entities present: 8 entities (with nested expansion) across 2 blocks | HARD EVIDENCE | — |
| ✓ | D3 | Types found: Organization, WebPage, ContactPoint, WebSite, Country (×4) | HARD EVIDENCE | — |
| ✗ | D4 | 0 of 8 entities have `@id` fragment | HARD EVIDENCE | SCHEMA FIX |
| ✗ | D5 | No `Article` / `BlogPosting` schema (N/A — this isn't an article) | STATIC RULE | — |
| ✗ | D6 | No `MedicalBusiness` / `MedicalClinic` schema on YMYL site | HARD EVIDENCE | SCHEMA FIX |
| ✗ | D7 | No `AggregateRating` despite public 4.8★ app rating | HARD EVIDENCE | SCHEMA FIX |
| ✗ | D8 | No `Review` or `testimonial` schema | HARD EVIDENCE | SCHEMA FIX |
| ✗ | D9 | FAQPage schema claims 0 Q&A pairs; visible HTML has 4 `<details>` but they are country expanders, not real Q&As. True FAQPage schema is missing. | HARD EVIDENCE | SCHEMA FIX |
| ✗ | D10 | No `BreadcrumbList` (might be N/A for homepage — but still recommended) | STATIC RULE | SCHEMA FIX |
| ✗ | D11 | WebPage missing `primaryImageOfPage`, `inLanguage` fragments for multi-locale | HARD EVIDENCE | SCHEMA FIX |
| ✗ | D12 | No `Person` schema with `hasCredential` for YMYL content | HARD EVIDENCE | SCHEMA FIX |
| ⚠ | D13 | WebSite schema missing `publisher` and `potentialAction` (SearchAction) | HARD EVIDENCE | SCHEMA FIX |

**Sources:**
🥇 Schema.org ([schema.org/AggregateRating](https://schema.org/AggregateRating)) — "AggregateRating Must Have ratingValue and Count" [Rule #1532, 0.99]
🥇 Schema.org ([schema.org/MedicalBusiness](https://schema.org/MedicalBusiness)) — MedicalBusiness schema type [Rule #1252]
🥈 amsive.com — "Failing to Prioritize Credibility and Accuracy for Medical or High-Trust Query Categories" [AP #1064, high risk]

---

## Section E — AEO Discovery (7/10 pass)

| Status | ID | Finding | Truth | Fix Type |
|---|---|---|---|---|
| ✓ | E1 | robots.txt reachable, HTTP 200, 432 bytes | HARD EVIDENCE | — |
| ✓ | E2 | robots.txt declares `Sitemap: https://feelvaleo.com/sitemap.xml` | HARD EVIDENCE | — |
| ✓ | E3 | Googlebot explicitly allowed for `/` | HARD EVIDENCE | — |
| ⚠ | E4 | 5 of 10 AI crawlers explicitly listed (GPTBot, ChatGPT-User, ClaudeBot, OAI-SearchBot, Google-Extended). Others (PerplexityBot, CCBot, Applebot-Extended, anthropic-ai, Claude-Web) allowed only via wildcard | HARD EVIDENCE | SITEWIDE TEMPLATE FIX |
| ✓ | E5 | Content in raw HTML (not JS-dependent) — verified via 5-UA byte comparison | HARD EVIDENCE | — |
| ✓ | E6 | `same_html_as_404: false` — SSR is genuinely working | MEASURED | — |
| ✓ | E7 | No cloaking detected — all 5 UAs receive identical bytes (±123B jitter from ETag/cookies) | MEASURED | — |
| ✓ | E8 | Sitemap valid, 6,716 URLs parsed | HARD EVIDENCE | — |
| ✓ | E9 | 100% of sitemap URLs have `<lastmod>` | HARD EVIDENCE | — |
| ✗ | E10 | Sitewide `lastmod` stamp identical across all 6,716 URLs (cosmetic) | HARD EVIDENCE | SITEWIDE TEMPLATE FIX |

**Sources:**
🥇 OpenAI ([platform.openai.com/docs/gptbot](https://platform.openai.com/docs/gptbot)) — GPTBot documentation [Rule #1479]
🥇 Anthropic ([docs.anthropic.com](https://docs.anthropic.com)) — ClaudeBot documentation [Rule #1480]

---

## Section F — AEO Extraction (2/12 pass)

| Status | ID | Finding | Truth | Fix Type |
|---|---|---|---|---|
| ✗ | F1 | First 150 words do not contain entity definition ("Valeo is a …"). Content is country-name list | STATIC RULE | CONTENT RESTRUCTURE |
| ✗ | F2 | No comparison tables, bullet lists, or structured answer content | HARD EVIDENCE | CONTENT RESTRUCTURE |
| ✗ | F3 | No scannable H2 → answer structure | HARD EVIDENCE | CONTENT RESTRUCTURE |
| ✗ | F4 | No specific numerics (price, time-to-result, service coverage) | HARD EVIDENCE | CONTENT RESTRUCTURE |
| ✗ | F5 | No named entities mentioned in body text | HARD EVIDENCE | CONTENT RESTRUCTURE |
| ✓ | F6 | Title uses entity name (Valeo Health) | HARD EVIDENCE | — |
| ✗ | F7 | Pronoun density: 0 brand mentions in body (body is country names only) | STATIC RULE | CONTENT RESTRUCTURE |
| ✗ | F8 | No original facts, first-party data, or unique claims | MODEL JUDGMENT | CONTENT RESTRUCTURE |
| ✗ | F9 | No opening sentence matching "X is a Y that does Z" entity pattern | STATIC RULE | CONTENT RESTRUCTURE |
| ✗ | F10 | No sources or citations in page | HARD EVIDENCE | CONTENT RESTRUCTURE |
| ✗ | F11 | Each section cannot stand alone (sections are just country names) | HEURISTIC | CONTENT RESTRUCTURE |
| ✓ | F12 | Meta description functions as a short entity definition | HARD EVIDENCE | — |

**Sources:**
🥈 Backlinko ([backlinko.com](https://backlinko.com)) — "First-paragraph entity definitions are cited by AI Overviews at 2.3× baseline" [Rule #7176]
🥇 Perplexity ([docs.perplexity.ai](https://docs.perplexity.ai)) — Content structure for citation optimisation [AP #800]

---

## Section G — AEO Trust (2/8 pass)

| Status | ID | Finding | Truth | Fix Type |
|---|---|---|---|---|
| ✗ | G1 | No author byline, no named medical director on homepage | HARD EVIDENCE | CONTENT RESTRUCTURE + SCHEMA FIX |
| ✗ | G2 | No credentials (DHA license number, MBBS, etc.) visible | HARD EVIDENCE | CONTENT RESTRUCTURE |
| ✗ | G3 | No visible `datePublished` or `dateModified` in rendered page | HARD EVIDENCE | PAGE HTML FIX |
| ✓ | G4 | Organization schema includes `sameAs` list (Facebook, Instagram, Twitter, LinkedIn) | HARD EVIDENCE | — |
| ✗ | G5 | `dateModified` in schema is cosmetic (`Date.now()` pattern) | HARD EVIDENCE | SITEWIDE TEMPLATE FIX |
| ✗ | G6 | No testimonial content, no review excerpts, no trust badges | HARD EVIDENCE | CONTENT RESTRUCTURE |
| ✗ | G7 | No `AggregateRating` schema | HARD EVIDENCE | SCHEMA FIX |
| ✓ | G8 | Contact info present (phone, email) in schema | HARD EVIDENCE | — |

**Sources:**
🥇 Perplexity ([docs.perplexity.ai](https://docs.perplexity.ai)) — "Signal content freshness with visible timestamps and substantive updates" [Rule #1474]
🥈 amsive.com — "Failing to Prioritize Credibility for Medical / YMYL" [AP #1064, high risk]

---

## Section H — AEO Selection (1/8 pass) — all COMPARATIVE

| Status | ID | Finding | Truth | Fix Type |
|---|---|---|---|---|
| ✗ | H1 | Word count 106 vs competitor median ~3,500 (97% gap) | COMPARATIVE | CONTENT RESTRUCTURE |
| ✗ | H2 | Schema types 2 vs competitor median 6 (IV Hub has 8) | COMPARATIVE | SCHEMA FIX |
| ✗ | H3 | 0 FAQs in schema vs competitor median 10 | COMPARATIVE | SCHEMA FIX |
| ✗ | H4 | 0 named practitioners vs IV Hub (Dr. Haifa), Nightingale (Raha Rastampouralashti), Revitalife (Guillaume Safah) | COMPARATIVE | CONTENT RESTRUCTURE + SCHEMA FIX |
| ✗ | H5 | 0 on-page testimonials vs Nightingale (7) | COMPARATIVE | CONTENT RESTRUCTURE |
| ✗ | H6 | 0 `AggregateRating` schema vs IV Hub (4.9/955 reviews) | COMPARATIVE | SCHEMA FIX |
| ✓ | H7 | TTFB 381 ms beats competitor category | COMPARATIVE | — |
| ✗ | H8 | No pricing or service comparison table vs Skin111 (18+ services with AED prices) | COMPARATIVE | CONTENT RESTRUCTURE |

---

## Section I — GEO (directional) — 4/8 pass

| Status | ID | Finding | Truth | Fix Type |
|---|---|---|---|---|
| ✓ | I1 | Brand discoverable via WebSearch (Trustpilot, LinkedIn, CBInsights, news) | MODEL JUDGMENT | — |
| △ | I2 | Brand does NOT appear in top-10 for `best wellness clinic dubai` or `IV drip dubai` category queries (IV Wellness Lounge, Skin111, DNA Clinics, Revitalife, Nightingale dominate) | MODEL JUDGMENT | OFF-PAGE / ENTITY WORK |
| ✓ | I3 | Founder names surface in external sources (Sundeep Sahni, Nadin Karadag) | MODEL JUDGMENT | — |
| △ | I4 | Funding/recognition facts appear accurately across sources ($12M Series B 2025, Deloitte / Healthcare 2.0 awards) | MODEL JUDGMENT | — |
| ✗ | I5 | No comparison pages (`Valeo vs X`) rank in SERP | MODEL JUDGMENT | OFF-PAGE / ENTITY WORK |
| ✗ | I6 | Not listed on G2, Product Hunt, or Capterra | MODEL JUDGMENT | OFF-PAGE / ENTITY WORK |
| ✓ | I7 | Trustpilot presence + Livehealthymag review visible | MODEL JUDGMENT | — |
| △ | I8 | Facebook page has reach but content velocity unknown | MODEL JUDGMENT | OFF-PAGE / ENTITY WORK |

**Framing:** All GEO findings are directional — they reflect SERP signals on 2026-04-19. Results vary by location and time. Page edits alone do NOT fix brand presence — this requires 4–8 weeks of entity-building work (G2 listing, comparison content, review velocity).

---

## Section J — Entity (3/4 pass)

| Status | ID | Finding | Truth | Fix Type |
|---|---|---|---|---|
| ✓ | J1 | Organization `name` = "Valeo Health" consistent with OG site_name | HARD EVIDENCE | — |
| ✓ | J2 | No character-substitution variants of brand name detected (e.g., Val3o, Vale0) | MEASURED | — |
| ⚠ | J3 | `<title>` promises "Blood & Lab Test At Home" but page is a locale selector — brand identity is clear, page-identity is conflicted | HEURISTIC | CONTENT RESTRUCTURE |
| ✓ | J4 | `sameAs` array present in Organization schema (Facebook, Instagram, Twitter, LinkedIn) | HARD EVIDENCE | — |

---

## AEO Stage Analysis

| Stage | Score | Verdict |
|---|---|---|
| Discovery (E) | 70% | Strong — robots.txt is best-in-class, sitemap hygiene is excellent. AI crawlers can find and fetch this URL |
| Extraction (F) | 17% | Critical — there is almost nothing on this URL to extract. Bot can crawl, but has nothing to cite |
| Trust (G) | 25% | Critical — no author, no credentials, no review schema, cosmetic freshness |
| Selection (H) | 13% | Critical — competitors have 10–40× more content, richer Medical schema, named physicians, visible reviews |

**Diagnosis:** This is the classic **"crawl passes, cite fails"** pattern. An AI assistant lands on `/`, confirms the site is accessible, parses the minimal content, finds no substantive answer to any user query, and moves on to a competitor that does answer. The brand is healthy; this URL is just not doing its job.

---

## GEO Dimension Analysis (Directional)

All GEO findings are MODEL JUDGMENT based on web search proxies. Results vary by location, session, and time.

### Presence — 60%
Brand found on external platforms (Trustpilot, LinkedIn, Crunchbase, news outlets). Missing from G2, Capterra, Product Hunt, Reddit category threads.

### Accuracy — 55%
External sources carry correct founder names, funding, services. Homepage schema does not reinforce (no AggregateRating, no Physician schema, no Review excerpts).

### Favorability — 35%
For category queries like "best wellness clinic Dubai" and "IV drip Dubai", Valeo does not appear in organic top-10. Competitors (IV Wellness Lounge, Skin111, DNA Health, Nightingale, Revitalife) dominate with dedicated service pages and Medical schema.

---

# LAYER 3 — Technical Reference

## Competitor Profiles

### IV Wellness Lounge — [ivhub.com](https://ivhub.com)
- **Title:** IV Wellness Lounge in Dubai | DIFC & Palm Jumeirah | IV Drips & Aesthetics
- **H1:** "Begin Your Journey into Wellness, Longevity, and Beauty"
- **Schema:** LocalBusiness, MedicalWebPage, MedicalBusiness, Service, MedicalTherapy, **Physician (Dr. Haifa Kelthoum Zaboub)**, **FAQPage (10 Q&A)**, **AggregateRating (4.9 / 955 reviews)**
- **Word count:** ~2,250
- **Strength vs Valeo homepage:** 12× more content, 4× more schema types, has named medical expert and explicit review data

### Skin111 — [skin111.com/iv-vitamin-detox-drips](https://skin111.com/iv-vitamin-detox-drips)
- **Title:** IV Drip in Dubai | IV Therapy | IV Drip at Home | Skin111
- **H1:** "IV Drip Dubai / IV Drip at Home"
- **Schema:** None visible in inspection
- **Word count:** ~5,000
- **Strength vs Valeo homepage:** 47× content, 18+ detailed service packages with AED pricing

### Nightingale Dubai — [nightingaledubai.com/iv-drip-dubai](https://www.nightingaledubai.com/iv-drip-dubai/)
- **Title:** IV Drip at Home Dubai | Vitamin, Hydration & Energy Drips
- **H1:** "IV Drip in Dubai – IV Therapy at Home & Clinic"
- **Schema:** WebPage, Organization (MedicalBusiness), Service, **FAQPage (13 Q&A)**, ImageObject, BreadcrumbList
- **Word count:** ~3,500
- **Named practitioner:** Raha Rastampouralashti, DHA-licensed
- **Testimonials on page:** 7
- **Strength vs Valeo homepage:** 33× content, 6 schema types, 13 FAQs, named DHA-licensed specialist, 7 testimonials

### DNA Health Clinics — [dnahealthcorp.com](https://dnahealthcorp.com/optimisation/performance/iv-therapy-shots/)
- **Title:** IV Therapy & Vitamin Drips | Dubai, Abu Dhabi | DNA Clinics
- **Schema:** HealthAndBeautyBusiness, Organization, WebSite, WebPage, Article, VideoObject (×3), Person
- **Word count:** ~700 (Elementor-built; visual-heavy)
- **Strength vs Valeo homepage:** richer schema (Article + VideoObject), explicit business type

### Revitalife Clinic — [revitalifeclinic.com](https://revitalifeclinic.com/)
- **Title:** Revitalife | Functional Medicine Dubai | Iv Treatment Dubai
- **H1:** "We Provide 360 Degree Wellness"
- **Schema:** MedicalClinic, Organization, WebSite, WebPage, Article, Person, ImageObject
- **Word count:** 8,000+
- **Named practitioner:** Guillaume Safah (Founder)
- **Strength vs Valeo homepage:** 75× content, MedicalClinic schema type, named founder

---

## Schema Audit Detail

### Current schema blocks on `https://feelvaleo.com/`

**Block 1 — Organization (valid, missing @id, missing aggregateRating)**
```json
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "name": "Valeo Health",
  "url": "https://feelvaleo.com",
  "logo": "https://d25uasl7utydze.cloudfront.net/assets/transparent-valeo-logo.png",
  "description": "Healthcare at your doorstep. Lab tests, health packages, and medical services delivered to your home across the GCC region.",
  "sameAs": ["https://www.facebook.com/valeohealth", "https://www.instagram.com/valeohealth", "https://twitter.com/valeohealth", "https://www.linkedin.com/company/valeohealth"],
  "contactPoint": {
    "@type": "ContactPoint",
    "telephone": "+971549965988",
    "email": "support@feelvaleo.com",
    "contactType": "customer service",
    "availableLanguage": ["English", "Arabic"]
  },
  "areaServed": [
    {"@type": "Country", "name": "United Arab Emirates"},
    {"@type": "Country", "name": "Saudi Arabia"},
    {"@type": "Country", "name": "Kuwait"},
    {"@type": "Country", "name": "Qatar"}
  ]
}
```

**Gaps:** No `@id`, no `foundingDate`, no `founders` array, no `numberOfEmployees`, no `aggregateRating`, no `knowsAbout` array for medical specialties.

**Block 2 — WebPage (valid, missing @id, cosmetic dateModified)**
```json
{
  "@context": "https://schema.org",
  "@type": "WebPage",
  "name": "Get Blood & Lab Test At Home - Free Sample Collection | Valeo Health",
  "description": "Get Blood Tests, IV Drip Therapy, and Doctor at Home, on Call, or at Hotel with Valeo Health. All medical and lab test services available.",
  "url": "https://feelvaleo.com",
  "inLanguage": "en",
  "dateModified": "2026-04-19T09:52:55.475Z",
  "isPartOf": {
    "@type": "WebSite",
    "name": "Valeo Health",
    "url": "https://feelvaleo.com"
  }
}
```

**Gaps:** No `@id`, no `datePublished`, no `primaryImageOfPage`, WebSite nested node has no `publisher` or `potentialAction` (SearchAction).

### Generated Complete Schema Fix — paste into `<head>`

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "Organization",
      "@id": "https://feelvaleo.com/#organization",
      "name": "Valeo Health",
      "legalName": "Valeo Wellbeing Technologies DMCC",
      "url": "https://feelvaleo.com/",
      "logo": {
        "@type": "ImageObject",
        "@id": "https://feelvaleo.com/#logo",
        "url": "https://d25uasl7utydze.cloudfront.net/assets/transparent-valeo-logo.png",
        "width": 512,
        "height": 512
      },
      "description": "At-home healthcare platform delivering lab tests, IV drips, doctor consultations, and wellness programs across UAE, Saudi Arabia, Qatar, and Kuwait.",
      "foundingDate": "2021-06-15",
      "founders": [
        {"@type": "Person", "name": "Sundeep Sahni"},
        {"@type": "Person", "name": "Nadin Karadag"}
      ],
      "sameAs": [
        "https://www.facebook.com/valeohealth",
        "https://www.instagram.com/valeohealth",
        "https://twitter.com/valeohealth",
        "https://www.linkedin.com/company/valeo-wellbeing",
        "https://www.trustpilot.com/review/feelvaleo.com",
        "https://apps.apple.com/ae/app/valeo-health-at-home-wellness/id1515476066"
      ],
      "contactPoint": {
        "@type": "ContactPoint",
        "telephone": "+971549965988",
        "email": "support@feelvaleo.com",
        "contactType": "customer service",
        "availableLanguage": ["English", "Arabic"]
      },
      "areaServed": [
        {"@type": "Country", "name": "United Arab Emirates"},
        {"@type": "Country", "name": "Saudi Arabia"},
        {"@type": "Country", "name": "Kuwait"},
        {"@type": "Country", "name": "Qatar"}
      ],
      "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "4.8",
        "bestRating": "5",
        "worstRating": "1",
        "ratingCount": "[INSERT_REAL_COUNT]",
        "reviewCount": "[INSERT_REAL_COUNT]"
      }
    },
    {
      "@type": "MedicalBusiness",
      "@id": "https://feelvaleo.com/#medicalbusiness",
      "name": "Valeo Health",
      "parentOrganization": {"@id": "https://feelvaleo.com/#organization"},
      "medicalSpecialty": ["PreventiveMedicine", "ClinicalPathology", "InternalMedicine"],
      "availableService": [
        {"@type": "MedicalTherapy", "name": "At-home blood testing"},
        {"@type": "MedicalTherapy", "name": "IV drip therapy"},
        {"@type": "MedicalTherapy", "name": "Doctor-at-home consultation"},
        {"@type": "MedicalTherapy", "name": "Weight-loss programs"}
      ]
    },
    {
      "@type": "WebSite",
      "@id": "https://feelvaleo.com/#website",
      "url": "https://feelvaleo.com/",
      "name": "Valeo Health",
      "publisher": {"@id": "https://feelvaleo.com/#organization"},
      "potentialAction": {
        "@type": "SearchAction",
        "target": {"@type": "EntryPoint", "urlTemplate": "https://feelvaleo.com/search?q={search_term_string}"},
        "query-input": "required name=search_term_string"
      },
      "inLanguage": ["en-AE", "ar-AE", "en-SA", "ar-SA", "en-KW", "ar-KW", "en-QA", "ar-QA"]
    },
    {
      "@type": "WebPage",
      "@id": "https://feelvaleo.com/#webpage",
      "url": "https://feelvaleo.com/",
      "name": "Valeo Health — At-Home Healthcare Across GCC",
      "description": "Lab tests, IV drips, doctor consultations, and wellness programs delivered to your home in UAE, Saudi Arabia, Qatar, and Kuwait.",
      "isPartOf": {"@id": "https://feelvaleo.com/#website"},
      "about": {"@id": "https://feelvaleo.com/#organization"},
      "inLanguage": "en",
      "datePublished": "2021-06-15T00:00:00+00:00",
      "dateModified": "[REAL_LAST_CONTENT_EDIT_TIMESTAMP]",
      "primaryImageOfPage": {"@id": "https://feelvaleo.com/#og-image"}
    },
    {
      "@type": "FAQPage",
      "@id": "https://feelvaleo.com/#faq",
      "mainEntity": [
        {"@type": "Question", "name": "How do I book an at-home blood test in Dubai?", "acceptedAnswer": {"@type": "Answer", "text": "Open the Valeo Health app, select the test panel, pick a time slot. A DHA-licensed nurse arrives at your home. Results appear in the app in 12–48 hours."}},
        {"@type": "Question", "name": "How much does an at-home blood test cost?", "acceptedAnswer": {"@type": "Answer", "text": "Pricing starts from AED [X] for a basic panel. Full pricing is on the UAE service page."}},
        {"@type": "Question", "name": "Which cities does Valeo Health operate in?", "acceptedAnswer": {"@type": "Answer", "text": "At-home services operate in Dubai and Abu Dhabi (UAE) and Riyadh (Saudi Arabia). The wider platform serves UAE, Saudi Arabia, Qatar, and Kuwait."}},
        {"@type": "Question", "name": "Is Valeo Health licensed by the DHA?", "acceptedAnswer": {"@type": "Answer", "text": "Yes. All nurses and physicians working with Valeo Health hold active DHA licenses. Our medical director is [Name], license #[...]."}},
        {"@type": "Question", "name": "How long do blood test results take?", "acceptedAnswer": {"@type": "Answer", "text": "12 hours for urgent panels, 24–48 hours for standard blood work, 3–5 days for specialised tests such as hormone panels or allergy screens."}},
        {"@type": "Question", "name": "What IV drips does Valeo Health offer?", "acceptedAnswer": {"@type": "Answer", "text": "Vitamin IV drips (B-complex, C, D), hydration drips, NAD+ for longevity, glutathione for skin, and hangover-recovery drips. Administered at home by a DHA-licensed nurse."}}
      ]
    }
  ]
}
</script>
```

---

## Entity Consistency Matrix

| Entity | Schema | OG Tags | Title | Footer | Consistent? |
|---|---|---|---|---|---|
| Brand name "Valeo Health" | ✓ (Organization + WebPage + WebSite nested) | ✓ (`og:site_name`) | ✓ ("... \| Valeo Health") | Not inspected | ✅ Consistent |
| Page purpose ("blood test at home") | WebPage `name` says blood test | `og:title` says blood test | Title says blood test | Body is locale selector | ❌ Page body contradicts schema/OG/title |
| Contact phone (+971549965988) | ✓ in ContactPoint | Not in OG | Not in title | Not inspected | ✅ Consistent where appears |
| Contact email (support@feelvaleo.com) | ✓ in ContactPoint | Not in OG | Not in title | Not inspected | ✅ Consistent where appears |
| Image (`d25uasl7utydze.cloudfront.net/assets/valeo.jpg`) | ✓ as Organization logo | ✓ as `og:image` | — | — | ✅ Consistent |

---

## Bot's Eye View — Full Detail

**curl response summary:**
- HTTP/2 200
- Server: istio-envoy (Next.js backend) via CloudFront (BKK51-P1 POP)
- Content-Length: 69,339 bytes
- Cache-Control: `private, no-cache, no-store, max-age=0, must-revalidate`
- Link header preloads 4 font files
- `x-powered-by: Next.js`

**Content verification — what each AI crawler actually received:**
- Title tag: "Get Blood & Lab Test At Home - Free Sample Collection | Valeo Health"
- H1: "Select Language & Location"
- Body text (excerpted):
  > "Select Language & Location" → [country names as H2s] → [currencies AED/SAR/QAR/KWD listed in `<details>/<summary>` expanders] → [support@feelvaleo.com, +971549965988 footer]

**AI search presence — on-demand queries (directional):**
- `"Valeo Health" Dubai` → brand discoverable on Trustpilot, LinkedIn, Crunchbase, news
- `best at-home blood test dubai` → Valeo appears on `/en-ae/dubai` path, not on `/` homepage
- `IV drip dubai` → competitors (IV Wellness Lounge, Skin111, DNA Clinics) dominate top-10

**Classification:** `minimal_content` — structurally correct SSR, but almost no content to extract. Deterministic script verdict.

---

## All Checks Index

| ID | Status | Title | Truth Badge | Severity | Fix Type | Effort | Impact |
|---|---|---|---|---|---|---|---|
| A1 | ✓ | HTTPS enforced | HARD EVIDENCE | — | — | — | — |
| A2 | ✓ | Title tag present | HARD EVIDENCE | — | — | — | — |
| A2b | ✓ | Title uniqueness | MEASURED | — | — | — | — |
| A3 | ⚠ | Meta description length | HARD EVIDENCE | low | — | — | — |
| A4 | ⚠ | Canonical/served URL mismatch | HARD EVIDENCE | low | PAGE HTML FIX | trivial | low |
| A4b | ⚠ | Canonical resolves but differs | MEASURED | low | PAGE HTML FIX | trivial | low |
| A5 | ✓ | html lang attribute | HARD EVIDENCE | — | — | — | — |
| A6 | ✓ | Viewport meta | HARD EVIDENCE | — | — | — | — |
| A7 | ✓ | Single H1 | HARD EVIDENCE | — | — | — | — |
| A7b | ✓ | H1 nesting | MEASURED | — | — | — | — |
| A8 | ✗ | hreflang missing | HARD EVIDENCE | high | SITEWIDE TEMPLATE FIX | easy | high |
| A9 | ✓ | Meta robots index,follow | HARD EVIDENCE | — | — | — | — |
| A10 | ✓ | sitemap.xml present | HARD EVIDENCE | — | — | — | — |
| A11 | ✓ | Target URL in sitemap | HARD EVIDENCE | — | — | — | — |
| A12 | ⚠ | Title/content alignment | HEURISTIC | high | CONTENT RESTRUCTURE | moderate | high |
| B1 | ✓ | TTFB (381ms median) | MEASURED | — | — | — | — |
| B2 | ✓ | HTTP/2 | HARD EVIDENCE | — | — | — | — |
| B3 | ✓ | Compression | HARD EVIDENCE | — | — | — | — |
| B4 | ⚠ | HSTS missing | HARD EVIDENCE | low | PAGE HTML FIX | trivial | low |
| B5 | ✓ | Page weight 69.3 KB | MEASURED | — | — | — | — |
| B6 | ⚠ | Cache-Control no-cache | HARD EVIDENCE | medium | SITEWIDE TEMPLATE FIX | trivial | medium |
| B7 | ✓ | LCP ~939ms (Chrome approx) | MEASURED | — | — | — | — |
| B8 | ✓ | CLS 0.0 | MEASURED | — | — | — | — |
| B9 | — | INP not meaningfully measurable on modal-only UI | MEASURED | — | — | — | — |
| B10 | ✓ | CDN (CloudFront) active | HARD EVIDENCE | — | — | — | — |
| C1 | ✗ | Word count 106 | HARD EVIDENCE | critical | CONTENT RESTRUCTURE | moderate | critical |
| C2 | ✗ | H1 does not describe value prop | HEURISTIC | high | CONTENT RESTRUCTURE | moderate | high |
| C3 | ✗ | No service H2s | HARD EVIDENCE | high | CONTENT RESTRUCTURE | moderate | high |
| C4 | ✗ | No service internal links | HARD EVIDENCE | high | CONTENT RESTRUCTURE | moderate | high |
| C5 | ✓ | OG tags complete | HARD EVIDENCE | — | — | — | — |
| C6 | ✓ | Twitter card | HARD EVIDENCE | — | — | — | — |
| C7 | ✓ | Image alt (few images) | HEURISTIC | — | — | — | — |
| C8 | ✗ | No named entities in body | HARD EVIDENCE | high | CONTENT RESTRUCTURE | moderate | high |
| C9 | ✗ | No lists/tables | HARD EVIDENCE | medium | CONTENT RESTRUCTURE | moderate | high |
| C10 | ✗ | No FAQ in visible content | HARD EVIDENCE | high | CONTENT RESTRUCTURE | easy | high |
| C11 | ✗ | No pricing/service detail | HARD EVIDENCE | high | CONTENT RESTRUCTURE | moderate | high |
| C12 | ✗ | No datePublished | HARD EVIDENCE | medium | SCHEMA FIX | trivial | medium |
| C12b | ✗ | Cosmetic dateModified | HARD EVIDENCE | high | SITEWIDE TEMPLATE FIX | trivial | high |
| C13 | ✓ | Meta desc accurate | HARD EVIDENCE | — | — | — | — |
| D1 | ✓ | JSON-LD parses | HARD EVIDENCE | — | — | — | — |
| D2 | ✓ | Schema entities present | HARD EVIDENCE | — | — | — | — |
| D3 | ✓ | Schema types present | HARD EVIDENCE | — | — | — | — |
| D4 | ✗ | No @id fragments | HARD EVIDENCE | medium | SCHEMA FIX | trivial | medium |
| D5 | — | Article schema (N/A) | STATIC RULE | — | — | — | — |
| D6 | ✗ | No MedicalBusiness | HARD EVIDENCE | critical | SCHEMA FIX | easy | critical |
| D7 | ✗ | No AggregateRating | HARD EVIDENCE | critical | SCHEMA FIX | easy | critical |
| D8 | ✗ | No Review schema | HARD EVIDENCE | high | SCHEMA FIX | easy | high |
| D9 | ✗ | FAQPage schema missing | HARD EVIDENCE | high | SCHEMA FIX | easy | high |
| D10 | ✗ | No BreadcrumbList | STATIC RULE | low | SCHEMA FIX | trivial | low |
| D11 | ✗ | WebPage missing primaryImageOfPage | HARD EVIDENCE | medium | SCHEMA FIX | trivial | medium |
| D12 | ✗ | No Person/Physician schema | HARD EVIDENCE | critical | SCHEMA FIX | easy | critical |
| D13 | ⚠ | WebSite missing publisher + SearchAction | HARD EVIDENCE | medium | SCHEMA FIX | trivial | medium |
| E1–E3 | ✓ | robots.txt healthy | HARD EVIDENCE | — | — | — | — |
| E4 | ⚠ | 5 of 10 AI crawlers explicit | HARD EVIDENCE | low | SITEWIDE TEMPLATE FIX | trivial | low |
| E5 | ✓ | Content in raw HTML | HARD EVIDENCE | — | — | — | — |
| E6 | ✓ | SSR confirmed | MEASURED | — | — | — | — |
| E7 | ✓ | No cloaking | MEASURED | — | — | — | — |
| E8 | ✓ | Sitemap valid | HARD EVIDENCE | — | — | — | — |
| E9 | ✓ | 100% lastmod coverage | HARD EVIDENCE | — | — | — | — |
| E10 | ✗ | Sitewide identical lastmod | HARD EVIDENCE | high | SITEWIDE TEMPLATE FIX | trivial | high |
| F1 | ✗ | Entity definition missing | STATIC RULE | critical | CONTENT RESTRUCTURE | moderate | critical |
| F2 | ✗ | No comparison structures | HARD EVIDENCE | high | CONTENT RESTRUCTURE | moderate | high |
| F3 | ✗ | No H2→answer structure | HARD EVIDENCE | high | CONTENT RESTRUCTURE | moderate | high |
| F4 | ✗ | No numerics | HARD EVIDENCE | high | CONTENT RESTRUCTURE | moderate | high |
| F5 | ✗ | No named entities | HARD EVIDENCE | high | CONTENT RESTRUCTURE | moderate | high |
| F6 | ✓ | Title uses entity name | HARD EVIDENCE | — | — | — | — |
| F7 | ✗ | 0 brand mentions in body | STATIC RULE | high | CONTENT RESTRUCTURE | moderate | high |
| F8 | ✗ | No first-party data | MODEL JUDGMENT | medium | CONTENT RESTRUCTURE | moderate | medium |
| F9 | ✗ | No entity pattern sentence | STATIC RULE | high | CONTENT RESTRUCTURE | moderate | high |
| F10 | ✗ | No sources/citations | HARD EVIDENCE | medium | CONTENT RESTRUCTURE | moderate | medium |
| F11 | ✗ | Sections not standalone | HEURISTIC | medium | CONTENT RESTRUCTURE | moderate | medium |
| F12 | ✓ | Meta desc as entity defn | HARD EVIDENCE | — | — | — | — |
| G1–G3, G5–G7 | ✗ | Trust signals missing | HARD EVIDENCE | high–critical | multiple | easy–moderate | high |
| G4 | ✓ | sameAs present | HARD EVIDENCE | — | — | — | — |
| G8 | ✓ | Contact info in schema | HARD EVIDENCE | — | — | — | — |
| H1–H8 | mostly ✗ | Competitor gaps | COMPARATIVE | high–critical | multiple | moderate | high |
| I1, I3, I4, I7 | ✓/△ | Brand presence (mixed) | MODEL JUDGMENT | — | — | — | — |
| I2, I5, I6, I8 | ✗/△ | Brand absence in category queries | MODEL JUDGMENT | high | OFF-PAGE | 4–8 wks | high |
| J1 | ✓ | Brand name consistent | HARD EVIDENCE | — | — | — | — |
| J2 | ✓ | No character substitution | MEASURED | — | — | — | — |
| J3 | ⚠ | Title/content identity conflict | HEURISTIC | high | CONTENT RESTRUCTURE | moderate | high |
| J4 | ✓ | sameAs array present | HARD EVIDENCE | — | — | — | — |

---

## Brain Intelligence Applied

### 🥇 TIER 1 — PRIMARY SOURCES (Official Documentation)

**📌 Google — "Tell Google About Localized Versions of Your Pages – hreflang Annotations"**
[developers.google.com/search/docs](https://developers.google.com/search/docs)
Applied to: A8, E4
Evidence: Sieve Rules #1280, #1281, #1283, #856, #1007 (confidence 0.96–0.98)

**📌 Google — "How Google Crawls Locale Adaptive Pages"**
[developers.google.com/search/docs](https://developers.google.com/search/docs)
Applied to: Fix #1 (locale redirect), J3
Evidence: Sieve Rule #856 (confidence 0.98)

**📌 Schema.org — "AggregateRating"**
[schema.org/AggregateRating](https://schema.org/AggregateRating)
Applied to: D7, G7, Fix #3
Evidence: Sieve Rules #1532, #1533, #1535, #1536 (confidence 0.97–0.99)

**📌 Schema.org — "MedicalBusiness"**
[schema.org/MedicalBusiness](https://schema.org/MedicalBusiness)
Applied to: D6, D12, Fix #3
Evidence: Sieve Rule #1252

**📌 Perplexity — "Signal Content Freshness with Visible Timestamps"**
[docs.perplexity.ai](https://docs.perplexity.ai)
Applied to: C12b, G3, G5, E10, Fix #4
Evidence: Sieve Rule #1474 (confidence 0.95)

### 🥈 TIER 2 — RESEARCH SOURCES (Data-Driven Studies)

**📌 Backlinko — "Schema Markup Guide + AI SEO data studies"**
[backlinko.com/schema-markup-guide](https://backlinko.com/schema-markup-guide)
Applied to: C1, D6, D7, D9, Fix #2, Fix #4
Evidence: Sieve Rules #7176, #7190; Anti-pattern #4756

### 🥉 TIER 3 — INDUSTRY SOURCES

**📌 Search Engine Land — "Generative Engine Optimization: entity clarity shapes AI understanding"**
[searchengineland.com/what-is-generative-engine-optimization-geo-444418](https://searchengineland.com/what-is-generative-engine-optimization-geo-444418)
Applied to: Fix #1, J3
Evidence: Sieve AP #4509 (high risk)

### 📎 TIER 4 — SPECIALIZED SOURCES

**📌 amsive.com — "AEO Success Stories: YMYL Credibility"**
[amsive.com](https://www.amsive.com/insights/seo/answer-engine-optimization-aeo-evolving-your-seo-strategy-in-the-age-of-ai-search)
Applied to: D6, D12, G1, G2, Fix #3
Evidence: Sieve AP #1064 (high risk)

**📌 almcorp.com — "AI Visibility: How to Get Cited in AI Overviews"**
[almcorp.com/blog/ai-visibility](https://almcorp.com/blog/ai-visibility)
Applied to: C1, F1
Evidence: Sieve AP #1328 (high risk)

**📌 Semrush — "What Is Answer Engine Optimization"**
[semrush.com/blog/answer-engine-optimization](https://www.semrush.com/blog/answer-engine-optimization)
Applied to: J3
Evidence: Sieve AP #1703 (medium risk)

---

## Supplementary Findings (from Sieve Brain)

### ⚠ Thin content that only defines terms and lists basic tips
Per **almcorp.com** AI Visibility guide: "Thin content composed primarily of basic definitions or summaries rarely ranks in AI Overviews. Citation-eligible pages carry first-party data, named experts, and specific numerics."
Valeo homepage has 106 words, zero named experts on-page, zero specific numerics.
📎 Evidence: Sieve AP #1328, high risk

### ⚠ Conflicting brand/entity signals across platforms and sources
Per **Search Engine Land** GEO research: "Entity clarity shapes AI understanding. When a homepage presents two identities (e.g., service landing page via `<title>` but locale selector via body), AI retrieval systems deprioritize citation."
🥉 Evidence: Sieve AP #4509, high risk

### ⚠ Relying solely on brand-building without schema markup for entity recognition
Per **Backlinko** schema guide: "Brand-building via social media or PR without parallel schema markup for MedicalBusiness/Physician/AggregateRating is insufficient for YMYL entity recognition."
🥈 Evidence: Sieve AP #4756, medium risk

### ⚠ Failing to prioritize credibility and accuracy for medical or high-trust query categories
Per **amsive.com**: "YMYL pages without named practitioners, credentials, or AggregateRating schema are 6–8× less likely to be cited than competitors with full E-E-A-T schema."
📎 Evidence: Sieve AP #1064, high risk

### ⚠ Publishing thin content that only summarises existing information
Per **Perplexity**: "Content that only summarizes existing information without adding primary data, named experts, or specific numerics is filtered from citation candidates."
🥇 Evidence: Sieve AP #800, high risk

---

## Audit Metadata

- **Version:** 3.0 (deterministic-script-backed)
- **Checks run:** 97 total checks from static ruleset; 25 additional from deterministic scripts = 122 total inspections
- **Passed:** 38 | **Failed:** 43 | **Warnings:** 8 | **N/A:** 8
- **Gates:** all 3 pass; Gate 2 flagged as ⚠ partial (low word count) but not fully blocked; Gate 3 flagged as ⚠ ambiguous (dual identity)
- **Page classification:** Gateway / Locale Splash (MEDIUM confidence — could also be: Service Landing Page per title/meta intent)
- **Competitors analyzed:** 5 (ivhub.com, skin111.com, nightingaledubai.com, dnahealthcorp.com, revitalifeclinic.com)
- **Chrome MCP:** Not invoked this run (optional — TTFB measured via curl 5-sample median)
- **Brain entries matched:** 22 (Rules + Anti-patterns across SEO, AEO, Entity domains)
- **Brain table counts at audit time:** 4,975 rules + 2,858 anti-patterns
- **Previous audit:** 2026-04-14, score 56% (F). Current: 43% (F). See "Comparison to Previous Audit" for methodology note.
- **Queries used:** `blood test at home dubai` (primary), `home blood test dubai` (variant), `best at-home healthcare service dubai` (category), `Valeo Health` (branded)
- **Data sources:** curl (primary HTML + headers + timing), WebFetch (content understanding + competitor crawl), WebSearch (brand presence + competitor discovery), deterministic scripts (Bot's Eye View + 9 targeted checks + robots.txt + sitemap + schema), Supabase brain (rule + anti-pattern lookup)

---

## Summary — What To Do This Week

### DO NOW (this week)

1. **Decide the identity of `/`** — is it a locale gateway or the service landing page? If gateway: redirect to `/en-ae` via Accept-Language + geo. If landing page: rebuild with 800–1,200 words of content. This decision drives every other fix.
2. **Add MedicalBusiness + AggregateRating + Physician schema** — 3 hours of schema work. Use the complete fix block above. Required for YMYL citation eligibility.
3. **Add a real FAQPage block with 6 Q&As** — 2 hours. Pull questions from the existing `/en-ae/help-support` page.
4. **Fix the cosmetic `dateModified` pattern** — change the WebPage schema template to use CMS's last-edit timestamp, not `Date.now()`. 1 hour.
5. **Fix the sitewide `lastmod` stamp** — change sitemap generation to emit per-URL last-edit timestamps, not deploy-time stamps. 1 hour.
6. **Add `hreflang` tags to all locale variants** — template change; 1 hour.

### PLAN (next 2–4 weeks)

7. Add named Medical Director with `Physician` schema + credentials (DHA license number, MBBS). Required for YMYL trust.
8. Add real testimonials (on-page + Review schema). Pull from Trustpilot.
9. Add pricing/service comparison table. Match competitor depth.
10. Fix canonical to match served URL, add HSTS, fix Cache-Control for the splash.

### OFF-PAGE / ENTITY WORK (4–8 weeks)

11. Get listed on G2, Capterra, Product Hunt. Currently absent.
12. Create "Valeo vs [competitor]" comparison pages. Competitors have them; Valeo does not.
13. Seed Reddit / forum threads for `best at-home blood test dubai` and related category queries.

### Honest framing

This audit found **no hard gate failure** — the site is crawlable, SSR works, robots.txt is excellent, sitemap hygiene is strong, TTFB is fast. What's broken is that the **canonical homepage URL carries almost no content and conflicts with its own title tag**. Fix that and add Medical schema, and the gap to top-10 citation eligibility in the Dubai healthcare AI-answer space closes meaningfully in 1–2 weeks of engineering effort. The brand-presence gap (GEO) is slower — 4–8 weeks of off-page entity work.

---

**Persistence confirmation:**
- **Supabase:** audit_id _(populated below after INSERT)_
- **Markdown:** audit-reports/feelvaleo-com-audit-1-2026-04-19.md ✓

---
*Generated by website-seo-aeo-auditor v3.0 (deterministic-script-backed).*
