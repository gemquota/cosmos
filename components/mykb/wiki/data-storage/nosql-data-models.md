---
type: "concept"
title: "NoSQL Data Models"
description: "Key-value, document, wide-column, graph, and search models"
tags: ["nosql", "data-models", "databases", "scaling"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://en.wikipedia.org/wiki/NoSQL", "https://en.wikipedia.org/wiki/Document-oriented_database"]
---

# NoSQL Data Models

## Summary

NoSQL databases trade relational rigidity for scale, flexibility, or specialized query power.
The main models are key-value, document, wide-column, graph, and search.
Model choice should follow access patterns, not fashion.
The models differ in what they optimize: consistency, flexibility, scale, or traversal.

## Details

- Key-value: simple get/put at massive scale (Redis, DynamoDB).
- Document: JSON-centric with rich queries (MongoDB).
- Wide-column: sparse rows and high write throughput (Cassandra, ScyllaDB).
- Graph: relationship traversal (Neo4j); search: inverted indexes (Elasticsearch).
- Polyglot persistence uses several models where each fits best.
- Polyglot persistence is a strategy, not an accident.
- Revisit model choice as access patterns change.
- The right NoSQL model is the one that matches your access patterns and operational constraints.

## Related

- [[wiki/data-storage/document-databases|Document Databases]] — document model
- [[wiki/data-storage/key-value-stores|Key Value Stores]] — KV model
- [[wiki/data-storage/wide-column-stores|Wide Column Stores]] — column model
- [[wiki/data-storage/document-stores|Document Stores]] — existing note
- [[wiki/data-storage/graph-databases-timeseries-databases|Graph and Time-Series Databases]] — graph model
- [[wiki/data-storage/data-quality-dimensions|Data Quality Dimensions]] — quality dimensions
- [[wiki/data-storage/data-observability-and-monitoring|Data Observability and Monitoring]] — observability
- [[wiki/data-storage/data-testing-frameworks|Data Testing Frameworks]] — testing
- [[wiki/data-storage/feature-stores-and-ml-features|Feature Stores and ML Features]] — ML features
- [[wiki/data-storage/data-contracts-and-agreements|Data Contracts and Agreements]] — data contracts
- [[wiki/data-storage/incremental-loading-strategies|Incremental Loading Strategies]] — incremental loading
- [[wiki/data-storage/schema-evolution-in-streams|Schema Evolution In Streams]] — schema evolution
- [[wiki/data-storage/streaming-sinks-and-sources|Streaming Sinks And Sources]] — streams
- [[wiki/data-storage/data-warehouse|Data Warehouse]] — warehouse reference

