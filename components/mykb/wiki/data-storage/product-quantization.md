---
type: "concept"
title: "Product Quantization"
description: "Compressing vectors by quantizing sub-vectors into learned codebooks"
tags: ["pq", "quantization", "compression", "ann"]
timestamp: "2026-07-31T00:00:00Z"
status: "stub"
---

# Product Quantization

## Summary
Product quantization splits each vector into sub-vectors, learns a small codebook per subspace, and stores only codes — shrinking memory 10-100x at some recall cost. It is how billion-scale ANN indexes fit in RAM.

## Details
- **Mechanism** — each sub-vector is replaced by its nearest centroid index; distances are approximated by lookup tables.
- **Trade-off** — aggressive compression reduces memory and speeds scans but degrades recall unless combined with refinement.
- **Agent relevance** — PQ indexes let a local device hold very large embedding collections for mykb-style recall.

## Related
- [[wiki/data-storage/hnsw|HNSW]] — graph index that can be PQ-compressed
- [[wiki/data-storage/ivf|IVF Index]] — clustering usually paired with PQ
- [[wiki/data-storage/faiss|FAISS]] — where PQ is implemented and tuned
- [[wiki/data-storage/vector-databases|Vector Databases]] — the systems that ship PQ options
- [[wiki/data-storage/index|Data Storage]] — ANN compression family
