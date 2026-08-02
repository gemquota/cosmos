---
type: "concept"
title: "Statistics and Optimizer Hints"
description: "Feeding the optimizer better information about data"
tags: ["statistics", "hints", "optimizer", "query-tuning"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Statistics and Optimizer Hints

## Summary

A stub to be expanded into a full article; frames the concept and open questions.

## Details

- Table statistics (row counts, cardinality, histograms) drive join order and access paths.
- Stale or missing stats cause bad plans; ANALYZE refreshes them.
- Hints (join type, index, parallelism) override the optimizer when it is wrong.
- Hints are a workaround: keep stats fresh before resorting to them.

## Related

- [[wiki/data-storage/cost-based-query-optimization|Cost-Based Query Optimization]] — optimizer
- [[wiki/data-storage/query-tuning|Query Tuning]] — tuning
- [[wiki/data-storage/cost-model-and-cardinality-estimation|Cost Model And Cardinality Estimation]] — cost model
- [[wiki/data-storage/explain-plans-and-profiling|Explain Plans And Profiling]] — checking plans
- [[wiki/data-storage/data-engineering-fundamentals|Data Engineering Fundamentals]] — core data engineering concepts
