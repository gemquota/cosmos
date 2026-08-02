---
type: "concept"
title: "ETL vs ELT"
description: "Where transformation happens and the shift to ELT"
tags: ["etl", "elt", "data-pipelines", "transformation"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://docs.getdbt.com/docs/introduction", "https://en.wikipedia.org/wiki/Extract,_transform,_load"]
---

# ETL vs ELT

## Summary
ETL extracts, transforms, then loads; ELT loads raw data first and transforms inside the target. Cheap, powerful cloud warehouses made ELT dominant: raw data lands quickly and SQL-based tools like dbt own the transformation layer with full auditability.

## Details
- **Classic ETL** — a transformation server cleans, joins, and reshapes data before loading; suited to limited target capacity and legacy warehouses, but slow to land data and hard to reprocess.
- **ELT flow** — extraction writes raw tables; transformation runs as SQL inside the warehouse (or lakehouse) using unlimited-scale compute; raw data stays available, so re-transforming after logic changes is cheap.
- **Why ELT won** — warehouse costs fell, storage got cheap, and SQL became the transformation language of choice; engineers debug with the same tools analysts use, and lineage tools read the SQL DAG.
- **dbt's role** — dbt models define transforms as versioned SQL files with tests and documentation, compiled into the warehouse; Airflow or Dagster schedules them, completing the modern stack.
- **Trade-offs** — ELT stores duplicates (raw + transformed) and pushes transformation compute to the warehouse; ETL still wins for strict masking, tiny targets, or heavyweight custom logic.
- **Practical blend** — pipelines usually land raw (ELT), apply light staging transforms, then load curated marts; the boundary is a matter of compute placement, not ideology.

## Related
- [[wiki/data-storage/data-pipeline-orchestration|Data Pipeline Orchestration]] — scheduling either pattern
- [[wiki/data-storage/data-warehouse|Data Warehouse]] — the ELT target
- [[wiki/data-storage/schema-on-read|Schema-on-Read vs Schema-on-Write]] — when structure is applied
- [[wiki/data-storage/incremental-loading|Incremental Loading]] — keeping ELT fresh
- [[wiki/data-storage/data-lineage|Data Lineage]] — tracing the transform DAG
