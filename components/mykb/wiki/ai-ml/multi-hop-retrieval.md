---
type: "concept"
title: "Multi-Hop Retrieval"
description: "Retrieval that chains several search steps, using intermediate results to formulate the next query"
tags: ["rag", "retrieval", "reasoning"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Multi-Hop Retrieval

## Summary
Retrieval that chains several search steps, using intermediate results to formulate the next query

## Details
- Each hop retrieves evidence that refines the next hop query.
- Needed for questions whose answer spans documents.
- Drift and compounding error are the main failure modes.
- Agentic RAG and query-decomposition are practical implementations.

## Related
- [[wiki/ai-ml/query-decomposition|Query Decomposition]] — planning hops up front
- [[wiki/ai-ml/recursive-retrieval|Recursive Retrieval]] — navigating nested sources
- [[wiki/ai-ml/agentic-rag|Agentic RAG]] — agent chooses hop strategy
- [[wiki/prompt-engineering/self-ask-technique|Self-Ask Technique]] — prompt-level chain of retrieval
- [[wiki/ai-ml/grounded-generation|Grounded Generation]] — evidence chaining end goal
