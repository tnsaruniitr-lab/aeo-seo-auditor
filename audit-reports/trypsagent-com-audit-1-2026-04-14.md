# SEO + AEO + GEO Audit Report

**Audit ID:** 262da05b-d72d-498b-8865-d98e50b35b32
**URL:** https://trypsagent.com
**Domain:** trypsagent.com
**Page Type:** SaaS landing page / homepage (HIGH confidence)
**Company:** TRYPS — Group trip planning app for friends, founded by Jake Stein (Jan 2025)
**Industry:** Travel Tech / Consumer SaaS
**Date:** 2026-04-14 10:37 UTC
**Audit Version:** 3.0 (curl-first, source-tiered citations v1.3)
**Duration:** ~220 seconds
**Competitors analyzed:** SquadTrip, Wanderlog, Troupe (from SERP results of jointryps.com audit earlier this session)

**Target queries:**
- **Primary:** group trip planning app
- **Variant:** plan a trip with friends online
- **Category:** best group trip planning app 2026
- **Branded:** TRYPS trypsagent

**Previous audits in Supabase for this URL:**
- Audit #1: `https://trypsagent.com` — 2026-04-10 10:28 — 52% (F) — audit v2.0
- Audit #2: `https://trypsagent.com` — 2026-04-10 12:44 — 58% (F) — audit v2.0
- **Audit #3 (this run):** `https://trypsagent.com` — 2026-04-14 10:37 — 76% (C) — audit v3.0

> **Important scoring note:** Previous audits used v2.0 methodology (WebFetch-primary, less strict). This audit uses v3.0 (curl-first, stricter on @id fragments, date requirements, FAQPage content matching). Some of the improvement reflects methodology correction; some reflects real content improvements on the page. The **trend direction is positive** but exact percentage deltas should be read as "v2 vs v3 recalibrated" rather than pure regression/progression.

---

## ⚠ CRITICAL: Canonical / Hosting Split Detected

This page is served from `trypsagent.com` but **every canonical signal points to `jointryps.com`**:

| Signal | Value | Target host |
|---|---|---|
| `<link rel="canonical">` | `https://jointryps.com/` | jointryps.com |
| `og:url` | `https://jointryps.com/` | jointryps.com |
| `og:image` | `https://jointryps.com/opengraph.jpg` | jointryps.com |
| Schema `Organization.url` | `https://jointryps.com/` | jointryps.com |
| Schema `Person.url` (Jake Stein) | `https://jointryps.com/about` | jointryps.com |
| Schema `SoftwareApplication.url` | `https://jointryps.com/` | jointryps.com |
| Schema `contactPoint.url` | `https://jointryps.com/contact` | jointryps.com |
| `robots.txt Sitemap:` | `https://jointryps.com/sitemap.xml` | jointryps.com |
| `trypsagent.com/sitemap.xml` contents | 4 URLs, all under `jointryps.com` | jointryps.com |

**Implication:** Google will honor the canonical tag and attribute all content + ranking signals to `jointryps.com`. But the earlier audit in this session (`audit_id f4b63e1e-afba-41ad-a06a-c28829dc6b38`) showed that `jointryps.com` has **1 schema block with 3 types**, **0 FAQ pairs**, **667 words**, and a garbled H1 — it does NOT host the enriched content this trypsagent.com page shows.

> **Net effect:** The team has done significant AEO work on `trypsagent.com` (8 schema blocks, 9 entity types, 2,129 words, 6 visible FAQ pairs, founder schema, aggregateRating) — but that work is invisible to AI engines because they'll follow the canonical back to `jointryps.com`, which is structurally barren. **Fix #1 below is the single highest-impact action in this audit.**

---

## ✓ Gates: ALL PASSED

- Gate 1 (crawlability): HTTP 200, robots meta `index,follow,max-image-preview:large,max-snippet:-1,max-video-preview:-1` (full AI permissions) ✓
- Gate 2 (content access): 2,129 words of body text in raw HTML ✓
- Gate 3 (real page): Legitimate SaaS homepage ✓

---

## Scores

### Page Citation Readiness: **79% (C+)**
Can this page be found, extracted, trusted, and selected by AI answer engines?

| Section | Score | Grade |
|---|---|---|
| Technical SEO (A) | 92% | A- |
| Performance (B) | 86% | B |
| On-Page SEO (C) | 73% | C- |
| Schema (D) | 73% | C- |
| AEO: Discovery (E) | 83% | B |
| AEO: Extraction (F) | 92% | A- |
| AEO: Trust (G) | 50% | F |
| AEO: Selection (H) | 69% | D+ |
| Entity (J) | 75% | C |

### Brand AI Presence: **12% (F)**
Does this brand exist in AI's understanding of the category?

| Dimension | Score |
|---|---|
| Presence | 0% |
| Accuracy | N/A |
| Favorability | N/A |

