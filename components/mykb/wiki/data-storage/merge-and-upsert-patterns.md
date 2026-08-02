---
type: "concept"
title: "Merge and Upsert Patterns"
description: "Combining new records with existing state via INSERT/UPDATE/DELETE semantics"
tags: ["merge", "upsert", "scd", "data-loading"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Merge and Upsert Patterns

## Summary

A stub to be expanded into a full article; frames the concept and open questions.

## Details

- SQL MERGE (and INSERT ... ON CONFLICT) reconciles incoming rows against a target table by key.
- Merge patterns implement Type 1 overwrites and Type 2 history when paired with effective-dating columns.
- Open table formats like Delta Lake and Iceberg provide atomic merge operations over object storage.
- Design questions: which key, which columns change, whether deletes propagate, and how to detect no-ops.

## Related

- [[wiki/data-storage/incremental-loading|Incremental Loading]] — merging is the incremental update step
- [[wiki/data-storage/slowly-changing-dimensions|Slowly Changing Dimensions]] — Type 1/2 semantics via merges
- [[wiki/data-storage/open-table-formats|Open Table Formats]] — ACID merges on the lakehouse
- [[wiki/data-storage/idempotent-writes-and-upserts|Idempotent Writes And Upserts]] — replay-safety of merge targets
- [[wiki/data-storage/delta-lake-and-merge-operations|Delta Lake And Merge Operations]] — Delta merge operations in practice
