---
type: "concept"
title: "SCD Type 2: Slowly Changing Dimensions"
description: "Keeping full history of dimension attribute changes by inserting new versions"
tags: ["scd", "dimensional-modeling", "history", "warehouse"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# SCD Type 2: Slowly Changing Dimensions

## Summary
SCD Type 2 adds a new row whenever a tracked attribute changes, preserving the old version for historical reporting. Effective start/end dates plus a current-flag let queries join facts to the version that was true at the time — at the cost of table growth, more complex merge logic, and surrogate keys to disambiguate versions.

## Details
- Mechanism: a dimension row carries valid_from, valid_to, and a current flag; an attribute change closes the current row (sets valid_to) and inserts a new version (valid_from = change time, current = true); fact rows join on the surrogate key, so historical facts point at the version that was current when they happened.
- Concrete example: a customer moves; the customer dimension closes the old row and opens a new one with the new address; sales from last year still join to the old address; a Type 2 product rename preserves both names for reporting; the merge job detects the change, expires the old row, and inserts the new one atomically.
- Failure modes: Type 2 applied to every attribute, doubling the table on each change and fragmenting history; missing effective dates, so versions are ambiguous; no current flag maintained, forcing expensive max(valid_from) lookups; merge races expiring and inserting the same row; surrogate key collisions across versions.
- Tradeoffs: Type 2 preserves auditable history at the cost of table growth and load complexity; the alternatives — Type 1 overwrite (simple, no history), Type 3 (prior value only), Type 6 (mix) — trade history for simplicity; the mature pattern is Type 2 for audited dimensions, Type 1 for attributes history does not matter for.
- Operational notes: track tracked-attribute lists explicitly, index effective dates, and test historical joins in CI.
- RSIS3 relevance: the wiki's entity and status history are naturally Type 2 — preserving versioned truth is what makes the knowledge graph auditable.


## Related
- [[wiki/data-storage/slowly-changing-dimensions|Slowly Changing Dimensions]] — existing note on SCD family
- [[wiki/data-storage/surrogate-keys|Surrogate vs Natural Keys]] — versioning requires surrogate keys
- [[wiki/data-storage/dimension-tables-and-grains|Dimension Tables And Grains]] — dimension design fundamentals
- [[wiki/data-storage/merge-and-upsert-patterns|Merge And Upsert Patterns]] — SQL mechanics for Type 2 loads
- [[wiki/data-storage/time-travel-queries|Time Travel Queries]] — history without explicit versions
