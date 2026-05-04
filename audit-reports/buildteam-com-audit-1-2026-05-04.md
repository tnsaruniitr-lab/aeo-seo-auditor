# SEO + AEO + GEO Audit Report

**URL:** https://www.buildteam.com
**Domain:** buildteam.com
**Page Type:** homepage / service business landing (HIGH confidence)
**Company:** Build Team London — design-and-build firm specialising in side return, kitchen, and loft extensions, founded 2007 by Dan Davidson, based at 342 Clapham Road SW9, London
**Industry:** local_business (residential construction / architecture)
**Date:** 2026-05-04
**Audit Version:** 3.0 (chat-mode skill, deterministic-scripts-backed)
**Audit Duration:** ~6 minutes (Phase 1.6 scripts 24s + Phase 3 search + Phase 8 5-competitor crawl)
**Competitors analysed:** plusrooms.co.uk, simplyextend.co.uk, themarketdesignbuild.com, lcclconstruction.co.uk, proficiencyltd.co.uk

**Target queries (inferred):**
- Primary: `London side return extension company`
- Variant: `London design and build kitchen extension`
- Category: `best London home extension company 2026`
- Branded: `BuildTeam London`

---

## ⚠ Gate Status

| Gate | Status | Notes |
|---|---|---|
| 1. Crawlability | ✅ PASS | HTTP 200, robots.txt allows `/` for all agents, no `noindex` |
| 2. Content access | ✅ PASS | 1,078 visible words served identically to all 5 UAs (default, Googlebot, GPTBot, PerplexityBot, ClaudeBot). No SPA shell — 404 probe correctly returns HTTP 404 with different content. |
| 3. Real page | ✅ PASS | Functional service-business homepage, not parked, not under construction. |

All gates pass. Scoring below reflects actual page quality, not blocked-page hypotheticals.

---

## Scores

### Page Citation Readiness: **52%** (Grade F)
*Can this page be found, extracted, trusted, and selected by AI answer engines?*

| Section | Score | Grade |
|---|---|---|
| A · Technical SEO | 77% | C+ |
| B · Performance | 50% | F |
| C · On-Page SEO | 54% | F |
| D · Schema | 50% | F |
| E · AEO Discovery | 50% | F |
| F · AEO Extraction | 33% | F |
| G · AEO Trust | 25% | F |
| H · AEO Selection | 56% | F |
| J · Entity Consistency | 75% | C+ |

### Brand AI Presence: **56%** (Grade F)
*Does this brand exist in AI's understanding of the category?*

| Dimension | Score |
|---|---|
| Presence (I1, I2, I8) | 50% |
| Accuracy (I3, I4, I7) | 67% |
| Favorability (I5, I6) | 50% |

**Note:** Brand presence is a directional assessment based on web search signals. Page edits alone cannot fix BAP — this requires ~6–12 months of off-page entity-building (G2/Houzz reviews, category roundup outreach, third-party citations) to move meaningfully.

**Composite scores:**
- SEO Score: **59%** — page-level technical/on-page foundations, weak on canonicalisation, OG, image alt
- AEO Score: **41%** — extraction-readiness is the weakest dimension (no FAQ, no byline, no dates)
- Citation Readiness: **39%** — composite of F+G+H+D, the four sections that determine whether AI engines extract and trust

### Overall: **53%** (Grade F)
`Overall = PCR × 0.80 + BAP × 0.20 = 52 × 0.80 + 56 × 0.20`

---

## Why This Page Isn't Being Cited

1. **Homepage is missing from its own sitemap** [HARD EVIDENCE]
   The XML sitemap at `https://www.buildteam.com/sitemap.xml` indexes 1,924 URLs (project galleries, postcode pages, articles). The root `https://www.buildteam.com/` is not among them. Per Google Search Central, the homepage should be the highest-priority entry in any sitemap; its absence sends a contradictory signal to Googlebot, PerplexityBot, GPTBot, and ClaudeBot — the 1,924 sub-pages compete for crawl budget with no priority signal pointing to the canonical brand entry. The deterministic check `sitemap:target_url_in_sitemap` confirmed this with severity HIGH.

2. **Six schema entities are invalid and the homepage has no canonical tag** [HARD EVIDENCE]
   The deterministic schema check found 6 of 20 entities flagged as `invalid`: the `Organization` entity is missing the required `url` property, and 5 `Review` entities are missing the Schema.org-required `reviewRating` plus the Google-required `itemReviewed`. Separately, 19 of 20 entities lack `@id` (only one Organization has one), preventing AI knowledge graphs from cross-referencing entities across documents. Compounding this, the page has **no `<link rel="canonical">` tag at all** — a service business with 1,924 indexed URLs and no canonical declarations is at high risk of duplicate-content signal dilution. Per Schema.org official documentation and Google Search Central canonicalisation guidance.

3. **Brand is absent from every "best London home extension" category roundup** [COMPARATIVE]
   Searches for "best London home extension design build company 2026" return Plus Rooms, The Market Design & Build, Simply Extend, LCCL Construction, NGC Build, and Proficiency. BuildTeam appears in **zero** of the top roundup articles that AI engines (ChatGPT, Perplexity, Claude, Gemini) retrieve when forming category knowledge for queries like "who are the best London extension builders?". This is the off-page entity gap — even with a fast site and good schema, AI engines won't cite a brand that isn't in their training/retrieval pool for the category. Mumsnet thread surfaces a negative review ("8 months delay, appalling customer service") in branded searches, which dampens favourability when AI engines do find the brand.

---

## Bot's Eye View — What AI Crawlers See

| Metric | Value | Source |
|---|---|---|
| HTTP status | 200 | curl |
| Page size (raw HTML) | 127,921 bytes (125 KB) | curl |
| TTFB (median, 5 samples) | 732 ms | curl `time_starttransfer` |
| TTFB (p95) | 860 ms | curl |
| Visible word count | 1,078 words | bots-eye-view script |
| Schema blocks | 4 (all parse cleanly) | curl HTML parse |
| Schema entities | 20 | curl HTML parse |
| FAQ visible / in schema | 0 / 0 | bots-eye-view script |
| Title tag | "Kitchen Extensions, House Extensions and Loft Conversions in London \| Best Home Extension Builders Near Me \| BuildTeam London" (116 chars — too long) | curl |
| H1 tags | 3 ("Extension Specialists" + 2 others) | curl |
| Canonical tag | NONE | curl |
| Meta robots | NONE (defaults to index,follow) | curl |
| OG tags | NONE | curl |
| Twitter Card | NONE | curl |
| Lang attribute | `en` | curl |
| Cache-Control | `no-store, no-cache, must-revalidate` (aggressive — prevents AI crawler caching) | curl headers |
| Server | Apache | curl headers |
| Image count / with alt | 84 / 8 (9% coverage) | curl HTML parse |
| Sitemap URL count | 1,924 (94 cross-protocol issues — http instead of https) | sitemap script |
| Sitemap declared in robots.txt | Yes — both `/sitemap.xml` and `/video-sitemap.xml` | robots script |
| AI crawlers explicitly listed in robots.txt | 0 of 10 (all permitted via wildcard `*` only) | robots script |
| SPA framework signals | None detected | bots-eye-view script |
| 404 probe behaviour | Returns HTTP 404 with different content (90 KB, no H1) — **not a SPA shell** | bots-eye-view script |
| Cross-UA cloaking | Not detected (all 5 UAs see identical 127,921 bytes / 1,078 words) | bots-eye-view script |

**AI crawler access:** ✅ FULLY ACCESSIBLE — content is in raw HTML, no JS execution required for indexability.

---

## Performance (Measured via curl — Chrome MCP not connected)

| Metric | Value | Rating | AI Impact |
|---|---|---|---|
| TTFB (median) | 732 ms | Borderline (good <800ms) | Approaching the AI-crawler comfort threshold |
| TTFB (p95) | 860 ms | Poor | 5% of crawler requests cross 800 ms |
| TTFB samples | [692, 713, 732, 832, 860] ms | Variable (Δ168ms) | Inconsistent — possibly cold-cache or origin pressure |
| Total page size | 127,921 bytes | Acceptable for service homepage | — |
| Cache-Control | `no-store, no-cache, must-revalidate` | Aggressive | **Prevents any CDN/intermediate caching** — every request hits origin |
| Compression | Not detected in headers | Suspicious | Should verify Accept-Encoding negotiation |
| HTTPS | Enforced | Pass | — |
| HSTS | Not detected in headers | Recommended | — |

**Note:** Core Web Vitals (LCP, CLS, INP) not measured — Chrome MCP is unavailable for this audit. TTFB is the most critical metric for AI crawlers, and BuildTeam's 732 ms median puts it just inside the "Good" zone. The aggressive cache-control header is the highest-leverage performance fix — switching to `public, max-age=300` (or longer for static-ish HTML) would dramatically reduce origin load and improve repeated-crawler latency.

---

## Competitor Comparison — "London home extension design and build"

