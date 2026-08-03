---
type: "concept"
title: "Bidirectional Link Ratio"
description: "Fraction of links that are reciprocated between pages"
tags: ["wiki", "graph", "metrics", "link-structure"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
---

# Bidirectional Link Ratio

## Summary
The bidirectional link ratio measures how many of a wiki's links are reciprocated — if page A links to B, does B link back to A? It is a structural health metric for knowledge graphs: high reciprocity signals a well-connected cluster of mutually relevant notes, while low reciprocity can signal dead ends, hub pages, or one-way dependencies.

## Details
- The metric is computed as the fraction of directed edges that have a reverse edge, either globally (all links in the wiki) or per page (of the pages this article links to, how many link back). A page that links out without receiving backlinks is a "leaf" in the graph's conversational sense: it points at its neighbors but nothing points back, which usually means the neighbors are missing context they should reference.
- What a low ratio means depends on the page type. Hub or index pages naturally have low reciprocity because they link to many topics that have no reason to link back. Synthesis pages often have low reciprocity too — they consolidate sources rather than being referenced by each source. The metric is therefore a diagnostic, not a target: flag pages with unexpectedly low ratios relative to their type, and investigate rather than mechanically adding backlinks.
- Conversely, a very high ratio across the whole wiki can indicate over-clustering: pages that only ever cite their immediate neighbors, forming a clique that never connects to the rest of the graph. Healthy knowledge graphs show a mix — reciprocal cluster links plus directed bridge links that carry ideas between clusters.
- The related outbound-link-counts and orphan-page-report metrics complement it: outbound counts reveal pages that never link anywhere (graph sinks), orphan reports reveal pages nobody links to, and the bidirectional ratio reveals the quality of the links that do exist.
- RSIS3 relevance: link reciprocity is a cheap proxy for knowledge-flow health. When RSIS3 retrieves evidence for an improvement cycle, the retrieval path traverses these links, and a chain of unreciprocated links can strand the search in a dead end. Monitoring the ratio across clusters tells the system where the graph needs cross-linking before retrieval fails.

## Related
- [[wiki/concepts/outbound-link-counts|Outbound Link Counts]] — complement metric
- [[wiki/concepts/orphan-page-report|Orphan Page Report]] — pages nobody links to
- [[wiki/concepts/wiki-health-dashboard|Wiki Health Dashboard]] — where these metrics surface
- [[wiki/concepts/growth-ratio|Growth Ratio]] — another graph-health signal
- [[wiki/concepts/reciprocal-links|Reciprocal Links]]
- [[wiki/concepts/one-way-links|One Way Links]]
- [[wiki/concepts/related-link-reciprocity|Related Link Reciprocity]]
- [[wiki/concepts/incoming-link-counts|Incoming Link Counts]]
- [[wiki/ai-ml/link-score|Link Score]]
- [[wiki/syntheses/knowledge-graph-maintenance|Knowledge Graph Maintenance]]
