#!/usr/bin/env python3
"""
Sitemap generator for rankfyno.

Outputs:
  - sitemap.xml         : top-level pages (root)
  - <slug>-sitemap.xml  : one per category in CATEGORIES
  - sitemap-index.xml   : registers every sitemap file

Adding a new category (e.g. PPC, web-design, content) is a one-line change
to CATEGORIES below — the script will auto-discover every index.php in the
category subtree and emit a matching sitemap.
"""

import re
import sys
from datetime import date
from pathlib import Path
from xml.sax.saxutils import escape

# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------

BASE = "https://rankfyno.com"
ROOT = Path(__file__).resolve().parent.parent  # agency/

# Top-level pages that live at the root (outside any category folder).
# Path is relative to ROOT. The URL path is the same as the file path with
# index.php collapsed to trailing slash.
ROOT_PAGES = [
    ("index.php",                       "/",                     "1.0", "weekly"),
    ("team.php",                        "/team.php",             "0.6", "monthly"),
    ("contact.php",                     "/contact.php",          "0.7", "monthly"),
    ("seo-agency-in-india/index.php",   "/seo-agency-in-india/", "0.9", "weekly"),
]

# Category folders. Each one becomes its own <slug>-sitemap.xml.
# slug   = output filename stem (no .xml)
# folder = directory under ROOT, walked recursively for index.php
# priority/changefreq = defaults applied to every URL in that sitemap
CATEGORIES = [
    {
        "slug": "seo",
        "folder": "seo",
        "changefreq": "monthly",
        "hub_priority": "0.9",
        "leaf_priority": "0.7",
        "leaf_changefreq": "monthly",
    },
    # Future categories — uncomment / add as you ship:
    # {"slug": "ppc",         "folder": "ppc",         "changefreq": "monthly", "hub_priority": "0.9", "leaf_priority": "0.7", "leaf_changefreq": "monthly"},
    # {"slug": "web-design",  "folder": "web-design",  "changefreq": "monthly", "hub_priority": "0.9", "leaf_priority": "0.7", "leaf_changefreq": "monthly"},
    # {"slug": "content",     "folder": "content",     "changefreq": "monthly", "hub_priority": "0.9", "leaf_priority": "0.7", "leaf_changefreq": "monthly"},
]

# Folders that look like content but should never appear in a sitemap.
SKIP_DIR_NAMES = {"_tools", "_build", "assets", "images", "team", "photos",
                  ".git", "node_modules", "vendor", "scratch"}

TODAY = date.today().isoformat()

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

CANONICAL_RE = re.compile(
    r'<link\s+rel="canonical"\s+href="([^"]+)"', re.IGNORECASE
)


def file_to_url_path(rel_to_root: Path) -> str:
    """Convert a file path like 'seo/india/karnataka/index.php' to '/seo/india/karnataka/'."""
    parts = list(rel_to_root.parts)
    # Collapse trailing index.php to a directory URL
    if parts[-1] == "index.php":
        parts = parts[:-1]
    else:
        # keep .php as-is
        return "/" + "/".join(parts)
    if not parts:
        return "/"
    return "/" + "/".join(parts) + "/"


def read_canonical(index_file: Path) -> str | None:
    """Pull the canonical URL out of the <head> of an index.php (cheap scan)."""
    try:
        with index_file.open("r", encoding="utf-8", errors="ignore") as fh:
            head = fh.read(16_000)  # canonical is always in <head>
    except OSError:
        return None
    m = CANONICAL_RE.search(head)
    return m.group(1).strip() if m else None


