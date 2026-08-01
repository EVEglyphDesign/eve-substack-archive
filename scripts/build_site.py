#!/usr/bin/env python3
"""Render the mirrored archive into the EVEglyphDesign reading surface under docs/.

One index per publication, one page per post, one register at the root. No
Substack click-through: everything is read here.

    python3 scripts/build_site.py
"""
import html
import json
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOCS = os.path.join(ROOT, "docs")

CSS = """
:root{--cream:#fdfaf4;--cream2:#f7f2e7;--ink:#1a1a1a;--line:#e7e1d3;--mute:#6b665c;--accent:#e87722}
*{box-sizing:border-box}
html{-webkit-text-size-adjust:100%}
body{margin:0;background:var(--cream);color:var(--ink);
 font:400 17px/1.68 Inter,system-ui,-apple-system,Segoe UI,sans-serif}
.wrap{max-width:760px;margin:0 auto;padding:0 22px}
header.top{border-bottom:1px solid var(--line);background:var(--cream2)}
header.top .wrap{padding-top:26px;padding-bottom:26px}
.kicker{font-size:11px;letter-spacing:.22em;text-transform:uppercase;color:var(--mute);margin:0 0 8px}
h1{font-family:Fraunces,Georgia,serif;font-weight:600;font-size:34px;line-height:1.15;margin:0 0 8px}
h2{font-family:Fraunces,Georgia,serif;font-weight:600;font-size:25px;line-height:1.2;margin:38px 0 12px}
h3{font-family:Fraunces,Georgia,serif;font-weight:600;font-size:20px;margin:30px 0 10px}
.lede{color:var(--mute);font-size:17px;margin:0}
a{color:var(--accent);text-decoration:none;border-bottom:1px solid rgba(232,119,34,.35)}
a:hover{border-bottom-color:var(--accent)}
main{padding:34px 0 70px}
.meta{font-size:13px;color:var(--mute);margin:0 0 26px}
.meta b{color:var(--ink);font-weight:600}
table{border-collapse:collapse;width:100%;font-size:15px;margin:18px 0}
th,td{text-align:left;padding:9px 10px;border-bottom:1px solid var(--line);vertical-align:top}
th{font-size:11px;letter-spacing:.14em;text-transform:uppercase;color:var(--mute);font-weight:600}
td.n,th.n{text-align:right;white-space:nowrap;font-variant-numeric:tabular-nums}
td.d{white-space:nowrap;color:var(--mute);font-size:13px}
blockquote{margin:22px 0;padding:2px 0 2px 18px;border-left:3px solid var(--accent);color:var(--mute)}
code{background:var(--cream2);padding:1px 5px;border-radius:3px;font-size:14px}
img{max-width:100%;height:auto;border-radius:3px;margin:18px 0}
hr{border:0;border-top:1px solid var(--line);margin:32px 0}
.nav{font-size:13px;color:var(--mute);padding:16px 0;border-bottom:1px solid var(--line)}
.pager{display:flex;justify-content:space-between;gap:16px;font-size:14px;
 border-top:1px solid var(--line);padding-top:20px;margin-top:38px}
footer{border-top:1px solid var(--line);background:var(--cream2);color:var(--mute);font-size:13px}
footer .wrap{padding:22px}
.mark{font-family:Fraunces,Georgia,serif;font-style:italic;color:var(--accent)}
.card{border:1px solid var(--line);border-radius:4px;padding:16px 18px;margin:14px 0;background:#fff}
.card h3{margin:0 0 4px;font-size:19px}
.card p{margin:4px 0 0;font-size:14px;color:var(--mute)}
.off{opacity:.62}
@media(max-width:520px){h1{font-size:27px}body{font-size:16px}}
"""

HEAD = """<!doctype html><html lang="en"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>%(title)s</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,400;9..144,600&family=Inter:wght@400;600;700&display=swap" rel="stylesheet">
<style>%(css)s</style></head><body>
"""

FOOT = ("<footer><div class=\"wrap\">&copy; 2026 EVEglyphDesign. Reading surface, controlled copy. "
        "Key ID EgD-KEY-2026-07. Copyright in each post remains with its author; this mirror is held "
        "for private reading and review. <span class=\"mark\">Pour le bien-&ecirc;tre du peuple</span>"
        "</div></footer></body></html>\n")


def e(s):
    return html.escape(s or "")


# --------------------------------------------------------------- markdown

