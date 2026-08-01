---
type: "concept"
title: "ColBERT"
description: "Late-interaction retriever scoring query-document pairs token-by-token"
tags: ["colbert", "retrieval", "reranking", "late-interaction"]
timestamp: "2026-07-31T00:00:00Z"
status: "stub"
---

# ColBERT

## Summary
ColBERT computes separate token embeddings for query and document, then scores matches with MaxSim over token pairs — a late-interaction design that gets cross-attention quality at near bi-encoder speed. It is a leading model for retrieval and reranking.

## Details
- **Mechanism** — encode query and document independently (fast precomputation), then sum per-token max similarity (the late interaction).
- **Deployment** — used both as a retriever and, with ColBERTv2, as a reranker over candidate sets.
- **Trade-off** — stronger than bi-encoders, heavier than cross-encoders; index storage grows with token embeddings.

## Related
- [[wiki/data-storage/semantic-search|Semantic Search]] — the task ColBERT targets
- [[wiki/meta-learning/bi-encoder|Bi-Encoder]] — the faster, weaker baseline
- [[wiki/meta-learning/cross-encoder|Cross-Encoder]] — the stronger, slower baseline
- [[wiki/meta-learning/sentence-transformers|Sentence Transformers]] — the framework hosting ColBERT variants
- [[wiki/data-storage/retrieval-augmented-generation|Retrieval-Augmented Generation]] — ColBERT reranking improves RAG
- [[wiki/meta-learning/index|Meta-Learning]] — retrieval model family
