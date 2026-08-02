---
type: "concept"
title: "Data Quality Checks"
description: "Assertions for completeness, uniqueness, and validity"
tags: ["data-quality", "tests", "assertions", "data-engineering"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://docs.getdbt.com/docs/build/tests", "https://docs.greatexpectations.io/docs/"]
---

# Data Quality Checks

## Summary
Data quality checks are automated assertions about data: row counts, uniqueness, null rates, value ranges, and cross-table relationships. Run after every load, they catch broken pipelines before bad data reaches reports, and they are the difference between a pipeline and a promise.

## Details
- **Standard dimensions** — completeness (no missing rows or nulls where required), uniqueness (keys are distinct), validity (values in range or format), timeliness (freshness), and consistency (same entity agrees across tables).
- **dbt tests** — `not_null`, `unique`, `accepted_values`, and `relationships` are built in; custom SQL tests express arbitrary predicates, and tests run as part of the model DAG so failures stop downstream.
- **Great Expectations** — data-contract-style expectation suites (expect_column_values_to_be_between, expect_table_row_count_to_equal) with profiling to bootstrap thresholds; runs inside notebook, batch, and streaming contexts.
- **Thresholds vs binary** — row-count equality is fragile; freshness SLA, null-rate tolerance, and anomaly windows beat hard equality. Failure behavior — block downstream, alert, quarantine — should be explicit per check.
- **Where they live** — checks belong in CI (schema tests on sample data), in the pipeline (post-load assertions), and in production monitoring (dashboards over check results).

## Related
- [[wiki/data-storage/data-profiling|Data Profiling]] — discovering what to assert
- [[wiki/data-storage/data-observability|Data Observability]] — running checks in production
- [[wiki/data-storage/data-contracts|Data Contracts]] — checks as contract terms
- [[wiki/data-storage/data-lineage|Data Lineage]] — knowing check blast radius
- [[wiki/data-storage/idempotent-ingestion|Idempotent Ingestion]] — preventing duplicates checks detect
