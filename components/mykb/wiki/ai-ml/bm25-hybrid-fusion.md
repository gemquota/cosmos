---
type: "concept"
title: "BM25 and Hybrid Fusion"
description: "Combining lexical BM25 scoring with dense vector similarity and fusing rankings for better retrieval"
tags: ["lexical", "hybrid", "retrieval"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# BM25 and Hybrid Fusion

## Summary
BM25 and hybrid fusion combines lexical BM25 scoring with dense vector similarity and merges the two rankings into one result list. The hybrid covers both lexical precision — exact terms and rare identifiers that embeddings miss — and semantic recall — paraphrase and synonym matches that keyword search misses.

## Details
- **BM25 half** — a sparse, bag-of-words score based on term frequency, document length, and inverse document frequency; it excels at exact matches, product codes, and domain jargon.
- **Dense half** — embedding similarity captures meaning beyond surface form, so queries phrased differently from the document still match.
- **Fusion methods** — weighted score blending requires calibrated score ranges; rank-based fusion (reciprocal rank fusion) ignores raw scores and merges by position, which is simpler and robust to scale differences.
- **When hybrid wins** — neither retriever alone is sufficient: the lexical side misses paraphrases, the dense side misses rare exact tokens; fusing them lifts recall while preserving precision.
- **Tuning** — fusion weights or rank cutoffs need validation on the target corpus; naive 50/50 blends can be worse than either retriever when one side is noisy.
- **Failures** — duplicate evidence across both lists can over-represent one document; deduplication and cap-per-document policies fix the worst cases.
- **In practice** — hybrid retrieval is the standard backbone for retrieval-augmented generation over heterogeneous corpora, with reranking applied after fusion.

- **Score normalization note** — when blending scores directly, BM25 ranges and cosine ranges differ by orders of magnitude; min-max or z-score normalization per retriever on a validation query set prevents one side from silently dominating the blend.
## Related
- [[wiki/data-storage/reciprocal-rank-fusion|Reciprocal Rank Fusion]] — rank-based fusion method
- [[wiki/ai-ml/hybrid-search-systems|Hybrid Search Systems]] — system-level pattern
- [[wiki/ai-ml/dense-passage-retrieval|Dense Passage Retrieval]] — dense half of the pair
- [[wiki/ai-ml/reranking-strategies|Reranking Strategies]] — applied after fusion
- [[wiki/data-storage/retrieval-augmented-generation|Retrieval-Augmented Generation]] — consumer of fused retrieval
- [[wiki/data-storage/search-and-relevance-ranking|Search and Relevance Ranking]] — ranking foundations
