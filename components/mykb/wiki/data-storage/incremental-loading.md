---
type: "concept"
title: "Incremental Loading"
description: "Watermark-based delta extraction strategies"
tags: ["incremental-loading", "watermarks", "etl", "pipelines"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Task.CDC.html", "https://docs.getdbt.com/docs/build/incremental-models"]
---

# Incremental Loading

## Summary
Incremental loading copies only data changed since the last run instead of reloading everything. A watermark — the maximum timestamp or sequence previously seen — drives the extraction window, cutting runtime and warehouse cost dramatically on large tables.

## Details
- **Watermark mechanics** — the pipeline stores the last high-water mark (e.g., `max(updated_at)` or the last sequence/offset); each run selects rows above it and then advances the mark after success.
- **Timestamp-based deltas** — `updated_at` or `created_at` columns are simplest, but clock skew, backdated writes, and missing index support cause missed rows; indexes on the watermark column are mandatory.
- **Log-based deltas** — change data capture reads the database log (binlog, WAL) instead of polling, giving near-real-time deltas with no source query load; Debezium and AWS DMS are common tools.
- **Incremental models** — dbt's `is_incremental()` macro and Spark's `MERGE`/`upsert` patterns apply deltas into target tables; uniqueness keys decide insert versus update.
- **Failure handling** — an advance-then-fail race loses data; the mark must advance only after the target write commits, and reruns must be idempotent.
- **Trade-offs** — incremental is fast but accumulates correctness debt (schema drift, late-arriving data); occasional full refreshes re-baseline the deltas.

## Related
- [[wiki/data-storage/cdc-change-data-capture|Change Data Capture]] — log-based delta extraction
- [[wiki/data-storage/idempotent-ingestion|Idempotent Ingestion]] — safe retries for delta runs
- [[wiki/data-storage/backfilling|Backfilling]] — correcting missed windows
- [[wiki/data-storage/data-pipeline-orchestration|Data Pipeline Orchestration]] — scheduling delta runs
- [[wiki/data-storage/data-observability|Data Observability]] — monitoring watermark freshness
