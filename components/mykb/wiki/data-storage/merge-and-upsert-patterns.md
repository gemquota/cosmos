---
type: "concept"
title: "Merge and Upsert Patterns"
description: "Combining new records with existing state via INSERT/UPDATE/DELETE semantics"
tags: ["merge", "upsert", "scd", "data-loading"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Merge and Upsert Patterns

## Summary
SQL MERGE (and INSERT ... ON CONFLICT) reconciles incoming rows against a target table by key: new rows insert, matching rows update, and deletes can propagate. Merge patterns implement Type 1 overwrites and Type 2 history when paired with effective-dating columns, and open table formats like Delta Lake and Iceberg provide atomic merges over object storage.

## Details
- Mechanism: MERGE matches incoming rows to target rows on a key; actions specify insert, update, or delete behavior per match state; INSERT ... ON CONFLICT is the lighter single-row variant; effective-dating columns (valid_from/valid_to) turn an overwrite into a history-preserving Type 2 update; Delta/Iceberg MERGE runs atomically on lakehouse tables.
- Concrete example: a nightly load merges a product feed into the product table by SKU — new SKUs insert, existing update, removed SKUs delete or expire; a customer address change with effective dating inserts a new row and closes the old one, preserving history; a replay of the same feed converges to the same state (idempotent).
- Failure modes: merge keys chosen on mutable attributes, splitting history; update actions that overwrite unrelated concurrent changes; delete propagation that destroys fact-referenced dimensions; no-op detection missing, rewriting every row each run and bloating logs; merge performance collapsing without partition pruning.
- Tradeoffs: merge patterns centralize reconciliation logic in one statement at the cost of key and semantics design — the wrong key silently corrupts state; the alternative, delete-and-reload, is simpler and destructive; the mature pattern is natural keys, explicit update/delete policy, and idempotent replay verified in tests.
- Operational notes: document the merge key and policy per table, test replays, and monitor rows-affected for anomalies.
- RSIS3 relevance: RSIS3's state updates (registry rows, checkpoint tables) are merge workloads — key design determines whether replays converge or corrupt.


## Related
- [[wiki/data-storage/incremental-loading|Incremental Loading]] — merging is the incremental update step
- [[wiki/data-storage/slowly-changing-dimensions|Slowly Changing Dimensions]] — Type 1/2 semantics via merges
- [[wiki/data-storage/open-table-formats|Open Table Formats]] — ACID merges on the lakehouse
- [[wiki/data-storage/idempotent-writes-and-upserts|Idempotent Writes And Upserts]] — replay-safety of merge targets
- [[wiki/data-storage/delta-lake-and-merge-operations|Delta Lake And Merge Operations]] — Delta merge operations in practice
