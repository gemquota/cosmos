---
type: "concept"
title: "Document Databases"
description: "JSON-first databases for flexible, developer-friendly data"
tags: ["document-databases", "mongodb", "json", "nosql"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://www.mongodb.com/docs/manual/", "https://en.wikipedia.org/wiki/Document-oriented_database"]
---

# Document Databases

## Summary

Document databases store records as JSON-like documents with flexible schemas.
They map naturally to application objects and evolve easily.
MongoDB is the archetype, with rich indexing and aggregation.
Document databases win when the data naturally nests and reads dominate writes.

## Details

- Documents embed related data, reducing joins.
- Indexes support queries; aggregation pipelines process server-side.
- Replica sets and sharding scale reads and writes.
- Flexible schema demands discipline: validation and migrations matter.
- Modeling (embed vs reference) drives performance more than hardware.
- Aggregation pipelines move logic server-side for efficiency.
- Modeling reviews with the team prevent schema drift.
- Document databases keep developer velocity high when schemas evolve quickly and reads dominate.

## Related

- [[wiki/data-storage/mongodb-data-modeling|Mongodb Data Modeling]] — modeling
- [[wiki/data-storage/json-and-semi-structured-data|Json And Semi Structured Data]] — JSON
- [[wiki/infrastructure/mongodb-atlas-and-replica-sets|Mongodb Atlas And Replica Sets]] — operations
- [[wiki/data-storage/document-stores|Document Stores]] — existing note
- [[wiki/data-storage/schema-evolution|Schema Evolution]] — evolution
- [[wiki/data-storage/data-quality-dimensions|Data Quality Dimensions]] — quality dimensions
- [[wiki/data-storage/data-observability-and-monitoring|Data Observability and Monitoring]] — observability
- [[wiki/data-storage/data-testing-frameworks|Data Testing Frameworks]] — testing
- [[wiki/data-storage/feature-stores-and-ml-features|Feature Stores And Ml Features]] — ML features
- [[wiki/data-storage/data-contracts-and-agreements|Data Contracts and Agreements]] — data contracts
- [[wiki/data-storage/incremental-loading-strategies|Incremental Loading Strategies]] — incremental loading
- [[wiki/data-storage/schema-evolution-in-streams|Schema Evolution In Streams]] — schema evolution

