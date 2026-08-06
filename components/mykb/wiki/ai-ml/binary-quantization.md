---
type: "concept"
title: "Binary Quantization"
description: "Representing vectors as compact binary codes and computing similarity via Hamming distances"
tags: ["quantization", "vector-search", "compression"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Binary Quantization

## Summary
Binary quantization represents high-dimensional vectors as compact binary codes — one sign bit per dimension — and estimates similarity with Hamming distance instead of floating-point dot products. It trades recall for a large cut in memory and a large speedup in distance computation, which makes it attractive for very large embedding collections.

## Details
- **Mechanics** — encode each dimension as +1 or −1 by its sign; similarity between two codes is a bitwise XOR-popcount, which modern CPUs execute as a single instruction stream.
- **Space savings** — one bit per dimension versus 32 for FP32 gives roughly 32x compression, and the compact codes also reduce cache misses and memory bandwidth pressure.
- **Recall trade-off** — magnitude information is discarded, so fine-grained distinctions suffer; recall degrades most for dimensions where sign alone is a weak discriminator.
- **Where it wins** — large, high-dimensional collections (millions of items, 768+ dimensions) where the index would otherwise dominate memory; it is a common coarse stage in two-tier search.
- **Rescoring pattern** — a binary pass selects a shortlist, then the original float vectors re-rank the shortlist, recovering much of the lost precision at modest cost.
- **Variants** — signed thresholds other than the median, multi-bit codes, and learned codes exist; scalar quantization and product quantization occupy the same design space with different trade-offs.
- **Practical notes** — always benchmark recall@k against the float baseline on the target distribution before adopting, because win rates vary by embedding model and data.

- **Centering matters** — subtracting a per-dimension mean before taking signs improves the codes because the sign boundary then sits near the data center, a cheap change that recovers meaningful recall.
## Related
- [[wiki/data-storage/product-quantization|Product Quantization]] — codebook alternative
- [[wiki/data-storage/embeddings|Embeddings]] — what gets quantized
- [[wiki/data-storage/vector-databases|Vector Databases]] — where quantization lives
- [[wiki/data-storage/cosine-similarity|Cosine Similarity]] — what binary codes approximate
- [[wiki/ai-ml/reranking-strategies|Reranking Strategies]] — rescoring after coarse search
- [[wiki/ai-ml/bm25-hybrid-fusion|BM25 and Hybrid Fusion]] — combining lexical and vector tiers
