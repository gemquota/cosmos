---
type: "concept"
title: "Product Quantization"
description: "Compressing vectors by quantizing sub-vectors into learned codebooks"
tags: ["pq", "quantization", "compression", "ann"]
timestamp: "2026-07-31T00:00:00Z"
status: "growing"
---

# Product Quantization

## Summary
Product quantization splits each vector into sub-vectors, learns a small codebook per subspace, and stores only codes — shrinking memory 10-100x at some recall cost. It is how billion-scale ANN indexes fit in RAM.

## Details
- Mechanism: each vector is divided into m sub-vectors; k-means learns a codebook (typically 256 centroids, 8 bits) per subspace; each sub-vector is replaced by its nearest centroid's code; distance between a query and a stored vector is approximated via lookup tables over the codes, avoiding full vector math.
- Concrete example: a 128-dim float vector (512 bytes) compressed to 16 codes of 8 bits (16 bytes) — a 32x memory cut; an IVF-PQ index with 1B vectors fits in tens of GB; recall drops a few points but the index becomes practical on one machine.
- Failure modes: codebook training on an unrepresentative sample, degrading all distances; too few centroids per subspace collapsing distinct vectors; recall loss compounded when PQ is combined with aggressive IVF probing; reconstruction error for vectors in sparse regions of the space.
- Tradeoffs: PQ trades accuracy and some query complexity for dramatic memory savings and faster scans; the alternative, full-precision vectors, is exact and memory-hungry; the mature pattern is PQ for memory-bound corpora, with refinement (re-ranking exact distances for the top candidates) to recover recall.
- Operational notes: train codebooks on representative data, benchmark recall versus memory, and add candidate re-ranking where accuracy matters.
- RSIS3 relevance: PQ indexes let a local device hold very large embedding collections for mykb-style recall — the memory lever when the wiki corpus grows.

## Practice
- Combine PQ with re-ranking: compress for the candidate scan, then re-score the top candidates on full vectors.
## Related
- [[wiki/data-storage/hnsw|HNSW]] — graph index that can be PQ-compressed
- [[wiki/data-storage/ivf|IVF Index]] — clustering usually paired with PQ
- [[wiki/data-storage/faiss|FAISS]] — where PQ is implemented and tuned
- [[wiki/data-storage/vector-databases|Vector Databases]] — the systems that ship PQ options
- [[wiki/data-storage/index|Data Storage]] — ANN compression family
