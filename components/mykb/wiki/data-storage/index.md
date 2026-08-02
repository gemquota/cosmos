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

- [CACHE](entities/cache.md)

## Concepts

- [ACID Transactions](acid-transactions.md) — ACID Transactions
- [B-Tree Indexing](b-tree-indexing.md) — B-Tree Indexing
- [Backfilling](backfilling.md) — Backfilling
- [Backpressure](backpressure.md) — Backpressure
- [Backup Strategies](backup-strategies.md) — Backup Strategies
- [Batch vs Stream Processing](batch-vs-stream-processing.md) — Batch vs Stream Processing
- [Bitmap Indexes](bitmap-indexes.md) — Bitmap Indexes
- [BM25](bm25.md) — BM25
- [Buffer Pool Management](buffer-pool-management.md) — Buffer Pool Management
- [Cache Eviction Policies](cache-eviction-policies.md) — Cache Eviction Policies
- [Caching Strategies](caching-strategies.md) — Caching Strategies
- [CAP Theorem](cap-theorem.md) — CAP Theorem
- [Change Data Capture](cdc-change-data-capture.md) — Change Data Capture
- [ChromaDB](chromadb.md) — ChromaDB
- [Chunking Strategies](chunking-strategies.md) — Chunking Strategies
- [Clustered Tables](clustered-tables.md) — Clustered Tables
- [Columnar Storage](columnar-storage.md) — Columnar Storage
- [Composite Indexes](composite-indexes.md) — Composite Indexes
- [Compression Codecs](compression-codecs.md) — Compression Codecs
- [Consistency Models](consistency-models.md) — Consistency Models
- [Consistent Hashing](consistent-hashing.md) — Consistent Hashing
- [Content-Addressable Storage](content-addressable-storage.md) — Content-Addressable Storage
- [Cosine Similarity](cosine-similarity.md) — Cosine Similarity
- [Cost-Based Query Optimization](cost-based-query-optimization.md) — Cost-Based Query Optimization
- [Covering Indexes](covering-indexes.md) — Covering Indexes
- [Crash Recovery](crash-recovery.md) — Crash Recovery
- [CRDTs](crdts.md) — CRDTs
- [Data Contracts](data-contracts.md) — Data Contracts
- [Data Federation](data-federation.md) — Data Federation
- [Data Lake](data-lake.md) — Data Lake
- [Data Lifecycle Management](data-lifecycle-management.md) — Data Lifecycle Management
- [Data Lineage](data-lineage.md) — Data Lineage
- [Data Modeling](data-modeling.md) — Data Modeling
- [Data Observability](data-observability.md) — Data Observability
- [Data Pipeline Orchestration](data-pipeline-orchestration.md) — Data Pipeline Orchestration
- [Data Profiling](data-profiling.md) — Data Profiling
- [Data Quality Checks](data-quality-checks.md) — Data Quality Checks
- [Data Versioning](data-versioning.md) — Data Versioning
- [Data Warehouse](data-warehouse.md) — Data Warehouse
- [Database Constraints](database-constraints.md) — Database Constraints
- [Database Normalization](database-normalization.md) — Database Normalization
- [Database Performance Monitoring](database-performance-monitoring.md) — Database Performance Monitoring
- [Dead Letter Queues](dead-letter-queues.md) — Dead Letter Queues
- [Deadlock Detection](deadlock-detection.md) — Deadlock Detection
- [Deduplication](deduplication.md) — Deduplication
- [Denormalization](denormalization.md) — Denormalization
- [Dimensional Modeling](dimensional-modeling.md) — Dimensional Modeling
- [Disaster Recovery](disaster-recovery.md) — Disaster Recovery
- [Distributed Transactions](distributed-transactions.md) — Distributed Transactions
- [Document Stores](document-stores.md) — Document Stores
- [Dot Product](dot-product.md) — Dot Product
- [Edit Distance](edit-distance.md) — Edit Distance
- [Elasticsearch](elasticsearch.md) — Elasticsearch
- [Embeddings](embeddings.md) — Embeddings
- [Entity Resolution](entity-resolution.md) — Entity Resolution
- [ETL vs ELT](etl-vs-elt.md) — ETL vs ELT
- [Euclidean Distance](euclidean-distance.md) — Euclidean Distance
- [Event Streaming Platforms](event-streaming-platforms.md) — Event Streaming Platforms
- [Exactly-Once Semantics](exactly-once-semantics.md) — Exactly-Once Semantics
- [Expand-Contract Migrations](expand-contract-migrations.md) — Expand-Contract Migrations
- [FAISS](faiss.md) — FAISS
- [Hash Indexes](hash-indexes.md) — Hash Indexes
- [HNSW](hnsw.md) — HNSW
- [Hybrid Search](hybrid-search.md) — Hybrid Search
- [Idempotent Ingestion](idempotent-ingestion.md) — Idempotent Ingestion
- [In-Memory Databases](in-memory-databases.md) — In-Memory Databases
- [Incremental Loading](incremental-loading.md) — Incremental Loading
- [Index Maintenance](index-maintenance.md) — Index Maintenance
- [Inverted Index](inverted-index.md) — Inverted Index
- [IVF Index](ivf.md) — IVF Index
- [Jaccard Similarity](jaccard-similarity.md) — Jaccard Similarity
- [Join Algorithms](join-algorithms.md) — Join Algorithms
- [JSON-LD](json-ld.md) — JSON-LD
- [Kappa Architecture](kappa-architecture.md) — Kappa Architecture
- [Key-Value Stores](key-value-stores.md) — Key-Value Stores
- [Knowledge Graph](knowledge-graph.md) — Knowledge Graph
- [Lakehouse Architecture](lakehouse-architecture.md) — Lakehouse Architecture
- [Lambda Architecture](lambda-architecture.md) — Lambda Architecture
- [Latent Dirichlet Allocation](latent-dirichlet-allocation.md) — Latent Dirichlet Allocation
- [Latent Semantic Analysis](latent-semantic-analysis.md) — Latent Semantic Analysis
- [Leaderless Replication](leaderless-replication.md) — Leaderless Replication
- [Lemmatization](lemmatization.md) — Lemmatization
- [Locality-Sensitive Hashing](locality-sensitive-hashing.md) — Locality-Sensitive Hashing
- [Lock Granularity](lock-granularity.md) — Lock Granularity
- [Log Collection & Aggregation](log-collection-and-aggregation.md) — Log Collection & Aggregation
- [LSM Trees](lsm-trees.md) — LSM Trees
- [Lucene](lucene.md) — Lucene
- [Massively Parallel Processing](massively-parallel-processing.md) — Massively Parallel Processing
- [Materialized Views](materialized-views.md) — Materialized Views
- [Message Queues](message-queues.md) — Message Queues
- [Metadata Filtering](metadata-filtering.md) — Metadata Filtering
- [Milvus](milvus.md) — Milvus
- [MinHash](minhash.md) — MinHash
- [Multi-Leader Replication](multi-leader-replication.md) — Multi-Leader Replication
- [Multiversion Concurrency Control](multiversion-concurrency-control.md) — Multiversion Concurrency Control
- [N-grams](n-grams.md) — N-grams
- [Named Entity Recognition](named-entity-recognition.md) — Named Entity Recognition
- [Object Storage](object-storage.md) — Object Storage
- [OLAP vs OLTP](olap-vs-oltp.md) — OLAP vs OLTP
- [Open Knowledge Format](open-knowledge-format.md) — Open Knowledge Format
- [Open Table Formats](open-table-formats.md) — Open Table Formats
- [Optimistic Concurrency Control](optimistic-concurrency-control.md) — Optimistic Concurrency Control
- [Partial Indexes](partial-indexes.md) — Partial Indexes
- [Partition Pruning](partition-pruning.md) — Partition Pruning
- [Pinecone](pinecone.md) — Pinecone
- [Point-in-Time Recovery](point-in-time-recovery.md) — Point-in-Time Recovery
- [PostgreSQL tsvector](postgres-tsvector.md) — PostgreSQL tsvector
- [Product Quantization](product-quantization.md) — Product Quantization
- [Property Graph](property-graph.md) — Property Graph
- [Qdrant](qdrant.md) — Qdrant
- [Query Tuning](query-tuning.md) — Query Tuning
- [Quorum Protocols](quorum-protocols.md) — Quorum Protocols
- [Raft Consensus](raft-consensus.md) — Raft Consensus
- [RDF](rdf.md) — RDF
- [Reciprocal Rank Fusion](reciprocal-rank-fusion.md) — Reciprocal Rank Fusion
- [Record Linkage](record-linkage.md) — Record Linkage
- [Replication Strategies](replication-strategies.md) — Replication Strategies
- [Retrieval-Augmented Generation](retrieval-augmented-generation.md) — Retrieval-Augmented Generation
- [RPO and RTO](rpo-and-rto.md) — RPO and RTO
- [Schema Evolution](schema-evolution.md) — Schema Evolution
- [Schema Migrations](schema-migrations.md) — Schema Migrations
- [Schema-on-Read vs Schema-on-Write](schema-on-read.md) — Schema-on-Read vs Schema-on-Write
- [Semantic Search](semantic-search.md) — Semantic Search
- [Sharding Strategies](sharding-strategies.md) — Sharding Strategies
- [SimHash](simhash.md) — SimHash
- [Slowly Changing Dimensions](slowly-changing-dimensions.md) — Slowly Changing Dimensions
- [SPARQL](sparql.md) — SPARQL
- [Spatial Indexes](spatial-indexes.md) — Spatial Indexes
- [SQL Engine Architecture](sql-engines.md) — SQL Engine Architecture
- [SQLite FTS5](sqlite-fts5.md) — SQLite FTS5
- [Stemming](stemming.md) — Stemming
- [Stopwords](stopwords.md) — Stopwords
- [Storage Engines](storage-engines.md) — Storage Engines
- [Storage Tiering](storage-tiering.md) — Storage Tiering
- [Stream Processing Engines](stream-processing-engines.md) — Stream Processing Engines
- [Stream Windowing](stream-windowing.md) — Stream Windowing
- [Surrogate vs Natural Keys](surrogate-keys.md) — Surrogate vs Natural Keys
- [Table Partitioning](table-partitioning.md) — Table Partitioning
- [TF-IDF](tf-idf.md) — TF-IDF
- [Time-Series Databases](time-series-databases.md) — Time-Series Databases
- [Tokenization](tokenization.md) — Tokenization
- [Topic Modeling](topic-modeling.md) — Topic Modeling
- [Transaction Isolation Levels](transaction-isolation-levels.md) — Transaction Isolation Levels
- [Triplestore](triplestore.md) — Triplestore
- [Two-Phase Commit](two-phase-commit.md) — Two-Phase Commit
- [Two-Phase Locking](two-phase-locking.md) — Two-Phase Locking
- [Vacuuming & Compaction](vacuuming-and-compaction.md) — Vacuuming & Compaction
- [Vector Databases](vector-databases.md) — Vector Databases
- [Vectorized Query Execution](vectorized-query-execution.md) — Vectorized Query Execution
- [Weaviate](weaviate.md) — Weaviate
- [Wide-Column Stores](wide-column-stores.md) — Wide-Column Stores
- [Write-Ahead Logging](write-ahead-logging.md) — Write-Ahead Logging
- [YAML Frontmatter](yaml-frontmatter.md) — YAML Frontmatter
