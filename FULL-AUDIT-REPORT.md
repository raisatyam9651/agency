# rankfyno.com — Full SEO Audit Report

**Date:** 2026-06-22
**Site:** rankfyno.com (Gurugram, India)
**Type:** Brick-and-mortar digital marketing agency
**Scope:** 768 PHP files (~6 core + 40 blog + ~720 programmatic India location pages)

---

## Executive Summary

### Overall SEO Health Score: **57 / 100**

| Category | Weight | Score | Notes |
|---|---|---|---|
| Technical SEO | 22% | 62 | Strong structure, but root pages missing canonical/OG, no 404, no security headers |
| Content Quality (E-E-A-T) | 23% | 48 | Strong structure, weak uniqueness across 720 city pages, generic author |
| On-Page SEO | 20% | 70 | Blog & city pages well-optimized; root pages lack meta |
| Schema / Structured Data | 10% | 65 | Blog has Article+FAQPage; homepage has zero; city pages use generic Organization (no LocalBusiness) |
| Performance (CWV) | 10% | 55 | Render-blocking CSS (57 KB), no lazy-loading, no preload, no WebP |
| AI Search Readiness (GEO) | 10% | 58 | No llms.txt, no homepage schema, broken social links, generic author |
| Images | 5% | 30 | No WebP, no srcset, og-default.jpg missing (referenced in 41 files!) |

### Top 5 Critical Issues
1. **`og-default.jpg` does not exist** but is referenced in 41 blog posts → broken social shares (image SEO: Critical)
2. **All 40 blog posts are missing from the sitemap** → search engines may not discover or re-crawl them
3. **Root pages have NO canonical, OG, or structured data** (homepage, team, contact, seo-agency-in-india)
4. **720 city pages with near-identical templates** → high duplicate-content risk; can trigger helpful-content suppression
5. **No `llms.txt`** → AI search engines (ChatGPT, Perplexity, Google AIO) lack a curated page index

### Top 5 Quick Wins (≤1 hour each)
1. Create `/og-default.jpg` (1200×630) at project root
2. Add canonical + OG meta to `header-include.php` (fixes 4 root pages at once)
3. Create `/llms.txt` listing top 20 pages
4. Create `/404.php` and add `ErrorDocument 404 /404.php` to `.htaccess`
5. Add `LocalBusiness` (or `ProfessionalService`) subtype to the homepage Organization schema

---

## Technical SEO (62/100)

### Critical
- **Sitemap omits all 40 blog posts.** `sitemap.xml` lists only 4 URLs. `_sitemap/generate_sitemaps.py` CATEGORIES has no `blog` entry. Add a `blog` walker.
- **Root pages missing canonical + OG + robots.** `index.php`, `contact.php`, `team.php`, `seo-agency-in-india/index.php` rely on `header-include.php` which emits zero SEO meta.
- **No 404 page.** Create `/404.php`; add `ErrorDocument 404 /404.php` to `.htaccess`.

### High
- **Hardcoded `lastmod = TODAY`** in `generate_sitemaps.py:194`. Use `os.path.getmtime`.
- **No security headers.** Add HSTS, X-Content-Type-Options, Referrer-Policy, X-Frame-Options to `.htaccess`.
- **57 KB render-blocking CSS** (`style.css`). Inline critical CSS; async-load the rest.
- **Render-blocking Google Fonts** in `header-include.php:3-5`. Use `media="print" onload` pattern.

### Medium
- Dead `seo-services/` directory (0 `index.php` files). Populate or remove.
- Static `changefreq`/`priority` for all 720 city pages — should vary.
- WebGL canvas on `contact.php:6` — heavy on low-power devices, hurts INP.

### Low
- Inline `<style>` block in `team.php:7` — consider moving to `style.css`.
- No `indexnow` key file for Bing/Yandex/Naver.

---

## Content Quality / E-E-A-T (48/100)

| Factor | Score | Finding |
|---|---|---|
| Experience | 35/100 | Testimonials use initials only. Hero "$180M revenue" / "48 awards" unbacked. |
| Expertise | 40/100 | 21 team members listed, but no bios, no LinkedIn, no credentials. Blog author = "the rankfyno team". |
| Authoritativeness | 25/100 | No awards page, no press, no external citations, no client logos. |
| Trustworthiness | 55/100 | NAP in footer/contact, but no privacy/terms, no GST/CIN. |

### Critical
- **720 city pages with near-identical templates.** Word counts 2,531–4,383 but body copy is templated. Risk: helpful-content suppression. Differentiate per city with real local data (population, industries, landmarks).
- **"Other districts" carousel has duplicate cards** — 4 cards all linking to same URL on some pages.

