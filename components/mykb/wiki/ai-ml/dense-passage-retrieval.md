---
type: "concept"
title: "Dense Passage Retrieval (DPR)"
description: "Bi-encoder retrieval model that maps queries and passages to shared dense vectors for similarity search"
tags: ["retrieval", "embeddings", "bi-encoder"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Dense Passage Retrieval (DPR)

## Summary
Bi-encoder retrieval model that maps queries and passages to shared dense vectors for similarity search

## Details
- Query and passage encoders are trained so relevant pairs are close in vector space.
- DPR established the modern dual-encoder retrieval paradigm.
- Requires hard-negative mining for good training signal.
- Still a reference baseline for dense retrieval systems.

## Related
- [[wiki/ai-ml/embeddings-and-vector-search|Embeddings and Vector Search]] — deployment substrate
- [[wiki/ai-ml/colbert-model|ColBERT]] — token-level successor
- [[wiki/ai-ml/bm25-hybrid-fusion|BM25 Hybrid Fusion]] — lexical counterpart to combine
- [[wiki/meta-learning/sentence-transformers|Sentence Transformers]] — tooling to train and deploy
- [[wiki/ai-ml/reranking-strategies|Reranking Strategies]] — post-filtering stage