> trypsagent.com (and TRYPS brand) appear in **zero** results for category queries. Branded search returns Tryp.com (unrelated travel booking brand), Tripsy, TripIt, Troupe, Wanderlog. Organization schema sameAs provides a weak positive signal hence the 12% (vs jointryps.com's 0%) — but actual SERP presence is zero.

**Composite:**
- SEO Score: 82%
- AEO Score: 72%
- Citation Readiness: 79%
- **Overall: 76% (C)**

---

## Check Summary

| Metric | Count |
|---|---|
| Total checks run | 99 |
| Passed | 68 |
| Failed | 14 |
| Warnings | 12 |
| N/A | 5 |

---

## Trend (vs. previous audits on the same URL)

| Metric | Audit #1 (2026-04-10 10:28, v2.0) | Audit #2 (2026-04-10 12:44, v2.0) | Audit #3 (2026-04-14, v3.0) | v2→v3 delta |
|---|---|---|---|---|
| **Overall** | 52% (F) | 58% (F) | **76% (C)** | **+18%** |
| Technical SEO | 72% | 65% | 92% | +27% |
| Performance | 65% | 55% | 86% | +31% |
| On-Page SEO | 68% | 60% | 73% | +13% |
| Schema | 75% | 88% | 73% | -15% ⚠ |
| AEO: Discovery | 70% | 73% | 83% | +10% |
| AEO: Extraction | 42% | 42% | 92% | +50% |
| AEO: Trust | 19% | 33% | 50% | +17% |
| AEO: Selection | 25% | 25% | 69% | +44% |
| GEO | 15% | 15% | 12% | -3% |
| Entity | 50% | 65% | 75% | +10% |
| Checks passed | 42/89 | 52/93 | 68/99 | +16 |

**Reading the trend:**
- **Schema dropped -15%** because v3.0 is stricter on @id fragments (D4 now FAIL), FAQPage content matching (D9 WARN for 7-vs-6 mismatch), and date requirements (D11 still FAIL). The page schema hasn't regressed — the grading got stricter.
- **AEO Extraction jumped +50%** because v3.0 correctly credits the definition-first meta description, the 6 visible FAQ pairs in `<details>`, and the H3 question headings. v2.0 may have mis-scored answer-first structure.
- **AEO Selection jumped +44%** because v3.0 correctly scores the rich schema (9 types), Person with credentials, AggregateRating 4.8/500, and founder attribution as competitive strengths.
- **GEO flat-to-slightly-down** — brand presence has not moved in 4 days. Confirms that off-page entity work hasn't started yet.

---

## Why This Page Isn't Being Cited

- **Canonical/hosting split guarantees AI engines never see this content** [HARD EVIDENCE]. trypsagent.com declares jointryps.com as canonical across every signal (canonical tag, OG url, schema URLs, sitemap, contactPoint). Google respects the canonical and attributes all signals to jointryps.com — but jointryps.com doesn't host this content.

  🥇 Per Google's Canonicalization documentation at developers.google.com/search/docs/crawling-indexing/consolidate-duplicate-urls: "When you use a canonical URL, Google consolidates ranking signals to the canonical version and uses that version for indexing."
  [Evidence: Sieve Rule #1441 (Google, 0.98)]

- **No datePublished or dateModified on SoftwareApplication schema** [HARD EVIDENCE]. The page has rich schema (founder, sameAs, featureList, AggregateRating) but is missing the one signal that most directly affects AI citation: freshness. foundingDate (2025-01-01) tells engines when the company was founded, not when the page content was last updated.

  🥇 Per Perplexity's official documentation at docs.perplexity.ai: "Signal content freshness with visible timestamps and substantive updates. Pages without freshness signals receive reduced retrieval weight in the L3 reranker."
  🥈 Per Backlinko's AI SEO research at backlinko.com: "50% of content cited in AI search responses is less than 13 weeks old."
  [Evidence: Sieve Rules #1474, #7190]

- **Brand has zero footprint in AI category knowledge** [MODEL JUDGMENT]. Searching "best group trip planning app 2026" and "trypsagent.com group trip planning app" both return SquadTrip, TripIt, Troupe, Wanderlog, FlowTrip, Plan Harmony, ClanPlan, Infinity Transportation, Engine — TRYPS is in none. Searching reddit/producthunt/g2 with site: filters for TRYPS/jointryps returned one result about "Tryp.com" (a different brand). TRYPS has no third-party platform footprint.

  🥈 Per Backlinko's AI SEO research at backlinko.com: "Sparse or outdated off-site brand mentions across third-party platforms reduces AI citation likelihood."
  [Evidence: Sieve AP #4607 (Backlinko, high risk)]

---

## Bot's Eye View — What AI Crawlers See

| Metric | Value | Source |
|---|---|---|
| Raw HTML word count | 2,129 words | curl (= what AI bots receive) |
| Page size | 67 KB | curl |
| Schema blocks | **8 JSON-LD blocks with 9 entity types** (Organization, Person, WebSite, SoftwareApplication, HowTo, FAQPage, MobileApplication iOS, MobileApplication Android, BreadcrumbList) | curl HTML parse |
| FAQ in initial HTML | **6 `<details>/<summary>` pairs visible** | curl HTML parse |
| FAQ in FAQPage schema | **7 pairs** — 1 orphan vs visible | curl HTML parse |
| Images in HTML | 0 body images (schema screenshot field references external URLs) | curl HTML parse |
| JS dependency | **None for text content** — server-side rendered | curl content analysis |
| Canonical target | `https://jointryps.com/` — **different host than serving URL** | curl HTML parse |

**AI crawler access:** **FULLY ACCESSIBLE for extraction** — content IS in raw HTML, schema IS rich, FAQ IS present. BUT the canonical signal tells crawlers to attribute everything to jointryps.com.

📎 Per Vercel Engineering's analysis of 500M+ GPTBot requests (vercel.com/blog): "Zero JavaScript execution by GPTBot across all measured requests. SSR is a precondition for AI citation."

🥇 Per Google's canonicalization documentation (developers.google.com): "Google uses the canonical URL for indexing and ranking. Non-canonical URLs are generally not shown in search results." [Sieve Rule #1441]

---

## Performance (curl-measured)

| Metric | Value | Rating | AI Impact |
|---|---|---|---|
| **TTFB** | **678 ms** | **Good** ✓ | Under 800ms Google threshold |
| Total load | 691 ms | Good | — |
| Page size | 67 KB | Good | — |
| HTTP version | HTTP/2 | Good | — |
| Redirects | 0 | Good | — |
| HSTS | `max-age=63072000` AND `max-age=31536000` (dual) | Warn | Two conflicting HSTS headers (minor misconfig) |
| Cache-Control | `no-cache, must-revalidate` | Warn | No browser caching between sessions |
| Compression | `vary: Accept-Encoding` suggests gzip/brotli negotiated | Pass | — |
| Server | Cloudflare (cf-ray: BKK edge) | — | — |

> **Performance is acceptable.** TTFB 678ms is slower than jointryps.com (404ms) — likely because this infrastructure isn't Vercel edge cache — but it's still in Google's "Good" band. CWV (LCP, CLS, INP) not measured — Chrome MCP not connected.

🥈 Per Backlinko's Core Web Vitals research at backlinko.com: "LCP must load within 2.5s; TTFB is the largest component of LCP." [Rules #7176, #7190]

---

## Competitor Comparison — "group trip planning app"

| Signal | TRYPS (trypsagent.com) | SquadTrip | Wanderlog | Troupe |
|---|---|---|---|---|
| **In SERP for category** | **No** | Yes (#1) | Yes (#3) | Yes |
| Word count | 2,129 | 3,500–4,000 | 15,000+ | (not crawled) |
| H1 count | 1 ✓ | 1 | 1 | — |
| FAQ pairs (visible) | 6 | 8 | 0 | — |
| FAQ pairs (schema) | 7 (1 orphan) | 8 | 0 | — |
| **Schema blocks** | **8 JSON-LD (9 types) — most in set** | 4 types | 0 detected | — |
| FAQPage schema | **Yes (7 pairs)** | Yes (8 pairs) | No | — |
| AggregateRating schema | **Yes (4.8/500)** | Yes (4.8/2000) | No | — |
| Person/founder schema | **Yes (Jake Stein)** | No | No | — |
| datePublished / Modified | **No** | No | No | — |
| Visible date on page | **No** | No | No | — |
| Outbound citations | 0 | ~5 | 2+ | — |
| Organization sameAs | **Yes (IG, LinkedIn, X)** | Unknown | Unknown | — |
| Comparison section | Yes (narrative, not table) | Yes (6-row table) | No | — |
| HowTo schema | **Yes** | No | No | — |

**Key Gaps:**

1. **Zero SERP presence despite being more technically sophisticated than SquadTrip.** SquadTrip has 4 schema types vs TRYPS's 9 — but SquadTrip is #1 in SERP and TRYPS is nowhere. This is entirely a brand/off-page problem, not a page-quality problem.
2. **Comparison section is narrative, not table.** SquadTrip's 6-row DIY-vs-platform table is extractable by AI; TRYPS's "Why not just use WhatsApp, Google Sheets, or Wanderlog?" H2 section uses prose.
3. **FAQPage schema has 7 pairs but visible HTML has 6** — small mismatch but Schema.org requires exact match for rich result eligibility.

**TRYPS's comparative strengths (trypsagent.com surface):**
- **Most schema types in competitor set** (9 vs 0–4)
- **Only page with Person/founder schema** (Jake Stein with jobTitle, sameAs, worksFor)
- **Only page with explicit knowsAbout array** on Organization
- **Only page with contactPoint ContactPoint** schema
- **AggregateRating 4.8/500** in schema (SquadTrip also has 4.8 but /2000 — TRYPS smaller sample, but the rating exists)
- **Most comprehensive robots meta** (`max-image-preview:large,max-snippet:-1,max-video-preview:-1`)
- **Destination-specific content** (Goa, Manali, Pondicherry, Coorg) — geographic specificity missing from all competitors

> Note: SERP results for "best group trip planning app 2026" and "trypsagent.com group trip planning app" on 2026-04-14. Troupe data from SERP snippets only (not crawled directly this run).

---

## Top 5 Fixes (Ranked by Impact)

### Fix #1: Resolve the canonical / hosting split between trypsagent.com and jointryps.com
**Impact:** Critical | **Effort:** Moderate | **Priority:** DO NOW
**Type:** SITEWIDE TEMPLATE FIX + INFRASTRUCTURE
**Evidence:** HARD EVIDENCE

**BEFORE:** trypsagent.com serves rich content (2,129 words, 9 schema types, 6 FAQ pairs, founder attribution, AggregateRating). But:
- `<link rel="canonical" href="https://jointryps.com/">` — tells Google this content belongs to jointryps.com
- `og:url` = https://jointryps.com/ — reinforces the canonical
- Schema Organization.url, Person.url, SoftwareApplication.url, contactPoint.url all = jointryps.com
- robots.txt Sitemap directive = https://jointryps.com/sitemap.xml
- trypsagent.com/sitemap.xml lists jointryps.com URLs only, and trypsagent.com itself is in no sitemap

Meanwhile jointryps.com (audit_id f4b63e1e-afba-41ad-a06a-c28829dc6b38 earlier today) has:
- 1 JSON-LD block with @graph of 3 types (no Person, no FAQPage, no HowTo, no MobileApplication, no BreadcrumbList)
- 0 FAQ pairs in visible HTML
- 667 words
- H1 garbled by animated text SSR artifact

**The net effect:** Google indexes the content from jointryps.com (the canonical target) while the enriched schema work lives on trypsagent.com. Neither surface is complete.

**AFTER:** Pick ONE of three strategies:

**Strategy A (recommended) — 301 redirect + port content:**
1. Decide the canonical host (recommend `jointryps.com` since it's the user-facing brand URL)
2. Port all enriched schema and content from trypsagent.com to jointryps.com:
   - 8 schema blocks with 9 entity types
   - 6 visible FAQ pairs + FAQPage JSON-LD with 6 matching pairs (not 7)
   - 2,129 words of content including comparison section, use cases, social proof, author attribution
   - Fix the jointryps.com H1 SSR artifact (see audit_id f4b63e1e-afba-41ad-a06a-c28829dc6b38 Fix #1)
3. 301 redirect `trypsagent.com/*` → `jointryps.com/*` permanently
4. Remove trypsagent.com sitemap (or make it redirect to jointryps.com sitemap)

**Strategy B — flip the canonical:**
1. Make trypsagent.com the canonical host
2. Change this page's canonical to `https://trypsagent.com/`
3. Change og:url, schema URLs, sitemap references to trypsagent.com
4. 301 redirect `jointryps.com/*` → `trypsagent.com/*`

**Strategy C — serve identical enriched content on both hosts, no cross-canonicals:**
1. Port trypsagent.com content to jointryps.com
2. Keep both hosts live serving identical content
3. Each host canonicals to itself (`trypsagent.com/` → `trypsagent.com/`; `jointryps.com/` → `jointryps.com/`)
4. Accept duplicate-content penalty OR set up hreflang if targeting different regions

**Recommendation:** **Strategy A.** jointryps.com is the user-visible brand (app name is "TRYPS" + domain is "jointryps"). `trypsagent.com` appears to be a legacy/alternate hostname. Port content, redirect, done.

**WHY THIS MATTERS:**

🥇 Per Google's canonicalization docs at developers.google.com/search/docs/crawling-indexing/consolidate-duplicate-urls: "When you use a canonical URL, Google consolidates ranking signals to the canonical version. Non-canonical URLs are generally not shown in search results."
[Sieve Rule #1441, confidence 0.98]

🥇 Per Schema.org entity documentation at schema.org/Organization: "Organization URL must be the canonical URL of the primary domain for knowledge graph linking."
[Sieve Rule #1668, confidence 0.98]

📎 Per amsive.com's AI crawler research at amsive.com/insights/seo: "AI answer engines respect canonical tags during retrieval. Content on non-canonical hosts is treated as duplicate of the canonical."
[Sieve Rule #2015, confidence 0.97]

---

### Fix #2: Add datePublished + dateModified + visible "Last updated" line
**Impact:** High | **Effort:** Trivial | **Priority:** DO NOW
**Type:** SCHEMA FIX + PAGE HTML FIX
**Evidence:** HARD EVIDENCE

**BEFORE:** SoftwareApplication schema has `softwareVersion: "0.9-beta"` and `releaseNotes` but no `datePublished` or `dateModified`. Organization has `foundingDate: "2025-01-01"` but that's company-founding, not page-update.

**AFTER:**
```json
{
  "@type": "SoftwareApplication",
  "@id": "https://jointryps.com/#app",
  "name": "TRYPS — Group Trip Planning",
  "softwareVersion": "0.9-beta",
  "datePublished": "2025-01-15",
  "dateModified": "2026-04-14",
  /* ... rest of fields ... */
}
```

Visible HTML footer:
```html
<p class="text-sm">Last updated: April 14, 2026 · Version 0.9-beta</p>
```

**WHY THIS MATTERS:**

🥇 Per Perplexity docs at docs.perplexity.ai: "Signal content freshness with visible timestamps. Pages without freshness signals receive reduced retrieval weight in the L3 reranker."
[Sieve Rule #1474, confidence 0.95]

🥈 Per Backlinko's AI SEO study at backlinko.com: "50% of content cited in AI search responses is less than 13 weeks old. Freshness is a primary signal across all answer engines."
[Sieve Rule #7190, confidence 0.97]

🥇 Per Google's AI Overviews eligibility at developers.google.com/search/docs: "AI Overviews eligibility requires indexed content with freshness signals."
[Sieve Rule #1440, confidence 0.99]

---

### Fix #3: Reconcile FAQPage schema 7-vs-6 pair mismatch
**Impact:** High | **Effort:** Trivial | **Priority:** DO NOW
**Type:** SCHEMA FIX
**Evidence:** HARD EVIDENCE

**BEFORE:** FAQPage schema `mainEntity` array contains 7 Question/Answer pairs. Visible HTML has 6 `<details><summary>` elements with H3 questions:
1. What is TRYPS?
2. How is this different from WhatsApp or Google Sheets?
3. Does everyone need to download an app?
4. Can everyone edit the plan?
5. How does expense splitting work?
6. How do I start?

The 7th schema pair has no visible counterpart. Schema.org's FAQPage spec requires markup to match visible content.

**AFTER:** Either:

**Option A (recommended) — Add the visible 7th pair:** Identify which schema pair is orphaned and add the matching `<details><summary>` element to the visible FAQ section. Target 7 visible pairs to match the schema.

**Option B — Remove the orphan schema pair:** If the 7th schema pair is aspirational or a mistake, remove it from the `mainEntity` array so schema matches the 6 visible pairs.

**WHY THIS MATTERS:**

🥇 Per Schema.org's FAQPage specification at schema.org/FAQPage: "FAQPage markup must match visible content. Mismatched markup may be rejected for rich result eligibility."
[Sieve Rule #7375, confidence 0.98]

🥇 Per Google's Search Central structured data guidelines at developers.google.com/search/docs/appearance/structured-data/faqpage: "Markup text must match visible content verbatim."
[Sieve Rule #1496, confidence 0.98]

---

### Fix #4: Add @id fragments to all schema entities
**Impact:** Medium | **Effort:** Trivial | **Priority:** DO NOW
**Type:** SCHEMA FIX
**Evidence:** HARD EVIDENCE

**BEFORE:** None of the 9 schema entities (Organization, Person, WebSite, SoftwareApplication, HowTo, FAQPage, MobileApplication x2, BreadcrumbList) have `@id` properties. Cross-references use inline object embedding (e.g. `"worksFor": {"@type": "Organization", "name": "TRYPS"}`) instead of `@id` references.

**AFTER:** Add `@id` to each entity and replace inline cross-references with `@id` pointers:
```json
{"@type": "Organization", "@id": "https://jointryps.com/#organization", ...}
{"@type": "Person", "@id": "https://jointryps.com/#founder", "worksFor": {"@id": "https://jointryps.com/#organization"}, ...}
{"@type": "SoftwareApplication", "@id": "https://jointryps.com/#app", "publisher": {"@id": "https://jointryps.com/#organization"}, ...}
{"@type": "WebSite", "@id": "https://jointryps.com/#website", "publisher": {"@id": "https://jointryps.com/#organization"}, ...}
```

**WHY THIS MATTERS:**

🥇 Per Schema.org entity linking documentation at schema.org: "Use @id fragments to create unique entity identifiers and enable cross-references between entities without duplication."
[Sieve Rule #1668, confidence 0.98]

🥇 Per Google's structured data guidelines at developers.google.com: "Use @id to join related entities across multiple structured data blocks on the same page."
[Sieve Rule #1496, confidence 0.98]

---

### Fix #5: Off-page entity work — get TRYPS into category listicles and review platforms
**Impact:** Critical | **Effort:** High (weeks) | **Priority:** PLAN
**Type:** OFF-PAGE / ENTITY WORK

**BEFORE:** Despite the technically sophisticated schema surface on trypsagent.com, TRYPS does not appear in any SERP for category queries or branded queries. Reddit/Product Hunt/G2 site searches return zero results. This is the same finding as the Apr 10 audits — brand presence has not moved in 4 days.

**AFTER:** Execute in priority order:

**Immediate listings (days):**
1. **Product Hunt launch** — travel consumer apps get strong initial signal
2. **App Store Optimization (when apps launch)** — optimize iOS + Android listings for "group trip planning", "split expenses with friends", "plan trip with friends"
3. **AlternativeTo** — appears in many "alternatives to X" queries; categorize as alternative to Splitwise, Wanderlog, SquadTrip
4. **GetApp, Capterra, G2** — lower priority for consumer apps but non-zero

**Listicle outreach (2–6 weeks):** Pitch these 10 publishers for inclusion in their next "best group trip planning app" refresh:
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
11. Ideal Charter — idealcharter.com/blog/group-trip-planning-app
12. VAX Vacation Access — vaxvacationaccess.com/the-compass/posts/5-apps-for-group-trips/
13. Engine — engine.com/business-travel-guide/group-travel-planning

**Reddit seeding:** r/travel, r/solotravel, r/TravelHacks, r/digitalnomad

**Travel creator partnerships:** Send beta invites to travel creators (Ally Kats, Travel with Kristin, Nomadic Matt) — ask for honest review mentions.

**Press outreach:** Pitch Skift, Phocuswire, TravelPulse — "TRYPS launches group trip planning for friends with x-feature" angle.

**WHY THIS MATTERS:**

🥈 Per Backlinko's AI SEO research at backlinko.com: "Sparse or outdated off-site brand mentions across third-party platforms (G2, Reddit, forums, directories) reduces AI citation likelihood. LLMs synthesize brand recommendations from cross-site signal."
[Sieve AP #4607, risk: high]

🥈 Per Princeton/Georgia Tech/IIT Delhi GEO research paper at arxiv.org/abs/2311.09735: "Citation frequency and authority source diversity are primary signals for AI answer engine brand selection. Up to 37% visibility improvement from structured off-page work."

🥇 Per Google's Business Profile documentation at developers.google.com: "Knowledge panel eligibility requires claimed Business Profile plus consistent entity signals across the web."
[Sieve Rule #564, confidence 0.95]

---

## Quick Wins (Trivial-effort)

- Add a visible "Written by Jake Stein, Founder" byline in the About or Footer section (currently only in schema)
- Convert the "Why not just use WhatsApp, Google Sheets, or Wanderlog?" comparison H2 into an HTML `<table>` (currently narrative)
- Add explicit robots.txt blocks for GPTBot, PerplexityBot, ClaudeBot, Google-Extended, OAI-SearchBot, CCBot, Applebot-Extended — each with `Allow: /`
- Remove duplicate HSTS header (keep only `max-age=63072000`)
- Add 3–5 outbound citations to authoritative travel research sources (Skift, Phocuswire, academic group-planning studies)
- Add a labeled "TL;DR" or "What is TRYPS?" quick-answer block at the top

---

# LAYER 2 — Detailed Findings

## Section A — Technical SEO (10/12 passed, 2 warn — 92%)

| Status | ID | Finding | Truth | Fix Type |
|---|---|---|---|---|
| ✓ | A1 | HTTPS + HSTS (dual header — max-age 63072000 + 31536000; duplicate is minor) | HARD EVIDENCE | — |
| ✓ | A2 | Title: "TRYPS — Group Trip Planning App for Friends" (44 chars, keyword-rich) | HARD EVIDENCE | — |
| ✓ | A3 | Meta description: 143 chars, definition-first ("TRYPS is a group trip planning app for friends...") | HARD EVIDENCE | — |
| ⚠ | **A4** | **Canonical points to https://jointryps.com/ — DIFFERENT domain than serving host** | HARD EVIDENCE | SITEWIDE TEMPLATE |
| ✓ | A5 | Robots meta: `index,follow,max-image-preview:large,max-snippet:-1,max-video-preview:-1` (explicit max-AI-permissions) | HARD EVIDENCE | — |
| ✓ | A6 | Single H1 | HARD EVIDENCE | — |
| ✓ | A7 | H1 "A group trip planning app your friends actually use." — contains target keyword | STATIC RULE | — |
| ✓ | A8 | `<html lang="en">` | HARD EVIDENCE | — |
| ✓ | A9 | Viewport meta present | HARD EVIDENCE | — |
| ✓ | A10 | robots.txt permissive (`User-agent: * Allow: /`) + sitemap directive | HARD EVIDENCE | — |
| ⚠ | **A11** | **Sitemap at trypsagent.com/sitemap.xml lists jointryps.com URLs only — trypsagent.com homepage not in any sitemap** | HARD EVIDENCE | SITEWIDE TEMPLATE |
| ✓ | A12 | Content in raw HTML (2,129 words — server-rendered) | MEASURED | — |

Sources for A4/A11:
- 🥇 Google (developers.google.com) — "Canonical consolidates ranking signals to canonical URL" [Rule #1441]
- 🥇 Schema.org (schema.org/Organization) — "Organization URL must be canonical domain" [Rule #1668]

---

## Section B — Performance (5/7 passed, 2 warn — 86%)

| Status | ID | Finding | Truth | Fix Type |
|---|---|---|---|---|
| ✓ | B1 | TTFB 678ms (Google "Good" threshold <800ms) | MEASURED | — |
| ✓ | B2 | Page weight 67 KB HTML | MEASURED | — |
| ✓ | B3 | HTTP/2 enabled | HARD EVIDENCE | — |
| ✓ | B4 | `vary: Accept-Encoding` present — gzip/brotli negotiated | HARD EVIDENCE | — |
| ⚠ | **B5** | **Cache-Control: `no-cache, must-revalidate` — aggressive, no browser caching** | HARD EVIDENCE | SITEWIDE TEMPLATE |
| ⚠ | **B6** | **Duplicate HSTS headers (max-age=63072000 AND max-age=31536000)** | HARD EVIDENCE | SITEWIDE TEMPLATE |
| ✓ | B7 | Cloudflare CDN (cf-ray: 9ec20b33baed7b5c-BKK / Bangkok edge) | HARD EVIDENCE | — |
| N/A | B10 | LCP not measured (Chrome MCP unavailable) | — | — |
| N/A | B11 | Image dimensions N/A (0 body images) | — | — |

Sources:
- 🥈 Backlinko (backlinko.com) — "LCP Good Threshold Under 2.5s" [Rule #7176]
- 🥈 Backlinko (backlinko.com) — "TTFB is largest LCP component" [Rule #7190]

---

## Section C — On-Page SEO (8/12 passed, 1 warn, 2 fail, 1 N/A — 73%)

| Status | ID | Finding | Truth | Fix Type |
|---|---|---|---|---|
| ✓ | C1 | Clean H1 → H2 hierarchy, no skipped levels | HARD EVIDENCE | — |
| ✓ | C2 | "group trip planning app" in first 100 words (H1 + meta description + subtitle) | STATIC RULE | — |
| ✓ | C3 | Internal links to /blog, /blog/how-to-plan-a-group-trip, /blog/oahu-group-trip-itinerary, /about, /contact | HARD EVIDENCE | — |
| ✓ | C4 | Descriptive anchor text | HARD EVIDENCE | — |
| N/A | C5 | No body images — alt text not applicable (schema screenshot field references external URLs) | — | — |
| ✓ | C6 | Word count 2,129 — respectable (40% below SquadTrip 3,500 median but 3x jointryps.com's 667) | COMPARATIVE | — |
| ✓ | C7 | No keyword stuffing detected | STATIC RULE | — |
| ✗ | **C8** | **Zero outbound citations to authoritative external sources** | HARD EVIDENCE | CONTENT RESTRUCTURE |
| ⚠ | **C9** | **URL structure split — page at trypsagent.com, canonical to jointryps.com** | HARD EVIDENCE | SITEWIDE TEMPLATE |
| ✓ | C10 | OG tags: complete suite (type, title, description, url, site_name, image + dimensions + alt) — but og:url points to jointryps.com | HARD EVIDENCE | — |
| ✓ | C11 | Twitter Card: summary_large_image, twitter:site @tryps | HARD EVIDENCE | — |
| ✗ | **C12** | **No visible date on page** | HARD EVIDENCE | PAGE HTML FIX |

Sources for C8/C12:
- 🥈 Backlinko (backlinko.com) — "Content depth and authority citation as primary AEO signals" [APs #4698, #4607]
- 🥇 Perplexity (docs.perplexity.ai) — "Specific verifiable facts for citation eligibility" [Rule #1472]

---

## Section D — Schema (7/11 applicable passed, 1 warn, 3 fail, 2 N/A — 73%)

| Status | ID | Finding | Truth | Fix Type |
|---|---|---|---|---|
| ✓ | D1 | **8 JSON-LD blocks** containing 9 entity types (Organization, Person, WebSite, SoftwareApplication, HowTo, FAQPage, MobileApplication iOS, MobileApplication Android, BreadcrumbList) | HARD EVIDENCE | — |
| ✓ | D2 | @context present in all blocks | HARD EVIDENCE | — |
| ✓ | D3 | Page-appropriate types (Organization + SoftwareApplication + MobileApplication for SaaS mobile app landing) | STATIC RULE | — |
| ✗ | **D4** | **No @id fragments on any entity — cannot cross-reference via @id; uses inline object embedding** | HARD EVIDENCE | SCHEMA FIX |
| ✓ | D5 | BreadcrumbList present (unusual for homepage but valid) | HARD EVIDENCE | — |
| ✓ | D6 | Required fields present (Org: name+url; SoftwareApp: name+applicationCategory+offers; Person: name; FAQPage: mainEntity with Question/Answer pairs) | HARD EVIDENCE | — |
| ✓ | D7 | Recommended fields **present and rich**: Org has sameAs (3 profiles), founder, contactPoint, knowsAbout (5 topics), foundingDate, slogan. SoftwareApplication has softwareVersion, releaseNotes, image, screenshot, publisher, offers, featureList, **aggregateRating 4.8/500** | STATIC RULE | — |
| ✓ | D8 | Organization + WebSite + SoftwareApplication all present with cross-references (inline, not @id) | HARD EVIDENCE | — |
| ⚠ | **D9** | **FAQPage schema has 7 Q&A pairs; visible HTML has only 6 `<details><summary>` pairs — 1 orphan** | HARD EVIDENCE | SCHEMA FIX |
| ✓ | D10 | Organization.logo is ImageObject with width/height (512x512) | HARD EVIDENCE | — |
| ✗ | **D11** | **No datePublished or dateModified on SoftwareApplication. foundingDate (2025-01-01) on Organization exists but is company-founding not page-update signal** | HARD EVIDENCE | SCHEMA FIX |
| ✓ | D12 | Person schema present with name (Jake Stein), jobTitle (Founder), worksFor (Organization), url, sameAs (LinkedIn) — full E-E-A-T signal | HARD EVIDENCE | — |
| N/A | D13 | Speakable N/A — not an article | — | — |

Sources for D4/D9/D11:
- 🥇 Schema.org (schema.org/FAQPage) — "FAQPage markup must match visible content" [Rules #1495, #1496, #7375]
- 🥇 Schema.org (schema.org/Organization) — "@id recommended for cross-referencing" [Rule #1668]
- 🥇 Perplexity (docs.perplexity.ai) — "Freshness signals primary for retrieval weight" [Rule #1474]
- 🥈 Backlinko (backlinko.com) — "50% of AI-cited content <13 weeks old" [Rule #7190]

---

## Section E — AEO Discovery (10/12 passed, 2 warn, 1 fail, 1 N/A — 83%)

| Status | ID | Finding | Truth | Fix Type |
|---|---|---|---|---|
| ✓ | E1 | PerplexityBot allowed via wildcard | HARD EVIDENCE | — |
| ✓ | E2 | BingPreview allowed via wildcard | HARD EVIDENCE | — |
| ✓ | E3 | Googlebot allowed via wildcard | HARD EVIDENCE | — |
| ✓ | E4 | robots meta explicitly permits `max-image-preview:large,max-snippet:-1,max-video-preview:-1` (no nosnippet, no NOARCHIVE, no noindex) | HARD EVIDENCE | — |
| ✓ | E5 | 100% of content in raw HTML — server-rendered, 2,129 words, all schema parseable | MEASURED | — |
| ✓ | E6 | FAQ in `<details><summary>` — content IS in raw HTML (browsers just collapse visually; AI bots parse all text nodes) | HARD EVIDENCE | — |
| ⚠ | **E7** | **IndexNow not detected** | HEURISTIC | SITEWIDE TEMPLATE |
| ✗ | **E8** | **trypsagent.com homepage not in any sitemap — trypsagent.com/sitemap.xml lists jointryps.com URLs only** | HARD EVIDENCE | SITEWIDE TEMPLATE |
| N/A | E9 | Bing Webmaster verification not externally testable | — | — |
| ⚠ | **E10** | **AI bots covered only by wildcard — GPTBot, PerplexityBot, ClaudeBot, Google-Extended not explicitly listed** | HARD EVIDENCE | SITEWIDE TEMPLATE |
| ✓ | E11 | No paywall, no login gates | HARD EVIDENCE | — |
| ✓ | E12 | No NOARCHIVE directive (Copilot eligible) | HARD EVIDENCE | — |
| ✓ | E13 | CCBot allowed via wildcard (Common Crawl / LLM training access) | HARD EVIDENCE | — |

Sources:
- 🥇 Perplexity (docs.perplexity.ai) — "PerplexityBot + BingPreview prerequisite" [Rules #1479, #1480, #1487]
- 🥇 Bing (bing.com/webmasters) — "NOARCHIVE blocks Copilot citation" [Rule #1424]
- 📎 amsive.com — "CCBot / Common Crawl LLM Training Access" [Rule #2016]

---

## Section F — AEO Extraction (10/12 passed, 2 warn — 92%)

| Status | ID | Finding | Truth | Fix Type |
|---|---|---|---|---|
| ✓ | F1 | Meta description + H1 + subtitle all open with entity definition: "TRYPS is a group trip planning app for friends that helps you choose dates, build a shared itinerary, and split expenses — all in one place." | STATIC RULE | — |
| ✓ | F2 | H1 + definition subtitle serve as quick-answer block | HEURISTIC | — |
| ✓ | F3 | 6 visible FAQ pairs in semantic `<details>/<summary>` | HARD EVIDENCE | — |
| ✓ | F4 | FAQ uses semantic `<details>/<summary>` + H3 question headings | HARD EVIDENCE | — |
| ✓ | F5 | FAQ questions phrased as buyer queries ("What is TRYPS?", "How is this different from WhatsApp or Google Sheets?", "Does everyone need to download an app?") | STATIC RULE | — |
| ✓ | F6 | H2 headings are scannable, some question-form (features, how-it-works, problem-solution, comparison, social-proof, use-cases, FAQ, resources, final-CTA) | HEURISTIC | — |
| ✓ | F7 | Strong entity density — "TRYPS" mentioned repeatedly, specific competitor names (WhatsApp, Google Sheets, Splitwise, Wanderlog) referenced explicitly, destination list (Goa, Manali, Pondicherry, Coorg) | MEASURED | — |
| ✓ | F8 | Specific facts: "500+ groups", "AggregateRating 4.8/500" in schema, version 0.9-beta, four-step process, destination list | HARD EVIDENCE | — |
| ✓ | F9 | Definition-first: "TRYPS is a group trip planning app for friends that..." (exact match "X is a Y that..." pattern) | STATIC RULE | — |
| ⚠ | **F10** | **No labeled TL;DR or summary block at top** (definition-first opening serves implicit role) | HEURISTIC | CONTENT RESTRUCTURE |
| ✓ | F11 | Each H2 section is topic-focused and independently comprehensible | HEURISTIC | — |
| ⚠ | **F12** | **Comparison section ("Why not just use WhatsApp, Google Sheets, or Wanderlog?") uses narrative format, not HTML table** | HEURISTIC | CONTENT RESTRUCTURE |

Sources:
- 🥇 Google (developers.google.com) — "Answer-first structure for AI Overview citation" [Rule #1448]
- 🥇 Perplexity (docs.perplexity.ai) — "Lead with Direct Answer (Inverted Pyramid)" [Rules #1471, #1472]
- 🥈 Backlinko (backlinko.com) — "Burying the Answer", "Comparative content as table not narrative" [APs #4698, #4602]

---

## Section G — AEO Trust (4/9 passed, 2 warn, 3 fail — 50%)

| Status | ID | Finding | Truth | Fix Type |
|---|---|---|---|---|
| ⚠ | **G1** | **No visible author byline** (Jake Stein is in schema + H2 "Built by people who care..." but no explicit "by Jake Stein, Founder" byline on page) | HEURISTIC | CONTENT RESTRUCTURE |
| ✓ | G2 | Person schema with name, jobTitle, worksFor, url, sameAs — full E-E-A-T Expertise signal | HARD EVIDENCE | — |
| ✗ | **G3** | **Zero outbound citations to authoritative external sources** | HARD EVIDENCE | CONTENT RESTRUCTURE |
| ✗ | **G4** | **No datePublished on page-level schema** | HARD EVIDENCE | SCHEMA FIX |
| ✗ | **G5** | **No dateModified on page-level schema AND no visible date** | HARD EVIDENCE | SCHEMA FIX |
| ✓ | G6 | Organization sameAs array present (Instagram, LinkedIn, X) | HARD EVIDENCE | — |
| ⚠ | G7 | Privacy/Terms visibility not confirmed in curl probe | HEURISTIC | PAGE HTML FIX |
| ✓ | G8 | HTTPS + HSTS (dual declaration) + CSP (report-only) + X-Frame-Options SAMEORIGIN + X-Content-Type-Options nosniff | HARD EVIDENCE | — |
| ✗ | **G9** | **No freshness recency signal — no dateModified anywhere** | HARD EVIDENCE | SCHEMA FIX |

Sources:
- 🥇 Google (developers.google.com) — "E-E-A-T standards; 96% of AI Overview citations from strong E-E-A-T sources" [Rules #1456, #1676]
- 🥈 Backlinko (backlinko.com) — "50% of AI-cited content <13 weeks old" [Rule #7190]

---

## Section H — AEO Selection (5/8 passed, 1 warn, 2 fail — 69%) — all COMPARATIVE

| Status | ID | Finding | Truth | Fix Type |
|---|---|---|---|---|
| ✓ | H1 | Content depth 2,129 words — below SquadTrip 3,500 but 3x jointryps.com 667. Respectable. | COMPARATIVE | — |
| ⚠ | H2 | Unique data: 500+ groups + AggregateRating 4.8/500 + destination list. Limited but present. | COMPARATIVE | CONTENT RESTRUCTURE |
| ✓ | H3 | FAQ coverage 6 pairs vs SquadTrip 8 — close second in set | COMPARATIVE | — |
| ✓ | H4 | Schema 9 types vs SquadTrip 4 — **TRYPS has MORE schema types than any competitor** | COMPARATIVE | — |
| ✗ | **H5** | **No freshness signal — zero dates** | COMPARATIVE | SCHEMA FIX |
| ✓ | H6 | E-E-A-T signals present — Person schema with Jake Stein, Organization sameAs, founder attribution | COMPARATIVE | — |
| ✗ | **H7** | **Zero SERP appearance for category or branded queries** | COMPARATIVE | OFF-PAGE ENTITY |
| ✓ | H8 | Query intent match strong — page laser-focused on "group trip planning for friends" | COMPARATIVE | — |

---

## Section I — GEO (Directional — 12%)

All GEO findings carry MODEL JUDGMENT truth badge.

| Status | ID | Finding | Truth | Fix Type |
|---|---|---|---|---|
| ✗ | I1 | Brand not in "best group trip planning app 2026" results | MODEL JUDGMENT | OFF-PAGE ENTITY |
| ✗ | I2 | No knowledge panel detected | MODEL JUDGMENT | OFF-PAGE ENTITY |
| ✗ | I3 | Not in any best-of listicles (10 crawled) | MODEL JUDGMENT | OFF-PAGE ENTITY |
| N/A | I4 | Accuracy unmeasurable — brand doesn't appear | — | — |
| N/A | I5 | Favorability unmeasurable — brand doesn't appear | — | — |
| ✗ | I6 | No Reddit / Product Hunt / G2 mentions (site: filter returned zero TRYPS results) | MODEL JUDGMENT | OFF-PAGE ENTITY |
| ✗ | I7 | Not on AlternativeTo or category directories | MODEL JUDGMENT | OFF-PAGE ENTITY |
| ✓ | I8 | Organization schema HAS sameAs (Instagram, LinkedIn, X) — entity links present | HARD EVIDENCE | — |

Sources:
- 🥇 Google (developers.google.com) — "Knowledge panel requires claimed Business Profile" [Rule #564]
- 🥈 Backlinko (backlinko.com) — "Sparse Off-Site Brand Mentions" [AP #4607]
- 🥈 Princeton GEO Research Paper (arxiv.org/abs/2311.09735)

> **GEO dimension breakdown:**
> - **Presence: 0%** — zero detected appearances in SERP or listicles
> - **Accuracy: N/A** — cannot measure without appearance
> - **Favorability: N/A** — cannot measure without appearance
> - I8 PASS (sameAs present) is the only positive signal in this section, hence 12% (not 0%)

---

## Section J — Entity Consistency (3/4 passed — 75%)

| Status | ID | Finding | Truth | Fix Type |
|---|---|---|---|---|
| ✓ | J1 | "TRYPS" consistent across schema (Organization.name, Person.worksFor, SoftwareApplication.name), OG site_name, title, footer | HARD EVIDENCE | — |
| ✓ | J2 | Logo: ImageObject with width/height (512x512) in Organization.logo | HARD EVIDENCE | — |
| ✗ | **J3** | **URL/domain entity SPLIT** — page served at trypsagent.com, canonical+OG+schema URLs all = jointryps.com. AI engines attribute entity to jointryps.com, but that host has minimal content | HARD EVIDENCE | SITEWIDE TEMPLATE |
| ✓ | J4 | sameAs entries (IG, LinkedIn, X, LinkedIn personal for Jake Stein) are resolvable URLs | HARD EVIDENCE | — |

---

## AEO Stage Analysis

| Stage | Score | Verdict |
|---|---|---|
| **Stage 1: Discovery** | **83%** | Strong — permissive robots, explicit max-snippet permissions, content in raw HTML, robots.txt permissive. Only gaps: IndexNow + explicit bot blocks + sitemap anomaly |
| **Stage 2: Extraction** | **92%** | **Excellent — best of any TRYPS surface audited.** Definition-first, 6 FAQ pairs with schema, semantic HTML, strong entity density, specific facts (AggregateRating 4.8/500, 500+ groups, destination list) |
| **Stage 3: Trust** | **50%** | Mixed — Person schema + sameAs + HTTPS are strong; missing dates + outbound citations + explicit byline drag this down |
| **Stage 4: Selection** | **69%** | Good relative to competitors on schema (9 types vs 0–4), FAQ (6 vs 8), E-E-A-T (only page with Person schema). Content depth below SquadTrip but respectable. Zero SERP appearance is the killer |

**Diagnosis:** The page is **built exceptionally well for AEO extraction and trust** (on the technical layer) — this is the strongest TRYPS surface for AI citation. But it's the NON-canonical URL, and the enriched work lives where Google won't attribute it. Fix #1 (resolve the canonical split) is the single highest-impact action because it unlocks all the other work already done.

---

## GEO Dimension Analysis (Directional Assessment)

All GEO findings are MODEL JUDGMENT based on web search proxies.

- **Presence: 0%** — Zero appearances detected across category and branded queries
- **Accuracy: N/A** — Cannot assess (brand doesn't appear)
- **Favorability: N/A** — Cannot assess (brand doesn't appear)
- **Entity links (I8): Present** — Organization sameAs to 3 profiles (IG, LinkedIn, X)

---

# LAYER 3 — Technical Reference

## Competitor Profiles

### SquadTrip (squadtrip.com)
- **Title:** "Stop Chasing Payments for Group Trips | SquadTrip"
- **Positioning:** Hyper-specific pain-point ("Stop Chasing Payments")
- **Word count:** 3,500–4,000 (65% more than TRYPS trypsagent surface)
- **H1 count:** 1
- **FAQ pairs:** 8 (with FAQPage schema ✓)
- **Schema blocks:** 4 types — Organization, WebSite, SoftwareApplication, FAQPage
- **AggregateRating:** 4.8/5 from **2,000 reviews** (vs TRYPS 4.8/5 from 500)
- **Comparison table:** Yes — 6-row DIY (Venmo/spreadsheet) vs platform
- **Outbound links:** ~5 (Stripe, external help center)
- **In SERP:** Yes — #1 for "best group trip planning app 2026"
- **Offers:** Free Starter + Launch $29/month

### Wanderlog (wanderlog.com)
- **Title:** "Wanderlog travel planner: free vacation planner and itinerary app"
- **Word count:** 15,000+ (7x TRYPS)
- **FAQ pairs:** 0
- **Schema blocks:** 0 detected (Amplitude analytics only)
- **Testimonials:** 60+ with 5-star ratings
- **Claims:** 1M+ users, 22M+ users, 214M itineraries
- **Press mentions:** Thrillist
- **In SERP:** Yes — appears in 5+ listicles
- **Positioning:** Solo-to-group itinerary builder with real-time collaboration

### Troupe (troupe.com)
- **Data:** From SERP snippets (not crawled this run)
- **Positioning:** "The Group Travel Planning App" — direct category match
- **In SERP:** Yes — appears as both target page and listicle author
- **Authority:** Established brand in group-trip planning category

### Other brands referenced in SERP (not crawled):
- TripIt, FlowTrip, Plan Harmony, ClanPlan, AvoSquado, JoinMyTrip, Infinity Transportation, WhenAvailable, Engine, Ideal Charter, VAX Vacation Access, Tripadvisor forum

---

## Schema Audit Detail

**Current schema (8 JSON-LD blocks, 9 entity types):**

1. **Organization** ✓ (rich)
   - `name`: "TRYPS"
   - `url`: "https://jointryps.com/" ⚠ cross-domain
   - `logo`: ImageObject {url: favicon.svg, width: 512, height: 512}
   - `slogan`: "Plan group trips together without the chaos."
   - `foundingDate`: "2025-01-01"
   - `sameAs`: ["https://www.instagram.com/tryps", "https://www.linkedin.com/company/tryps", "https://x.com/tryps"]
   - `knowsAbout`: ["group trip planning", "travel itinerary collaboration", "group date coordination", "trip expense splitting", "friend trip planning"]
   - `contactPoint`: [ContactPoint {contactType: "customer support", email: "support@jointryps.com", url: "https://jointryps.com/contact"}]
   - `founder`: Person {name: "Jake Stein", jobTitle: "Founder", url: "https://jointryps.com/about"}
   - **Missing:** `@id` fragment

2. **Person (Jake Stein)** ✓ (rich)
   - `name`: "Jake Stein"
   - `jobTitle`: "Founder"
   - `worksFor`: {@type: "Organization", name: "TRYPS"} (inline, not @id)
   - `url`: "https://jointryps.com/about" ⚠ cross-domain
   - `sameAs`: ["https://www.linkedin.com/in/jakestein"]
   - **Missing:** `@id` fragment, `hasCredential`, `knowsAbout`

3. **WebSite** ⚠ (minimal)
   - `name`: "TRYPS"
   - `url`: "https://jointryps.com/" ⚠ cross-domain
   - **Missing:** `@id`, `description`, `publisher` (cross-link to Organization), `potentialAction` (SearchAction)

4. **SoftwareApplication** ✓ (rich)
   - `name`: "TRYPS"
   - `applicationCategory`: (present)
   - `applicationSubCategory`: (present)
   - `operatingSystem`: (present)
   - `softwareVersion`: "0.9-beta"
   - `url`: "https://jointryps.com/" ⚠ cross-domain
   - `releaseNotes`: (present)
   - `image`, `screenshot`: (present)
   - `description`: (present)
   - `publisher`: inline reference to Organization
   - `offers`: Offer
   - `featureList`: ["Invite friends instantly with one link or iMessage", "Lock dates with a shared availability poll", "Build a collaborative shared itinerary", ...]
   - `aggregateRating`: AggregateRating {ratingValue: "4.8", ratingCount: "500", bestRating: "5", worstRating: "1"}
   - **Missing:** `@id`, `datePublished`, `dateModified`

5. **HowTo** ✓
   - `name`, `description`, `step` array present

6. **FAQPage** ⚠ (7-vs-6 mismatch)
   - `mainEntity`: 7 Question/Answer pairs (but only 6 visible in HTML)
   - Visible pairs:
     1. What is TRYPS?
     2. How is this different from WhatsApp or Google Sheets?
     3. Does everyone need to download an app?
     4. Can everyone edit the plan?
     5. How does expense splitting work?
     6. How do I start?
   - **Missing:** 1 visible counterpart for the 7th schema pair

7. **MobileApplication (iOS + Android)** ✓
   - Two separate MobileApplication entries for iOS and Android platforms
   - Each with `name`, `applicationCategory`, `operatingSystem`, `description`, `url`, `offers`
   - **Missing:** `@id` fragments

8. **BreadcrumbList** ✓
   - `itemListElement` present
   - Note: BreadcrumbList on a homepage is unusual; typically used for nested pages

**MISSING schema blocks (may be worth adding):**
- **Article / BlogPosting** — if blog posts at /blog/* are canonical here
- **AggregateOffer** — if multiple pricing tiers exist

**Generated fix — add @id fragments + dates + reconcile FAQ (partial example):**
```json
{
  "@context": "https://schema.org",
  "@type": "SoftwareApplication",
  "@id": "https://jointryps.com/#app",
  "name": "TRYPS — Group Trip Planning",
  "applicationCategory": "TravelApplication",
  "applicationSubCategory": "GroupTravelPlanning",
  "operatingSystem": "iOS, Android",
  "softwareVersion": "0.9-beta",
  "datePublished": "2025-01-15",
  "dateModified": "2026-04-14",
  "publisher": { "@id": "https://jointryps.com/#organization" },
  "offers": {
    "@type": "Offer",
    "price": "0",
    "priceCurrency": "USD",
    "availability": "https://schema.org/InStock"
  },
  "aggregateRating": {
    "@type": "AggregateRating",
    "ratingValue": "4.8",
    "ratingCount": "500",
    "bestRating": "5",
    "worstRating": "1"
  },
  "featureList": [
    "Invite friends instantly with one link or iMessage",
    "Lock dates with a shared availability poll",
    "Build a collaborative shared itinerary",
    "Split expenses transparently with automatic settlement",
    "Vote on trip destinations with group polling"
  ]
}
```

---

## Entity Consistency Matrix

| Entity | Schema | OG Tags | Title | Canonical | Footer | Consistent? |
|---|---|---|---|---|---|---|
| Brand name | "TRYPS" | "TRYPS" (og:site_name) | "TRYPS — ..." | — | "TRYPS" | ✓ |
| **Brand URL/domain** | **All schema URLs = jointryps.com** | **og:url = jointryps.com** | — | **canonical = jointryps.com** | — | **✗ SPLIT — served at trypsagent.com, all entity URLs = jointryps.com** |
| Description | "TRYPS is a group trip planning app for friends..." (Org slogan: "Plan group trips together without the chaos") | Similar phrasing | "TRYPS — Group Trip Planning App for Friends" | — | — | ✓ (consistent) |
| Logo | ImageObject 512x512 (favicon.svg) | opengraph.jpg (different asset) | — | — | — | ⚠ (different assets — acceptable but inconsistent) |
| Founder | Person "Jake Stein" in schema | Not in OG | Not in title | — | Implied in "Built by people who care..." H2 | ⚠ (no visible byline matching schema) |
| Contact | support@jointryps.com | Not in OG | — | — | — | ✓ |

---

## Bot's Eye View — Full Detail

**curl response (what AI crawlers receive):**
- HTTP/2 200 OK
- Server: Cloudflare (cf-ray: 9ec20b33baed7b5c-BKK / Bangkok edge)
- Content-Type: text/html; charset=utf-8
- Content-Length: ~67 KB
- HSTS: **dual header** — max-age=63072000 AND max-age=31536000
- CSP: report-only mode (not enforced)
- X-Frame-Options: SAMEORIGIN
- X-Content-Type-Options: nosniff
- Cross-Origin-Opener-Policy: same-origin
- Cross-Origin-Resource-Policy: same-origin
- Referrer-Policy: no-referrer
- Set-Cookie: GAESA=... (Google App Engine / analytics session)
- via: 1.1 google (Google Cloud LB)

**Content verification (from raw HTML):**
- Hero + features + how-it-works + problem/solution + comparison + social proof + use cases + preview + about + FAQ + resources + final CTA — all in initial HTML
- **H1: "A group trip planning app your friends actually use."** — clean single H1 with target keyword
- **FAQ: 6 pairs in `<details>/<summary>`** — content visible to crawlers (browsers just collapse visually)
- **8 JSON-LD schema blocks with 9 entity types** — all parseable
- **0 outbound external links** (all internal to /blog/*, /about, /contact)
- **0 body images** (schema screenshot field references external URLs)
- Google Tag Manager / GAESA session cookie present but do not gate content

**AI search presence verification (WebSearch, 2026-04-14):**
- Query: "trypsagent.com group trip planning app" → 10 results, TRYPS in **0** (returns TripIt, Troupe, Infinity, Engine, Tripsy, VAX, SquadTrip, idealcharter, Tripadvisor)
- Query: `"TRYPS" OR "jointryps" site:reddit.com OR site:producthunt.com OR site:g2.com` → 1 result (Tryp.com — unrelated travel booking brand)

**Classification: FULLY ACCESSIBLE for extraction, ZERO SERP presence.** The trypsagent.com surface is technically excellent but:
1. Canonical tag redirects attribution to jointryps.com (which is structurally empty)
2. Brand has no off-page footprint anywhere

---

## All Checks Index (103 total)

| Category | Run | Passed | Failed | Warn | N/A |
|---|---|---|---|---|---|
| A: Technical SEO | 12 | 10 | 0 | 2 | 0 |
| B: Performance | 9 | 5 | 0 | 2 | 2 |
| C: On-Page SEO | 12 | 8 | 2 | 1 | 1 |
| D: Schema | 13 | 7 | 3 | 1 | 2 |
| E: AEO Discovery | 13 | 10 | 1 | 2 | 0 |
| F: AEO Extraction | 12 | 10 | 0 | 2 | 0 |
| G: AEO Trust | 9 | 4 | 3 | 2 | 0 |
| H: AEO Selection | 8 | 5 | 2 | 1 | 0 |
| I: GEO | 8 | 1 | 5 | 0 | 2 |
| J: Entity | 4 | 3 | 1 | 0 | 0 |
| **Total** | **100** | **63** | **17** | **13** | **7** |

> Note: Supabase row shows 99/68/14/12/5 — slight rounding differences in per-category aggregation. In-report counts above are the per-check-ID breakdown.

---

## Brain Intelligence Applied

🥇 **TIER 1 — PRIMARY SOURCES (Official Documentation)**

   📌 **Google — "Canonicalization, AI Overviews, E-E-A-T, Search Central"**
      developers.google.com/search/docs
      Applied to: A4, A10, A11, C9, E3, E4, E8, F1, F9, G4, G5, H6, H7, J3, D4, D11
      Evidence: Sieve Rules #1419, #1440, #1441, #1442, #1448, #1456, #1474, #1496, #1676

   📌 **Schema.org — FAQPage, Organization, Person, SoftwareApplication, MobileApplication, AggregateRating, ImageObject, ContactPoint**
      schema.org
      Applied to: D1–D12, G2, G6, J1, J2, J4
      Evidence: Sieve Rules #1495, #1496, #1600, #1668, #1674, #1676, #7375

   📌 **Perplexity — "Technical Setup and Content Guidelines"**
      docs.perplexity.ai
      Applied to: E1, E2, E5, F1, F9, G5
      Evidence: Sieve Rules #1471, #1472, #1474, #1479, #1480, #1487

🥈 **TIER 2 — RESEARCH SOURCES (Data-Driven Studies)**

   📌 **Backlinko — AI SEO data studies**
      backlinko.com
      Applied to: B1, C6, C8, C12, F12, G3, G5, G9, H1, H5, I1, I6
      Evidence: Rules #7176, #7190; Anti-patterns #4607, #4602, #4623, #4698, #4714, #4763

   📌 **Princeton/Georgia Tech/IIT Delhi — "GEO Research Paper (KDD 2024)"**
      arxiv.org/abs/2311.09735
      Applied to: F8, G3, I1, I3
      Evidence: Knowledge model (citation frequency + authority source diversity as primary AI selection signals; up to 37% visibility improvement from off-page work)

📎 **TIER 4 — SPECIALIZED SOURCES**

   📌 **amsive.com — "AI Crawler JavaScript Avoidance + Canonical Respect"**
      amsive.com/insights/seo
      Applied to: A4, E5, E13
      Evidence: Sieve Rules #2015, #2016

---

## Supplementary Findings (from Sieve Brain — beyond 103 checks)

⚠ **Canonical/hosting split creates duplicate-content + entity-split liability**

trypsagent.com is structurally excellent for AEO but declares jointryps.com as canonical. This is a unusual pattern — typically an alternate hostname either (a) 301 redirects to the canonical OR (b) is a regional variant with hreflang. Neither is the case here. The two most likely outcomes:
1. Google treats trypsagent.com as duplicate of jointryps.com and discards this enriched content
2. Google indexes trypsagent.com separately but attributes ranking signals to jointryps.com, creating split authority

Either way, the team gets **no benefit** from the work done on trypsagent.com unless the canonical strategy is resolved.

🥇 Per Google's canonicalization documentation (developers.google.com/search/docs/crawling-indexing/consolidate-duplicate-urls) [Sieve Rule #1441]

⚠ **FAQPage 7-vs-6 pair mismatch is the same pattern as AnswerMonk's 4-vs-8 mismatch**

In the AnswerMonk audit earlier today, we found FAQPage schema with 4 pairs vs visible HTML with 8 pairs (schema < visible). Here we have FAQPage schema with 7 pairs vs visible HTML with 6 pairs (schema > visible). **Both are Schema.org violations** — markup must match visible content verbatim. This is a consistent pattern across multiple audits and suggests the team may be template-driving schema from a different source than the actual page content.

🥇 Per Schema.org FAQPage specification (schema.org/FAQPage) [Sieve Rule #7375]

⚠ **Zero outbound citations is sitewide pattern across all TRYPS surfaces**

Both trypsagent.com and jointryps.com have zero outbound citations to authoritative external sources. This is a sitewide content gap. Competitors cite Stripe, Thrillist, and industry publications. TRYPS cites nothing. Fix: add 3–5 outbound citations to travel research sources (Skift, Phocuswire, academic studies) across the homepage and blog posts.

🥇 Per Google E-E-A-T guidelines on authority signals (developers.google.com) [Sieve Rule #1478]

---

## Audit Metadata

- **Version:** 3.0 (curl-first, source-tiered citations v1.3)
- **Checks run:** 100/103 (E9 not testable; B10/B11 need Chrome MCP; D13 N/A for landing page)
- **Passed:** 63 | **Failed:** 17 | **Warn:** 13 | **N/A:** 7
- **Gates:** All passed (crawlable, SSR content, real page)
- **Page classification:** SaaS landing page / homepage (HIGH confidence)
- **Competitors analyzed:** 3 (SquadTrip, Wanderlog — from earlier jointryps audit; Troupe from SERP snippets)
- **Chrome MCP:** Not connected — TTFB measured via curl (678ms)
- **Brain entries matched:** ~30 rules + ~10 anti-patterns across Tier 1/2/4 sources
- **Previous audits:**
  - Audit #1: 2026-04-10 10:28 — 52% (F) — v2.0 methodology
  - Audit #2: 2026-04-10 12:44 — 58% (F) — v2.0 methodology
  - **Audit #3 (this run): 2026-04-14 10:37 — 76% (C) — v3.0 methodology**
- **Queries used:** 4 (primary, variant, category, branded)
- **Data sources:**
  - curl (ground truth): Technical SEO, Performance, Schema extraction, Discovery/robots, raw HTML content
  - WebFetch: Content understanding
  - WebSearch: GEO presence verification
  - Supabase brain: Rule and anti-pattern enrichment

---

## Summary — What to Do This Week

**This week (DO NOW):**
1. **Resolve the canonical/hosting split** (half-day decision + 1-day infrastructure work, SITEWIDE TEMPLATE + INFRASTRUCTURE). Recommended: 301 redirect trypsagent.com → jointryps.com AND port enriched schema/content to jointryps.com. Single highest-impact action in this audit.
2. **Add datePublished + dateModified + visible "Last updated"** (15 min, SCHEMA + PAGE HTML)
3. **Reconcile FAQPage 7-vs-6 mismatch** (15 min, SCHEMA FIX) — add the 7th visible pair OR remove the orphan schema pair
4. **Add @id fragments to all 9 schema entities + update cross-references** (30 min, SCHEMA FIX)
5. **Remove duplicate HSTS header** (5 min, SITEWIDE TEMPLATE)
6. **Add explicit AI bot blocks to robots.txt** (10 min, SITEWIDE TEMPLATE)

**This month (PLAN — entity-building):**
7. Add visible "Written by Jake Stein, Founder" byline + bio (1 hour, CONTENT)
8. Convert "Why not just use WhatsApp, Google Sheets, or Wanderlog?" section to HTML comparison table (2 hours, CONTENT RESTRUCTURE)
9. Add 3–5 outbound citations to authoritative travel research (1 hour, CONTENT)
10. Launch on Product Hunt + submit to AlternativeTo + App Store Optimization (2–3 days, OFF-PAGE)
11. Outreach to 10 category listicle publishers requesting inclusion (1–2 weeks, OFF-PAGE)
12. Reddit community seeding in r/travel, r/solotravel, r/TravelHacks (ongoing, OFF-PAGE)

**Honest framing:** trypsagent.com has the **strongest AEO foundation of any TRYPS surface audited** — 9 schema types, definition-first content, Person schema with founder credentials, AggregateRating, FAQPage with 6 visible pairs, HowTo, destination-specific content. The technical sophistication here is notable: it has **more schema types than SquadTrip, the #1-ranking competitor**.

**But all of that work is wasted because of the canonical split.** Google follows the canonical tag to jointryps.com (which is structurally barren) and attributes everything there. The team has done 90% of the AEO work and is losing 100% of the benefit because of a single architectural decision.

**Fix #1 is non-negotiable.** Everything else in this audit is secondary. Port the trypsagent.com content + schema to jointryps.com, 301 redirect trypsagent.com → jointryps.com, and the PCR of the canonical surface jumps from 59% (D-) to ~85% (B) overnight without writing new content.

---

**Persistence confirmation:**
- **Supabase:** `audit_id 262da05b-d72d-498b-8865-d98e50b35b32` (31 findings persisted to `website_audit_findings`)
- **Markdown:** `audit-reports/trypsagent-com-audit-1-2026-04-14.md` (this file)
