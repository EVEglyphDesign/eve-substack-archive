#!/usr/bin/env python3
"""Restamp registry/PROVENANCE.md — SHA-256 of every mirrored file."""
import datetime
import hashlib
import json
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
now = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
src = json.load(open(os.path.join(ROOT, "sources.json")))

out = ["# Provenance register", "",
       "`EgD-ARC-001` · Key ID `EgD-KEY-2026-07` · restamped **%s**" % now, "",
       "SHA-256 of every mirrored file, taken at the moment of the last ingest. "
       "A file whose hash has not moved has not been touched.", ""]
total = 0
for s in src["sources"]:
    p = os.path.join(ROOT, "archive", s["key"], "index.json")
    if not os.path.exists(p):
        continue
    m = json.load(open(p))
    out += ["## %s — `%s`" % (s["title"], s["key"]), "",
            "Source `%s` · %d posts · %s to %s" % (
                s["host"], m["post_count"], m["posts"][-1]["date"], m["posts"][0]["date"]), "",
            "| Date | File | SHA-256 |", "|---|---|---|"]
    for r in m["posts"]:
        out.append("| %s | `%s` | `%s` |" % (r["date"], os.path.basename(r["file"]), r["sha256"]))
        total += 1
    out.append("")
    idx = open(os.path.join(ROOT, "archive", s["key"], "index.md"), "rb").read()
    out += ["Index digest `%s`" % hashlib.sha256(idx).hexdigest(), ""]

out += ["---", "", "%d files registered." % total, "",
        "© 2026 EVEglyphDesign. All rights reserved. Controlled copy.",
        "*Pour le bien-être du peuple.*", ""]
os.makedirs(os.path.join(ROOT, "registry"), exist_ok=True)
open(os.path.join(ROOT, "registry", "PROVENANCE.md"), "w",
     encoding="utf-8").write("\n".join(out))
print("registry/PROVENANCE.md — %d files" % total)
