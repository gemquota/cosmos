---
type: "concept"
title: "Scalar Quantization"
description: "Compressing vector dimensions to fewer bits per scalar to shrink index memory"
tags: ["quantization", "vector-search", "compression"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Scalar Quantization

## Summary
Compressing vector dimensions to fewer bits per scalar to shrink index memory

## Details
- Floats are mapped to INT8 or lower with per-vector or global ranges.
- Roughly 4x memory savings with modest recall loss.
- Simple to implement and fast to compute distances on.
- Often combined with graph indexes like HNSW.

## Related
- [[wiki/data-storage/product-quantization|Product Quantization]] — codebook-based alternative
- [[wiki/ai-ml/binary-quantization|Binary Quantization]] — extreme 1-bit variant
- [[wiki/ai-ml/hnsw-index|HNSW Index]] — index it compresses
- [[wiki/ai-ml/vector-database-sharding|Vector Database Sharding]] — memory pressure driver
- [[wiki/ai-ml/model-quantization|Model Quantization]] — same idea for model weights
