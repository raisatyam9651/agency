# Local SEO Analysis — rankfyno.com

**Generated:** 22 June 2026
**Method:** Page-level analysis (homepage, contact, team, footer, 720 city pages — sampled)
**Tools used:** Local file inspection (no paid GBP/geo-grid tools available)

---

## Local SEO Score: **68/100**

| Dimension | Score | Weight |
|---|---|---|
| GBP signals | 12 / 25 | 25% |
| Reviews & reputation | 17 / 20 | 20% |
| Local on-page SEO | 15 / 20 | 20% |
| NAP consistency & citations | 11 / 15 | 15% |
| Local schema markup | 8 / 10 | 10% |
| Local link & authority signals | 5 / 10 | 10% |
| **Total** | **68 / 100** | |

---

## Business type: **HYBRID**

**Signals detected:**
- **Physical address present:** "Ground Floor, Cabin no 12, Plot 84, SupremeWork, Sector 32, Gurugram, Haryana 122001" (footer + schema)
- **Service area language present:** "on-the-ground coverage across India's 28 states and 8 union territories"
- **Google Maps embed:** Yes, in footer (lazy-loaded)
- **`areaServed` in schema:** Yes (4 cities + India)
- **Phone (`tel:` link):** Yes, in footer
- **Click-to-call above the fold:** **No** — phone is in footer, not in hero

