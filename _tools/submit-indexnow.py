#!/usr/bin/env python3
"""
Submit recently-modified URLs to Bing IndexNow.

Setup:
  1. Generate a key file at the site root (32-char hex + .txt):
       openssl rand -hex 16 > <KEY>.txt
  2. Upload that file to https://rankfyno.com/<KEY>.txt
  3. Add INDEXNOW_KEY env var to your shell or pass --key

Usage:
  python3 _tools/submit-indexnow.py                       # submit sitemap URLs (default)
  python3 _tools/submit-indexnow.py --url <single-url>    # submit one URL
  python3 _tools/submit-indexnow.py --recent 50           # submit last 50 modified pages

Reference: https://www.indexnow.org/documentation
"""
import argparse
import json
import sys
import urllib.request
import urllib.error
from pathlib import Path

INDEXNOW_ENDPOINT = "https://api.indexnow.org/indexnow"

def submit(urls: list[str], key: str) -> dict:
    body = {
        "host": "rankfyno.com",
        "key": key,
        "keyLocation": f"https://rankfyno.com/{key}.txt",
        "urlList": urls,
    }
    req = urllib.request.Request(
        INDEXNOW_ENDPOINT,
        data=json.dumps(body).encode("utf-8"),
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            return {"status": resp.status, "submitted": len(urls), "ok": True}
    except urllib.error.HTTPError as e:
        return {"status": e.code, "submitted": len(urls), "ok": False, "error": e.read().decode("utf-8")[:200]}

def collect_from_sitemap(sitemap_path: Path) -> list[str]:
    import re
    if not sitemap_path.exists():
        return []
    text = sitemap_path.read_text()
    return re.findall(r"<loc>(.*?)</loc>", text)

def collect_recent(root: Path, n: int) -> list[str]:
    import re
    pages = []
    for p in list(root.rglob("index.php")) + list(root.glob("*.php")) + list(root.glob("blog/*.php")):
        if any(skip in p.parts for skip in ("_tools", "_sitemap", "_build", "node_modules", ".git")):
            continue
        if p.name.startswith("index") and p.parent == root:
            # root index.php — include
            pass
        if p.name in ("header.php", "footer.php", "header-include.php"):
            continue
        try:
            rel = p.relative_to(root)
            url_path = "/" + str(rel).replace("index.php", "").replace("\\", "/").rstrip("/")
            url_path = url_path.replace(".php", "")
            if url_path == "/":
                url_path = "/"
            else:
                url_path = url_path.replace("//", "/")
            full_url = "https://rankfyno.com" + (url_path if url_path.endswith("/") else url_path + "/")
            if p.name != "index.php":
                full_url = "https://rankfyno.com/" + str(rel).replace("\\", "/").replace(".php", "")
            pages.append((p.stat().st_mtime, full_url))
        except Exception:
            continue
    pages.sort(reverse=True)
    seen = set()
    out = []
    for _, url in pages:
        if url in seen:
            continue
        seen.add(url)
        out.append(url)
        if len(out) >= n:
            break
    return out

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--key", help="IndexNow key (or env INDEXNOW_KEY)")
    ap.add_argument("--url", help="Submit a single URL")
    ap.add_argument("--recent", type=int, default=0, help="Submit the N most recently modified pages")
    ap.add_argument("--sitemap", default="sitemap.xml", help="Sitemap to harvest URLs from (default: sitemap.xml)")
    args = ap.parse_args()

    key = args.key or ""
    if not key:
        print("ERROR: provide --key <32-char-hex> or set INDEXNOW_KEY env var.", file=sys.stderr)
        sys.exit(1)

    root = Path(__file__).parent.parent

    if args.url:
        urls = [args.url]
    elif args.recent:
        urls = collect_recent(root, args.recent)
    else:
        urls = collect_from_sitemap(root / args.sitemap) + collect_from_sitemap(root / "seo-sitemap.xml") + collect_from_sitemap(root / "blog-sitemap.xml")
        urls = list(dict.fromkeys(urls))  # dedupe, preserve order

    if not urls:
        print("No URLs to submit.")
        sys.exit(1)

    print(f"Submitting {len(urls)} URLs to IndexNow…")
    result = submit(urls, key)
    print(json.dumps(result, indent=2))
    sys.exit(0 if result.get("ok") else 1)

if __name__ == "__main__":
    main()