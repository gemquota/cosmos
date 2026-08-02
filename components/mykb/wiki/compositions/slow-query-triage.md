---
type: "concept"
title: "Slow Query Triage"
description: "The workflow for finding and fixing slow database queries"
tags: ["slow-queries", "databases", "performance", "triage"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Slow Query Triage

## Summary
Slow query triage finds queries that violate latency budgets and drives them to resolution: capture via logs, rank by impact, explain, fix, verify. A repeatable triage loop beats ad-hoc panic.

## Details
- Capture slow queries with log_min_duration-style settings and track the worst offenders.
- Rank by frequency times cost — one slow query under heavy load outranks a rare disaster.
- Fix categories: missing index, bad statistics, pathological joins, N+1 from the app.
- mykb relevance: the wiki sync pipeline triages slow upserts the same way each cycle.

## Related
- [[wiki/compositions/explain-analyze|EXPLAIN ANALYZE]]
- [[wiki/compositions/query-plans|Query Plans]]
- [[wiki/compositions/query-optimization|Query Optimization]]
- [[wiki/compositions/index-selection|Index Selection]]
- [[wiki/software-engineering/metrics-and-monitoring|Metrics and Monitoring]]