### High
- Replace generic "the rankfyno team" with named authors + `Person` schema + author bio pages.
- Add `about.php` (currently missing) with company history, GST/CIN, mission.
- Publish real case studies with named clients, before/after metrics, screenshots.

### Medium
- Add phone + address to footer (already there — verified ✓).
- Publish 1+ original research piece (e.g., "2026 India SEO Benchmark Study").
- Build industry vertical pages (healthcare SEO, SaaS SEO, real estate SEO) with depth.

### Low
- Replace initials-only testimonials with photos + full names.
- Add "As featured in" badges backed by verifiable links.

---

## On-Page SEO (70/100)

### Strengths
- Blog posts: title, description, canonical, OG, Twitter Card, robots, Article+FAQPage schema — all complete.
- City pages: same level of meta coverage; canonicals correct; geo meta tags present.
- Heading structure: clear H1/H2 hierarchy on blog posts.
- Internal linking: blog posts have 5-8 internal blog links each; city pages link to state hubs.

### Critical
- **Root pages (homepage, contact, team, seo-agency-in-india) have NO meta at all.** No canonical, no OG, no robots meta, no schema.

### High
- **Broken internal anchor references** in city-page footers: `index.html#section` should be `index.php#section` or `/#section`.

### Medium
- Internal blog links previously had no styling (now fixed — blue underline).
- Hero badge "GUR · 24/7" implies Gurugram but never spells it out on homepage.

---

## Schema / Structured Data (65/100)

### Critical
- **Homepage (`index.php`) has ZERO schema.** No `Organization`, no `WebSite`, no `WebPage`. Brand has no machine-readable identity on its most important page.
- **City pages use generic `Organization` schema** — no `LocalBusiness` or `ProfessionalService` subtype, missing local SERP opportunity.

### High
- **Footer social links are `href="#"`** (dead). Search engines + AI interpret as "no social presence exists."
- 3 blog files contain `noindex` (`how-many-pages-should-my-website-have.php`, `why-did-my-rankings-drop.php`, `why-is-my-website-not-ranking.php`) but they're not in the sitemap anyway, so the impact is latent.

### Medium
- No `ItemList` schema on `blog/index.php` (could get carousel).
- No `Person` schema on `team.php` or bylines.
- No `ImageObject` schema on logo or team photos.

### Low
- No `Service` schema on homepage service cards.
- No `aggregateRating` / `Review` schema (if any third-party ratings exist).

---

## Performance / Core Web Vitals (55/100)

### Critical
- **`og-default.jpg` referenced in 41 files but missing** — broken images.
- **No WebP / AVIF** anywhere. 50 state hero JPGs at ~100 KB each = 5 MB across the site. Convert to WebP for ~30 KB each.

### High
- **No `loading="lazy"` on `<img>` tags** — only the footer Maps iframe uses it.
- **No `fetchpriority="high"` on LCP image** (logo).
- **No `srcset` / `sizes`** for responsive images. Team photos served full size to mobile.
- **Rankfyno.png is 1.42 MB** (used as logo + favicon). Convert to SVG + WebP favicon.

### Medium
- **Inline SVGs in header.php** bloat HTML — consider an SVG sprite.
- **Google Fonts render-blocking** — switch to async pattern.

### Low
- WebGL canvas on `contact.php` — consider conditional loading.

---

## AI Search Readiness (GEO) (58/100)

| Dimension | Score | Notes |
|---|---|---|
| Citability | 65 | FAQ blocks + stats present, but author is generic |
| Structural readability | 72 | Clear H2s, Q-based headings, extractable FAQ |
| Multi-modal content | 40 | Logo only, no video/YouTube, alt-text weak |
| Authority & brand signals | 35 | No Organization schema on homepage, social `href="#"` |
| Technical accessibility | 85 | robots.txt allows all crawlers; no blocks |

### Critical
- **No `/llms.txt`** — single highest-leverage GEO gap. AI crawlers have to crawl the sitemap and guess.

### High
- **No `Organization` + `WebSite` + `WebPage` JSON-LD on homepage.**
- **Footer social links `href="#"`** — feeds `sameAs` schema missing.
- **Generic "rankfyno team" author** — replace with `Person` schema + author bios.

### Medium
- No "What is X" definition-style cornerstone posts (highest-citation format for AIO).
- No original research / proprietary data (drives citations).

### Platform Outlook
- Google AIO: 60/100
- ChatGPT: 45/100 (weak brand entity)
- Perplexity: 55/100
- Bing Copilot: 50/100

---

## Images (30/100)

### Critical
1. **Create `/og-default.jpg` (1200×630)** — referenced in 41 blog files but missing.
2. **Add `og:image` to root pages** — homepage, contact, team currently have none.
3. **Convert all hero/team JPGs to WebP** — ~70% size cut, 53 files affected.
4. **Optimize `Rankfyno.png`** — 1.42 MB → <5 KB as SVG + WebP favicon.

