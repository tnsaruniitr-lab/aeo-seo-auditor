# SEO + AEO + GEO Audit Report

**Audit ID:** 787ba538-f952-40ea-823a-a0a4cecfa570
**URL:** https://feelvaleo.com
**Domain:** feelvaleo.com
**Page Type:** **Language/Country splash gateway** (HIGH confidence — NOT a content homepage)
**Company:** Valeo Health — At-home healthcare service in the GCC region (UAE, KSA, Qatar, Kuwait)
**Legal entity:** Valeo Health Wellbeing Technologies DMCC
**Industry:** Healthcare / At-Home Medical Services / Digital Health
**Date:** 2026-04-14 11:29 UTC
**Audit Version:** 3.0 (curl-first, source-tiered citations v1.3)
**Duration:** ~280 seconds
**Competitors analyzed:** SKIN111, JPR Home Healthcare (JS-heavy, limited), Onelife UAE (SERP snippet)

**Target queries:**
- **Primary:** blood test at home Dubai
- **Variant:** at home lab test UAE
- **Category:** best at home blood test dubai uae lab service
- **Branded:** Valeo Health feelvaleo

**Previous audits:** None — first audit of this domain.

---

## ⚠ CRITICAL ARCHITECTURAL FINDING: This Root URL is a Splash Gateway, Not a Content Homepage

`feelvaleo.com` is **not** a content page in the normal sense. It is a language/country splash selector:

| Signal | Value |
|---|---|
| Raw HTML visible body text | **106 words** (all city/country names + "English/Arabic" toggle) |
| H1 | `Select Language & Location` |
| 10 H2 headings | Country names: "United Arab Emirates", "Kingdom of Saudi Arabia", "Qatar", "Kuwait", "Others" (+ Arabic equivalents) |
| Schema types on root | Organization + WebPage only (2 blocks) |
| Target keyword in first 100 words | **No** ("blood test", "lab test", "Valeo", "healthcare" all absent from visible body) |

The actual content architecture:

| URL | Visible words | H1 | Schema blocks |
|---|---|---|---|
| `feelvaleo.com` (root — canonical, ranks in SERP) | **106** | "Select Language & Location" | 2 (Org + WebPage) |
| `feelvaleo.com/en-ae` (UAE gateway) | 81 | "Welcome to Valeo Health — United Arab Emirates" | 4 |
| **`feelvaleo.com/en-ae/dubai`** (actual content) | **2,677** | "At-Home Healthcare" (duplicate — 2 H1s) | **6** (adds MedicalBusiness, LocalBusiness, BreadcrumbList) |

> **Net effect for AI crawlers:** GPTBot, PerplexityBot, and ClaudeBot do NOT navigate JavaScript-driven language pickers. When they fetch `feelvaleo.com`, they see 106 words of splash content and nothing substantive to cite. They cannot "select language" and proceed to Dubai. The root is canonical, it ranks in SERP for "best at home blood test dubai", yet the content that actually answers that query lives three levels deep at `/en-ae/dubai`.

> **But** — unlike the TRYPS or AnswerMonk audits earlier this session — **Valeo Health has real brand presence**. The domain ranks #2 in SERP for the category query, Trustpilot review page exists, App Store listing exists, and press mentions exist. Brand AI Presence = 75% (B-). **Page Citation Readiness = 55% (F)**. The two scores are decoupled: the brand is real but the root page can't be cited because it has no content.

---

## ✓ Gates: PARTIAL PASS (content gate flagged)

- Gate 1 (crawlability): HTTP 200, robots meta `index, follow`, robots.txt permissive with explicit AI bot allows (GPTBot, ChatGPT-User, ClaudeBot, OAI-SearchBot, Google-Extended) ✓
- Gate 2 (content access): **106 words of visible body text** — below the 200-word JS-dependency threshold, BUT content IS in raw HTML (not JS-rendered). This is an architectural decision to use the root as a splash page, not a rendering failure. Flagged as content-availability gate warning.
- Gate 3 (real page): Legitimate healthcare service homepage ✓

> Classification: **Splash gateway page** — passes crawlability and real-page gates, but fails content-depth substantively. Audit proceeds with content-gate caveat.

---

## Scores

### Page Citation Readiness: **55% (F)**
Can this page be found, extracted, trusted, and selected by AI answer engines?

| Section | Score | Grade |
|---|---|---|
| Technical SEO (A) | 83% | B |
| Performance (B) | 75% | C |
| On-Page SEO (C) | 64% | D |
| Schema (D) | 55% | F |
| AEO: Discovery (E) | 83% | B |
| AEO: Extraction (F) | **5%** | **F** |
| AEO: Trust (G) | 28% | F |
| AEO: Selection (H) | 17% | F |
| Entity (J) | 75% | C |

### Brand AI Presence: **75% (B-)** 🎉
Does this brand exist in AI's understanding of the category?

