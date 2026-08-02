---
type: "concept"
title: "Query Planning and Optimization"
description: "How databases turn SQL into efficient execution plans"
tags: ["optimizer", "query-planning", "sql", "performance"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://en.wikipedia.org/wiki/Query_optimization", "https://www.postgresql.org/docs/current/index.html"]
---

# Query Planning and Optimization

## Summary

Query planners translate SQL into operator trees and search for low-cost plans.
Statistics, indexes, and join order drive plan quality.
Understanding plans is the core skill of query tuning.
Plan quality decays with stale statistics; make ANALYZE part of load workflows.

## Details

- Plan search considers join order, join algorithms, and access paths.
- Cost models estimate rows, IO, and CPU; bad estimates cause bad plans.
- Statistics (histograms, correlation) improve estimates.
- Explain/analyze compares estimates to actuals.
- Hints and plan guides override the optimizer when needed.
- Parameterized and prepared queries keep plans stable and cacheable.
- Plan diffs after upgrades or data changes explain sudden regressions.
- Good planning needs good statistics, good indexes, and a disciplined process for reviewing plan changes.

## Related

- [[wiki/data-storage/indexing-strategies-revisited|Indexing Strategies Revisited]] — index-driven access
- [[wiki/data-storage/cost-model-and-cardinality-estimation|Cost Model And Cardinality Estimation]] — estimation
- [[wiki/data-storage/explain-plans-and-profiling|Explain Plans And Profiling]] — reading plans
- [[wiki/data-storage/cost-based-query-optimization|Cost-Based Query Optimization]] — optimizer note
- [[wiki/data-storage/query-tuning|Query Tuning]] — tuning

