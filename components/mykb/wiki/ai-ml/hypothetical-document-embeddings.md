---
type: "concept"
title: "Hypothetical Document Embeddings (HyDE)"
description: "Technique that asks the LLM to draft a hypothetical answer and embeds that draft to search the index"
tags: ["embeddings", "rag", "retrieval"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Hypothetical Document Embeddings (HyDE)

## Summary
Technique that asks the LLM to draft a hypothetical answer and embeds that draft to search the index

## Details
- The generated answer often sits closer in embedding space to real documents than the raw query.
- HyDE improves recall on short or ambiguous queries at the cost of one generation call.
- Its synthetic text can drift from the actual answer, so verify retrieved evidence.
- Composes with query-decomposition and reranking.

## Related
- [[wiki/ai-ml/embeddings-and-vector-search|Embeddings and Vector Search]] — embedding space it exploits
- [[wiki/ai-ml/query-transformations|Query Transformations]] — family it belongs to
- [[wiki/ai-ml/reranking-strategies|Reranking Strategies]] — fixing false positives
- [[wiki/ai-ml/agentic-rag|Agentic RAG]] — using generation inside retrieval
- [[wiki/ai-ml/grounded-generation|Grounded Generation]] — why evidence still matters
