---
type: "concept"
title: "Slowly Changing Dimensions"
description: "Tracking historical dimension attributes (SCD types)"
tags: ["scd", "dimensions", "dimensional-modeling", "history"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://en.wikipedia.org/wiki/Slowly_changing_dimension", "https://www.kimballgroup.com/data-warehouse-business-intelligence-resources/kimball-techniques/dimensional-modeling-techniques/"]
---

# Slowly Changing Dimensions

## Summary
Slowly changing dimensions (SCD) describe how warehouse dimensions record changes to attributes like customer address or product category. The numbered SCD types trade storage and complexity for historical accuracy, and every team should pick a type per attribute deliberately.

## Details
- **Type 1 (overwrite)** — the new value replaces the old; simple and compact, but history is lost, so past reports change meaning. Best for corrections and attributes where history is irrelevant.
- **Type 2 (version rows)** — a new row with effective dates and an active flag preserves full history; queries must filter by date and active status, which complicates joins but makes point-in-time reporting correct.
- **Type 3 (original/current)** — keeps a small set of columns for before/after values; limited history depth, useful for "previous vs current" questions like territory reassignments.
- **Type 4–6** — miniature dimension tables, hybrid approaches, and combinations of 1+2+3 exist; they suit specialized audit or high-churn cases.
- **Selection guidance** — regulatory reporting wants Type 2; operational metrics often tolerate Type 1; start with Type 2 for core dimensions and document the choice per attribute.
- **Operational cost** — Type 2 needs surrogate keys, effective-date joins, and dedup handling in the ETL; the warehouse schema and BI tooling must understand active-row semantics.

## Related
- [[wiki/data-storage/dimensional-modeling|Dimensional Modeling]] — the schema SCD lives in
- [[wiki/data-storage/surrogate-keys|Surrogate vs Natural Keys]] — keys that stay stable across versions
- [[wiki/data-storage/data-warehouse|Data Warehouse]] — where history matters most
- [[wiki/data-storage/cdc-change-data-capture|Change Data Capture]] — feeding dimension changes
- [[wiki/data-storage/point-in-time-recovery|Point-in-Time Recovery]] — time-travel alternatives
