# rankfyno.com — Prioritized Action Plan

## CRITICAL (fix within 1 week)

| # | Issue | Surface | File | Effort |
|---|---|---|---|---|
| 1 | `og-default.jpg` referenced in 41 blog files but **does not exist** | All blog posts | create `og-default.jpg` (1200×630) at project root | 1 hr |
| 2 | All 40 blog posts **missing from sitemap** | `sitemap.xml`, `_sitemap/generate_sitemaps.py` | Add `"folder": "blog"` to CATEGORIES, regenerate | 2 hrs |
| 3 | Root pages have **NO canonical, OG, robots, or schema** | homepage, team, contact, seo-agency-in-india | Add meta block to `header-include.php` (one fix covers all) | 1 hr |
| 4 | **720 city pages with near-identical templates** — duplicate-content risk | All `seo/india/*/*/index.php` | Add per-city unique content (population, local industry, landmarks) — start with top 50 | 8 hrs |
| 5 | **No `/llms.txt`** — AI crawlers lack a curated page index | Root | Create `/llms.txt` listing top 20 pages with one-line descriptions | 1 hr |
| 6 | **No `404.php`** — bad UX and SEO | Root | Create `/404.php`, add `ErrorDocument 404 /404.php` to `.htaccess` | 1 hr |
| 7 | **No `Organization` + `WebSite` + `LocalBusiness` schema on homepage** | Homepage | Add to `header-include.php` | 1 hr |

## HIGH (fix within 2-3 weeks)

| # | Issue | File | Effort |
|---|---|---|---|
| 8 | Hardcoded `lastmod = TODAY` for all 724 URLs | `_sitemap/generate_sitemaps.py:194` | 2 hrs |
| 9 | 57 KB render-blocking CSS | `style.css`, `header-include.php:7` | 4 hrs |
| 10 | Render-blocking Google Fonts | `header-include.php:3-5` | 30 min |
| 11 | No WebP/AVIF anywhere | All image files | 3 hrs |
| 12 | No `loading="lazy"` on `<img>` tags | All template pages | 2 hrs |
| 13 | No `fetchpriority="high"` on LCP image (logo) | `header.php` | 30 min |
| 14 | No security headers | `.htaccess` | 1 hr |
| 15 | Generic author "the rankfyno team" — no E-E-A-T | All 40 blog posts + `team.php` | 3 hrs |
| 16 | Footer social links `href="#"` (4 dead links) | `footer.php:17-28` | 30 min |
| 17 | "Other districts" carousel has duplicate cards | City-page templates | 2 hrs |
| 18 | `Rankfyno.png` is 1.42 MB | Convert to SVG + WebP favicon | 1 hr |
| 19 | No `noindex` skip in sitemap walker | `_sitemap/generate_sitemaps.py` | 1 hr |
| 20 | `index.html#section` anchor references (PHP site) | City-page footers | 1 hr |

## MEDIUM (fix within 1 month)

| # | Issue | Effort |
|---|---|---|
| 21 | Drop `priority` and `changefreq` from sitemaps (Google ignores) | 30 min |
| 22 | Add `Person` schema to `team.php` | 2 hrs |
| 23 | Add `ItemList` schema to `blog/index.php` | 1 hr |
| 24 | Differentiate 50 highest-traffic city pages with real local data | 8 hrs |
| 25 | Build 1 industry vertical page (SaaS SEO) | 8 hrs |
| 26 | Publish 1 original research piece | 16 hrs |
| 27 | Inline SVGs in header.php → SVG sprite system | 4 hrs |
| 28 | WebGL canvas on `contact.php:6` — load conditionally | 2 hrs |
| 29 | Add `aggregateRating` schema if third-party data exists | 1 hr |
| 30 | Add Tier-1 citation signals (Justdial, IndiaMART, Clutch) | 4 hrs |
| 31 | `seo-services/` dead folder — populate or remove | 2 hrs |

## LOW (backlog)

| # | Issue | Effort |
|---|---|---|
| 32 | Static `changefreq`/`priority` for all 720 city pages — vary by population | 2 hrs |
| 33 | Add `ImageObject` schema to logo + team photos | 2 hrs |
| 34 | Build per-state hero.jpg variations (29 shared asset) | 8 hrs |
| 35 | Enrich team alt text with role + company | 1 hr |
| 36 | Submit to Bing IndexNow | 1 hr |
| 37 | Add `openingHoursSpecification` + `priceRange` to schema | 1 hr |
| 38 | Inline `<style>` block in `team.php:7` → `style.css` | 1 hr |

---

## Total Estimated Effort

- **Critical (1-2 weeks):** 15 hrs → ship ASAP
- **High (2-3 weeks):** 22 hrs
- **Medium (1 month):** 50 hrs
- **Low (backlog):** 16 hrs
- **Total:** ~100 hrs to a fully-optimized site
