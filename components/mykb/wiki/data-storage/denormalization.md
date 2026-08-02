---
type: "concept"
title: "Denormalization"
description: "Intentional redundancy to speed up reads"
tags: ["denormalization", "schema-design", "performance", "data-modeling"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://en.wikipedia.org/wiki/Denormalization", "https://dev.mysql.com/doc/refman/8.4/en/optimization-index.html"]
---

# Denormalization

## Summary
Denormalization adds intentional redundancy to a schema — duplicate columns, summary tables, or embedded values — so hot reads avoid joins and aggregations. It trades write complexity and consistency risk for latency, and it only pays off when measured queries justify it.

## Details
- **Common moves** — precomputing a `total` column, duplicating a lookup name into the fact row, caching counts in parent rows, or materializing join results as tables.
- **Why it helps** — joins and GROUP BY are expensive at scale; an embedded value turns a multi-table read into a single-row fetch. Read-heavy applications (dashboards, feeds) often denormalize heavily.
- **Consistency burden** — every redundant copy must be updated together; triggers, application code, or streaming pipelines keep copies in sync, and the window of inconsistency is a correctness risk.
- **Normalization vs denormalization** — normalization is the safe default; denormalization is a deliberate, documented exception driven by query profiling, not a starting posture.
- **Modern equivalents** — materialized views and generated columns (Postgres 12+ `GENERATED ALWAYS AS`, MySQL 8) push the same pattern into the engine; columnar and vector stores denormalize structurally by design.
- **Operational notes** — schedule re-syncs and backfills for copied data, monitor drift with data-quality checks, and be ready to revert once schema or access patterns change.

## Related
- [[wiki/data-storage/database-normalization|Database Normalization]] — the baseline being relaxed
- [[wiki/data-storage/materialized-views|Materialized Views]] — engine-managed denormalization
- [[wiki/data-storage/dimensional-modeling|Dimensional Modeling]] — denormalized warehouse design
- [[wiki/data-storage/data-quality-checks|Data Quality Checks]] — catching drift in copies
- [[wiki/data-storage/query-tuning|Query Tuning]] — evidence for denormalizing
