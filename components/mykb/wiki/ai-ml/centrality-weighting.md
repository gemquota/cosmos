---
type: "concept"
title: "Centrality Weighting"
description: "Giving graph-central articles more weight"
tags: ["weighting", "centrality", "metrics", "graph"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Centrality Weighting

## Summary
Centrality weighting gives articles that sit centrally in the link graph more influence, using metrics like degree, betweenness, or PageRank-style scores.

## Details
- Central articles carry disproportionate navigation value, so their quality and freshness matter more than peripheral ones.
- Centrality is computed from the graph and changes as the graph changes, so the weight must be recomputed, not cached forever.
- For mykb, centrality weighting feeds impact-labels and the maintenance priority of keystone articles.

## Related
- [[wiki/concepts/weight-articles|Weighting Articles]]
- [[wiki/ai-ml/centrality-weighting|Centrality Weighting]]
- [[wiki/concepts/keystone-articles|Keystone Articles]]
- [[wiki/concepts/incoming-link-counts|Incoming Link Counts]]
- [[wiki/concepts/impact-labels|Impact Labels]]
- [[wiki/ai-ml/graph-density-metrics|Graph Density Metrics]]
