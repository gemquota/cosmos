---
type: "concept"
title: "Centrality Weighting"
description: "Giving graph-central articles more weight"
tags: ["weighting", "centrality", "metrics", "graph"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Centrality Weighting

## Summary
Centrality weighting gives articles that sit centrally in the link graph more influence, using metrics like degree, betweenness, or PageRank-style scores. Central articles carry disproportionate navigation value, so their quality and freshness matter more than peripheral ones.

## Details
- **Why it matters** — a broken or stale keystone article distorts many downstream readers; weighting concentrates maintenance attention where the graph already concentrates navigation.
- **Metrics** — degree counts direct links; betweenness counts how often an article lies on shortest paths; PageRank-style scores propagate importance from neighbors; each captures a different notion of centrality.
- **Dynamic recomputation** — centrality changes as the graph changes, so weights must be recomputed on graph updates rather than cached forever; a stale weight can send effort to a page that is no longer central.
- **Combining with weakness scores** — centrality says where damage is worst; the article score says where quality is lowest; maintenance priority is the join of the two.
- **For mykb** — centrality weighting feeds impact labels and the maintenance priority of keystone articles, and it keeps the graph-health dashboard pointed at the highest-leverage nodes.
- **Caveats** — raw degree is easy to game with redundant links, hub pages are not always the most useful pages, and centrality says nothing about content correctness by itself.

- **Worked example** — two articles score equally on quality; the one linked from twenty other pages gets the rewrite first because fixing it improves navigation for the most readers; the peripheral article waits for the next scheduled pass.
- **Weight application** — the weight can scale maintenance priority, search ranking boosts, or dashboard impact labels; applying it in several places at once can double-count, so the system should declare one canonical use and reuse it.
- **Measuring correctness** — validate a centrality choice by checking that the top-weighted pages match a human-curated list of important articles; disagreement reveals a graph artifact such as a link-farm hub.
## Related
- [[wiki/concepts/keystone-articles|Keystone Articles]] — the high-centrality set
- [[wiki/ai-ml/article-score|Article Score]] — quality-side counterpart
- [[wiki/concepts/incoming-link-counts|Incoming Link Counts]] — degree-style signal
- [[wiki/concepts/impact-labels|Impact Labels]] — centrality-derived labels
- [[wiki/ai-ml/graph-density-metrics|Graph Density Metrics]] — graph-wide measures
- [[wiki/data-storage/knowledge-graph|Knowledge Graph]] — the graph being measured
