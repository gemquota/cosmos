---
type: "entity"
title: "MongoDB"
description: "Document-oriented NoSQL database storing flexible BSON documents with horizontal scaling"
tags: ["mongodb", "nosql", "document-db", "database", "data"]
timestamp: "2026-07-31T00:00:00Z"
status: "growing"
---

# MongoDB

## Summary
MongoDB is a document database storing JSON-like BSON documents with dynamic schemas. It scales horizontally via sharding and suits flexible, read-heavy data where the shape of records evolves faster than a fixed relational schema would allow.

## Details
- Documents map naturally to JSON API payloads; embedded arrays avoid joins.
- Aggregation pipeline does server-side transforms; indexes matter for performance.
- The existing `data-storage/entities/mongodb` entity already notes mykb evaluations of document stores.
- Replica sets provide high availability: a primary accepts writes and secondaries replicate them, with automatic failover when the primary is lost.
- Sharding distributes data across clusters by a shard key; choosing that key well keeps writes and reads balanced instead of hot-spotting on one node.
- Queries support equality, range, and text search, and compound indexes cover common access patterns; an explain plan exposes whether an index is being used.
- Schema validation and unique indexes can be applied where guarantees are needed, compensating for the otherwise flexible document model.
- Atomic operations are scoped to a single document, so multi-document consistency is achieved through patterns like the two-phase commit or outbox tables.
- For read-heavy workloads, secondary reads and caching layers reduce primary load, while TTL indexes expire old data without application code.
- Backup and restore are operationally distinct from relational dumps: mongodump exports BSON, and file-system snapshots or Atlas continuous backups cover recovery point objectives.
- Horizontal scale-out is not automatic: capacity planning, shard-key selection, and rebalancing are operational responsibilities the team must own.
- Change streams expose database changes as events, enabling reactive integrations and outbox-style consumers without polling.
- Read preference settings trade consistency for latency and must be chosen per workload, not set once globally.

## Related
- [[wiki/devops-infra/postgresql|PostgreSQL]] — relational alternative with JSONB
- [[wiki/devops-infra/sharding|Sharding]] — horizontal scaling model
- [[wiki/devops-infra/database-indexing|Database Indexing]] — query performance
- [[wiki/devops-infra/backups|Backups]] — operational durability
- [[wiki/api-protocols/json-schema|JSON Schema]] — document shape validation
