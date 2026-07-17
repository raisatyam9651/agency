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

# The progress output below uses "✓", which a cp1252 Windows console cannot encode —
# without this the run dies on its first print, after sitemap.xml is already written
# but before the rest, leaving the set half-regenerated.
try:
    sys.stdout.reconfigure(encoding="utf-8")
except (AttributeError, OSError):
    pass

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
    },
    {
        "slug": "seo-services",
        "folder": "seo-services",
        "walker_type": "directory",
    },
    {
        "slug": "youtube",
        "folder": "youtube-marketing",
        "walker_type": "directory",
    },
    {
        "slug": "blog",
        "folder": "blog",
        "walker_type": "flat_files",
        # index.php is the paginated blog hub at /blog/ — a real indexable page,
        # so it belongs here. read_canonical() rejects its concatenated canonical
        # and the path-derived /blog/ is used instead.
        "skip_files": [],
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
    """
    Pull a literal canonical out of the page source, or None to fall back to the
    path-derived URL.

    This greps unrendered PHP, so a match is only usable if it is already a plain
    URL. Two cases must return None rather than a bogus loc:
      - blog/index.php builds its canonical by concatenation:
        href="' . $canonical . '"  -> would capture   ' . $canonical . '
      - pages that set $canonical_url instead of emitting the tag have no match.
    Pages that hold the tag inside $custom_head write it escaped (rel=\"canonical\"),
    which CANONICAL_RE does not match either — all of these fall back correctly.
    """
    try:
        with file.open("r", encoding="utf-8", errors="ignore") as fh:
            head = fh.read(16_000)
    except OSError:
        return None
    m = CANONICAL_RE.search(head)
    if not m:
        return None
    val = m.group(1).strip()
    if not val.startswith(BASE):
        return None
    if any(ch in val for ch in ("$", "'", '"', " ", "<", ">")):
        return None
    return val


def is_noindex(file: Path) -> bool:
    try:
        with file.open("r", encoding="utf-8", errors="ignore") as fh:
            head = fh.read(16_000)
    except OSError:
        return False
    return bool(NOINDEX_RE.search(head))


def _build_git_lastmod_map() -> dict:
    """
    slug -> date of the last commit that touched it, for every tracked file.

    Walking `git log` newest-first means the first commit mentioning a path is
    that path's last change; one subprocess beats ~800 individual `git log` calls.
    Preferred over mtime: a fresh clone or checkout stamps every file with the
    checkout time, which would tell Google the whole site changed at once.
    """
    import subprocess
    try:
        raw = subprocess.run(
            ["git", "log", "--pretty=format:C|%cd", "--date=short", "--name-only"],
            cwd=ROOT, capture_output=True, timeout=120,
        ).stdout.decode("utf-8", "ignore")
    except Exception:
        return {}
    out, cur = {}, None
    for line in raw.split("\n"):
        line = line.strip()
        if not line:
            continue
        if line.startswith("C|"):
            cur = line[2:]
        elif cur:
            out.setdefault(line, cur)
    return out


_GIT_LASTMOD = None


def file_lastmod_iso(file: Path) -> str:
    """Date of the file's last commit; falls back to mtime, then today."""
    global _GIT_LASTMOD
    if _GIT_LASTMOD is None:
        _GIT_LASTMOD = _build_git_lastmod_map()
    try:
        rel = file.resolve().relative_to(ROOT).as_posix()
    except ValueError:
        rel = None
    if rel and rel in _GIT_LASTMOD:
        return _GIT_LASTMOD[rel]
    try:
        import os
        from datetime import datetime
        return datetime.fromtimestamp(os.path.getmtime(file)).date().isoformat()
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
    entries = list of (loc, lastmod). changefreq/priority dropped — Google
    has stated both signals are ignored.
    """
    lines = [URLSET_HEADER]
    for loc, lastmod in entries:
        lines.append("  <url>\n")
        lines.append(f"    <loc>{escape(loc)}</loc>\n")
        lines.append(f"    <lastmod>{lastmod}</lastmod>\n")
        lines.append("  </url>\n")
    lines.append(URLSET_FOOTER)
    path.write_text("".join(lines), encoding="utf-8")


def write_sitemap_index(path: Path, sitemap_files: list[str], lastmods: dict) -> None:
    """
    Each child is stamped with the newest lastmod it actually contains, not
    TODAY — stamping every child on every run claims the whole site changed
    each time the script is run, and Google learns to distrust the signal.
    """
    body = ['<?xml version="1.0" encoding="UTF-8"?>\n',
            '<sitemapindex xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n']
    for fname in sitemap_files:
        body.append("  <sitemap>\n")
        body.append(f"    <loc>{BASE}/{fname}</loc>\n")
        body.append(f"    <lastmod>{lastmods.get(fname, TODAY)}</lastmod>\n")
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
    for rel, url_path, _prio, _freq in ROOT_PAGES:
        full_path = ROOT / rel
        lastmod = file_lastmod_iso(full_path) if full_path.exists() else TODAY
        loc = BASE + url_path
        root_entries.append((loc, lastmod))
    write_urlset(ROOT / "sitemap.xml", root_entries)
    print(f"  ✓ sitemap.xml          ({len(root_entries)} URLs)")

    # 2. Per-category sitemaps
    sitemap_index_entries: list[str] = ["sitemap.xml"]
    total_urls = len(root_entries)
    # newest lastmod per sitemap file, for the index
    index_lastmods: dict = {
        "sitemap.xml": max((lm for _, lm in root_entries), default=TODAY)
    }

    for cat in CATEGORIES:
        folder = ROOT / cat["folder"]
        if cat["walker_type"] == "flat_files":
            pages = walk_flat_files(folder, cat.get("skip_files", []))
        else:
            pages = walk_directory(folder)

        if not pages:
            print(f"  · skipping {cat['slug']} (no pages under {folder})")
            continue

        entries = [(p["loc"], p["lastmod"]) for p in pages]
        out_name = f"{cat['slug']}-sitemap.xml"
        write_urlset(ROOT / out_name, entries)
        sitemap_index_entries.append(out_name)
        index_lastmods[out_name] = max((lm for _, lm in entries), default=TODAY)
        total_urls += len(entries)
        print(f"  ✓ {out_name:<22} ({len(entries)} URLs)")

    # 3. Sitemap index
    write_sitemap_index(ROOT / "sitemap-index.xml", sitemap_index_entries, index_lastmods)
    print(f"  ✓ sitemap-index.xml    ({len(sitemap_index_entries)} sitemaps registered)")
    print(f"Done. {total_urls} total URLs across {len(sitemap_index_entries)} sitemaps.")
    return 0


if __name__ == "__main__":
    sys.exit(main())