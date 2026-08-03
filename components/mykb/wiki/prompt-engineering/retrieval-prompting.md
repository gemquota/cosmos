---
type: "concept"
title: "Retrieval Prompting"
description: "Augmenting prompts with relevant documents fetched from a knowledge base, the core of retrieval-augmented generation"
tags: ["retrieval", "rag", "prompting", "knowledge-base"]
timestamp: "2026-07-31T00:00:00Z"
status: "growing"
---

# Retrieval Prompting

## Summary
Retrieval prompting fetches the most relevant passages from a knowledge store and inserts them into the prompt, grounding the model in external facts. It is the standard way to keep models current and factual without retraining — the core of retrieval-augmented generation.

## Details
- Pipeline: embed the query (or tokenize for TF-IDF/BM25), search the index, take top-k passages, and append them with citations; the model answers from the supplied evidence; reranking, chunking, and metadata filtering tune which passages arrive.
- Concrete example: a query about a wiki topic embeds, searches mykb's index, retrieves the top-3 passages, and the model composes an answer citing them; a RAG chatbot grounds answers in the latest docs; a reranker reorders the top-50 candidates so the best evidence reaches the prompt.
- Failure modes: ungrounded filler when retrieval returns nothing relevant — the model guesses; answers contradicting retrieved evidence; indirect prompt injection from poisoned documents; chunking that splits meaning across passage boundaries; metadata filters that exclude the right documents.
- Tradeoffs: retrieval prompting trades prompt budget and pipeline complexity for freshness and grounding; the alternative, relying on parametric memory, is simple and stale; the mature pattern is a strong retrieval layer, citation-required prompting, and security handling for untrusted passages.
- Operational notes: eval retrieval quality and answer faithfulness, monitor retrieval hit rates, and treat retrieved content as untrusted.
- RSIS3 relevance: mykb's TF-IDF and embedding search are the retrieval layer RSIS3 prompts draw from — retrieval quality bounds loop answer quality.

- Require the model to cite or quote retrieved evidence, which makes ungrounded filler visible in the output.
## Related
- [[wiki/prompt-engineering/context-engineering|Context Engineering]] — The umbrella practice retrieval fits into
- [[wiki/ml-frameworks/embeddings-api|Embeddings API]] — Vector retrieval via embeddings
- [[wiki/prompt-engineering/indirect-injection|Indirect Injection]] — The security risk of retrieved content
- [[wiki/prompt-engineering/prompt-chaining|Prompt Chaining]] — Retrieve-then-generate as a chain
- [[wiki/concepts/mykb-analysis|mykb: Personal LLM Wiki — Analysis & Enrichment Theory]] — mykb is the retrieval store for RSIS3
