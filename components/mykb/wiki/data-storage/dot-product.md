---
type: "concept"
title: "Dot Product"
description: "Scalar sum of element-wise vector products, the raw score behind cosine similarity"
tags: ["dot-product", "similarity", "metrics", "embeddings"]
timestamp: "2026-07-31T00:00:00Z"
status: "stub"
---

# Dot Product

## Summary
The dot product `a·b = sum(a_i * b_i)` is the simplest vector similarity: high when vectors are large and aligned. It is used directly for retrieval when vectors are normalized or when magnitude carries meaning.

## Details
- **Relation to cosine** — cosine is the dot product of unit-normalized vectors; many systems normalize embeddings once and then use the dot product.
- **When to use** — fast inner-product search, recommendation-style scoring, and models trained with dot-product objectives.
- **Caveat** — unnormalized dot products reward long vectors, which can bias results.

## Related
- [[wiki/data-storage/cosine-similarity|Cosine Similarity]] — dot product after normalization
- [[wiki/data-storage/euclidean-distance|Euclidean Distance]] — the geometric distance alternative
- [[wiki/data-storage/embeddings|Embeddings]] — the vectors being multiplied
- [[wiki/data-storage/vector-databases|Vector Databases]] — metric choice happens at index creation
- [[wiki/data-storage/index|Data Storage]] — similarity metrics
