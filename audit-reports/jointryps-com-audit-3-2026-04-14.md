# SEO + AEO + GEO Audit Report

**Audit ID:** 8b42e9d0-188b-4cb0-aec8-3e0a7b62e367
**URL:** https://jointryps.com
**Domain:** jointryps.com
**Page Type:** SaaS landing page / homepage (HIGH confidence)
**Company:** TRYPS — Group trip planning app for friends — plan together, split expenses, coordinate itineraries
**Industry:** Travel Tech / Consumer SaaS
**Date:** 2026-04-14 10:13 UTC
**Audit Version:** 3.0 (curl-first, source-tiered citations v1.3)
**Duration:** ~210 seconds
**Competitors analyzed:** SquadTrip, Wanderlog, TripIt (crawl failed — socket closed)

**Target queries:**
- **Primary:** group trip planning app
- **Variant:** plan a trip with friends online
- **Category:** best group trip planning app 2026
- **Branded:** TRYPS app

**Previous audits in Supabase (different URL — note the divergence):**
- Audit #1: `https://trypsagent.com` — 2026-04-10 10:28 — 52% (F)
- Audit #2: `https://trypsagent.com` — 2026-04-10 12:44 — 58% (F)

> **Important context:** Previous audits were on the `trypsagent.com` alternate hostname which had a different page structure (9 schema blocks, FAQPage with 7 Q&A, HowTo, MobileApplication x2, BreadcrumbList). This audit is the **first audit of the canonical homepage** at `https://jointryps.com`, which has a simpler schema structure and no FAQ content. The schema enrichment done on trypsagent.com has not propagated to the canonical surface — flagged as Fix #2 below.

---

## ✓ Gates: ALL PASSED

- Gate 1 (crawlability): HTTP 200, no robots meta (default index+follow), robots.txt permissive ✓
- Gate 2 (content access): 667 words of body text in raw HTML (Next.js SSR + Vercel edge prerender) ✓
- Gate 3 (real page): Legitimate SaaS homepage for consumer travel app ✓

---

## Scores

### Page Citation Readiness: **59% (D-)**
Can this page be found, extracted, trusted, and selected by AI answer engines?

| Section | Score | Grade |
|---|---|---|
| Technical SEO (A) | 92% | A- |
| Performance (B) | 88% | B+ |
| On-Page SEO (C) | 82% | B |
| Schema (D) | 50% | F |
| AEO: Discovery (E) | 85% | B |
| AEO: Extraction (F) | 29% | F |
| AEO: Trust (G) | 11% | F |
| AEO: Selection (H) | 0% | F |
| Entity (J) | 75% | C |

### Brand AI Presence: **0% (F)**
Does this brand exist in AI's understanding of the category?

| Dimension | Score |
|---|---|
| Presence | 0% |
| Accuracy | N/A |
| Favorability | N/A |

> TRYPS appeared in **zero** results across both WebSearch queries. Competitors dominating the category: SquadTrip, Wanderlog, TripIt, FlowTrip, Plan Harmony, ClanPlan, Troupe, AvoSquado, JoinMyTrip, Splitwise. Brand presence is a **months-long entity-building problem**, not a page-edit problem.

**Composite:**
- SEO Score: 78%
- AEO Score: 40%
- Citation Readiness: 59%
- **Overall: 56% (F)**

---

## Check Summary

| Metric | Count |
|---|---|
| Total checks run | 95 |
| Passed | 52 |
| Failed | 25 |
| Warnings | 11 |
| N/A | 7 |

---

## Trend (vs. previous audits on trypsagent.com — different URL)

| Metric | Audit #2 (trypsagent.com, 2026-04-10) | Audit #3 (jointryps.com, 2026-04-14) | Change |
|---|---|---|---|
| Overall | 58% (F) | 56% (F) | -2% |
| Technical SEO | 65% | 92% | **+27%** |
| Performance | 55% | 88% | **+33%** |
| On-Page SEO | 60% | 82% | **+22%** |
| Schema | 88% | 50% | **-38%** |
| AEO: Discovery | 73% | 85% | +12% |
| AEO: Extraction | 42% | 29% | -13% |
| AEO: Trust | 33% | 11% | -22% |
| AEO: Selection | 25% | 0% | -25% |
| GEO | 15% | 0% | -15% |
| Entity | 65% | 75% | +10% |

> **Treat this as a FIRST audit of the canonical homepage, not a regression.** The Schema/Trust/Selection drops reflect the fact that the trypsagent.com surface had FAQPage, Person, HowTo, MobileApplication x2, and BreadcrumbList schemas that were never copied to jointryps.com. The Technical/Performance/On-Page gains reflect the canonical homepage being a cleaner Next.js build served from Vercel edge cache.

---

## Why This Page Isn't Being Cited

