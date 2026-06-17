import os
import re
from urllib.parse import urlparse

# Directories to search
base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

def check_html_files():
    html_files = []
    for root, dirs, files in os.walk(base_dir):
        if "_build" in root:
            continue
        for file in files:
            if file.endswith(".html"):
                html_files.append(os.path.join(root, file))
                
    print(f"Checking {len(html_files)} HTML files for broken relative links...")
    broken_count = 0
    checked_count = 0
    
    # Regex to find links: href="...", src="..."
    link_pattern = re.compile(r'(?:href|src)="([^"]+)"')
    
    for html_file in html_files:
        with open(html_file, "r", encoding="utf-8") as f:
            content = f.read()
            
        links = link_pattern.findall(content)
        for link in links:
            # Skip absolute urls, mailto, tel, hashes
            if link.startswith(("http://", "https://", "mailto:", "tel:", "#")):
                continue
            # Parse url to ignore queries or hashes
            parsed = urlparse(link)
            path = parsed.path
            if not path:
                continue
                
            # Compute target path relative to html file
            target_path = os.path.abspath(os.path.join(os.path.dirname(html_file), path))
            
            checked_count += 1
            if not os.path.exists(target_path):
                print(f"❌ Broken link in {os.path.relpath(html_file, base_dir)}: {link} (resolved to {os.path.relpath(target_path, base_dir)})")
                broken_count += 1
                
    if broken_count == 0:
        print(f"✅ All {checked_count} relative links resolve successfully across all pages!")
    else:
        print(f"❌ Found {broken_count} broken relative links.")

if __name__ == "__main__":
    check_html_files()