### High
5. **Add `loading="lazy"` to all team/state-page `<img>` tags.**
6. **Add `<link rel="preload" as="image">` for homepage LCP (logo).**
7. **Add `srcset`/`sizes` to team photos** for mobile.

### Medium
8. **Enrich team alt text** with role + company.
9. **Build per-state hero.jpg variations** (29 pages share identical asset).
10. **Convert Ansh-Singh.png → JPG/WebP** (645 KB → ~40 KB).

### Low
11. Add `ImageObject` schema to logo + team members.

---

## Local SEO (38/100)

| Dimension | Score |
|---|---|
| GBP signals | 12/25 |
| Reviews & reputation | 4/20 |
| Local on-page SEO | 14/20 |
| NAP consistency & citations | 11/15 |
| Local schema markup | 7/10 |
| Local link & authority signals | 2/10 |

### NAP Consistency: **PASS**
Name (rankfyno), Address (Ground Floor, Cabin no 12, Plot 84, SupremeWork, Sector 32, Gurugram, Haryana 122001), Phone (+91 7317564794) consistent across `contact.php` and `footer.php`. **But missing from `index.php` and `team.php`.**

### Critical
1. Add `LocalBusiness` or `ProfessionalService` schema (currently using generic Organization).
2. Add a noindex quality gate or canonical-cluster rule for sub-tier city pages (720 indexable pages with near-identical word counts).
3. Surface NAP on the homepage (footer-only NAP fails proximity/authority tests).

### High
4. Differentiate small-town pages with real local data (population, nearest city, local language).
5. Fix geo coordinate precision to 5 decimal places.
6. Embed Google Maps iframe on contact.php.
7. Add `aggregateRating` schema if third-party review data exists.

### Medium
8. Fix `index.html#section` anchor references → `index.php#section`.
9. Move the "locations grid" out of collapsed toggle on city pages (Googlebot may not expand JS-only widgets).
10. Add Tier-1 citation signals (Justdial, IndiaMART, Clutch).

---

## Sitemap Architecture

| Asset | Count |
|---|---|
| Total PHP files | 768 |
| Index.php files (sitemap-eligible) | 723 |
| Root `sitemap.xml` URLs | 4 |
| `seo-sitemap.xml` URLs | 720 |
| **Blog .php files** | **41** |
| **Blog URLs in any sitemap** | **0** |
| **Blog pagination URLs in any sitemap** | **0** |

### Critical
1. **Add `blog` to CATEGORIES** in `generate_sitemaps.py`. 40 posts + 1 index = 41 URLs missing.
2. **Add `seo-services` to CATEGORIES** — folder exists but no walker entry. 3 URLs missing.

### High
3. **Use real `lastmod` per file** via `os.path.getmtime`.
4. **Add `noindex` skip** to the walker.

### Medium
5. Drop `priority` and `changefreq` (Google ignores both).
6. Handle blog pagination — either noindex paginated pages or include them with their own canonicals.

---

## Implementation Roadmap

### Week 1 (Critical — blocking)
1. Create `/og-default.jpg` (1 hr)
2. Add canonical + OG to `header-include.php` (1 hr)
3. Add `blog` to sitemap CATEGORIES + regenerate (2 hrs)
4. Create `/llms.txt` (1 hr)
5. Create `/404.php` + add ErrorDocument to `.htaccess` (1 hr)
6. Add `Organization` + `WebSite` + `LocalBusiness` schema to homepage (1 hr)

### Weeks 2-3 (High — significant impact)
7. Fix hardcoded `lastmod` to use `os.path.getmtime` (2 hrs)
8. Convert hero/team JPGs to WebP (3 hrs)
9. Add security headers to `.htaccess` (1 hr)
10. Add `loading="lazy"` + `fetchpriority` to images (2 hrs)
11. Inline critical CSS, async-load rest (4 hrs)
12. Replace generic author with `Person` schema + author bios (3 hrs)
13. Fix `index.html#section` → `index.php#section` in city-page footers (1 hr)

### Month 1 (Medium — optimization)
14. Optimize `Rankfyno.png` to SVG + WebP (1 hr)
15. Fix render-blocking Google Fonts (30 min)
16. Add `Person` schema to `team.php` (2 hrs)
17. Differentiate 50 highest-traffic city pages with real local data (8 hrs)
18. Publish 1 original research piece (16 hrs)
19. Add `aggregateRating` if third-party data exists (1 hr)
20. Build 1 industry vertical page (SaaS SEO) (8 hrs)

### Quarter (Low — backlog)
21. Fix `seo-services/` dead folder
22. Add `ImageObject` schema throughout
23. Build per-state hero.jpg variations
24. Submit to Bing IndexNow
