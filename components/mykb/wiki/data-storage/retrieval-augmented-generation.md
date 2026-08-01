---
type: "concept"
title: "Retrieval-Augmented Generation"
description: "Pattern that grounds LLM answers in retrieved evidence from an external knowledge store"
tags: ["rag", "llm", "retrieval", "grounding", "generation"]
timestamp: "2026-07-31T00:00:00Z"
status: "growing"
source: ["https://arxiv.org/abs/2005.11401"]
---

# Retrieval-Augmented Generation

## Summary
Retrieval-augmented generation (RAG) retrieves relevant passages from a knowledge store and feeds them to a language model as context before generation. It reduces hallucination, keeps answers grounded in up-to-date sources, and lets a static model answer over a private corpus. RSIS3-style loops use RAG whenever a pulse needs to consult mykb memory.

## Details
- **Pipeline** — embed the query, search a vector index (or hybrid index), take the top-k passages, then prompt the LLM with `context + question`.
- **Origin** — Lewis et al. (2020) introduced RAG as an end-to-end model combining a dense retriever with a seq2seq generator; the pattern is now standard for knowledge-grounded chatbots and agents.
- **Quality levers** — chunk size, top-k, reranking, and metadata filters matter more than model choice for many domain Q&A tasks.
- **Failure modes** — irrelevant or contradictory retrieved passages propagate errors; provenance (which source the answer cites) is the mitigation.
- **Worked example** — mykb's daemon returns TF-IDF and embedding search results as context; the answer is written back with `source:` links so RSIS3 can audit claims.
- **Variants** — naive RAG (single retrieval) vs advanced flows (multi-hop, query rewriting, agentic retrieval) trade latency for precision.

## Related
- [[wiki/data-storage/vector-databases|Vector Databases]] — the primary index backing RAG retrieval
- [[wiki/data-storage/embeddings|Embeddings]] — dense representations that make retrieval semantic
- [[wiki/data-storage/chunking-strategies|Chunking Strategies]] — decides what granularity of evidence gets retrieved
- [[wiki/data-storage/hybrid-search|Hybrid Search]] — combines lexical and semantic recall for RAG
- [[wiki/data-storage/chromadb|ChromaDB]] — a lightweight local vector store for RAG experiments
- [[wiki/meta-learning/colbert|ColBERT]] — late-interaction reranker used to improve RAG precision
- [[wiki/concepts/mykb-research-report|Mykb Research Report]] — documents the RAG-style search design in mykb
- [[wiki/concepts/mykb-implementation-report|Mykb Implementation Report]] — records how the retrieval pipeline was actually built
