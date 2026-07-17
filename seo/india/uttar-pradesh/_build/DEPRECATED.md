# UP `_build/` is retired — do not regenerate the live pages from it

## What was wrong

`generate_up_pages.py` built the 75 Uttar Pradesh district pages from an **archetype**
model: each district in `up_districts.py` was tagged with one of six categories
(`agriculture_trade`, `handicraft_export`, `tourism_historic`, `administrative_edu`,
`industrial`, `it_tech`), and `CATEGORIES_COPIES` held a single block of body copy per
category. Every district sharing a category received **byte-identical** copy with only
the city name swapped in.

Result:

- **48 of 75** districts were tagged `agriculture_trade` → 48 near-identical pages.
- The same fabricated testimonial (e.g. "Yadav Cold Storage · Farrukhabad") appeared on
  all 48, including 47 districts it had nothing to do with.
- City-normalized pages were ~85% identical → Google flagged **duplicate / doorway pages**.

The generator is also **doubly stale**: it emits pre-rebrand static HTML (`<!DOCTYPE html>`,
brand "NEXUS"), but the live site was converted to dynamic PHP (`header.php`/`footer.php`
includes, brand "rankfyno") in commit `1bdd85c`. Running it would revert the rebrand,
the recent H1/pricing changes, **and** re-introduce the duplicate content.

## What changed

The 75 live pages under `seo/india/uttar-pradesh/<district>/index.php` now carry
**genuinely per-district content** (grounded in each district's real economy / UP ODOP
signature product): a unique tagline, why-section lede, four "why" pillars, and four
district-specific FAQs (kept in sync between the visible HTML and the FAQPage JSON-LD).
The fabricated "Client voices" testimonial section was removed from every page. The
"Other UP districts" sibling cards now show each neighbour's real tagline.

The per-district source content is saved alongside this file as **`up_content.json`**
(one object per district). The live PHP pages are the **single source of truth** — edit
them directly, or edit `up_content.json` and re-apply with the rewriter that produced them.

## If you must regenerate

Don't use `generate_up_pages.py` as-is. It is guarded to refuse execution. Any future
generator must (1) emit dynamic PHP matching the current `header.php` template, (2) use
`up_content.json` (real per-district copy), not `CATEGORIES_COPIES` archetypes, and
(3) not fabricate testimonials.
