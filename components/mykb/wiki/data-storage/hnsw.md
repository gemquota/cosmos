---
type: "concept"
title: "HNSW"
description: "Hierarchical Navigable Small World graphs for approximate nearest-neighbour search"
tags: ["hnsw", "ann", "graph-index", "vector-search"]
timestamp: "2026-07-31T00:00:00Z"
status: "stub"
---

# HNSW

## Summary
HNSW builds a multi-layer graph where each layer is a navigable small-world network, enabling logarithmic-time approximate nearest-neighbour search. It is the default index in most modern vector databases for its speed-recall balance.

## Details
- **Construction** — insertion connects each point to a few neighbours per layer; upper layers are sparser and longer-range.
- **Parameters** — M (connections), efConstruction (build quality), efSearch (query effort); tuning trades recall for latency and memory.
- **Trade-off** — excellent search performance but higher memory than IVF or quantization; dynamic inserts are supported.

## Related
- [[wiki/data-storage/vector-databases|Vector Databases]] — HNSW is their common default index
- [[wiki/data-storage/faiss|FAISS]] — implements HNSW among other indexes
- [[wiki/data-storage/ivf|IVF Index]] — the clustering-based alternative
- [[wiki/data-storage/product-quantization|Product Quantization]] — compression that can pair with HNSW
- [[wiki/data-storage/index|Data Storage]] — ANN index family
