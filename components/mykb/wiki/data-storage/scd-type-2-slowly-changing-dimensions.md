---
type: "concept"
title: "SCD Type 2: Slowly Changing Dimensions"
description: "Keeping full history of dimension attribute changes by inserting new versions"
tags: ["scd", "dimensional-modeling", "history", "warehouse"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# SCD Type 2: Slowly Changing Dimensions

## Summary

A stub to be expanded into a full article; frames the concept and open questions.

## Details

- Type 2 adds a new row whenever a tracked attribute changes, preserving the old version for historical reporting.
- Effective start/end dates plus a current-flag let queries join facts to the version that was true at the time.
- Costs: table growth, more complex merge logic, and surrogate keys needed to disambiguate versions.
- Type 1 overwrites, Type 3 tracks prior value, and Type 6 mixes approaches; most warehouses standardize on Type 2 for audited dimensions.

## Related

- [[wiki/data-storage/slowly-changing-dimensions|Slowly Changing Dimensions]] — existing note on SCD family
- [[wiki/data-storage/surrogate-keys|Surrogate vs Natural Keys]] — versioning requires surrogate keys
- [[wiki/data-storage/dimension-tables-and-grains|Dimension Tables And Grains]] — dimension design fundamentals
- [[wiki/data-storage/merge-and-upsert-patterns|Merge And Upsert Patterns]] — SQL mechanics for Type 2 loads
- [[wiki/data-storage/time-travel-queries|Time Travel Queries]] — history without explicit versions
