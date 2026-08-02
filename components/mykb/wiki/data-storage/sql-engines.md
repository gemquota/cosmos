---
type: "concept"
title: "SQL Engine Architecture"
description: "How parsers, optimizers, and executors turn SQL into results"
tags: ["sql", "query-processing", "query-engine", "databases"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://www.postgresql.org/docs/current/planner-optimizer.html", "https://dev.mysql.com/doc/refman/8.4/en/optimizer.html"]
---

# SQL Engine Architecture

## Summary
A SQL engine converts declarative statements into executable plans through a pipeline of parsing, binding, optimization, and execution. Understanding the stages explains why equivalent queries perform so differently and where most performance leverage lives.

## Details
- **Parser** — tokenizes the statement and builds an abstract syntax tree (AST) using a grammar; PostgreSQL and MySQL both hand-parse SQL rather than using generic parser generators for better error messages.
- **Binder/analyzer** — resolves table and column references, checks privileges, and infers types; the analyzer output is a decorated tree with catalog lookups.
- **Optimizer** — rewrites the tree (subquery flattening, view expansion, predicate pushdown), then searches join orders and access paths with a cost model over table statistics.
- **Executor** — runs the physical plan; the classic iterator model pulls one row at a time from each operator, while analytical engines batch tuples for vectorized processing.
- **Plan caching** — prepared statements reuse plans across executions; PostgreSQL re-plans when generic plans would be too costly, MySQL caches plans per session for prepared statements.
- **mykb relevance** — the local DuckDB/Postgres engines in this stack share this architecture, so tuning SQL here maps to the same optimizer stages.

## Related
- [[wiki/data-storage/cost-based-query-optimization|Cost-Based Query Optimization]] — the optimizer stage that picks plans
- [[wiki/data-storage/join-algorithms|Join Algorithms]] — executor operators that dominate query cost
- [[wiki/data-storage/vectorized-query-execution|Vectorized Query Execution]] — the batch-at-a-time execution model
- [[wiki/data-storage/storage-engines|Storage Engines]] — the layer below the SQL layer
- [[wiki/devops-infra/query-planning|Query Planning]] — reading EXPLAIN output in practice
- [[wiki/devops-infra/postgresql|PostgreSQL]] — a reference open-source SQL engine
