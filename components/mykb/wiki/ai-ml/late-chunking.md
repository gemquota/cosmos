---
type: "concept"
title: "Late Chunking"
description: "Embedding long contexts as a whole and then deriving per-chunk embeddings from the shared representation"
tags: ["embeddings", "rag", "chunking"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Late Chunking

## Summary
Embedding long contexts as a whole and then deriving per-chunk embeddings from the shared representation

## Details
- Encodes the full document, then pools the resulting token vectors into chunk vectors.
- Keeps contextual information that per-chunk encoding loses.
- Requires models that expose token-level embeddings.
- Improves retrieval quality on context-dependent passages.

## Related
- [[wiki/ai-ml/contextual-retrieval|Contextual Retrieval]] — contrasting approach
- [[wiki/data-storage/chunking-strategies|Chunking Strategies]] — the pipeline it changes
- [[wiki/ai-ml/embeddings-and-vector-search|Embeddings and Vector Search]] — embedding family
- [[wiki/ai-ml/small-to-big-retrieval|Small-to-Big Retrieval]] — retrieval granularity strategies
- [[wiki/ai-ml/parent-document-retrieval|Parent Document Retrieval]] — context preservation family