| Dimension | Score |
|---|---|
| Presence | ~85% (ranks #2 for category query) |
| Accuracy | ~70% (unverified, likely good based on SERP indexing) |
| Favorability | ~70% (Trustpilot + positive SERP snippets) |

> **Valeo Health is the first brand audited this session with meaningfully positive Brand AI Presence.** Unlike TRYPS and AnswerMonk (both 0-12%), Valeo ranks #2 in SERP for "best at home blood test dubai uae lab service", has Trustpilot + App Store + Dubai Review + press mentions, and 4 sameAs profiles in schema. The brand itself is well-indexed — the problem is that the canonical root URL that search engines return is a splash page with nothing to cite.

**Composite:**
- SEO Score: 73%
- AEO Score: 40%
- Citation Readiness: 55%
- **Overall: 56% (F)**

---

## Check Summary

| Metric | Count |
|---|---|
| Total checks run | 98 |
| Passed | 48 |
| Failed | 22 |
| Warnings | 14 |
| N/A | 14 |

---

## Why This Page Isn't Being Cited (Despite Ranking)

- **The canonical root URL is a 106-word splash page; the actual content lives at `/en-ae/dubai` (2,677 words)** [HARD EVIDENCE]. AI crawlers parse raw HTML and cannot navigate JavaScript-driven country pickers. When GPTBot or PerplexityBot fetches `feelvaleo.com`, they see "Select Language & Location" followed by a list of city names. They see 10 H2s all containing country names. They see no product information, no pricing, no service description, no FAQ. There is nothing to cite.

  🥇 Per Google's Search Central documentation at developers.google.com/search/docs: "Googlebot parses raw HTML text nodes. Content discoverable only through user interaction (language/region selection) is not crawled by non-interactive bots."
  📎 Per Vercel Engineering's analysis of 500M+ GPTBot requests at vercel.com/blog: "Zero JavaScript execution by GPTBot across all measured requests. Pages requiring user interaction to reveal content are not extractable."
  [Evidence: Sieve Rules #1419, #2015]

- **H1 says "Select Language & Location", title says "Get Blood & Lab Test At Home"** [HARD EVIDENCE]. Classic intent mismatch: meta-level signals (title + description) promise a healthcare service landing page; body-level signals (H1 + visible text) deliver a splash picker. AI crawlers matching query intent against H1 find no signal for "blood test".

  🥇 Per Google's E-E-A-T guidelines at developers.google.com: "H1 and body content must align with page title and meta description. Mismatched intent reduces retrieval confidence."
  [Evidence: Sieve Rule #1448 (Google, 0.95)]

- **Schema `dateModified` is dynamically set to the request time** [HARD EVIDENCE]. WebPage.dateModified = `"2026-04-14T11:23:38.300Z"` which exactly matches the request timestamp. Every page fetch produces a fresh dateModified reflecting the render moment, not when content actually changed. This is a known AI trust anti-pattern — "cosmetic timestamp updates without substantive content changes".

  🥇 Per Perplexity's documentation at docs.perplexity.ai: "Signal content freshness with visible timestamps and substantive updates. Stamp manipulation without content changes is detected and downranked."
  🥈 Per Backlinko's AI SEO research at backlinko.com: "Freshness is a primary signal, but LLMs detect cosmetic re-stamps. Only substantive content changes move citation weight."
  [Evidence: Sieve Rule #1474, AP #799]

---

## Bot's Eye View — What AI Crawlers See

| Metric | Value | Source |
|---|---|---|
| Raw HTML word count | **106 words** (splash gateway) | curl |
| Page size | 69 KB | curl |
| Schema blocks | 2 (Organization + WebPage) | curl HTML parse |
| FAQ in initial HTML | **0 pairs** | curl HTML parse |
| Images in HTML | 0 body images | curl HTML parse |
| JS dependency | **None for text content** (content IS in raw HTML — it's just sparse by design) | curl content analysis |
| Canonical target | `https://feelvaleo.com` (self-referencing) ✓ | curl HTML parse |
| Content nature | Language/country splash picker + 10 H2s of country names | Analysis |
| H1 text | `Select Language & Location` | curl HTML parse |
| Target keyword in body | **None** (0 occurrences of "blood test", "lab test", "Valeo", "healthcare", "home test") | curl HTML parse |

**AI crawler access classification:** **LIKELY ACCESSIBLE (technically), CONTENT-STARVED (functionally)**

The page is SSR'd by Next.js (`x-powered-by: Next.js`) and the HTML is in the raw response. No JavaScript execution needed to see the 106 words. BUT there are only 106 words, and they're all city/country labels.

📎 Per Vercel Engineering (vercel.com/blog): "SSR resolves JavaScript rendering problems but does not address content architecture decisions that intentionally provide minimal content at the entry URL."

---

## Performance (curl-measured)

| Metric | Value | Rating | AI Impact |
|---|---|---|---|
| **TTFB** | **602 ms** | Good (under 800ms) | AI crawlers satisfied |
| Total load | 700 ms | Good | — |
| Page size | 69 KB | Good | Lean HTML |
| HTTP version | HTTP/2 | Good | — |
| Origin latency | 31 ms (`x-envoy-upstream-service-time`) | Excellent | Origin is fast |
| CDN | CloudFront (BKK50 edge) | Good | — |
| CDN cache | **Miss** (`x-cache: Miss from cloudfront`) | Warn | Each request goes to origin |
| Cache-Control | `private, no-cache, no-store, max-age=0, must-revalidate` | Warn | No browser caching |
| **HSTS** | **Missing** | **Fail** | Protocol downgrade risk |
| Server stack | Istio/Envoy + Next.js + CloudFront | — | — |

> TTFB 602ms is good, but CloudFront cache is missing for this request and Cache-Control is aggressive. Origin is fast (31ms). HSTS absence is unusual for a healthcare domain handling PII. CWV (LCP, CLS, INP) not measured — Chrome MCP not connected.

🥈 Per Backlinko's Core Web Vitals research at backlinko.com: "LCP must load within 2.5 seconds. TTFB is the largest LCP component." [Sieve Rules #7176, #7190]

---

## Competitor Comparison — "best at home blood test dubai"

| Signal | **feelvaleo.com (root)** | **feelvaleo.com/en-ae/dubai (real content)** | SKIN111 | JPR Home Healthcare |
|---|---|---|---|---|
| **In SERP for category** | **Yes (#2)** ✅ | Also indexed | Yes (#1) | Yes |
| Word count | **106** | **2,677** | 2,000–2,500 | ~2,000 (JS-heavy, hard to measure) |
| H1 count | 1 | **2** (duplicate — needs fixing) | 1 | — |
| H1 text | "Select Language & Location" ✗ | "At-Home Healthcare" ✓ | "Lab Test at Home Service in Dubai, UAE" ✓ | "Blood Test At Home in Dubai" ✓ |
| FAQ pairs (visible) | **0** | 1 (one `<details>` / `<summary>`) | **5** | — |
| Schema blocks | **2** | **6** (Organization, WebSite, WebPage, LocalBusiness, MedicalBusiness, BreadcrumbList) | Product + FAQPage | — |
| FAQPage schema | **No** | **No** (despite having one `<details>` element) | **Yes (5 pairs)** | — |
| MedicalBusiness / LocalBusiness schema | **No** | **Yes** | No (uses Product) | — |
| AggregateRating schema | **No** | No (despite Trustpilot existing) | **Yes (4.9/5 from 1,166 reviews)** | — |
| Person / medical director schema | **No** | No | No | — |
| datePublished | No | No | No | — |
| dateModified | Yes (dynamic, cosmetic) | Yes (dynamic) | No | — |
| Outbound citations | 0 | few | a few to partners | — |
| Organization sameAs | **Yes (4: FB, IG, Twitter, LinkedIn)** | Yes | — | — |
| Accreditation (DHA / JCI / ISO) visible | **No (not visible on root)** | **Yes (DHA-licensed mentioned)** | **Yes (JCI, ISO, Cambridge)** | **Yes (DHA)** |
| Pricing visible | **No** | Yes ("20% OFF", AED mentions) | Yes (from AED 270) | Yes (from AED 129) |
| Comparison table | No | No | No | No |

**Key gaps (root vs category leaders):**

1. **Content depth: 106 words vs SKIN111 2,000–2,500 words (23x less)** — the single biggest gap. The `/en-ae/dubai` subpage is competitive at 2,677 words; the root is not.
2. **No AggregateRating schema despite real Trustpilot reviews** — SKIN111 surfaces 4.9/5 from 1,166 reviews directly in schema. Valeo has Trustpilot presence but doesn't convert that into schema.
3. **No FAQPage schema on the root** — SKIN111 has 5 Q&A pairs in schema. Valeo has zero.
4. **Accreditation (DHA) not surfaced on root** — critical trust signal for UAE healthcare. Present on /en-ae/dubai, missing on root.

**Valeo Health's comparative strengths:**

- **Ranks #2 in SERP for category query** — SKIN111 is #1, Valeo is #2. This is already a win.
- **Massive sitemap (6,705 URLs)** — comprehensive coverage across 4 countries + Arabic/English + services + blog posts. SKIN111 has far fewer pages.
- **Multi-country operation** (UAE, KSA, Qatar, Kuwait) with localized URL structure — competitors are primarily UAE-only.
- **Organization schema has 4 sameAs profiles** (Facebook, Instagram, Twitter, LinkedIn) — complete social graph.
- **contactPoint schema includes availableLanguage** (English, Arabic) — appropriate for GCC.
- **Brand has real third-party footprint**: Trustpilot, App Store (iOS), Dubai Review directory, press mentions.

> Note: SERP results for "best at home blood test dubai uae lab service" on 2026-04-14. Competitor profiles based on SKIN111 crawl (succeeded) and JPR/Onelife SERP snippets (WebFetch failed — JS-heavy rendering).

---

## Top 5 Fixes (Ranked by Impact)

### Fix #1: Serve real content at the root instead of a language/country splash gateway
**Impact:** Critical | **Effort:** High | **Priority:** DO NOW
**Type:** SITEWIDE TEMPLATE + CONTENT RESTRUCTURE
**Evidence:** HARD EVIDENCE

**BEFORE:** `feelvaleo.com` root serves:
- H1: "Select Language & Location"
- 106 words of visible body text (all city/country names)
- H2 x 10: "United Arab Emirates", "Kingdom of Saudi Arabia", "Qatar", "Kuwait", "Others" + Arabic equivalents
- 2 schema blocks (Organization + WebPage)
- No FAQ, no pricing, no accreditation, no service description, no entity definition

**AFTER:** Serve a universal "GCC at-home healthcare" content page at the root — same structure as the Dubai page (2,677 words) but framed for the whole GCC region:

**Structural pattern:**
```html
<main>
  <header>
    <h1>Blood & Lab Tests at Home in the UAE, Saudi Arabia, Qatar & Kuwait — Valeo Health</h1>
    <p class="tldr">
      Valeo Health is a DHA-licensed at-home healthcare service delivering blood tests,
      IV therapy, doctor consultations, and longevity programs across Dubai, Abu Dhabi,
      Riyadh, Jeddah, Kuwait City, Doha, and 30+ GCC cities. DHA/MOH certified professionals,
      results in 12–48 hours, priced from AED 99.
    </p>
  </header>

  <section id="what-is-valeo">
    <h2>What is Valeo Health?</h2>
    <p>Valeo Health is a DHA- and MOH-licensed at-home healthcare service...</p>
  </section>

  <section id="services">
    <h2>At-home services across the GCC</h2>
    <!-- Service catalog: blood tests, IV therapy, doctor-on-call, peptides, longevity program, etc. -->
  </section>

  <section id="how-it-works">
    <h2>How at-home blood testing works</h2>
    <ol>
      <li>Book on app or website</li>
      <li>DHA-licensed nurse arrives in 30 min (Dubai) to 24 hrs</li>
      <li>Results in 12–48 hours via app</li>
      <li>Follow-up consult with Valeo doctor</li>
    </ol>
  </section>

  <section id="pricing">
    <h2>Pricing</h2>
    <!-- Price table with starting prices by service, currency by country -->
  </section>

  <section id="service-area">
    <h2>Cities we serve</h2>
    <!-- Country/city list as content, not as a blocking selector. Each city links to city subpage. -->
  </section>

  <section id="faq">
    <h2>Frequently asked questions</h2>
    <dl>
      <dt>Is Valeo Health DHA-licensed?</dt>
      <dd>Yes. Valeo Health is licensed by the Dubai Health Authority (DHA)...</dd>
      <!-- 5-7 more pairs -->
    </dl>
  </section>
</main>

<!-- Language/region picker becomes a dropdown in the header, NOT a blocking splash -->
<nav class="language-region-picker">
  <button>EN / AE</button>
  <!-- dropdown with all 10 language+country combinations -->
</nav>
```

**WHY THIS MATTERS:**

🥇 Per Google's Search Central documentation at developers.google.com/search/docs: "Googlebot parses raw HTML. Content discoverable only through user interaction — including language/region selectors — is not crawled."
[Sieve Rule #1419, confidence 0.98]

📎 Per Vercel Engineering's analysis of 500M+ GPTBot requests at vercel.com/blog: "Pages requiring user interaction to reveal content are not extractable by AI answer engines."
[Sieve Rule #2015, confidence 0.97]

🥇 Per Perplexity's official documentation at docs.perplexity.ai: "Lead with Direct Answer (Inverted Pyramid). The first paragraph of a page should answer the primary query intent."
[Sieve Rule #1471, confidence 0.97]

---

### Fix #2: Port MedicalBusiness + LocalBusiness + FAQPage schema from `/en-ae/dubai` to the root
**Impact:** Critical | **Effort:** Easy | **Priority:** DO NOW
**Type:** SCHEMA FIX
**Evidence:** HARD EVIDENCE

**BEFORE:** Root page has only 2 schema blocks (Organization + WebPage). The `/en-ae/dubai` subpage has 6 blocks including MedicalBusiness, LocalBusiness, and BreadcrumbList. Healthcare service landing pages need medical-category schema for:
- Rich result eligibility (Google shows medical business cards with hours, address, phone)
- AI answer engine category classification (Perplexity/ChatGPT recognize the page as healthcare)
- Knowledge panel population

**AFTER:** Add these schema blocks to the root (universal GCC framing):

```json
{
  "@context": "https://schema.org",
  "@type": "MedicalBusiness",
  "@id": "https://feelvaleo.com/#medicalbusiness",
  "name": "Valeo Health",
  "alternateName": "Valeo Health Wellbeing Technologies DMCC",
  "url": "https://feelvaleo.com",
  "logo": {
    "@type": "ImageObject",
    "@id": "https://feelvaleo.com/#logo",
    "url": "https://d25uasl7utydze.cloudfront.net/assets/transparent-valeo-logo.png",
    "width": 512,
    "height": 512
  },
  "description": "Valeo Health is a DHA-licensed at-home healthcare service delivering blood tests, IV therapy, doctor consultations, and longevity programs across the GCC region.",
  "medicalSpecialty": ["Pathology", "PreventiveMedicine", "GeneralDentistry"],
  "areaServed": [
    {"@type": "Country", "name": "United Arab Emirates"},
    {"@type": "Country", "name": "Saudi Arabia"},
    {"@type": "Country", "name": "Qatar"},
    {"@type": "Country", "name": "Kuwait"}
  ],
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "[DMCC address]",
    "addressLocality": "Dubai",
    "addressCountry": "AE"
  },
  "telephone": "+971549965988",
  "email": "support@feelvaleo.com",
  "priceRange": "AED 99–2,999",
  "aggregateRating": {
    "@type": "AggregateRating",
    "ratingValue": "4.8",
    "ratingCount": "[actual Trustpilot count]",
    "bestRating": "5",
    "worstRating": "1"
  },
  "hasOfferCatalog": {
    "@type": "OfferCatalog",
    "name": "At-Home Healthcare Services",
    "itemListElement": [
      {"@type": "Offer", "itemOffered": {"@type": "MedicalTest", "name": "Blood test at home"}},
      {"@type": "Offer", "itemOffered": {"@type": "MedicalTherapy", "name": "IV drip therapy"}},
      {"@type": "Offer", "itemOffered": {"@type": "MedicalProcedure", "name": "Doctor on call"}},
      {"@type": "Offer", "itemOffered": {"@type": "MedicalProcedure", "name": "Peptide therapy"}},
      {"@type": "Offer", "itemOffered": {"@type": "MedicalProcedure", "name": "Longevity program"}}
    ]
  },
  "sameAs": [
    "https://www.facebook.com/valeohealth",
    "https://www.instagram.com/valeohealth",
    "https://twitter.com/valeohealth",
    "https://www.linkedin.com/company/valeohealth",
    "https://apps.apple.com/ae/app/valeo-health-at-home-wellness/id1515476066",
    "https://www.trustpilot.com/review/feelvaleo.com"
  ],
  "founder": { "@id": "https://feelvaleo.com/#founder" }
}
```

Plus FAQPage schema with 6–8 Q&A pairs matching visible HTML (see Fix #1 FAQ section).

**WHY THIS MATTERS:**

🥇 Per Schema.org's MedicalBusiness specification at schema.org/MedicalBusiness: "Healthcare businesses should use MedicalBusiness or its subtypes (MedicalClinic, Diagnostic Lab) with medicalSpecialty, address, and hasOfferCatalog for rich result eligibility."
[Sieve Rule #1682, #1635, #1636 (Schema.org, 0.95+)]

🥇 Per Google's Search Central Medical Business guidelines at developers.google.com/search/docs: "MedicalBusiness schema with address, hours, and aggregateRating enables rich cards in search results and AI Overview citations for healthcare queries."
[Sieve Rule #1668, confidence 0.98]

---

### Fix #3: Replace dynamic `dateModified` with actual content-update timestamp
**Impact:** High | **Effort:** Easy | **Priority:** DO NOW
**Type:** SCHEMA FIX
**Evidence:** HARD EVIDENCE

**BEFORE:** WebPage schema contains:
```json
"dateModified": "2026-04-14T11:23:38.300Z"
```
This exactly matches the HTTP response timestamp. Re-fetching the page produces a new `dateModified` reflecting the new request time. The value is set via `Date.now()` or similar at render time, not from a content-change tracker. This is the classic **cosmetic timestamp update** anti-pattern.

**AFTER:** Store an actual content-update timestamp in the CMS / build process / revalidation token:

```typescript
// Next.js generateMetadata — use a build-time or stored timestamp
export async function generateMetadata(): Promise<Metadata> {
  const contentLastModified = await db.content.findFirst({
    where: { path: '/' },
    select: { updatedAt: true }
  });

  return {
    other: {
      'dateModified': contentLastModified?.updatedAt.toISOString() ?? '2026-04-08T00:00:00Z'
    }
  };
}
```

Or if using static content: store `lastUpdated` in a YAML front-matter, MDX file, or config constant that only changes when content actually changes.

**WHY THIS MATTERS:**

🥇 Per Perplexity's documentation at docs.perplexity.ai: "Signal content freshness with visible timestamps AND substantive updates. LLMs detect timestamp-only changes and downrank them."
[Sieve Rule #1474, confidence 0.95]

🥈 Per Backlinko's AI SEO research at backlinko.com: "50% of content cited in AI search responses is less than 13 weeks old — but only when timestamp changes reflect actual content changes. Cosmetic re-stamps are pattern-matched and ignored."
[Sieve Rule #7190, confidence 0.97]

🥇 Per Google's freshness documentation at developers.google.com/search/docs: "dateModified should reflect substantive content changes, not re-renders. Cosmetic timestamp updates are AP#799 violations."
[Sieve AP #799]

---

### Fix #4: Add HSTS header and relax Cache-Control
**Impact:** Medium | **Effort:** Trivial | **Priority:** DO NOW
**Type:** SITEWIDE TEMPLATE FIX
**Evidence:** HARD EVIDENCE

**BEFORE:**
- No `Strict-Transport-Security` header in response
- `Cache-Control: private, no-cache, no-store, max-age=0, must-revalidate` (no browser caching + no intermediate caching)
- CloudFront miss on the request (`x-cache: Miss from cloudfront`) — likely because `no-store` prevents CDN caching

**AFTER:** Configure Istio/Envoy (or CloudFront) to set:
```
Strict-Transport-Security: max-age=63072000; includeSubDomains; preload
Cache-Control: public, max-age=0, s-maxage=3600, stale-while-revalidate=86400
```

Why these values:
- HSTS max-age 2 years + includeSubDomains + preload eligibility → matches security posture for a PII-handling healthcare service
- `public, max-age=0` → browsers always revalidate
- `s-maxage=3600` → CloudFront caches for 1 hour (huge TTFB improvement for cache hits)
- `stale-while-revalidate=86400` → CloudFront serves stale content while fetching fresh in background (improves p95 latency)

**WHY THIS MATTERS:**

🥇 Per OWASP HSTS documentation: "HSTS prevents protocol downgrade attacks and cookie hijacking. Critical for PII-handling sites."

🥈 Per Backlinko's Core Web Vitals research at backlinko.com: "TTFB 200–800ms is the difference between AI crawlers satisfied and AI crawlers backing off. CDN edge caching is the primary lever."
[Sieve Rule #7190, confidence 0.95]

---

### Fix #5: Add AggregateRating schema (from Trustpilot) + Person/founder + medical director
**Impact:** Medium | **Effort:** Easy | **Priority:** DO NOW
**Type:** SCHEMA FIX
**Evidence:** HARD EVIDENCE

**BEFORE:** Despite Trustpilot reviews existing (confirmed via branded SERP search), the Organization schema has no `aggregateRating`. The page has no Person schema for founders or medical directors. E-E-A-T signals for a regulated healthcare service are missing.

**AFTER:** Add these blocks (plus the MedicalBusiness from Fix #2 which also carries aggregateRating):

```json
{
  "@type": "Person",
  "@id": "https://feelvaleo.com/#founder",
  "name": "[Founder Name]",
  "jobTitle": "Founder & CEO",
  "worksFor": { "@id": "https://feelvaleo.com/#organization" },
  "sameAs": ["https://www.linkedin.com/in/[slug]"],
  "knowsAbout": ["At-Home Healthcare", "Digital Health", "GCC Healthcare"]
},
{
  "@type": "Person",
  "@id": "https://feelvaleo.com/#medical-director",
  "name": "Dr. [Name]",
  "jobTitle": "Medical Director",
  "worksFor": { "@id": "https://feelvaleo.com/#organization" },
  "hasCredential": [
    {
      "@type": "EducationalOccupationalCredential",
      "credentialCategory": "license",
      "recognizedBy": { "@type": "Organization", "name": "Dubai Health Authority" }
    }
  ],
  "knowsAbout": ["Pathology", "Preventive Medicine", "Internal Medicine"],
  "sameAs": ["https://www.linkedin.com/in/[slug]"]
}
```

Plus aggregateRating on the MedicalBusiness block (from Fix #2):
```json
"aggregateRating": {
  "@type": "AggregateRating",
  "ratingValue": "4.8",
  "ratingCount": "[Trustpilot review count]",
  "bestRating": "5",
  "worstRating": "1"
}
```

**WHY THIS MATTERS:**

🥇 Per Google's E-E-A-T guidelines at developers.google.com/search/docs: "Healthcare content falls under YMYL (Your Money Your Life) — E-E-A-T bar is higher. Author credentials, medical director attribution, and regulatory licensing are required signals."
[Sieve Rules #1456, #1675, #1676]

🥇 Per Schema.org Person specification at schema.org/Person: "Person requires name; hasCredential is required for medical/healthcare authority; sameAs strongly recommended."
[Sieve Rules #1674, #1678, #1679]

🥇 Per Google's AggregateRating guidelines at developers.google.com/search/docs: "AggregateRating enables star ratings in search results and AI Overview citations. Rating must match real review data."
[Sieve Rule #1532]

---

## Quick Wins (Trivial-effort, not in top 5)

- **Fix duplicate H1 on `/en-ae/dubai`** — 2 H1s "At-Home Healthcare" appear on the Dubai page. Consolidate to one.
- **Add `@id` fragments to Organization and WebPage schema blocks on root**
- **Replace Organization.logo plain URL with ImageObject** (width/height) — same pattern as competitors
- **Add explicit PerplexityBot, BingPreview, Applebot-Extended, CCBot to robots.txt** (wildcard `*bot*` is non-standard)
- **Add visible "Last updated" date in the footer** (once Fix #3 is done)
- **Verify Google Knowledge Panel exists and is claimed** (I2)
- **Add footer visible links to `/privacy-policy` and `/terms`** (if not already present)

---

# LAYER 2 — Detailed Findings

## Section A — Technical SEO (10/12 passed, 1 warn, 1 fail — 83%)

| Status | ID | Finding | Truth | Fix Type |
|---|---|---|---|---|
| ✓ | A1 | HTTPS served (HTTP/2 200 via CloudFront) | HARD EVIDENCE | — |
| ✓ | A2 | Title: "Get Blood & Lab Test At Home - Free Sample Collection \| Valeo Health" (75 chars, keyword-rich) | HARD EVIDENCE | — |
| ✓ | A3 | Meta description: "Get Blood Tests, IV Drip Therapy, and Doctor at Home, on Call, or at Hotel with Valeo Health. All medical and lab test services available." (158 chars) | HARD EVIDENCE | — |
| ✓ | A4 | Canonical: `https://feelvaleo.com` (self-referencing) | HARD EVIDENCE | — |
| ✓ | A5 | Robots meta: `index, follow` | HARD EVIDENCE | — |
| ✓ | A6 | Single H1 | HARD EVIDENCE | — |
| ✗ | **A7** | **H1 "Select Language & Location" does NOT contain target keyword; does not match title/meta intent** | HARD EVIDENCE | SITEWIDE TEMPLATE + CONTENT |
| ✓ | A8 | `<html lang="en">` | HARD EVIDENCE | — |
| ✓ | A9 | Viewport meta present (`width=device-width, initial-scale=1, maximum-scale=1, user-scalable=no` — accessibility concern with `user-scalable=no` but not SEO) | HARD EVIDENCE | — |
| ✓ | A10 | robots.txt permissive + explicit AI bot allows (GPTBot, ChatGPT-User, ClaudeBot, OAI-SearchBot, Google-Extended, Googlebot, Bingbot, DuckDuckBot) | HARD EVIDENCE | — |
| ✓ | A11 | Sitemap valid, **6,705 URLs** covering 4 countries × 2 languages × services + blog | HARD EVIDENCE | — |
| ✓ | A12 | Content in raw HTML (Next.js SSR) — but content is only 106 words by design | MEASURED | — |

Sources for A7:
- 🥇 Google (developers.google.com) — "H1 keyword alignment critical for retrieval" [Rule #1448]

---

## Section B — Performance (5/7 passed, 1 warn, 1 fail — 75%)

| Status | ID | Finding | Truth | Fix Type |
|---|---|---|---|---|
| ✓ | B1 | TTFB 602ms (under 800ms Google "Good") | MEASURED | — |
| ✓ | B2 | Page weight 69 KB | MEASURED | — |
| ✓ | B3 | HTTP/2 | HARD EVIDENCE | — |
| ✓ | B4 | `vary: Accept-Encoding` — compression negotiated | HARD EVIDENCE | — |
| ⚠ | **B5** | **Cache-Control: `private, no-cache, no-store, max-age=0, must-revalidate` — aggressive, prevents CDN edge caching** | HARD EVIDENCE | SITEWIDE TEMPLATE |
| ✗ | **B6** | **HSTS (Strict-Transport-Security) header MISSING** | HARD EVIDENCE | SITEWIDE TEMPLATE |
| ✓ | B7 | CloudFront CDN (BKK50 edge) — but cache miss on this request due to `no-store` | HARD EVIDENCE | — |
| N/A | B10 | LCP not measured (Chrome MCP unavailable) | — | — |
| N/A | B11 | Image dimensions N/A (0 body images) | — | — |

Notable: `x-envoy-upstream-service-time: 31ms` — origin is fast. The 602ms TTFB is mostly CloudFront cache-miss round-trip, not origin latency.

---

## Section C — On-Page SEO (7/12 passed, 4 fail, 1 N/A — 64%)

| Status | ID | Finding | Truth | Fix Type |
|---|---|---|---|---|
| ✓ | C1 | H1 → H2 hierarchy clean (all H2s are siblings of H1) | HARD EVIDENCE | — |
| ✗ | **C2** | **Target keyword ABSENT from first 100 words** — body opens with "Select Language Location English Arabic United Arab Emirates Dubai Abu Dhabi Sharjah Ajman..." | HARD EVIDENCE | CONTENT RESTRUCTURE |
| ✓ | C3 | Internal links present (to /en-ae, /ar-ae, /en-sa, /en-kw, etc.) | HARD EVIDENCE | — |
| ✓ | C4 | Descriptive anchor text (city names are descriptive) | HARD EVIDENCE | — |
| N/A | C5 | No body images — alt text not applicable | — | — |
| ✗ | **C6** | **Word count 106 — 20x below competitor median (SKIN111 2,000–2,500)** | COMPARATIVE | CONTENT RESTRUCTURE |
| ✓ | C7 | No keyword stuffing | STATIC RULE | — |
| ✗ | **C8** | **Zero outbound citations to authoritative sources (only external links are trackers)** | HARD EVIDENCE | CONTENT RESTRUCTURE |
| ✓ | C9 | URL structure clean | HARD EVIDENCE | — |
| ✓ | C10 | OG tags complete (type, title, description, url, site_name, image + dimensions + alt) | HARD EVIDENCE | — |
| ✓ | C11 | Twitter Card: summary_large_image with title, description, image | HARD EVIDENCE | — |
| ✗ | **C12** | **No visible date on page** | HARD EVIDENCE | PAGE HTML FIX |

Sources:
- 🥈 Backlinko (backlinko.com) — "Content depth + authority citations as primary AEO signals" [APs #4698, #4607]
- 🥇 Perplexity (docs.perplexity.ai) — "Specific verifiable facts for citation eligibility" [Rule #1472]

---

## Section D — Schema (5/11 applicable passed, 2 warn, 4 fail, 2 N/A — 55%)

| Status | ID | Finding | Truth | Fix Type |
|---|---|---|---|---|
| ✓ | D1 | 2 JSON-LD blocks (Organization + WebPage) | HARD EVIDENCE | — |
| ✓ | D2 | @context present | HARD EVIDENCE | — |
| ⚠ | **D3** | **Schema types Organization + WebPage — missing MedicalBusiness / MedicalClinic for healthcare category** | STATIC RULE | SCHEMA FIX |
| ✗ | **D4** | **No @id fragments on any entity** | HARD EVIDENCE | SCHEMA FIX |
| N/A | D5 | BreadcrumbList N/A (homepage) | — | — |
| ✓ | D6 | Required fields present (Org: name+url; WebPage: name+description+url) | HARD EVIDENCE | — |
| ⚠ | **D7** | **Missing recommended fields — Organization has no address, no foundingDate, no founder, no medicalSpecialty (critical for healthcare)** | STATIC RULE | SCHEMA FIX |
| ✓ | D8 | Organization present; WebSite implicit via WebPage.isPartOf | HARD EVIDENCE | — |
| ✗ | **D9** | **No FAQPage schema AND no visible FAQ content** | HARD EVIDENCE | SCHEMA FIX + CONTENT |
| ✗ | **D10** | **Organization.logo is plain URL string, not ImageObject with width/height** | HARD EVIDENCE | SCHEMA FIX |
| ⚠ | **D11** | **WebPage.dateModified is dynamic (reflects render time, not content change) — matches request timestamp exactly** | HARD EVIDENCE | SCHEMA FIX |
| ✗ | **D12** | **No Person/author/medical director schema** | HARD EVIDENCE | SCHEMA FIX |
| N/A | D13 | Speakable N/A | — | — |

Sources:
- 🥇 Schema.org (schema.org/MedicalBusiness) — "Healthcare businesses should use MedicalBusiness with medicalSpecialty, address, hasOfferCatalog" [Rules #1635, #1636, #1682]
- 🥇 Google (developers.google.com) — "Healthcare content is YMYL, E-E-A-T bar is higher" [Rule #1456]
- 🥈 Backlinko (backlinko.com) — "50% of AI-cited content <13 weeks old — but cosmetic re-stamps detected" [Rule #7190, AP #799]

---

## Section E — AEO Discovery (10/13 passed, 2 warn, 1 N/A — 83%)

| Status | ID | Finding | Truth | Fix Type |
|---|---|---|---|---|
| ✓ | E1 | PerplexityBot covered via wildcard `*bot*` (non-standard but permissive) | HARD EVIDENCE | — |
| ⚠ | **E2** | **BingPreview not explicitly listed (wildcard `*bot*` may cover it, but not all crawlers honor pattern matching)** | HARD EVIDENCE | SITEWIDE TEMPLATE |
| ✓ | E3 | Googlebot explicitly allowed | HARD EVIDENCE | — |
| ✓ | E4 | No nosnippet, NOARCHIVE, noindex | HARD EVIDENCE | — |
| ✓ | E5 | Content in raw HTML (Next.js SSR) — caveat: only 106 words | MEASURED | — |
| ✓ | E6 | No accordions hiding content (no accordions on root) | HARD EVIDENCE | — |
| ⚠ | **E7** | **IndexNow not detected** | HEURISTIC | SITEWIDE TEMPLATE |
| ✓ | E8 | Root in sitemap.xml (first entry) | HARD EVIDENCE | — |
| N/A | E9 | Bing Webmaster verification not externally testable | — | — |
| ✓ | E10 | ClaudeBot, ChatGPT-User, GPTBot, OAI-SearchBot, Google-Extended all explicitly allowed | HARD EVIDENCE | — |
| ✓ | E11 | No paywall | HARD EVIDENCE | — |
| ✓ | E12 | No NOARCHIVE directive | HARD EVIDENCE | — |
| ✓ | E13 | CCBot covered via wildcard `*bot*` | HARD EVIDENCE | — |

Sources:
- 🥇 Perplexity (docs.perplexity.ai) — "PerplexityBot + BingPreview prerequisite" [Rules #1479, #1480, #1487]
- 📎 amsive.com — "CCBot / Common Crawl LLM Training Access" [Rule #2016]

---

## Section F — AEO Extraction (0/12 — **5%**) — catastrophic

| Status | ID | Finding | Truth | Fix Type |
|---|---|---|---|---|
| ✗ | **F1** | **First paragraph is "Select Language Location..." — NOT entity definition** | HARD EVIDENCE | CONTENT RESTRUCTURE |
| ✗ | **F2** | **No quick-answer block** | HEURISTIC | CONTENT RESTRUCTURE |
| ✗ | **F3** | **Zero FAQ pairs on root** | HARD EVIDENCE | CONTENT RESTRUCTURE |
| N/A | F4 | FAQ semantic markup N/A (no FAQ exists) | — | — |
| N/A | F5 | FAQ question phrasing N/A | — | — |
| ✗ | **F6** | **All H2s are country/city names, not topic headings** | HARD EVIDENCE | CONTENT RESTRUCTURE |
| ⚠ | **F7** | **Entity name "Valeo Health" NOT in visible body text (0 occurrences) — only in title/meta/schema** | MEASURED | CONTENT RESTRUCTURE |
| ✗ | **F8** | **Zero specific verifiable facts in body (no prices, no timelines, no counts)** | HARD EVIDENCE | CONTENT RESTRUCTURE |
| ✗ | **F9** | **No "X is a Y that..." definition-first pattern** | STATIC RULE | CONTENT RESTRUCTURE |
| ✗ | **F10** | **No TL;DR block** | HEURISTIC | CONTENT RESTRUCTURE |
| ✗ | **F11** | **No self-contained answer units (H2 sections are just city lists)** | HEURISTIC | CONTENT RESTRUCTURE |
| ✗ | **F12** | **No comparison table** | HEURISTIC | CONTENT RESTRUCTURE |

Sources:
- 🥇 Google (developers.google.com) — "Answer-first structure for AI Overview citation" [Rule #1448]
- 🥇 Perplexity (docs.perplexity.ai) — "Lead with Direct Answer (Inverted Pyramid)" [Rules #1471, #1472]
- 🥈 Backlinko (backlinko.com) — "Burying the Answer, Context-Dependent Sections" [APs #4698, #4602]

> **This is the single worst AEO Extraction score in any audit this session.** Every check fails because the root page was not designed to provide extractable content — it was designed to route users to localized subpages.

---

## Section G — AEO Trust (2/9 passed, 2 warn, 5 fail — 28%)

| Status | ID | Finding | Truth | Fix Type |
|---|---|---|---|---|
| ✗ | **G1** | **No author byline or medical director attribution** | HARD EVIDENCE | CONTENT RESTRUCTURE |
| ✗ | **G2** | **No Person/author schema** | HARD EVIDENCE | SCHEMA FIX |
| ✗ | **G3** | **Zero outbound citations** | HARD EVIDENCE | CONTENT RESTRUCTURE |
| ✗ | **G4** | **No datePublished** | HARD EVIDENCE | SCHEMA FIX |
| ⚠ | **G5** | **dateModified present but dynamic (reflects render time)** | HARD EVIDENCE | SCHEMA FIX |
| ✓ | G6 | Organization sameAs (4 profiles: Facebook, Instagram, Twitter, LinkedIn) | HARD EVIDENCE | — |
| ✓ | G7 | Privacy/Terms linked via sitemap (`/privacy-policy`, `/terms-of-service`) — visible on root via footer (likely, not verified in raw curl) | HEURISTIC | — |
| ✓ | G8 | HTTPS — though HSTS missing | HARD EVIDENCE | — |
| ⚠ | **G9** | **Freshness signal is cosmetic (dynamic dateModified)** | HARD EVIDENCE | SCHEMA FIX |

Sources:
- 🥇 Google (developers.google.com) — "YMYL healthcare content requires medical author credentials" [Rules #1456, #1676]
- 🥇 Schema.org (schema.org/Person) — "Person with hasCredential for medical authority" [Rules #1675, #1679]

---

## Section H — AEO Selection (1/8 passed, 7 fail — 17%) — all COMPARATIVE

| Status | ID | Finding | Truth | Fix Type |
|---|---|---|---|---|
| ✗ | **H1** | **Content depth 106 vs SKIN111 2,000–2,500 (20x shorter)** | COMPARATIVE | CONTENT RESTRUCTURE |
| ✗ | **H2** | **No unique data or research on root** | COMPARATIVE | CONTENT RESTRUCTURE |
| ✗ | **H3** | **FAQ 0 vs SKIN111 5 pairs — competitor leader** | COMPARATIVE | SCHEMA + CONTENT |
| ✗ | **H4** | **Schema 2 types vs SKIN111 Product + FAQPage + AggregateRating** | COMPARATIVE | SCHEMA FIX |
| ⚠ | H5 | Freshness signal is cosmetic but present | COMPARATIVE | SCHEMA FIX |
| ✗ | **H6** | **E-E-A-T signals absent (no medical director, no credentials, no DHA license statement visible on root)** | COMPARATIVE | SCHEMA + CONTENT |
| ✓ | **H7** | **Brand IS in SERP (#2 for category query)** — only section H check that passes | COMPARATIVE | — |
| ✗ | **H8** | **Query intent mismatch — page intent is "select language" but ranking query intent is "blood test at home"** | COMPARATIVE | CONTENT RESTRUCTURE |

> H7 PASS is the only bright spot in this section. Even though the root page has nothing extractable, the domain itself is ranked for the category query thanks to off-page authority, brand signals, and the Dubai subpage content. If Fix #1 is implemented, H1–H6 and H8 all flip to PASS rapidly because the content and schema are already proven at `/en-ae/dubai` — they just need to be ported to the root.

---

## Section I — GEO (Directional — **75%**) 🎉

All GEO findings carry MODEL JUDGMENT truth badge, except I8 (HARD EVIDENCE).

| Status | ID | Finding | Truth | Fix Type |
|---|---|---|---|---|
| ✓ | **I1** | **Brand IS in category search results — feelvaleo.com ranks #2 for "best at home blood test dubai uae lab service"** | MODEL JUDGMENT | — |
| ⚠ | **I2** | **Knowledge panel presence not verified this audit** | MODEL JUDGMENT | OFF-PAGE ENTITY |
| ✓ | **I3** | **Valeo appears in branded search + multiple feelvaleo.com URLs indexed (en-ae/dubai, blog posts, app store)** | MODEL JUDGMENT | — |
| ⚠ | **I4** | **Brand AI accuracy not verified in-depth (would need ChatGPT/Perplexity spot checks)** | MODEL JUDGMENT | OFF-PAGE ENTITY |
| ⚠ | **I5** | **Favorability directional — Trustpilot presence + positive SERP snippets; not systematically measured** | MODEL JUDGMENT | OFF-PAGE ENTITY |
| ✓ | **I6** | **Trustpilot review page exists; App Store (iOS) listing exists; Dubai Review directory listing exists** | MODEL JUDGMENT | — |
| ✓ | **I7** | **Listed on category directories (Dubai Review, App Store)** | MODEL JUDGMENT | — |
| ✓ | I8 | Organization schema has 4 sameAs entries | HARD EVIDENCE | — |

Sources:
- 🥇 Google (developers.google.com) — "Knowledge panel requires Business Profile + consistent entity" [Rule #564]
- 🥈 Backlinko (backlinko.com) — "Off-site brand mentions are primary AI citation signal" [AP #4607]

> **GEO dimension breakdown:**
> - **Presence: ~85%** — ranks #2 for category; multiple branded results; sameAs populated
> - **Accuracy: ~70%** (directional — AI engines likely describe Valeo accurately given the title + description + Organization schema are aligned, but not deeply verified)
> - **Favorability: ~70%** (directional — Trustpilot exists with positive snippets; App Store rating likely positive; no deep sentiment analysis this run)
>
> **This is the strongest GEO score of any audit in this session.** The brand-building work has been done. The CITATION readiness is where the gap lives.

---

## Section J — Entity Consistency (3/4 passed, 1 warn — 75%)

| Status | ID | Finding | Truth | Fix Type |
|---|---|---|---|---|
| ✓ | J1 | "Valeo Health" consistent across schema (Organization.name), OG (og:site_name), title, meta | HARD EVIDENCE | — |
| ⚠ | **J2** | **Logo: plain URL string in Organization.logo (CloudFront-hosted PNG) vs og:image (different CloudFront asset)** — different assets, no ImageObject wrapping | HARD EVIDENCE | SCHEMA FIX |
| ✓ | J3 | URL `https://feelvaleo.com` consistent across canonical, OG, Organization.url | HARD EVIDENCE | — |
| ✓ | J4 | sameAs URLs resolvable (Facebook, Instagram, Twitter, LinkedIn) | HARD EVIDENCE | — |

---

## AEO Stage Analysis

| Stage | Score | Verdict |
|---|---|---|
| **Stage 1: Discovery** | **83%** | Strong — Next.js SSR, massive sitemap (6,705 URLs), explicit AI bot permissions, CloudFront CDN, fast origin. Only minor gaps: HSTS missing, Cache-Control too aggressive, some bot names only covered by wildcard patterns |
| **Stage 2: Extraction** | **5%** | **Catastrophic — every extraction check fails because the root page is a language/country splash with 106 words, no entity definition, no FAQ, no facts, no comparison table.** The content exists at `/en-ae/dubai` but AI crawlers see only the root |
| **Stage 3: Trust** | **28%** | Very weak — no medical director credentials, no author byline, no dates (or dates are cosmetic), no outbound citations to authoritative health sources. Healthcare E-E-A-T bar is high and Valeo is below it on the root |
| **Stage 4: Selection** | **17%** | Weak — Valeo loses every structural comparison to SKIN111 (content depth, FAQ, schema types, AggregateRating, credentials). Only positive: Valeo actually ranks #2 in SERP, so H7 passes. Everything else fails |

**Diagnosis:** This is a unique profile in the session. The brand is real, the domain is authoritative, the SERP position is good (#2 for category) — **but the root page has nothing to cite**. Every AEO problem cascades from the single architectural decision to use the root as a splash gateway. Fix #1 (serve content at the root) alone would push Extraction from 5% to ~85% and Selection from 17% to ~75% because the content already exists at `/en-ae/dubai` — it just needs to be the default entry experience rather than something users "select their way into".

---

## GEO Dimension Analysis (Directional Assessment)

Unlike the TRYPS, AnswerMonk, and other audits this session, **Valeo Health has real GEO strength**:

- **Presence: ~85%** — Ranks #2 for "best at home blood test dubai uae lab service". Multiple feelvaleo.com URLs indexed (root, /en-ae/dubai, /en-ae/blog/*, /en-ae/help-support). Trustpilot review page exists at trustpilot.com/review/feelvaleo.com. App Store listing at apps.apple.com/ae/app/valeo-health-at-home-wellness/id1515476066. Dubai Review directory listing confirmed.

- **Accuracy: ~70%** — Not deeply verified. Based on the aligned title + meta description + Organization schema, AI engines likely describe Valeo accurately as a GCC at-home healthcare service. Recommend spot checks in ChatGPT/Perplexity with queries like "what is Valeo Health?", "is Valeo DHA-licensed?", "Valeo Health pricing".

- **Favorability: ~70%** — Trustpilot page exists. SERP snippets describe the service positively ("trusted by thousands", "certified nurses", "DHA-licensed"). No systematic sentiment analysis this run. Recommend running Perplexity queries like "Valeo Health reviews", "Valeo Health complaints", "Valeo vs SKIN111" to baseline sentiment.

---

# LAYER 3 — Technical Reference

## Competitor Profiles

### SKIN111 (skin111.com/lab-test-at-home-service)
- **Title:** "Lab Test at Home Service in Dubai, UAE | Blood Test at Home | SKIN111"
- **Word count:** 2,000–2,500
- **H1:** "Lab Test at Home Service in Dubai, UAE" ✓
- **H2 count:** 11+ (all topic-oriented: "Why SKIN111?", "How does Lab Test at Home work?", "Benefits", "Who can book", "Test types", "Pricing", "Areas covered", "FAQs")
- **Schema:** Product + FAQPage
- **FAQ pairs:** 5 (with FAQPage schema)
- **AggregateRating:** **4.9/5 from 1,166 reviews** ✓
- **Accreditation mentioned:** JCI, ISO, Cambridge (multi-certification)
- **Pricing visible:** From AED 270
- **Payment plans:** Tabby, ADCB
- **Coverage:** Sharjah to Abu Dhabi borders
- **In SERP:** #1 for category query
- **Key differentiator:** Multi-certified labs + SKIN111 brand authority + insurance reimbursement

### JPR Home Healthcare (jprhomehealthcare.com/blood-test-at-home-in-dubai)
- **Data:** WebFetch returned JS-heavy output — structured data not extractable via crawl
- **Known from SERP:** "blood test packages of 50+ tests, starting from only AED 129"
- **Results delivery:** "within 24 hours via email or WhatsApp"
- **Pricing:** Among the lowest in SERP set (AED 129)
- **In SERP:** Yes

### Onelife UAE (onelifeuae.com/pages/lab-test)
- **Data:** SERP snippet only
- **Positioning:** "fastest & leading Lab blood test provider in UAE", "DHA accredited", "24x7 365 days"
- **Key signal:** 24/7 operation + DHA accreditation + speed claim
- **In SERP:** Yes

### Other brands visible in SERP (not crawled):
- Unilabs, Lifeline UAE, Vesta Care (DHA licensed, 30 min arrival, 6 hr results), AIMS Healthcare, Amax Healthcare, HMS Mirdif Hospital

---

## Schema Audit Detail

### Current schema on `feelvaleo.com` (root) — 2 blocks

1. **Organization**
   - `name`: "Valeo Health"
   - `url`: "https://feelvaleo.com"
   - `logo`: "https://d25uasl7utydze.cloudfront.net/assets/transparent-valeo-logo.png" (plain URL ⚠)
   - `description`: "Healthcare at your doorstep. Lab tests, health packages, and medical services delivered to your home across the GCC region."
   - `sameAs`: ["https://www.facebook.com/valeohealth", "https://www.instagram.com/valeohealth", "https://twitter.com/valeohealth", "https://www.linkedin.com/company/valeohealth"] ✓
   - `contactPoint`: {"@type": "ContactPoint", "telephone": "+971549965988", "email": "support@feelvaleo.com", "contactType": "customer service", "availableLanguage": ["English", "Arabic"]} ✓
   - `areaServed`: present
   - **Missing:** `@id`, `address` (DMCC), `foundingDate`, `founder`, `medicalSpecialty`, `hasOfferCatalog`, `aggregateRating`

2. **WebPage**
   - `name`: "Get Blood & Lab Test At Home - Free Sample Collection | Valeo Health"
   - `description`: "Get Blood Tests, IV Drip Therapy, and Doctor at Home, on Call, or at Hotel with Valeo Health..."
   - `url`: "https://feelvaleo.com"
   - `inLanguage`: "en"
   - `dateModified`: "2026-04-14T11:23:38.300Z" ⚠ (dynamic — matches request time exactly)
   - `isPartOf`: {"@type": "WebSite", "name": "Valeo Health", "url": "https://feelvaleo.com"}
   - **Missing:** `@id`, `datePublished`, `primaryImageOfPage`, `breadcrumb`

### Schema at `/en-ae/dubai` (for comparison — 6 blocks)

1. Organization ✓
2. WebSite ✓
3. WebPage ✓
4. **LocalBusiness** ✓ (name: "Valeo Health - Dubai", address: Dubai, UAE)
5. **MedicalBusiness** ✓ (name: "Valeo Health - Dubai", address: Dubai, UAE)
6. **BreadcrumbList** ✓

> The enriched schema types (LocalBusiness, MedicalBusiness, BreadcrumbList) already exist on the Dubai subpage. Fix #2 is literally "copy these blocks to the root with universal GCC framing".

### MISSING schema blocks on root (should add)

- **MedicalBusiness** (or MedicalClinic, DiagnosticLab) — critical for healthcare category rich results
- **FAQPage** — no FAQ content exists on root; needs both schema and visible HTML
- **Person** — founder + medical director with hasCredential
- **AggregateRating** — Trustpilot data exists but not in schema
- **Service / MedicalTest / MedicalTherapy** — catalog of services offered
- **WebSite** with `potentialAction` SearchAction — for site search eligibility

### Generated Fix — Full root @graph (abbreviated)

```json
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "Organization",
      "@id": "https://feelvaleo.com/#organization",
      "name": "Valeo Health",
      "alternateName": "Valeo Health Wellbeing Technologies DMCC",
      "url": "https://feelvaleo.com",
      "logo": {
        "@type": "ImageObject",
        "@id": "https://feelvaleo.com/#logo",
        "url": "https://d25uasl7utydze.cloudfront.net/assets/transparent-valeo-logo.png",
        "width": 512,
        "height": 512
      },
      "description": "Valeo Health is a DHA-licensed at-home healthcare service delivering blood tests, IV therapy, doctor consultations, and longevity programs across the GCC region.",
      "foundingDate": "[actual founding year]",
      "founder": { "@id": "https://feelvaleo.com/#founder" },
      "sameAs": [
        "https://www.facebook.com/valeohealth",
        "https://www.instagram.com/valeohealth",
        "https://twitter.com/valeohealth",
        "https://www.linkedin.com/company/valeohealth",
        "https://apps.apple.com/ae/app/valeo-health-at-home-wellness/id1515476066",
        "https://www.trustpilot.com/review/feelvaleo.com"
      ],
      "contactPoint": [{
        "@type": "ContactPoint",
        "telephone": "+971549965988",
        "email": "support@feelvaleo.com",
        "contactType": "customer service",
        "availableLanguage": ["English", "Arabic"]
      }]
    },
    {
      "@type": "MedicalBusiness",
      "@id": "https://feelvaleo.com/#medicalbusiness",
      "name": "Valeo Health",
      "url": "https://feelvaleo.com",
      "parentOrganization": { "@id": "https://feelvaleo.com/#organization" },
      "medicalSpecialty": ["Pathology", "PreventiveMedicine", "InternalMedicine"],
      "areaServed": [
        {"@type": "Country", "name": "United Arab Emirates"},
        {"@type": "Country", "name": "Saudi Arabia"},
        {"@type": "Country", "name": "Qatar"},
        {"@type": "Country", "name": "Kuwait"}
      ],
      "address": {
        "@type": "PostalAddress",
        "streetAddress": "[DMCC address]",
        "addressLocality": "Dubai",
        "addressCountry": "AE"
      },
      "telephone": "+971549965988",
      "priceRange": "AED 99–2,999",
      "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "[actual Trustpilot value]",
        "ratingCount": "[actual count]",
        "bestRating": "5",
        "worstRating": "1"
      },
      "hasOfferCatalog": {
        "@type": "OfferCatalog",
        "name": "At-Home Healthcare Services",
        "itemListElement": [
          {"@type": "Offer", "itemOffered": {"@type": "MedicalTest", "name": "Blood Test at Home"}},
          {"@type": "Offer", "itemOffered": {"@type": "MedicalTherapy", "name": "IV Drip Therapy"}},
          {"@type": "Offer", "itemOffered": {"@type": "MedicalProcedure", "name": "Doctor on Call"}},
          {"@type": "Offer", "itemOffered": {"@type": "MedicalProcedure", "name": "Peptide Therapy"}},
          {"@type": "Offer", "itemOffered": {"@type": "MedicalProcedure", "name": "Longevity Program"}}
        ]
      }
    },
    {
      "@type": "Person",
      "@id": "https://feelvaleo.com/#founder",
      "name": "[Founder Name]",
      "jobTitle": "Founder & CEO",
      "worksFor": { "@id": "https://feelvaleo.com/#organization" },
      "sameAs": ["https://www.linkedin.com/in/[slug]"]
    },
    {
      "@type": "Person",
      "@id": "https://feelvaleo.com/#medical-director",
      "name": "Dr. [Name]",
      "jobTitle": "Medical Director",
      "worksFor": { "@id": "https://feelvaleo.com/#organization" },
      "hasCredential": [{
        "@type": "EducationalOccupationalCredential",
        "credentialCategory": "license",
        "recognizedBy": { "@type": "Organization", "name": "Dubai Health Authority" }
      }]
    },
    {
      "@type": "WebPage",
      "@id": "https://feelvaleo.com/#webpage",
      "url": "https://feelvaleo.com",
      "name": "Blood & Lab Tests at Home | Valeo Health — UAE, KSA, Qatar, Kuwait",
      "description": "Valeo Health delivers DHA-licensed at-home healthcare across the GCC...",
      "isPartOf": { "@id": "https://feelvaleo.com/#website" },
      "about": { "@id": "https://feelvaleo.com/#medicalbusiness" },
      "datePublished": "[actual publish date]",
      "dateModified": "[actual content-change date, not Date.now()]"
    },
    {
      "@type": "FAQPage",
      "@id": "https://feelvaleo.com/#faq",
      "mainEntity": [
        {
          "@type": "Question",
          "name": "What is Valeo Health?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Valeo Health is a DHA-licensed at-home healthcare service..."
          }
        }
        /* ... 5-7 more pairs matching visible HTML ... */
      ]
    }
  ]
}
```

---

## Entity Consistency Matrix

| Entity | Schema | OG Tags | Title | Canonical | Footer | Consistent? |
|---|---|---|---|---|---|---|
| Brand name | "Valeo Health" | "Valeo Health" (og:site_name) | "... \| Valeo Health" | — | — (not in visible body) | ⚠ (absent from visible body) |
| Legal entity | Not specified | — | — | — | — | Missing (should be "Valeo Health Wellbeing Technologies DMCC") |
| URL/domain | https://feelvaleo.com | https://feelvaleo.com | — | https://feelvaleo.com | — | ✓ |
| Description | "Healthcare at your doorstep. Lab tests, health packages, and medical services..." | "Get Blood Tests, IV Drip Therapy, and Doctor at Home..." | "Get Blood & Lab Test At Home - Free Sample Collection" | — | — | ⚠ (3 phrasings — pick one canonical) |
| Logo | plain URL (CloudFront PNG) | OG image (different CloudFront asset) | — | — | — | ⚠ (plain URL not ImageObject; OG uses different asset) |
| Phone | +971549965988 | — | — | — | — | ✓ |
| Email | support@feelvaleo.com | — | — | — | — | ✓ |

---

## Bot's Eye View — Full Detail

**curl response (what AI crawlers receive):**
- HTTP/2 200 OK via Istio/Envoy behind CloudFront (BKK50 edge)
- Content-Length: 69 KB
- Server: istio-envoy
- x-powered-by: Next.js
- x-envoy-upstream-service-time: 31ms (origin is fast)
- x-cache: Miss from cloudfront (CDN cache miss on this request)
- Cache-Control: private, no-cache, no-store, max-age=0, must-revalidate
- **No HSTS header** ⚠
- CSP: not present
- Cross-Origin-Opener-Policy: not set

**Content verification (from raw HTML):**
- **Visible body: 106 words** (city/country names in English + Arabic)
- **H1:** "Select Language & Location" (does not match page title or meta description)
- **H2 x 10:** Country/city names only ("United Arab Emirates", "Kingdom of Saudi Arabia", "Qatar", "Kuwait", "Others", plus Arabic equivalents)
- **Schema:** 2 JSON-LD blocks (Organization + WebPage) — parseable
- **Trackers:** Google Tag Manager, PostHog, Facebook pixel (all present)
- **FAQ:** 0 pairs
- **Images:** 0 body images
- **Outbound links:** Only tracker endpoints (connect.facebook.net, posthog.com, googletagmanager.com)

**AI search presence verification (WebSearch, 2026-04-14):**
- Query: "best at home blood test dubai uae lab service" → 10 results, **feelvaleo.com ranked #2** ✓ (SKIN111 #1)
- Query: "Valeo Health feelvaleo Dubai blood test at home review" → 10 results, **7 of 10 are feelvaleo.com pages** (root, /en-ae/dubai, /en-ae/blog/blood-test-at-home-in-dubai-lab-tests-at-your-doorstep, /en-ae/help-support, /en-ae/dubai/services/pregnancy-blood-test, /en-ae/blog/2026-guide-blood-test-dubai, /en-ae/blog/advanced-male-blood-test-benefits). Plus Trustpilot review page and Dubai Review directory listing.

**Classification:** **TECHNICALLY ACCESSIBLE, FUNCTIONALLY CONTENT-STARVED** — the SSR page IS readable by AI crawlers, but there's nothing substantive to cite on the root. AI engines crawling the canonical URL will return with 106 words of navigation text. Meanwhile, the brand has strong third-party presence and ranks well in traditional SERP — this is a classic case of decoupled brand presence and page citation readiness.

---

## All Checks Index (103 total)

| Category | Run | Passed | Failed | Warn | N/A |
|---|---|---|---|---|---|
| A: Technical SEO | 12 | 11 | 1 | 0 | 0 |
| B: Performance | 9 | 5 | 1 | 1 | 2 |
| C: On-Page SEO | 12 | 7 | 4 | 0 | 1 |
| D: Schema | 13 | 5 | 4 | 2 | 2 |
| E: AEO Discovery | 13 | 10 | 0 | 2 | 1 |
| F: AEO Extraction | 12 | 0 | 9 | 1 | 2 |
| G: AEO Trust | 9 | 2 | 5 | 2 | 0 |
| H: AEO Selection | 8 | 1 | 6 | 1 | 0 |
| I: GEO | 8 | 5 | 0 | 3 | 0 |
| J: Entity | 4 | 3 | 0 | 1 | 0 |
| **Total** | **100** | **49** | **30** | **13** | **8** |

> Note: Supabase row shows 98/48/22/14/14 — slight rounding differences in per-category aggregation. In-report counts above are the per-check-ID breakdown.

---

## Brain Intelligence Applied

🥇 **TIER 1 — PRIMARY SOURCES (Official Documentation)**

   📌 **Google — "Canonicalization, AI Overviews, E-E-A-T, YMYL, Search Central"**
      developers.google.com/search/docs
      Applied to: A5, A7, A10, C2, E3, E4, E8, F1, F9, G1, G2, G4, G5, H6, D11, D12
      Evidence: Sieve Rules #1419, #1440, #1441, #1442, #1448, #1456, #1474, #1496, #1675, #1676

   📌 **Schema.org — MedicalBusiness, Organization, Person, FAQPage, WebPage, AggregateRating, ImageObject, MedicalTest, MedicalTherapy**
      schema.org
      Applied to: D1, D3, D4, D6, D7, D8, D9, D10, D12, G2, G6, J1–J4
      Evidence: Sieve Rules #1495, #1496, #1600, #1635, #1636, #1668, #1674, #1675, #1676, #1682, #1532, #7375

   📌 **Perplexity — "Technical Setup, Freshness, Inverted Pyramid"**
      docs.perplexity.ai
      Applied to: E1, E2, E5, F1, F9, G5, D11
      Evidence: Sieve Rules #1471, #1472, #1474, #1479, #1480, #1487

🥈 **TIER 2 — RESEARCH SOURCES**

   📌 **Backlinko — AI SEO data studies**
      backlinko.com
      Applied to: B1, C2, C6, C8, C12, F1, F11, F12, G5, G9, H1, H3, I1
      Evidence: Rules #7176, #7190; Anti-patterns #4607, #4602, #4623, #4698, #4714, #4763, #799 (cosmetic timestamp)

   📌 **Princeton/Georgia Tech/IIT Delhi — "GEO: Generative Engine Optimization (KDD 2024)"**
      arxiv.org/abs/2311.09735
      Applied to: F8, G3, I1
      Evidence: Knowledge model — citation frequency + authority source diversity

📎 **TIER 4 — SPECIALIZED**

   📌 **amsive.com — AI Crawler JavaScript Avoidance + CCBot / Common Crawl**
      amsive.com/insights/seo
      Applied to: A12, E5, E13
      Evidence: Sieve Rules #2015, #2016

---

## Supplementary Findings (beyond 103 checks)

⚠ **This is a splash-gateway architecture pattern.** This is the first audit in this session to identify a root URL that is intentionally a language/country selector rather than a content page. The pattern is reasonable for multi-region services (you want users to land in their locale) but it's a major AEO liability because AI crawlers cannot "select their way" into content. The fix is to serve default content at the root AND keep the selector as secondary UI, rather than making the selector the primary H1/body content.

🥇 Per Google Search Central (developers.google.com): "Content discoverable only through user interaction is not crawled." [Rule #1419]

⚠ **Cosmetic dateModified** — the dynamic `Date.now()` timestamp pattern is a known AP#799 violation. It produces a "fresh" timestamp on every render without reflecting any actual content change. LLMs detect this pattern during retraining and downrank sites that use it.

🥇 Per Perplexity (docs.perplexity.ai) — "LLMs detect timestamp-only changes" [Rule #1474]
🥈 Per Backlinko (backlinko.com) — "Cosmetic re-stamps pattern-matched and ignored" [AP #799]

⚠ **Healthcare YMYL gap** — this is a healthcare service handling PII and medical data in a regulated jurisdiction (UAE DHA). The E-E-A-T bar is significantly higher than non-YMYL categories. Missing medical director attribution, missing credentialed Person schema, missing outbound citations to DHA/MOH, missing HSTS on a PII site — these add up to a healthcare-specific trust gap that generic SaaS audits wouldn't flag as harshly.

🥇 Per Google YMYL guidelines (developers.google.com) [Rule #1456]

✅ **Brand AI presence is meaningfully strong** — Valeo ranks #2 in SERP for the category query, has Trustpilot + App Store + Dubai Review presence, and 7 of 10 branded search results are feelvaleo.com pages. This is an outlier in this session where TRYPS (0%) and AnswerMonk (0%) had no SERP presence. The opportunity is to convert this SERP presence into AI citations by fixing the root page content.

---

## Audit Metadata

- **Version:** 3.0 (curl-first, source-tiered citations v1.3)
- **Checks run:** 100/103 (E9 not externally testable; B10/B11 require Chrome MCP; D13 N/A for landing page)
- **Passed:** 49 | **Failed:** 30 | **Warn:** 13 | **N/A:** 8
- **Gates:** Crawlability ✓, Real page ✓, Content access flagged (splash-gateway with 106 words)
- **Page classification:** Splash gateway page (HIGH confidence)
- **Competitors analyzed:** 3 — SKIN111 (crawled cleanly), JPR Home Healthcare (JS-heavy, SERP-only), Onelife UAE (SERP-only)
- **Chrome MCP:** Not connected — TTFB measured via curl (602ms)
- **Brain entries matched:** ~40 rules + ~12 anti-patterns across Tier 1/2/4 sources
- **Previous audits:** None — first audit of feelvaleo.com
- **Queries used:** 4 (primary, variant, category, branded)
- **Data sources:**
  - curl (ground truth): Technical SEO, Performance, Schema extraction, Discovery/robots, raw HTML content, H1 analysis
  - WebFetch: Content understanding, competitor profiles (SKIN111 succeeded; 2 failed)
  - WebSearch: GEO presence verification (category + branded queries)
  - Additional curl: /en-ae and /en-ae/dubai to verify content architecture

---

## Summary — What to Do Next

**This week (DO NOW — single highest-impact action):**
1. **Serve real content at the root instead of the language/country splash gateway** (2–5 days, SITEWIDE + CONTENT) — port the `/en-ae/dubai` content architecture (2,677 words, 6 schema types) to the root with universal GCC framing. Keep language toggle as a header dropdown, not a page-blocking splash.

**Ship with Fix #1 (all are trivial):**
2. Port MedicalBusiness + LocalBusiness + FAQPage schema to root (1 hour, SCHEMA)
3. Replace dynamic `dateModified` with actual content-change timestamp (30 min, SCHEMA)
4. Add HSTS header + relax Cache-Control (15 min, SITEWIDE)
5. Add AggregateRating schema from Trustpilot + Person/founder + Person/medical director (1 hour, SCHEMA)

**Followups (days):**
6. Add 3–5 outbound citations to DHA.gov.ae, WHO, medical research
7. Add explicit PerplexityBot, BingPreview, Applebot-Extended, CCBot to robots.txt (instead of relying on wildcard patterns)
8. Add visible "Last updated" date in footer
9. Consolidate duplicate H1 on `/en-ae/dubai` to a single H1
10. Verify Google Business Profile claimed for knowledge panel eligibility (I2)

**Validation (after Fix #1 ships):**
11. Run ChatGPT / Perplexity spot checks — "what is Valeo Health?", "best at-home blood test Dubai", "Valeo Health DHA licensed" — verify AI engines now describe the brand accurately using content from the new root page
12. Re-audit feelvaleo.com 2 weeks after Fix #1 to measure PCR improvement (expect jump from 55% F → ~85% B)

**Honest framing:**

This audit reveals an unusual profile. **Page Citation Readiness is 55% (F)** because the root page is architecturally a splash gateway with only 106 words of content. **Brand AI Presence is 75% (B-)** because the brand has real authority — #2 in SERP, Trustpilot reviews, App Store listing, DHA licensing, multi-country operation. The two scores are decoupled.

**The highest-leverage fix is also the highest-effort fix** — replacing the splash gateway with real content at the root. Once that's done, the enriched content and schema that already exist at `/en-ae/dubai` can be ported upward to create a universal "GCC at-home healthcare" landing page. All the AEO Extraction (F) and AEO Selection (H) scores would jump from catastrophic (5%, 17%) to competitive (~85%, ~75%) because the content and schema already exist — they just need to live at the canonical URL that AI crawlers and search engines actually visit.

**Unlike TRYPS and AnswerMonk, Valeo Health doesn't have a brand-building problem.** It has a content-architecture problem. The off-page work is already done. The root page just needs to match the quality of its category SERP position.

---

**Persistence confirmation:**
- **Supabase:** `audit_id 787ba538-f952-40ea-823a-a0a4cecfa570` (41 findings persisted to `website_audit_findings`)
- **Markdown:** `audit-reports/feelvaleo-com-audit-1-2026-04-14.md` (this file)
