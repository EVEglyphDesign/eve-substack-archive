#!/usr/bin/env python3
"""EVEglyphDesign — Substack ingester.

Pulls a publication's full post archive into Markdown files under
archive/<key>/posts/, writes a per-publication index, and records a SHA-256 for
every file in registry/PROVENANCE.md. Re-runnable: existing files are rewritten
only when the source content hash changes.

    python3 scripts/ingest.py <key> <host>
    python3 scripts/ingest.py --all
"""
import hashlib
import html as htmlmod
import json
import os
import re
import subprocess
import sys
import time

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SOURCES = os.path.join(ROOT, "sources.json")
UA = "Mozilla/5.0 (compatible; EVEglyphDesign-archive/1.0)"


def curl(url):
    for attempt in range(3):
        r = subprocess.run(["curl", "-sSL", "-A", UA, url],
                           capture_output=True, text=True)
        if r.returncode == 0 and r.stdout.strip():
            return r.stdout
        time.sleep(1.5 * (attempt + 1))
    return ""


def archive_list(host):
    """Every post in the publication, newest first."""
    out, off = [], 0
    while True:
        raw = curl("https://%s/api/v1/archive?sort=new&offset=%d&limit=50" % (host, off))
        try:
            page = json.loads(raw)
        except Exception:
            break
        if not isinstance(page, list) or not page:
            break
        out += page
        if len(page) < 50:
            break
        off += 50
        time.sleep(0.4)
    return out


def sitemap_slugs(host):
    """The archive API only returns recent posts; the sitemap carries them all."""
    out = []
    for path in ("sitemap.xml", "sitemap/2024", "sitemap/2025", "sitemap/2026"):
        raw = curl("https://%s/%s" % (host, path))
        for loc in re.findall(r"<loc>([^<]+)</loc>", raw):
            m = re.match(r"https?://[^/]+/p/([^/?#]+)", loc)
            if m and m.group(1) not in out:
                out.append(m.group(1))
    return out


def post_body(host, slug):
    raw = curl("https://%s/api/v1/posts/%s" % (host, slug))
    try:
        return json.loads(raw)
    except Exception:
        return {}


# ---------------------------------------------------------------- html -> md

BLOCK = re.compile(r"</?(div|figure|figcaption|section|article|span|a|img|p|h[1-6]|"
                   r"ul|ol|li|blockquote|pre|code|em|strong|b|i|hr|br|table|thead|"
                   r"tbody|tr|td|th)[^>]*>", re.I)


def to_markdown(html):
    s = html or ""
    s = re.sub(r"<script[\s\S]*?</script>", "", s, flags=re.I)
    s = re.sub(r"<style[\s\S]*?</style>", "", s, flags=re.I)
    # images
    s = re.sub(r'<img[^>]*?src="([^"]+)"[^>]*?>', r"\n\n![](\1)\n\n", s, flags=re.I)
    # an anchor wrapping nothing but an image is chrome, not a link
    s = re.sub(r"<a\b[^>]*>\s*(!\[\]\([^)]*\))\s*</a>", r"\1", s, flags=re.I)
    # links
    s = re.sub(r'<a[^>]*?href="([^"]+)"[^>]*?>([\s\S]*?)</a>',
               lambda m: ("[%s](%s)" % (re.sub(r"\s+", " ", m.group(2)).strip(), m.group(1))
                          if "![](" not in m.group(2)
                          else re.sub(r"\s+", " ", m.group(2)).strip()),
               s, flags=re.I)
    # headings
    for n in range(1, 7):
        s = re.sub(r"<h%d[^>]*>([\s\S]*?)</h%d>" % (n, n),
                   lambda m, n=n: "\n\n%s %s\n\n" % ("#" * min(n + 1, 6), m.group(1).strip()),
                   s, flags=re.I)
    s = re.sub(r"<(strong|b)[^>]*>([\s\S]*?)</\1>", r"**\2**", s, flags=re.I)
    s = re.sub(r"<(em|i)[^>]*>([\s\S]*?)</\1>", r"*\2*", s, flags=re.I)
    s = re.sub(r"<li[^>]*>([\s\S]*?)</li>", r"\n- \1", s, flags=re.I)
    s = re.sub(r"<blockquote[^>]*>([\s\S]*?)</blockquote>",
               lambda m: "\n\n" + "\n".join("> " + x for x in
                                            re.sub(r"<[^>]+>", "", m.group(1)).strip().split("\n") if x.strip()) + "\n\n",
               s, flags=re.I)
    s = re.sub(r"<hr[^>]*>", "\n\n---\n\n", s, flags=re.I)
    s = re.sub(r"</p>|<br[^>]*>", "\n\n", s, flags=re.I)
    s = BLOCK.sub("", s)
    s = re.sub(r"<[^>]+>", "", s)
    s = htmlmod.unescape(s)
    s = re.sub(r"[ \t]+\n", "\n", s)
    s = re.sub(r"\n{3,}", "\n\n", s)
    return s.strip()


