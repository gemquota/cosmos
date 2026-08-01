---
type: "concept"
title: "IVF Index"
description: "Inverted-file index that partitions vectors into clusters for approximate search"
tags: ["ivf", "ann", "clustering", "index"]
timestamp: "2026-07-31T00:00:00Z"
status: "stub"
---

# IVF Index

## Summary
An IVF (inverted file) index clusters the corpus into cells, then searches only the cells nearest the query — a classic speed-up with controllable recall loss. It is the workhorse index for very large collections.

## Details
- **Mechanics** — k-means centroids partition vectors; the query visits nprobe nearest centroids and scans their lists.
- **Parameters** — nlist (cell count) and nprobe (cells visited) trade speed against recall; more probes = slower, better.
- **Trade-off** — lower memory than HNSW, high recall with enough probes; less flexible for dynamic insertions.

## Related
- [[wiki/data-storage/vector-databases|Vector Databases]] — IVF is a standard index option
- [[wiki/data-storage/faiss|FAISS]] — the library that made IVF canonical
- [[wiki/data-storage/hnsw|HNSW]] — the graph alternative to clustering
- [[wiki/data-storage/product-quantization|Product Quantization]] — often combined with IVF for compression
- [[wiki/data-storage/index|Data Storage]] — ANN index family
