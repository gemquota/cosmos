---
type: "concept"
title: "Backlinks"
description: "Inbound references to a page that reveal how other notes point to it"
tags: ["backlinks", "links", "wiki", "navigation"]
timestamp: "2026-07-31T00:00:00Z"
status: "growing"
---

# Backlinks

## Summary
Backlinks are the set of pages that link to a given page. They turn a flat pile of notes into a navigable network and surface unexpected connections, which is why Obsidian and Logseq make them a core view — and why a wiki without a backlink view feels dead even when it is full of links.

## Details
- **Mechanics** — the wiki index inverts the link table: for every target, list all sources. In a file-based wiki this is a scan (or a maintained index) that maps each inbound `[[wikilink]]` to its origin page; the result is per-page "linked mentions" and "unlinked mentions" (pages that mention the title without a link).
- **Value** — discover context (who discusses this concept?), find orphans (zero backlinks = unintegrated), and grow links during review. Backlinks also power navigation upward: from a detail page you can walk to every broader discussion that cites it.
- **Concrete example** — a concept page "Polysemanticity" gains new meaning when its backlink list shows it is cited by circuit-analysis, superposition-research, and dictionary-learning pages; the reviewer sees at once that the concept bridges three clusters and checks whether each citation is accurate.
- **Failure modes** — orphan pages that nothing links to (they never get reviewed); over-citation where a term is linked from every sentence, diluting the signal; stale links that still resolve but point at a renamed concept, silently misdirecting readers; and unlinked mentions that never become links, so the graph undercounts real connections.
- **Tradeoffs** — automatic backlinks are cheap for a static wiki but show every mention, including trivial ones; curated "see also" lists are higher signal but rot without maintenance. The two complement each other: automation for completeness, curation for salience.
- **Agent relevance** — mykb's backlink engine already traverses incoming links; RSIS3 uses them to find related memories during planning. When the system plans a task, the backlink set of a chosen concept is a ready-made list of adjacent knowledge to retrieve.
- **RSIS3/mykb relevance** — backlinks are the structural signal wikis depend on: they let the retrieval layer move from a concept to its neighborhood without knowing the neighborhood in advance.

## Related
- [[wiki/memory/graph-notes|Graph Notes]] — the network view built from backlinks
- [[wiki/memory/obsidian|Obsidian]] — a tool whose backlink panel drives navigation
- [[wiki/memory/wiki-science|Wiki Science]] — backlinks are the structural signal wikis depend on
- [[wiki/memory/zettelkasten|Zettelkasten]] — links are the method's connective tissue
- [[wiki/syntheses/knowledge-system|Knowledge System]] — the loop that grows and uses backlinks
