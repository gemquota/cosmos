---
type: "concept"
title: "Locality-Sensitive Hashing"
description: "Hashing scheme where similar items collide with high probability"
tags: ["lsh", "hashing", "similarity", "ann"]
timestamp: "2026-07-31T00:00:00Z"
status: "growing"
---

# Locality-Sensitive Hashing

## Summary
Locality-sensitive hashing (LSH) maps items so that near neighbours land in the same hash bucket more often than distant ones, enabling approximate similarity search without vector indexes. It was the pre-embedding workhorse for near-duplicate detection and still serves set-similarity workloads.

## Details
- Mechanism: a family of hash functions preserves locality — random projections for cosine similarity, MinHash for Jaccard; several hashes (bands of rows) are combined so only items sharing enough hashes become candidates; candidate pairs are then verified exactly.
- Concrete example: near-duplicate detection over millions of documents: shingle each document, compute MinHash signatures, band them into LSH buckets, and only pairs landing in the same bucket get exact Jaccard checks — turning an impossible pairwise scan into a tiny candidate set.
- Failure modes: band/row tuning off, so recall collapses (too few bands) or candidate sets explode (too many); hash functions from the wrong family for the metric; signature sizes too small, increasing false positives; updates requiring full re-hashing; relying on LSH for dense-vector search where embedding indexes dominate.
- Tradeoffs: LSH gives probabilistic, tunable, interpretable approximate search with no training step, at the cost of tuning and weaker guarantees than learned indexes; the alternative, ANN vector indexes (HNSW, IVF), is better for dense embeddings; the mature pattern is LSH for set and text fingerprints, ANN indexes for embeddings.
- Operational notes: tune bands and rows against a labeled recall test, and keep exact verification as the final step.
- RSIS3 relevance: LSH and MinHash give mykb cheap near-duplicate detection across capture sources — the same dedup guarantee RSIS3 wants before curating.

## Practice
- Keep the exact verification step mandatory: LSH only proposes candidates, it never decides similarity on its own.
## Related
- [[wiki/data-storage/minhash|MinHash]] — the LSH family for set similarity
- [[wiki/data-storage/simhash|SimHash]] — the LSH family for text fingerprints
- [[wiki/data-storage/cosine-similarity|Cosine Similarity]] — the metric random-projection LSH targets
- [[wiki/data-storage/embeddings|Embeddings]] — the modern alternative for dense search
- [[wiki/data-storage/index|Data Storage]] — similarity techniques
