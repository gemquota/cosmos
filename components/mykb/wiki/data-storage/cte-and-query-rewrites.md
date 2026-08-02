---
type: "concept"
title: "CTEs and Query Rewrites"
description: "Structuring complex queries with common table expressions"
tags: ["cte", "sql", "recursion", "query-structure"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://www.postgresql.org/docs/current/queries-with.html", "https://en.wikipedia.org/wiki/Hierarchical_and_recursive_queries_in_SQL"]
---

# CTEs and Query Rewrites

## Summary

Common table expressions (WITH clauses) name subqueries for readability and reuse.
Recursive CTEs traverse hierarchies like org charts and bill-of-materials.
CTEs are a structuring tool; the optimizer may inline or materialize them.
Recursive CTEs turn recursive business structures into single declarative queries.

## Details

- WITH improves readability by decomposing complex queries.
- Recursive CTEs walk trees and graphs with anchor plus recursive terms.
- Materialization control (AS MATERIALIZED vs INLINE) affects performance.
- CTEs can hide poor plans; check EXPLAIN when they slow down.
- They compose naturally with window functions and aggregations.
- Check whether the optimizer inlines or materializes each CTE.
- Use CTEs to make complex queries auditable and testable.
- Well-structured queries are maintainable queries; CTEs are the primary structuring tool.

## Related

- [[wiki/data-storage/sql-optimization-techniques|Sql Optimization Techniques]] — performance
- [[wiki/data-storage/window-functions-in-sql|Window Functions In Sql]] — composition
- [[wiki/data-storage/query-planning-and-optimization|Query Planning And Optimization]] — plans
- [[wiki/data-storage/sql-engines|SQL Engine Architecture]] — engines
- [[wiki/data-storage/cte-and-query-rewrites|CTEs and Query Rewrites]] — recursion
- [[wiki/data-storage/data-quality-dimensions|Data Quality Dimensions]] — quality dimensions
- [[wiki/data-storage/data-observability-and-monitoring|Data Observability And Monitoring]] — observability
- [[wiki/data-storage/data-testing-frameworks|Data Testing Frameworks]] — testing
- [[wiki/data-storage/feature-stores-and-ml-features|Feature Stores And Ml Features]] — ML features
- [[wiki/data-storage/data-contracts-and-agreements|Data Contracts And Agreements]] — data contracts
- [[wiki/data-storage/incremental-loading-strategies|Incremental Loading Strategies]] — incremental loading
- [[wiki/data-storage/schema-evolution-in-streams|Schema Evolution In Streams]] — schema evolution
- [[wiki/data-storage/streaming-sinks-and-sources|Streaming Sinks And Sources]] — streams
- [[wiki/data-storage/data-warehouse|Data Warehouse]] — warehouse reference