def walk_category(folder: Path) -> list[dict]:
    """Return all index.php pages under a category folder, in deterministic order."""
    pages: list[dict] = []
    if not folder.exists():
        return pages

    # Hub page first (category root), then everything else alphabetically
    candidates: list[Path] = []
    for p in folder.rglob("index.php"):
        rel = p.relative_to(folder)
        if any(part in SKIP_DIR_NAMES for part in rel.parts):
            continue
        candidates.append(p)
    candidates.sort(key=lambda p: (len(p.relative_to(folder).parts), str(p).lower()))

    for p in candidates:
        rel_to_root = p.relative_to(ROOT)
        url_path = file_to_url_path(rel_to_root)
        canonical = read_canonical(p)
        loc = canonical or (BASE + url_path)
        # The hub is whichever page has the shortest URL path under this folder
        # (the category's own index.php). State pages get leaf treatment; if a
        # category is one-level deep its root index.php is the hub.
        depth = len(rel_to_root.parts)
        pages.append({"loc": loc, "depth": depth})
    return pages


# ---------------------------------------------------------------------------
# XML writers
# ---------------------------------------------------------------------------

URLSET_HEADER = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
URLSET_FOOTER = "</urlset>\n"


def write_urlset(path: Path, entries: list[tuple[str, str, str, str]]) -> None:
    """
    entries = list of (loc, lastmod, changefreq, priority).
    Writes a sitemap urlset XML file.
    """
    lines = [URLSET_HEADER]
    for loc, lastmod, changefreq, priority in entries:
        lines.append("  <url>\n")
        lines.append(f"    <loc>{escape(loc)}</loc>\n")
        lines.append(f"    <lastmod>{lastmod}</lastmod>\n")
        lines.append(f"    <changefreq>{changefreq}</changefreq>\n")
        lines.append(f"    <priority>{priority}</priority>\n")
        lines.append("  </url>\n")
    lines.append(URLSET_FOOTER)
    path.write_text("".join(lines), encoding="utf-8")


def write_sitemap_index(path: Path, sitemap_files: list[str]) -> None:
    body = ['<?xml version="1.0" encoding="UTF-8"?>\n',
            '<sitemapindex xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n']
    for fname in sitemap_files:
        body.append("  <sitemap>\n")
        body.append(f"    <loc>{BASE}/{fname}</loc>\n")
        body.append(f"    <lastmod>{TODAY}</lastmod>\n")
        body.append("  </sitemap>\n")
    body.append("</sitemapindex>\n")
    path.write_text("".join(body), encoding="utf-8")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> int:
    print(f"Generating sitemaps in {ROOT}  (base: {BASE})")

    # 1. Main sitemap — top-level pages
    root_entries = []
    for rel, url_path, prio, freq in ROOT_PAGES:
        loc = BASE + url_path
        root_entries.append((loc, TODAY, freq, prio))
    write_urlset(ROOT / "sitemap.xml", root_entries)
    print(f"  ✓ sitemap.xml          ({len(root_entries)} URLs)")

    # 2. Per-category sitemaps + collect for index
    sitemap_index_entries: list[str] = ["sitemap.xml"]
    total_urls = len(root_entries)

    for cat in CATEGORIES:
        folder = ROOT / cat["folder"]
        pages = walk_category(folder)
        if not pages:
            print(f"  · skipping {cat['slug']} (no pages under {folder})")
            continue

        min_depth = min(p["depth"] for p in pages)
        entries: list[tuple[str, str, str, str]] = []
        for p in pages:
            is_hub = (p["depth"] == min_depth)
            prio = cat["hub_priority"] if is_hub else cat["leaf_priority"]
            freq = cat["changefreq"] if is_hub else cat["leaf_changefreq"]
            entries.append((p["loc"], TODAY, freq, prio))

        out_name = f"{cat['slug']}-sitemap.xml"
        write_urlset(ROOT / out_name, entries)
        sitemap_index_entries.append(out_name)
        total_urls += len(entries)
        print(f"  ✓ {out_name:<22} ({len(entries)} URLs)")

    # 3. Sitemap index
    write_sitemap_index(ROOT / "sitemap-index.xml", sitemap_index_entries)
    print(f"  ✓ sitemap-index.xml    ({len(sitemap_index_entries)} sitemaps registered)")
    print(f"Done. {total_urls} total URLs across {len(sitemap_index_entries)} sitemaps.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
