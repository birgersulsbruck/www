#!/usr/bin/env python3
"""Injects per-page SEO + Open Graph metadata into the static pages."""
import io, os

BASE = "https://birgersulsbruck.github.io/www"
DEFAULT_IMG = f"{BASE}/assets/Welcome_files/shapeimage_1.jpg"

PAGES = {
    "index.html": ("Birger Sulsbrück — Percussionist, Author & Educator",
        "Danish percussionist, author and educator. Specialist in Latin American percussion, Cuban music and salsa. Teacher at the Royal Danish Academy of Music.", ""),
    "Welcome.dc.html": ("Welcome — Birger Sulsbrück",
        "Danish percussionist, author and educator. Specialist in Latin American percussion, Cuban music and salsa. Teacher at the Royal Danish Academy of Music.", "Welcome.dc.html"),
    "News.dc.html": ("News — Birger Sulsbrück",
        "Latest news, concerts and projects from Danish percussionist Birger Sulsbrück.", "News.dc.html"),
    "Info.dc.html": ("Info & Biography — Birger Sulsbrück",
        "Biography and career of Birger Sulsbrück: Salsa Ná Ma, Royal Danish Academy of Music, RNCM Manchester, and 50+ years of Latin percussion.", "Info.dc.html"),
    "Seminars.dc.html": ("Seminars & Workshops — Birger Sulsbrück",
        "Percussion seminars, clinics and workshops in Latin American percussion, Cuban rhythms and salsa by Birger Sulsbrück.", "Seminars.dc.html"),
    "Books_CDs.dc.html": ("Books and CDs — Birger Sulsbrück",
        "Books and recordings by Birger Sulsbrück: 'Latin American Percussion', 'Congas • Tumbadoras', 'The Little Conga Book' and more.", "Books_CDs.dc.html"),
    "Download.dc.html": ("Download — Birger Sulsbrück",
        "Free downloads from Birger Sulsbrück, including recordings and teaching material.", "Download.dc.html"),
    "Photos.dc.html": ("Photos — Birger Sulsbrück",
        "Photo gallery: meetings with friends and great moments from Birger Sulsbrück's career, 1966 to today.",
        "Photos.dc.html", f"{BASE}/assets/Photos_files/originals/TitoP_84_LOW.jpg"),
    "Reviews.dc.html": ("Reviews — Birger Sulsbrück",
        "Press reviews and posters from Birger Sulsbrück's concerts, seminars and releases.", "Reviews.dc.html"),
}

NOINDEX = ["SiteNav.dc.html", "HappyMates.dc.html", "test.html"]
MARK = '<script src="./support.js"></script>'


def block(title, desc, path, img=DEFAULT_IMG):
    url = f"{BASE}/{path}" if path else f"{BASE}/"
    return f"""<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{url}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Birger Sulsbrück">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{img}">
<meta property="og:locale" content="en_GB">
<meta property="og:locale:alternate" content="da_DK">
<meta name="twitter:card" content="summary_large_image">
{MARK}"""


def inject(fname, snippet):
    with io.open(fname, encoding="utf-8") as f:
        s = f.read()
    if "og:title" in s or "noindex" in s:
        print(f"skip (already done): {fname}")
        return
    s = s.replace("<html>", '<html lang="en">', 1)
    s = s.replace(MARK, snippet, 1)
    with io.open(fname, "w", encoding="utf-8") as f:
        f.write(s)
    print(f"ok: {fname}")


for fname, meta in PAGES.items():
    img = meta[3] if len(meta) > 3 else DEFAULT_IMG
    inject(fname, block(meta[0], meta[1], meta[2], img))

for fname in NOINDEX:
    if os.path.exists(fname):
        inject(fname, f'<meta name="robots" content="noindex">\n{MARK}')

with io.open("sitemap.xml", "w", encoding="utf-8") as f:
    f.write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n')
    for meta in PAGES.values():
        url = f"{BASE}/{meta[2]}" if meta[2] else f"{BASE}/"
        f.write(f"  <url><loc>{url}</loc></url>\n")
    f.write("</urlset>\n")

with io.open("robots.txt", "w", encoding="utf-8") as f:
    f.write(f"User-agent: *\nAllow: /\nSitemap: {BASE}/sitemap.xml\n")

print("sitemap.xml + robots.txt written")
