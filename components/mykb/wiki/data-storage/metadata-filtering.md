---
type: "concept"
title: "Metadata Filtering"
description: "Using structured attributes on stored items to narrow retrieval before or after similarity search"
tags: ["metadata", "filtering", "retrieval", "vector-search", "curation"]
timestamp: "2026-07-31T00:00:00Z"
status: "growing"
source: ["https://qdrant.tech/documentation/concepts/filtering/"]
---

# Metadata Filtering

## Summary
Metadata filtering restricts vector or lexical search to items satisfying structured conditions — tags, timestamps, status, or source. It prevents irrelevant-but-similar results from dominating and is essential for curated knowledge bases. mykb's YAML frontmatter is exactly the metadata layer such filtering consumes.

## Details
- **Pre-filter vs post-filter** — pre-filter restricts the candidate set before ANN search (accurate, but can miss close neighbours outside the filter); post-filter removes non-matching results after search (fast, but recall drops when filters are selective).
- **Common fields** — tags, type, date ranges, status, source path, domain; combined with boolean operators.
- **Worked example** — a mykb query scoped to `tags: [memory]` and `timestamp > 2026-01-01` never retrieves a 2025 note on frontend CSS even if its embedding is close.
- **Implementation** — vector databases (Qdrant, Weaviate, Pinecone, Milvus) index payload fields; FTS engines filter on indexed columns.
- **Trade-off** — filter selectivity vs index size; selective filters can make ANN search degenerate, so some systems fold filter conditions into the query vector.

## Related
- [[wiki/data-storage/vector-databases|Vector Databases]] — payload filtering is a core feature
- [[wiki/data-storage/yaml-frontmatter|YAML Frontmatter]] — the metadata source in markdown wikis
- [[wiki/data-storage/open-knowledge-format|Open Knowledge Format]] — standardizes metadata fields for filtering
- [[wiki/data-storage/hybrid-search|Hybrid Search]] — filters apply to both lexical and vector halves
- [[wiki/memory/provenance|Provenance]] — a metadata dimension worth filtering on
- [[wiki/data-storage/index|Data Storage]] — directory home for storage and search tech
- [[wiki/questions/index|Open Questions]] — filtering questions worth resolving
