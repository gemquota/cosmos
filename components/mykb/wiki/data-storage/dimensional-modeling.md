---
type: "concept"
title: "Dimensional Modeling"
description: "Fact and dimension design including star schemas"
tags: ["dimensional-modeling", "star-schema", "facts", "dimensions"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://en.wikipedia.org/wiki/Dimensional_modeling", "https://www.kimballgroup.com/data-warehouse-business-intelligence-resources/kimball-techniques/dimensional-modeling-techniques/"]
---

# Dimensional Modeling
## Summary
Dimensional modeling organizes warehouse data into facts — numeric measures with foreign keys — and dimensions — descriptive attributes that give measures context. The star schema joins them into simple, query-friendly structures that business users and BI tools understand without deep schema knowledge.

## Details
- **Fact tables** — store business events (sales, orders, clicks) with additive measures and foreign keys to dimensions; they are long, narrow, and grow fast, so they drive partitioning and compression decisions.
- **Dimension tables** — hold attribute hierarchies (time, product, customer, geography) that describe each fact row; they are wider, shorter, and heavily used in GROUP BY and filter clauses.
- **Star schema** — one fact table in the center with directly joined dimensions; denormalized dimensions keep joins short. Snowflake schemas normalize dimensions, trading simplicity for storage.
- **Conformed dimensions** — shared dimension definitions across fact tables make metrics consistent (the same "customer" means the same thing everywhere), which is the core of an integrated warehouse.
- **Grain** — the fact table's grain (one row per order line, per click) must be declared; double-counting happens when facts are aggregated at the wrong grain.
- **Slowly changing dimensions** — history is tracked via SCD types; degenerate dimensions (order numbers in the fact) avoid useless joins.

## Related
- [[wiki/data-storage/data-warehouse|Data Warehouse]] — the host system
- [[wiki/data-storage/slowly-changing-dimensions|Slowly Changing Dimensions]] — tracking dimension history
- [[wiki/data-storage/denormalization|Denormalization]] — why dimensions store attributes inline
- [[wiki/data-storage/surrogate-keys|Surrogate vs Natural Keys]] — dimension key design
- [[wiki/data-storage/materialized-views|Materialized Views]] — accelerating star queries
