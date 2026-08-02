---
type: "concept"
title: "Small-to-Big Retrieval"
description: "Retrieval strategy that searches small chunks then feeds bigger blocks or the whole document to the model"
tags: ["rag", "retrieval", "chunks"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Small-to-Big Retrieval

## Summary
Retrieval strategy that searches small chunks then feeds bigger blocks or the whole document to the model

## Details
- The index stores small granular units; the context sent to the model is larger.
- Improves recall on precise queries while keeping generation context rich.
- Implementation varies: parent docs, sibling merge, or sliding windows.
- Related to parent-document-retrieval and often used interchangeably.

## Related
- [[wiki/ai-ml/parent-document-retrieval|Parent Document Retrieval]] — canonical variant
- [[wiki/prompt-engineering/context-window-management|Context Window Management]] — fits bigger units into context
- [[wiki/data-storage/chunking-strategies|Chunking Strategies]] — unit size decisions
- [[wiki/ai-ml/recursive-retrieval|Recursive Retrieval]] — hierarchical traversal
- [[wiki/ai-ml/agentic-rag|Agentic RAG]] — agent chooses granularity
