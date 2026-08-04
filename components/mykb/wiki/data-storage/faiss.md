---
type: "entity"
title: "FAISS"
description: "Facebook's library for efficient similarity search and clustering of dense vectors"
tags: ["faiss", "ann", "similarity-search", "library"]
timestamp: "2026-07-31T00:00:00Z"
status: "growing"
---

# FAISS

## Summary
FAISS (Facebook AI Similarity Search) is the foundational open-source library for approximate nearest-neighbour search over dense vectors, written in C++ with Python bindings. IVF, HNSW, PQ, and scalar quantization — the ideas most vector databases standardize on — were made practical by FAISS.

## Details
- Capabilities: IVF (inverted-file) indexes cluster vectors and search the nearest clusters; HNSW builds navigable graph indexes; product quantization compresses vectors for memory-efficient search; scalar/quantization variants trade recall for size; GPU support accelerates index building and search; batch search and clustering are first-class.
- Role: FAISS is a library, not a server — callers manage index construction, persistence, and lifecycle themselves; it integrates with file formats and can be embedded in applications or wrapped by vector databases.
- Concrete example: a local FAISS index over mykb embeddings: embed each article, build an IVF or HNSW index, save it to disk, and query in-process for semantic retrieval; index rebuilds run on a schedule as articles change; a vector database would add serving, replication, and filtering at the cost of infrastructure.
- Failure modes: index staleness — queries run against an index that predates new articles; memory blowup with HNSW on large corpora (quantization mitigates); metric mismatch (index built with inner product, queried with cosine); rebuilding indexes synchronously, stalling the pipeline; persistence gaps — a rebuilt index lost on restart.
- Tradeoffs: FAISS gives full control and no server overhead at the cost of building and maintaining indexes yourself; the alternative, a vector database, manages lifecycle and serving but adds operations; the mature pattern is FAISS for in-process, single-node needs and a vector DB for scale.
- Operational notes: persist indexes, rebuild on a schedule, and verify the metric matches the embeddings' training objective.
- RSIS3 relevance: a local FAISS index over mykb embeddings gives in-process semantic search with full control — the right scale for the wiki today.

## Related
- [[wiki/data-storage/vector-databases|Vector Databases]] — FAISS is often the engine inside them
- [[wiki/data-storage/hnsw|HNSW]] — the graph index FAISS implements
- [[wiki/data-storage/ivf|IVF Index]] — the inverted-file index FAISS popularized
- [[wiki/data-storage/product-quantization|Product Quantization]] — compression FAISS supports
- [[wiki/data-storage/embeddings|Embeddings]] — the vectors FAISS searches
- [[wiki/data-storage/00-index|Data Storage]] — ANN libraries