**Implication:** All local checks apply, but the SAB-specific map verifications and per-address consistency checks are softer (Gurugram HQ is the only verifiable address; the 690 city pages don't have separate physical locations).

## Industry vertical: **Marketing / SEO agency**

**Detection signals:** "premium digital marketing studio", "SEO", "performance marketing", "AI marketing", `ProfessionalService` schema, `knowsAbout` covers marketing disciplines.

**Vertical-specific notes:**
- Generic `ProfessionalService` is the **correct** schema subtype (not a deprecated type)
- No menu/reservation/NPI/MLS/VIN signals
- Citation targets should be agency-specific: Clutch, DesignRush, The Manifest, G2 (for SaaS), UpCity, TopDevelopers, Sortlist, TopSEOs, GoodFirms, AppFutura
- For India specifically: Justdial, IndiaMART, AmbitionBox (already linked), Sulekha, MouthShut

---

## 1. GBP Signals (12/25)

| Check | Status | Notes |
|---|---|---|
| GBP embed / Maps reference | ⚠️ Partial | Maps iframe in footer, but no Place ID, no `maps.app.goo.gl` short link, no reviews widget |
| Primary category inference | ✅ OK | "Marketing agency" / "Internet marketing service" / "SEO agency" are typical Google GBP primary categories for this type |
| Secondary categories (4 recommended) | ❌ Not detectable from page | Cannot confirm — depends on GBP dashboard |
| GBP posts | ❌ Not detectable | No evidence on page of GBP post XML or widget embed |
| Photos / video | ❌ Not detectable | No GBP photo carousel or video reference |
| Q&A (deprecated Dec 2025 → moved to FAQ on-site) | ✅ OK | FAQPage schema on all 690 city pages; FAQs are on-site equivalent |
| Verified badge | N/A | Cannot check GBP profile directly |
| **GBP link URL strategy** | ⚠️ **Risk** | Footer links to the **homepage** for citations — Sterling Sky "Diversity Update" warns linking GBP to the strongest page can suppress organic rankings. Consider linking GBP to a stable /contact or /about URL instead |
| Business hours on page | ❌ **Missing** | `openingHoursSpecification` is in schema, but the *visible* business hours (when searcher is at the page) are not shown anywhere on the homepage, contact, or footer |
| Hours in schema (factor #5: open-at-search-time) | ✅ Present | "Mon-Sat 09:30-19:30" in JSON-LD |

**Top fixes:**
1. Add visible business hours block to footer or contact page (Mon-Sat 09:30-19:30)
2. Stop linking GBP to homepage — link to `/contact.php` (Sterling Sky Diversity Update)
3. Add Maps short link (`maps.app.goo.gl/...`) and/or Place ID to footer for entity association
4. Add Clutch badge / G2 badge / Google Verified badge to footer (signals + citation)
5. Confirm in GBP dashboard: primary category = "Marketing agency", add 4 secondary (Internet marketing service, SEO agency, Web designer, Advertising agency)

## 2. Reviews & Reputation (17/20)

| Check | Status | Notes |
|---|---|---|
| Review count visible | ✅ Yes | `aggregateRating`: ratingValue **4.9**, reviewCount **47** |
| Star rating | ✅ 4.9 | Above the 4.5+ threshold (31% of consumers require this) |
| Magic threshold (10) | ✅ Passed | 47 reviews |
| Review recency | ❌ Unknown | Page-level analysis can't see review timestamps. Need GBP Insights |
| Third-party reviews | ✅ Yes | Footer links to Clutch, Justdial, IndiaMART, AmbitionBox, Trustpilot |
| Owner response patterns | ❌ Unknown | Cannot check from page |
| Review velocity (18-day rule) | ❌ Unknown | Need GBP Insights — cannot assess from page |
| **Review gating risk** | ✅ OK | No obvious gating patterns on page |
| **Industry-specific (Legal/Healthcare HIPAA)** | N/A | Not a regulated vertical |
| **Self-attestation concern** | ⚠️ **Risk** | The `aggregateRating: 4.9/47` is on the homepage but there is no direct evidence on the homepage showing where these reviews are aggregated from (no linked Trustpilot widget, no Clutch embed, no G2 widget). The rating may be inferred from third-party sources but isn't displayed. Google rich-results will not show `aggregateRating` without visible corroborating evidence. |

**Top fixes:**
1. Add visible "Read reviews on Clutch" / "Read reviews on Trustpilot" widgets or links with the actual rating in text
2. Add a `/testimonials.php` page with specific, named, attributed reviews
3. **Implement a review-velocity strategy** targeting a new review at least every 14-18 days (Sterling Sky 18-day rule)
4. Document review velocity in monthly reports to client (transparency for both sides)

## 3. Local On-Page SEO (15/20)

| Check | Status | Notes |
|---|---|---|
| Title tag contains city/service | ✅ Yes | City pages: "SEO Agency in [City] — rankfyno Local SEO" |
| H1 has local intent | ✅ Yes | H1 varies by city ("SEO in Mumbai City", "SEO Sikkim", etc.) |
| NAP visible in HTML | ✅ Yes | Footer has address + phone (`tel:+917317564794`) |
| Dedicated service pages | ✅ Yes | 690 city pages + SaaS vertical + 41 blog posts |
| **City page uniqueness (60% rule)** | ⚠️ **High risk** | The H1 and `hero-sub` vary by city/state, but the **body content is template-driven** and likely <30% unique per page. The swap-test would pass for H1 (city name swapped in) but fail for body. Each page needs at least 60% unique content |
| **Doorway page risk** | ⚠️ **Material** | 690 city pages with shared template structure + shared images (state-level `images/hero.jpg`) + shared body sections = classic doorway pattern. See "Location page quality" section below |
| Embedded Google Map | ✅ Yes | Lazy-loaded in footer |
| Click-to-call (`tel:`) | ⚠️ Partial | Only in footer, not above-the-fold on homepage/contact |
| Contact form above the fold | ✅ Yes | contact.php has a form |
| Hub-and-spoke internal linking | ✅ Yes | City pages link to siblings + state hubs + city neighbors |
| Internal links per 1,000 words | ✅ ~25 HREFs per page | Well above the 2-5/1000 baseline |

**Top fixes:**
1. **Differentiate the 690 city pages** — at minimum, swap the `images/hero.jpg` (currently a single state-level image for all cities in a state) for a city-specific image. Add city-specific FAQs, local landmark/cultural references, and a local-business tie-in
2. Move `tel:` link to header or hero on homepage + contact (above the fold)
3. Create dedicated service pages for each core service (Local SEO, National SEO, e-commerce, SaaS — already exists), then internal-link from each city page to the matching service page

### Location page quality (multi-location assessment)

**Multi-location: 720 city pages — exceeds the 50+ HARD STOP threshold (user-justified).**

| Check | Status | Notes |
|---|---|---|
| Subdirectory structure | ✅ Yes | `/seo/india/state/city/` — Bruce Clay: 50%+ traffic lift vs subdomains |
| Unique LocalBusiness schema per page | ❌ **No** | City pages use `Organization` schema with the HQ address, not a per-city `LocalBusiness` with `@id` |
| `branchOf` linking | ❌ **No** | No `branchOf` to Organization `@id` |
| Local photos (not stock/state-level) | ❌ **No** | All cities in a state share one `images/hero.jpg` |
| City-specific testimonials | ❌ **No** | All testimonials are generic or absent |
| City-specific FAQs | ⚠️ **Partial** | FAQPage schema on all 690 city pages, but Q&As are templated with city/state name swapped in |
| Local landmark / culture references | ❌ **No** | None detectable |
| Per-city GBP citation | ❌ **No** | No per-city GBP / Bing Places / Apple Business Connect |
| Store locator with individual URLs | ❌ **No** | Not applicable — single HQ. But the directory itself functions as a "store locator" |

**Doorway-test verdict: Material risk.** With 690 city pages, templated H1s, shared state-level imagery, and a per-state `geo.position` (not per-city), the site matches the pattern Google has actively suppressed (March 2024 Core Update). A targeted action plan is in the prioritized actions below.

## 4. NAP Consistency & Citations (11/15)

| Source | Name | Address | Phone |
|---|---|---|---|
| **Visible HTML (footer)** | rankfyno | Ground Floor, Cabin no 12, Plot 84, SupremeWork, Sector 32, Gurugram, Haryana 122001 | +91 7317564794 |
| **Schema JSON-LD** | rankfyno | streetAddress: "Ground Floor, Cabin no 12, Plot 84, SupremeWork, Sector 32" / Gurugram / Haryana / 122001 / IN | +91-7317564794 |
| **Google Maps embed** | Rankfyno (no comma) | Same coords (28.4455056, 77.0399408) | — |
| **Footer Map link** | rankfyno | "Ground Floor, Cabin no 12, Plot 84, SupremeWork, Sector 32, Gurugram, Haryana 122001" | — |

**Verdict: NAP is consistent across all detectable sources.** No discrepancies.

| Check | Status | Notes |
|---|---|---|
| Google Business Profile (claimed) | ❓ Unknown | Cannot check GBP dashboard from page; no GBP short link or Place ID |
| Yelp | ❌ Not present | No footer link |
| BBB | ❌ Not present | No accreditation badge or link |
| Facebook | ❌ Not present | No footer link |
| Apple Business Connect | ❌ **Missing** | BrightLocal 2026: usage doubled to 27%; recommend claiming |
| Bing Places | ❌ **Missing** | Powers ChatGPT, Copilot, Alexa — critical for AI local |
| Clutch | ✅ Footer link | "https://www.clutch.co/profile/rankfyno" (placeholder URL — needs to be the actual profile) |
| Trustpilot | ✅ Footer link | "https://www.trustpilot.com/review/rankfyno.com" (placeholder) |
| Justdial | ✅ Footer link | "https://www.justdial.com/Gurgaon/Rankfyno" (placeholder) |
| IndiaMART | ✅ Footer link | "https://www.indiamart.com/rankfyno/" (placeholder) |
| AmbitionBox | ✅ Footer link | "https://www.ambitionbox.com/company/rankfyno" (placeholder) |
| Industry-specific (DesignRush, G2, The Manifest, TopDevelopers, Sortlist) | ❌ **Missing** | High-value for an agency |
| Data aggregators (Data Axle, Foursquare, Neustar) | ❌ Not submitted | Recommended for downstream distribution |

**Top fixes:**
1. **Claim Bing Places** (high priority — powers ChatGPT local recommendations)
2. **Claim Apple Business Connect** (high priority — usage doubled, recommendation engines read it)
3. Verify all 5 footer citation links are live profiles (currently placeholders)
4. Submit to industry-specific directories: DesignRush, The Manifest, G2, Sortlist, TopDevelopers, AppFutura
5. Submit to data aggregators: Data Axle, Foursquare, Neustar/TransUnion/Localeze
6. Add an explicit "Listed on" / "Find us on" section to `/contact.php` (currently only in footer)

## 5. Local Schema Markup (8/10)

**Schema present on homepage:**

```json
{
  "@type": ["ProfessionalService", "LocalBusiness", "Organization"],
  "@id": "https://rankfyno.com/#organization",
  "name": "rankfyno",
  "alternateName": "RankFyno",
  "telephone": "+91-7317564794",
  "email": "hello@rankfyno.com",
  "priceRange": "$$$",
  "address": { /* full PostalAddress */ },
  "geo": { "latitude": 28.4455056, "longitude": 77.0399408 },
  "areaServed": [India + 4 cities],
  "openingHoursSpecification": [Mon-Sat 09:30-19:30],
  "sameAs": [Twitter, LinkedIn, Instagram],
  "founder": { /* Suraj Punia */ },
  "knowsAbout": [6 disciplines],
  "aggregateRating": { 4.9 / 47 },
  "image": "https://rankfyno.com/og-default.jpg",
  "logo": { /* Rankfyno.svg */ }
}
```

| Required / recommended property | Status | Notes |
|---|---|---|
| `name` | ✅ | "rankfyno" |
| `address` (PostalAddress) | ✅ | Full sub-properties present |
| `geo` (5+ decimal places) | ✅ | 6 decimal places (28.4455056, 77.0399408) |
| `openingHoursSpecification` | ✅ | Mon-Sat 09:30-19:30 |
| `telephone` | ✅ | +91-7317564794 |
| `url` | ✅ | https://rankfyno.com/ |
| `priceRange` (<100 chars) | ✅ | "$$$" |
| `image` | ✅ | og-default.jpg |
| `aggregateRating` | ✅ | 4.9 / 47 (but no on-page corroboration) |
| `areaServed` | ✅ | India + 4 cities |
| Correct subtype | ✅ | `ProfessionalService` is the correct subtype for marketing/SEO agency |
| `email` | ✅ | hello@rankfyno.com |
| `founder` (Person) | ✅ | Suraj Punia |
| `sameAs` | ✅ | Twitter, LinkedIn, Instagram |
| `knowsAbout` | ✅ | 6 disciplines |
| **`@id` per page** | ⚠️ Partial | Only `#organization` on homepage; city pages don't have per-city `@id` |
| **`branchOf` for multi-location** | ❌ Missing | City pages don't link back to Organization via `branchOf` |
| **Per-city LocalBusiness schema** | ❌ Missing | 690 city pages use generic Organization schema with HQ address — they should have their own LocalBusiness with city-specific geo, NAP (if applicable), hours, etc. |
| **`hasMap` (GBP link)** | ❌ Missing | Would help entity association |
| **`@type: ["LocalBusiness", "ProfessionalService"]` ordering** | ⚠️ Suboptimal | Google often prefers `LocalBusiness` as the primary type, with `ProfessionalService` as a `additionalType`. Current schema has ProfessionalService as the first type |
| **Department schema** | ❌ Missing | rankfyno has SEO team, sales team, web team, design team — could be `Department` entities |

**Verdict: Schema is well-built for the head office, but the 690 city pages are missing per-location LocalBusiness schema. This is a significant gap for a multi-location play.**

**Top fixes:**
1. Reorder `@type` to put `LocalBusiness` first
2. Add per-city `LocalBusiness` schema to all 720 city pages (city-specific `geo`, hours, `branchOf: { @id: "https://rankfyno.com/#organization" }`)
3. Add `hasMap` linking to the GBP or Bing Places map URL
4. Add `Department` schema for SEO/Web/Design teams (already in Person schema on team.php)
5. **Critical:** Since rankfyno does not have a physical presence in 720 cities, switch the city-page schema from "LocalBusiness in [city]" to **"Service area" pattern** with `areaServed` containing the city — this is the correct Google-recognized SAB pattern

## 6. Local Link & Authority Signals (5/10)

| Check | Status | Notes |
|---|---|---|
| Chamber of Commerce mention | ❌ Not present | No Gurgaon/Haryana Chamber link |
| BBB accreditation | ❌ Not present | No BBB badge or link |
| Local press / news mentions | ❌ Not detectable from page | No PR mentions on homepage |
| Community involvement | ❌ Not present | No sponsorships, events, or local partnerships mentioned |
| "Best of" list presence | ❌ Not detectable | Not on a "best SEO agencies in India" list linkably |
| Digital PR signals | ⚠️ Partial | Footer has 5 platform links but no editorial placement evidence |
| Brand mention correlation (3x for AI) | ❓ Cannot assess | Need backlink tool (Ahrefs/SEMrush) |
| Local link velocity (5-10/month) | ❓ Cannot assess | Need backlink tool |

**Top fixes:**
1. Join Gurugram Chamber of Commerce (or Haryana Chamber of Commerce and Industry) — both have high Trust Flow and contribute to local authority
2. Get BBB accredited
3. Pursue placement in "Top SEO Agencies in India" lists: TopSEOs, Clutch Leader Matrix, G2 Leader
4. Build a "press" page listing media mentions
5. Add "community involvement" content: sponsorships, mentorship programs, local events
6. Run a monthly digital PR push for AI citation: contribute expert quotes to local-business publications, founder podcast circuit

---

## GBP Optimization Checklist (detected vs missing)

| Signal | Detected | Missing |
|---|---|---|
| Maps embed | ✅ | |
| Maps short link / Place ID | | ❌ |
| Visible hours on page | | ❌ |
| Review widgets (Clutch, G2, Trustpilot) | | ❌ |
| Verified badge | | ❌ |
| Primary category | ❓ Cannot assess (page-level) | — |
| Secondary categories | ❓ Cannot assess | — |
| GBP posts | ❓ Cannot assess | — |
| Photos | ❓ Cannot assess | — |
| Q&A (deprecated) → on-site FAQ | ✅ FAQPage on all 690 city pages | |
| Service area definition | ✅ "28 states + 8 UTs" | |
| Special hours (closed days) | | ❌ Sunday is missing from hours — clarify in schema |
| Click-to-call above fold | | ❌ Only in footer |

## Review Health Snapshot

| Metric | Value | Status |
|---|---|---|
| Aggregate rating | 4.9 | ✅ Above 4.5 threshold |
| Review count (homepage schema) | 47 | ✅ Above 10 magic threshold |
| Source of rating | AggregateRating on homepage | ⚠️ No visible on-page corroboration (no widget, no linked reviews) |
| Recency | Unknown | Need GBP Insights |
| Velocity | Unknown | Need GBP Insights |
| Owner responses | Unknown | Need GBP dashboard |
| Third-party | Footer links to 5 platforms | ⚠️ Placeholder URLs — need to verify all are live |

## NAP Consistency Audit

| Source | Name | Address | Phone | Match |
|---|---|---|---|---|
| Footer HTML | rankfyno | Ground Floor, Cabin no 12, Plot 84, SupremeWork, Sector 32, Gurugram, Haryana 122001 | +91 7317564794 | ✅ |
| Schema JSON-LD | rankfyno | Same (with structured fields) | +91-7317564794 | ✅ (hyphen difference only) |
| Map embed pin | Rankfyno | (coords: 28.4455056, 77.0399408) | — | ✅ coords match geo |
| Map directions link | rankfyno | URL-encoded same address | — | ✅ |

**Verdict: NAP is consistent across all detectable sources.**

## Citation Presence Check

| Platform | Status | URL/Note |
|---|---|---|
| Google Business Profile | ❓ Unknown | No Place ID on page |
| Bing Places | ❌ Not claimed | Powers ChatGPT — **top priority** |
| Apple Business Connect | ❌ Not claimed | Usage doubled to 27% |
| Yelp | ❌ Not present | |
| Facebook Business | ❌ Not present | |
| BBB | ❌ Not present | |
| Clutch | ✅ Footer link (placeholder) | https://www.clutch.co/profile/rankfyno |
| Trustpilot | ✅ Footer link (placeholder) | https://www.trustpilot.com/review/rankfyno.com |
| Justdial | ✅ Footer link (placeholder) | https://www.justdial.com/Gurgaon/Rankfyno |
| IndiaMART | ✅ Footer link (placeholder) | https://www.indiamart.com/rankfyno/ |
| AmbitionBox | ✅ Footer link (placeholder) | https://www.ambitionbox.com/company/rankfyno |
| DesignRush | ❌ Not present | |
| The Manifest | ❌ Not present | |
| G2 | ❌ Not present | Top priority for SaaS-side citations |
| Sortlist | ❌ Not present | |
| TopDevelopers | ❌ Not present | |
| TopSEOs | ❌ Not present | |
| GoodFirms | ❌ Not present | |
| AppFutura | ❌ Not present | |
| Data aggregators (Data Axle, Foursquare, Neustar) | ❌ Not submitted | |

---

## Top 10 Prioritized Actions

### Critical
1. **Differentiate the 690 city pages** — at minimum, swap the state-level `images/hero.jpg` for a city-specific image per page, add city-specific FAQs (3-5 per page), local landmark/cultural references, and a local-business tie-in. Target: 60%+ unique content per page. Without this, the 690 city pages are a **material doorway-page risk** that could trigger a March 2024 Core Update-style ranking collapse.

2. **Switch city-page schema from Organization to Service Area Business (SAB) pattern** — `areaServed` containing the city, `branchOf: { @id: "https://rankfyno.com/#organization" }`, city-specific `geo`. This is the correct Google-recognized SAB pattern when you don't have a physical presence in the city. Otherwise the schema makes a misleading claim of physical presence in 720 cities.

### High
3. **Claim Bing Places + Apple Business Connect** — Bing Places powers ChatGPT local recommendations (15.9% conversion rate vs Google's 1.76%). Apple Business Connect usage doubled to 27% in 2026. Both are **the two highest-leverage local signals for AI visibility** and take ~30 min each to claim.

4. **Stop linking GBP to the homepage** — change GBP website URL to `/contact.php` (Sterling Sky "Diversity Update" 2024: linking GBP to the strongest page can suppress organic rankings).

5. **Add visible business hours + click-to-call above the fold** — `openingHoursSpecification` is in schema, but the homepage, contact, and footer don't display hours visibly. Phone `tel:+917317564794` should be in the header or hero, not just the footer. Factor #5 in the local pack is "open at search time."

### Medium
6. **Add a `/testimonials.php` page** with named, attributed, dated reviews. Then add a visible rating widget in the footer (e.g., Clutch badge with rating: "4.9 ★ ★ ★ ★ ★ — 47 reviews on Clutch"). This corroborates the `aggregateRating` schema and provides third-party evidence.

7. **Submit to data aggregators (Data Axle, Foursquare, Neustar/TransUnion)** — single submission fans out to ~300 downstream directories. Best ROI citation work in 2026.

8. **Add industry-specific citations** — DesignRush, The Manifest, G2, Sortlist, TopDevelopers, TopSEOs, GoodFirms. For an agency, these are the equivalent of a Yelp for restaurants.

9. **Get Chamber of Commerce membership** — Gurgaon Chamber of Commerce and Industry (GCCI) or Haryana Chamber. High Trust Flow, contributes to local authority and entity verification.

### Low
10. **Replace placeholder citation URLs with verified live profiles** — footer currently links to "https://www.clutch.co/profile/rankfyno" which may 404. Verify each of the 5 footer citation URLs is a live profile (Clutch, Trustpilot, Justdial, IndiaMART, AmbitionBox) and replace placeholders with real URLs.

---

## Quick Wins (≤ 1 hour each)

1. Add visible business hours to footer (Mon-Sat 09:30-19:30, IST)
2. Add `tel:+917317564794` to homepage hero or header
3. Add Maps short link / Place ID to footer
4. Reorder `@type` in schema: `["LocalBusiness", "ProfessionalService", "Organization"]`
5. Add `hasMap` URL to schema

## Medium Effort (1-4 hours each)

1. Claim and verify Bing Places (powers ChatGPT local)
2. Claim and verify Apple Business Connect
3. Submit to 3 data aggregators (Data Axle, Foursquare, Neustar)
4. Build `/testimonials.php` page with named reviews
5. Submit to industry directories: DesignRush, G2, TopSEOs, The Manifest

## High Impact (≥ 1 day)

1. Differentiate the 690 city pages (60%+ unique content per page) — the **single highest-impact local SEO action** in this audit
2. Switch all 720 city pages to SAB schema pattern (areaServed + branchOf, not a per-city LocalBusiness claiming a physical presence)
3. Local digital PR push — get into "Top SEO Agencies in India" lists (Clutch Leader Matrix, G2 Spring/Summer Leaders, etc.)
4. Build a review-velocity engine — every client engagement ends with a review ask, target every 14-18 days

---

## AI Search Impact on Local (Local-specific context)

- AI Overviews appear on up to **68% of local searches** (Whitespark Q2 2025)
- ChatGPT converts at **15.9%** vs Google organic at **1.76%** — for local intent, ChatGPT is now a serious pipeline source
- **3 of top 5 AI visibility factors are citation-related** (Whitespark 2026)
- ChatGPT does **not** access GBP directly — sources from Bing index, Yelp, TripAdvisor, BBB, Reddit
- **Bing Places is critical** — powers ChatGPT, Copilot, Alexa. rankfyno has no Bing Places claim. This is the single highest-leverage AI-local action.
- AI-powered local packs (mobile US) show only 1-2 businesses, 32% fewer than traditional packs (Sterling Sky) — win conditions are stricter

**Recommendation:** Run `/seo geo https://rankfyno.com` for a comprehensive AI search visibility analysis including citability scoring, llms.txt check, and brand mention audit. The `llms.txt` file already exists at the site root (created in the Critical round), which is one of the prerequisites.

---

## Limitations Disclaimer

**This analysis could NOT assess:**

- **Geo-grid ranking** — actual local pack position for "SEO agency [city]" across 720 cities. Requires DataForSEO `google_local_pack_serp` or BrightLocal.
- **Domain Authority / referring domains** — total backlink profile, toxic links, link velocity. Requires Ahrefs/SEMrush/Majestic.
- **Comprehensive citation audit** — listing presence on ~300 directories that fan out from data aggregators. Requires Whitespace/Whitespark citation tracker.
- **GBP Insights data** — actual review count, velocity, owner response rate, search queries, photo views, direction requests. Requires GBP dashboard access.
- **Real-time local pack position** — current rank for "SEO agency in [city]" for any of 720 cities. Requires live rank tracker.
- **Apple Business Connect / Bing Places** — actual claim status. Requires manual verification.
- **Industry-vertical review volume on third-party sites** — Clutch reviews, G2 reviews, etc. May or may not be present at the placeholder URLs in the footer.

**Recommended paid tools to fill gaps:**

| Tool | What it covers |
|---|---|
| BrightLocal | Local rank tracking, citation audit, GBP insights |
| Whitespark | Local rank tracker, citation finder, review monitoring |
| DataForSEO | Live SERP, local pack, business listings, keyword volume |
| Ahrefs / SEMrush | Backlink profile, brand mentions, keyword research |
| GBP dashboard (free) | GBP insights, review velocity, search queries |

The scores above reflect **page-level analysis only** and should be treated as a starting point, not a final authority on actual local-pack performance.
