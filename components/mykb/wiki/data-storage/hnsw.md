---
type: "concept"
title: "HNSW"
description: "Hierarchical Navigable Small World graphs for approximate nearest-neighbour search"
tags: ["hnsw", "ann", "graph-index", "vector-search"]
timestamp: "2026-07-31T00:00:00Z"
status: "growing"
---

# HNSW

## Summary
HNSW builds a multi-layer graph where each layer is a navigable small-world network, enabling logarithmic-time approximate nearest-neighbour search. It is the default index in most modern vector databases for its speed-recall balance, at the cost of higher memory than clustering-based indexes.

## Details
- Construction: insertion connects each point to a few neighbours per layer (parameter M); upper layers are sparser with longer-range links that let search jump across the graph, lower layers refine; efConstruction controls build quality, efSearch controls query effort.
- Parameters: M (connections per node) trades recall and memory against speed; efConstruction trades build time for index quality; efSearch trades query latency for recall; typical values are M 16-64, efConstruction 100-400, efSearch 10-100.
- Concrete example: a 100k-vector index with HNSW returns top-10 results in a few milliseconds with ~95% recall at efSearch 64; memory sits around 10x vector size before compression; pairing with product quantization cuts memory at a recall cost.
- Failure modes: memory blowup on large corpora without quantization; parameters tuned for latency that collapse recall; indexes built with the wrong metric; dynamic insertions degrading graph quality over time; efSearch set once and never tuned as the corpus grows.
- Tradeoffs: HNSW offers the best speed-recall balance among popular ANN indexes at the cost of memory; IVF is leaner but needs training and has lower recall at equal speed; the mature pattern is HNSW for in-memory workloads and quantization or IVF for memory-bound ones.
- Operational notes: benchmark recall at your efSearch, monitor index size, and rebuild when the corpus changes materially.
- RSIS3 relevance: HNSW as the default index gives mykb fast, high-recall semantic retrieval over article embeddings — the speed-recall balance that matters for agent-time queries.

## Related
- [[wiki/data-storage/vector-databases|Vector Databases]] — HNSW is their common default index
- [[wiki/data-storage/faiss|FAISS]] — implements HNSW among other indexes
- [[wiki/data-storage/ivf|IVF Index]] — the clustering-based alternative
- [[wiki/data-storage/product-quantization|Product Quantization]] — compression that can pair with HNSW
- [[wiki/data-storage/00-index|Data Storage]] — ANN index family
