---
type: "concept"
title: "Locality-Sensitive Hashing"
description: "Hashing scheme where similar items collide with high probability"
tags: ["lsh", "hashing", "similarity", "ann"]
timestamp: "2026-07-31T00:00:00Z"
status: "stub"
---

# Locality-Sensitive Hashing

## Summary
Locality-sensitive hashing (LSH) maps items so that near neighbours land in the same hash bucket more often than distant ones, enabling approximate similarity search without vector indexes. It was the pre-embedding workhorse for near-duplicate detection.

## Details
- **Mechanism** — several hash functions per family (random projections for cosine, MinHash for Jaccard); items sharing enough hashes are candidates.
- **Use** — deduplication, entity resolution, and early ANN systems; embeddings have largely replaced it for dense vectors.
- **Trade-off** — probabilistic guarantees and tuning (bands, rows) vs simplicity and interpretability.

## Related
- [[wiki/data-storage/minhash|MinHash]] — the LSH family for set similarity
- [[wiki/data-storage/simhash|SimHash]] — the LSH family for text fingerprints
- [[wiki/data-storage/cosine-similarity|Cosine Similarity]] — the metric random-projection LSH targets
- [[wiki/data-storage/embeddings|Embeddings]] — the modern alternative for dense search
- [[wiki/data-storage/index|Data Storage]] — similarity techniques
