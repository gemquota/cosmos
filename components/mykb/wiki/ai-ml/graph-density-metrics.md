---
type: "concept"
title: "Graph Density Metrics"
description: "Measures of how connected a knowledge graph is relative to its size"
tags: ["graph", "density", "metrics", "links"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Graph Density Metrics

## Summary
Graph density compares actual links to the maximum possible: for n articles the ceiling is n(n-1), so density is links divided by that ceiling, with self-links and duplicates excluded. It is the single most direct numeric signal for whether a wiki's articles are actually connected to one another.

## Details
Computing density is straightforward once the link set is clean: count distinct directed edges between distinct pages and divide by n(n-1). The main pitfalls are definitional. Self-links must be excluded or they inflate the count; duplicate or bidirectional variants must be counted consistently; and stub or redirect pages should either be excluded or flagged, or they silently change both n and the edge count. Tools that compute density on the raw file set versus the resolved wikilink set can disagree, so the metric definition belongs in one canonical place.

The interpretation matters more than the number. Sparse graphs hide knowledge: two related articles that never link are a discovery failure even if both are individually excellent, because no traversal path leads a reader from one to the other. Low density is therefore a reliable early signal that articles were written in isolation rather than synthesized against their neighbours.

Density must be read together with link diversity and clustering. A graph can report respectable overall density while a dense corner of it coexists with an orphaned region, and that corner can be dominated by a few hub pages that accumulate links without the outlying pages ever connecting back. Reporting density alone hides both pathologies, which is why the metric belongs in a dashboard alongside stub ratio, orphan counts, and clustering measures rather than as a standalone KPI.

For mykb, density metrics are computed from the wikilink set and reported alongside stub ratio, because a graph that is dense but stub-heavy has connectedness without depth. The practical use inside RSIS3 is loop hygiene: when a consolidation pass links a new synthesis note into the graph, density changes are a cheap check that the note actually integrated rather than landing as an isolated file.

## Related
- [[wiki/ai-ml/link-diversity|Link Diversity]]
- [[wiki/concepts/incoming-link-counts|Incoming Link Counts]]
- [[wiki/concepts/outbound-link-counts|Outbound Link Counts]]
- [[wiki/concepts/bidirectional-link-ratio|Bidirectional Link Ratio]]
- [[wiki/data-storage/knowledge-graph|Knowledge Graph]]
- [[wiki/concepts/orphan-page-report|Orphan Page Report]]
