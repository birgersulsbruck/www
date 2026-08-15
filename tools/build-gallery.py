#!/usr/bin/env python3
"""Rebuilds the photo grid in Photos.dc.html from photo-captions.json."""
import html, io, json

items = json.load(io.open("photo-captions.json", encoding="utf-8"))

cells = []
for file, title in items:
    src = "assets/Photos_files/originals/" + file.replace("&", "%26").replace(" ", "%20")
    t = html.escape(title, quote=True)
    cells.append(
        f'''        <figure style="margin: 0;">
          <a href="{src}" target="_blank" rel="noopener"><img src="{src}" alt="{t}" loading="lazy" style="width: 100%; aspect-ratio: 1; object-fit: cover; display: block;"></a>
          <figcaption style="padding: 6px 2px 0; font-size: 11px; line-height: 1.5; color: #ccc;">{t}</figcaption>
        </figure>''')

grid = f'''    <!-- GALLERY:START -->
    <div style="margin: 24px 30px 0; padding: 20px; background: #111;">
      <div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 24px 20px;">
{chr(10).join(cells)}
      </div>
    </div>
    <!-- GALLERY:END -->'''

with io.open("Photos.dc.html", encoding="utf-8") as f:
    s = f.read()

start, end = "    <!-- GALLERY:START -->", "<!-- GALLERY:END -->"
if start in s:
    pre = s[: s.index(start)]
    post = s[s.index(end) + len(end):]
    s = pre + grid + post
else:
    anchor = '    <div style="padding: 24px 30px 0;">\n\n      <dc-import name="HappyMates"'
    s = s.replace(anchor, grid + "\n" + anchor, 1)

with io.open("Photos.dc.html", "w", encoding="utf-8") as f:
    f.write(s)
print(f"wrote {len(items)} photos into Photos.dc.html")
