---
type: "concept"
title: "ChromaDB"
description: "Embedded, Python-first vector database popular for local RAG prototypes"
tags: ["chromadb", "vector-database", "python", "local"]
timestamp: "2026-07-31T00:00:00Z"
status: "stub"
---

# ChromaDB

## Summary
ChromaDB is an open-source, Python-first vector database that runs embedded or as a client-server, designed for quick RAG experimentation. Its API is minimal: `add`, `query`, and filters over metadata.

## Details
- **Usage** — `collection.add(ids, documents, metadatas, embeddings)` then `collection.query(query_texts, n_results)`.
- **Trade-off** — simplicity and fast iteration vs scale and advanced indexing; persistent mode writes to disk.
- **Agent relevance** — ChromaDB is the fastest path for mykb experiments with embedding search over wiki notes.

## Related
- [[wiki/data-storage/vector-databases|Vector Databases]] — the category
- [[wiki/data-storage/embeddings|Embeddings]] — documents are embedded on add
- [[wiki/data-storage/metadata-filtering|Metadata Filtering]] — filters over stored metadatas
- [[wiki/data-storage/retrieval-augmented-generation|Retrieval-Augmented Generation]] — ChromaDB's typical use case
- [[wiki/data-storage/00-index|Data Storage]] — vector database family
