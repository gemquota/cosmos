---
type: "concept"
title: "IVF Index"
description: "Inverted File index that clusters vectors and searches only nearby clusters at query time"
tags: ["ann", "vector-search", "index"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# IVF Index

## Summary
Inverted File index that clusters vectors and searches only nearby clusters at query time

## Details
- Vectors are grouped by k-means centroids; queries probe the nearest clusters.
- Fast and memory-light, with recall controlled by nprobe.
- IVF-PQ combines clustering with product quantization for scale.
- A classic baseline for billion-scale approximate search.

## Related
- [[wiki/ai-ml/hnsw-index|HNSW Index]] — graph alternative
- [[wiki/data-storage/product-quantization|Product Quantization]] — compression used with IVF
- [[wiki/ai-ml/vector-database-sharding|Vector Database Sharding]] — scaling strategy
- [[wiki/ai-ml/index-rebuild-strategies|Index Rebuild Strategies]] — centroid retraining
- [[wiki/ai-ml/scalar-quantization|Scalar Quantization]] — alternative compression
