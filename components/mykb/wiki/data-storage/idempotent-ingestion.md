---
type: "concept"
title: "Idempotent Ingestion"
description: "Safe retries via dedup keys and upserts"
tags: ["idempotency", "ingestion", "deduplication", "data-pipelines"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://docs.getdbt.com/docs/build/incremental-models", "https://spark.apache.org/docs/latest/sql-ref-syntax-dml-merge-into.html"]
---

# Idempotent Ingestion

## Summary
Idempotent ingestion guarantees that applying the same input twice yields the same result, so retries, redeliveries, and replay don't corrupt the target. Dedup keys, upserts, and deterministic runs are the mechanisms, and they are the price of reliable pipelines.

## Details
- **Why it matters** — networks redeliver, schedulers retry, and operators re-run; without idempotency, each replay duplicates rows, inflates aggregates, and erodes trust in the data.
- **Dedup keys** — a stable natural key (event ID, order ID) plus a unique constraint turns a second insert into a conflict; `INSERT ... ON CONFLICT DO NOTHING` (Postgres) and `INSERT IGNORE` (MySQL) implement it cheaply.
- **Upserts** — `MERGE`, `INSERT ... ON CONFLICT DO UPDATE`, and Spark's `MERGE INTO` update existing rows by key; the write must be a true merge, not delete-then-insert, to avoid races.
- **Deterministic runs** — same input, same output: tasks should avoid random IDs, `now()` in keys, and nondeterministic partitioning; processing time is recorded separately from event time.
- **At-least-once realities** — streaming systems deliver at least once; the target's idempotency, not the source, decides whether duplicates survive.
- **Operational checks** — row-count monitors and uniqueness tests catch idempotency breaks; re-running a batch over a date range is the standard regression drill.

## Related
- [[wiki/data-storage/incremental-loading|Incremental Loading]] — deltas that must not double-apply
- [[wiki/data-storage/deduplication|Deduplication]] — cleaning data that was already doubled
- [[wiki/data-storage/exactly-once-semantics|Exactly-Once Semantics]] — the streaming-side guarantee
- [[wiki/data-storage/data-quality-checks|Data Quality Checks]] — catching duplicate violations
- [[wiki/data-storage/backfilling|Backfilling]] — replays that rely on idempotency
