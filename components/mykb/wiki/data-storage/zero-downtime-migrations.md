---
type: "concept"
title: "Zero-Downtime Migrations"
description: "Changing schemas without stopping services"
tags: ["migrations", "zero-downtime", "schema-change", "reliability"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://en.wikipedia.org/wiki/Schema_migration", "https://docs.liquibase.com/"]
---

# Zero-Downtime Migrations

## Summary

Zero-downtime migrations change schema or data while services keep running.
Expand-contract (parallel run, cutover) is the standard pattern.
They eliminate maintenance windows and deploy coupling.
Zero-downtime migrations change the deploy calculus: schema changes stop being release events.

## Details

- Expand: add new columns/tables while old and new coexist.
- Migrate: backfill and dual-write during transition.
- Contract: drop old structures after validation.
- Online DDL tools reduce lock impact.
- Test the cutover; keep rollback paths.
- Dual-write windows need idempotency and reconciliation.
- Contract-phase cleanup should be scheduled, not forgotten.
- Zero-downtime migrations make schema change a continuous, reviewable process.

## Related

- [[wiki/data-storage/schema-migration-tools|Schema Migration Tools]] — tooling
- [[wiki/infrastructure/data-deployment-strategies|Data Deployment Strategies]] — deploy
- [[wiki/data-storage/backward-compatible-schema-changes|Backward Compatible Schema Changes]] — compatibility
- [[wiki/data-storage/expand-contract-migrations|Expand-Contract Migrations]] — existing note
- [[wiki/infrastructure/zero-downtime-deploys|Zero-Downtime Deploys]] — deploy analog
- [[wiki/data-storage/data-quality-dimensions|Data Quality Dimensions]] — quality dimensions
- [[wiki/data-storage/data-observability-and-monitoring|Data Observability and Monitoring]] — observability
- [[wiki/data-storage/data-testing-frameworks|Data Testing Frameworks]] — testing

