---
type: "concept"
title: "Dot Product Similarity"
description: "Score between vectors computed as the sum of elementwise products"
tags: ["similarity", "metrics", "embeddings"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Dot Product Similarity

## Summary
Score between vectors computed as the sum of elementwise products

## Details
- Fast and simple; equals cosine similarity for normalized vectors.
- Preferred by many ANN libraries for throughput.
- Sensitive to vector magnitude, so normalization decisions matter.
- A core option in metric-space-cosine design.

## Related
- [[wiki/data-storage/cosine-similarity|Cosine Similarity]] — equivalent under normalization
- [[wiki/ai-ml/euclidean-distance-manhattan|Euclidean and Manhattan Distance]] — distance metrics
- [[wiki/ai-ml/embeddings-and-vector-search|Embeddings and Vector Search]] — scoring used in search
- [[wiki/ai-ml/scalar-quantization|Scalar Quantization]] — approximation preserves ranking
- [[wiki/ai-ml/metric-space-cosine|Cosine Similarity]] — metric family
