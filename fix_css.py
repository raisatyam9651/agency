import os
import glob
import re

files = glob.glob('c:/Users/GCV/Desktop/Tools/agency/youtube-marketing/**/*.php', recursive=True)

for path in files:
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    modified = False
    
    if '<style>' in content and '.ytm-hero' in content:
        # We need to move <style>...</style> into $custom_head if it's not already
        if '0 2px' in content:
            content = content.replace('rgba(255,255,255,0.03) 0 2px, transparent 2px 26px', 'rgba(255,255,255,0.03) 0, rgba(255,255,255,0.03) 2px, transparent 2px, transparent 26px')
            modified = True
        
        # Check if the style is outside PHP block but before <main class="ytm">
        if '?>\n<style>' in content or '?>\r\n<style>' in content:
            style_match = re.search(r'<style>.*?</style>', content, re.DOTALL)
            if style_match:
                style_str = style_match.group(0)
                # Remove it from current position
                content = content.replace(style_str + '\n', '')
                content = content.replace(style_str + '\r\n', '')
                content = content.replace(style_str, '')
                # Append to custom_head
                # Need to find custom_head assignment
                ch_match = re.search(r'(\$custom_head\s*=\s*".*?)(";\s*include)', content, re.DOTALL)
                if ch_match:
                    # Escape quotes in style_str
                    style_escaped = style_str.replace('"', '\\"')
                    new_ch = ch_match.group(1) + '\\n' + style_escaped + ch_match.group(2)
                    content = content.replace(ch_match.group(0), new_ch)
                    modified = True

    if modified:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f'Fixed {path}')
