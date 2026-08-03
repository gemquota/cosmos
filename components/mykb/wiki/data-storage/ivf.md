---
type: "concept"
title: "IVF Index"
description: "Inverted-file index that partitions vectors into clusters for approximate search"
tags: ["ivf", "ann", "clustering", "index"]
timestamp: "2026-07-31T00:00:00Z"
status: "growing"
---

# IVF Index

## Summary
An IVF (inverted file) index clusters the corpus into cells, then searches only the cells nearest the query — a classic speed-up with controllable recall loss. It is the workhorse index for very large collections because it keeps memory low while staying fast.

## Details
- Mechanics: k-means centroids partition the vectors into nlist cells; each vector is assigned to its nearest centroid and stored in that cell's list; a query finds the nprobe nearest centroids and scans only those lists, skipping the rest; nprobe is the recall dial.
- Concrete example: 1M vectors with nlist 4096 and nprobe 8 — the query visits 8 of 4096 cells, scanning about 2,000 vectors instead of 1M; recall lands near 90-95%; increasing nprobe to 64 raises recall toward exact at 8x the scan cost.
- Failure modes: nlist too small, making cells huge and scans slow; nprobe too small, missing the true nearest neighbour; a skewed corpus where one cell holds most vectors, defeating the partition; index built on outdated centroids after the data distribution shifts; dynamic insertions landing in wrong cells, degrading accuracy.
- Tradeoffs: IVF uses far less memory than HNSW and gives high recall with enough probes, at the cost of a training step (k-means) and weaker support for dynamic inserts; the mature pattern is IVF with product quantization for memory-bound corpora, tuned nlist/nprobe against a recall benchmark.
- Operational notes: benchmark recall at your nprobe, monitor cell balance, and rebuild the index when the corpus changes materially.
- RSIS3 relevance: IVF gives mykb a lean, scalable semantic index — the clustering-based option when the embedding corpus grows large.

## Related
- [[wiki/data-storage/vector-databases|Vector Databases]] — IVF is a standard index option
- [[wiki/data-storage/faiss|FAISS]] — the library that made IVF canonical
- [[wiki/data-storage/hnsw|HNSW]] — the graph alternative to clustering
- [[wiki/data-storage/product-quantization|Product Quantization]] — often combined with IVF for compression
- [[wiki/data-storage/index|Data Storage]] — ANN index family
