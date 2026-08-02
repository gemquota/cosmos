---
type: "concept"
title: "Entity Resolution"
description: "Identifying records across sources that refer to the same real-world entity"
tags: ["entity-resolution", "data-quality", "matching", "knowledge-graph"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://en.wikipedia.org/wiki/Record_linkage", "https://en.wikipedia.org/wiki/Entity_resolution", "https://github.com/J535D165/recordlinkage"]
---

# Entity Resolution

## Summary
Entity resolution determines whether two records — a wiki page and a citation, a log line and a concept — denote the same real entity. It is the prerequisite for merging knowledge bases and building trustworthy graphs.

## Details
- **Signals** — names, aliases, context, dates, and embeddings; matching is fuzzy because spellings differ.
- **Pipeline** — blocking (candidate pairs) then scoring (rules or models) then merging with provenance.
- **Agent relevance** — when RSIS3 extracts entities from sessions, resolution against existing `wiki/entities/` pages decides whether to link or create.
- Entity resolution identifies records that refer to the same real-world entity across or within datasets, even when they are not identically keyed.
- It uses blocking (candidate grouping) to make comparison feasible, then similarity scoring and a decision rule to classify matches, non-matches, and uncertain pairs.
- The quality bar is precision-recall tradeoff: missing matches loses information, false matches corrupt the merged data.
- Entity resolution is the generalization of record linkage to arbitrary entity types and is central to graph construction and data cleaning.
- **Worked example / comparison** — Worked example — two wiki captures mention 'GRPC' and 'gRPC' plus the same documentation URL; entity resolution decides they are the same concept and merges their links.
- For mykb, entity resolution is documented as the merge engine that keeps the concept graph free of duplicate nodes.

## Related
- [[wiki/data-storage/record-linkage|Record Linkage]]
- [[wiki/data-storage/deduplication|Deduplication]]
- [[wiki/data-storage/knowledge-graph|Knowledge Graph]]
- [[wiki/memory/provenance|Provenance]]
- [[wiki/data-storage/index|Data Storage]]
- [[wiki/concepts/promotion-readiness|Promotion Readiness]]
- [[wiki/ai-ml/article-health-scores|Article Health Scores]]
- [[wiki/concepts/explainers|Explainers]]
