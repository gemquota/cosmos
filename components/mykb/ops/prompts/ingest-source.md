---
type: prompt
title: ingest-source
description: Agent prompt for ingest source
tags: [prompt, ops]
---

# Prompt: Ingest Source

Ingest one source from `raw/inbox/` into the wiki.

Follow these steps:

1. Preserve the original source path or link.
2. Create a source page in `wiki/sources/YYYY-MM-DD-slug.md`.
3. Fill in frontmatter with `type: source`, `status: seed`, and source links.
4. Summarize the source in your own words.
5. Extract key claims, useful ideas, and uncertainties.
6. Link or create related concept, question, project, domain, or synthesis pages.
7. Update `wiki/index.md` if this source becomes an important entry point.
8. Add a short entry to `wiki/log.md` for meaningful changes.

Do not invent missing facts. Mark uncertain points as `to verify`.
