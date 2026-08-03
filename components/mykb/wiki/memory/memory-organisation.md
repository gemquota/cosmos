---
type: "concept"
title: "Memory Organisation"
description: "Structures and conventions that arrange memories so they can be found and reused"
tags: ["memory", "organisation", "indexing", "structure"]
timestamp: "2026-07-31T00:00:00Z"
status: "growing"
---

# Memory Organisation

## Summary
Memory organisation is how a knowledge base arranges its contents — namespaces, types, indexes, links, and retrieval aids — so items are findable when needed. It is the bridge between storing something and being able to use it: a fact that cannot be found is indistinguishable from a fact that was never stored.

## Details
- **Layers** — physical (directories/files), logical (types, taxonomies), and associative (links, co-occurrence). A well-organized memory works at all three levels at once: the file lives in a predictable place, its frontmatter declares what kind of thing it is, and its links embed it in a web of related items.
- **Patterns** — typed namespaces, stable titles, frontmatter conventions, and index pages that enumerate the collection. Stability is the key rule: renaming a namespace or title without updating links is how a knowledge base accumulates rot, so organization changes should be treated as migrations with link updates.
- **Concrete example** — mykb organizes memory by `type` (concept, synthesis, pulse, decision) plus domains; the temporal engine adds a time axis for retrieval. A planner looking for past decisions queries the decision type; a researcher looks across a domain; a temporal query asks what changed in the last month — each organization layer serves a different retrieval pattern.
- **Failure modes** — over-nesting, where every topic gets a subfolder and the physical layout mirrors a taxonomy that does not match how items are actually retrieved; duplicate homes, where a page could belong to two namespaces and ends up in neither; and stale indexes that no longer enumerate the collection, making the index actively misleading.
- **Tradeoffs** — tight organization makes navigation predictable but rigid, and every new item must be classified; loose organization is cheap at capture but pushes the classification cost into every retrieval. The balance most wikis strike is a small set of stable types plus free linking, with namespaces kept shallow.
- **Agent relevance** — autonomous retrieval depends on organization being machine-readable: frontmatter types, consistent titles, and a maintained index are what let an agent query the memory layer instead of grepping it.
- **RSIS3/mykb relevance** — organisation is a PKM core step; the L3 consolidation practice writes new pages into the existing scheme (types, namespaces, links) rather than inventing new structure, which is what keeps the memory layer coherent across sessions.

## Related
- [[wiki/memory/memory-consolidation|Memory Consolidation]] — consolidation integrates items into the organization
- [[wiki/memory/information-architecture|Information Architecture]] — the design discipline for organization
- [[wiki/memory/personal-knowledge-management|Personal Knowledge Management]] — organization is a PKM core step
- [[wiki/memory/ontology-design|Ontology Design]] — formal schemas for organizing knowledge
- [[wiki/memory/README|Memory Layer]] — the layer whose organization this describes
