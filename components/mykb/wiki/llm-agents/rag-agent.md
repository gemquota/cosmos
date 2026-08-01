---
type: "concept"
title: "RAG Agent"
description: "An agent that retrieves external knowledge before answering or acting"
tags: ["rag", "retrieval", "grounding", "llm"]
timestamp: "2026-07-31T00:00:00Z"
status: "stub"
---

# RAG Agent

## Summary
A RAG agent combines retrieval with generation: at each step it queries external stores (mykb, documents, the web) and grounds its reasoning in the results. It matters because retrieval makes answers current, sourced, and verifiable. It is the read path of memory-augmented agents.

## Details
- Pipeline: query formulation → retrieval → context assembly → generation.
- Hybrid search (TF-IDF + embeddings + backlinks) improves recall.
- Retrieval quality bounds answer quality: garbage in, grounded garbage out.
- Open questions: when to retrieve, and how to cite faithfully.

## Related
- [[wiki/llm-agents/memory-augmented-agents|Memory-Augmented Agents]] — the architecture RAG serves
- [[wiki/llm-agents/context-management|Context Management]] — assembling retrieved context
- [[wiki/concepts/semantic-memory|Semantic Memory]] — the store being retrieved
- [[wiki/llm-agents/hallucination-mitigation|Hallucination Mitigation]] — grounding reduces fabrication
- [[wiki/llm-agents/prompt-caching|Prompt Caching]] — caching retrieved context
