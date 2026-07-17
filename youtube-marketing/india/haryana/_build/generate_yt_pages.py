"""
Generator for the Haryana YouTube-marketing section.

Reads:
  - yt_content.json  (per-district copy: industries, hero_sub, why_lede, pillars, faqs)
  - ../../../../seo/india/haryana/_build/cities.py  (geo: lat/lng per district)
  - yt_styles.css, yt_district_template.php, yt_hub_template.php

Writes:
  - ../<slug>/index.php   for each of the 22 districts
  - ../index.php          the Haryana hub

Unlike the SEO _build generators, this one targets the CURRENT dynamic-PHP site
(includes header.php/footer.php, brand rankfyno) and is the live source of truth
for these pages. Re-running it regenerates the pages from yt_content.json.

Usage:
  python generate_yt_pages.py            # write pages
  python generate_yt_pages.py --check    # validate content only, write nothing
"""
import os, sys, json, html

HERE = os.path.dirname(os.path.abspath(__file__))
HARYANA = os.path.dirname(HERE)                      # .../youtube-marketing/india/haryana
REPO = os.path.abspath(os.path.join(HARYANA, '..', '..', '..'))
sys.path.insert(0, os.path.join(REPO, 'seo', 'india', 'haryana', '_build'))
from cities import CITIES  # noqa

GEO = {c['slug']: c for c in CITIES}
ORDER = [c['slug'] for c in CITIES]                  # canonical district order


def esc_html(s):
    return html.escape(s, quote=False)


def jsonld_str(s):
    # value goes inside a PHP double-quoted string as \"...\"; content is ASCII,
    # no double-quotes/backslashes/dollar signs (enforced upstream). Escape defensively.
    return s.replace('\\', '\\\\').replace('"', '\\"')


def industries_inline(items):
    items = list(items)
    if len(items) > 1:
        return ', '.join(items[:-1]) + ' and ' + items[-1]
    return items[0] if items else ''


def initials(name):
    parts = [p for p in name.split() if p]
    if len(parts) >= 2:
        return (parts[0][0] + parts[1][0]).upper()
    return name[:2].upper()


def pillars_html(pillars):
    keys = ['A', 'B', 'C', 'D', 'E', 'F']
    out = []
    for i, p in enumerate(pillars):
        out.append(
            f'        <div class="ytm-pillar"><div class="pk">/ {keys[i]}</div>'
            f'<div><h4>{esc_html(p["title"])}</h4><p>{esc_html(p["body"])}</p></div></div>'
        )
    return '\n'.join(out)


def faq_item_html(q, a):
    return (
        '        <div class="faq-item">\n'
        '          <button class="faq-q" data-cursor-hover>\n'
        f'            {esc_html(q)}\n'
        '            <span class="icon"></span>\n'
        '          </button>\n'
        '          <div class="faq-a">\n'
        f'            <div class="faq-a-inner">{esc_html(a)}</div>\n'
        '          </div>\n'
        '        </div>'
    )


def faq_jsonld_obj(q, a):
    Q = '\\"'
    return (
        '      {\n'
        f'        {Q}@type{Q}: {Q}Question{Q},\n'
        f'        {Q}name{Q}: {Q}{jsonld_str(q)}{Q},\n'
        f'        {Q}acceptedAnswer{Q}: ' + '{\n'
        f'          {Q}@type{Q}: {Q}Answer{Q},\n'
        f'          {Q}text{Q}: {Q}{jsonld_str(a)}{Q}\n'
        '        }\n'
        '      }'
    )


def build_faqs(rec):
    name = rec['name']
    faqs = list(rec['faqs'])  # 4 district-specific
    # 3 generic, district-personalised
    faqs += [
        (f"How long until my {name} channel starts working?",
         f"Most {name} businesses see steady watch-time and subscriber growth within 60-90 days of a consistent upload cadence. Search-optimised videos keep compounding well beyond that."),
        ("Do you make videos in Hindi and English?",
         f"Yes. We produce and optimise in both Hindi and English so your {name} channel reaches the audience that actually searches and buys in your market."),
        ("Do I have to appear on camera?",
         "No. We work with faceless formats too - screen recordings, product shots, voiceover, and motion graphics - so you can grow a channel without ever being on camera."),
    ]
    faqs = [(f[0], f[1]) if isinstance(f, tuple) else (f['q'], f['a']) for f in faqs]
    vis = '\n'.join(faq_item_html(q, a) for q, a in faqs)
    ld = ',\n'.join(faq_jsonld_obj(q, a) for q, a in faqs)
    return vis, ld


