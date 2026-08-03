---
type: "concept"
title: "Cross-Encoder"
description: "Model scoring query-document pairs jointly through full attention"
tags: ["cross-encoder", "reranking", "retrieval", "transformer"]
timestamp: "2026-07-31T00:00:00Z"
status: "growing"
---

# Cross-Encoder

## Summary
A cross-encoder feeds the query and a document together into a transformer and outputs a single relevance score, capturing full token interactions. It is the most accurate but slowest ranking architecture, typically used to rerank top-k candidates.

## Details
- **Mechanism** — `[CLS] query [SEP] doc` through the transformer; the pooled output scores relevance. Because query and document tokens attend to each other in every layer, the model sees exact lexical overlap, negation, paraphrase, and cross-references that independent encodings miss.
- **Use pattern** — retrieve 50-100 candidates with a bi-encoder, rerank the top 10 with a cross-encoder; this two-stage design keeps corpus-wide search fast while putting the strongest model on the small candidate set where its cost is affordable.
- **Trade-off** — accuracy vs cost: pairwise scoring cannot be precomputed, so corpus-wide search is impractical; every query-document pair is a full forward pass, and latency grows linearly with candidates, which is why cross-encoders are a reranking stage, not a retriever.
- **Failure modes** — long documents exceed the token window and are truncated (losing the decisive evidence), so passage segmentation matters; cross-encoders trained on one domain transfer poorly to out-of-distribution queries; and they inherit the biases of their training labels, so a sloppy relevance dataset produces a confident but wrong ranker.
- **Training** — fine-tuned on relevance labels with pairwise or listwise losses, and commonly used as teachers to distill ranking quality into bi-encoders, which inherit most of the accuracy at a fraction of the serving cost.
- **mykb relevance** — a documented design for the wiki's search pipeline would be the classic two-stage design: bi-encoder retrieval for recall, cross-encoder reranking for precision; adding a lightweight cross-encoder rerank step would measurably improve which notes surface for RSIS3's context retrieval without changing the index at all.

## Related
- [[wiki/meta-learning/bi-encoder|Bi-Encoder]] — the precomputation-friendly alternative
- [[wiki/meta-learning/colbert|ColBERT]] — the middle ground between the two
- [[wiki/meta-learning/sentence-transformers|Sentence Transformers]] — hosts cross-encoder models
- [[wiki/data-storage/semantic-search|Semantic Search]] — the pipeline cross-encoders refine
- [[wiki/meta-learning/knowledge-distillation|Knowledge Distillation]] — cross-encoders often distill into bi-encoders
- [[wiki/meta-learning/index|Meta-Learning]] — retrieval model family
