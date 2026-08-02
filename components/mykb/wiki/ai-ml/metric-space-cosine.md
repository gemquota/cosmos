---
type: "concept"
title: "Cosine Similarity Metric"
description: "Angular similarity between vectors used as the standard embedding search metric"
tags: ["similarity", "metrics", "embeddings"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Cosine Similarity Metric

## Summary
Angular similarity between vectors used as the standard embedding search metric

## Details
- Cosine similarity measures the angle between vectors, ignoring magnitude.
- Invariant to embedding scale, which suits normalized LLM embeddings.
- Often equivalent to dot product after L2 normalization.
- The default metric for most embedding models and indexes.

## Related
- [[wiki/ai-ml/dot-product-similarity|Dot-Product Similarity]] — equivalent under normalization
- [[wiki/ai-ml/euclidean-distance-manhattan|Euclidean and Manhattan Distance]] — distance-based alternatives
- [[wiki/ai-ml/embeddings-and-vector-search|Embeddings and Vector Search]] — search metric of choice
- [[wiki/ai-ml/embeddings-alignment|Embeddings Alignment]] — metric-sensitive training
- [[wiki/ai-ml/hnsw-index|HNSW Index]] — indexes built for this metric
