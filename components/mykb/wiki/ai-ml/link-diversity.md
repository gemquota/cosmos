---
type: "concept"
title: "Link Diversity"
description: "The variety of distinct neighbors a page or the whole wiki links to"
tags: ["links", "diversity", "graph", "quality"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Link Diversity

## Summary
Link diversity measures how many distinct articles a page reaches versus repeated links to the same few hubs; high repetition signals a hub-and-spoke page rather than genuine integration.

## Details
- Diverse links spread navigation value and make the graph robust — no single hub failure isolates a topic cluster.
- A page that only links to its own parent and children is shallow; a page that links to related-but-distinct concepts demonstrates real synthesis.
- For mykb, link diversity is part of the link-score: the wiki linter can report pages whose outbound set is dominated by one or two targets.

## Related
- [[wiki/concepts/outbound-link-counts|Outbound Link Counts]]
- [[wiki/ai-ml/link-score|Link Score]]
- [[wiki/ai-ml/graph-density-metrics|Graph Density Metrics]]
- [[wiki/concepts/connector-articles|Connector Articles]]
- [[wiki/memory/graph-notes|Graph Notes]]
- [[wiki/concepts/link-placement|Link Placement]]
