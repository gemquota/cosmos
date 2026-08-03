---
type: "concept"
title: "Embeddings API"
description: "Hosted endpoints that convert text into dense vectors for search, clustering, and classification"
tags: ["embeddings-api", "embeddings", "rag", "apis"]
timestamp: "2026-07-31T00:00:00Z"
status: "growing"
---
# Embeddings API

## Summary

The Embeddings API turns text into dense vectors so similarity is computable — semantic search, clustering, and retrieval over the wiki and beyond. The quality of the embedding model and the indexing strategy decide the ceiling of every vector application.

## Details
- Mechanism: the API maps text to a fixed-dimension vector (dimensions vary by model, with Matryoshka options for truncation); similarity is cosine distance; indexes (HNSW, IVF, flat) trade recall for speed; hybrid retrieval fuses vector similarity with BM25/keyword scores; chunking and normalization (per-document, per-paragraph) determine what granularity gets compared.
- Concrete example: the wiki indexes note chunks with embeddings; a query "how does the loop handle constraint violations" is embedded and the index returns the nearest syntheses; re-ranking the top-k with a cross-encoder or keyword overlap lifts precision; a clustering pass groups related notes for the graph view.
- Failure modes: embedding drift — changing models changes the space and invalidates old vectors (re-index); chunking mismatch (searching whole notes but indexing paragraphs); dimension/cost surprises at scale; and semantic false positives — vector proximity is not factual relevance (verify with re-rankers and filters).
- Operational tradeoffs: embeddings buy semantic matching that keyword search misses at index and API cost; the discipline is hybrid retrieval, re-ranking for precision, versioned embedding models with re-index runs, and evaluating retrieval offline before trusting it online.
- RSIS3/mykb relevance: the wiki's search fuses TF-IDF, embeddings, and backlinks; this note records the embedding model and re-index policy so retrieval stays reproducible.
- Cost per token: embedding large corpora bills per token on hosted APIs; batch requests and cache embeddings per document version to avoid re-embedding unchanged text.
- Quality checks: run a small gold set of similar/not-similar pairs against the chosen model; embedding quality varies by domain (code, legal, wiki prose) and the leaderboard may not reflect yours.

## Related
- [[wiki/prompt-engineering/retrieval-prompting|Retrieval Prompting]] — The RAG pattern embeddings enable
- [[wiki/ml-frameworks/openai-api|OpenAI API]] — A major embeddings provider
- [[wiki/ml-frameworks/google-gemini|Google Gemini]] — Google's embedding options
- [[wiki/prompt-engineering/context-engineering|Context Engineering]] — Choosing what to embed and retrieve
- [[wiki/concepts/mykb-analysis|mykb: Personal LLM Wiki — Analysis & Enrichment Theory]] — mykb's vector search implementation
- [[wiki/prompt-engineering/context-windows|Context Windows]] — Embedding retrieval must fit the window
