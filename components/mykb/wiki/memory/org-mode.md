---
type: "concept"
title: "Org Mode"
description: "Emacs plain-text outlining and note system with agenda, links, and literate programming"
tags: ["org-mode", "emacs", "outliner", "plain-text"]
timestamp: "2026-07-31T00:00:00Z"
status: "growing"
---

# Org Mode

## Summary
Org Mode is Emacs' plain-text system for notes, outlines, todos, and agendas, where structure comes from `*` headings in ordinary files. Its longevity and programmability make it the benchmark for text-based personal knowledge tools: an org file from 2005 still opens, edits, and exports today.

## Details
- **Features** — hierarchical outlines, TODO states, timestamps and agendas, inline links, and export to many formats. The agenda turns scattered timestamps and TODOs into a synthesized daily view, and property drawers add structured metadata without leaving plain text.
- **Plain text** — everything is editable and greppable; org files survive decades and migrate between tools. Because the format is text with simple heading markers, it has no vendor lock-in and no database to corrupt — a property that matters for knowledge meant to outlive its authoring tool.
- **Concrete example** — a research notebook where each `*` heading is a topic, subheadings are claims, TODO states track reading and synthesis, and `[[file:...]]` links connect related files; a weekly agenda collects the timestamps; export produces HTML or PDF on demand.
- **Failure modes** — emacs-centric workflows that assume the user lives in Emacs, making the knowledge hard to share with others; org markup that drifts into complex forms (Babel blocks, drawers) that other tools cannot render; and agenda features that silently depend on timestamps being maintained.
- **Tradeoffs** — org's power and durability come with a steep learning curve and an editor-centric philosophy; for teams that do not use Emacs, the plain-text core is still valuable, but the advanced features (agenda, literate programming) are locked behind it.
- **Agent relevance** — org headings map naturally to wiki page structure; exporting org to markdown keeps the knowledge in mykb's format. An agent can treat an org outline as a structured source and convert it into atomic wiki pages, preserving the heading hierarchy as links.
- **RSIS3/mykb relevance** — org is the archetype of the plain-text, structured, long-lived knowledge format; the memory layer's markdown conventions inherit the same philosophy, and this node keeps the comparison retrievable when tooling decisions arise.

## Related
- [[wiki/memory/logseq|Logseq]] — an outliner inspired by org's structure
- [[wiki/data-storage/yaml-frontmatter|YAML Frontmatter]] — metadata conventions for plain-text notes
- [[wiki/memory/git-for-notes|Git for Notes]] — plain-text systems pair with git versioning
- [[wiki/memory/personal-knowledge-management|Personal Knowledge Management]] — org as a lifelong PKM substrate
- [[wiki/memory/README|Memory Layer]] — the memory layer org files can feed
- [[wiki/memory/knowledge-curation|Knowledge Curation]] — tending a lifetime of org notes
