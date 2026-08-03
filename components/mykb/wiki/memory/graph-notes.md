---
type: "concept"
title: "Graph Notes"
description: "Practice of managing notes as a graph where links define structure instead of folders"
tags: ["graph", "notes", "pkm", "visualization"]
timestamp: "2026-07-31T00:00:00Z"
status: "growing"
---

# Graph Notes

## Summary
Graph notes treat a note collection as a network: pages are nodes, links are edges, and structure emerges from connectivity rather than folders. The graph view exposes clusters, bridges, and orphans that folders hide, turning the act of linking into the primary organizing activity instead of a secondary decoration.

## Details
- **Graph view** — nodes cluster by link density; communities of related ideas become visible at a glance. A well-linked wiki shows dense clusters for each topic area, with a few high-degree hubs (concepts like "spaced repetition" or "schema migrations") bridging clusters — and these hubs are exactly the notes worth writing well.
- **Benefits** — find concept bridges, spot isolated notes needing integration, and navigate by association. Orphans (nodes with no links) are a direct to-do list: each one is knowledge that exists but is not yet usable, because retrieval cannot reach it from any other note.
- **Limits** — dense graphs become hairballs; filters and local views are needed beyond a few hundred nodes. A global graph of a large wiki is a wall of spaghetti; the useful views are local neighborhoods (a node, its links, their links) and cluster summaries.
- **Concrete example** — a reviewer opens the graph, sees a cluster of networking notes with one isolated note "Traffic Shaping" attached to nothing, reads it, and adds links to QoS, traffic engineering, and DSCP — integrating the note and raising its retrieval odds from near zero.
- **Failure modes** — link rot (links that resolve but point at stale content); promiscuous linking where every note links to every related note, so the graph loses its signal and clusters collapse; and graph-watching as a substitute for actual curation, where notes are linked but never deepened.
- **Tradeoffs** — graph organization is flexible and scales with meaning, but it demands link hygiene and better search than folder hierarchies; folders are cheap and predictable for navigation, graphs are expensive but high-signal. Most wikis do both: folders for provenance and namespaces, links for structure.
- **Agent relevance** — mykb's NetworkX co-occurrence graph with community detection is graph notes at the level of an autonomous curator, automatically finding the bridges and orphans a human reviewer would hunt for.
- **RSIS3/mykb relevance** — the connect step grows the graph: every synthesis pass adds links, and graph statistics (orphan counts, cluster sizes) are standing health signals for the wiki.

## Related
- [[wiki/memory/backlinks|Backlinks]] — the edge data the graph view renders
- [[wiki/data-storage/knowledge-graph|Knowledge Graph]] — the general concept graph notes instantiate
- [[wiki/memory/obsidian|Obsidian]] — offers a built-in graph view
- [[wiki/memory/wiki-science|Wiki Science]] — how graph structure correlates with wiki health
- [[wiki/syntheses/knowledge-system|Knowledge System]] — connect step grows the graph
