# eve-substack-archive

`EgD-ARC-001` · **EVEglyphDesign** · Key ID `EgD-KEY-2026-07`

A sovereign mirror of the Substack publications we read, and of everything we
eventually publish there. The repository is the record. The reading surface is ours.

**Read it here:** [the EVEglyphDesign Substack Archive](https://eveglyphdesign.github.io/eve-substack-archive/)

No click-through. Nothing that disappears when a platform changes its terms, its owner,
or its mind.

---

## What is held

| Publication | Author | Posts | Range | Mirrored |
|---|---|---:|---|---|
| [Frictionless Decisions](https://eveglyphdesign.github.io/eve-substack-archive/zanehall/) | Zane Hall | 107 | 2024-09-04 → 2026-07-24 | yes |
| The Wright Report | Bryan Dean Wright | — | — | registered |
| Rami Krispin's Newsletter | Rami Krispin | — | — | registered |
| AI Supremacy | Michael Spencer | — | — | registered |
| The Transformation Advantage | Ashutosh Bansal | — | — | LinkedIn, not Substack |

Registered means the source is in `sources.json` and one flag away from being mirrored.

## Layout

```
sources.json              register of tracked publications; "ingest": true mirrors it
archive/<key>/posts/      one Markdown file per post, YAML front matter, source URL
archive/<key>/index.md    human index, newest first
archive/<key>/index.json  machine index: dates, word counts, reactions, SHA-256
docs/                     the reading surface (GitHub Pages)
registry/PROVENANCE.md    SHA-256 of every mirrored file, and when it was taken
scripts/ingest.py         the ingester
scripts/build_site.py     the renderer
```

## Refreshing

```bash
python3 scripts/ingest.py --all        # pull new posts, rewrite only what changed
python3 scripts/build_site.py          # rebuild the reading surface
python3 scripts/provenance.py          # restamp the hash register
```

To add a publication, append it to `sources.json` with `"ingest": true` and run the
ingester. The ingester reads the publication's own public API and its sitemap; the
sitemap is what makes the archive complete, because the API only returns recent posts.
It crawls at one request per second by design — a quiet crawl gets every post, a fast
one gets rate-limited and silently drops half the archive.

## Standing

Copyright in each post remains with its author. This mirror is held for private reading,
citation and review, and it exists because a reader should not have to ask a platform's
permission to re-read something they already subscribed to. Nothing here is republished.

---

© 2026 EVEglyphDesign. All rights reserved. Controlled copy.
*Pour le bien-être du peuple.*
