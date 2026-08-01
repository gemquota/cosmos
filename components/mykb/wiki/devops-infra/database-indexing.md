---
type: "concept"
title: "Database Indexing"
description: "Data structures that accelerate lookups and scans at the cost of write overhead and storage"
tags: ["indexing", "database", "performance", "sql", "query"]
timestamp: "2026-07-31T00:00:00Z"
status: "stub"
---

# Database Indexing

## Summary
Indexes are auxiliary data structures (B-trees, hash tables, GiST) that let the database find rows without full scans. They trade write cost and storage for read speed.

## Details
- B-tree is the default for range queries; hash indexes suit equality; covering indexes serve whole queries.
- Composite index column order matters: leftmost-prefix rule governs usability.
- Over-indexing slows writes and bloats storage; measure with `EXPLAIN`.

## Related
- [[wiki/devops-infra/query-planning|Query Planning]] — how indexes get chosen
- [[wiki/devops-infra/postgresql|PostgreSQL]] — index types and tuning
- [[wiki/devops-infra/connection-pooling|Connection Pooling]] — complements read scaling
- [[wiki/api-protocols/json-schema|JSON Schema]] — validated fields can be indexed
- [[wiki/concepts/mykb-research-report|Mykb Research Report]] — TF-IDF inverted index notes
