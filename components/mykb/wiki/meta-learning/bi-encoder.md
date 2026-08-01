---
type: "concept"
title: "Bi-Encoder"
description: "Model encoding query and document separately into vectors for fast similarity search"
tags: ["bi-encoder", "embeddings", "retrieval", "architecture"]
timestamp: "2026-07-31T00:00:00Z"
status: "stub"
---

# Bi-Encoder

## Summary
A bi-encoder runs the query and each document through the same encoder independently, producing vectors that are compared by cosine or dot product. Because document vectors are precomputed, it is the architecture behind scalable semantic search.

## Details
- **Mechanism** — two encoders (often weight-shared) → one vector each → similarity score; nothing is computed per query-document pair.
- **Use** — first-stage retrieval over millions of items; the vectors live in a vector database.
- **Trade-off** — fast and scalable, weaker than cross-encoders on fine-grained relevance.

## Related
- [[wiki/meta-learning/sentence-transformers|Sentence Transformers]] — the toolkit for training bi-encoders
- [[wiki/data-storage/embeddings|Embeddings]] — the vectors bi-encoders produce
- [[wiki/meta-learning/cross-encoder|Cross-Encoder]] — the reranking counterpart
- [[wiki/meta-learning/colbert|ColBERT]] — the late-interaction middle ground
- [[wiki/data-storage/vector-databases|Vector Databases]] — where bi-encoder vectors are indexed
- [[wiki/meta-learning/index|Meta-Learning]] — retrieval model family
