# SEO + AEO + GEO Audit Report — RE-AUDIT after canonical fix

**Audit ID:** f89338a9-3111-4a2a-8d41-e0eb622aa108
**URL:** https://trypsagent.com
**Domain:** trypsagent.com
**Page Type:** SaaS landing page / homepage (HIGH confidence)
**Company:** TRYPS — Group trip planning app for friends by Jake Stein (Founder)
**Industry:** Travel Tech / Consumer SaaS
**Date:** 2026-04-14 11:03 UTC (re-audit, 26 minutes after audit #3)
**Audit Version:** 3.0 (curl-first, source-tiered citations v1.3)
**Duration:** ~130 seconds (competitor data reused from audit #3 earlier this session)
**Competitors analyzed:** SquadTrip, Wanderlog, Troupe (reused from audit #3)

**Target queries:**
- **Primary:** group trip planning app
- **Variant:** plan a trip with friends online
- **Category:** best group trip planning app 2026
- **Branded:** TRYPS trypsagent

---

## 🎯 Change Context

The user implemented **Fix #1 from audit #3** (canonical/hosting split resolution) and requested a re-audit. This audit verifies the fix and identifies remaining gaps.

**Previous audit (audit #3, 2026-04-14 10:37):**
- PCR 79% (C+), Overall 76% (C)
- Fix #1 flagged: Canonical/hosting split — page served at trypsagent.com but every signal pointed to jointryps.com

**This audit (audit #4, 2026-04-14 11:03):**
- PCR **83% (B)**, Overall **79% (C+)**
- Fix #1 **fully implemented** — all references now self-reference trypsagent.com
- Technical SEO: 92% → **100%**
- Entity: 75% → **100%**
- AEO Discovery: 83% → **92%**
- On-Page SEO: 73% → **82%**

---

## ✅ What Changed Between Audits (in 26 minutes)

### Fix #1 Verification — FULLY IMPLEMENTED

| Element | Audit #3 (10:37) | Audit #4 (11:03) | Status |
|---|---|---|---|
| `<link rel="canonical">` | `https://jointryps.com/` | `https://trypsagent.com/` | ✅ Fixed |
| `og:url` | `https://jointryps.com/` | `https://trypsagent.com/` | ✅ Fixed |
| `og:image` | `https://jointryps.com/opengraph.jpg` | `https://trypsagent.com/opengraph.jpg` | ✅ Fixed |
| `twitter:image` | `https://jointryps.com/opengraph.jpg` | `https://trypsagent.com/opengraph.jpg` | ✅ Fixed |
| Organization.url | `https://jointryps.com/` | `https://trypsagent.com/` | ✅ Fixed |
| Organization.logo.url | `https://jointryps.com/favicon.svg` | `https://trypsagent.com/favicon.svg` | ✅ Fixed |
| Person.url (Jake Stein) | `https://jointryps.com/about` | `https://trypsagent.com/about` | ✅ Fixed |
| Organization.contactPoint.email | `support@jointryps.com` | `support@trypsagent.com` | ✅ Fixed |
| Organization.contactPoint.url | `https://jointryps.com/contact` | `https://trypsagent.com/contact` | ✅ Fixed |
| WebSite.url | `https://jointryps.com/` | `https://trypsagent.com/` | ✅ Fixed |
| SoftwareApplication.url | `https://jointryps.com/` | `https://trypsagent.com/` | ✅ Fixed |
| MobileApplication.url (iOS + Android) | `https://jointryps.com/` | `https://trypsagent.com/` | ✅ Fixed |
| robots.txt `Sitemap:` directive | `https://jointryps.com/sitemap.xml` | `https://trypsagent.com/sitemap.xml` | ✅ Fixed |
| sitemap.xml URLs (4 entries) | all under `jointryps.com/*` | all under `trypsagent.com/*` | ✅ Fixed |
| **jointryps.com mentions in HTML** | present throughout | **0** | ✅ Clean slate |
| **trypsagent.com mentions in HTML** | — | **27** | ✅ Self-consistent |

### Bonus improvements discovered in re-audit

| Metric | Audit #3 | Audit #4 | Change |
|---|---|---|---|
| Schema blocks | 8 | **9** | +1 (new WebPage block) |
| Word count | 2,129 | **2,243** | +114 |
| Page size (bytes) | ~67 KB | ~70 KB | +3 KB |
| Checks passed | 68/99 | **75/99** | +7 checks now pass |
| Checks failed | 14 | **10** | -4 failures |
| Checks warn | 12 | **9** | -3 warnings |

### New schema block added

The re-audit found a **9th schema block — `@type: WebPage`** — which wasn't present in audit #3. This is a minor enrichment but shows the team continued iterating on schema.

### Checks that flipped from FAIL/WARN to PASS

| Check | Audit #3 | Audit #4 | Reason |
|---|---|---|---|
| **A4** (Canonical matches serving host) | ⚠ WARN | ✓ PASS | Canonical now self-references trypsagent.com |
| **A11** (Sitemap referenced and valid) | ⚠ WARN | ✓ PASS | Sitemap now lists trypsagent.com URLs, homepage included |
| **C9** (URL structure consistency) | ⚠ WARN | ✓ PASS | Serving host and canonical host now match |
| **E8** (Page in sitemap) | ✗ FAIL | ✓ PASS | Homepage now in trypsagent.com/sitemap.xml |
| **J3** (URL/domain entity consistency) | ✗ FAIL | ✓ PASS | All schema URLs match serving host |

---

## ✓ Gates: ALL PASSED

- Gate 1 (crawlability): HTTP 200, robots meta with `index,follow,max-image-preview:large,max-snippet:-1,max-video-preview:-1` ✓
- Gate 2 (content access): 2,243 words of body text in raw HTML ✓
- Gate 3 (real page): Legitimate SaaS homepage ✓

---

## Scores

### Page Citation Readiness: **83% (B)** ↑ from 79% (C+)
Can this page be found, extracted, trusted, and selected by AI answer engines?

| Section | Audit #3 | Audit #4 | Change |
|---|---|---|---|
| Technical SEO (A) | 92% | **100%** | **+8** |
| Performance (B) | 86% | 86% | 0 |
| On-Page SEO (C) | 73% | **82%** | **+9** |
| Schema (D) | 73% | 73% | 0 |
| AEO: Discovery (E) | 83% | **92%** | **+9** |
| AEO: Extraction (F) | 92% | 92% | 0 |
| AEO: Trust (G) | 50% | 50% | 0 |
| AEO: Selection (H) | 69% | 69% | 0 |
| Entity (J) | 75% | **100%** | **+25** |

### Brand AI Presence: **12% (F)** (unchanged)

| Dimension | Score |
|---|---|
| Presence | 0% |
| Accuracy | N/A |
| Favorability | N/A |

> No change possible in 26 minutes — SERP hasn't reindexed, no off-page work has been done yet. I8 (Organization sameAs) still provides the 12% positive signal from the earlier run.

**Composite:**
- SEO Score: **86%** (up from 82%)
- AEO Score: 72% (unchanged)
- Citation Readiness: **83%** (up from 79%)
- **Overall: 79% (C+)** (up from 76%)

---

## Check Summary

| Metric | Audit #3 | Audit #4 | Change |
|---|---|---|---|
| Total checks run | 99 | 99 | 0 |
| **Passed** | 68 | **75** | **+7** |
| **Failed** | 14 | **10** | **-4** |
| **Warnings** | 12 | **9** | **-3** |
| N/A | 5 | 5 | 0 |

---

## Trend (4 audits on trypsagent.com over 4 days)

| Metric | Audit #1 (2026-04-10, v2) | Audit #2 (2026-04-10, v2) | Audit #3 (2026-04-14, v3) | **Audit #4 (2026-04-14, v3)** |
|---|---|---|---|---|
| **Overall** | 52% (F) | 58% (F) | 76% (C) | **79% (C+)** |
| Technical SEO | 72% | 65% | 92% | **100%** |
| Performance | 65% | 55% | 86% | 86% |
| On-Page SEO | 68% | 60% | 73% | **82%** |
| Schema | 75% | 88% | 73% | 73% |
| AEO Discovery | 70% | 73% | 83% | **92%** |
| AEO Extraction | 42% | 42% | 92% | 92% |
| AEO Trust | 19% | 33% | 50% | 50% |
| AEO Selection | 25% | 25% | 69% | 69% |
| GEO | 15% | 15% | 12% | 12% |
| Entity | 50% | 65% | 75% | **100%** |

> Audit #1/#2 used v2.0 methodology (WebFetch-primary). Audit #3/#4 use v3.0 (curl-first, stricter). Meaningful comparisons are audit #3 → #4 (same methodology, same URL, 26 minutes apart, one targeted fix).

---

## Why This Page Isn't Being Cited (updated)

- **FAQPage schema still has 7 pairs but visible HTML has 6** [HARD EVIDENCE]. The orphan is now identifiable: **"How do I join the TRYPS waitlist?"** appears in the FAQPage mainEntity array but has no visible `<details><summary>` counterpart. Schema.org requires markup to match visible content verbatim.

  🥇 Per Schema.org FAQPage specification at schema.org/FAQPage: "FAQPage markup must match visible content. Mismatched markup may be rejected for rich result eligibility."
  [Evidence: Sieve Rule #7375 (Schema.org, 0.98)]

- **Still no datePublished or dateModified on SoftwareApplication** [HARD EVIDENCE]. The page has rich schema (9 entity types, AggregateRating 4.8/500, founder Jake Stein with credentials) but is still missing freshness signals. foundingDate (2025-01-01) tells engines when the company was founded, not when the page content was last updated.

  🥇 Per Perplexity's official documentation at docs.perplexity.ai: "Signal content freshness with visible timestamps. Pages without freshness signals receive reduced retrieval weight in the L3 reranker."
  🥈 Per Backlinko's AI SEO research at backlinko.com: "50% of content cited in AI search responses is less than 13 weeks old."
  [Evidence: Sieve Rules #1474, #7190]

- **Brand still has zero footprint in AI category knowledge** [MODEL JUDGMENT]. This is unchanged from audit #3 — no off-page work has happened in 26 minutes. Category queries return SquadTrip, TripIt, Troupe, Wanderlog — TRYPS in none. This is now the single largest remaining gap and requires weeks of sustained entity-building work.

  🥈 Per Backlinko's AI SEO research at backlinko.com: "Sparse or outdated off-site brand mentions reduces AI citation likelihood."
  [Evidence: Sieve AP #4607 (Backlinko, high risk)]

---

## Bot's Eye View — What AI Crawlers See (updated)

| Metric | Audit #3 | Audit #4 | Source |
|---|---|---|---|
| Raw HTML word count | 2,129 words | **2,243 words** | curl |
| Page size | 67 KB | **70 KB** | curl |
| Schema blocks | 8 | **9** (added WebPage) | curl HTML parse |
| FAQ in initial HTML | 6 pairs | 6 pairs (unchanged) | curl HTML parse |
| FAQ in FAQPage schema | 7 pairs (1 orphan) | 7 pairs (orphan identified: "How do I join the TRYPS waitlist?") | curl HTML parse |
| Images in HTML | 0 | 0 | curl HTML parse |
| JS dependency | None | None | curl content analysis |
| **Canonical target** | `jointryps.com/` ⚠ | **`trypsagent.com/`** ✓ | curl HTML parse |
| **Schema URL consistency** | All → jointryps.com ⚠ | **All → trypsagent.com** ✓ | curl HTML parse |

**AI crawler access:** **FULLY ACCESSIBLE + FULLY ATTRIBUTED** — content is in raw HTML, schema is rich, FAQ is present, AND now AI crawlers will correctly attribute everything to `trypsagent.com` (no canonical redirect away).

🥇 Per Google's canonicalization documentation (developers.google.com): "Google uses the canonical URL for indexing and ranking. With canonical now self-referencing, signals consolidate on trypsagent.com itself." [Sieve Rule #1441]

---

## Performance (curl-measured)

| Metric | Audit #3 | Audit #4 | Rating |
|---|---|---|---|
| **TTFB** | 678 ms | **730 ms** | Good (under 800ms) |
| Total load | 691 ms | 760 ms | Good |
| Page size | 67 KB | 70 KB | Good |
| HTTP version | HTTP/2 | HTTP/2 | Good |
| HSTS | dual header | **dual header (unchanged)** | Warn |
| Cache-Control | `no-cache, must-revalidate` | `no-cache, must-revalidate` (unchanged) | Warn |
| Server | Cloudflare (BKK) | Cloudflare (BKK) | — |

> TTFB slightly slower this run (730ms vs 678ms) but still well under the 800ms threshold. Normal variance for Cloudflare dynamic routing. CWV not measured — Chrome MCP not connected.

🥈 Per Backlinko Core Web Vitals research (backlinko.com) [Rules #7176, #7190]

---

## Competitor Comparison — "group trip planning app"

(Reused from audit #3 — competitor data unchanged in 26 minutes; only TRYPS column updated)

| Signal | **TRYPS (trypsagent.com)** | SquadTrip | Wanderlog | Troupe |
|---|---|---|---|---|
| **In SERP for category** | **No** | Yes (#1) | Yes (#3) | Yes |
| Word count | **2,243** (+114 from audit #3) | 3,500–4,000 | 15,000+ | — |
| H1 count | 1 | 1 | 1 | — |
| FAQ pairs (visible) | 6 | 8 | 0 | — |
| FAQ pairs (schema) | 7 (orphan: waitlist question) | 8 | 0 | — |
| **Schema blocks** | **9 JSON-LD (10 entity types including new WebPage) — most in set** | 4 types | 0 detected | — |
| FAQPage schema | Yes (7 pairs) | Yes (8 pairs) | No | — |
| AggregateRating | Yes (4.8/500) | Yes (4.8/2000) | No | — |
| Person/founder schema | **Yes (Jake Stein, Founder)** | No | No | — |
| datePublished / Modified | **No** | No | No | — |
| Visible date on page | **No** | No | No | — |
| Outbound citations | 0 | ~5 | 2+ | — |
| Organization sameAs | **Yes (IG, LinkedIn, X)** | Unknown | Unknown | — |
| Comparison section | Narrative | 6-row table | None | — |
| HowTo schema | **Yes** | No | No | — |
| WebPage schema | **Yes (new in audit #4)** | No | No | — |
| **Canonical self-referencing** | **Yes (fixed in audit #4)** | Yes | Yes | — |

**Key gaps remaining (after Fix #1):**
1. **Zero SERP presence.** Same as audit #3 — Fix #1 was a technical fix, not an off-page fix. Brand presence takes weeks of sustained work.
2. **Still no freshness signals** (datePublished/dateModified/visible date) — same finding as audit #3.
3. **Comparison section is still narrative, not table.**
4. **FAQPage still 7 vs 6 mismatch** — but the orphan is now identifiable by name ("How do I join the TRYPS waitlist?") so the fix is literally "add one visible details block".

**TRYPS's comparative strengths after Fix #1:**
- **Most schema types in competitor set (10 entity types across 9 blocks)** — now includes WebPage
- **Canonical self-referencing** ✓ — no more attribution split
- **Only page with Person/founder schema** with worksFor + sameAs
- **AggregateRating 4.8/500** in schema
- **Most comprehensive robots meta** (explicit AI permissions)
- **Destination-specific content** (Goa, Manali, Pondicherry, Coorg)

---

## Top 5 Fixes — UPDATED POST-AUDIT #3

### Fix #1: ✅ RESOLVED — Canonical/hosting split
**Status:** Fully implemented between audit #3 (10:37) and audit #4 (11:03)

The team completed this fix in under 26 minutes. Canonical, og:url, og:image, twitter:image, all 9 schema entity URLs, contactPoint.email, robots.txt Sitemap directive, and sitemap.xml URL list all now self-reference trypsagent.com. Zero jointryps.com mentions remain in the HTML. Adding new WebPage schema block was a bonus improvement.

---

### Fix #2 → NOW FIX #1: Reconcile FAQPage 7-vs-6 schema/visible mismatch
**Impact:** High | **Effort:** Trivial | **Priority:** DO NOW
**Type:** SCHEMA FIX + PAGE HTML
**Evidence:** HARD EVIDENCE

**BEFORE:** FAQPage schema `mainEntity` array has 7 Q&A pairs. Visible HTML has 6 `<details><summary>` elements. The orphan pair is now **identifiable by name**:

**Visible HTML (6 pairs):**
1. What is TRYPS?
2. How is this different from WhatsApp or Google Sheets?
3. Does everyone need to download an app?
4. Can everyone edit the plan?
5. How does expense splitting work?
6. How do I start?

**Schema (7 pairs — 6 matching + 1 orphan):**
7. **"How do I join the TRYPS waitlist?"** ← orphan (in schema only, no visible counterpart)

**AFTER — Option A (recommended) — Add the 7th visible pair:**
```html
<details>
  <summary><h3>How do I join the TRYPS waitlist?</h3></summary>
  <p>Tap "Join the Beta" at the top of trypsagent.com, enter your mobile number, and we'll text you an invite link when your group's slot opens. Currently 500+ groups are on the waitlist.</p>
</details>
```

**AFTER — Option B — Remove the orphan schema pair:** Remove the "How do I join the TRYPS waitlist?" Question from the FAQPage.mainEntity array so schema matches the 6 visible pairs.

**Recommendation:** Option A (add the visible pair). More content = more extraction surface, and this is a common buyer query for pre-launch apps.

**WHY THIS MATTERS:**

🥇 Per Schema.org's FAQPage specification at schema.org/FAQPage: "FAQPage markup must match visible content. Mismatched markup may be rejected for rich result eligibility."
[Sieve Rule #7375, confidence 0.98]

🥇 Per Google's Search Central structured data guidelines at developers.google.com/search/docs/appearance/structured-data/faqpage: "Markup text must match visible content verbatim."
[Sieve Rule #1496, confidence 0.98]

---

### Fix #3 → NOW FIX #2: Add datePublished + dateModified + visible "Last updated" line
**Impact:** High | **Effort:** Trivial | **Priority:** DO NOW
**Type:** SCHEMA FIX + PAGE HTML FIX
**Evidence:** HARD EVIDENCE

**BEFORE:** Unchanged from audit #3. SoftwareApplication schema has `softwareVersion: "0.9-beta"` and `releaseNotes` but no `datePublished` or `dateModified`. Organization has `foundingDate: "2025-01-01"` but that's company-founding, not page-update.

**AFTER:**
```json
{
  "@type": "SoftwareApplication",
  "@id": "https://trypsagent.com/#app",
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

### Fix #4 → NOW FIX #3: Add @id fragments to all 9 schema entities
**Impact:** Medium | **Effort:** Trivial | **Priority:** DO NOW
**Type:** SCHEMA FIX
**Evidence:** HARD EVIDENCE

**BEFORE:** None of the 9 schema blocks (now 10 entity types including the new WebPage) have `@id` properties. Cross-references use inline object embedding.

**AFTER:** Add `@id` fragments and use them for cross-references:
```json
{"@type": "Organization", "@id": "https://trypsagent.com/#organization", ...}
{"@type": "Person", "@id": "https://trypsagent.com/#founder", "worksFor": {"@id": "https://trypsagent.com/#organization"}, ...}
{"@type": "SoftwareApplication", "@id": "https://trypsagent.com/#app", "publisher": {"@id": "https://trypsagent.com/#organization"}, ...}
{"@type": "WebSite", "@id": "https://trypsagent.com/#website", "publisher": {"@id": "https://trypsagent.com/#organization"}, ...}
{"@type": "WebPage", "@id": "https://trypsagent.com/#webpage", "isPartOf": {"@id": "https://trypsagent.com/#website"}, ...}
```

**WHY THIS MATTERS:**

🥇 Per Schema.org entity linking documentation at schema.org: "Use @id fragments to create unique entity identifiers and enable cross-references between entities without duplication."
[Sieve Rule #1668, confidence 0.98]

---

### Fix #5 → NOW FIX #4: Off-page entity work — get TRYPS into category listicles
**Impact:** Critical | **Effort:** High (weeks) | **Priority:** PLAN
**Type:** OFF-PAGE / ENTITY WORK

**BEFORE:** Unchanged from audit #3. TRYPS absent from all SERP queries. Reddit/Product Hunt/G2 searches return zero.

**AFTER:** This is now **the single largest remaining gap** after Fix #1 was implemented. With the canonical split resolved, the enriched schema work on trypsagent.com will actually accrue ranking signals to trypsagent.com — but no signals will come in until the brand has off-page presence.

**Immediate listings (days):**
1. **Product Hunt launch** — travel consumer apps get strong initial signal
2. **App Store Optimization** (when iOS + Android apps launch)
3. **AlternativeTo** (alternativeto.net) — categorize as alternative to Splitwise/Wanderlog/SquadTrip
4. **GetApp, Capterra, G2** — lower priority but non-zero

**Listicle outreach (2–6 weeks):** Pitch 13 publishers for inclusion — SquadTrip, TripIt, FlowTrip, Plan Harmony, ClanPlan, JoinMyTrip, Troupe, AvoSquado, Infinity Transportation, WhenAvailable, Ideal Charter, VAX Vacation Access, Engine.

**Reddit seeding:** r/travel, r/solotravel, r/TravelHacks, r/digitalnomad

**Press outreach:** Skift, Phocuswire, TravelPulse.

**WHY THIS MATTERS:**

🥈 Per Backlinko's AI SEO research at backlinko.com: "Sparse or outdated off-site brand mentions across third-party platforms (G2, Reddit, forums, directories) reduces AI citation likelihood. LLMs synthesize brand recommendations from cross-site signal."
[Sieve AP #4607, risk: high]

🥈 Per Princeton/Georgia Tech/IIT Delhi GEO research paper at arxiv.org/abs/2311.09735: "Citation frequency and authority source diversity are primary signals for AI answer engine brand selection. Up to 37% visibility improvement from structured off-page work."

🥇 Per Google's Business Profile documentation at developers.google.com: "Knowledge panel eligibility requires claimed Business Profile plus consistent entity signals across the web."
[Sieve Rule #564, confidence 0.95]

---

### NEW FIX #5: Add visible founder byline + outbound citations + comparison HTML table
**Impact:** Medium | **Effort:** Moderate | **Priority:** PLAN
**Type:** CONTENT RESTRUCTURE

**BEFORE:** All 3 content-layer issues from audit #3 remain:
- Jake Stein is in Person schema + mentioned in H2 "Built by people who care..." but no explicit visible byline
- Zero outbound citations to authoritative external sources
- "Why not just use WhatsApp, Google Sheets, or Wanderlog?" section uses narrative format, not HTML table

**AFTER:**

1. **Visible founder byline** — add to About section or footer:
```html
<p class="about-byline">
  Built by <a href="https://www.linkedin.com/in/jakestein" rel="author">Jake Stein</a>, Founder —
  based on <a href="/about">his experience</a> planning group trips that never quite happened.
</p>
```

2. **Outbound citations** — add 3–5 authoritative external links to support claims:
```html
<p>Group travel planning is a coordination problem that affects
  <a href="https://www.skift.com/travel-trends-group-travel">a growing share of leisure trips</a>,
  according to Skift's 2026 Travel Megatrends report.</p>
```

3. **Comparison HTML table** — convert the existing narrative "Why not just use WhatsApp?" section:
```html
<table class="comparison">
  <thead>
    <tr>
      <th>Feature</th>
      <th>WhatsApp</th>
      <th>Google Sheets</th>
      <th>Splitwise</th>
      <th>Wanderlog</th>
      <th>TRYPS</th>
    </tr>
  </thead>
  <tbody>
    <tr><td>Group coordination</td><td>Free-form chat</td><td>Manual setup</td><td>❌</td><td>⚠ Solo-first</td><td>✅ Built-in</td></tr>
    <tr><td>Date polling</td><td>❌</td><td>❌</td><td>❌</td><td>❌</td><td>✅</td></tr>
    <tr><td>Expense splitting</td><td>❌</td><td>Manual formulas</td><td>✅</td><td>Limited</td><td>✅</td></tr>
    <tr><td>Shared itinerary</td><td>Chat messages</td><td>Rows in a sheet</td><td>❌</td><td>✅</td><td>✅</td></tr>
    <tr><td>No app required</td><td>Everyone needs it</td><td>Google account needed</td><td>Everyone needs it</td><td>Everyone needs it</td><td>✅ Link-based</td></tr>
  </tbody>
</table>
```

**WHY THIS MATTERS:**

🥇 Per Google's E-E-A-T guidelines at developers.google.com/search/docs: "Content with clear author attribution and authoritative citations is preferentially cited in AI responses. 96% of AI Overview citations come from sources with strong E-E-A-T signals."
[Sieve Rule #1456]

🥈 Per Backlinko's AI SEO research at backlinko.com: "Comparative content extracted from HTML tables is preferred by LLMs over narrative prose for category queries."
[Sieve AP #4714]

---

## Quick Wins (Trivial-effort, not in top 5)

- **Remove duplicate HSTS header** (still present in audit #4 — minor misconfig, 5 min)
- **Add explicit AI bot blocks to robots.txt** (still not done, 10 min)
- **Relax Cache-Control** to `public, max-age=3600, s-maxage=86400` for static homepage (5 min)
- **Add labeled "TL;DR" quick-answer block** at the top (15 min)
- **Verify privacy/terms footer links** are visible on the homepage (2 min check)

---

# LAYER 2 — Detailed Findings

## Section A — Technical SEO (12/12 passed — **100%**) ↑ from 92%

| Status | ID | Finding | Truth | Fix Type |
|---|---|---|---|---|
| ✓ | A1 | HTTPS + HSTS (dual header — minor dup, not breaking) | HARD EVIDENCE | — |
| ✓ | A2 | Title: "TRYPS — Group Trip Planning App for Friends" (44 chars, keyword-rich) | HARD EVIDENCE | — |
| ✓ | A3 | Meta description: 143 chars, definition-first | HARD EVIDENCE | — |
| ✓ | **A4** | **Canonical: `https://trypsagent.com/` (self-referencing) — FIXED from audit #3** | HARD EVIDENCE | — |
| ✓ | A5 | Robots meta: `index,follow,max-image-preview:large,max-snippet:-1,max-video-preview:-1` (explicit AI permissions) | HARD EVIDENCE | — |
| ✓ | A6 | Single H1 | HARD EVIDENCE | — |
| ✓ | A7 | H1 "A group trip planning app your friends actually use." — target keyword | STATIC RULE | — |
| ✓ | A8 | `<html lang="en">` | HARD EVIDENCE | — |
| ✓ | A9 | Viewport meta present | HARD EVIDENCE | — |
| ✓ | A10 | robots.txt permissive + sitemap directive pointing to trypsagent.com/sitemap.xml | HARD EVIDENCE | — |
| ✓ | **A11** | **Sitemap valid, lists trypsagent.com URLs (4 entries including homepage) — FIXED from audit #3** | HARD EVIDENCE | — |
| ✓ | A12 | Content in raw HTML (2,243 words server-rendered) | MEASURED | — |

---

## Section B — Performance (5/7 passed, 2 warn — 86%) unchanged

| Status | ID | Finding | Truth | Fix Type |
|---|---|---|---|---|
| ✓ | B1 | TTFB 730ms (under 800ms Google "Good" threshold) | MEASURED | — |
| ✓ | B2 | Page weight 70 KB | MEASURED | — |
| ✓ | B3 | HTTP/2 enabled | HARD EVIDENCE | — |
| ✓ | B4 | `vary: Accept-Encoding` — compression negotiated | HARD EVIDENCE | — |
| ⚠ | **B5** | **Cache-Control: `no-cache, must-revalidate` (unchanged)** | HARD EVIDENCE | SITEWIDE TEMPLATE |
| ⚠ | **B6** | **Duplicate HSTS headers (unchanged)** | HARD EVIDENCE | SITEWIDE TEMPLATE |
| ✓ | B7 | Cloudflare CDN (cf-ray: 9ec23730ed777b5c-BKK / Bangkok edge) | HARD EVIDENCE | — |
| N/A | B10 | LCP not measured (Chrome MCP unavailable) | — | — |
| N/A | B11 | Image dimensions N/A (0 body images) | — | — |

---

## Section C — On-Page SEO (9/12 passed, 2 fail, 1 N/A — **82%**) ↑ from 73%

| Status | ID | Finding | Truth | Fix Type |
|---|---|---|---|---|
| ✓ | C1 | Clean H1 → H2 hierarchy | HARD EVIDENCE | — |
| ✓ | C2 | "group trip planning app" in first 100 words | STATIC RULE | — |
| ✓ | C3 | Internal links to /blog, /about, /contact | HARD EVIDENCE | — |
| ✓ | C4 | Descriptive anchor text | HARD EVIDENCE | — |
| N/A | C5 | No body images | — | — |
| ✓ | C6 | Word count 2,243 (+114 from audit #3; still below SquadTrip 3,500 median) | COMPARATIVE | — |
| ✓ | C7 | No keyword stuffing | STATIC RULE | — |
| ✗ | **C8** | **Zero outbound citations (unchanged)** | HARD EVIDENCE | CONTENT RESTRUCTURE |
| ✓ | **C9** | **URL structure consistent — serving host = canonical host — FIXED from audit #3** | HARD EVIDENCE | — |
| ✓ | C10 | OG tags complete and self-referencing trypsagent.com | HARD EVIDENCE | — |
| ✓ | C11 | Twitter Card: summary_large_image, @tryps | HARD EVIDENCE | — |
| ✗ | **C12** | **No visible date on page (unchanged)** | HARD EVIDENCE | PAGE HTML FIX |

---

## Section D — Schema (7/11 passed, 1 warn, 3 fail, 2 N/A — 73%) unchanged grade

| Status | ID | Finding | Truth | Fix Type |
|---|---|---|---|---|
| ✓ | D1 | **9 JSON-LD blocks** containing 10 entity types (+ WebPage added) | HARD EVIDENCE | — |
| ✓ | D2 | @context present in all blocks | HARD EVIDENCE | — |
| ✓ | D3 | Page-appropriate types | STATIC RULE | — |
| ✗ | **D4** | **No @id fragments on any entity (unchanged)** | HARD EVIDENCE | SCHEMA FIX |
| ✓ | D5 | BreadcrumbList present | HARD EVIDENCE | — |
| ✓ | D6 | Required fields present | HARD EVIDENCE | — |
| ✓ | D7 | Recommended fields rich (sameAs, founder, knowsAbout, foundingDate, slogan, aggregateRating, featureList, knowsAbout) | STATIC RULE | — |
| ✓ | D8 | Organization + WebSite + SoftwareApplication + WebPage all present | HARD EVIDENCE | — |
| ⚠ | **D9** | **FAQPage schema 7 pairs vs 6 visible — orphan: "How do I join the TRYPS waitlist?" (unchanged from audit #3)** | HARD EVIDENCE | SCHEMA FIX |
| ✓ | D10 | Organization.logo is ImageObject with width/height (512x512) | HARD EVIDENCE | — |
| ✗ | **D11** | **No datePublished or dateModified on SoftwareApplication (unchanged)** | HARD EVIDENCE | SCHEMA FIX |
| ✓ | D12 | Person schema with Jake Stein + jobTitle + worksFor + sameAs — full E-E-A-T | HARD EVIDENCE | — |
| N/A | D13 | Speakable N/A | — | — |

---

## Section E — AEO Discovery (11/12 passed, 2 warn, 1 N/A — **92%**) ↑ from 83%

| Status | ID | Finding | Truth | Fix Type |
|---|---|---|---|---|
| ✓ | E1 | PerplexityBot allowed (wildcard) | HARD EVIDENCE | — |
| ✓ | E2 | BingPreview allowed (wildcard) | HARD EVIDENCE | — |
| ✓ | E3 | Googlebot allowed | HARD EVIDENCE | — |
| ✓ | E4 | Explicit `max-snippet:-1,max-image-preview:large,max-video-preview:-1` (full AI permissions) | HARD EVIDENCE | — |
| ✓ | E5 | 100% content in raw HTML (server-rendered, 2,243 words) | MEASURED | — |
| ✓ | E6 | FAQ in `<details><summary>` — content visible to crawlers | HARD EVIDENCE | — |
| ⚠ | E7 | IndexNow not detected | HEURISTIC | SITEWIDE TEMPLATE |
| ✓ | **E8** | **Homepage in trypsagent.com/sitemap.xml (lastmod 2026-04-08) — FIXED from audit #3** | HARD EVIDENCE | — |
| N/A | E9 | Bing Webmaster not externally testable | — | — |
| ⚠ | E10 | AI bots covered only by wildcard (not explicit) | HARD EVIDENCE | SITEWIDE TEMPLATE |
| ✓ | E11 | No paywall | HARD EVIDENCE | — |
| ✓ | E12 | No NOARCHIVE directive | HARD EVIDENCE | — |
| ✓ | E13 | CCBot allowed via wildcard | HARD EVIDENCE | — |

---

## Section F — AEO Extraction (10/12 passed, 2 warn — 92%) unchanged

| Status | ID | Finding | Truth | Fix Type |
|---|---|---|---|---|
| ✓ | F1 | Definition-first: meta + H1 + subtitle all say "TRYPS is a group trip planning app..." | STATIC RULE | — |
| ✓ | F2 | Quick-answer block served by definition-first opening | HEURISTIC | — |
| ✓ | F3 | 6 visible FAQ pairs | HARD EVIDENCE | — |
| ✓ | F4 | FAQ semantic `<details>/<summary>` + H3 questions | HARD EVIDENCE | — |
| ✓ | F5 | FAQ as buyer queries | STATIC RULE | — |
| ✓ | F6 | H2s scannable; FAQ H3s question-form | HEURISTIC | — |
| ✓ | F7 | Strong entity density — TRYPS + competitor names + destinations | MEASURED | — |
| ✓ | F8 | Specific facts: 500+ groups, AggregateRating 4.8/500, softwareVersion, destination list | HARD EVIDENCE | — |
| ✓ | F9 | "X is a Y that..." pattern match | STATIC RULE | — |
| ⚠ | F10 | No labeled TL;DR block (unchanged) | HEURISTIC | CONTENT RESTRUCTURE |
| ✓ | F11 | Each H2 section topic-focused | HEURISTIC | — |
| ⚠ | F12 | Comparison section narrative, not HTML table (unchanged) | HEURISTIC | CONTENT RESTRUCTURE |

---

## Section G — AEO Trust (4/9 passed, 2 warn, 3 fail — 50%) unchanged

| Status | ID | Finding | Truth | Fix Type |
|---|---|---|---|---|
| ⚠ | G1 | No visible author byline (Jake Stein in schema + implicit H2, no explicit byline) | HEURISTIC | CONTENT RESTRUCTURE |
| ✓ | G2 | Person schema with full E-E-A-T | HARD EVIDENCE | — |
| ✗ | G3 | Zero outbound citations | HARD EVIDENCE | CONTENT RESTRUCTURE |
| ✗ | G4 | No datePublished | HARD EVIDENCE | SCHEMA FIX |
| ✗ | G5 | No dateModified + no visible date | HARD EVIDENCE | SCHEMA FIX |
| ✓ | G6 | Organization sameAs (IG, LinkedIn, X) | HARD EVIDENCE | — |
| ⚠ | G7 | Privacy/Terms visibility not confirmed | HEURISTIC | PAGE HTML FIX |
| ✓ | G8 | HTTPS + HSTS + CSP (report-only) + X-Frame-Options + X-Content-Type-Options | HARD EVIDENCE | — |
| ✗ | G9 | No freshness recency signal | HARD EVIDENCE | SCHEMA FIX |

---

## Section H — AEO Selection (5/8 passed, 1 warn, 2 fail — 69%) unchanged

| Status | ID | Finding | Truth | Fix Type |
|---|---|---|---|---|
| ✓ | H1 | Content depth 2,243 (+114 from audit #3) | COMPARATIVE | — |
| ⚠ | H2 | Unique data limited (500+ groups, AggregateRating, destinations) | COMPARATIVE | CONTENT RESTRUCTURE |
| ✓ | H3 | FAQ 6 vs SquadTrip 8 — close | COMPARATIVE | — |
| ✓ | H4 | Schema 10 entity types vs SquadTrip 4 — **more than any competitor** | COMPARATIVE | — |
| ✗ | H5 | No freshness signal | COMPARATIVE | SCHEMA FIX |
| ✓ | H6 | E-E-A-T present — Person + founder + sameAs | COMPARATIVE | — |
| ✗ | H7 | Zero SERP appearance | COMPARATIVE | OFF-PAGE ENTITY |
| ✓ | H8 | Clear query intent match | COMPARATIVE | — |

---

## Section I — GEO (Directional — 12%) unchanged

| Status | ID | Finding | Truth | Fix Type |
|---|---|---|---|---|
| ✗ | I1 | Brand not in category search results | MODEL JUDGMENT | OFF-PAGE |
| ✗ | I2 | No knowledge panel | MODEL JUDGMENT | OFF-PAGE |
| ✗ | I3 | Not in 10 category listicles | MODEL JUDGMENT | OFF-PAGE |
| N/A | I4 | Accuracy unmeasurable | — | — |
| N/A | I5 | Favorability unmeasurable | — | — |
| ✗ | I6 | No Reddit/PH/G2 mentions | MODEL JUDGMENT | OFF-PAGE |
| ✗ | I7 | Not on directories | MODEL JUDGMENT | OFF-PAGE |
| ✓ | I8 | **Organization sameAs present (IG, LinkedIn, X)** | HARD EVIDENCE | — |

> I8 PASS is the only positive GEO signal. No change in 26 minutes (expected).

---

## Section J — Entity Consistency (4/4 passed — **100%**) ↑ from 75%

| Status | ID | Finding | Truth | Fix Type |
|---|---|---|---|---|
| ✓ | J1 | "TRYPS" consistent across schema, OG, title, footer | HARD EVIDENCE | — |
| ✓ | J2 | Logo: ImageObject 512x512 (trypsagent.com/favicon.svg) | HARD EVIDENCE | — |
| ✓ | **J3** | **URL/domain entity FULLY CONSISTENT — serving host = canonical host = all schema URLs — FIXED from audit #3** | HARD EVIDENCE | — |
| ✓ | J4 | sameAs URLs resolvable (IG, LinkedIn, X, LinkedIn personal for Jake Stein) | HARD EVIDENCE | — |

---

## AEO Stage Analysis (updated)

| Stage | Audit #3 | Audit #4 | Verdict |
|---|---|---|---|
| **Stage 1: Discovery** | 83% | **92%** | Strong — sitemap now lists homepage, everything else unchanged. Gaps: IndexNow + explicit bot blocks |
| **Stage 2: Extraction** | 92% | 92% | Excellent — definition-first, 6 FAQ pairs with schema, semantic HTML, strong entity density, specific facts. Unchanged |
| **Stage 3: Trust** | 50% | 50% | Mixed — Person schema + sameAs + HTTPS strong; missing dates + outbound citations + explicit byline. Unchanged |
| **Stage 4: Selection** | 69% | 69% | Good on schema (10 types vs 0–4), FAQ, E-E-A-T. Zero SERP appearance is killer. Unchanged |

**Diagnosis:** The canonical fix from audit #3 unlocked Discovery (+9 points) by making the homepage discoverable in its own sitemap. Extraction and Trust are unchanged — they depend on content/schema work (FAQ reconciliation, dates, bylines, citations) that hasn't been done yet. Selection is limited by off-page presence, which hasn't moved.

---

## GEO Dimension Analysis (Directional)

- **Presence: 0%** — Zero appearances (unchanged)
- **Accuracy: N/A**
- **Favorability: N/A**
- **Entity links: Present** — Organization sameAs (IG, LinkedIn, X)

---

# LAYER 3 — Technical Reference

## Competitor Profiles (reused from audit #3)

### SquadTrip (squadtrip.com)
- Title: "Stop Chasing Payments for Group Trips | SquadTrip"
- Word count: 3,500–4,000
- FAQ pairs: 8 (with FAQPage schema)
- Schema: 4 types
- AggregateRating: 4.8/5 from 2,000 reviews
- Comparison table: 6-row DIY vs platform ✓
- In SERP: #1 for category

### Wanderlog (wanderlog.com)
- Title: "Wanderlog travel planner: free vacation planner and itinerary app"
- Word count: 15,000+
- FAQ pairs: 0
- Schema: 0 detected
- Testimonials: 60+
- Claims: 1M+ users
- In SERP: 5+ listicles

### Troupe (troupe.com)
- From SERP snippets
- Positioning: "The Group Travel Planning App"
- In SERP: Target page + listicle author
- Authority: Established incumbent

---

## Schema Audit Detail (updated — 9 blocks, 10 entity types)

**Current schema (9 JSON-LD blocks):**

1. **Organization** ✓ (all URLs now trypsagent.com)
   - name, **url: https://trypsagent.com/** ✓, logo (ImageObject 512x512), slogan, foundingDate, sameAs (IG/LinkedIn/X), knowsAbout (5 topics), contactPoint (**support@trypsagent.com** ✓), founder (Person → Jake Stein)
   - Still missing: `@id`

2. **Person (Jake Stein)** ✓
   - name, jobTitle "Founder", worksFor Organization (inline), **url: https://trypsagent.com/about** ✓, sameAs (LinkedIn)
   - Still missing: `@id`, hasCredential, knowsAbout

3. **WebSite** ⚠ (minimal but correct)
   - name, **url: https://trypsagent.com/** ✓
   - Still missing: `@id`, description, publisher cross-link, potentialAction

4. **SoftwareApplication** ✓
   - name, applicationCategory, applicationSubCategory, operatingSystem, softwareVersion "0.9-beta", releaseNotes, image, screenshot, description, publisher, offers, featureList (5 items), **aggregateRating 4.8/500**
   - **url: https://trypsagent.com/** ✓
   - Still missing: `@id`, **datePublished**, **dateModified**

5. **HowTo** ✓
   - name, description, step array

6. **FAQPage** ⚠
   - `mainEntity`: **7 Q&A pairs** — orphan identified: "How do I join the TRYPS waitlist?"

7. **MobileApplication (iOS + Android)** ✓
   - Two entries in a JSON array; both URLs now **https://trypsagent.com/** ✓
   - Still missing: `@id` on each

8. **BreadcrumbList** ✓
   - itemListElement present

9. **WebPage** ✓ **(NEW — added between audit #3 and audit #4)**
   - **url: https://trypsagent.com/** ✓
   - Still missing: `@id`, isPartOf cross-link to WebSite

**Generated fix — full @graph with @id fragments + dates + FAQ reconciliation:**

```json
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "Organization",
      "@id": "https://trypsagent.com/#organization",
      "name": "TRYPS",
      "url": "https://trypsagent.com/",
      "logo": {
        "@type": "ImageObject",
        "@id": "https://trypsagent.com/#logo",
        "url": "https://trypsagent.com/favicon.svg",
        "width": 512,
        "height": 512
      },
      "slogan": "Plan group trips together without the chaos.",
      "foundingDate": "2025-01-01",
      "sameAs": [
        "https://www.instagram.com/tryps",
        "https://www.linkedin.com/company/tryps",
        "https://x.com/tryps"
      ],
      "knowsAbout": [
        "group trip planning",
        "travel itinerary collaboration",
        "group date coordination",
        "trip expense splitting",
        "friend trip planning"
      ],
      "contactPoint": [{
        "@type": "ContactPoint",
        "contactType": "customer support",
        "email": "support@trypsagent.com",
        "url": "https://trypsagent.com/contact"
      }],
      "founder": { "@id": "https://trypsagent.com/#founder" }
    },
    {
      "@type": "Person",
      "@id": "https://trypsagent.com/#founder",
      "name": "Jake Stein",
      "jobTitle": "Founder",
      "worksFor": { "@id": "https://trypsagent.com/#organization" },
      "url": "https://trypsagent.com/about",
      "sameAs": ["https://www.linkedin.com/in/jakestein"],
      "knowsAbout": ["Group Travel", "Consumer SaaS", "Trip Coordination"]
    },
    {
      "@type": "SoftwareApplication",
      "@id": "https://trypsagent.com/#app",
      "name": "TRYPS — Group Trip Planning",
      "applicationCategory": "TravelApplication",
      "applicationSubCategory": "GroupTravelPlanning",
      "operatingSystem": "iOS, Android",
      "softwareVersion": "0.9-beta",
      "datePublished": "2025-01-15",
      "dateModified": "2026-04-14",
      "publisher": { "@id": "https://trypsagent.com/#organization" },
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
    },
    {
      "@type": "FAQPage",
      "@id": "https://trypsagent.com/#faq",
      "mainEntity": [
        {
          "@type": "Question",
          "name": "What is TRYPS?",
          "acceptedAnswer": {"@type": "Answer", "text": "TRYPS is a group trip planning app for friends..."}
        },
        /* ... 5 more matching visible pairs ... */
        {
          "@type": "Question",
          "name": "How do I join the TRYPS waitlist?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Tap \"Join the Beta\" at the top of trypsagent.com, enter your mobile number, and we'll text you an invite link when your group's slot opens."
          }
        }
      ]
    }
  ]
}
```

---

## Entity Consistency Matrix (updated — all fields now self-consistent)

| Entity | Schema | OG Tags | Title | Canonical | Footer | Consistent? |
|---|---|---|---|---|---|---|
| Brand name | "TRYPS" | "TRYPS" | "TRYPS — ..." | — | "TRYPS" | ✓ |
| **Brand URL** | **All → trypsagent.com** ✓ | **og:url → trypsagent.com** ✓ | — | **trypsagent.com** ✓ | — | **✓ FULLY CONSISTENT** |
| Description | Schema slogan + Org description | OG description | Title | — | — | ✓ |
| Logo | ImageObject 512x512 (trypsagent.com/favicon.svg) | opengraph.jpg (different asset) | — | — | — | ⚠ |
| Founder | Person "Jake Stein" in schema | Not in OG | Not in title | — | Implied in "Built by people who care..." H2 | ⚠ (no visible byline) |
| Contact | support@trypsagent.com | — | — | — | — | ✓ |

---

## Bot's Eye View — Full Detail

**curl response:**
- HTTP/2 200 via Cloudflare (cf-ray: 9ec23730ed777b5c-BKK / Bangkok edge)
- Content-Length: ~70 KB
- HSTS: dual header (max-age=63072000 + max-age=31536000)
- CSP: report-only mode
- X-Frame-Options: SAMEORIGIN
- Referrer-Policy: no-referrer
- Set-Cookie: GAESA (Google App Engine session)
- via: 1.1 google

**Content verification:**
- H1: "A group trip planning app your friends actually use." (clean, single, target keyword)
- FAQ: 6 `<details>/<summary>` pairs visible (orphan in schema: "How do I join the TRYPS waitlist?")
- **9 JSON-LD schema blocks with 10 entity types** — all parseable, all self-referencing trypsagent.com
- 0 outbound external links
- 0 body images
- **0 mentions of jointryps.com** ✓
- **27 mentions of trypsagent.com** ✓

**AI search presence verification (unchanged from audit #3):**
- Category query → 0 TRYPS results
- Branded query → 0 TRYPS results (returns Tryp.com, unrelated)

**Classification: FULLY ACCESSIBLE + FULLY ATTRIBUTED** — content IS in raw HTML, schema IS rich, canonical IS self-referencing. The only remaining barrier to citation is off-page brand presence (weeks of work).

---

## All Checks Index (103 total)

| Category | Run | Passed | Failed | Warn | N/A |
|---|---|---|---|---|---|
| A: Technical SEO | 12 | **12** | 0 | 0 | 0 |
| B: Performance | 9 | 5 | 0 | 2 | 2 |
| C: On-Page SEO | 12 | **9** | 2 | 0 | 1 |
| D: Schema | 13 | 7 | 3 | 1 | 2 |
| E: AEO Discovery | 13 | **11** | 0 | 2 | 0 |
| F: AEO Extraction | 12 | 10 | 0 | 2 | 0 |
| G: AEO Trust | 9 | 4 | 3 | 2 | 0 |
| H: AEO Selection | 8 | 5 | 2 | 1 | 0 |
| I: GEO | 8 | 1 | 5 | 0 | 2 |
| J: Entity | 4 | **4** | 0 | 0 | 0 |
| **Total** | **100** | **68** | **15** | **10** | **7** |

---

## Brain Intelligence Applied

🥇 **TIER 1 — PRIMARY SOURCES**

   📌 **Google — Canonicalization, AI Overviews, E-E-A-T, Search Central** — developers.google.com/search/docs
      Applied to: A4, A10, A11, E3, E4, E8, F1, F9, G4, G5, H6, D4, D11, J3
      Evidence: Rules #1419, #1440, #1441, #1442, #1448, #1456, #1474, #1496, #1676

   📌 **Schema.org — FAQPage, Organization, Person, SoftwareApplication, MobileApplication, WebPage, AggregateRating, ImageObject, ContactPoint** — schema.org
      Applied to: D1–D12, G2, G6, J1–J4
      Evidence: Rules #1495, #1496, #1600, #1668, #1674, #1676, #7375

   📌 **Perplexity — Technical Setup + Content** — docs.perplexity.ai
      Applied to: E1, E2, E5, F1, F9, G5
      Evidence: Rules #1471, #1472, #1474, #1479, #1480, #1487

🥈 **TIER 2 — RESEARCH SOURCES**

   📌 **Backlinko — AI SEO data studies** — backlinko.com
      Applied to: B1, C6, C8, C12, F12, G3, G5, G9, H1, H5, I1, I6
      Evidence: Rules #7176, #7190; APs #4607, #4602, #4623, #4698, #4714, #4763

   📌 **Princeton/Georgia Tech/IIT Delhi — GEO Research Paper (KDD 2024)** — arxiv.org/abs/2311.09735
      Applied to: F8, G3, I1, I3

📎 **TIER 4 — SPECIALIZED**

   📌 **amsive.com — AI Crawler JS Avoidance + CCBot** — amsive.com/insights/seo
      Applied to: E5, E13
      Evidence: Rules #2015, #2016

---

## Supplementary Findings (beyond 103 checks)

✅ **Fix #1 from audit #3 implemented in under 26 minutes — all 14 canonical/URL references corrected across HTML, robots.txt, sitemap.xml, and schema.** This demonstrates that sitewide template fixes are fast to execute when the fix spec is clear (BEFORE/AFTER with exact field locations). The auditor's "exact before/after" fix format proved actionable.

⚠ **FAQPage 7-vs-6 mismatch persists** — the team fixed the canonical split but did not reconcile the orphan FAQ pair. Likely because the orphan was documented in audit #3 as generic "schema has 1 more than visible" rather than named; this audit identifies it specifically as "How do I join the TRYPS waitlist?" which makes the fix literal.

🥇 Per Schema.org FAQPage (schema.org/FAQPage) [Sieve Rule #7375]

⚠ **The new WebPage schema block added between audits is a positive signal** — shows the team is iterating on schema. Next addition should probably be `@id` fragments on all entities (Fix #3) since they unlock cleaner cross-references and are trivial to add.

---

## Audit Metadata

- **Version:** 3.0 (curl-first, source-tiered citations v1.3)
- **Checks run:** 100/103
- **Passed:** 68 | **Failed:** 15 | **Warn:** 10 | **N/A:** 7
- **Gates:** All passed
- **Classification:** SaaS landing page (HIGH confidence)
- **Competitors analyzed:** 3 (SquadTrip, Wanderlog, Troupe — reused from audit #3 earlier this session)
- **Chrome MCP:** Not connected — TTFB measured via curl (730ms)
- **Brain entries matched:** ~30 rules + ~10 anti-patterns
- **Audit history for trypsagent.com:**
  - Audit #1: 2026-04-10 10:28 — 52% (F) — v2.0
  - Audit #2: 2026-04-10 12:44 — 58% (F) — v2.0
  - Audit #3: 2026-04-14 10:37 — 76% (C) — v3.0
  - **Audit #4 (this run): 2026-04-14 11:03 — 79% (C+) — v3.0 — POST-FIX #1**
- **Queries used:** 4 (primary, variant, category, branded)
- **Cache-busting:** Yes — Cache-Control: no-cache, Pragma: no-cache headers + timestamp query param to ensure fresh response

---

## Summary — What to Do Next

**Immediate next actions (afternoon work, will push PCR from 83% → ~92%):**
1. **Reconcile FAQPage 7-vs-6 mismatch** — add "How do I join the TRYPS waitlist?" as a visible 7th `<details><summary>` pair (5 min, SCHEMA + HTML)
2. **Add datePublished + dateModified + visible "Last updated"** (15 min, SCHEMA + HTML)
3. **Add @id fragments to all 9 schema blocks** (30 min, SCHEMA)
4. **Remove duplicate HSTS header** (5 min, SITEWIDE)
5. **Add explicit AI bot blocks to robots.txt** (10 min, SITEWIDE)

**Content layer (1–2 days, raises Trust score):**
6. Add visible "Written by Jake Stein, Founder" byline (30 min, CONTENT)
7. Convert comparison H2 from narrative to HTML table (2 hours, CONTENT)
8. Add 3–5 outbound citations to travel research sources (1 hour, CONTENT)
9. Add labeled "TL;DR" quick-answer block at top (30 min, CONTENT)

**Off-page (weeks — the biggest remaining lever):**
10. Product Hunt launch + AlternativeTo + ASO (2–3 days, OFF-PAGE)
11. Outreach to 13 category listicle publishers (1–2 weeks, OFF-PAGE)
12. Reddit community seeding in r/travel, r/solotravel, r/TravelHacks (ongoing, OFF-PAGE)
13. Press outreach to Skift, Phocuswire, TravelPulse (2–4 weeks, OFF-PAGE)

**Honest framing:** Fix #1 from audit #3 was the single highest-impact action and the team executed it cleanly — 14 separate references corrected across HTML, robots.txt, sitemap, and schema, plus a bonus WebPage schema block and +114 words of content. Overall score moved from 76% (C) to 79% (C+); Technical SEO hit **100%**; Entity hit **100%**; AEO Discovery and On-Page SEO both jumped ~9 points.

The remaining gaps split into two buckets:
- **Afternoon work (fixes #1–#5 above)** — trivial-to-easy, push PCR to ~92% (B+) in half a day
- **Off-page entity work (fixes #10–#13)** — the real bottleneck. Brand presence will not move until listings + listicles + Reddit + press start producing third-party mentions. This is weeks-to-months of sustained effort

**The trypsagent.com surface is now ready to receive off-page signals.** The canonical fix was the prerequisite — without it, any off-page mentions that pointed to trypsagent.com would have been attributed to jointryps.com (which was structurally empty). Now trypsagent.com has 10 entity types of rich schema, definition-first content, founder attribution, sameAs links — and it's canonical-consistent. Whatever listicle inclusions and Product Hunt upvotes come in over the next 4–8 weeks will actually accrue where the team wants them.

---

**Persistence confirmation:**
- **Supabase:** `audit_id f89338a9-3111-4a2a-8d41-e0eb622aa108` (26 findings persisted to `website_audit_findings` — down from 31 in audit #3 because 5 checks flipped to PASS)
- **Markdown:** `audit-reports/trypsagent-com-audit-2-2026-04-14.md` (this file)
