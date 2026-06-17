import os
import re
from urllib.parse import urlparse

def get_relative_links(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    links = re.findall(r'(?:href|src)=["\']([^"\']+)["\']', content)
    relative_links = []
    for link in links:
        if (link.startswith('http://') or link.startswith('https://') or
            link.startswith('#') or link.startswith('mailto:') or link.startswith('tel:')):
            continue
        parsed = urlparse(link)
        clean_link = parsed.path
        if not clean_link:
            continue
        relative_links.append(clean_link)
    return relative_links

def verify_links():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    print(f"Base Directory: {base_dir}")
    html_files = []
    for root, dirs, files in os.walk(base_dir):
        if '_build' in root or 'images' in root:
            continue
        for file in files:
            if file.endswith('.html'):
                html_files.append(os.path.join(root, file))
    print(f"Found {len(html_files)} HTML files to check.")
    broken_links_count = 0
    total_links_checked = 0
    for file_path in html_files:
        rel_dir = os.path.dirname(file_path)
        rel_links = get_relative_links(file_path)
        for link in rel_links:
            total_links_checked += 1
            target_path = os.path.abspath(os.path.join(rel_dir, link))
            if os.path.isdir(target_path):
                target_path = os.path.join(target_path, 'index.html')
            if not os.path.exists(target_path):
                print(f"BROKEN LINK in [{os.path.relpath(file_path, base_dir)}]: '{link}' -> Resolved as: {target_path}")
                broken_links_count += 1
    print("-" * 50)
    print(f"Verification completed.")
    print(f"Total links checked: {total_links_checked}")
    print(f"Broken links found: {broken_links_count}")
    if broken_links_count > 0:
        return False
    return True

if __name__ == "__main__":
    success = verify_links()
    if not success:
        exit(1)
    else:
        print("Success! All links are valid.")
        exit(0)
