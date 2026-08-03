---
type: "concept"
title: "RAG Agent"
description: "An agent that retrieves external knowledge before answering or acting"
tags: ["rag", "retrieval", "grounding", "llm"]
timestamp: "2026-07-31T00:00:00Z"
status: "growing"
---
# RAG Agent

## Summary

A RAG agent combines retrieval with generation: before answering or acting it queries external stores — the wiki, documents, the web — and grounds its reasoning in the results. Retrieval makes answers current, sourced, and verifiable; it is the read path of memory-augmented agents.

## Details
- Mechanism: the pipeline is query formulation → retrieval → context assembly → generation (→ optional tool use and re-retrieval); retrievers include TF-IDF/BM25 (exact keyword), embeddings (semantic), hybrid fusion (combine both), and backlink/graph traversal over the wiki's OKF structure; retrieved chunks are ranked, deduplicated, and assembled into the prompt with citations.
- Concrete example: a wiki assistant receives "what does the loop do on constraint violations?" — it formulates the query, retrieves the top-k synthesis and constraint notes via hybrid search, assembles their key sections, and answers with the source note names; a follow-up can retrieve more. Without retrieval, the model answers from parametric memory: plausible, outdated, or fabricated.
- Failure modes: retrieval quality bounds answer quality — garbage in, grounded garbage out (bad chunking, stale index, wrong ranker); context stuffing (dumping 50 chunks dilutes signal and costs tokens); citations that do not match the claim; and the agent never verifying that retrieved content actually supports its answer (faithfulness gap).
- Operational tradeoffs: RAG trades latency and index maintenance for groundedness; the discipline is evaluating retrieval (recall@k) and generation (faithfulness) separately, keeping the index fresh, and logging which chunks shaped each answer for audit.
- RSIS3/mykb relevance: the wiki is the RAG corpus — TF-IDF plus embeddings plus backlinks surface syntheses from prior loops, so new sessions inherit durable conclusions instead of re-deriving them.
- Retrieval evals: maintain a query→relevant-chunk gold set and track recall@k after every index or chunking change; retrieval regressions are invisible in end-to-end demos.
- Grounding check: for high-stakes answers, verify each claim against its cited chunk (self-check or a verifier pass); retrieval plus fluent generation is not yet groundedness.

## Related
- [[wiki/llm-agents/memory-augmented-agents|Memory-Augmented Agents]] — the architecture RAG serves
- [[wiki/llm-agents/context-management|Context Management]] — assembling retrieved context
- [[wiki/concepts/semantic-memory|Semantic Memory]] — the store being retrieved
- [[wiki/llm-agents/hallucination-mitigation|Hallucination Mitigation]] — grounding reduces fabrication
- [[wiki/llm-agents/prompt-caching|Prompt Caching]] — caching retrieved context
