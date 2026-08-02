---
type: "concept"
title: "Flyway and Liquibase"
description: "The standard Java-ecosystem migration tools"
tags: ["flyway", "liquibase", "migrations", "schema"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://docs.liquibase.com/", "https://en.wikipedia.org/wiki/Schema_migration"]
---

# Flyway and Liquibase

## Summary

Flyway and Liquibase version database schemas with scripted migrations.
Both integrate with build pipelines and multiple databases.
They bring software-engineering discipline to schema change.
The tools differ in format and rollback philosophy; consistency matters more than the choice.

## Details

- Flyway: SQL-based versioned migrations with checksums.
- Liquibase: XML/YAML/SQL changelogs with rollback support.
- Both track applied versions in a schema-history table.
- Pair with zero-downtime patterns for safe deploys.
- Choose by language, format preference, and rollback needs.
- Lock files prevent concurrent migration races.
- Integrate migrations into CI so they deploy with code.
- Flyway and Liquibase are the standard answer to version-controlled schemas.

## Related

- [[wiki/data-storage/schema-migration-tools|Schema Migration Tools]] — tools
- [[wiki/data-storage/zero-downtime-migrations|Zero Downtime Migrations]] — pattern
- [[wiki/infrastructure/data-environments-dev-staging-prod|Data Environments Dev Staging Prod]] — environments
- [[wiki/data-storage/schema-migrations|Schema Migrations]] — existing note
- [[wiki/data-storage/backward-compatible-schema-changes|Backward Compatible Schema Changes]] — compatibility
- [[wiki/data-storage/data-warehouse|Data Warehouse]] — warehouse reference
- [[wiki/data-storage/data-quality-dimensions|Data Quality Dimensions]] — quality dimensions
- [[wiki/data-storage/data-observability-and-monitoring|Data Observability and Monitoring]] — observability

