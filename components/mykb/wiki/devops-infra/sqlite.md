---
type: "concept"
title: "SQLite"
description: "Embedded, zero-configuration SQL database stored in a single file"
tags: ["sqlite", "database", "embedded", "sql", "local"]
timestamp: "2026-07-31T00:00:00Z"
status: "stub"
---

# SQLite

## Summary
SQLite is an embedded SQL database stored in one file with no server process. It is the most deployed database engine in the world and ideal for local state, prototypes, and single-node tools.

## Details
- Zero-config, transactional (ACID), and durable via WAL mode; full SQL support.
- Fits mykb's local index and RSIS3 state files; decision records note SQLite for local databases.
- Limitations: single-writer concurrency — choose Postgres when concurrent writers scale up.

## Related
- [[wiki/devops-infra/transactions|Transactions]] — ACID guarantees
- [[wiki/devops-infra/postgresql|PostgreSQL]] — server-based scale-up path
- [[wiki/devops-infra/acid|ACID]] — durability semantics
- [[wiki/devops-infra/backups|Backups]] — file-level snapshot simplicity
- [[wiki/decisions/decided-to-use-sqlite-for-the-local-database-because-it-re|SQLite Decision]] — local database rationale
- [[wiki/devops-infra/observability|Observability]] — query timing for local state
