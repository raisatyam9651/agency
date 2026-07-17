"""
Fix malformed hero <picture> markup across all city/location index.php pages.

Broken pattern (renders a literal "/>" text node + invalid nested <picture>):
    <picture>
      <picture><source srcset="../images/hero.webp" type="image/webp"><img ... />/></picture>
    </picture>

Fixed pattern (single, valid <picture>):
    <picture>
      <source srcset="../images/hero.webp" type="image/webp"><img ... />
    </picture>

Only the inner (nested) <picture>, the stray "/>", and the inner </picture> are
removed; the outer <picture>...</picture> wrapper and the per-page alt text are
preserved verbatim.
"""
import glob
import re

ROOT = 'c:/Users/GCV/Desktop/Tools/agency'
PATTERN = re.compile(
    r'<picture><source srcset="(?P<src>[^"]*)" type="image/webp">'
    r'(?P<img><img [^>]*?/>)'
    r'/></picture>'
)

def repl(m):
    return f'<source srcset="{m.group("src")}" type="image/webp">{m.group("img")}'

files = glob.glob(f'{ROOT}/**/index.php', recursive=True)
fixed = 0
skipped_multi = []
for path in files:
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    n = len(PATTERN.findall(content))
    if n == 0:
        continue
    if n > 1:
        skipped_multi.append((path, n))
    new = PATTERN.sub(repl, content)
    if new != content:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(new)
        fixed += 1

print(f'Files fixed: {fixed}')
if skipped_multi:
    print('WARNING multi-match files:', skipped_multi)
