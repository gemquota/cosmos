---
type: "concept"
title: "MongoDB"
description: "Document-oriented NoSQL database storing flexible BSON documents with horizontal scaling"
tags: ["mongodb", "nosql", "document-db", "database", "data"]
timestamp: "2026-07-31T00:00:00Z"
status: "stub"
---

# MongoDB

## Summary
MongoDB is a document database storing JSON-like BSON documents with dynamic schemas. It scales horizontally via sharding and suits flexible, read-heavy data.

## Details
- Documents map naturally to JSON API payloads; embedded arrays avoid joins.
- Aggregation pipeline does server-side transforms; indexes matter for performance.
- The existing `data-storage/entities/mongodb` entity already notes mykb evaluations of document stores.

## Related
- [[wiki/devops-infra/postgresql|PostgreSQL]] — relational alternative with JSONB
- [[wiki/devops-infra/sharding|Sharding]] — horizontal scaling model
- [[wiki/devops-infra/database-indexing|Database Indexing]] — query performance
- [[wiki/devops-infra/backups|Backups]] — operational durability
- [[wiki/api-protocols/json-schema|JSON Schema]] — document shape validation
