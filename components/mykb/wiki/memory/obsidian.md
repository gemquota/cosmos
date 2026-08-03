---
type: "concept"
title: "Obsidian"
description: "Local-first markdown note app whose linking, backlinks, and graph views suit networked notes"
tags: ["obsidian", "tool", "markdown", "pkm"]
timestamp: "2026-07-31T00:00:00Z"
status: "growing"
---

# Obsidian

## Summary
Obsidian is a local-first markdown note-taking app built around `wikilinks`, a backlink panel, and a graph view. It popularized the linked-notes workflow that Zettelkasten methods need, with plain files that stay portable — the vault is just a folder of markdown, so no proprietary format stands between the user and their knowledge.

## Details
- **Core** — files are plain markdown on disk; links, backlinks, and graph views derive from the text itself. A `[[wikilink]]` is text in the file, so the graph is a computed view of the files, not a stored structure — which means any tool that reads markdown can participate in the same vault.
- **Ecosystem** — plugins add spaced repetition, databases, and publishing; vaults sync over any file-sync tool. The plugin model extends the core cheaply, but plugins add complexity and version-skew risk, and sync remains the user's problem — Obsidian is not a service with a built-in backup.
- **Concrete example** — a vault of wiki pages where a concept page links to its sources and siblings; the backlink panel shows every page mentioning the concept, the graph view shows the cluster it belongs to, and git (or any sync tool) versions the whole vault because everything is text.
- **Failure modes** — link rot when files are renamed without updating links; plugin dependence, where a workflow built on an unmaintained plugin breaks silently; vault sprawl as thousands of files accumulate without an index; and the false sense of durability when the vault exists on only one device.
- **Tradeoffs** — the plain-text, local-first design gives portability, versioning, and longevity at the cost of no built-in collaboration, no access control, and weaker mobile workflows than cloud services. It is the right trade for a knowledge base that must outlive any single tool.
- **Agent relevance** — mykb's wiki is Obsidian-compatible by design: RSIS3 writes plain markdown with wikilinks and frontmatter that Obsidian renders. This compatibility means humans and agents browse the same vault with the same tooling.
- **RSIS3/mykb relevance** — Obsidian is the reference tool for the wiki format this repo uses; the memory layer's file conventions (frontmatter, wikilinks, namespaces) are chosen to stay renderable in Obsidian and its successors.

## Related
- [[wiki/memory/backlinks|Backlinks]] — the core navigation feature of Obsidian
- [[wiki/memory/graph-notes|Graph Notes]] — the graph view Obsidian made famous
- [[wiki/data-storage/yaml-frontmatter|YAML Frontmatter]] — the metadata format Obsidian vaults use
- [[wiki/memory/zettelkasten|Zettelkasten]] — the method Obsidian is built around
- [[wiki/memory/README|Memory Layer]] — mykb's Obsidian-compatible memory layer
- [[wiki/index|Wiki Index]] — the hub of the Obsidian-style vault