def sibling_cards(slug, content):
    idx = ORDER.index(slug)
    sibs = [ORDER[(idx + k) % len(ORDER)] for k in range(1, 5)]
    out = []
    for s in sibs:
        r = content[s]
        out.append(
            f'        <a href="../{s}/" class="ytm-loc" data-cursor-hover>'
            f'<strong>{esc_html(r["name"])}</strong>'
            f'<span>{esc_html(industries_inline(r["industries"]))}</span>'
            f'<span class="go">YouTube marketing -&gt;</span></a>'
        )
    return '\n'.join(out)


def district_cards_all(content):
    out = []
    for s in ORDER:
        r = content[s]
        out.append(
            f'        <a href="{s}/" class="ytm-loc" data-cursor-hover>'
            f'<strong>{esc_html(r["name"])}</strong>'
            f'<span>{esc_html(industries_inline(r["industries"]))}</span>'
            f'<span class="go">YouTube marketing -&gt;</span></a>'
        )
    return '\n'.join(out)


def load_content():
    d = {}
    for fn in ['yt_content.json']:
        path = os.path.join(HERE, fn)
        for rec in json.load(open(path, encoding='utf-8')):
            d[rec['slug']] = rec
    return d


def replace_all(tpl, mapping):
    for k, v in mapping.items():
        tpl = tpl.replace(k, v)
    return tpl


def main():
    check = '--check' in sys.argv
    content = load_content()
    styles = open(os.path.join(HERE, 'yt_styles.css'), encoding='utf-8').read()
    dtpl = open(os.path.join(HERE, 'yt_district_template.php'), encoding='utf-8').read()
    htpl = open(os.path.join(HERE, 'yt_hub_template.php'), encoding='utf-8').read()

    missing = [s for s in ORDER if s not in content]
    if missing:
        print('MISSING CONTENT for:', missing); return 1
    extra = [s for s in content if s not in GEO]
    if extra:
        print('CONTENT for unknown slug:', extra); return 1

    for slug in ORDER:
        rec = content[slug]
        for f in ['industries', 'hero_sub', 'why_lede', 'pillars', 'faqs']:
            if f not in rec:
                print(f'{slug}: missing field {f}'); return 1
        if len(rec['pillars']) != 4 or len(rec['faqs']) != 4:
            print(f'{slug}: expected 4 pillars/4 faqs, got {len(rec["pillars"])}/{len(rec["faqs"])}'); return 1

    if check:
        print(f'Content OK for all {len(ORDER)} districts.'); return 0

    written = 0
    for slug in ORDER:
        rec = content[slug]
        geo = GEO[slug]
        vis, ld = build_faqs(rec)
        ind = industries_inline(rec['industries'])
        mapping = {
            '@@STYLES@@': styles,
            '@@NAME@@': rec['name'],
            '@@SLUG@@': slug,
            '@@LAT@@': geo['lat'],
            '@@LNG@@': geo['lng'],
            '@@INITIALS@@': initials(rec['name']),
            '@@HERO_SUB@@': esc_html(rec['hero_sub']),
            '@@WHY_LEDE@@': esc_html(rec['why_lede']),
            '@@INDUSTRIES_INLINE@@': esc_html(ind),
            '@@META_DESC@@': f"rankfyno runs YouTube marketing for {rec['name']} businesses - {ind}. Channel growth, video SEO, Shorts, and YouTube Ads that turn watch-time into leads.",
            '@@OG_DESC@@': f"YouTube marketing for {rec['name']} businesses - channel growth, video SEO, Shorts, and YouTube Ads.",
            '@@PILLARS_HTML@@': pillars_html(rec['pillars']),
            '@@FAQ_HTML@@': vis,
            '@@FAQ_JSONLD@@': ld,
            '@@SIBLINGS_HTML@@': sibling_cards(slug, content),
        }
        page = replace_all(dtpl, mapping)
        outdir = os.path.join(HARYANA, slug)
        os.makedirs(outdir, exist_ok=True)
        with open(os.path.join(outdir, 'index.php'), 'w', encoding='utf-8', newline='\n') as fh:
            fh.write(page)
        written += 1

    hub = replace_all(htpl, {'@@STYLES@@': styles, '@@DISTRICT_CARDS@@': district_cards_all(content)})
    with open(os.path.join(HARYANA, 'index.php'), 'w', encoding='utf-8', newline='\n') as fh:
        fh.write(hub)

    print(f'Wrote {written} district pages + 1 hub under {HARYANA}')
    return 0


if __name__ == '__main__':
    sys.exit(main())
