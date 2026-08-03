---
type: "concept"
title: "ColBERT"
description: "Late-interaction retriever scoring query-document pairs token-by-token"
tags: ["colbert", "retrieval", "reranking", "late-interaction"]
timestamp: "2026-07-31T00:00:00Z"
status: "growing"
---

# ColBERT

## Summary
ColBERT computes separate token embeddings for query and document, then scores matches with MaxSim over token pairs — a late-interaction design that gets cross-attention quality at near bi-encoder speed. It is a leading model for retrieval and reranking.

## Details
- **Mechanism** — encode the query and each document independently with a transformer, producing a matrix of token embeddings per passage; the relevance score is the sum, over query tokens, of the maximum cosine similarity to any document token (MaxSim); interaction happens at scoring time instead of during encoding, which is why it is called 'late interaction'.
- **Deployment** — used both as a first-stage retriever and, with ColBERTv2, as a reranker over candidate sets; the token-level embeddings can be precomputed and compressed (residual compression) so that full-document re-encoding happens only for the top candidates.
- **Strengths** — far better than bi-encoders on fine-grained matching (multi-word terms, negation, paraphrase) because every query token gets its own evidence, and it is robust to vocabulary mismatch that bags-of-words miss.
- **Trade-offs** — heavier than bi-encoders: index storage grows with the number of token embeddings per document, and query-time scoring still loops over token pairs, so large corpora need an efficient first stage to keep latency acceptable.
- **Training** — typically fine-tuned from bi-encoder checkpoints with contrastive or distillation losses, using hard negatives from the retriever's own errors; ColBERTv2 improved robustness with denoised supervision from a cross-encoder teacher.
- **RAG relevance** — reranking with ColBERT narrows retrieval-augmented-generation to the passages that actually contain the evidence, cutting hallucination from irrelevant context while staying fast enough for interactive use; mykb-style retrieval pipelines pair a bi-encoder first stage with ColBERT reranking.

## Related
- [[wiki/data-storage/semantic-search|Semantic Search]] — the task ColBERT targets
- [[wiki/meta-learning/bi-encoder|Bi-Encoder]] — the faster, weaker baseline
- [[wiki/meta-learning/cross-encoder|Cross-Encoder]] — the stronger, slower baseline
- [[wiki/meta-learning/sentence-transformers|Sentence Transformers]] — the framework hosting ColBERT variants
- [[wiki/data-storage/retrieval-augmented-generation|Retrieval-Augmented Generation]] — ColBERT reranking improves RAG
- [[wiki/meta-learning/00-index|Meta-Learning]] — retrieval model family
