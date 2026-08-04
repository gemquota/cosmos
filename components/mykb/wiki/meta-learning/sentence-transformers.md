---
type: "entity"
title: "Sentence Transformers"
description: "Framework for embedding sentences and paragraphs with transformer models"
tags: ["sentence-transformers", "embeddings", "bert", "semantic"]
timestamp: "2026-07-31T00:00:00Z"
status: "stub"
---

# Sentence Transformers

## Summary
Sentence Transformers (SBERT) fine-tunes BERT-style models to map sentences to compact vectors so that semantically similar sentences are near each other. It is the standard toolkit for production semantic search embeddings.

## Details
- **Architecture** — pooling over transformer token embeddings (CLS or mean), trained with siamese/triplet objectives.
- **Applications** — semantic search, clustering, RAG retrieval, and paraphrase detection.
- **Practicality** — a huge model zoo (multilingual, specialized domains) and simple Python API make it the default embedder.

## Related
- [[wiki/data-storage/embeddings|Embeddings]] — the representations SBERT produces
- [[wiki/data-storage/semantic-search|Semantic Search]] — SBERT's primary application
- [[wiki/meta-learning/bi-encoder|Bi-Encoder]] — the architecture SBERT uses
- [[wiki/meta-learning/cross-encoder|Cross-Encoder]] — the reranking counterpart
- [[wiki/meta-learning/00-index|Meta-Learning]] — representation learning family
