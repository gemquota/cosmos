---
type: "concept"
title: "Semantic Search"
description: "Retrieval that matches meaning rather than surface keywords using embeddings or structured semantics"
tags: ["search", "semantic", "embeddings", "retrieval", "nlp"]
timestamp: "2026-07-31T00:00:00Z"
status: "growing"
source: ["https://en.wikipedia.org/wiki/Semantic_search"]
---

# Semantic Search

## Summary
Semantic search retrieves items by meaning: a query about 'memory techniques' can surface a note titled 'spaced repetition practice' with no shared words. It complements lexical search and is central to modern RAG. mykb exposes semantic search alongside TF-IDF so queries generalize beyond literal terms.

## Details
- **How it works** — encode query and documents as embeddings, then run nearest-neighbour search; optionally rerank with a cross-encoder.
- **Lexical vs semantic** — BM25 matches tokens (precise, fast, good for names and codes); semantic search matches meaning (better for paraphrase and conceptual recall).
- **Quality factors** — embedding model choice, chunk granularity, query reformulation, and reranking dominate end-to-end quality.
- **Worked example** — query 'how does RSIS3 consolidate memory?' is embedded and matched against wiki pages; a page on memory consolidation ranks high despite different wording.
- **Failure modes** — semantic search can miss exact identifiers ('FAISS 1.2.0') and over-generalize; hybrid search fixes this by blending lexical hits.
- **mykb relevance** — the daemon merges embedding hits with TF-IDF hits so both literal and conceptual recall are available to RSIS3.

## Related
- [[wiki/data-storage/embeddings|Embeddings]] — the vectors semantic search matches on
- [[wiki/data-storage/hybrid-search|Hybrid Search]] — lexical plus semantic retrieval combined
- [[wiki/data-storage/tf-idf|TF-IDF]] — the classic lexical baseline semantic search improves on
- [[wiki/data-storage/vector-databases|Vector Databases]] — infrastructure behind embedding search
- [[wiki/meta-learning/colbert|ColBERT]] — late-interaction model that boosts semantic ranking
- [[wiki/meta-learning/sentence-transformers|Sentence Transformers]] — typical encoder for semantic search
- [[wiki/memory/README|Memory Layer]] — the layer mykb semantic search serves
- [[wiki/concepts/mykb-analysis|Mykb Analysis]] — analyzes mykb's semantic retrieval design
