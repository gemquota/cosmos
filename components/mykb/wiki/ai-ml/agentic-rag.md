---
type: "concept"
title: "Agentic RAG"
description: "Retrieval-augmented generation where an agent decides when, what, and how often to retrieve"
tags: ["rag", "agents", "retrieval"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Agentic RAG

## Summary
Retrieval-augmented generation where an agent decides when, what, and how often to retrieve

## Details
- The agent plans retrieval steps, picks tools, and iterates with the retrieved context.
- Improves answers on multi-hop or ambiguous queries versus one-shot RAG.
- Adds cost and latency, so retrieval should be gated by need.
- Bridges classic RAG pipelines and full autonomous agents.

## Related
- [[wiki/data-storage/retrieval-augmented-generation|Retrieval-Augmented Generation]] — baseline pattern it extends
- [[wiki/ai-ml/multi-hop-retrieval|Multi-Hop Retrieval]] — query style it handles
- [[wiki/ai-ml/query-transformations|Query Transformations]] — agentic query rewriting
- [[wiki/llm-agents/tool-use-function-calling|Tool Use and Function Calling]] — retrieval as a tool
- [[wiki/prompt-engineering/agentic-context-crafting|Agentic Context Crafting]] — context assembly loop
