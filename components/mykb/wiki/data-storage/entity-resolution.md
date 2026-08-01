---
type: "concept"
title: "Entity Resolution"
description: "Identifying records across sources that refer to the same real-world entity"
tags: ["entity-resolution", "data-quality", "matching", "knowledge-graph"]
timestamp: "2026-07-31T00:00:00Z"
status: "stub"
---

# Entity Resolution

## Summary
Entity resolution determines whether two records — a wiki page and a citation, a log line and a concept — denote the same real entity. It is the prerequisite for merging knowledge bases and building trustworthy graphs.

## Details
- **Signals** — names, aliases, context, dates, and embeddings; matching is fuzzy because spellings differ.
- **Pipeline** — blocking (candidate pairs) then scoring (rules or models) then merging with provenance.
- **Agent relevance** — when RSIS3 extracts entities from sessions, resolution against existing `wiki/entities/` pages decides whether to link or create.

## Related
- [[wiki/data-storage/record-linkage|Record Linkage]] — the statistical cousin of entity resolution
- [[wiki/data-storage/deduplication|Deduplication]] — resolution then dedupes the merged records
- [[wiki/data-storage/knowledge-graph|Knowledge Graph]] — resolution keeps graph entities canonical
- [[wiki/memory/provenance|Provenance]] — merges must preserve where each record came from
- [[wiki/data-storage/index|Data Storage]] — the data-quality namespace
