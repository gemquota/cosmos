---
type: "concept"
title: "Link Diversity"
description: "The variety of distinct neighbors a page or the whole wiki links to"
tags: ["links", "diversity", "graph", "quality"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Link Diversity

## Summary
Link diversity measures how many distinct articles a page reaches versus repeated links to the same few hubs; high repetition signals a hub-and-spoke page rather than genuine integration. It is the complement to density: density asks how many links exist, diversity asks how many different neighbours they reach.

## Details
The metric is usually computed as distinct outbound targets divided by total outbound links, either per page or across the whole wiki. A page with twenty links to two recurring hubs has low diversity even though its raw outbound count looks healthy; a page with ten links to ten different articles has high diversity. The distinction matters because the two measures answer different questions about navigation and synthesis.

Diverse links spread navigation value and make the graph robust: no single hub failure isolates a topic cluster, and readers are offered multiple paths into a subject. A page that only links to its own parent and children is shallow — it restates the hierarchy without adding connections — while a page that links to related-but-distinct concepts demonstrates real synthesis, which is exactly what an OKF-style wiki wants from connector articles.

The failure modes are the mirror image. Hub-and-spoke pages concentrate outbound links on a handful of well-known targets, often because the author linked from memory rather than surveying the wiki. The result is a graph that looks connected at the top but has little cross-linking between topic clusters. Conversely, forcing diversity mechanically — replacing meaningful links with arbitrary ones — destroys precision, so diversity is a diagnostic signal, not a target to optimize directly.

For mykb, link diversity is part of the link-score: the wiki linter can report pages whose outbound set is dominated by one or two targets, and RSIS3 consolidation passes should treat a newly written synthesis note with low diversity as a sign that it was written in isolation rather than integrated with the existing graph.

## Related
- [[wiki/concepts/outbound-link-counts|Outbound Link Counts]]
- [[wiki/ai-ml/link-score|Link Score]]
- [[wiki/ai-ml/graph-density-metrics|Graph Density Metrics]]
- [[wiki/concepts/connector-articles|Connector Articles]]
- [[wiki/memory/graph-notes|Graph Notes]]
- [[wiki/concepts/link-placement|Link Placement]]
