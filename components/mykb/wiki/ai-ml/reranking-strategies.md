---
type: "concept"
title: "Reranking Strategies"
description: "Reordering retrieved candidates with a second, more expensive scorer to improve precision"
tags: ["reranking", "retrieval", "ranking", "precision"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://www.sbert.net/examples/applications/cross-encoder/README.html", "https://arxiv.org/abs/2104.09686"]
---

# Reranking Strategies

## Summary
Reranking takes a broad candidate list from a fast first stage and re-scores it with a stronger model. It matters because cheap retrievers trade precision for recall; a reranker restores precision on the top-k. The pattern dominates production search and RAG.

## Details
- **Design** — first stage (BM25 or bi-encoder) returns ~100 candidates; cross-encoder reranks top 10-20 for the final context.
- **Models** — cross-encoders score query-document pairs jointly; LLM-based rerankers add instructions and zero-shot flexibility.
- **Worked example** — hybrid search returns 50 chunks; a cross-encoder re-scores them; the top 5 enter the prompt.
- **Cost** — reranking is expensive per pair, so candidate counts must be tuned.
- **mykb relevance** — reranking lifts retrieval precision for RSIS3 grounded answers.
- **Worked example** — hybrid search returns 50 chunks; a cross-encoder re-scores them; the top 5 enter the prompt.
- **Latency budget** — reranking adds per-pair cost, so tune candidate count against quality gains.
- **Design** — a first stage returns roughly a hundred candidates; the reranker narrows to the top handful that enter the prompt.

## Related
- [[wiki/ai-ml/hybrid-search-systems|Hybrid Search Systems]] — first stage
- [[wiki/ai-ml/colbert-model|ColBERT]] — late-interaction scorer
- [[wiki/data-storage/reciprocal-rank-fusion|Reciprocal Rank Fusion]] — score fusion
- [[wiki/data-storage/retrieval-augmented-generation|Retrieval-Augmented Generation]] — consumer
- [[wiki/llm-agents/semantic-caching|Semantic Caching]] — cache interplay
- [[wiki/ai-ml/bm25-hybrid-fusion|BM25 Hybrid Fusion]] — related concept in this cluster
- [[wiki/data-storage/cosine-similarity|Cosine Similarity]] — vector metric
- [[wiki/data-storage/vector-databases|Vector Databases]] — vector search systems
