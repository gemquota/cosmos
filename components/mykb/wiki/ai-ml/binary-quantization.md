---
type: "concept"
title: "Binary Quantization"
description: "Representing vectors as compact binary codes and computing similarity via Hamming distances"
tags: ["quantization", "vector-search", "compression"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Binary Quantization

## Summary
Representing vectors as compact binary codes and computing similarity via Hamming distances

## Details
- Each dimension reduces to a sign bit, giving 32x memory savings over FP32.
- Hamming similarity is extremely fast on modern CPUs.
- Recall drops substantially; best for large, high-dimensional collections.
- Often paired with rescoring on original vectors.

## Related
- [[wiki/ai-ml/scalar-quantization|Scalar Quantization]] — multi-bit sibling
- [[wiki/data-storage/product-quantization|Product Quantization]] — codebook alternative
- [[wiki/ai-ml/embeddings-and-vector-search|Embeddings and Vector Search]] — use case
- [[wiki/ai-ml/reranking-strategies|Reranking Strategies]] — rescoring after coarse search
- [[wiki/ai-ml/metric-space-cosine|Cosine Similarity]] — what binary codes approximate