def inline(s):
    s = e(s)
    s = re.sub(r"!\[[^\]]*\]\((https?://[^)\s]+)\)", r'<img src="\1" alt="">', s)
    s = re.sub(r"\[([^\]]+?)\]\((https?://[^)\s]+?)\)", r'<a href="\2" rel="noopener">\1</a>', s)
    s = re.sub(r"\*\*([^*]+?)\*\*", r"<b>\1</b>", s)
    s = re.sub(r"(?<!\*)\*([^*\n]+?)\*(?!\*)", r"<i>\1</i>", s)
    s = re.sub(r"`([^`]+?)`", r"<code>\1</code>", s)
    return s


def md_to_html(md):
    out, buf, lst, quote = [], [], False, False

    def flush():
        if buf:
            out.append("<p>%s</p>" % inline(" ".join(buf).strip()))
            buf.clear()

    def close():
        nonlocal lst, quote
        if lst:
            out.append("</ul>")
            lst = False
        if quote:
            out.append("</blockquote>")
            quote = False

    for raw in md.split("\n"):
        line = raw.rstrip()
        if not line.strip():
            flush()
            close()
            continue
        m = re.match(r"^(#{1,6})\s+(.*)$", line)
        if m:
            flush()
            close()
            n = min(len(m.group(1)), 4)
            out.append("<h%d>%s</h%d>" % (n, inline(m.group(2)), n))
            continue
        if line.strip() in ("---", "***", "___"):
            flush()
            close()
            out.append("<hr>")
            continue
        if line.startswith("> "):
            flush()
            if lst:
                out.append("</ul>")
                lst = False
            if not quote:
                out.append("<blockquote>")
                quote = True
            out.append("<p>%s</p>" % inline(line[2:]))
            continue
        m = re.match(r"^[-*]\s+(.*)$", line)
        if m:
            flush()
            if quote:
                out.append("</blockquote>")
                quote = False
            if not lst:
                out.append("<ul>")
                lst = True
            out.append("<li>%s</li>" % inline(m.group(1)))
            continue
        if re.match(r"^!\[[^\]]*\]\(https?://", line.strip()):
            flush()
            close()
            out.append(inline(line.strip()))
            continue
        if quote:
            out.append("<p>%s</p>" % inline(line))
            continue
        buf.append(line.strip())
    flush()
    close()
    return "\n".join(out)


def split_front(text):
    if not text.startswith("---"):
        return {}, text
    end = text.index("\n---", 3)
    fm = {}
    for line in text[3:end].strip().split("\n"):
        if ":" in line:
            k, v = line.split(":", 1)
            v = v.strip()
            if v.startswith('"') and v.endswith('"'):
                try:
                    v = json.loads(v)
                except Exception:
                    v = v.strip('"')
            fm[k.strip()] = v
    return fm, text[end + 4:]


# ------------------------------------------------------------------ build

def build():
    src = json.load(open(os.path.join(ROOT, "sources.json")))
    os.makedirs(DOCS, exist_ok=True)
    cards = []
    for s in src["sources"]:
        key = s["key"]
        ipath = os.path.join(ROOT, "archive", key, "index.json")
        if not os.path.exists(ipath):
            cards.append('<div class="card off"><h3>%s</h3><p>%s &middot; %s</p>'
                         '<p>Not mirrored. Set <code>"ingest": true</code> in '
                         '<code>sources.json</code> and re-run the ingester.</p></div>'
                         % (e(s["title"]), e(s["author"]), e(s.get("subject", ""))))
            continue
        meta = json.load(open(ipath))
        posts = meta["posts"]
        build_pub(key, s, posts)
        cards.append('<div class="card"><h3><a href="./%s/">%s</a></h3>'
                     '<p>%s &middot; %d posts &middot; %s to %s &middot; %s words</p>'
                     '<p>%s</p></div>'
                     % (key, e(s["title"]), e(s["author"]), len(posts),
                        posts[-1]["date"], posts[0]["date"],
                        format(sum(p["words"] for p in posts), ","),
                        e(s.get("subject", ""))))
    body = (HEAD % {"title": "EVEglyphDesign — Substack Archive", "css": CSS}
            + '<header class="top"><div class="wrap">'
              '<p class="kicker">EVEglyphDesign &middot; EgD-ARC-001</p>'
              '<h1>Substack Archive</h1>'
              '<p class="lede">The publications we read, mirrored into the repository and '
              'rendered here. One surface, no click-through, nothing that disappears when a '
              'platform changes its mind.</p></div></header>'
            + '<main><div class="wrap">'
            + "\n".join(cards)
            + '<h2>How it works</h2><p>Every post is pulled from the publication\'s own API into '
              'Markdown under <code>archive/&lt;key&gt;/posts/</code>, hashed, and committed. '
              'The register of tracked publications is <code>sources.json</code>. Re-run '
              '<code>python3 scripts/ingest.py --all</code> to refresh, then '
              '<code>python3 scripts/build_site.py</code> to rebuild these pages. '
              'Source of record: <a href="https://github.com/EVEglyphDesign/eve-substack-archive">'
              'the repository</a>.</p>'
              '</div></main>' + FOOT)
    open(os.path.join(DOCS, "index.html"), "w", encoding="utf-8").write(body)
    print("wrote docs/index.html")


