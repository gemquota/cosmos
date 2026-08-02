---
type: "concept"
title: "Surrogate and Natural Keys"
description: "Artificial stable identifiers versus business-provided identifiers in warehouse modeling"
tags: ["keys", "modeling", "surrogate-keys", "warehouse"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Surrogate and Natural Keys

## Summary

A stub to be expanded into a full article; frames the concept and open questions.

## Details

- Surrogate keys are meaningless system-generated integers; natural keys come from the source business domain.
- Surrogates decouple warehouse rows from source changes: reissued or reused natural keys do not corrupt history.
- Natural keys are still stored as attributes for joins to sources, deduplication, and SCD versioning logic.
- Best practice: surrogate PK internally, natural key as a unique business key plus audit columns.

## Related

- [[wiki/data-storage/surrogate-keys|Surrogate vs Natural Keys]] — existing note on surrogate keys
- [[wiki/data-storage/entity-resolution|Entity Resolution]] — matching records when keys are messy
- [[wiki/data-storage/scd-type-2-slowly-changing-dimensions|Scd Type 2 Slowly Changing Dimensions]] — surrogates enable versioning
- [[wiki/data-storage/dimension-tables-and-grains|Dimension Tables And Grains]] — keys anchor dimension design
- [[wiki/data-storage/data-engineering-fundamentals|Data Engineering Fundamentals]] — core data engineering concepts
