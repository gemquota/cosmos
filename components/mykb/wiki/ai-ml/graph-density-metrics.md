---
type: "concept"
title: "Graph Density Metrics"
description: "Measures of how connected a knowledge graph is relative to its size"
tags: ["graph", "density", "metrics", "links"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Graph Density Metrics

## Summary
Graph density compares actual links to the maximum possible: for n articles the ceiling is n(n-1), so density is links divided by that ceiling, with self-links and duplicates excluded.

## Details
- Sparse graphs hide knowledge: two related articles that never link are a discovery failure even if both are individually excellent.
- Density should be read with link diversity and clustering: a dense corner of the graph can coexist with an orphaned region.
- For mykb, density metrics are computed from the wikilink set and reported alongside stub ratio, because a graph that is dense but stub-heavy has connectedness without depth.

## Related
- [[wiki/ai-ml/link-diversity|Link Diversity]]
- [[wiki/concepts/incoming-link-counts|Incoming Link Counts]]
- [[wiki/concepts/outbound-link-counts|Outbound Link Counts]]
- [[wiki/concepts/bidirectional-link-ratio|Bidirectional Link Ratio]]
- [[wiki/data-storage/knowledge-graph|Knowledge Graph]]
- [[wiki/concepts/orphan-page-report|Orphan Page Report]]