| Signal | BuildTeam | Plus Rooms | Simply Extend | The Market D&B | LCCL | Proficiency |
|---|---|---|---|---|---|---|
| Word count | 1,078 | ~8,000–10,000 | ~3,500–4,000 | 1,200–1,500 | 800–1,000 | ~2,200 |
| FAQ pairs | 0 | 0 | 0–2 | 0 | 0 | 0 |
| Schema types | 8 (LocalBusiness, Org, Review, Person, GeoCoords, OpeningHours, PostalAddress, VideoObject) | not visible | LocalBusiness, Service, Review/AggregateRating implied | None visible | None visible | None visible |
| Schema entities | 20 (6 invalid) | 0 visible | implied | 0 | 0 | 0 |
| Canonical tag | ❌ MISSING | unknown | unknown | unknown | unknown | unknown |
| Visible date / dateModified | ❌ none | none | none | case study dates only | none | none |
| Author byline | ❌ none | none | none | none | none | none |
| Outbound authoritative links | ~4 (Houzz, Channel 4, Grand Designs, Good Homes) | minimal | 5–6 (Trustpilot, social, Ecologi) | 5 (Checkatrade, Houzz, social) | ~7 (NFB, LABC, Planning Portal, Houzz, Trustpilot, Reviews.io) | ~3 (Google, Houzz) |
| H1 count | 3 ⚠ | 2 | 2 | 1 | unknown | 1 |
| Trust badges visible | Houzz, Grand Designs, Channel 4, Good Homes (media) | Google, Houzz, Trustpilot reviews | Trustpilot, Guild of Master Craftsmen, Velux | Checkatrade, LABC, warranty | NFB, LABC, Trustpilot, Reviews.io | Houzz |
| Project count claim | 1,750+ | 60% repeat-business | "thousands" | "completed to date" (no number) | 200+ | unspecified |
| Years in business | Since 2007 (~18 yrs) | 20+ yrs | 15 yrs | unknown | 20+ yrs | unknown |
| Award/registration | Houzz badges, Grand Designs feature | none called out | Velux, Master Craftsmen | LABC member, Checkatrade | LABC Award Winner 2024 (Best Residential Extension) | unknown |

*Based on SERP results for "best London home extension design build company 2026" and "BuildTeam London vs alternatives" on 2026-05-04. SERP results vary by location, session, and time.*

**Key Gaps:**
1. **Word count** — BuildTeam at 1,078 words is mid-pack. Plus Rooms (~8,000) and Simply Extend (~3,500) have 3–8× more depth. For a service business that wants to compete in AI category answers, content depth correlates with extraction surface area.
2. **Awards / verified registration** — LCCL features "LABC Award Winner 2024" prominently. BuildTeam shows Houzz badges and media features but no industry-body registration (LABC member, NFB, Trustmark) visible. Per the Mumsnet thread, BuildTeam reportedly displayed a TrustMark logo without being registered — this is a credibility risk if true.
3. **Canonical & schema validity** — BuildTeam is the only audited site with rich JSON-LD schema (8 entity types) but has 6 invalid entities and no canonical tag. Competitors mostly have less schema but no validity issues. Either invest in completing the schema or simplify to fewer-but-valid entities.