def slugify(t):
    return re.sub(r"-+", "-", re.sub(r"[^a-z0-9]+", "-", (t or "").lower())).strip("-")[:70]


def ingest(key, host, title):
    pdir = os.path.join(ROOT, "archive", key, "posts")
    os.makedirs(pdir, exist_ok=True)
    posts = archive_list(host)
    known = {p.get("slug"): p for p in posts if p.get("slug")}
    for slug in sitemap_slugs(host):
        known.setdefault(slug, {"slug": slug})
    rows, written = [], 0
    for slug, p in known.items():
        full = post_body(host, slug)
        time.sleep(1.0)  # Substack rate-limits; a quiet crawl gets every post
        if full:
            merged = dict(full)
            merged.update({k: v for k, v in p.items() if v not in (None, "")})
            p = merged
        date = (p.get("post_date") or "")[:10]
        body = to_markdown(full.get("body_html") or "")
        paywalled = not body and p.get("audience") not in ("everyone",)
        fname = "%s-%s.md" % (date, slug)
        url = p.get("canonical_url") or "https://%s/p/%s" % (host, slug)
        fm = [
            "---",
            "title: %s" % json.dumps(p.get("title") or ""),
            "subtitle: %s" % json.dumps(p.get("subtitle") or ""),
            "date: %s" % date,
            "publication: %s" % json.dumps(title),
            "author: %s" % json.dumps(", ".join(
                b.get("name", "") for b in (p.get("publishedBylines") or []))),
            "source_url: %s" % url,
            "audience: %s" % (p.get("audience") or ""),
            "wordcount: %s" % (p.get("wordcount") or 0),
            "reactions: %s" % (p.get("reaction_count") or 0),
            "comments: %s" % (p.get("comment_count") or 0),
            "restacks: %s" % (p.get("restacks") or 0),
            "ingested_by: EVEglyphDesign eve-substack-archive",
            "---",
            "",
            "# %s" % (p.get("title") or ""),
            "",
        ]
        if p.get("subtitle"):
            fm += ["*%s*" % p["subtitle"], ""]
        fm += [body if body else
               "> Body not retrievable from the public API%s." %
               (" (subscriber-only post)" if paywalled else ""), ""]
        fm += ["---", "", "Source: [%s](%s)" % (p.get("title") or url, url)]
        text = "\n".join(fm) + "\n"
        path = os.path.join(pdir, fname)
        old = open(path, encoding="utf-8").read() if os.path.exists(path) else ""
        if old != text:
            open(path, "w", encoding="utf-8").write(text)
            written += 1
        rows.append({
            "file": "archive/%s/posts/%s" % (key, fname),
            "date": date, "title": p.get("title") or "", "url": url,
            "words": p.get("wordcount") or 0,
            "reactions": p.get("reaction_count") or 0,
            "comments": p.get("comment_count") or 0,
            "restacks": p.get("restacks") or 0,
            "audience": p.get("audience") or "",
            "sha256": hashlib.sha256(text.encode()).hexdigest(),
            "body_chars": len(body),
        })
    rows.sort(key=lambda r: r["date"], reverse=True)
    meta = {"key": key, "host": host, "title": title,
            "post_count": len(rows), "posts": rows}
    json.dump(meta, open(os.path.join(ROOT, "archive", key, "index.json"), "w"), indent=1)
    # human index
    lines = ["# %s" % title, "",
             "`%s` · %d posts mirrored from `%s`." % (key, len(rows), host), "",
             "| Date | Post | Words | ♥ | 💬 | ↻ |", "|---|---|---:|---:|---:|---:|"]
    for r in rows:
        lines.append("| %s | [%s](posts/%s) | %s | %s | %s | %s |" % (
            r["date"], r["title"].replace("|", "\\|"),
            os.path.basename(r["file"]), r["words"], r["reactions"],
            r["comments"], r["restacks"]))
    lines += ["", "© 2026 EVEglyphDesign. Mirror held for private reading and review.",
              "Copyright in the posts remains with their author.", ""]
    open(os.path.join(ROOT, "archive", key, "index.md"), "w",
         encoding="utf-8").write("\n".join(lines))
    print("%s: %d posts, %d files written" % (key, len(rows), written))
    return meta


def main():
    src = json.load(open(SOURCES))
    args = sys.argv[1:]
    if args and args[0] == "--all":
        targets = [s for s in src["sources"] if s.get("ingest")]
    elif len(args) >= 2:
        targets = [{"key": args[0], "host": args[1], "title": args[0]}]
    else:
        targets = [s for s in src["sources"] if s.get("ingest")]
    for s in targets:
        ingest(s["key"], s["host"], s.get("title", s["key"]))


if __name__ == "__main__":
    main()
