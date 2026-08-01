---
type: "concept"
title: "Knowledge Acquisition"
description: "Repeatable workflow for research, ingestion, linking, and curation rounds in mykb"
tags: ["workflow", "curation", "research", "ingestion", "mykb"]
timestamp: "2026-07-31T00:00:00Z"
---

# Knowledge Acquisition

The acquisition loop turns online research into durable, linked knowledge. Each
round follows five phases; this page is the operating procedure.

## The Loop

1. **Scope** — pick themes aligned to RSIS3's needs (agents, memory, semantics,
   LLM engineering, infra) and list target concepts.
2. **Research** — fetch authoritative sources (docs, papers, repos); record
   provenance in `raw/inbox/`.
3. **Write** — one file per concept under `wiki/<area>/`, with YAML frontmatter
   (`type`, `title`, `description`, `tags`, `timestamp`).
4. **Link** — every article ends with a `## Related` block of `[[wikilinks]]` to
   other new and existing articles. The graph is the measure.
5. **Curate** — archive low-utility stubs (auto-generated session artifacts),
   expand high-utility ones, update indexes, and report in
   `ops/reports/`.

## Conventions

- Full articles: 150–400 words, sections, at least 3 related links.
- Stubs: frontmatter + 3–6 line skeleton + related links (expansion targets).
- Stub status marked `status: stub`; grown articles flip to `status: growing`.
- Never delete — archive under `raw/archive/` when an article has low utility.
- Run `okf validate .` and `okf lint .` after each round; regenerate
  `wiki/index.json`, `files.json`, and `graph.json`.

## Provenance

Keep a `## Sources` section with the URLs used; for web-derived facts, prefer
primary documentation over secondary summaries.

## Related

- [[ops/rsis3-memory-bridge|RSIS3 Memory Bridge]]
- [[wiki/syntheses/knowledge-system|Knowledge System]]
- [[ops/workflows|Workflows]]
- [[ops/wiki-schema|Wiki Schema]]
- [[wiki/sources/README|Sources]]
