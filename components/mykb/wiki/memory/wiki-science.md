---
type: "concept"
title: "Wiki Science"
description: "Study of how wikis and collaborative knowledge bases grow, stay coherent, and resist degradation"
tags: ["wiki", "knowledge-base", "collaboration", "curation", "hypertext"]
timestamp: "2026-07-31T00:00:00Z"
status: "growing"
source: ["https://en.wikipedia.org/wiki/Wiki"]
---

# Wiki Science

## Summary
Wiki science examines why some wikis thrive — high link density, stable structure, low duplication — while others decay into chaos. It studies editing norms, graph structure, and the social mechanics that keep knowledge bases coherent. mykb is a single-agent wiki, so the relevant lessons are structural: atomic pages, backlinks, and clear namespaces.

## Details
- **Structural findings** — coherent wikis exhibit power-law link distributions, short paths between pages, and page titles that carry meaning.
- **Governance** — clear rules (naming conventions, page ownership, review processes) prevent forking and duplicated content.
- **Worked example** — mykb's `wiki/concepts/`, `wiki/syntheses/`, and `wiki/sources/` namespaces mirror wiki conventions: claims live in concepts, evidence in sources, conclusions in syntheses.
- **Backlinks** — wiki software surfaces inbound links, turning a file system into a navigable graph and exposing orphans for curation.
- **Relevance to agents** — an LLM-written wiki needs the same hygiene: unique titles, typed links, and a review pass, or it silently degrades.

## Related
- [[wiki/memory/backlinks|Backlinks]] — the graph signal that keeps wikis navigable
- [[wiki/memory/graph-notes|Graph Notes]] — visualizing the wiki as a network
- [[wiki/memory/digital-garden|Digital Garden]] — personal wiki with public, evolving notes
- [[wiki/memory/knowledge-curation|Knowledge Curation]] — the maintenance practice wiki science studies
- [[wiki/syntheses/knowledge-synthesis|Knowledge Synthesis]] — what mature wikis enable
- [[wiki/syntheses/README|Syntheses]] — mykb's namespace for distilled conclusions
- [[wiki/concepts/triad-architecture|Triad Architecture]] — mykb is the memory layer of the triad
