---
type: "concept"
title: "Bi-Encoder"
description: "Model encoding query and document separately into vectors for fast similarity search"
tags: ["bi-encoder", "embeddings", "retrieval", "architecture"]
timestamp: "2026-07-31T00:00:00Z"
status: "growing"
---

# Bi-Encoder

## Summary
A bi-encoder runs the query and each document through the same encoder independently, producing vectors that are compared by cosine or dot product. Because document vectors are precomputed, it is the architecture behind scalable semantic search.

## Details
- **Mechanism** — two encoders (often weight-shared) → one vector each → similarity score; nothing is computed per query-document pair, so all document vectors can be embedded once and indexed ahead of time.
- **Use** — first-stage retrieval over millions of items; the vectors live in a vector database with approximate nearest-neighbour indexes (HNSW, IVF), so a query scans candidates in milliseconds rather than scoring every document.
- **Training** — bi-encoders are trained with contrastive losses on positive and negative pairs: in-batch negatives are the cheapest source, hard negatives mined from the model's own mistakes sharpen the boundary, and cross-encoder scores can label training pairs; in practice, mining good negatives matters more than the loss function itself.
- **Trade-off** — the independent encoding loses query-document interaction, so it is fast and scalable but weaker than cross-encoders on fine-grained relevance; retrieval quality depends heavily on how well the embedding space captures the notion of similarity the task needs.
- **Failure modes** — embedding spaces drift when the encoder is updated (indexes must be rebuilt), long documents exceed the token limit and get truncated, and frequency biases make popular terms dominate similarity; chunking strategy is therefore part of the design.
- **mykb relevance** — a documented design for the wiki's semantic search would be a bi-encoder pipeline: notes would be embedded once and queried at write time, so the quality of note retrieval would depend on the encoder choice, chunk boundaries, and index refresh policy, not just on the query text.

## Related
- [[wiki/meta-learning/sentence-transformers|Sentence Transformers]] — the toolkit for training bi-encoders
- [[wiki/data-storage/embeddings|Embeddings]] — the vectors bi-encoders produce
- [[wiki/meta-learning/cross-encoder|Cross-Encoder]] — the reranking counterpart
- [[wiki/meta-learning/colbert|ColBERT]] — the late-interaction middle ground
- [[wiki/data-storage/vector-databases|Vector Databases]] — where bi-encoder vectors are indexed
- [[wiki/meta-learning/00-index|Meta-Learning]] — retrieval model family
