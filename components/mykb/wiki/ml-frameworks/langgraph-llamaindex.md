---
type: "entity"
title: "LangGraph and LlamaIndex"
description: "Frameworks for graph-structured agent state and data-centric RAG pipelines respectively"
tags: ["llamaindex", "rag", "agents"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# LangGraph and LlamaIndex

## Summary
Frameworks for graph-structured agent state and data-centric RAG pipelines respectively

## Details
- LangGraph models agents as explicit state graphs with checkpointing and human interrupts.
- LlamaIndex focuses on loading, indexing, and querying documents for RAG.
- Both compose with LangChain primitives but emphasize control and data.
- Together they cover durable orchestration and retrieval plumbing.

## Related
- [[wiki/ml-frameworks/langchain-framework|LangChain Framework]] — shared ecosystem
- [[wiki/agent-systems/agent-state-machines|Agent State Machines]] — what LangGraph encodes
- [[wiki/data-storage/retrieval-augmented-generation|Retrieval-Augmented Generation]] — LlamaIndex core use case
- [[wiki/ai-ml/agentic-rag|Agentic RAG]] — their combined pattern
- [[wiki/ai-ml/parent-document-retrieval|Parent Document Retrieval]] — indexing strategy LlamaIndex supports
