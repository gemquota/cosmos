---
type: "entity"
title: "MongoDB Data Modeling"
description: "Embedding vs referencing documents for performance"
tags: ["mongodb", "data-modeling", "documents", "schema"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://www.mongodb.com/docs/manual/data-modeling/", "https://en.wikipedia.org/wiki/MongoDB"]
---

# MongoDB Data Modeling

## Summary

MongoDB modeling decides how to structure documents: embed related data or reference it.
The choice follows access patterns, not normalization theory.
Good models minimize round trips and keep documents bounded.
MongoDB modeling is iterative: model, measure, and adjust as access patterns become clear.

## Details

- Embed for reads of related data that change together.
- Reference for shared, frequently updated, or large data.
- Arrays and subdocuments model one-to-many and many-to-many.
- Indexes must match the query patterns you actually run.
- Schema validation adds discipline without rigidity.
- Avoid unbounded arrays; they break performance and document size.
- Index design follows the queries you actually run.
- MongoDB modeling rewards deliberate, query-driven design over relational habits.

## Related

- [[wiki/data-storage/document-databases|Document Databases]] — document model
- [[wiki/data-storage/json-and-semi-structured-data|JSON and Semi-Structured Data]] — JSON
- [[wiki/infrastructure/mongodb-atlas-and-replica-sets|Mongodb Atlas And Replica Sets]] — operations
- [[wiki/data-storage/document-stores|Document Stores]] — existing note
- [[wiki/data-storage/indexing-strategies-revisited|Indexing Strategies Revisited]] — indexes
- [[wiki/data-storage/data-quality-dimensions|Data Quality Dimensions]] — quality dimensions
- [[wiki/data-storage/data-observability-and-monitoring|Data Observability and Monitoring]] — observability
- [[wiki/data-storage/data-testing-frameworks|Data Testing Frameworks]] — testing
- [[wiki/data-storage/feature-stores-and-ml-features|Feature Stores and ML Features]] — ML features
- [[wiki/data-storage/data-contracts-and-agreements|Data Contracts and Agreements]] — data contracts
- [[wiki/data-storage/incremental-loading-strategies|Incremental Loading Strategies]] — incremental loading
- [[wiki/data-storage/schema-evolution-in-streams|Schema Evolution In Streams]] — schema evolution
- [[wiki/data-storage/data-warehouse|Data Warehouse]] — warehouse reference