def build_pub(key, s, posts):
    out = os.path.join(DOCS, key)
    os.makedirs(out, exist_ok=True)
    rows = []
    for p in posts:
        rows.append('<tr><td class="d">%s</td><td><a href="./%s.html">%s</a></td>'
                    '<td class="n">%s</td><td class="n">%s</td><td class="n">%s</td></tr>'
                    % (p["date"], os.path.basename(p["file"])[:-3], e(p["title"]),
                       p["words"], p["reactions"], p["comments"]))
    page = (HEAD % {"title": "%s — EVEglyphDesign Archive" % s["title"], "css": CSS}
            + '<header class="top"><div class="wrap">'
              '<p class="kicker"><a href="../">Substack Archive</a> &middot; %s</p>'
              '<h1>%s</h1><p class="lede">%s &mdash; %s</p></div></header>'
              % (e(key), e(s["title"]), e(s["author"]), e(s.get("subject", "")))
            + '<main><div class="wrap"><p class="meta"><b>%d posts</b> &middot; %s to %s '
              '&middot; %s words &middot; mirrored from %s</p>'
              % (len(posts), posts[-1]["date"], posts[0]["date"],
                 format(sum(p["words"] for p in posts), ","), e(s["host"]))
            + '<table><thead><tr><th>Date</th><th>Post</th><th class="n">Words</th>'
              '<th class="n">&hearts;</th><th class="n">Comments</th></tr></thead><tbody>'
            + "\n".join(rows) + "</tbody></table></div></main>" + FOOT)
    open(os.path.join(out, "index.html"), "w", encoding="utf-8").write(page)

    for i, p in enumerate(posts):
        text = open(os.path.join(ROOT, p["file"]), encoding="utf-8").read()
        fm, body = split_front(text)
        body = re.sub(r"^#\s+.*$", "", body.strip(), count=1, flags=re.M).strip()
        body = re.sub(r"\n---\n\nSource: \[[\s\S]*$", "", body).strip()
        nxt = posts[i - 1] if i > 0 else None
        prv = posts[i + 1] if i + 1 < len(posts) else None
        pager = []
        if prv:
            pager.append('<a href="./%s.html">&larr; %s</a>'
                         % (os.path.basename(prv["file"])[:-3], e(prv["title"])))
        else:
            pager.append("<span></span>")
        if nxt:
            pager.append('<a href="./%s.html">%s &rarr;</a>'
                         % (os.path.basename(nxt["file"])[:-3], e(nxt["title"])))
        else:
            pager.append("<span></span>")
        page = (HEAD % {"title": "%s — %s" % (p["title"], s["title"]), "css": CSS}
                + '<header class="top"><div class="wrap">'
                  '<p class="kicker"><a href="../">Archive</a> &middot; '
                  '<a href="./">%s</a></p><h1>%s</h1>%s</div></header>'
                  % (e(s["title"]), e(p["title"]),
                     '<p class="lede">%s</p>' % e(fm.get("subtitle", "")) if fm.get("subtitle") else "")
                + '<main><div class="wrap"><p class="meta">%s &middot; <b>%s</b> &middot; %s words '
                  '&middot; %s reactions &middot; %s comments &middot; '
                  '<a href="%s" rel="noopener">original</a></p>'
                  % (p["date"], e(s["author"]), p["words"], p["reactions"],
                     p["comments"], e(p["url"]))
                + md_to_html(body)
                + '<div class="pager">%s</div></div></main>' % "".join(pager) + FOOT)
        open(os.path.join(out, os.path.basename(p["file"])[:-3] + ".html"),
             "w", encoding="utf-8").write(page)
    print("wrote docs/%s/ (%d pages)" % (key, len(posts) + 1))


if __name__ == "__main__":
    build()
