---
type: "concept"
title: "HNSW Index"
description: "Hierarchical Navigable Small World graph index for approximate nearest neighbor search"
tags: ["ann", "vector-search", "index"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# HNSW Index

## Summary
Hierarchical Navigable Small World graph index for approximate nearest neighbor search

## Details
- Builds multi-layer proximity graphs where search descends from coarse to fine layers.
- Offers excellent recall-latency trade-offs and is the default in many engines.
- Memory-hungry; pairs with product quantization to shrink.
- Parameters (M, efConstruction) tune recall versus build cost.

## Related
- [[wiki/ai-ml/ivf-index|IVF Index]] — clustering alternative
- [[wiki/data-storage/product-quantization|Product Quantization]] — compression partner
- [[wiki/ai-ml/vector-database-sharding|Vector Database Sharding]] — scaling HNSW
- [[wiki/ai-ml/index-rebuild-strategies|Index Rebuild Strategies]] — graph maintenance
- [[wiki/ai-ml/metric-space-cosine|Cosine Similarity]] — similarity metric choice
