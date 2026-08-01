---
type: "concept"
title: "Embeddings API"
description: "Hosted endpoints that convert text into dense vectors for search, clustering, and classification"
tags: ["embeddings-api", "embeddings", "rag", "apis"]
timestamp: "2026-07-31T00:00:00Z"
status: "stub"
---

# Embeddings API

## Summary
Embeddings APIs map text to fixed-size dense vectors such that similar text is nearby in vector space. They power semantic search, RAG retrieval, and deduplication across most production LLM systems.

## Details
- Providers: OpenAI, Anthropic, Google, Cohere, and open local models (e.g., sentence-transformers).
- Dimension sizes (384-3072) trade quality against storage and latency.
- Usage patterns: chunk documents, index vectors, retrieve top-k by cosine similarity.
- RSIS3 relevance: mykb's semantic search layer consumes embeddings for retrieval prompting.

## Related
- [[wiki/prompt-engineering/retrieval-prompting|Retrieval Prompting]] — The RAG pattern embeddings enable
- [[wiki/ml-frameworks/openai-api|OpenAI API]] — A major embeddings provider
- [[wiki/ml-frameworks/google-gemini|Google Gemini]] — Google's embedding options
- [[wiki/prompt-engineering/context-engineering|Context Engineering]] — Choosing what to embed and retrieve
- [[wiki/concepts/mykb-analysis|mykb: Personal LLM Wiki — Analysis & Enrichment Theory]] — mykb's vector search implementation
- [[wiki/prompt-engineering/context-windows|Context Windows]] — Embedding retrieval must fit the window