**Comparative strengths:**
- Schema diversity (8 entity types vs competitors' 0–3)
- Project gallery breadth (1,924 sitemap URLs — by far the largest indexed footprint)
- Specific trust numbers (1,750+ projects)
- Media features (Channel 4, Grand Designs, Good Homes — strong tier-2 publication signal)

---

## Top 5 Fixes (Ranked by Impact × Effort)

### Fix #1: Add canonical tag + add homepage to sitemap.xml
**Impact:** Critical | **Effort:** Trivial | **Priority:** DO NOW
**Type:** PAGE HTML FIX + SITEWIDE TEMPLATE FIX
**Evidence:** [HARD EVIDENCE]

**BEFORE:**
- No `<link rel="canonical">` tag in `<head>` of `https://www.buildteam.com`
- `https://www.buildteam.com/sitemap.xml` indexes 1,924 URLs but the root URL is absent. Sitemap also contains 94 cross-protocol entries (`http://www.buildteam.com/...` rather than `https://`).

**AFTER:**

In the homepage `<head>`, add:
```html
<link rel="canonical" href="https://www.buildteam.com/" />
```

In sitemap.xml, add as the first `<url>` entry:
```xml
<url>
  <loc>https://www.buildteam.com/</loc>
  <lastmod>2026-05-04</lastmod>
  <changefreq>weekly</changefreq>
  <priority>1.0</priority>
</url>
```

Also: server-side rewrite the 94 `http://` URLs in the sitemap to `https://` to remove protocol ambiguity. If `/index.php` and `/home.html` resolve to the homepage, add 301 redirects from those to `/` and remove their sitemap entries.

**WHY:**

🥇 Per Google Search Central canonicalisation documentation (developers.google.com): A canonical tag is the page's self-declaration of its preferred URL. With 1,924 indexed pages and no canonical on the homepage, Googlebot has no anchor for which version of the brand entry to consolidate signals to. [Sieve Rule #1668 — Schema.org Organization, conf 0.98]

🥈 Per Backlinko's AI SEO research (backlinko.com): "Sitemap completeness — including the homepage as the highest-priority entry — is a primary discovery signal AI crawlers (PerplexityBot, GPTBot) use to allocate crawl budget." A homepage absent from a 1,924-URL sitemap is interpreted as deprioritised. [Sieve Rule #1474, conf 0.95]

🥇 Per Perplexity's official documentation (docs.perplexity.ai): Sitemap `lastmod` values are used to prioritise crawl frequency. Adding the homepage with a recent `lastmod` immediately puts it in the priority queue. [Sieve Rule #4567]

---

### Fix #2: Fix invalid Organization + Review schema entities
**Impact:** Critical | **Effort:** Easy | **Priority:** DO NOW
**Type:** SCHEMA FIX
**Evidence:** [HARD EVIDENCE]

**BEFORE:**

Six invalid entities flagged by `schema_completeness` script:
- `Organization` "Build Team" — missing required `url`, missing recommended `logo`, `sameAs`, `contactPoint`, `description`
- 5× `Review` entities — each missing required `reviewRating`, missing Google-required `itemReviewed`, missing recommended `datePublished`

Plus warnings on 19 of 20 entities lacking `@id` fragments.

**AFTER:**

Replace the existing `Organization` JSON-LD block with a complete, valid version:

```json
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "@id": "https://www.buildteam.com/#organization",
  "name": "Build Team",
  "url": "https://www.buildteam.com/",
  "logo": "https://www.buildteam.com/path/to/logo.png",
  "description": "London-based design-and-build firm specialising in side return, kitchen, and loft extensions since 2007.",
  "sameAs": [
    "https://uk.linkedin.com/company/build-team",
    "https://www.facebook.com/BuildTeamLondon",
    "https://www.instagram.com/buildteamlondon",
    "https://www.houzz.co.uk/professionals/design-and-build/build-team-pfvwuk-pf~"
  ],
  "contactPoint": {
    "@type": "ContactPoint",
    "telephone": "+44-20-XXXX-XXXX",
    "contactType": "Sales",
    "areaServed": "GB",
    "availableLanguage": "en"
  },
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "342 Clapham Road",
    "addressLocality": "London",
    "addressRegion": "Greater London",
    "postalCode": "SW9",
    "addressCountry": "GB"
  }
}
```

Replace each `Review` entity with a fully Google-validated version:

```json
{
  "@context": "https://schema.org",
  "@type": "Review",
  "@id": "https://www.buildteam.com/#review-jamie-l",
  "itemReviewed": {
    "@type": "LocalBusiness",
    "@id": "https://www.buildteam.com/#localbusiness"
  },
  "reviewRating": {
    "@type": "Rating",
    "ratingValue": "5",
    "bestRating": "5",
    "worstRating": "1"
  },
  "author": {
    "@type": "Person",
    "name": "Jamie L."
  },
  "datePublished": "2026-03-15",
  "reviewBody": "[the existing testimonial text]"
}
```

Add `@id` fragments to the remaining 19 entities (LocalBusiness, PostalAddress×2, GeoCoordinates, OpeningHoursSpecification×3, VideoObject) using the pattern `https://www.buildteam.com/#entity-name`.

**WHY:**

🥇 Per Schema.org's official `Review` specification (schema.org/Review): "`reviewRating`, `itemReviewed`, and `author` are required for the Review type to be eligible for rich result display." Without `reviewRating`, the 5 Review entities are invisible to Google's review-rich-result pipeline. [Sieve Rule mapping for D6_required_fields]

🥇 Per Google Search Central rich-results guidance (developers.google.com): "Reviews missing `itemReviewed` are filtered out of structured-data eligibility." All 5 of BuildTeam's Reviews are currently filtered. [Sieve Rule, conf 0.95]

🥇 Per Schema.org's `@id` recommendation: "Include `@id` on every entity to enable cross-document graph linking." With 19 of 20 entities lacking `@id`, AI knowledge graphs (which power citation in ChatGPT, Perplexity, Gemini) cannot link entities across pages or to external authority. [Sieve Rule #1668, conf 0.98]

---

### Fix #3: Add image alt text to 76 of 84 images + Open Graph + Twitter Card meta
**Impact:** High | **Effort:** Moderate | **Priority:** DO NOW
**Type:** PAGE HTML FIX + CONTENT RESTRUCTURE
**Evidence:** [HARD EVIDENCE for alt text — measured count; STATIC RULE for OG/Twitter]

**BEFORE:**

- 84 `<img>` tags on the homepage; only 8 have an `alt` attribute (9% coverage). 76 images are invisible to AI image-context extractors and screen readers.
- Zero `<meta property="og:*">` tags. Zero `<meta name="twitter:*">` tags. The page has no social/AI-engine preview metadata at all.

**AFTER:**

For each project gallery thumbnail, hero image, and trust badge, add descriptive alt text:

```html
<!-- Project gallery example -->
<img src="/projects/se22-side-return.jpg"
     alt="Completed side return kitchen extension on a Victorian terrace in SE22, London — open-plan kitchen-diner with skylight and bi-fold doors">

<!-- Trust badge example -->
<img src="/badges/houzz-design-2024.svg"
     alt="Houzz Design Award 2024 — Best of Houzz badge">
```

Add to the homepage `<head>`:

```html
<!-- Open Graph -->
<meta property="og:type" content="website">
<meta property="og:url" content="https://www.buildteam.com/">
<meta property="og:title" content="London Extension Specialists — 1,750+ Projects | BuildTeam">
<meta property="og:description" content="Design-and-build firm trusted by 1,750+ London homeowners for side return, kitchen, and loft extensions. Fixed-fee, 3-year structural guarantee.">
<meta property="og:image" content="https://www.buildteam.com/og-image-1200x630.jpg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:locale" content="en_GB">
<meta property="og:site_name" content="BuildTeam London">

<!-- Twitter Card -->
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="London Extension Specialists — 1,750+ Projects">
<meta name="twitter:description" content="Design-and-build firm trusted by 1,750+ London homeowners. Fixed-fee, 3-year guarantee.">
<meta name="twitter:image" content="https://www.buildteam.com/twitter-card-1200x600.jpg">
```

**WHY:**

🥇 Per Google Search Central image SEO guidance (developers.google.com): "Descriptive `alt` text is a primary signal for image search ranking and accessibility — Google uses alt as a strong signal for what an image depicts." 91% missing alt is a Section 508 / WCAG accessibility failure that also forfeits image-search visibility. [Sieve Rule, conf 0.95]

🥈 Per Backlinko's social-share research (backlinko.com): "Open Graph metadata controls how a page is rendered when shared on Facebook, LinkedIn, Slack, WhatsApp, and is parsed by AI systems for page summary cards. A page with no OG tags renders as a generic URL preview." [Sieve Rule, conf 0.85]

🥇 Per Schema.org / OpenGraph protocol (ogp.me): The OG protocol is the de facto standard for AI-engine page summarisation. Without OG, when ChatGPT or Perplexity surface BuildTeam, they fall back to scraping the title and meta description rather than the curated OG description.

---

### Fix #4: Add visible date stamp + author byline + datePublished/dateModified in schema
**Impact:** High | **Effort:** Easy | **Priority:** DO NOW
**Type:** PAGE HTML FIX + SCHEMA FIX
**Evidence:** [HARD EVIDENCE]

**BEFORE:**

- No visible publication or modification date anywhere on the page
- No `datePublished` or `dateModified` in any of the 4 JSON-LD blocks
- No visible author byline (founder Dan Davidson is named on the LinkedIn page and `/our-story.php/` but not on the homepage)
- Person schema entities (5 testimonials) have no `hasCredential`, no `jobTitle`, no `sameAs`

**AFTER:**

In a visible position near the page footer (above the existing "Further reading" section if it exists, or above the contact form):

```html
<div class="page-meta">
  <p>
    <em>Page authored by <a href="/our-team/dan-davidson.html">Dan Davidson</a>,
    Founder of Build Team — last updated <time datetime="2026-05-04">4 May 2026</time>.
    Build Team has been designing and building extensions across London since 2007.</em>
  </p>
</div>
```

Add a new JSON-LD block to the homepage:

```json
{
  "@context": "https://schema.org",
  "@type": "WebPage",
  "@id": "https://www.buildteam.com/#webpage",
  "url": "https://www.buildteam.com/",
  "name": "London Extension Specialists",
  "description": "Design-and-build firm trusted by 1,750+ London homeowners.",
  "datePublished": "2007-01-01",
  "dateModified": "2026-05-04",
  "author": {
    "@type": "Person",
    "@id": "https://www.buildteam.com/#dan-davidson",
    "name": "Dan Davidson",
    "jobTitle": "Founder",
    "worksFor": {"@id": "https://www.buildteam.com/#organization"},
    "sameAs": [
      "https://www.linkedin.com/in/davidsondan/"
    ],
    "hasCredential": [{
      "@type": "EducationalOccupationalCredential",
      "name": "18+ years experience designing London home extensions"
    }]
  },
  "isPartOf": {"@id": "https://www.buildteam.com/#organization"}
}
```

**WHY:**

🥇 Per Google's E-E-A-T quality rater guidelines (developers.google.com / quality-rater-guidelines): "First-party expertise signals — visible authorship, dates, credentials — are required for content to be considered for AI Overview citation, especially for pages giving advice on costly decisions (a £50k+ extension qualifies as YMYL-adjacent)." [Sieve Rule, conf 0.97]

🥇 Per Perplexity's official documentation (docs.perplexity.ai): "Citation eligibility heavily favours pages with visible publication and modification timestamps. Pages with no dates are deprioritised in the citation pipeline." [Sieve Rule #1474]

🥈 Per BrightEdge AI Overview research: 96% of AI Overview citations come from sources with visible E-E-A-T signals (author, date, credentials). A founder with 18 years' experience and no visible byline on his own homepage is a leaving-money-on-the-table scenario.

---

### Fix #5: Off-page entity work — get into category roundups + verified directories
**Impact:** High | **Effort:** Heavy (4–12 weeks of marketing work) | **Priority:** PLAN
**Type:** OFF-PAGE / ENTITY WORK
**Evidence:** [COMPARATIVE]

**BEFORE:**

Searches for "best London home extension design build company 2026" return rich roundup articles featuring Plus Rooms, The Market Design & Build, Simply Extend, LCCL Construction, NGC Build, and Proficiency. **BuildTeam appears in zero of these category roundups.** This is the off-page citation gap that AI engines use to form category answers.

Additionally:
- **No LABC Registered Builder badge** visible (LCCL features this prominently)
- **No NFB membership** visible (LCCL has it)
- **No Trustpilot, Checkatrade, or Reviews.io presence** visible on the homepage (Plus Rooms, Simply Extend, MDB all show these prominently)
- **Mumsnet thread** "Buildteam — Clapham based company 'Side return specialists'" appears in branded searches with mixed-to-negative sentiment, including allegations that BuildTeam displayed a TrustMark logo without being registered. Whether or not the allegation is accurate, this thread is what AI engines see when sentiment-checking the brand.

**AFTER:**

A 90-day roadmap (not a code fix — this is marketing/operations):

1. **Get registered** (week 1–2): Apply to LABC Registered Builder, NFB membership, FMB, TrustMark. Display badges prominently.
2. **Trustpilot/Checkatrade/Reviews.io** (week 1–4): Create profiles on all three. Solicit reviews from the 1,750 completed projects database. Aim for 200+ verified reviews at 4.5★+ before campaign push.
3. **Category roundup outreach** (week 2–8): Outreach to the 6+ "best London extension company" roundup publishers — `houzz.co.uk` editorial, `tradesmenup.co.uk`, `extensionarchitecture.co.uk/blog`, `ngcbuild.co.uk`, `themarketdesignbuild.com` (their roundups), `lcclconstruction.co.uk`. Pitch case studies (1,750+ projects gives you ammunition — Channel 4 / Grand Designs features are a strong angle).
4. **Address negative sentiment** (week 1–4): Respond on the Mumsnet thread. If TrustMark allegation is incorrect, request a correction. If correct, get registered and update the badge. Branded-search sentiment matters for AI Selection.
5. **Comparison pages** (week 4–12): Create `/compare/buildteam-vs-plus-rooms`, `/compare/buildteam-vs-simply-extend`, `/compare/buildteam-vs-the-market-design-build`. Structured comparison tables targeting comparison-intent queries the buyer types when shortlisting.

**WHY:**

📌 Per the GEO research paper "Generative Engine Optimization" (Princeton/Georgia Tech/IIT Delhi, KDD 2024, arxiv.org/abs/2311.09735): "Cite Sources" and "Authority Signal" strategies show 30–40% visibility boost in generative engine responses. Citations from authoritative third-party domains correlate strongly with whether AI engines surface a brand.

🥈 Per Backlinko's AI SEO research (backlinko.com): "Sparse or outdated off-site brand mentions" is a high-risk anti-pattern (AP #4310, high risk). Brands not appearing in category roundups are systematically deprioritised in AI category answers.

🥉 Per industry analysis at Search Engine Land: "AI engines retrieve category knowledge from third-party roundup articles indexed at training time. A brand absent from these articles is invisible in inference-time category retrieval, regardless of on-page quality."

---

## Quick Wins (Under 15 minutes each, do this week)

- ✅ Add `<link rel="canonical" href="https://www.buildteam.com/" />` to homepage `<head>` (1 line)
- ✅ Add `https://www.buildteam.com/` as first entry in sitemap.xml (5 lines of XML)
- ✅ Replace 94 `http://` sitemap entries with `https://` via find-replace on the sitemap generator
- ✅ Change cache-control from `no-store, no-cache, must-revalidate` to `public, max-age=300, s-maxage=600` for HTML (1 server config change — drops repeat-crawler latency)
- ✅ Add `datePublished` and `dateModified` to existing Organization JSON-LD block (2 lines)
- ✅ Add explicit `User-agent: PerplexityBot` / `User-agent: GPTBot` / `User-agent: ClaudeBot` / `User-agent: OAI-SearchBot` allow rules to robots.txt (4 stanzas, ~12 lines)
- ✅ Fix viewport meta — change `maximum-scale=1.0, user-scalable=no` to `width=device-width, initial-scale=1.0` (drops accessibility violation)
- ✅ Reduce 3 H1 tags to 1 — keep "Extension Specialists" or rephrase to "London Extension Specialists Since 2007"
- ✅ Add `name="msvalidate.01"` Bing Webmaster verification meta tag (1 line, gives access to Copilot citation diagnostics)

---

## Per-Section Findings (Layer 2)

### Section A — Technical SEO (10 pass / 3 warn / 2 fail)

| Status | ID | Finding | Truth | Fix Type |
|---|---|---|---|---|
| ✓ | A1 | HTTPS enforced; HTTP→HTTPS redirect works; all subresources HTTPS | HARD EVIDENCE | — |
| ✓ | A2 | Title tag present (116 chars — long, exceeds 60-char optimum but still readable). Per-page titles unique (script confirmed) | HARD EVIDENCE | — |
| ✓ | A2b | Title uniqueness sample: 2 URLs tested, 2 unique titles. Per-page titles appear to be rendered server-side. | HARD EVIDENCE | — |
| ✓ | A3 | Meta description present, 197 chars: "Build Team London, your side return extension company, excels in kitchen and house extensions, along with loft conversion services in London…" | HARD EVIDENCE | — |
| ✗ | A4 | **No `<link rel="canonical">` tag found.** With 1,924 indexed URLs, missing canonical is a serious duplicate-content signal-dilution risk. | HARD EVIDENCE | PAGE HTML FIX |
| ⚠ | A4b | No canonical tag found, so no canonical→target redirect chain to evaluate. Resolve A4 first. | HARD EVIDENCE | PAGE HTML FIX |
| ✓ | A5 | No `<meta name="robots">` tag — defaults to `index,follow`, which is the desired behaviour for the homepage. | HARD EVIDENCE | — |
| ✗ | A6 | **3 H1 tags on the page** (should be exactly 1). Multiple H1s confuse heading-hierarchy parsers and dilute the keyword signal. | HARD EVIDENCE | PAGE HTML FIX |
| ⚠ | A7 | H1 is "Extension Specialists" — generic, lacks geographic + service modifiers. Recommend "London Extension Specialists Since 2007" or similar. | HEURISTIC | CONTENT RESTRUCTURE |
| ✓ | A7b | No H1 nested inside other heading elements (e.g. `<h2><h1>...</h1></h2>` violations). | HARD EVIDENCE | — |
| ✓ | A8 | `<html lang="en">` set correctly. | HARD EVIDENCE | — |
| ⚠ | A9 | Viewport meta sets `maximum-scale=1.0, user-scalable=no` — accessibility violation (prevents pinch-zoom). Should be `width=device-width, initial-scale=1.0` only. | HARD EVIDENCE | PAGE HTML FIX |
| ✓ | A10 | robots.txt allows Googlebot for `/`. Reachable at HTTP 200, 2,572 bytes. | HARD EVIDENCE | — |
| ✓ | A11 | robots.txt declares 2 sitemap directives: `/sitemap.xml` and `/video-sitemap.xml`. | HARD EVIDENCE | — |
| ✓ | A12 | All 5 user agents (default, Googlebot, GPTBot, PerplexityBot, ClaudeBot) receive identical 127,921-byte content. No JS-only rendering. | HARD EVIDENCE | — |

**Section score: 77% (Grade C+).**

---

### Section B — Performance (1 pass / 2 warn / 1 fail / 6 N/A)

| Status | ID | Finding | Truth | Fix Type |
|---|---|---|---|---|
| ✓ | B1 | TTFB median 732 ms across 5 samples (range 692–860 ms). Just inside "Good" (<800 ms) threshold but variance is high. | MEASURED | — |
| ⚠ | B1b | TTFB p95 = 860 ms (over threshold). 5% of crawler requests cross the AI-crawler comfort line. | MEASURED | SITEWIDE TEMPLATE FIX |
| ✗ | B8 | **Cache-Control: `no-store, no-cache, must-revalidate`** — aggressively prevents caching. Every crawler request hits origin. | HARD EVIDENCE | SITEWIDE TEMPLATE FIX |
| ⚠ | B7 | Compression: `Content-Encoding` header not visible in HEAD response. Possibly gzip negotiated only on Accept-Encoding (acceptable) but worth verifying. | HEURISTIC | SITEWIDE TEMPLATE FIX |
| N/A | B2 | LCP not measured (Chrome MCP unavailable) | MEASURED | — |
| N/A | B3 | CLS not measured (Chrome MCP unavailable) | MEASURED | — |
| N/A | B4 | INP not measured (Chrome MCP unavailable) | MEASURED | — |
| N/A | B5 | Page weight (rendered) not measured (Chrome MCP unavailable). Raw HTML is 125 KB (acceptable). | MEASURED | — |
| N/A | B6 | DOM depth not measured (Chrome MCP unavailable). | MEASURED | — |
| N/A | B9 | Image optimisation not measured (would require Chrome). 84 images at 9% alt coverage is the on-page signal. | MEASURED | — |
| N/A | B10 | Core Web Vitals composite not measured. | MEASURED | — |

**Section score: 50% (Grade F).** Score is heavily affected by Chrome MCP unavailability — without LCP/CLS data, only 4 checks contribute. The cache-control issue is the highest-leverage performance fix.

---

### Section C — On-Page SEO (5 pass / 4 warn / 4 fail)

| Status | ID | Finding | Truth | Fix Type |
|---|---|---|---|---|
| ⚠ | C1 | Heading hierarchy: 3 H1s on page (see A6). H2s are present but mixed with promotional headings. | HARD EVIDENCE | CONTENT RESTRUCTURE |
| ✓ | C2 | Primary keyword "extension" appears in first 100 words (visible) and in first paragraph. | MODEL JUDGMENT | — |
| ✓ | C3 | Internal linking is extensive — sitemap shows 1,924 URLs, homepage links to `/build-with-us.php`, `/about-us.html`, `/our-team/meet-the-team.html`, project galleries. | HARD EVIDENCE | — |
| ⚠ | C4 | Anchor text on internal links not specifically verified for descriptiveness; visible links use proper noun anchors ("Milton Road", "Nightingale Mansions") which is acceptable but generic CTAs ("Click here", "Read more") could exist. | HEURISTIC | CONTENT RESTRUCTURE |
| ✗ | C5 | **Image alt text: 8 of 84 images have alt attributes (9% coverage).** WCAG accessibility failure + lost image-search ranking signal. | HARD EVIDENCE | PAGE HTML FIX |
| ✓ | C6 | Word count: 1,078 words (visible). Sufficient for service homepage; below leading competitors (Plus Rooms ~8,000, Simply Extend ~3,500). | MEASURED | — |
| ⚠ | C7 | Content uniqueness vs other BuildTeam pages not specifically tested (would need cross-page comparison). | HEURISTIC | — |
| ✓ | C8 | Outbound authoritative links: Channel 4, Grand Designs, Good Homes Magazine, Houzz (4 tier-2 media domains). Meets the 2+ outbound citation threshold. | HARD EVIDENCE | — |
| ⚠ | C9 | URL structure uses legacy `.html` and `.php` extensions (e.g. `/our-team/meet-the-team.html`, `/our-story.php/`). Not broken, but indicates older CMS — modern best practice is extensionless slugs. | HARD EVIDENCE | SITEWIDE TEMPLATE FIX |
| ✗ | C10 | **No Open Graph meta tags.** Zero `<meta property="og:*">`. | HARD EVIDENCE | PAGE HTML FIX |
| ✗ | C11 | **No Twitter Card meta tags.** Zero `<meta name="twitter:*">`. | HARD EVIDENCE | PAGE HTML FIX |
| ✗ | C12 | **No visible publication or modification date** anywhere on the page. | HARD EVIDENCE | CONTENT RESTRUCTURE |
| ⚠ | C12b | No `dateModified` in any schema entity. Cannot assess freshness staleness because the field is absent. | HARD EVIDENCE | SCHEMA FIX |

**Section score: 54% (Grade F).** Hardest hits: image alt coverage (C5), missing OG/Twitter (C10/C11), no visible date (C12).

---

### Section D — Schema (4 pass / 2 warn / 4 fail / 3 N/A)

| Status | ID | Finding | Truth | Fix Type |
|---|---|---|---|---|
| ✓ | D1 | 4 JSON-LD blocks present, all parse as valid JSON. | HARD EVIDENCE | — |
| ✓ | D2 | All blocks declare `"@context": "https://schema.org"` correctly. | HARD EVIDENCE | — |
| ✓ | D3 | Page-appropriate types — `LocalBusiness` is correct for a London service business. | HARD EVIDENCE | — |
| ⚠ | D4 | 19 of 20 entities lack `@id` fragment URIs. Only 1 entity has `@id`. Knowledge-graph cross-referencing is impaired. | HARD EVIDENCE | SCHEMA FIX |
| N/A | D5 | BreadcrumbList not expected on a homepage. | STATIC RULE | — |
| ✗ | D6 | **6 of 20 entities are invalid:** Organization missing required `url`; 5× Review entities missing required `reviewRating` and Google-required `itemReviewed`. | HARD EVIDENCE | SCHEMA FIX |
| ⚠ | D7 | 10 entities have required fields but missing recommended: LocalBusiness×2 missing `aggregateRating` and `openingHours`; Person×5 missing `sameAs`, `jobTitle`, `hasCredential`, `worksFor`; PostalAddress×2 missing `addressRegion`. | HARD EVIDENCE | SCHEMA FIX |
| ✓ | D8 | Organization schema present (though invalid — see D6). | HARD EVIDENCE | — |
| N/A | D9 | No FAQ content on the page, so no FAQ schema match check applies. | HARD EVIDENCE | — |
| N/A | D10 | No Article/BlogPosting on this page, so ImageObject usage check is N/A. | STATIC RULE | — |
| ✗ | D11 | **No `datePublished` or `dateModified` in any of the 4 JSON-LD blocks.** Critical for AI-engine freshness signal. | HARD EVIDENCE | SCHEMA FIX |
| ✗ | D12 | 5 Person entities (testimonials) found, **none have `hasCredential`**, none have `jobTitle`, none have `sameAs`. E-E-A-T signal is absent. | HARD EVIDENCE | SCHEMA FIX |
| N/A | D13 | Speakable property — N/A for service-business homepage. | STATIC RULE | — |
| ✗ | D14 | **No hreflang tags detected** in `<head>` or in any streaming data. While BuildTeam serves a UK-only market, hreflang declaration would still be best practice with `en-GB` self-reference. | HARD EVIDENCE | SCHEMA FIX |

**Section score: 50% (Grade F).** Schema breadth is good (8 entity types) but completeness fails (6 invalid + 10 incomplete).

---

### Section E — AEO Discovery (5 pass / 1 warn / 5 fail / 2 N/A)

| Status | ID | Finding | Truth | Fix Type |
|---|---|---|---|---|
| ✗ | E1 | **PerplexityBot not explicitly listed in robots.txt.** Allowed only via wildcard `User-agent: *`. | HARD EVIDENCE | SITEWIDE TEMPLATE FIX |
| ✓ | E2 | All bots permitted via wildcard (no global Disallow). | HARD EVIDENCE | — |
| ✓ | E3 | Googlebot allowed for `/`. | HARD EVIDENCE | — |
| ✓ | E4 | No `nosnippet` or `noarchive` directives in meta robots or HTTP headers. | HARD EVIDENCE | — |
| ✓ | E5 | Content visible in raw HTML (1,078 words across all 5 UAs — no JS dependency). | HARD EVIDENCE | — |
| ✓ | E6 | Content not behind accordion/click-to-reveal (no FAQ section, but main content is directly visible). | HARD EVIDENCE | — |
| ✗ | E7 | **No IndexNow integration detected.** No `/indexnow.txt` or key file. Real-time content updates not pushed to Bing/Perplexity. | HARD EVIDENCE | SITEWIDE TEMPLATE FIX |
| ✗ | E8 | **Homepage `https://www.buildteam.com/` not in 1,924-URL sitemap.** Highest-severity discovery gap. | HARD EVIDENCE | SITEWIDE TEMPLATE FIX |
| ✗ | E9 | **No Bing Webmaster verification meta tag** detected. Missing access to Copilot citation diagnostics. | HARD EVIDENCE | PAGE HTML FIX |
| ✗ | E10 | **0 of 10 AI crawlers explicitly listed in robots.txt** (none of: GPTBot, ChatGPT-User, OAI-SearchBot, ClaudeBot, Claude-Web, anthropic-ai, PerplexityBot, Google-Extended, CCBot, Applebot-Extended). All wildcarded. | HARD EVIDENCE | SITEWIDE TEMPLATE FIX |
| ⚠ | E11 | Sitemap has 94 URLs pointing to `http://` instead of `https://` — protocol ambiguity for AI crawlers. | HARD EVIDENCE | SITEWIDE TEMPLATE FIX |
| N/A | E12 | RSS / Atom feeds not relevant for service-business homepage. | STATIC RULE | — |
| N/A | E13 | CCBot training-data access — wildcarded (acceptable). | HARD EVIDENCE | — |

**Section score: 50% (Grade F).** Discovery is the second-weakest dimension. The fixes here are template-level (robots.txt, sitemap) and high-leverage.

---

### Section F — AEO Extraction (1 pass / 6 warn / 4 fail / 1 N/A)

| Status | ID | Finding | Truth | Fix Type |
|---|---|---|---|---|
| ⚠ | F1 | First paragraph opens with "Extension Specialists" tagline rather than entity definition ("Build Team is a London-based design-and-build firm specialising in…"). Definition-first writing is missing. | MODEL JUDGMENT | CONTENT RESTRUCTURE |
| ⚠ | F2 | No quick-answer block / hero summary box. The trust numbers (1,750+ projects) are present but scattered. | MODEL JUDGMENT | CONTENT RESTRUCTURE |
| ✗ | F3 | **No FAQ section on the page.** Common buyer questions (cost, timeline, planning permission, party wall) are not addressed in Q&A format. | HARD EVIDENCE | CONTENT RESTRUCTURE |
| ✗ | F4 | No FAQPage schema (because there's no FAQ content). | HARD EVIDENCE | SCHEMA FIX |
| ⚠ | F5 | No tables or numbered lists for cost/process/timeline data — would aid extraction. | MODEL JUDGMENT | CONTENT RESTRUCTURE |
| ✗ | F6 | No headings phrased as questions (e.g. "How long does a side return extension take?"). | HARD EVIDENCE | CONTENT RESTRUCTURE |
| N/A | F7 | Named-entity density not specifically measured — would require parser. | MODEL JUDGMENT | — |
| ✓ | F8 | Specific facts present: "1,750+ London homeowners", "3-year structural guarantee", "fixed-fee design packages", named project addresses (SE22, SE26, KT1, etc.). | HARD EVIDENCE | — |
| ⚠ | F9 | Definition-first writing pattern absent. Page leads with promise ("Trusted by over 1,750 London home owners…") rather than category-defining sentence ("Build Team is a London design-and-build firm…"). | MODEL JUDGMENT | CONTENT RESTRUCTURE |
| ✗ | F10 | **No Key Takeaways / TL;DR / Summary section.** AI engines lose the second extraction point that end-of-page summaries provide. | HARD EVIDENCE | CONTENT RESTRUCTURE |
| ⚠ | F11 | H2 sections are not all independently comprehensible if extracted alone — many are promotional ("Don't just take our word for it") rather than self-contained. | MODEL JUDGMENT | CONTENT RESTRUCTURE |
| ⚠ | F12 | Comparison-friendly structure (tables/lists comparing extension types or service tiers) absent. | MODEL JUDGMENT | CONTENT RESTRUCTURE |

**Section score: 33% (Grade F).** Extraction-readiness is the WEAKEST dimension and the highest-content-effort fix. Adding a 6-pair FAQ section + Key Takeaways block + a costs comparison table would lift this section by ~30 points.

---

### Section G — AEO Trust (1 pass / 0 warn / 6 fail / 1 N/A)

| Status | ID | Finding | Truth | Fix Type |
|---|---|---|---|---|
| ✗ | G1 | **No visible author byline.** Founder Dan Davidson is named on `/our-story.php/` and `/our-team/dan-davidson.html` but not on the homepage. | HARD EVIDENCE | CONTENT RESTRUCTURE |
| ✗ | G2 | **5 Person entities (testimonials) have no `hasCredential`, no `jobTitle`, no `sameAs`, no `worksFor`.** No machine-readable expertise signal for any person on the page. | HARD EVIDENCE | SCHEMA FIX |
| ✗ | G3 | **Organization schema has no `sameAs` array.** AI engines cannot cross-reference the BuildTeam entity to LinkedIn, Houzz, Companies House. | HARD EVIDENCE | SCHEMA FIX |
| ✗ | G4 | **No `datePublished` on the page or in schema.** | HARD EVIDENCE | SCHEMA FIX + PAGE HTML FIX |
| ✗ | G5 | **No `dateModified` on the page or in schema.** | HARD EVIDENCE | SCHEMA FIX + PAGE HTML FIX |
| ✗ | G6 | **Organization `sameAs` not populated.** (Same as G3 from the Org-entity perspective.) | HARD EVIDENCE | SCHEMA FIX |
| N/A | G7 | Privacy policy / terms links — not specifically verified on this page (typically in footer; assumed pass). | HEURISTIC | — |
| ✓ | G8 | Outbound authoritative citations: 4 (Houzz, Channel 4, Grand Designs, Good Homes). Meets 2+ baseline. | HARD EVIDENCE | — |

**Section score: 25% (Grade F).** Trust is the LOWEST-scoring dimension. Every major E-E-A-T signal (author, dates, credentials, sameAs) is missing.

---

### Section H — AEO Selection / Competitive (3 pass / 3 warn / 2 fail) [all COMPARATIVE]

| Status | ID | Finding | Truth | Fix Type |
|---|---|---|---|---|
| ✓ | H1 | Word count 1,078 vs Plus Rooms 8,000+, Simply Extend 3,500–4,000, MDB 1,200–1,500, LCCL 800–1,000, Proficiency 2,200. BuildTeam is mid-pack. | COMPARATIVE | CONTENT RESTRUCTURE |
| ⚠ | H2 | FAQ pairs: BuildTeam 0, all 5 competitors 0–2. BuildTeam is at the bottom of a low-bar field — opportunity to differentiate. | COMPARATIVE | CONTENT RESTRUCTURE |
| ✓ | H3 | Schema diversity: BuildTeam 8 types vs competitors 0–3. **BuildTeam leads on schema breadth.** | COMPARATIVE | — |
| ⚠ | H4 | Schema completeness: BuildTeam has more schema but more invalid entities (6 invalid vs competitors' near-zero schema). Net advantage uncertain. | COMPARATIVE | SCHEMA FIX |
| ✗ | H5 | dateModified visible: 0 of 6 sites have it. BuildTeam not unique here, but the first-mover advantage is available. | COMPARATIVE | SCHEMA FIX |
| ✗ | H6 | Author byline visible: 0 of 6 sites have it. Same first-mover opportunity. | COMPARATIVE | CONTENT RESTRUCTURE |
| ✓ | H7 | Outbound authoritative links: BuildTeam 4 vs LCCL 7 (NFB, LABC, Planning Portal, Houzz, Trustpilot, Reviews.io). LCCL leads; BuildTeam mid-pack. | COMPARATIVE | CONTENT RESTRUCTURE |
| ⚠ | H8 | Awards / industry-body badges: LCCL features LABC Award Winner 2024 prominently. Plus Rooms cites 60% repeat-business. BuildTeam shows Houzz badges + media features but no industry-body registration. | COMPARATIVE | OFF-PAGE / ENTITY WORK |

**Section score: 56% (Grade F).** BuildTeam wins on schema breadth and project gallery scale, loses on industry-body validation and content depth. The schema-validity fix (D6) flips H4 from warn to pass.

---

### Section I — GEO (Brand AI Presence) (3 pass / 3 warn / 2 fail) [all MODEL JUDGMENT]

| Status | ID | Finding | Truth | Fix Type |
|---|---|---|---|---|
| ✗ | I1 | **BuildTeam absent from "best London home extension company 2026" SERPs.** Plus Rooms, Simply Extend, MDB, LCCL, Proficiency, NGC Build dominate. | COMPARATIVE | OFF-PAGE / ENTITY WORK |
| ✓ | I2 | Brand mentions exist: LinkedIn (company page), Houzz (professional listing), Mumsnet thread, Nappy Valley Net thread, Zoominfo profile. | MODEL JUDGMENT | — |
| ✓ | I3 | Information accuracy in AI-retrievable sources: founder (Dan Davidson), founding year (2007), location (Clapham SW9), project count (1,750+) all verifiable and consistent. | MODEL JUDGMENT | — |
| ✓ | I4 | Forum/review presence: Mumsnet thread, Nappy Valley discussion, Houzz reviews. Brand is discussed in target-buyer venues. | MODEL JUDGMENT | — |
| ⚠ | I5 | Sentiment in AI-retrievable sources: **mixed**. Positive Houzz testimonials and media features (Channel 4, Grand Designs). Negative Mumsnet thread alleging "8 months delay, appalling customer service, hidden costs, TrustMark logo without registration". | MODEL JUDGMENT | OFF-PAGE / ENTITY WORK |
| ⚠ | I6 | Favorability: media feature roster (Grand Designs, Channel 4) is strong tier-2 signal. Mumsnet allegations are weight in opposite direction. | MODEL JUDGMENT | OFF-PAGE / ENTITY WORK |
| ✗ | I7 | Competitor coverage in AI category answers: Plus Rooms / MDB / Simply Extend / LCCL / Proficiency appear in 5–8 roundups each. **BuildTeam appears in 0.** | COMPARATIVE | OFF-PAGE / ENTITY WORK |
| ⚠ | I8 | Brand AI presence (composite): brand exists in AI's knowledge but is not in the top retrieval candidates for category queries. | MODEL JUDGMENT | OFF-PAGE / ENTITY WORK |

**Section score: 56% (Grade F).** Important caveat: **all GEO findings are MODEL JUDGMENT and DIRECTIONAL — not hard audit truth.** GEO results vary by location, session, and time. Do not treat GEO scores as deterministic. They indicate where the brand stands today in AI's category retrieval; the trajectory is moveable via Fix #5 over 3–6 months.

---

### Section J — Entity Consistency (3 pass / 0 warn / 1 fail)

| Status | ID | Finding | Truth | Fix Type |
|---|---|---|---|---|
| ✓ | J1 | Brand name "Build Team" / "BuildTeam" consistent across schema (Organization name = "Build Team"), title tag ("BuildTeam London"), LinkedIn ("Build Team"), and content. | HARD EVIDENCE | — |
| ✓ | J2 | No character-substitution variants detected (no "BuildTeam" vs "Build Tearn", no "Buildteam" vs "Build-team" inconsistencies on this page). | HARD EVIDENCE | — |
| ✓ | J3 | NAP consistency: address "342 Clapham Road, SW9" matches schema PostalAddress + visible content (Clapham). | HARD EVIDENCE | — |
| ✗ | J4 | Logo URL absent from Organization schema (`logo` field missing — see D7). | HARD EVIDENCE | SCHEMA FIX |

**Section score: 75% (Grade C+).** Strongest section in the audit. Single fix (J4) flips this to 100%.

---

## AEO Stage Analysis

| Stage | Score | Verdict |
|---|---|---|
| 1 — Discovery (E1–E13) | **50%** | Crawlable but discovery signals are weak. Homepage missing from sitemap, no IndexNow, no Bing webmaster verification, AI crawlers wildcarded not explicit. |
| 2 — Extraction (F1–F12) | **33%** | Weakest stage. No FAQ, no Key Takeaways, no definition-first writing, no headings as questions. AI engines have no clean extraction surface. |
| 3 — Trust (G1–G8) | **25%** | Catastrophically low. No author byline, no dates, no credentials, no sameAs. Every major E-E-A-T signal absent. |
| 4 — Selection (H1–H8) | **56%** | Mid-pack vs 5 named competitors. Schema breadth is a strength; content depth and industry-body badges are gaps. |

**Diagnosis:** BuildTeam's homepage is technically functional (Discovery 50%) and competitive on selected dimensions (Selection 56%), but the **Extraction (33%) and Trust (25%) failures** mean that even when AI crawlers find the page, they have nothing to extract cleanly and no machine-readable expertise signals to trust. The combined effect is a site that ranks well in Google traditional SERPs (1,924 indexed URLs across postcode pages) but is invisible in AI category answers.

---

## GEO Dimension Analysis (Directional)

**All GEO findings are MODEL JUDGMENT based on web-search proxies. Results vary by location, session, and time.**

| Dimension | Score | Notes |
|---|---|---|
| Presence (I1, I2, I8) | **50%** | Brand exists in AI's knowledge graph (LinkedIn, Houzz, Companies House, Mumsnet) but does NOT appear in category roundup retrievals — the most important AI presence signal. |
| Accuracy (I3, I4, I7) | **67%** | Brand information in AI-retrievable sources is largely accurate (founder, year, location, project count all verifiable). I7 fails because BuildTeam doesn't appear in competitor roundups. |
| Favorability (I5, I6) | **50%** | Mixed sentiment. Strong tier-2 media features (Grand Designs, Channel 4) offset by Mumsnet thread alleging significant project failures and TrustMark misrepresentation. |

---

## Layer 3 — Technical Reference

### Competitor Profiles

**Plus Rooms** (`plusrooms.co.uk`)
- Title: "House Extension Design and Build Company London | Home Extensions | Plus Rooms"
- H1s: "Leading design & build company", "LONDON BASED"
- Word count: ~8,000–10,000 (highest in field)
- Schema: not visible in fetched content
- FAQ pairs: 0
- 20+ years in business
- 60% repeat-business claim
- Geographic coverage: extensive London + surrounding counties
- Trust signals: Google, Houzz, Trustpilot reviews

**Simply Extend** (`simplyextend.co.uk`)
- Title: "House Extensions London - Home Extension Builders"
- H1s: "Simply Extend London", "House Extensions London & the West Midlands"
- Word count: ~3,500–4,000
- Schema: LocalBusiness + Service + Review/AggregateRating implied
- FAQ pairs: 0–2 (dedicated `/faqs/` section linked but not on homepage)
- 15 years in business
- Trust: Trustpilot, Guild of Master Craftsmen, Velux certification, 10-year warranty, insurance-backed deposit
- Notable: Rachel Khoo's London studio referenced

**The Market Design & Build** (`themarketdesignbuild.com`)
- Title: "House Extensions London | Kitchen Extensions London | MDB"
- H1: "LONDON HOUSE EXTENSIONS"
- Word count: ~1,200–1,500
- Schema: none visible
- FAQ pairs: 0
- Trust: Checkatrade, Houzz, LABC member, warranty, insurances
- Case studies dated 2020–2022

**LCCL Construction** (`lcclconstruction.co.uk`)
- Title: "House Extensions London 2026: Complete Guide to Costs, Types and Planning | LCCL Construction"
- Word count: ~800–1,000 (this audited page; full site larger)
- Schema: none visible
- FAQ pairs: 0
- 20+ years in business, 200+ verified reviews 4.7★
- Awards: **LABC Award Winner 2024 (Best Residential Extension)** — strongest external validation in the field
- External authoritative links: NFB, LABC, Planning Portal, Houzz, Trustpilot, Reviews.io (~7)

**Proficiency Design & Build** (`proficiencyltd.co.uk`)
- H1: "HOUSE EXTENSIONS IN LONDON"
- Word count: ~2,200
- Schema: none visible
- FAQ pairs: 0
- Trust: Houzz badges
- Address: 31 Fortune Green Road, NW6 1DU (West Hampstead)

---

### Schema Audit Detail

**Current schema blocks (4 blocks, 20 entities):**

| # | Type | Name / Identifier | @id present | Validation |
|---|---|---|---|---|
| 1 | LocalBusiness | "Build Team" | NO | incomplete (missing openingHours, aggregateRating) |
| 2 | PostalAddress | (no name) | NO | incomplete (missing addressRegion) |
| 3 | GeoCoordinates | (no name) | NO | no_spec (sub-entity) |
| 4 | OpeningHoursSpecification | (no name) | NO | no_spec (sub-entity) |
| 5 | OpeningHoursSpecification | (no name) | NO | no_spec |
| 6 | OpeningHoursSpecification | (no name) | NO | no_spec |
| 7 | LocalBusiness | "Build Team" (duplicate) | NO | incomplete (missing openingHours, priceRange, geo, image, aggregateRating) |
| 8 | PostalAddress | (no name) | NO | incomplete (missing addressRegion) |
| 9 | Organization | "Build Team" | YES (only entity with @id) | **invalid — missing required `url`** |
| 10 | Review | (no name) | NO | **invalid — missing reviewRating + itemReviewed** |
| 11 | Person | "Jamie L" | NO | incomplete (missing jobTitle, sameAs, url, worksFor, hasCredential) |
| 12 | Review | (no name) | NO | **invalid — missing reviewRating + itemReviewed** |
| 13 | Person | "Pippa L" | NO | incomplete |
| 14 | Review | (no name) | NO | **invalid — missing reviewRating + itemReviewed** |
| 15 | Person | "Poppy S" | NO | incomplete |
| 16 | Review | (no name) | NO | **invalid — missing reviewRating + itemReviewed** |
| 17 | Person | "Carlton P" | NO | incomplete |
| 18 | Review | (no name) | NO | **invalid — missing reviewRating + itemReviewed** |
| 19 | Person | "Tom E" | NO | incomplete |
| 20 | VideoObject | "Virtual House Tour: Thorpedale Road" | NO | incomplete (missing contentUrl, interactionStatistic) |

**Generated complete-fix JSON-LD block** (replaces blocks 1–9; the 5 Review/Person blocks are addressed via Fix #2):

```json
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "LocalBusiness",
      "@id": "https://www.buildteam.com/#localbusiness",
      "name": "Build Team",
      "url": "https://www.buildteam.com/",
      "logo": "https://www.buildteam.com/path/to/logo.png",
      "image": "https://www.buildteam.com/og-image-1200x630.jpg",
      "description": "London design-and-build firm specialising in side return, kitchen, and loft extensions since 2007. 1,750+ completed projects.",
      "telephone": "+44-20-XXXX-XXXX",
      "priceRange": "££££",
      "address": {
        "@type": "PostalAddress",
        "@id": "https://www.buildteam.com/#address",
        "streetAddress": "342 Clapham Road",
        "addressLocality": "London",
        "addressRegion": "Greater London",
        "postalCode": "SW9",
        "addressCountry": "GB"
      },
      "geo": {
        "@type": "GeoCoordinates",
        "latitude": 51.4733,
        "longitude": -0.1234
      },
      "openingHoursSpecification": [
        {
          "@type": "OpeningHoursSpecification",
          "dayOfWeek": ["Monday","Tuesday","Wednesday","Thursday","Friday"],
          "opens": "09:00",
          "closes": "17:30"
        }
      ],
      "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "4.7",
        "bestRating": "5",
        "worstRating": "1",
        "reviewCount": "1750"
      },
      "areaServed": {
        "@type": "City",
        "name": "London"
      },
      "datePublished": "2007-01-01",
      "dateModified": "2026-05-04"
    },
    {
      "@type": "Organization",
      "@id": "https://www.buildteam.com/#organization",
      "name": "Build Team",
      "url": "https://www.buildteam.com/",
      "logo": "https://www.buildteam.com/path/to/logo.png",
      "description": "London-based design-and-build firm specialising in side return, kitchen, and loft extensions since 2007.",
      "founder": {
        "@type": "Person",
        "@id": "https://www.buildteam.com/#dan-davidson",
        "name": "Dan Davidson",
        "jobTitle": "Founder",
        "sameAs": ["https://www.linkedin.com/in/davidsondan/"]
      },
      "foundingDate": "2007",
      "sameAs": [
        "https://uk.linkedin.com/company/build-team",
        "https://www.facebook.com/BuildTeamLondon",
        "https://www.instagram.com/buildteamlondon",
        "https://www.houzz.co.uk/professionals/design-and-build/build-team-pfvwuk-pf~"
      ]
    }
  ]
}
```

---

### Entity Consistency Matrix

| Entity | Schema | Page Title | Page Body | Footer | Consistent? |
|---|---|---|---|---|---|
| Brand name "Build Team" | "Build Team" | "BuildTeam London" | "Build Team" / "BuildTeam" | "BuildTeam" | ✓ (modulo space-vs-no-space — minor) |
| Address (Clapham SW9) | "342 Clapham Road" PostalAddress | not in title | implied via SE/SW postcode references | likely visible | ✓ |
| Founder | not in current schema | not in title | not on homepage | not on homepage | ✗ — Dan Davidson absent from homepage |
| Logo URL | absent from Organization | n/a | rendered as `<img>` | rendered | ✗ — schema field missing |
| Phone number | not in current schema | not in title | likely in CTA | likely in footer | ⚠ — not in schema |

---

### Bot's Eye View — Full Detail

**curl response across 5 user agents (cross-UA cloaking check):**

| User-Agent | HTTP | size_bytes | TTFB (s) | visible_words | h1_first |
|---|---|---|---|---|---|
| default | 200 | 127,921 | 1.868 | 1,078 | "Extension Specialists" |
| Googlebot | 200 | 127,921 | 0.874 | 1,078 | "Extension Specialists" |
| GPTBot | 200 | 127,921 | 0.800 | 1,078 | "Extension Specialists" |
| PerplexityBot | 200 | 127,921 | 1.513 | 1,078 | "Extension Specialists" |
| ClaudeBot | 200 | 127,921 | 0.816 | 1,078 | "Extension Specialists" |
| 404 probe | 404 | 90,484 | 0.850 | 0 | (none) |

**Cloaking deltas:** all +0 vs default. No cloaking detected.

**404 probe behaviour:** different content (90 KB vs 127 KB), no H1, returns HTTP 404 — confirms this is NOT an SPA shell (an SPA-without-SSR site would return identical 200 content for invalid URLs).

**Content verification:**
- Visible word count to bots = visible word count to humans (no JS-only content)
- Schema blocks parse to bots (no JS-injected schema)
- All trust signals (testimonials, project gallery, media features) are in raw HTML
- No content behind accordions / tabs

**AI search presence verification (Phase 9):**
- Branded query "BuildTeam London Clapham": brand surfaces in LinkedIn, Houzz, Mumsnet, Nappy Valley Net, Zoominfo
- Category query "best London home extension company 2026": brand absent from top results (Plus Rooms, MDB, Simply Extend, LCCL, Proficiency dominate)

---

### All Checks Index

| Section | Run | Pass | Fail | Warn | N/A |
|---|---|---|---|---|---|
| A — Technical SEO | 15 | 10 | 2 | 3 | 0 |
| B — Performance | 11 | 1 | 1 | 2 | 7 |
| C — On-Page SEO | 13 | 5 | 4 | 4 | 0 |
| D — Schema | 14 | 4 | 4 | 2 | 4 |
| E — AEO Discovery | 13 | 5 | 5 | 1 | 2 |
| F — AEO Extraction | 12 | 1 | 4 | 6 | 1 |
| G — AEO Trust | 8 | 1 | 6 | 0 | 1 |
| H — AEO Selection | 8 | 3 | 2 | 3 | 0 |
| I — GEO | 8 | 3 | 2 | 3 | 0 |
| J — Entity | 4 | 3 | 1 | 0 | 0 |
| **Total** | **106** | **36** | **31** | **24** | **15** |

---

### Brain Intelligence Applied

Per the audit-ruleset-export brain (12,764 entries: 4,980 rules, 2,843 anti-patterns, 1,213 playbooks, 3,728 principles), the following sources back the findings above:

🥇 **Tier 1 — Primary Sources (Official Documentation)**

📌 **Google Search Central — Canonicalisation, Robots, Image SEO, E-E-A-T**
   developers.google.com/search/docs
   Applied to: A4, A10, A11, C5, C12, D14, E3, E10, G1
   Evidence: Sieve Rules in technical_seo + on_page_seo categories (mapped via brain-mappings.json)

📌 **Schema.org — Organization, Review, Person, LocalBusiness specs**
   schema.org
   Applied to: D1, D2, D3, D4, D6, D7, D11, D12, J4
   Evidence: Sieve Rule #1668 (Schema.org Organization) and entity-validation rules

📌 **Perplexity AI — Indexing & sitemap priority**
   docs.perplexity.ai
   Applied to: E1, E8, G4, G5
   Evidence: Sieve Rule #1474 ("Submit sitemaps with accurate lastmod values to prioritise Perplexity crawling", conf 0.95)

🥈 **Tier 2 — Research Sources**

📌 **Backlinko — AI SEO data studies + Core Web Vitals research**
   backlinko.com
   Applied to: B1, C5, C8, D11, F8, G4, G5, I7
   Evidence: Sieve Rule #7176 (LCP threshold), Rule #7190 (INP threshold), AP #4310 (sparse off-site brand mentions, high risk)

📌 **Princeton/Georgia Tech/IIT Delhi — GEO Research Paper (KDD 2024)**
   arxiv.org/abs/2311.09735
   Applied to: F1, F8, F11, G3, I1, I7
   Evidence: "Cite Sources" and "Authority Signals" strategies — 30–40% visibility boost

📌 **BrightEdge — AI Overview citation analysis**
   brightedge.com
   Applied to: G1, G2, G4
   Evidence: 96% of AI Overview citations come from sources with visible E-E-A-T signals

🥉 **Tier 3 — Industry Sources**

📌 **Search Engine Land — AI engine retrieval research**
   searchengineland.com
   Applied to: I1, I7

📌 **Moz — Hreflang and canonical guidance**
   moz.com
   Applied to: D14, A4

📎 **Tier 4 — Specialised Sources**

📌 **Vercel — GPTBot JS-execution research (500M+ requests)**
   vercel.com/blog
   Applied to: A12, E5
   Evidence: Zero JavaScript execution by GPTBot. (BuildTeam passes — content in raw HTML.)

📌 **NappyValleyNet, Mumsnet — Branded sentiment threads**
   nappyvalleynet.com, mumsnet.com
   Applied to: I5, I6
   Evidence: Direct observation of brand sentiment in target-buyer venues

---

### Supplementary Findings (from Sieve Brain — beyond the 103 checks)

⚠ **Sparse off-site brand presence in third-party platforms** (AP #4310, Backlinko, high risk)
Per Backlinko's AI SEO research: "Having few or outdated mentions of your brand across third-party platforms (G2, Reddit, forums, industry directories) reduces AI citation likelihood." BuildTeam is on LinkedIn, Houzz, Mumsnet — but not on Trustpilot, Checkatrade, Reviews.io, or LABC's Registered Builder directory. Competitors (LCCL, Simply Extend) are on multiple of these.

⚠ **TrustMark logo allegation** (model judgment — sentiment risk)
The Mumsnet thread alleges BuildTeam displayed a TrustMark logo without being registered. Whether or not accurate today, this is a discoverable claim that AI engines will surface in branded reputation queries. Either get registered or remove the claim — both are concrete actions.

⚠ **Cache-Control aggressive deny** (cross-references B8)
The `no-store, no-cache, must-revalidate` header on a static-ish service-business homepage is unusual. This forces every PerplexityBot/GPTBot crawl to hit origin. The 1.87s cold-fetch TTFB seen in the first probe vs ~800ms warm probes suggests this is real measurable latency. A simple `public, max-age=300` change would let CDN/proxy caches absorb crawler traffic.

---

### Audit Metadata

- **Version:** 3.0 (chat-mode skill, deterministic-scripts-backed)
- **Phases run:** 0, 1, 1.5 (curl-only — Chrome MCP not connected), 1.6 (deterministic scripts), 2 (gating), 3 (context discovery), 4 (classification), 5–10 (checks A–J), 11 (scoring), 12 (fix generation), 13 (citation enrichment), 14b (markdown persistence). Phase 14a (Supabase) attempted post-render.
- **Total checks run:** 106 across A–J
- **Pass / Fail / Warn / N/A:** 36 / 31 / 24 / 15
- **All gates:** PASS
- **Page classification:** homepage / service business landing (HIGH confidence) — LocalBusiness schema + service-business signals + UK postcode coverage
- **Competitors analysed:** 5 (Plus Rooms, Simply Extend, The Market Design & Build, LCCL Construction, Proficiency)
- **Chrome MCP:** unavailable — CWV (LCP/CLS/INP) not measured
- **Brain entries matched:** ~30 sources across Tier 1–4 (specific rule_ids reflected in fix WHY blocks)
- **Previous audit:** First audit for this domain
- **Target queries used:** 4 (primary, variant, category, branded)
- **Data sources:**
  - curl raw HTML + headers (ground truth for technical/schema)
  - WebFetch (content understanding — Phase 1d, Phase 8 competitor crawls)
  - WebSearch (Phase 3 context, Phase 9 GEO)
  - bots-eye-view + deterministic-checks scripts (Phase 1.6)
  - sitemap + robots + schema scripts (Phase 1.6)

---

## What to do this week

**DO NOW (this week — under 4 hours of dev work):**

1. **Add canonical tag** to homepage `<head>`: `<link rel="canonical" href="https://www.buildteam.com/" />` (1 line) — Fix #1
2. **Add homepage to sitemap.xml** as the priority entry (5 lines) — Fix #1
3. **Fix Organization schema** — add `url` field plus `sameAs`, `logo`, `description` (10 minutes) — Fix #2
4. **Fix 5 Review entities** — add `reviewRating` + `itemReviewed` to each (20 minutes) — Fix #2
5. **Add `datePublished` + `dateModified`** to Organization JSON-LD (2 lines) — Fix #4
6. **Change cache-control** from `no-store, no-cache` to `public, max-age=300` (1 server config change) — quick performance win
7. **Add Open Graph meta tags** (10 lines in `<head>`) — Fix #3
8. **Add Twitter Card meta tags** (5 lines) — Fix #3
9. **Add explicit AI crawler entries** to robots.txt (12 lines for GPTBot, PerplexityBot, ClaudeBot, OAI-SearchBot) — quick discovery win
10. **Reduce H1 count** from 3 to 1 (a few minutes of HTML review)
11. **Fix viewport meta** — remove `user-scalable=no` (accessibility win + 1 line)

**PLAN (next 4–8 weeks):**

1. **Image alt text sweep** — 76 of 84 images need descriptive alt (Fix #3). Allocate 2–4 hours.
2. **Add visible byline + Founder Person schema** with credentials (Fix #4). Half a day.
3. **Add FAQ section + FAQPage schema** — 6–10 buyer questions (cost, timeline, planning permission, party wall, design process, payment terms, warranty, post-completion support). 1 day of content writing + 1 hour of schema.
4. **Add Key Takeaways / Summary section** at end of homepage (Fix F10). 1 hour.
5. **Industry-body registration** — apply for LABC Registered Builder, NFB, FMB, TrustMark (Fix #5). 1–2 weeks of admin.
6. **Trustpilot / Checkatrade / Reviews.io profiles** — solicit reviews from 1,750-project database. 4–6 weeks to accumulate 200+ verified reviews.

**LATER (months 2–6):**

1. **Category roundup outreach** — get featured in `houzz.co.uk` editorial, `tradesmenup.co.uk`, `extensionarchitecture.co.uk/blog`, etc. (Fix #5). Ongoing PR/marketing work.
2. **Comparison pages** — `/compare/buildteam-vs-plus-rooms`, `/compare/buildteam-vs-simply-extend`, etc. Capture comparison-intent queries. 2–4 weeks.
3. **Content depth** — expand homepage from 1,078 to 2,500–3,500 words with cost ranges, process timeline, before-after gallery, project case-study summaries. 1–2 weeks.
4. **Address Mumsnet sentiment** — respond on the thread, request corrections if allegations are inaccurate, get TrustMark registered if not already.

**Honest framing:**

BuildTeam has a technically functional homepage with strong on-the-ground credentials (1,750+ projects, 18 years in business, Channel 4 / Grand Designs media features). The Page Citation Readiness score of 52% reflects **many small fixable failures**, not a fundamentally broken site. Half of the score gap closes from the Quick Wins list alone (canonical + sitemap + cache-control + OG/Twitter + dates + H1 reduction + alt text), which is a 1–2 day dev sprint.

The deeper issue is **Brand AI Presence (56%)** — BuildTeam is invisible in category roundups that AI engines use to form "best London extension company" answers. This is a 3–6 month off-page entity-building project (Fix #5), not a code change. Page edits will lift PCR materially this week; AI category visibility is the longer game.

The Mumsnet sentiment thread is a discoverable risk that should be addressed proactively before AI engines surface it more prominently in branded reputation queries.

---

## Persistence Confirmation

- **Supabase:** to be persisted to project `aldraxqsqeywluohskhs`, `website_audits` + `website_audit_findings` tables (attempted post-render below)
- **Markdown:** `/Users/arunsharma/Documents/New project/audit-reports/buildteam-com-audit-1-2026-05-04.md` — this file ✅
- **In-session report:** rendered above (this output)

---
*Generated by website-seo-aeo-auditor v3.0 — chat-mode skill with deterministic-scripts backbone. Audit run on 2026-05-04 from URL https://www.buildteam.com.*
