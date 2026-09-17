"""Extract structured content blocks from fetched picocss.com docs HTML.

Emits one JSON file per page into en_src/<slug>.json with:
  meta: {slug, chapter, title, lead(md), url}
  blocks: ordered list of typed blocks for translation
"""
import json, pathlib, re
from bs4 import BeautifulSoup, NavigableString, Tag

BASE = pathlib.Path(__file__).parent
SRC = BASE / "en"
OUT = BASE / "en_src"
OUT.mkdir(exist_ok=True)

PAGES = sorted(p.stem for p in SRC.glob("*.html"))
SKIP = set()

def norm_text(s):
    return re.sub(r"\s+", " ", s.replace("\xa0", " ")).strip()

def inline_md(el):
    """Convert an inline-ish element subtree to markdown text."""
    if isinstance(el, NavigableString):
        return re.sub(r"\s+", " ", str(el).replace("\xa0", " "))
    if not isinstance(el, Tag):
        return ""
    name = el.name
    if name == "a":
        href = el.get("href", "")
        if href.startswith("/"):
            href = "https://picocss.com" + href
        return f"[{inline_md_children(el)}]({href})"
    if name == "code":
        return f"`{el.get_text()}`"
    if name == "mark":
        return f"**[{el.get_text(strip=True)}]**"
    if name in ("strong", "b"):
        return f"**{inline_md_children(el)}**"
    if name in ("em", "i"):
        return f"*{inline_md_children(el)}*"
    if name == "br":
        return "  \n"
    if name == "svg":
        return ""
    if name == "img":
        src = el.get("src", "")
        alt = el.get("alt", "")
        return f"![{alt}]({src})"
    return inline_md_children(el)

def inline_md_children(el):
    return "".join(inline_md(c) for c in el.children)

def clean_demo(node):
    """Serialize demo html: strip copy-to-clipboard link + footer code if any."""
    import copy
    el = copy.copy(node)
    for x in el.find_all(["footer", "svg"], limit=200):
        pass
    # remove footer.code and .copy-to-clipboard (shallow demo only)
    for f in el.find_all("footer", class_="code"):
        f.decompose()
    for a in el.find_all("a", class_="copy-to-clipboard"):
        a.decompose()
    html = str(el)
    html = re.sub(r"<!--\s*-->", "", html)
    html = re.sub(r"[ \t]+", " ", html)
    html = re.sub(r"\n\s*\n", "\n", html).strip()
    return html

def code_of(pre_container):
    pre = pre_container.find("pre") or pre_container.find("code")
    code = pre_container.find("code")
    lang = "html"
    if code and code.get("class"):
        m = [c for c in code["class"] if c.startswith("language-")]
        if m:
            lang = m[0][len("language-"):]
    text = pre.get_text() if pre else code.get_text()
    text = text.replace("\xa0", " ").strip("\n")
    return lang, text

def blockquote_md(bq):
    return "\n".join("> " + line for line in inline_md_children(bq).strip().splitlines())

def table_to_md(tbl):
    rows = []
    for tr in tbl.find_all("tr"):
        cells = [inline_md(td).replace("|", "\\|") for td in tr.find_all(["th", "td"])]
        rows.append("| " + " | ".join(cells) + " |")
    if len(rows) >= 2:
        ncol = rows[0].count("|") - 1
        rows.insert(1, "|" + " --- |" * ncol)
    return "\n".join(rows)

