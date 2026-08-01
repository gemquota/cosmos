---
type: "concept"
title: "LlamaIndex"
description: "A data framework for connecting LLMs to enterprise and personal data via indexing and retrieval"
tags: ["llamaindex", "rag", "retrieval", "framework"]
timestamp: "2026-07-31T00:00:00Z"
status: "stub"
---

# LlamaIndex

## Summary
LlamaIndex specializes in the data side of LLM apps: ingesting documents, building indexes (vector, keyword, graph), and exposing query interfaces for RAG. It is the retrieval-first counterpart to LangChain.

## Details
- Data connectors cover files, databases, APIs, and unstructured stores.
- Index types include vector, summary, tree, and knowledge-graph structures.
- Query engines add reranking, citations, and structured outputs on top.
- RSIS3 relevance: mykb's own search could be exposed through LlamaIndex-style query interfaces.

## Related
- [[wiki/ml-frameworks/langchain|LangChain]] — The orchestration sibling
- [[wiki/prompt-engineering/retrieval-prompting|Retrieval Prompting]] — The RAG pattern it serves
- [[wiki/ml-frameworks/embeddings-api|Embeddings API]] — The vector backbone
- [[wiki/prompt-engineering/structured-output|Structured Output]] — Query result contracts
- [[wiki/concepts/mykb-analysis|mykb: Personal LLM Wiki — Analysis & Enrichment Theory]] — mykb's retrieval architecture parallels it
