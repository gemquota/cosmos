---
type: "concept"
title: "mykb for Humans — a Conceptual Guide"
description: "A plain-language orientation to mykb: what it is, how the knowledge is organized, how to read and navigate notes, and how RSIS3 consumes it"
tags: ["guide", "mykb", "onboarding", "orientation", "knowledge-base"]
timestamp: "2026-08-01T00:00:00Z"
status: "stable"
source: []
---

# mykb for Humans — a Conceptual Guide

## What mykb Is

mykb is a persistent, human-readable **knowledge base** and, at the same time,
the **long-term memory** of the RSIS3 self-improvement system. Everything in
it is a plain Markdown file with a small YAML header. That is the whole
trick: because the knowledge is ordinary files, a human can read it with any
text editor, and the machine can read it with the same tools that read code.

Think of it as a **wiki where every link is a graph edge**. Notes are typed
(`concept`, `source`, `synthesis`, `decision`, …), tagged, and timestamped;
the links between them are the structure. `graph.json` is a machine-readable
export of that structure, and the wiki browser renders it interactively.

## The Mental Model

One sentence: **mykb is a graph of typed notes that gets denser over time.**

- **Notes** are the nodes. Each note is a fact, idea, decision, session, or
  synthesis.
- **Wikilinks** (`[[wiki/concepts/...|Label]]`) are the edges. They are
  bidirectional in spirit: a note's `## Related` block points outward, and
  the graph view shows what points back.
- **Types** tell you what kind of knowledge a note holds. Frontmatter
  `type` is the first thing to read on any page.
- **Indexes** (`wiki/index.md`, `files.json`, `wiki/index.json`) are
  generated maps that let both humans and the browser find pages without
  walking the graph.

## The Layer Model

Knowledge moves through four layers as it matures:

| Layer | Location | What lives there |
|---|---|---|
| Raw | `raw/inbox/`, `raw/archive/` | unprocessed material, session dumps, archived low-utility artifacts |
| Sources | `wiki/sources/` | provenance: books, articles, conversations, datasets |
| Notes | `wiki/<area>/` | processed knowledge: concepts, decisions, sessions, area maps |
| Syntheses | `wiki/syntheses/` | distilled, durable conclusions — the highest-value layer |

Acquisition pushes material in from the bottom; synthesis pulls durable rules
out at the top. Curation (archiving, linking, pruning) keeps the middle
layers from rotting into a dump.

## The Knowledge Flywheel

1. **Acquire** — bring material in (see [[ops/knowledge-acquisition|Knowledge Acquisition]]).
2. **Curate** — type, tag, link, and archive so the graph stays dense and honest.
3. **Synthesize** — distill recurring patterns into `wiki/syntheses/` notes (see [[wiki/syntheses/knowledge-system|Knowledge System]]).
4. **Consume** — RSIS3 reads concepts and syntheses for planning, and writes pulses, decisions, and log lines back.

Each loop of the flywheel makes the next one cheaper: more links → better
retrieval → faster synthesis → better plans.

## How to Read a Note

1. **Frontmatter first**: `type`, `title`, `description`, `tags`, `timestamp`, `status` — one glance tells you what and how reliable.
2. **Summary** (if present): the claim in two sentences.
3. **Details**: the substance, usually bulleted with worked examples.
4. **Related**: the links outward — follow them to build context.

A good note is *one idea, well linked*. If a page needs a paragraph of
context, that context belongs in its own note.

## How to Navigate

- **Start**: [[Home]] → [[wiki/index|Wiki Index]].
- **By area**: `wiki/<area>/` directories each have an `index.md` listing their pages.
- **By graph**: open the graph view (browser or `okf server`), pick a hub like [[wiki/concepts/nine-loop-hierarchy|Nine-Loop Hierarchy]], and follow edges.
- **By search**: `okf search components/mykb <term>` for ranked concept search; the browser uses a bounded client-side search over `files.json`.

## How to Contribute

1. Use the templates in `templates/` (concept, source, synthesis, …).
2. Always write a `## Related` block with 3–8 real wikilinks.
3. Regenerate the maps after batch changes:
   `python3 .wiki-daemon/build_graph.py`, then `python3 gen-static-data.py` (repo root).
4. Validate: `okf validate .` and `okf lint .`.
5. Log the change in [[wiki/log|Iteration Log]] and update the relevant `index.md`.

## How RSIS3 Consumes It

RSIS3 treats mykb as its semantic database (the contract lives in
[[ops/rsis3-memory-bridge|RSIS3 Memory Bridge]]):

- reads concepts and syntheses to inform planning and strategy;
- writes pulses, decisions, identity snapshots, and log lines after loops;
- feeds the dashboard's MyKB tab (wiki browser + knowledge graph).

The rule that keeps this healthy: **mykb stays human-first** — machine
readability is a consequence of clean structure, never an excuse for
machine-only content.

## Glossary

- **OKF** — Open Knowledge Format: the frontmatter + markdown conventions this wiki follows.
- **Frontmatter** — the YAML header between `---` lines.
- **Wikilink** — `[[path|label]]`, the graph edge syntax.
- **Synthesis** — a distilled, cross-note conclusion (type `synthesis`).
- **Graph** — the node/edge structure derived from wikilinks and shared tags.

## Related

- [[wiki/index|Wiki Index]] — the map
- [[ops/rsis3-memory-bridge|RSIS3 Memory Bridge]] — the machine contract
- [[ops/wiki-schema|Wiki Schema]] — the frontmatter rules
- [[ops/knowledge-acquisition|Knowledge Acquisition]] — the workflow
- [[wiki/syntheses/knowledge-system|Knowledge System]] — the iteration loop
- [[wiki/concepts/triad-architecture|Triad Architecture]] — the wider ecosystem
