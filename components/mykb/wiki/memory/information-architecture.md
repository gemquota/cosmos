---
type: "concept"
title: "Information Architecture"
description: "Design of how information is organized, labeled, and navigated in a system"
tags: ["ia", "organization", "navigation", "design"]
timestamp: "2026-07-31T00:00:00Z"
status: "growing"
---

# Information Architecture

## Summary
Information architecture (IA) is the discipline of structuring, labeling, and interlinking content so users (or agents) can find what they need. It covers navigation schemes, naming conventions, and the mental model a system presents — and in a wiki, IA is what separates a searchable knowledge base from a pile of markdown files.

## Details
- **Components** — organization systems (taxonomies, faceted classification), labeling systems (titles, tags, frontmatter fields), navigation (indexes, links, backlinks), and search. All four must agree: a page labeled one way in navigation and another way in search is a page users cannot find.
- **Principles** — predictable names, minimal depth, multiple paths to the same item, and clear distinction between browse and search. A concept should be reachable both by browsing its cluster and by searching its exact title; if either path fails, the IA has a gap.
- **Concrete example** — a wiki with namespaces `concepts/`, `infrastructure/`, and `syntheses/` tells every reader what kind of page they are on and what kind of links it should carry; a synthesis linking to concepts and an infrastructure page linking to other infrastructure pages gives both browse paths and search paths their structure.
- **Failure modes** — namespace sprawl where every new topic gets its own folder, so related pages are scattered by naming accident; ambiguous labels ("Index", "Main", "Overview" pointing at different places); duplicate pages for one concept under two names, splitting its backlinks; and deep hierarchies that bury pages five clicks from the index.
- **Tradeoffs** — folders give predictable physical organization but freeze a single classification; typed links and tags give flexible multi-classification at the cost of discipline. The common resolution is folders for provenance and namespaces plus links and tags for meaning, with the frontmatter type as the spine of both.
- **Agent relevance** — mykb's namespaces, frontmatter typing, and index pages are IA decisions; good IA is what makes autonomous retrieval reliable, because an agent cannot navigate a wiki that humans find confusing.
- **RSIS3/mykb relevance** — IA decisions are structural invariants: renaming a namespace or retyping pages ripples through every link and index, so changes should be treated as schema migrations with a plan, not ad-hoc edits.

## Related
- [[wiki/memory/ontology-design|Ontology Design]] — semantic schema behind good IA
- [[wiki/memory/taxonomy|Taxonomy]] — hierarchical organization systems
- [[wiki/memory/personal-knowledge-management|Personal Knowledge Management]] — IA applied to personal knowledge
- [[wiki/memory/para-method|PARA Method]] — an actionability-based IA
- [[wiki/data-storage/index|Data Storage]] — an example namespace in mykb
- [[wiki/index|Wiki Index]] — the top-level navigation hub
