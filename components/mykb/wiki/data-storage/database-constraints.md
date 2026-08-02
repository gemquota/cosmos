---
type: "concept"
title: "Database Constraints"
description: "Primary keys, uniques, checks, and foreign-key enforcement"
tags: ["constraints", "referential-integrity", "schema", "databases"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://www.postgresql.org/docs/current/ddl-constraints.html", "https://dev.mysql.com/doc/refman/8.4/en/constraint-primary-key.html"]
---

# Database Constraints

## Summary
Constraints are declarative rules the engine enforces on every write: primary keys, unique keys, not-null, check predicates, and foreign keys. They are the cheapest integrity layer because enforcement is atomic with the write and immune to application bugs.

## Details
- **Primary key** — uniquely identifies a row and, in InnoDB, is the clustering key; Postgres creates a unique index plus not-null marks. Every table should have one.
- **Unique constraints** — guarantee no duplicate values; implemented as unique indexes, so they double as query accelerators. NULLs are exempt by default in most engines.
- **Check constraints** — boolean predicates validated per row, e.g., `CHECK (price >= 0)`; Postgres uses them for partial unique emulation and they can be `NOT VALID` then validated in bulk.
- **Foreign keys** — enforce referential integrity with `ON DELETE/ON UPDATE` actions (CASCADE, SET NULL, RESTRICT); InnoDB enforces them natively, while MySQL historically required both columns to be indexed; Postgres checks them with triggers internally.
- **Costs** — constraints add validation work and lock/trigger overhead on writes; foreign-key checks on hot child tables are a classic write bottleneck, sometimes mitigated by removing constraints and enforcing in the application — a trade-off that must be explicit.
- **Deferred constraints** — Postgres and Oracle support `DEFERRABLE INITIALLY DEFERRED`, letting multi-row operations validate at commit instead of per statement.

## Related
- [[wiki/data-storage/database-normalization|Database Normalization]] — constraints that encode relational design
- [[wiki/data-storage/data-modeling|Data Modeling]] — where constraints come from
- [[wiki/data-storage/data-quality-checks|Data Quality Checks]] — validating outside the database
- [[wiki/data-storage/surrogate-keys|Surrogate vs Natural Keys]] — choosing what the PK is
- [[wiki/devops-infra/postgresql|PostgreSQL]] — full constraint feature set
