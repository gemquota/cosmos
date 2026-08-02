---
type: "concept"
title: "Euclidean and Manhattan Distance"
description: "Classic L2 and L1 distance metrics used for similarity search in some vector stores"
tags: ["similarity", "metrics", "vector-search"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Euclidean and Manhattan Distance

## Summary
Classic L2 and L1 distance metrics used for similarity search in some vector stores

## Details
- Euclidean (L2) measures straight-line distance; Manhattan (L1) sums absolute differences.
- Better suited to raw feature vectors than normalized embeddings.
- Index type and metric must match or results degrade.
- Choosing the right metric is part of index design.

## Related
- [[wiki/data-storage/cosine-similarity|Cosine Similarity]] — angular alternative
- [[wiki/ai-ml/dot-product-similarity|Dot-Product Similarity]] — un-normalized preference
- [[wiki/ai-ml/metric-space-cosine|Cosine Similarity]] — metric family
- [[wiki/ai-ml/hnsw-index|HNSW Index]] — metric-aware graph construction
- [[wiki/ai-ml/embeddings-alignment|Embeddings Alignment]] — metric choice in training
