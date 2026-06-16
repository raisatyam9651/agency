#!/usr/bin/env python3
"""Wire <picture> hero images into all Haryana district pages + Haryana hub."""
import os

BASE = '/Users/bp/Desktop/Tools/Website-ui-ux-designe-skill/agency/seo/india'

districts = [
    ('ambala', 'Ambala'),
    ('bhiwani', 'Bhiwani'),
    ('charkhi-dadri', 'Charkhi Dadri'),
    ('faridabad', 'Faridabad'),
    ('fatehabad', 'Fatehabad'),
    ('gurugram', 'Gurugram'),
    ('hisar', 'Hisar'),
    ('jhajjar', 'Jhajjar'),
    ('jind', 'Jind'),
    ('kaithal', 'Kaithal'),
    ('karnal', 'Karnal'),
    ('kurukshetra', 'Kurukshetra'),
    ('mahendragarh', 'Mahendragarh'),
    ('nuh', 'Nuh'),
    ('palwal', 'Palwal'),
    ('panchkula', 'Panchkula'),
    ('panipat', 'Panipat'),
    ('rewari', 'Rewari'),
    ('rohtak', 'Rohtak'),
    ('sirsa', 'Sirsa'),
    ('sonipat', 'Sonipat'),
    ('yamunanagar', 'Yamunanagar'),
]

img_block_template = '''      <div class="hero-image-wrap">
        <picture>
          <img src="images/hero.jpg" alt="Best SEO Company in {name} — NEXUS organic growth trophy" class="hero-image" loading="eager" width="1280" height="720" />
        </picture>
      </div>
'''

old_marker = '</nav>\n      <div class="hero-meta">'

done = 0
failed = []

# Process district pages
for slug, name in districts:
    p = os.path.join(BASE, 'haryana', slug, 'index.html')
    with open(p) as f:
        h = f.read()
    new = h.replace(old_marker, '</nav>\n' + img_block_template.format(name=name) + '      <div class="hero-meta">', 1)
    if new == h:
        failed.append(slug)
        continue
    with open(p, 'w') as f:
        f.write(new)
    done += 1

# Process Haryana hub
hub_path = os.path.join(BASE, 'haryana', 'index.html')
with open(hub_path) as f:
    h = f.read()
hub_block = '''      <div class="hero-image-wrap">
        <picture>
          <img src="images/hero.jpg" alt="Best SEO Agency in Haryana — NEXUS district coverage map" class="hero-image" loading="eager" width="1280" height="720" />
        </picture>
      </div>
'''
hub_new = h.replace(old_marker, '</nav>\n' + hub_block + '      <div class="hero-meta">', 1)
hub_ok = hub_new != h
if hub_ok:
    with open(hub_path, 'w') as f:
        f.write(hub_new)

print(f'Districts updated: {done}/{len(districts)}')
print(f'Haryana hub updated: {hub_ok}')
if failed:
    print('Failed:', failed)
