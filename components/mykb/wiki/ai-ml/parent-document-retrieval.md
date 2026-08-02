---
type: "concept"
title: "Parent Document Retrieval"
description: "Retrieving small chunks for precision but returning the larger parent passage for generation"
tags: ["rag", "chunking", "retrieval"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Parent Document Retrieval

## Summary
Retrieving small chunks for precision but returning the larger parent passage for generation

## Details
- Small child chunks are embedded and searched; hits map back to bigger parent sections.
- Balances semantic precision with sufficient context for the LLM.
- Adds a mapping layer between index chunks and returned units.
- A standard production RAG refinement.

## Related
- [[wiki/ai-ml/small-to-big-retrieval|Small-to-Big Retrieval]] — same idea at another granularity
- [[wiki/ai-ml/late-chunking|Late Chunking]] — embedding-level variant
- [[wiki/ai-ml/contextual-retrieval|Contextual Retrieval]] — context-in-chunk variant
- [[wiki/ai-ml/recursive-retrieval|Recursive Retrieval]] — nested structure handling
- [[wiki/data-storage/retrieval-augmented-generation|Retrieval-Augmented Generation]] — overall pattern
