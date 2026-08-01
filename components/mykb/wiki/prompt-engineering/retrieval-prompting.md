---
type: "concept"
title: "Retrieval Prompting"
description: "Augmenting prompts with relevant documents fetched from a knowledge base, the core of retrieval-augmented generation"
tags: ["retrieval", "rag", "prompting", "knowledge-base"]
timestamp: "2026-07-31T00:00:00Z"
status: "stub"
---

# Retrieval Prompting

## Summary
Retrieval prompting fetches the most relevant passages from a knowledge store and inserts them into the prompt, grounding the model in external facts. It is the standard way to keep models current and factual without retraining.

## Details
- Pipeline: embed the query, search a vector index (or TF-IDF/BM25), take top-k passages, and append them with citations.
- Passage selection quality dominates answer quality; chunking, reranking, and metadata filtering all matter.
- Failure modes: ungrounded filler, contradicting retrieved evidence, and indirect prompt injection from poisoned documents.
- RSIS3 relevance: mykb's TF-IDF and embedding search are the retrieval layer RSIS3 prompts draw from.

## Related
- [[wiki/prompt-engineering/context-engineering|Context Engineering]] — The umbrella practice retrieval fits into
- [[wiki/ml-frameworks/embeddings-api|Embeddings API]] — Vector retrieval via embeddings
- [[wiki/prompt-engineering/indirect-injection|Indirect Injection]] — The security risk of retrieved content
- [[wiki/prompt-engineering/prompt-chaining|Prompt Chaining]] — Retrieve-then-generate as a chain
- [[wiki/concepts/mykb-analysis|mykb: Personal LLM Wiki — Analysis & Enrichment Theory]] — mykb is the retrieval store for RSIS3
