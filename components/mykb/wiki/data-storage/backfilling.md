---
type: "concept"
title: "Backfilling"
description: "Reprocessing historical ranges after logic or schema changes"
tags: ["backfill", "data-pipeline", "etl", "reprocessing"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://docs.getdbt.com/terms/backfill", "https://airflow.apache.org/docs/apache-airflow/stable/cli-and-env-variables-ref.html#backfill"]
---

# Backfilling

## Summary
Backfilling reprocesses a historical range of data after a logic, schema, or source change so downstream tables reflect the new behavior. It is a scheduled, idempotent replay of transformations over past time partitions — distinct from a full rebuild because it targets a bounded window instead of the entire dataset.

## Details
- **Why it happens** — a dbt model, SQL transformation, or ingestion parser changes meaning; only new rows would reflect it, so historical partitions are recomputed to keep the dataset consistent.
- **Window selection** — the backfill range is typically bounded by the oldest affected partition and the deploy time; outside that window the data is assumed correct.
- **Idempotency** — replays must produce identical results when run twice, so transformations use upserts, `MERGE`, or partition replacement rather than blind appends.
- **Tooling** — dbt runs historical models with `--full-refresh` or date-spine macros; Airflow exposes a `backfill` CLI command that runs a DAG for past execution dates; stream processors use offsets or timestamps to re-consume topic ranges.
- **Ordering** — dependencies matter: parent tables should be backfilled before children that aggregate them, and tables with referential integrity need coordinated windowing.
- **Operational concerns** — backfills compete with production compute, so they run on dedicated warehouses, lower concurrency, or at off-peak times; progress tracking and cancellation are needed for long windows.
- **Schema backfills** — when a column is added or a value is re-encoded, the backfill may be a pure `UPDATE` over rows rather than a full transformation replay.

## Related
- [[wiki/data-storage/schema-migrations|Schema Migrations]] — backfills often accompany versioned DDL changes
- [[wiki/data-storage/cdc-change-data-capture|Change Data Capture]] — reconstructing history when capture starts mid-stream
- [[wiki/data-storage/idempotent-ingestion|Idempotent Ingestion]] — the replay-safety requirement backfills depend on
- [[wiki/data-storage/incremental-loading|Incremental Loading]] — what backfill must respect when rewinding a window
- [[wiki/data-storage/data-quality-checks|Data Quality Checks]] — validating that a backfill matched expectations
- [[wiki/data-storage/data-lifecycle-management|Data Lifecycle Management]] — how backfills interact with retention
