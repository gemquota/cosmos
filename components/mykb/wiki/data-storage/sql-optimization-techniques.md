---
type: "concept"
title: "SQL Optimization Techniques"
description: "Making slow queries fast with structure and statistics"
tags: ["sql", "optimization", "performance", "query-tuning"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://en.wikipedia.org/wiki/Query_optimization", "https://www.postgresql.org/docs/current/indexes.html"]
---

# SQL Optimization Techniques

## Summary

SQL optimization improves query performance by changing access paths, shapes, and statistics.
The optimizer responds to schema, indexes, and statistics.
Most gains come from data modeling and index design, not micro-tuning.
Most slow queries are slow because of missing indexes, not missing cleverness.

## Details

- Filter early: push predicates and reduce join inputs.
- Indexes and clustering keys should match hot predicates.
- Avoid functions on indexed columns that defeat index use.
- Rewrite anti-patterns: N+1 loops, implicit conversions, non-sargable filters.
- Measure with EXPLAIN ANALYZE and compare estimates to actuals.
- Benchmark before and after each change with realistic data.
- Monitor plan changes after schema or statistics updates.
- SQL optimization is a measurement discipline: every change should come with a before and after explain.

## Related

- [[wiki/data-storage/query-planning-and-optimization|Query Planning and Optimization]] — planner
- [[wiki/data-storage/indexing-strategies-revisited|Indexing Strategies Revisited]] — index design
- [[wiki/data-storage/explain-plans-and-profiling|Explain Plans And Profiling]] — reading plans
- [[wiki/data-storage/query-tuning|Query Tuning]] — existing note
- [[wiki/data-storage/vectorized-query-execution|Vectorized Query Execution]] — execution
- [[wiki/data-storage/data-quality-dimensions|Data Quality Dimensions]] — quality dimensions
- [[wiki/data-storage/data-observability-and-monitoring|Data Observability and Monitoring]] — observability
- [[wiki/data-storage/data-testing-frameworks|Data Testing Frameworks]] — testing
- [[wiki/data-storage/feature-stores-and-ml-features|Feature Stores and ML Features]] — ML features
- [[wiki/data-storage/data-contracts-and-agreements|Data Contracts and Agreements]] — data contracts
- [[wiki/data-storage/incremental-loading-strategies|Incremental Loading Strategies]] — incremental loading
- [[wiki/data-storage/schema-evolution-in-streams|Schema Evolution In Streams]] — schema evolution

