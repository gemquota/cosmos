---
type: "concept"
title: "Cross-Encoder"
description: "Model scoring query-document pairs jointly through full attention"
tags: ["cross-encoder", "reranking", "retrieval", "transformer"]
timestamp: "2026-07-31T00:00:00Z"
status: "stub"
---

# Cross-Encoder

## Summary
A cross-encoder feeds the query and a document together into a transformer and outputs a single relevance score, capturing full token interactions. It is the most accurate but slowest ranking architecture, typically used to rerank top-k candidates.

## Details
- **Mechanism** — `[CLS] query [SEP] doc` through the transformer; the pooled output scores relevance.
- **Use pattern** — retrieve 50-100 candidates with a bi-encoder, rerank the top 10 with a cross-encoder.
- **Trade-off** — accuracy vs cost: pairwise scoring cannot be precomputed, so corpus-wide search is impractical.

## Related
- [[wiki/meta-learning/bi-encoder|Bi-Encoder]] — the precomputation-friendly alternative
- [[wiki/meta-learning/colbert|ColBERT]] — the middle ground between the two
- [[wiki/meta-learning/sentence-transformers|Sentence Transformers]] — hosts cross-encoder models
- [[wiki/data-storage/semantic-search|Semantic Search]] — the pipeline cross-encoders refine
- [[wiki/meta-learning/knowledge-distillation|Knowledge Distillation]] — cross-encoders often distill into bi-encoders
- [[wiki/meta-learning/index|Meta-Learning]] — retrieval model family
