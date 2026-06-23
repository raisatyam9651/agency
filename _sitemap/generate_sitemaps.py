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
ROOT_PAGES = [
    ("index.php",                       "/",                     "1.0", "weekly"),
    ("team.php",                        "/team.php",             "0.6", "monthly"),
    ("contact.php",                     "/contact.php",          "0.7", "monthly"),
    ("seo-agency-in-india/index.php",   "/seo-agency-in-india/", "0.9", "weekly"),
]

# Category folders. walker_type = "directory" walks for index.php recursively
# (used by state/city hubs). walker_type = "flat_files" walks for *.php files
# directly inside the folder (used by blog where posts are sibling PHP files).
CATEGORIES = [
    {
        "slug": "seo",
        "folder": "seo",
        "walker_type": "directory",
        "changefreq": "monthly",
        "hub_priority": "0.9",
        "leaf_priority": "0.7",
        "leaf_changefreq": "monthly",
    },
    {
        "slug": "seo-services",
        "folder": "seo-services",
        "walker_type": "directory",
        "changefreq": "monthly",
        "hub_priority": "0.8",
        "leaf_priority": "0.6",
        "leaf_changefreq": "monthly",
    },
    {
        "slug": "blog",
        "folder": "blog",
        "walker_type": "flat_files",
        "skip_files": ["index.php"],
        "changefreq": "monthly",
        "hub_priority": "0.9",
        "leaf_priority": "0.7",
        "leaf_changefreq": "monthly",
    },
]

SKIP_DIR_NAMES = {"_tools", "_build", "assets", "images", "team", "photos",
                  ".git", "node_modules", "vendor", "scratch"}

NOINDEX_RE = re.compile(r'<meta\s+name="robots"\s+content="[^"]*noindex', re.IGNORECASE)
CANONICAL_RE = re.compile(r'<link\s+rel="canonical"\s+href="([^"]+)"', re.IGNORECASE)

TODAY = date.today().isoformat()

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def file_to_url_path(rel_to_root: Path) -> str:
    parts = list(rel_to_root.parts)
    if parts[-1] == "index.php":
        parts = parts[:-1]
    else:
        return "/" + "/".join(parts)
    if not parts:
        return "/"
    return "/" + "/".join(parts) + "/"


def read_canonical(file: Path) -> str | None:
    try:
        with file.open("r", encoding="utf-8", errors="ignore") as fh:
            head = fh.read(16_000)
    except OSError:
        return None
    m = CANONICAL_RE.search(head)
    return m.group(1).strip() if m else None


def is_noindex(file: Path) -> bool:
    try:
        with file.open("r", encoding="utf-8", errors="ignore") as fh:
            head = fh.read(16_000)
    except OSError:
        return False
    return bool(NOINDEX_RE.search(head))


def file_lastmod_iso(file: Path) -> str:
    """Use the file's actual mtime so Google sees real update signals."""
    try:
        import os
        mtime = os.path.getmtime(file)
        from datetime import datetime
        return datetime.fromtimestamp(mtime).date().isoformat()
    except OSError:
        return TODAY


# ---------------------------------------------------------------------------
# Walkers
# ---------------------------------------------------------------------------


def walk_directory(folder: Path) -> list[dict]:
    """Find every index.php recursively. Returns [{loc, depth, path}]."""
    if not folder.exists():
        return []
    candidates: list[Path] = []
    for p in folder.rglob("index.php"):
        rel = p.relative_to(folder)
        if any(part in SKIP_DIR_NAMES for part in rel.parts):
            continue
        candidates.append(p)
    candidates.sort(key=lambda p: (len(p.relative_to(folder).parts), str(p).lower()))

    pages = []
    for p in candidates:
        if is_noindex(p):
            continue
        rel_to_root = p.relative_to(ROOT)
        url_path = file_to_url_path(rel_to_root)
        canonical = read_canonical(p)
        loc = canonical or (BASE + url_path)
        pages.append({
            "loc": loc,
            "depth": len(rel_to_root.parts),
            "path": p,
            "lastmod": file_lastmod_iso(p),
        })
    return pages


def walk_flat_files(folder: Path, skip: list[str]) -> list[dict]:
    """Find every *.php directly inside folder. Returns [{loc, depth, path}]."""
    if not folder.exists():
        return []
    skip_set = set(skip)
    pages = []
    for p in sorted(folder.glob("*.php")):
        if p.name in skip_set:
            continue
        if is_noindex(p):
            continue
        rel_to_root = p.relative_to(ROOT)
        url_path = file_to_url_path(rel_to_root)
        canonical = read_canonical(p)
        loc = canonical or (BASE + url_path)
        pages.append({
            "loc": loc,
            "depth": len(rel_to_root.parts),
            "path": p,
            "lastmod": file_lastmod_iso(p),
        })
    return pages


WALKERS = {
    "directory": walk_directory,
    "flat_files": lambda f: walk_flat_files(f, []),
}


# ---------------------------------------------------------------------------
# XML writers
# ---------------------------------------------------------------------------

URLSET_HEADER = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
URLSET_FOOTER = "</urlset>\n"


def write_urlset(path: Path, entries: list[tuple]) -> None:
    """
    entries = list of (loc, lastmod, changefreq, priority).
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

    # 1. Root sitemap
    root_entries = []
    for rel, url_path, prio, freq in ROOT_PAGES:
        full_path = ROOT / rel
        lastmod = file_lastmod_iso(full_path) if full_path.exists() else TODAY
        loc = BASE + url_path
        root_entries.append((loc, lastmod, freq, prio))
    write_urlset(ROOT / "sitemap.xml", root_entries)
    print(f"  ✓ sitemap.xml          ({len(root_entries)} URLs)")

    # 2. Per-category sitemaps
    sitemap_index_entries: list[str] = ["sitemap.xml"]
    total_urls = len(root_entries)

    for cat in CATEGORIES:
        folder = ROOT / cat["folder"]
        walker_fn = WALKERS.get(cat["walker_type"], walk_directory)
        if cat["walker_type"] == "flat_files":
            pages = walk_flat_files(folder, cat.get("skip_files", []))
        else:
            pages = walk_directory(folder)

        if not pages:
            print(f"  · skipping {cat['slug']} (no pages under {folder})")
            continue

        min_depth = min(p["depth"] for p in pages)
        entries: list[tuple] = []
        for p in pages:
            is_hub = (p["depth"] == min_depth)
            prio = cat["hub_priority"] if is_hub else cat["leaf_priority"]
            freq = cat["changefreq"] if is_hub else cat["leaf_changefreq"]
            entries.append((p["loc"], p["lastmod"], freq, prio))

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