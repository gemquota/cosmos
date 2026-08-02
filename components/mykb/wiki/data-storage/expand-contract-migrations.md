---
type: "concept"
title: "Expand-Contract Migrations"
description: "Phased zero-downtime schema change patterns"
tags: ["expand-contract", "zero-downtime", "schema-migrations", "releases"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://martinfowler.com/articles/evodb.html", "https://www.postgresql.org/docs/current/ddl.html"]
---

# Expand-Contract Migrations

## Summary
Expand-contract (also expand-migrate-contract) changes a schema in phases so old and new code keep working during deployment: first add the new structure while keeping the old, migrate data and switch readers, then remove the obsolete structure. It is the standard pattern for zero-downtime DDL on live tables.

## Details
- **Expand** — add the new column, table, or index while the old path still serves traffic; this phase must be backward compatible so running code is unaffected.
- **Migrate** — backfill and copy data, deploy the new code path, and switch traffic; dual-writes (writing both old and new structures) keep the systems in sync during the transition.
- **Contract** — once no reader or writer uses the old structure, drop it in a later release; premature contraction breaks the guarantee, so a full release cycle between phases is common.
- **Dual-write discipline** — the application must update both representations atomically or accept replayable queues; shadow reads compare old and new results before the switch.
- **When it applies** — column renames, format changes, shard-key changes, and table splits; for simple additive changes a single migration is enough, so expand-contract is reserved for breaking changes.

## Related
- [[wiki/data-storage/schema-migrations|Schema Migrations]] — versioned DDL mechanics
- [[wiki/data-storage/schema-evolution|Schema Evolution]] — compatibility rules behind the phases
- [[wiki/data-storage/backfilling|Backfilling]] — migrating data between structures
- [[wiki/data-storage/idempotent-ingestion|Idempotent Ingestion]] — safe dual-write retries
- [[wiki/devops-infra/rollback-plans|Rollback Plans]] — keeping the old path viable
