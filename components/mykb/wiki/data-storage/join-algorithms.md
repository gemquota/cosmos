---
type: "concept"
title: "Join Algorithms"
description: "Nested-loop, hash, and merge joins and when each wins"
tags: ["join", "query-execution", "sql", "performance"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://dev.mysql.com/doc/refman/8.4/en/nested-loop-joins.html", "https://www.postgresql.org/docs/current/planner-optimizer.html"]
---

# Join Algorithms

## Summary
Join algorithms turn the optimizer's join order into a concrete operator. Three families dominate: nested-loop, hash, and merge joins, each with a distinct cost profile that decides when the optimizer uses it.

## Details
- **Nested-loop join** — for each outer row, probe the inner relation; with an index on the inner side it becomes "indexed nested-loop" and wins on small outer inputs with selective filters, even on non-equi predicates.
- **Hash join** — build a hash table on the smaller side, probe with the larger side; ideal for equijoins of large unsorted inputs; memory spills to disk when the build side exceeds work memory, degrading to a hybrid grace hash join.
- **Merge join** — both inputs arrive sorted (index order or explicit sort); a single merge pass matches keys; best when inputs are already sorted or the join is on ranges rather than equality.
- **Block nested-loop** — MySQL batches outer rows and buffers them, reducing inner scans for cases without usable indexes.
- **Optimizer choice** — PostgreSQL defaults change with `enable_hashjoin`/`enable_mergejoin`/`enable_nestloop` flags; forcing a join type is usually a symptom of bad statistics, not a good long-term fix.
- **mykb relevance** — joining wiki metadata against FTS results should produce hash joins on equality keys; seeing nested-loop on large inputs signals a missing index.

## Related
- [[wiki/data-storage/cost-based-query-optimization|Cost-Based Query Optimization]] — chooses among these algorithms
- [[wiki/data-storage/hash-indexes|Hash Indexes]] — the lookup structure inside hash joins
- [[wiki/data-storage/b-tree-indexing|B-Tree Indexing]] — powers indexed nested-loop and sorted merge inputs
- [[wiki/data-storage/buffer-pool-management|Buffer Pool Management]] — memory that determines hash-join spill
- [[wiki/data-storage/query-tuning|Query Tuning]] — diagnosing join regressions
- [[wiki/devops-infra/query-planning|Query Planning]] — reading join plans in EXPLAIN