def parse_section(sec, blocks):
    for ch in sec.find_all(recursive=False):
        if id(ch) in SKIP:
            continue
        cls = ch.get("class") or []
        name = ch.name
        if name in ("h2", "h3"):
            a = ch.find("a")
            hid = (a.get("href", "")[1:] if a else "") or re.sub(r"[^a-z0-9-]", "-", ch.get_text(strip=True).lower())
            txt = norm_text(ch.get_text())
            blocks.append({"t": name, "text": re.sub(r"#$", "", txt), "id": hid})
        elif name == "p":
            md = inline_md_children(ch)
            if md.strip():
                blocks.append({"t": "p", "md": re.sub(r" {2,}", " ", md).strip()})
        elif name == "ul":
            blocks.append({"t": "ul", "items": [inline_md_children(li) for li in ch.find_all("li", recursive=False)]})
        elif name == "ol":
            blocks.append({"t": "ol", "items": [inline_md_children(li) for li in ch.find_all("li", recursive=False)]})
        elif name == "hr":
            blocks.append({"t": "hr"})
        elif name == "blockquote":
            blocks.append({"t": "quote", "md": inline_md_children(ch).strip()})
        elif name == "table":
            blocks.append({"t": "table", "md": table_to_md(ch)})
        elif name == "details":
            inner_code = ch.find("div", class_="code")
            if inner_code:
                lang, code = code_of(inner_code)
                summary = ch.find("summary")
                blocks.append({"t": "code", "lang": lang, "code": code, "title": norm_text(summary.get_text()) if summary else "", "collapsed": True})
            else:
                blocks.append({"t": "raw", "html": clean_demo(ch)})
        elif "code" in cls:
            lang, code = code_of(ch)
            blocks.append({"t": "code", "lang": lang, "code": code, "title": "", "collapsed": False, "small": "small" in cls})
        elif "component" in cls:  # article.component example
            footer = ch.find("footer", class_="code")
            lang, code = code_of(footer) if footer else ("html", "")
            demo = clean_demo(ch)
            blocks.append({"t": "example", "label": ch.get("aria-label", ""), "demo": demo, "lang": lang, "code": code})
        elif "family" in cls:  # colors palette card
            blocks.append({"t": "raw", "html": clean_demo(ch)})
        elif "overflow-auto" in cls:
            nxt = ch.find_next_sibling("div")
            lang, code = ("html", "")
            if nxt and "code" in (nxt.get("class") or []):
                lang, code = code_of(nxt)
                SKIP.add(id(nxt))
            blocks.append({"t": "example", "label": "", "demo": clean_demo(ch), "lang": lang, "code": code})
        elif name == "dialog":
            nxt = ch.find_next_sibling("div")
            lang, code = ("html", "")
            if nxt and "code" in (nxt.get("class") or []):
                lang, code = code_of(nxt)
                SKIP.add(id(nxt))
            blocks.append({"t": "example", "label": "", "demo": clean_demo(ch), "lang": lang, "code": code})
        elif name == "article":
            nxt = ch.find_next_sibling("div")
            if nxt and "code" in (nxt.get("class") or []) and ch.get("aria-label", "").endswith("example"):
                lang, code = code_of(nxt)
                SKIP.add(id(nxt))
                blocks.append({"t": "example", "label": ch.get("aria-label", ""), "demo": clean_demo(ch), "lang": lang, "code": code})
            else:
                blocks.append({"t": "raw", "html": clean_demo(ch)})
        elif name == "div":
            blocks.append({"t": "raw", "html": clean_demo(ch)})
        elif name == "section":
            parse_section(ch, blocks)  # nested section
        elif name in ("svg", "script", "style"):
            continue
        else:
            blocks.append({"t": "raw", "html": clean_demo(ch)})

def fix_dup_ids(blocks):
    seen = {}
    for b in blocks:
        if b["t"] in ("h2", "h3") and b.get("id"):
            i = seen.get(b["id"], 0)
            seen[b["id"]] = i + 1
            if i:
                b["id"] = f"{b['id']}-{i}"

def main():
    total = 0
    for slug in PAGES:
        SKIP.clear()
        soup = BeautifulSoup((SRC / f"{slug}.html").read_text(encoding="utf-8"), "html.parser")
        content = soup.find("div", id="content")
        hgroup = soup.find("hgroup")
        chapter = title = lead = ""
        if hgroup:
            cp = hgroup.find("p")
            chapter = norm_text(cp.get_text()) if cp else ""
            h1 = hgroup.find("h1")
            title = norm_text(h1.get_text()) if h1 else slug
            lead_p = hgroup.find_all("p")
            if len(lead_p) > 1:
                lead = norm_text(lead_p[1].get_text())
        # code-ish <code> inside lead: keep backticks via inline_md
        if hgroup and len(hgroup.find_all("p")) > 1:
            lead = inline_md_children(hgroup.find_all("p")[1]).strip()
        blocks = []
        for sec in content.find_all("section", recursive=False):
            if "edit-on-github" in (sec.get("class") or []):
                continue
            parse_section(sec, blocks)
        fix_dup_ids(blocks)
        # skip trailing nav paragraph (prev/next links)
        if blocks and blocks[-1]["t"] == "p" and blocks[-1]["md"].startswith("[") and "](/docs" in blocks[-1]["md"]:
            blocks.pop()
        out = {"meta": {"slug": slug, "chapter": chapter, "title": title, "lead": lead,
                        "url": f"https://picocss.com/docs/{'' if slug=='docs' else slug}"},
               "blocks": blocks}
        (OUT / f"{slug}.json").write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
        total += len(blocks)
    print("pages:", len(PAGES), "blocks:", total)

if __name__ == "__main__":
    main()
