---
type: "concept"
title: "Contextual Retrieval"
description: "Chunking and indexing method that prepends chunk-level context so each embedding stands alone"
tags: ["rag", "chunking", "embeddings"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Contextual Retrieval

## Summary
Chunking and indexing method that prepends chunk-level context so each embedding stands alone

## Details
- Each chunk is augmented with surrounding document context before embedding.
- Reduces ambiguity when chunks are retrieved out of sequence.
- Works with both embedding similarity and BM25.
- Costs extra tokens at indexing time but improves hit rate.

## Related
- [[wiki/data-storage/chunking-strategies|Chunking Strategies]] — chunk design it builds on
- [[wiki/ai-ml/late-chunking|Late Chunking]] — alternative that defers splitting
- [[wiki/ai-ml/parent-document-retrieval|Parent Document Retrieval]] — related context-preserving strategy
- [[wiki/ai-ml/small-to-big-retrieval|Small-to-Big Retrieval]] — retrieve small, return big
- [[wiki/ai-ml/hybrid-search-systems|Hybrid Search Systems]] — lexical partner for contextual vectors
