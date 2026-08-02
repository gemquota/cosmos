---
type: "concept"
title: "Incremental Loading Strategies"
description: "Loading only what changed instead of rebuilding tables"
tags: ["incremental-loading", "delta", "cdc", "performance"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://en.wikipedia.org/wiki/Data_pipeline", "https://docs.delta.io/latest/"]
---

# Incremental Loading Strategies

## Summary

Incremental loading moves only new or changed records, keeping pipelines fast and cheap.
Strategies range from timestamp watermarks to log-based change data capture.
Correct incremental logic requires stable ordering and idempotent merges.
Incremental logic must be auditable: record high-water marks, source offsets, and affected partitions per run.

## Details

- Watermark strategy: track last load timestamp and filter source rows.
- CDC strategy: capture inserts/updates/deletes from database logs.
- Merge strategy: upsert incrementally into target tables by key.
- Compare-and-catch-up: reload partitions that changed since last run.
- Every strategy needs backfill capability when logic changes.
- Mismatches between strategy and source capabilities cause silent gaps.
- A full-refresh fallback keeps you honest when incremental assumptions break.
- Every incremental strategy should ship with a backfill path and a reconciliation check against a full refresh.

## Related

- [[wiki/data-storage/change-data-capture|Change Data Capture]] — log-based loading
- [[wiki/data-storage/merge-and-upsert-patterns|Merge And Upsert Patterns]] — merge mechanics
- [[wiki/data-storage/incremental-loading|Incremental Loading]] — existing note
- [[wiki/data-storage/backfilling|Backfilling]] — backfill
- [[wiki/data-storage/data-quality-dimensions|Data Quality Dimensions]] — quality dimensions
- [[wiki/data-storage/data-observability-and-monitoring|Data Observability and Monitoring]] — observability
- [[wiki/data-storage/data-testing-frameworks|Data Testing Frameworks]] — testing
- [[wiki/data-storage/feature-stores-and-ml-features|Feature Stores and ML Features]] — ML features
- [[wiki/data-storage/data-contracts-and-agreements|Data Contracts and Agreements]] — data contracts
- [[wiki/data-storage/incremental-loading-strategies|Incremental Loading Strategies]] — incremental loading
- [[wiki/data-storage/schema-evolution-in-streams|Schema Evolution In Streams]] — schema evolution

