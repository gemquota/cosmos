---
type: "entity"
title: "PostgreSQL"
description: "Advanced open-source relational database with strong consistency, extensions, and SQL standards"
tags: ["postgresql", "database", "sql", "relational", "data"]
timestamp: "2026-07-31T00:00:00Z"
status: "stub"
---

# PostgreSQL

## Summary
PostgreSQL is the most advanced open-source relational database: ACID transactions, full SQL, JSON, and rich extensions. It is the default choice for transactional workloads needing reliability.

## Details
- Extensions like PostGIS, pgvector (embeddings), and TimescaleDB broaden its reach — pgvector makes it viable for mykb-style semantic search.
- MVCC concurrency, WAL replication, and point-in-time recovery are built in.
- ORM support: SQLAlchemy, Prisma, Drizzle, TypeORM all target it first.

## Related
- [[wiki/devops-infra/acid|ACID]] — transactional guarantees
- [[wiki/devops-infra/isolation-levels|Isolation Levels]] — concurrency semantics
- [[wiki/tooling/sqlalchemy|SQLAlchemy]] — Python ORM
- [[wiki/js-ts-ecosystem/prisma|Prisma]] — TypeScript ORM
- [[wiki/devops-infra/replication|Replication]] — high availability
- [[wiki/devops-infra/backups|Backups]] — durability practice
- [[wiki/devops-infra/observability|Observability]] — pg_stat monitoring and slow-query logs
