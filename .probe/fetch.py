"""Fetch all picocss.com/docs pages to en/*.html"""
import pathlib, re, sys, urllib.request

PAGES = [
    "docs", "version-picker", "color-schemes", "classless", "conditional", "rtl",
    "css-variables", "sass", "colors",
    "container", "landmarks-section", "grid", "overflow-auto",
    "typography", "link", "button", "table",
    "forms", "forms/input", "forms/textarea", "forms/select", "forms/checkboxes",
    "forms/radios", "forms/switch", "forms/range",
    "accordion", "card", "dropdown", "group", "loading", "modal", "nav",
    "progress", "tooltip",
    "v2", "mission", "usage-scenarios", "brand", "built-with",
]

OUT = pathlib.Path(__file__).parent / "en"
OUT.mkdir(exist_ok=True)
UA = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}

def fetch(slug):
    dest = OUT / (slug.replace("/", "-") + ".html")
    if dest.exists() and dest.stat().st_size > 5000:
        return dest.name, "cached"
    url = f"https://picocss.com/docs/{'' if slug == 'docs' else slug}"
    req = urllib.request.Request(url, headers=UA)
    html = urllib.request.urlopen(req, timeout=30).read()
    dest.write_bytes(html)
    return dest.name, len(html)

from concurrent.futures import ThreadPoolExecutor
with ThreadPoolExecutor(6) as ex:
    for name, info in ex.map(fetch, PAGES):
        print(name, info)
