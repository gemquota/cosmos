---
type: "concept"
title: "Document Stores"
description: "JSON/BSON-oriented NoSQL databases"
tags: ["nosql", "document-database", "mongodb", "json"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://www.mongodb.com/docs/manual/core/document/", "https://docs.couchbase.com/server/current/learn/data/data.html"]
---

# Document Stores

## Summary
Document stores are NoSQL databases that persist self-describing documents — JSON, BSON, or XML — instead of rows in fixed tables. Each document can have its own structure, which makes them a natural fit for semi-structured data, content-heavy domains, and schemas that evolve quickly.

## Details
- **Data model** — a document is a nested key-value structure (fields, arrays, subdocuments) addressed by a unique `_id`; unlike a relational row, fields can vary between documents and nesting replaces joins for related data.
- **Querying** — queries match on field values, ranges, arrays, and text; MongoDB's query language and aggregation pipeline, Couchbase N1QL, and CouchDB views/Mango cover the spectrum from key lookups to SQL-like analytics.
- **Indexing** — document stores support single-field, compound, and multi-key (array) indexes plus text and geospatial indexes; query planners use them much like relational ones, so index selection still drives performance.
- **Consistency and transactions** — MongoDB supports multi-document ACID transactions on replica sets and sharded clusters; document stores generally follow the CAP trade-off, with replica-set writes acknowledged per configurable write concerns.
- **Scaling** — horizontal scaling is core: shard keys distribute documents across nodes, and the document model keeps most operations single-document, avoiding cross-shard joins.
- **When they win** — catalog, user-profile, content, and event-shaped data with heterogeneous fields; when data is highly relational with heavy multi-way joins, a relational store is usually the better fit.
- **Evolution** — schema validation is optional (MongoDB schema validation, Couchbase `$json-schema`), letting teams tighten structure gradually instead of forcing upfront migrations.

## Related
- [[wiki/data-storage/key-value-stores|Key-Value Stores]] — the simpler cousin
- [[wiki/data-storage/wide-column-stores|Wide-Column Stores]] — another columnar-ish NoSQL family
- [[wiki/data-storage/schema-evolution|Schema Evolution]] — the flexibility document stores buy
- [[wiki/data-storage/sharding-strategies|Sharding Strategies]] — scaling document workloads
- [[wiki/data-storage/object-storage|Object Storage]] — storing the raw documents at scale
