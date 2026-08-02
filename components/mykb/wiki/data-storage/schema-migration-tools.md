---
type: "concept"
title: "Schema Migration Tools"
description: "Version-controlled schema changes as code"
tags: ["migrations", "schema", "versioning", "tools"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://en.wikipedia.org/wiki/Schema_migration", "https://docs.liquibase.com/"]
---

# Schema Migration Tools

## Summary

Migration tools manage schema changes as versioned, repeatable scripts.
They apply changes consistently across environments.
Migrations-as-code brings CI/CD to databases.
Migration tools make schema state explicit and reproducible across environments.

## Details

- Versioned migrations run in order and record applied versions.
- Tools: Flyway, Liquibase, Alembic, Prisma, and ORM sync.
- Repeatable migrations handle idempotent changes.
- Branches and environments need merge-safe migration flows.
- Rollback and forward-fix policies matter for production.
- Ordered versioning prevents drift between dev and prod.
- Review generated SQL before applying to production.
- Migration tools make database changes deployable, reversible, and auditable.

## Related

- [[wiki/data-storage/flyway-and-liquibase|Flyway and Liquibase]] — tools
- [[wiki/data-storage/zero-downtime-migrations|Zero Downtime Migrations]] — zero downtime
- [[wiki/infrastructure/ci-cd-for-data|Ci Cd For Data]] — CI/CD
- [[wiki/data-storage/schema-migrations|Schema Migrations]] — existing note
- [[wiki/infrastructure/schema-change-management-and-branching|Schema Change Management And Branching]] — branching
- [[wiki/data-storage/data-warehouse|Data Warehouse]] — warehouse reference
- [[wiki/data-storage/data-quality-dimensions|Data Quality Dimensions]] — quality dimensions
- [[wiki/data-storage/data-observability-and-monitoring|Data Observability and Monitoring]] — observability
- [[wiki/data-storage/data-testing-frameworks|Data Testing Frameworks]] — testing

