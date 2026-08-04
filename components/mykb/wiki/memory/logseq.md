---
type: "entity"
title: "Logseq"
description: "Outliner-based, local-first note app with block-level links and a graph view"
tags: ["logseq", "tool", "outliner", "pkm"]
timestamp: "2026-07-31T00:00:00Z"
status: "growing"
---

# Logseq

## Summary
Logseq is a local-first knowledge app organized as an outliner, where every block can be linked, tagged, and referenced. Its block-level granularity suits dense interlinking and daily-journal workflows: a single bullet is a first-class addressable unit, so a note can embed another note's bullet instead of copying it.

## Details
- **Blocks** — every bullet is addressable; a block can appear in many places via block references, reducing duplication. A block reference keeps one canonical copy and renders it wherever needed, which is the outliner answer to the copy-paste problem that file-based wikis solve with wikilinks.
- **Workflow** — journal-first capture with pages emerging from tags and links; graph view shows structure. Days are the primary entry point (everything starts in the journal), and pages are built by aggregating the blocks tagged or linked with their names — a different rhythm from file-first wikis where pages are created before content.
- **Concrete example** — a daily journal entry lists a session's findings as blocks; each finding is tagged with the concept it concerns; the concept's page then shows every block ever tagged with it, in reverse chronological order, with backlinks to the journal entries where each claim appeared.
- **Failure modes** — block-reference sprawl, where the same block is embedded so many times that editing it surprises readers of every embedding; orphan blocks that are tagged but never assembled into a page; and the tension between journal-first capture (time-ordered) and concept-first retrieval (topic-ordered), which requires the tagging discipline to hold.
- **Tradeoffs** — block granularity is more precise than whole-file links but costs more effort per link and can fragment knowledge into micro-notes that are hard to survey; file-based wikis trade that precision for simpler provenance and versioning. Plain-text storage means git works on Logseq data, but block-level diffs are less readable than file diffs.
- **Agent relevance** — block-level linking is finer-grained than file-level wiki pages; mykb's atomic notes approximate block granularity at page scale, which is a deliberate simplification for autonomous curation.
- **RSIS3/mykb relevance** — the journal-first, page-emerges model is close to how mykb's session hooks work: pulses land in time-ordered logs, and concept pages aggregate them; this node documents the outliner variant of that loop for comparison.

## Related
- [[wiki/memory/obsidian|Obsidian]] — the file-based alternative to Logseq
- [[wiki/memory/org-mode|Org Mode]] — the outliner tradition Logseq extends
- [[wiki/memory/backlinks|Backlinks]] — block references create dense backlink graphs
- [[wiki/memory/wiki-science|Wiki Science]] — outliner wikis have their own structural dynamics
- [[wiki/memory/README|Memory Layer]] — the memory layer tools like Logseq serve