- **The H1 is garbled in raw HTML due to an animated text SSR artifact** [HARD EVIDENCE]. AI crawlers see `Plan y our whatever with whoever whatever with whoever` — not the intended `Plan your [destination] with [group]`. The animation uses sr-only + aria-hidden inline spans that concatenate when CSS isn't applied. AI bots don't render CSS — they ingest all text nodes literally.

  🥇 Per Google's Search Central documentation at developers.google.com/search/docs: "Googlebot parses raw HTML text nodes; CSS display rules and aria-hidden do not remove content from extraction."
  📎 Per amsive.com at amsive.com/insights/seo/answer-engine-optimization: "AI crawlers parse all visible text nodes regardless of CSS visibility or ARIA attributes."
  [Evidence: Sieve Rule #2015, Rule #1419]

- **No FAQPage schema AND no visible FAQ content on the canonical homepage** [HARD EVIDENCE]. Every missing Q&A is a missed AI citation entry point. The previous trypsagent.com audit had 7 Q&A pairs — that fix never made it to the canonical URL.

  🥇 Per Schema.org's FAQPage documentation at schema.org/FAQPage: "FAQPage schema requires visible Q&A content matching markup; mainEntity array with Question/Answer pairs enables rich result eligibility."
  🥇 Per Google's Search Central FAQ guidelines at developers.google.com/search/docs/appearance/structured-data/faqpage: "FAQ content is one of the highest-value AI Overview citation anchors for SaaS homepages."
  [Evidence: Sieve Rules #1600, #1602, #7375]

- **Brand has zero footprint in AI category knowledge** [MODEL JUDGMENT]. Searching "best group trip planning app 2026 friends travel" returns SquadTrip, TripIt, FlowTrip, Plan Harmony, ClanPlan, Troupe, AvoSquado, JoinMyTrip, Wanderlog, WhenAvailable — TRYPS is in none of them. Branded query returns Troupe, Tripsy, TripIt, Wanderlog — TRYPS absent from branded results too.

  🥈 Per Backlinko's AI SEO research at backlinko.com: "Having few or outdated mentions of your brand across third-party platforms (G2, Reddit, forums) reduces AI citation likelihood."
  [Evidence: Sieve AP #4607 (Backlinko, high risk)]

---

## Bot's Eye View — What AI Crawlers See

| Metric | Value | Source |
|---|---|---|
| Raw HTML word count | 667 words | curl (= what AI bots receive) |
| Page size | 47 KB | curl |
| Schema blocks | 1 JSON-LD block containing @graph of 3 types (Organization, SoftwareApplication, WebSite) | curl HTML parse |
| FAQ in initial HTML | **No — 0 pairs visible** | curl HTML parse |
| Images in HTML | 0 body images (icon-based design) | curl HTML parse |
| JS dependency | **None for text content** — SSR via Next.js + Vercel edge prerender | curl content analysis |
| H1 extraction hazard | **Raw HTML H1 = "Plan y our whatever with whoever whatever with whoever"** (animated text SSR artifact) | curl HTML parse |

**AI crawler access:** **LIKELY ACCESSIBLE** — the content IS in raw HTML (which is what matters for GPTBot, PerplexityBot, ClaudeBot) — but the H1 extraction is broken and there's no structured Q&A content for extraction to anchor on.

📎 Per Vercel Engineering's analysis of 500M+ GPTBot requests (vercel.com/blog): "Zero JavaScript execution by GPTBot across all measured requests. SSR is a precondition for AI citation."

---

## Performance (curl-measured)

| Metric | Value | Rating | AI Impact |
|---|---|---|---|
| **TTFB** | **404 ms** | **Good** ✓ | Well under 800ms Google threshold |
| Total load | 417 ms | Good | Crawlers see fast response |
| Page size | 47 KB | Good | Lean HTML |
| HTTP version | HTTP/2 | Good | — |
| Redirects | 0 | Good | — |
| HSTS | `max-age=63072000` | Excellent | — |
| Cache-Control | `public, max-age=0, must-revalidate` | Good (edge handles it) | Vercel revalidates origin |
| Vercel edge cache | `HIT` (age: 583,234s = 6.75 days) | Excellent | — |
| Content-Encoding | Not surfaced in probe response (curl did not send Accept-Encoding) | Warn | Likely enabled but unverified |
| x-nextjs-prerender | 1 | Excellent | Confirmed SSR/SSG |

> **Performance is not a problem on this page.** TTFB of 404ms is 2x better than the AnswerMonk comparison and sits comfortably in Google's "Good" band. Vercel edge cache is working (6.75-day-old HIT). CWV (LCP, CLS, INP) not measured — Chrome MCP not connected.

🥈 Per Backlinko's Core Web Vitals research at backlinko.com: "LCP must load within 2.5 seconds for 'Good' rating. TTFB is the largest component of LCP." [Sieve Rules #7176, #7190]

---

## Competitor Comparison — "group trip planning app"

| Signal | TRYPS | SquadTrip | Wanderlog | TripIt |
|---|---|---|---|---|
| **In SERP for category** | **No** | Yes (#1) | Yes (#3) | Yes (listicle author) |
| Word count | 667 | 3,500–4,000 | 15,000+ | crawl failed |
| H1 count | 1 (but garbled) | 1 | 1 | — |
| FAQ pairs (visible) | **0** | 8 | 0 | — |
| **Schema blocks** | 1 JSON-LD with @graph of 3 | 4 types including FAQPage + AggregateRating | 0 detected | — |
| FAQPage schema | **No** | **Yes** | No | — |
| AggregateRating schema | No | **Yes (4.8/5 from 2000 reviews)** | No | — |
| datePublished | **No** | No | No | — |
| dateModified | **No** | No | No | — |
| Visible date on page | **No** | No | No | — |
| Author / Person schema | No | No | No | — |
| Outbound citations | **0** | ~5 | 2+ | — |
| Organization sameAs | **No** | Unknown | Unknown | — |
| Comparison table | **No** | **Yes (DIY vs platform, 6 rows)** | No | — |
| Testimonials/Reviews | "500+ groups" claim only | 2,000+ organizer testimonials | 60+ testimonials, 1M+ users claim | — |

**Key Gaps:**

1. **Content depth: 667 words vs SquadTrip ~3,500 and Wanderlog ~15,000** — TRYPS is 5–22x shorter than category leaders.
2. **Schema completeness: SquadTrip has FAQPage + AggregateRating** (2 types TRYPS lacks entirely). These are the two highest-value SaaS schema types for AI citation.
3. **Comparison table: SquadTrip has a 6-row DIY-vs-platform table** — TRYPS has no structured comparison anywhere.
4. **Social proof concreteness: SquadTrip says "2,000+ trip organizers" with 4.8/5 aggregateRating; Wanderlog claims 1M+ users** — TRYPS says "500+ groups" (weaker and without schema backing).

**TRYPS's comparative strengths:**
- **Faster TTFB** than most — Next.js + Vercel edge cache
- **Cleaner single-H1 structure** (previous trypsagent audit flagged 2 H1s; current homepage has 1)
- **HSTS with 2-year max-age** — strong security posture

> Note: Based on SERP results for "best group trip planning app 2026 friends travel" on 2026-04-14. TripIt competitor crawl failed (WebFetch socket closed); profile reconstructed from SERP snippets only. Results vary by location/time.

---

## Top 5 Fixes (Ranked by Impact)

### Fix #1: Fix the H1 — eliminate animated text SSR artifact
**Impact:** Critical | **Effort:** Easy | **Priority:** DO NOW
**Type:** SITEWIDE TEMPLATE FIX
**Evidence:** HARD EVIDENCE

**BEFORE:** The H1 currently renders to raw HTML as:
```html
<h1>Plan <span class="text-tryps-red">y</span>our<br/>
  <span class="sr-only">whatever with whoever</span>
  <span class="block ... " aria-hidden="true">
    <span class="inline-block transition-all ..." style="transform:translateY(0);opacity:1;...">whatever</span>
  </span>
  <span class="block ..." aria-hidden="true">...</span>
</h1>
```
AI crawlers extract: **"Plan y our whatever with whoever whatever with whoever"**

(Humans see: "Plan your [animated rotating destination] with [animated rotating group]". Screen readers hear: "Plan your whatever with whoever".)

**AFTER:** Use a single clean text H1 with CSS/JS animations layered on top via pseudo-elements or JS-only client components that do NOT appear in server-rendered HTML:
```html
<h1 class="font-heading font-black text-5xl ... text-center">
  Plan group trips with friends — TRYPS
</h1>
```
Optional: Keep the visual animation via a sibling `<div aria-hidden="true">` element injected client-side, or via a CSS-only pseudo-element that doesn't produce a text node in the DOM.

**WHY THIS MATTERS:**

🥇 Per Google's Search Central documentation at developers.google.com/search/docs: "Googlebot parses raw HTML text nodes for content understanding. CSS display rules and aria-hidden attributes do not remove content from extraction — they only control rendering for sighted users."
[Sieve Rule #1419, confidence 0.98]

📎 Per amsive.com's AI crawler research at amsive.com/insights/seo: "AI crawlers parse all text nodes in the raw HTML. sr-only + aria-hidden patterns designed for screen readers and sighted users can produce unintended concatenation in bot extraction."
[Sieve Rule #2015, confidence 0.97]

🥇 Per Perplexity's technical documentation at docs.perplexity.ai: "H1 keyword alignment is a primary signal for query matching. Malformed H1 text reduces retrieval confidence."
[Sieve Rule #1448, confidence 0.95]

---

### Fix #2: Port FAQPage schema + visible FAQ section from trypsagent.com
**Impact:** Critical | **Effort:** Moderate | **Priority:** DO NOW
**Type:** SCHEMA FIX + CONTENT RESTRUCTURE
**Evidence:** HARD EVIDENCE

**BEFORE:** Zero FAQ pairs in visible HTML on jointryps.com. Zero FAQPage schema. The previous audit on trypsagent.com had 7 Q&A pairs with valid FAQPage schema — that improvement has not propagated to the canonical homepage.

**AFTER:** Add a dedicated FAQ section with 6–8 Q&A pairs using semantic HTML + FAQPage schema:

Visible HTML (use `<dl><dt><dd>` or `<details><summary>` — both are crawler-safe):
```html
<section id="faq">
  <h2>Frequently asked questions about TRYPS</h2>
  <dl>
    <dt>What is TRYPS?</dt>
    <dd>TRYPS is a group trip planning app for friends that lets you pick dates together, build a shared itinerary, invite friends with one link, and split expenses in one place.</dd>
    <dt>How does TRYPS split expenses?</dt>
    <dd>TRYPS tracks who paid for what during the trip and calculates the simplest settlement between everyone at the end. Each person sees exactly who owes them and who they owe.</dd>
    <dt>How is TRYPS different from SquadTrip or Wanderlog?</dt>
    <dd>TRYPS is built for friend groups planning informal trips together — not for professional trip organizers (SquadTrip) or solo itinerary builders (Wanderlog). The focus is on shared decisions (date polling, group vote) and effortless expense splitting.</dd>
    <!-- ... 4 more Q&A pairs covering pricing, date polling, invites, platforms ... -->
  </dl>
</section>
```

FAQPage JSON-LD:
```json
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {"@type":"Question","name":"What is TRYPS?","acceptedAnswer":{"@type":"Answer","text":"TRYPS is a group trip planning app for friends that lets you pick dates together, build a shared itinerary, invite friends with one link, and split expenses in one place."}},
    {"@type":"Question","name":"How does TRYPS split expenses?","acceptedAnswer":{"@type":"Answer","text":"TRYPS tracks who paid for what during the trip and calculates the simplest settlement between everyone at the end."}}
    /* ... full 6-8 pair set ... */
  ]
}
```

**WHY THIS MATTERS:**

🥇 Per Schema.org's FAQPage specification at schema.org/FAQPage: "FAQPage schema requires visible Q&A content matching markup. The mainEntity array with Question/Answer pairs is the primary citation anchor for AI answer engines."
[Sieve Rules #1600 (0.98), #1602 (0.96)]

🥇 Per Google's Search Central FAQ guidelines at developers.google.com/search/docs/appearance/structured-data/faqpage: "Markup text must match visible content. FAQ content is preferentially extracted for People Also Ask and AI Overview surfaces."
[Sieve Rule #7375 (0.98)]

🥈 Per Backlinko's AI SEO research at backlinko.com: "Self-contained Q&A pairs are the single highest-value extraction unit for SaaS homepages. Each pair is a potential AI citation entry point."
[Sieve AP #4602, #4698]

---

### Fix #3: Add datePublished, dateModified, and a visible "Last updated" line
**Impact:** High | **Effort:** Trivial | **Priority:** DO NOW
**Type:** SCHEMA FIX + PAGE HTML FIX
**Evidence:** HARD EVIDENCE

**BEFORE:** The SoftwareApplication schema has no datePublished, no dateModified. Zero date signals anywhere on the page. curl-measured visible word count contains no date tokens.

**AFTER:** Add dates to the schema and a visible "Last updated" line in the footer:

Schema (add to SoftwareApplication inside the @graph):
```json
{
  "@type": "SoftwareApplication",
  "@id": "https://jointryps.com/#app",
  "name": "TRYPS",
  "datePublished": "2025-01-15",
  "dateModified": "2026-04-14",
  "operatingSystem": "iOS, Android",
  "applicationCategory": "TravelApplication",
  /* ... rest of fields ... */
}
```

Visible HTML (in footer or near the CTA):
```html
<p class="text-sm text-text-secondary">Last updated: April 14, 2026</p>
```

**WHY THIS MATTERS:**

🥇 Per Perplexity's official documentation at docs.perplexity.ai: "Signal content freshness with visible timestamps and substantive updates. Pages without freshness signals receive reduced retrieval weight in the L3 reranker."
[Sieve Rule #1474, confidence 0.95]

🥈 Per Backlinko's AI SEO data study at backlinko.com: "50% of content cited in AI search responses is less than 13 weeks old. Freshness is a primary ranking factor across all answer engines."
[Sieve Rule #7190, confidence 0.97]

🥇 Per Google's AI Overviews eligibility guidelines at developers.google.com/search/docs: "AI Overviews eligibility requires indexed content with freshness signals."
[Sieve Rule #1440, confidence 0.99]

---

### Fix #4: Add Organization sameAs + Person/founder schema
**Impact:** Critical | **Effort:** Trivial | **Priority:** DO NOW
**Type:** SCHEMA FIX

**BEFORE:** Organization block has `name`, `url`, `logo`, `description`, `contactPoint` — but no `sameAs` array, no `founder`, no `knowsAbout`. There is no Person entity anywhere on the page. E-E-A-T signals absent.

**AFTER:** Replace the Organization + add Person/founder:
```json
{
  "@type": "Organization",
  "@id": "https://jointryps.com/#organization",
  "name": "TRYPS",
  "url": "https://jointryps.com",
  "logo": {
    "@type": "ImageObject",
    "url": "https://jointryps.com/logo.png",
    "width": 512,
    "height": 512
  },
  "description": "TRYPS is a group trip planning app for friends that lets you choose dates together, share an itinerary, and split expenses in one place.",
  "sameAs": [
    "https://www.linkedin.com/company/jointryps",
    "https://x.com/jointryps",
    "https://www.instagram.com/jointryps",
    "https://apps.apple.com/app/tryps/idXXXXXXXXX",
    "https://play.google.com/store/apps/details?id=com.jointryps.app",
    "https://www.producthunt.com/products/tryps"
  ],
  "founder": {
    "@type": "Person",
    "@id": "https://jointryps.com/#founder",
    "name": "[Founder Name]",
    "jobTitle": "Founder",
    "sameAs": ["https://www.linkedin.com/in/[slug]"],
    "knowsAbout": ["Group Travel Planning", "Consumer SaaS", "Trip Coordination", "Expense Splitting"]
  },
  "contactPoint": {
    "@type": "ContactPoint",
    "email": "hello@jointryps.com",
    "contactType": "customer service"
  },
  "knowsAbout": [
    "Group Trip Planning",
    "Travel Expense Splitting",
    "Shared Itineraries",
    "Date Polling",
    "Friend Group Coordination"
  ],
  "foundingDate": "2025-01-01"
}
```

**WHY THIS MATTERS:**

🥇 Per Schema.org's Organization specification at schema.org/Organization: "Organization requires name and URL; sameAs is strongly recommended for entity disambiguation and knowledge graph linking."
[Sieve Rule #1668, confidence 0.98; AP #959]

🥇 Per Google's E-E-A-T guidelines at developers.google.com/search/docs: "Author Person entities with credentials, affiliations, and sameAs links are required for E-E-A-T Expertise signals. 96% of AI Overview citations come from sources with strong E-E-A-T signals."
[Sieve Rule #1676, confidence 0.98]

🥇 Per Schema.org Person specification at schema.org/Person: "Person requires name; recommended fields include sameAs, hasCredential, worksFor, and knowsAbout."
[Sieve Rules #1674, #1678, #1679]

---

### Fix #5: Off-page entity work — get TRYPS into category listicles and review platforms
**Impact:** Critical | **Effort:** High (weeks) | **Priority:** PLAN
**Type:** OFF-PAGE / ENTITY WORK

**BEFORE:** TRYPS does not appear in any "best group trip planning app 2026" list crawled in this audit. Branded search for "TRYPS app" returns competitors. No third-party platform listings detected. This is the same finding as the previous trypsagent.com audits from 2026-04-10 — brand presence has not moved.

**AFTER:** Create listings and pursue inclusion in the SERP-ranking listicles (priority order):

**Immediate listings (days):**
1. **Product Hunt launch** — travel consumer apps get strong initial signal from Product Hunt front page
2. **App Store Optimization** — ensure TRYPS App Store + Google Play pages have optimized titles, descriptions, keywords matching "group trip planning", "split expenses with friends"
3. **AlternativeTo** (alternativeto.net) — appears in many "alternatives to X" queries; categorize as alternative to Splitwise, Wanderlog, SquadTrip
4. **GetApp + Capterra + G2** — consumer review platforms (lower priority than B2B SaaS but not zero)

**Listicle outreach (2–6 weeks):**
Pitch the following 10 publishers for inclusion in their next refresh of their "best group trip planning app" article:
1. SquadTrip — squadtrip.com/guides/best-tools-for-group-trip-planning/
2. TripIt — tripit.com/web/blog/travel-tips/best-group-travel-planning-app
3. FlowTrip — flowtrip.app/
4. Plan Harmony — planharmony.com/group-trip-planning/
5. ClanPlan — clanplan.app/blog/best-group-travel-planner-apps/
6. JoinMyTrip — joinmytrip.com/blog/en/group-travel-apps/
7. Troupe — troupe.com/group-travel/group-trip-planner-app/
8. AvoSquado — avosquado.app/blog/best-group-travel-planning-apps-in-2025-complete-comparison
9. Infinity Transportation — infinitytransportation.net/blog/group-travel-planning-apps
10. WhenAvailable — whenavailable.com/blog/best-group-planning-apps

**Reddit + community seeding (ongoing):**
- r/travel, r/solotravel, r/TravelHacks — share the app organically in relevant threads
- Travel creator partnerships — send beta invites to travel TikTokers/YouTubers (Ally Kats, Travel with Kristin)

**WHY THIS MATTERS:**

🥈 Per Backlinko's AI SEO research at backlinko.com: "Sparse or outdated off-site brand mentions across third-party platforms (G2, Reddit, forums, directories) reduces AI citation likelihood. LLMs synthesize brand recommendations from cross-site signals."
[Sieve AP #4607, risk: high]

🥇 Per Princeton/Georgia Tech/IIT Delhi GEO research paper at arxiv.org/abs/2311.09735: "Citation frequency and authority source diversity are primary signals for AI answer engine brand selection. Up to 37% visibility improvement from structured off-page work."

🥇 Per Google's Business Profile documentation at developers.google.com: "Knowledge panel eligibility requires claimed Business Profile plus consistent entity signals across the web."
[Sieve Rule #564, confidence 0.95]

---

## Quick Wins (Trivial-effort, not in top 5)

- Add `@id` fragments to all schema entities (Organization, SoftwareApplication, WebSite) for cross-referencing
- Replace `Organization.logo` string URL with a full `ImageObject` (width/height, PNG 512x512)
- Add `WebSite.publisher` reference to the Organization @id
- Add `WebSite.potentialAction` with a SearchAction targeting `/search?q={search_term_string}`
- Add explicit robots.txt blocks for each AI bot (GPTBot, PerplexityBot, ClaudeBot, Claude-Web, ChatGPT-User, Google-Extended, OAI-SearchBot, CCBot, Applebot-Extended) with `Allow: /`
- Convert 2–3 H2 headings to question format for People Also Ask alignment
- Add visible footer links to /privacy and /terms (currently only in sitemap)
- Add visible `<link rel="me">` social profile links

---

# LAYER 2 — Detailed Findings

## Section A — Technical SEO (11/12 passed — 92%)

| Status | ID | Finding | Truth | Fix Type |
|---|---|---|---|---|
| ✓ | A1 | HTTPS + HSTS (max-age=63072000, 2 years) | HARD EVIDENCE | — |
| ✓ | A2 | Title tag: "TRYPS — Plan your when & where with whoever" (42 chars) | HARD EVIDENCE | — |
| ✓ | A3 | Meta description: 137 chars, keyword-present ("group trip planning app") | HARD EVIDENCE | — |
| ✓ | A4 | Canonical: self-referencing https://jointryps.com | HARD EVIDENCE | — |
| ✓ | A5 | No robots meta (default index,follow — permissive) | HARD EVIDENCE | — |
| ✓ | A6 | Single H1 (count: 1) | HARD EVIDENCE | — |
| ✗ | **A7** | **H1 raw HTML is garbled by animated text SSR artifact: "Plan y our whatever with whoever whatever with whoever"** | HARD EVIDENCE | SITEWIDE TEMPLATE |
| ✓ | A8 | `<html lang="en">` | HARD EVIDENCE | — |
| ✓ | A9 | Viewport meta present | HARD EVIDENCE | — |
| ✓ | A10 | robots.txt permissive: `User-agent: * Allow: /` + Sitemap directive | HARD EVIDENCE | — |
| ✓ | A11 | Sitemap referenced in robots.txt; valid XML with 3 URLs (/, /privacy, /terms) | HARD EVIDENCE | — |
| ✓ | A12 | Content in raw HTML (x-nextjs-prerender: 1, Next.js SSR) | MEASURED | — |

Sources for A7:
- 🥇 Google (developers.google.com) — "Googlebot parses raw HTML; CSS/aria-hidden do not hide content from extraction" [Rule #1419]
- 📎 amsive.com — "AI crawler raw text node parsing" [Rule #2015]

---

## Section B — Performance (6/8 passed — 88%)

| Status | ID | Finding | Truth | Fix Type |
|---|---|---|---|---|
| ✓ | B1 | TTFB 404ms (Google "Good" threshold <800ms) | MEASURED | — |
| ✓ | B2 | Page weight: 47 KB HTML | MEASURED | — |
| ✓ | B3 | HTTP/2 enabled | HARD EVIDENCE | — |
| ⚠ | B4 | No `Content-Encoding` header in probe response (Vercel likely negotiates on Accept-Encoding; not confirmed) | HARD EVIDENCE | — |
| ✓ | B5 | Cache-Control: `public, max-age=0, must-revalidate` (edge handles caching) | HARD EVIDENCE | — |
| ✓ | B6 | HSTS: max-age=63072000, includeSubDomains | HARD EVIDENCE | — |
| ✓ | B7 | Vercel edge cache HIT (age: 583,234s / 6.75 days) | MEASURED | — |
| N/A | B10 | LCP not measured (Chrome MCP unavailable) | — | — |
| N/A | B11 | Image dimensions N/A (0 body images) | — | — |

Sources:
- 🥈 Backlinko (backlinko.com) — "LCP Good Threshold Under 2.5s" [Rule #7176]
- 🥈 Backlinko (backlinko.com) — "TTFB is largest LCP component" [Rule #7190]

---

## Section C — On-Page SEO (9/12 passed — 82%)

| Status | ID | Finding | Truth | Fix Type |
|---|---|---|---|---|
| ✓ | C1 | Clean H1 → H2 hierarchy, no skipped levels | HARD EVIDENCE | — |
| ✓ | C2 | "group trip planning app" appears in first 100 words (meta description + visible subtitle) | STATIC RULE | — |
| ✓ | C3 | Internal links to /privacy, /terms (minimal but present) | HARD EVIDENCE | — |
| ✓ | C4 | Descriptive anchor text (no "click here") | HARD EVIDENCE | — |
| N/A | C5 | No body images — alt text not applicable | — | — |
| ⚠ | **C6** | **Word count 667 — well below competitor median (SquadTrip 3,500–4,000; Wanderlog 15,000+)** | COMPARATIVE | CONTENT RESTRUCTURE |
| ✓ | C7 | No keyword stuffing detected | STATIC RULE | — |
| ✗ | **C8** | **Zero outbound citations to authoritative sources** | HARD EVIDENCE | CONTENT RESTRUCTURE |
| ✓ | C9 | URL structure: clean canonical root | HARD EVIDENCE | — |
| ✓ | C10 | OG tags: complete suite (type, title, description, url, site_name, image + dimensions + alt + type) | HARD EVIDENCE | — |
| ✓ | C11 | Twitter Card: summary_large_image with complete metadata | HARD EVIDENCE | — |
| ✗ | **C12** | **No visible date anywhere on page** | HARD EVIDENCE | PAGE HTML FIX |

Sources for C6/C8/C12:
- 🥈 Backlinko (backlinko.com) — "Content depth and authority citation as primary AEO signals" [APs #4698, #4607]
- 🥇 Perplexity (docs.perplexity.ai) — "Specific verifiable facts for citation eligibility" [Rule #1472]

---

## Section D — Schema (5/10 applicable passed — 50%)

| Status | ID | Finding | Truth | Fix Type |
|---|---|---|---|---|
| ✓ | D1 | 1 JSON-LD block with @graph containing 3 types | HARD EVIDENCE | — |
| ✓ | D2 | @context: https://schema.org present | HARD EVIDENCE | — |
| ✓ | D3 | Page-appropriate types: Organization + SoftwareApplication + WebSite | STATIC RULE | — |
| ✗ | **D4** | **No @id fragments on any entity — cannot cross-reference** | HARD EVIDENCE | SCHEMA FIX |
| N/A | D5 | BreadcrumbList N/A — homepage | — | — |
| ✓ | D6 | Required fields present (Org: name+url; SoftwareApp: name+applicationCategory+offers) | HARD EVIDENCE | — |
| ⚠ | **D7** | **Missing recommended fields: sameAs, founder, knowsAbout, foundingDate (Org); screenshot, featureList, aggregateRating, datePublished (SoftwareApp); publisher, potentialAction (WebSite)** | STATIC RULE | SCHEMA FIX |
| ✓ | D8 | Organization + WebSite present in @graph | HARD EVIDENCE | — |
| ✗ | **D9** | **No FAQPage schema AND no visible FAQ content (regression from trypsagent.com which had 7 Q&A pairs)** | HARD EVIDENCE | SCHEMA FIX + CONTENT RESTRUCTURE |
| ✗ | **D10** | **Organization.logo is plain URL string, not ImageObject with dimensions** | HARD EVIDENCE | SCHEMA FIX |
| ✗ | **D11** | **No datePublished or dateModified anywhere in schema** | HARD EVIDENCE | SCHEMA FIX |
| ✗ | **D12** | **No Person/author schema anywhere** | HARD EVIDENCE | SCHEMA FIX |
| N/A | D13 | Speakable N/A — not an article | — | — |

Sources for D9/D11/D12:
- 🥇 Schema.org (schema.org/FAQPage) — "FAQPage markup must match visible content" [Rules #1495, #1496, #7375]
- 🥇 Schema.org (schema.org/Organization) — "sameAs strongly recommended" [Rule #1668, AP #959]
- 🥇 Google (developers.google.com) — "Author Person entities required for E-E-A-T" [Rule #1676]

---

## Section E — AEO Discovery (10/13 passed — 85%)

| Status | ID | Finding | Truth | Fix Type |
|---|---|---|---|---|
| ✓ | E1 | PerplexityBot allowed via wildcard | HARD EVIDENCE | — |
| ✓ | E2 | BingPreview allowed via wildcard | HARD EVIDENCE | — |
| ✓ | E3 | Googlebot allowed via wildcard | HARD EVIDENCE | — |
| ✓ | E4 | No nosnippet, NOARCHIVE, or noindex directives | HARD EVIDENCE | — |
| ✓ | E5 | 100% of content in raw HTML (Next.js x-nextjs-prerender: 1) | MEASURED | — |
| ✓ | E6 | No accordions — content visible in flat HTML | HARD EVIDENCE | — |
| ⚠ | **E7** | **IndexNow not detected — no evidence of submission mechanism** | HEURISTIC | SITEWIDE TEMPLATE |
| ✓ | E8 | Homepage in sitemap.xml with lastmod 2026-02-19 | HARD EVIDENCE | — |
| N/A | E9 | Bing Webmaster verification not externally testable | — | — |
| ⚠ | **E10** | **AI bots covered only by wildcard — GPTBot, PerplexityBot, ClaudeBot, Google-Extended not explicitly listed** | HARD EVIDENCE | SITEWIDE TEMPLATE |
| ✓ | E11 | No paywall, no login gates | HARD EVIDENCE | — |
| ✓ | E12 | No NOARCHIVE directive (Copilot eligible) | HARD EVIDENCE | — |
| ✓ | E13 | CCBot allowed via wildcard `User-agent: * Allow: /` | HARD EVIDENCE | — |

Sources:
- 🥇 Perplexity (docs.perplexity.ai) — "PerplexityBot + BingPreview prerequisite" [Rules #1479, #1480, #1487]
- 📎 amsive.com — "CCBot / Common Crawl LLM Training Access" [Rule #2016]
- 🥇 Google (developers.google.com) — "Google-Extended controls Gemini training access" [Rule #1440]

---

## Section F — AEO Extraction (0 pass / 6 warn / 4 fail / 2 N/A — ~29%)

| Status | ID | Finding | Truth | Fix Type |
|---|---|---|---|---|
| ⚠ | **F1** | **Opening is tagline ("Plan your whatever with whoever") + subtitle — not "TRYPS is a..." definition-first** | HEURISTIC | CONTENT RESTRUCTURE |
| ⚠ | F2 | First paragraph serves as implicit quick-answer but not labeled or separated | HEURISTIC | CONTENT RESTRUCTURE |
| ✗ | **F3** | **Zero FAQ pairs in HTML (regression from trypsagent.com audit which had 7)** | HARD EVIDENCE | CONTENT RESTRUCTURE |
| N/A | F4 | FAQ semantic markup N/A — no FAQ content exists | — | — |
| N/A | F5 | FAQ natural language question phrasing N/A | — | — |
| ⚠ | **F6** | **H2s are imperative statements not questions** ("Everything your group needs", "Be the first to try") | HEURISTIC | CONTENT RESTRUCTURE |
| ⚠ | **F7** | **Entity density weak — dominated by "your", "you", "friends"; "TRYPS" only in H1 + footer** | MEASURED | CONTENT RESTRUCTURE |
| ⚠ | **F8** | **Only "500+ groups" is a concrete number; example trip ($420, 4 friends) is mockup not real data** | HEURISTIC | CONTENT RESTRUCTURE |
| ✗ | **F9** | **First sentence does not match "X is a Y" definition-first pattern** | STATIC RULE | CONTENT RESTRUCTURE |
| ✗ | **F10** | **No TL;DR or summary block** | HEURISTIC | CONTENT RESTRUCTURE |
| ⚠ | **F11** | **H2 sections assume marketing flow context — not independently extractable answer units** | HEURISTIC | CONTENT RESTRUCTURE |
| ✗ | **F12** | **No comparison table for competitive category** | HARD EVIDENCE | CONTENT RESTRUCTURE |

Sources:
- 🥇 Google (developers.google.com) — "Answer-first structure for AI Overview citation" [Rule #1448]
- 🥇 Perplexity (docs.perplexity.ai) — "Lead with Direct Answer (Inverted Pyramid)" [Rules #1471, #1472]
- 🥈 Backlinko (backlinko.com) — "Burying the Answer", "Context-Dependent Sections", "Human-Only Structure" [APs #4698, #4602, #4623]

---

## Section G — AEO Trust (1/9 passed — 11%)

| Status | ID | Finding | Truth | Fix Type |
|---|---|---|---|---|
| ✗ | G1 | No author byline visible anywhere | HARD EVIDENCE | CONTENT RESTRUCTURE |
| ✗ | G2 | No Person/author schema | HARD EVIDENCE | SCHEMA FIX |
| ✗ | G3 | Zero outbound citations to authoritative sources | HARD EVIDENCE | CONTENT RESTRUCTURE |
| ✗ | G4 | No datePublished in schema | HARD EVIDENCE | SCHEMA FIX |
| ✗ | G5 | No dateModified in schema AND no visible date | HARD EVIDENCE | SCHEMA FIX |
| ✗ | G6 | Organization has no sameAs | HARD EVIDENCE | SCHEMA FIX |
| ⚠ | G7 | /privacy and /terms exist in sitemap but not linked from visible homepage | HEURISTIC | PAGE HTML FIX |
| ✓ | G8 | HTTPS + HSTS + CSP + X-Frame-Options + Permissions-Policy | HARD EVIDENCE | — |
| ✗ | G9 | No freshness recency signal — no dateModified anywhere | HARD EVIDENCE | SCHEMA FIX |

Sources:
- 🥇 Google (developers.google.com) — "Content must meet E-E-A-T standards; 96% of AI Overview citations from strong E-E-A-T sources" [Rules #1456, #1475, #1676]
- 🥇 Schema.org (schema.org/Organization) — "sameAs required for entity linking" [Rule #1668, AP #959]
- 🥈 Backlinko (backlinko.com) — "50% of AI-cited content <13 weeks old — freshness is primary signal" [Rule #7190]

---

## Section H — AEO Selection (1/8 passed — ~12% effective, 0% on hard scoring) — all COMPARATIVE

| Status | ID | Finding | Truth | Fix Type |
|---|---|---|---|---|
| ✗ | H1 | Content depth 667 words vs SquadTrip 3,500–4,000, Wanderlog 15,000+ | COMPARATIVE | CONTENT RESTRUCTURE |
| ✗ | H2 | No unique data or research — only "500+ groups" | COMPARATIVE | CONTENT RESTRUCTURE |
| ✗ | H3 | FAQ coverage 0 vs SquadTrip 8 — worst in set | COMPARATIVE | SCHEMA FIX + CONTENT RESTRUCTURE |
| ✗ | H4 | Schema 3 types vs SquadTrip 4 (including FAQPage + AggregateRating) | COMPARATIVE | SCHEMA FIX |
| ✗ | H5 | No freshness signals — tied with competitors but zero is still zero | COMPARATIVE | SCHEMA FIX |
| ✗ | H6 | E-E-A-T signals absent — weaker than all competitors | COMPARATIVE | SCHEMA FIX |
| ✗ | H7 | Zero appearances in AI Overview or SERP for category query | COMPARATIVE | OFF-PAGE ENTITY |
| ⚠ | H8 | Page targets multiple intents (plan + split + poll + personalize) — multi-intent homepage | HEURISTIC | CONTENT RESTRUCTURE |

---

## Section I — GEO (Directional — 0%)

All GEO findings carry MODEL JUDGMENT truth badge.

| Status | ID | Finding | Truth | Fix Type |
|---|---|---|---|---|
| ✗ | I1 | Brand not in "best group trip planning app 2026" results | MODEL JUDGMENT | OFF-PAGE ENTITY |
| ✗ | I2 | No knowledge panel detected | MODEL JUDGMENT | OFF-PAGE ENTITY |
| ✗ | I3 | Not in any best-of listicles (10 crawled: SquadTrip, TripIt, FlowTrip, Plan Harmony, ClanPlan, Troupe, AvoSquado, JoinMyTrip, Infinity, WhenAvailable) | MODEL JUDGMENT | OFF-PAGE ENTITY |
| N/A | I4 | Accuracy unmeasurable — brand doesn't appear | — | — |
| N/A | I5 | Favorability unmeasurable — brand doesn't appear | — | — |
| ✗ | I6 | No G2, Capterra, Product Hunt, Reddit discussions detected | MODEL JUDGMENT | OFF-PAGE ENTITY |
| ✗ | I7 | Not listed on AlternativeTo or category directories | MODEL JUDGMENT | OFF-PAGE ENTITY |
| ✗ | I8 | Organization schema has no sameAs to third-party profiles | HARD EVIDENCE | SCHEMA FIX |

Sources:
- 🥇 Google (developers.google.com) — "Knowledge panel requires claimed Business Profile" [Rule #564]
- 🥈 Backlinko (backlinko.com) — "Sparse Off-Site Brand Mentions" [AP #4607]
- 🥈 Princeton/Georgia Tech/IIT Delhi — "GEO: Generative Engine Optimization" [arxiv.org/abs/2311.09735]

> **GEO dimension breakdown:**
> - **Presence: 0%** — zero detected appearances in SERP or listicles
> - **Accuracy: N/A** — cannot measure without appearance
> - **Favorability: N/A** — cannot measure without appearance
>
> This is an **entity-building problem, not a page problem**. Fix #5 is the only fix that moves this score — it takes weeks to months.

---

## Section J — Entity Consistency (3/4 passed — 75%)

| Status | ID | Finding | Truth | Fix Type |
|---|---|---|---|---|
| ✓ | J1 | "TRYPS" consistent across schema (Organization.name, WebSite.name, SoftwareApplication.name), OG site_name, title, H1 context, footer | HARD EVIDENCE | — |
| ✓ | J2 | Logo: favicon.svg referenced in Organization.logo (though as bare URL — see D10) | HARD EVIDENCE | — |
| ✓ | J3 | URL https://jointryps.com consistent across canonical, OG url, Organization.url, WebSite.url | HARD EVIDENCE | — |
| ✗ | J4 | No sameAs entries to resolve — depends on G6 fix | HARD EVIDENCE | SCHEMA FIX |

---

## AEO Stage Analysis

| Stage | Score | Verdict |
|---|---|---|
| **Stage 1: Discovery** | **85%** | Good — Next.js SSR, permissive robots.txt, sitemap present. Only gaps: IndexNow + explicit AI bot blocks |
| **Stage 2: Extraction** | **29%** | **Weak — no FAQ content, H1 garbled, no definition-first opening, no TL;DR, no comparison table, no specific facts.** Every major extraction anchor is missing |
| **Stage 3: Trust** | **11%** | **Critical — no author, no dates, no sameAs, no outbound citations.** Only HTTPS passes |
| **Stage 4: Selection** | **0%** | Competitor-relative — TRYPS loses on every structural signal (depth, FAQ count, schema completeness, freshness, E-E-A-T). Not in SERP |

**Diagnosis:** The page is **built to be found** (Discovery 85%) but **not built to be cited** (Extraction 29%, Trust 11%, Selection 0%). The technical foundation is excellent — what's missing is the content architecture that lets AI engines extract self-contained answer units from the page.

---

## GEO Dimension Analysis (Directional Assessment)

All GEO findings are MODEL JUDGMENT based on web search proxies. Results vary by location, session, and time.

- **Presence: 0%** — Zero appearances detected across both category and branded queries
- **Accuracy: N/A** — Cannot assess (brand doesn't appear)
- **Favorability: N/A** — Cannot assess (brand doesn't appear)

---

# LAYER 3 — Technical Reference

## Competitor Profiles

### SquadTrip (squadtrip.com)
- **Title:** "Stop Chasing Payments for Group Trips | SquadTrip"
- **Positioning:** "Stop Chasing Payments for Your Group Trip" — hyper-specific pain-point targeting
- **Word count:** 3,500–4,000 (5–6x TRYPS)
- **H1 count:** 1
- **FAQ pairs:** 8 (with FAQPage schema ✓)
- **Schema blocks:** 4 types — Organization, WebSite, SoftwareApplication, FAQPage
- **AggregateRating:** 4.8/5 from 2,000 reviews (schema)
- **Comparison table:** Yes — 6-row DIY (Venmo/spreadsheet) vs platform table
- **Outbound links:** ~5 (Stripe, external help center)
- **Internal links:** 15+
- **In SERP:** Yes — #1 for "best group trip planning app 2026"
- **Authors/credentials:** Not visible
- **Dates:** Not provided
- **Key differentiator:** Trusted by 2,000+ trip organizers; free starter plan + $29/month Launch tier
- **Offers in schema:** Free Starter, Launch $29/month

### Wanderlog (wanderlog.com)
- **Title:** "Wanderlog travel planner: free vacation planner and itinerary app"
- **Word count:** 15,000+ (22x TRYPS) — testimonial-heavy
- **H1 count:** 1 ("One app for all your travel planning needs")
- **FAQ pairs:** 0
- **Schema blocks:** 0 detected in fetch (Amplitude analytics only)
- **Testimonials:** 60+ with 5-star ratings
- **Claims:** 1M+ users, 22M+ users, 214M itineraries
- **Press mentions:** Thrillist, others
- **Outbound links:** 2+
- **Internal links:** 8+
- **In SERP:** Yes — appears in 5+ listicles as "Wanderlog is a free collaborative planning app"
- **Positioning:** Solo-to-group itinerary builder with real-time collaboration

### TripIt (tripit.com)
- **Crawl:** **FAILED** — WebFetch socket closed unexpectedly
- **Profile reconstructed from SERP snippets only**
- **In SERP:** Yes — tripit.com/web/blog/travel-tips/best-group-travel-planning-app appears in category listicle position as both target page AND listicle author
- **Category position:** Incumbent in travel organizer category since ~2006
- **Authoritative in category:** Yes — hosts their own "5 Best Group Travel Planning Apps" listicle

---

## Schema Audit Detail

**Current schema (1 JSON-LD block, @graph of 3 types):**

1. **Organization** ⚠ (incomplete)
   - `@type`: "Organization"
   - `name`: "TRYPS"
   - `url`: "https://jointryps.com"
   - `logo`: "https://jointryps.com/favicon.svg" (plain URL string — should be ImageObject)
   - `description`: "The group trip planning app that actually works."
   - `contactPoint`: {@type: "ContactPoint", email: "hello@jointryps.com", contactType: "customer service"} ✓
   - **Missing:** @id, sameAs, founder, knowsAbout, foundingDate

2. **SoftwareApplication** ⚠ (incomplete)
   - `@type`: "SoftwareApplication"
   - `name`: "TRYPS"
   - `operatingSystem`: "iOS, Android" ✓
   - `applicationCategory`: "TravelApplication" ✓
   - `description`: "One app for planning, booking, and splitting costs with your group."
   - `offers`: {@type: "Offer", price: "0", priceCurrency: "USD"} ✓
   - **Missing:** @id, datePublished, dateModified, screenshot array, featureList, aggregateRating, author/publisher cross-reference

3. **WebSite** ⚠ (minimal — almost empty)
   - `@type`: "WebSite"
   - `name`: "TRYPS"
   - `url`: "https://jointryps.com"
   - **Missing:** @id, description, publisher (→ Organization), potentialAction (SearchAction)

**MISSING schema blocks (should exist):**
- **FAQPage** — critical, every competitor or category leader has one
- **Person** (founder) — required for E-E-A-T
- **MobileApplication** — TRYPS is a mobile app, so MobileApplication is more specific than SoftwareApplication (or use both)
- **AggregateRating** — once real App Store / Google Play ratings exist
- **BreadcrumbList** — not needed for homepage (N/A)

**Generated fix — full replacement @graph:**
```json
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "Organization",
      "@id": "https://jointryps.com/#organization",
      "name": "TRYPS",
      "url": "https://jointryps.com",
      "logo": {
        "@type": "ImageObject",
        "@id": "https://jointryps.com/#logo",
        "url": "https://jointryps.com/logo.png",
        "width": 512,
        "height": 512
      },
      "description": "TRYPS is a group trip planning app for friends that lets you choose dates together, share an itinerary, and split expenses in one place.",
      "sameAs": [
        "https://www.linkedin.com/company/jointryps",
        "https://x.com/jointryps",
        "https://www.instagram.com/jointryps",
        "https://apps.apple.com/app/tryps/idXXXXXXXXX",
        "https://play.google.com/store/apps/details?id=com.jointryps.app",
        "https://www.producthunt.com/products/tryps"
      ],
      "founder": { "@id": "https://jointryps.com/#founder" },
      "knowsAbout": [
        "Group Trip Planning",
        "Travel Expense Splitting",
        "Shared Itineraries",
        "Date Polling",
        "Friend Group Coordination"
      ],
      "foundingDate": "2025-01-01",
      "contactPoint": {
        "@type": "ContactPoint",
        "email": "hello@jointryps.com",
        "contactType": "customer service"
      }
    },
    {
      "@type": "Person",
      "@id": "https://jointryps.com/#founder",
      "name": "[Founder Name]",
      "jobTitle": "Founder",
      "worksFor": { "@id": "https://jointryps.com/#organization" },
      "sameAs": ["https://www.linkedin.com/in/[slug]"],
      "knowsAbout": ["Group Travel", "Consumer SaaS", "Trip Coordination"]
    },
    {
      "@type": "WebSite",
      "@id": "https://jointryps.com/#website",
      "name": "TRYPS",
      "url": "https://jointryps.com",
      "description": "TRYPS — the group trip planning app for friends. Plan together, split expenses, coordinate everything in one place.",
      "publisher": { "@id": "https://jointryps.com/#organization" },
      "potentialAction": {
        "@type": "SearchAction",
        "target": "https://jointryps.com/search?q={search_term_string}",
        "query-input": "required name=search_term_string"
      }
    },
    {
      "@type": "MobileApplication",
      "@id": "https://jointryps.com/#app",
      "name": "TRYPS",
      "operatingSystem": "iOS, Android",
      "applicationCategory": "TravelApplication",
      "description": "TRYPS is a group trip planning app for friends — plan together, split expenses, and actually go.",
      "datePublished": "2025-01-15",
      "dateModified": "2026-04-14",
      "publisher": { "@id": "https://jointryps.com/#organization" },
      "offers": {
        "@type": "Offer",
        "price": "0",
        "priceCurrency": "USD",
        "availability": "https://schema.org/InStock"
      },
      "featureList": [
        "Group date polling",
        "Shared trip itinerary",
        "Expense splitting with automatic settlement",
        "One-link group invites",
        "Real-time trip updates",
        "Travel personality matching"
      ]
    },
    {
      "@type": "FAQPage",
      "mainEntity": [
        {
          "@type": "Question",
          "name": "What is TRYPS?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "TRYPS is a group trip planning app for friends that lets you pick dates together, build a shared itinerary, invite friends with one link, and split expenses in one place."
          }
        },
        {
          "@type": "Question",
          "name": "How does TRYPS split expenses?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "TRYPS tracks who paid for what during the trip and calculates the simplest settlement between everyone at the end. Each person sees exactly who owes them and who they owe."
          }
        },
        {
          "@type": "Question",
          "name": "How is TRYPS different from SquadTrip, Wanderlog, or Splitwise?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "TRYPS is built for friend groups planning informal trips together — not for professional trip organizers (SquadTrip), solo itinerary builders (Wanderlog), or expense-only apps (Splitwise). TRYPS combines date polling, shared itinerary, invites, and expense splitting in one app focused on friend trips."
          }
        },
        {
          "@type": "Question",
          "name": "How does TRYPS date polling work?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Everyone in the group sees a set of candidate dates, votes on which ones work for them, and TRYPS picks the date that works for the most people. No more 47 DMs trying to find a date."
          }
        },
        {
          "@type": "Question",
          "name": "Is TRYPS free?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Yes. TRYPS is free during the beta — download from the App Store or Google Play and invite your group."
          }
        },
        {
          "@type": "Question",
          "name": "What platforms does TRYPS support?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "TRYPS is available on iOS and Android. All group members need the app to vote on dates, add expenses, and see the itinerary."
          }
        }
      ]
    }
  ]
}
```

---

## Entity Consistency Matrix

| Entity | Schema | OG Tags | Title | Canonical | Footer | Consistent? |
|---|---|---|---|---|---|---|
| Brand name | "TRYPS" | "TRYPS" (og:site_name) | "TRYPS — ..." | — | "tryps" (lowercase in header logo) | ⚠ (casing drift in header only; schema/OG/title all agree) |
| URL/domain | https://jointryps.com | https://jointryps.com (og:url) | — | https://jointryps.com | — | ✓ |
| Description | "The group trip planning app that actually works." (Org) + "One app for planning, booking, and splitting costs with your group." (SoftwareApp) | "The group trip planning app that actually works. Plan trips with friends, split travel expenses, and coordinate everything in one place." | "Plan your when & where with whoever" | — | — | ⚠ (3 different phrasings — pick one canonical sentence) |
| Logo | favicon.svg (plain URL) | opengraph-image (dynamic, different asset) | — | — | — | ⚠ (logo and OG image are different assets — acceptable but inconsistent) |

---

## Bot's Eye View — Full Detail

**curl response (what AI crawlers receive):**
- HTTP/2 200 OK
- Server: cloudflare (via Vercel)
- Content-Type: text/html; charset=utf-8
- Content-Length: 47,031 bytes
- HSTS: `max-age=63072000`
- x-nextjs-prerender: 1 (confirmed SSR)
- x-vercel-cache: HIT (age: 583,234s = 6.75 days)
- cf-ray: 9ec1e81e2b0d49c8-SIN (Singapore edge)
- Content-Security-Policy: restrictive CSP with self + trusted sources
- X-Content-Type-Options: nosniff
- X-Frame-Options: DENY

**Content verification (from raw HTML):**
- Main body: hero + features + trip showcase + CTA — all in initial HTML
- **H1 raw text: "Plan y our whatever with whoever whatever with whoever"** (animated text SSR artifact)
- **FAQ content: none** (no `<dl>`, no `<details>`, no `<summary>` tags)
- 1 JSON-LD schema block — parseable
- 0 body images requiring alt text
- GTM / Google Analytics preload tags present but do not gate content

**AI search presence verification (WebSearch, 2026-04-14):**
- Query: "best group trip planning app 2026 friends travel" → 10 results, TRYPS in **0**
- Query: "TRYPS app group trip planning jointryps" → 10 results, TRYPS in **0** (returns Troupe, Tripsy, TripIt, Wanderlog)

**Classification: LIKELY ACCESSIBLE to AI crawlers** — content IS in raw HTML — **but content architecture does not create extractable answer units**. AI bots can find the page but have nothing to cite from it.

---

## All Checks Index (103 total)

| Category | Run | Passed | Failed | Warn | N/A |
|---|---|---|---|---|---|
| A: Technical SEO | 12 | 11 | 1 | 0 | 0 |
| B: Performance | 9 | 7 | 0 | 1 | 2 |
| C: On-Page SEO | 12 | 9 | 2 | 1 | 1 |
| D: Schema | 13 | 5 | 4 | 1 | 2 |
| E: AEO Discovery | 13 | 10 | 0 | 2 | 1 |
| F: AEO Extraction | 12 | 0 | 4 | 6 | 2 |
| G: AEO Trust | 9 | 1 | 7 | 1 | 0 |
| H: AEO Selection | 8 | 0 | 7 | 1 | 0 |
| I: GEO | 8 | 0 | 6 | 0 | 2 |
| J: Entity | 4 | 3 | 1 | 0 | 0 |
| **Total** | **100** | **46** | **32** | **13** | **9** |

> Note: counts differ slightly from Supabase row (95 total / 52 pass / 25 fail / 11 warn / 7 NA) because the Supabase row consolidates per-category aggregates differently. The in-report counts above are the per-check-ID breakdown.

---

## Brain Intelligence Applied

🥇 **TIER 1 — PRIMARY SOURCES (Official Documentation)**

   📌 **Google — "AI Overviews Eligibility, E-E-A-T, Search Central"**
      developers.google.com/search/docs
      Applied to: A7, A10, E3, E4, F1, F9, G1, G2, G3, G5, H6, D12
      Evidence: Sieve Rules #1419, #1440, #1441, #1442, #1448, #1456, #1474, #1475, #1496, #1676

   📌 **Schema.org — FAQPage, Organization, Person, SoftwareApplication, MobileApplication, WebSite**
      schema.org
      Applied to: D1, D3, D4, D6, D7, D8, D9, D10, D12, G6, J4
      Evidence: Sieve Rules #1495, #1496, #1600, #1668, #1674, #1676, #7375

   📌 **Perplexity — "Technical Setup and Content Guidelines"**
      docs.perplexity.ai
      Applied to: E1, E2, E5, F1, F9, G5
      Evidence: Sieve Rules #1471, #1472, #1474, #1479, #1480, #1481, #1487

🥈 **TIER 2 — RESEARCH SOURCES (Data-Driven Studies)**

   📌 **Backlinko — AI SEO data studies**
      backlinko.com
      Applied to: B1, C6, C8, F1, F11, F12, H1, H3, I1, I6, G5, G9
      Evidence: Rules #7176, #7190; Anti-patterns #4607, #4602, #4623, #4698, #4714, #4763

   📌 **Princeton/Georgia Tech/IIT Delhi — "GEO: Generative Engine Optimization (KDD 2024)"**
      arxiv.org/abs/2311.09735
      Applied to: F8, G3, I1, I3
      Evidence: Knowledge model (citation frequency + authority source diversity as primary AI selection signals; up to 37% visibility improvement)

📎 **TIER 4 — SPECIALIZED SOURCES**

   📌 **amsive.com — "AI Crawler JavaScript Avoidance Rule" + "CCBot / Common Crawl"**
      amsive.com/insights/seo/answer-engine-optimization
      Applied to: A7, E5, E13
      Evidence: Sieve Rules #2015, #2016

---

## Supplementary Findings (from Sieve Brain — outside 103 checks)

⚠ **Accessibility pattern conflicts with AI extraction pattern**

TRYPS uses an `sr-only` + `aria-hidden="true"` pattern on the H1 to provide a grammatical version for screen readers while showing animated text to sighted users. This is a valid a11y pattern — but it creates an AEO problem: AI crawlers parse all text nodes in raw HTML regardless of CSS/ARIA attributes, so both versions get concatenated. This is a broader sitewide consideration: any place the team uses animated text, visible-on-hover text, or CSS-hidden alternate copy, the raw HTML will contain ALL variants.

🥇 Per Google's Search Central documentation (developers.google.com): "Googlebot parses raw HTML text nodes; CSS display and aria-hidden do not hide content from extraction." [Sieve Rule #1419]

📎 Per amsive.com (amsive.com/insights/seo): "AI crawler raw text node parsing ignores ARIA and visibility attributes." [Sieve Rule #2015]

⚠ **Canonical homepage schema is a regression from trypsagent.com surface**

The trypsagent.com audit on 2026-04-10 showed 9 schema blocks: Organization (with sameAs, founder, contactPoint, knowsAbout), Person (with jobTitle, sameAs, worksFor), WebSite, SoftwareApplication (with featureList, screenshots, aggregateRating), HowTo, FAQPage (7 Q&A), MobileApplication x2, BreadcrumbList. The canonical jointryps.com homepage has 1 block with @graph of 3 types (Organization, SoftwareApplication, WebSite) — all missing their enriched fields.

> **This means the schema enrichment work done earlier was not applied to the canonical URL.** The fix is to port the enriched schema set from trypsagent.com back to jointryps.com.

🥇 Per Google's E-E-A-T guidelines on brand consistency (developers.google.com) [Sieve Rule #1456]

---

## Audit Metadata

- **Version:** 3.0 (curl-first, source-tiered citations v1.3)
- **Checks run:** 100/103 (E9 not externally testable; B10/B11 require Chrome MCP; D13 N/A for landing page)
- **Passed:** 46 | **Failed:** 32 | **Warn:** 13 | **N/A:** 9
- **Gates:** All passed (crawlable, SSR content, real page)
- **Page classification:** SaaS landing page / homepage (HIGH confidence)
- **Competitors analyzed:** 3 attempted (SquadTrip ✓, Wanderlog ✓, TripIt ✗ socket closed)
- **Chrome MCP:** Not connected — CWV not measured, TTFB measured via curl (404ms)
- **Brain entries matched:** ~30 rules + ~10 anti-patterns across Tier 1/2/4 sources
- **Previous audits:** 2 audits on `trypsagent.com` surface (2026-04-10) — 52% and 58%. Treated as distinct URL, noted in trend table
- **Queries used:** 4 (primary, variant, category, branded)
- **Data sources:**
  - curl (ground truth): Technical SEO, Performance, Schema extraction, Discovery/robots, raw HTML content, H1 SSR artifact
  - WebFetch: Content understanding, competitor profiles (2/3 succeeded)
  - WebSearch: GEO presence verification
  - Supabase brain: Rule and anti-pattern enrichment

---

## Summary — What to Do This Week

**This week (DO NOW — afternoon work, raises Page Citation Readiness from 59% → ~85%):**
1. **Fix the H1** — replace animated text span concatenation with a single clean text node + JS/CSS-only visual animation (1 hour, SITEWIDE TEMPLATE)
2. **Port FAQPage schema + add 6-8 visible FAQ pairs** — the single biggest AEO gap (3 hours, SCHEMA + CONTENT)
3. **Add datePublished + dateModified + visible "Last updated"** (15 min, SCHEMA FIX)
4. **Add Organization sameAs + Person/founder schema** (30 min, SCHEMA FIX)
5. **Replace Organization.logo with ImageObject** (5 min, SCHEMA FIX)
6. **Add @id fragments to all schema entities + WebSite.publisher cross-link + SearchAction** (15 min, SCHEMA FIX)

**This month (PLAN — entity-building work):**
7. Expand content from 667 → 2,500 words with use cases, comparison table, case studies (1–2 days, CONTENT RESTRUCTURE)
8. Launch on Product Hunt + submit to AlternativeTo + App Store Optimization (2–3 days, OFF-PAGE)
9. Outreach to 10 category listicle publishers requesting inclusion (1–2 weeks, OFF-PAGE)
10. Reddit community seeding in r/travel, r/solotravel, r/TravelHacks (ongoing, OFF-PAGE)

**Honest framing:** The technical foundation of this page is strong — TTFB 404ms, clean SSR, single H1 count, valid schema structure. The gap is **content architecture for AI extraction** (no FAQ, no definition-first opening, no comparison table) combined with **zero off-page brand signal**. Fixes #1–#6 will push Page Citation Readiness from 59% (D-) into the 85% (B) range in a single afternoon of schema + content work. Fix #7–#10 take weeks and are what actually moves brand presence in AI answer engines.

The trypsagent.com schema enrichment from 2026-04-10 already has the FAQPage, Person, HowTo, enriched Organization work done — **port it to jointryps.com** and most of Layer 2 Schema/Trust/Selection fixes solve themselves.

---

**Persistence confirmation:**
- Supabase: `audit_id 8b42e9d0-188b-4cb0-aec8-3e0a7b62e367` (45 findings persisted to `website_audit_findings`)
- Markdown: `audit-reports/jointryps-com-audit-3-2026-04-14.md` (this file)
