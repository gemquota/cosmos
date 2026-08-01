## Overview

The **Data Storage** domain (1 concepts) covers database and caching technologies. The preference is for lightweight, embedded solutions with production-ready alternatives.

### Key Technologies

- **SQLite** — primary embedded database for local development
- **PostgreSQL** — production database with full ACID compliance
- **SQLAlchemy** — Python ORM for database abstraction
- **Redis** — in-memory cache and message broker
- **Alembic** — database migration management

### Data Patterns

1. SQLite for single-user agent data and wiki storage
2. PostgreSQL for multi-user production services
3. Redis for session caching and rate limiting
4. ORM-first approach with SQLAlchemy model definitions


---

## Entities by Sub-Group

### Caching

- [CACHE](../../wiki/entities/cache.md)

## Concepts

- [BM25](bm25.md) — BM25
- [ChromaDB](chromadb.md) — ChromaDB
- [Chunking Strategies](chunking-strategies.md) — Chunking Strategies
- [Content-Addressable Storage](content-addressable-storage.md) — Content-Addressable Storage
- [Cosine Similarity](cosine-similarity.md) — Cosine Similarity
- [Data Versioning](data-versioning.md) — Data Versioning
- [Deduplication](deduplication.md) — Deduplication
- [Dot Product](dot-product.md) — Dot Product
- [Edit Distance](edit-distance.md) — Edit Distance
- [Elasticsearch](elasticsearch.md) — Elasticsearch
- [Embeddings](embeddings.md) — Embeddings
- [Entity Resolution](entity-resolution.md) — Entity Resolution
- [Euclidean Distance](euclidean-distance.md) — Euclidean Distance
- [FAISS](faiss.md) — FAISS
- [HNSW](hnsw.md) — HNSW
- [Hybrid Search](hybrid-search.md) — Hybrid Search
- [IVF Index](ivf.md) — IVF Index
- [Jaccard Similarity](jaccard-similarity.md) — Jaccard Similarity
- [JSON-LD](json-ld.md) — JSON-LD
- [Knowledge Graph](knowledge-graph.md) — Knowledge Graph
- [Latent Dirichlet Allocation](latent-dirichlet-allocation.md) — Latent Dirichlet Allocation
- [Latent Semantic Analysis](latent-semantic-analysis.md) — Latent Semantic Analysis
- [Lemmatization](lemmatization.md) — Lemmatization
- [Locality-Sensitive Hashing](locality-sensitive-hashing.md) — Locality-Sensitive Hashing
- [Lucene](lucene.md) — Lucene
- [Metadata Filtering](metadata-filtering.md) — Metadata Filtering
- [Milvus](milvus.md) — Milvus
- [MinHash](minhash.md) — MinHash
- [N-grams](n-grams.md) — N-grams
- [Named Entity Recognition](named-entity-recognition.md) — Named Entity Recognition
- [Open Knowledge Format](open-knowledge-format.md) — Open Knowledge Format
- [Pinecone](pinecone.md) — Pinecone
- [PostgreSQL tsvector](postgres-tsvector.md) — PostgreSQL tsvector
- [Product Quantization](product-quantization.md) — Product Quantization
- [Property Graph](property-graph.md) — Property Graph
- [Qdrant](qdrant.md) — Qdrant
- [RDF](rdf.md) — RDF
- [Reciprocal Rank Fusion](reciprocal-rank-fusion.md) — Reciprocal Rank Fusion
- [Record Linkage](record-linkage.md) — Record Linkage
- [Retrieval-Augmented Generation](retrieval-augmented-generation.md) — Retrieval-Augmented Generation
- [Semantic Search](semantic-search.md) — Semantic Search
- [SimHash](simhash.md) — SimHash
- [SPARQL](sparql.md) — SPARQL
- [SQLite FTS5](sqlite-fts5.md) — SQLite FTS5
- [Stemming](stemming.md) — Stemming
- [Stopwords](stopwords.md) — Stopwords
- [TF-IDF](tf-idf.md) — TF-IDF
- [Tokenization](tokenization.md) — Tokenization
- [Topic Modeling](topic-modeling.md) — Topic Modeling
- [Triplestore](triplestore.md) — Triplestore
- [Vector Databases](vector-databases.md) — Vector Databases
- [Weaviate](weaviate.md) — Weaviate
- [YAML Frontmatter](yaml-frontmatter.md) — YAML Frontmatter
