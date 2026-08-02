---
type: "concept"
title: "Cost Model and Cardinality Estimation"
description: "How optimizers estimate row counts and pick plans"
tags: ["optimizer", "cardinality", "cost-model", "query-planning"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Cost Model and Cardinality Estimation

## Summary

A stub to be expanded into a full article; frames the concept and open questions.

## Details

- Cardinality estimation predicts intermediate result sizes from stats and predicates.
- Cost models combine IO, CPU, and memory estimates for candidate plans.
- Estimates degrade with correlated columns, complex predicates, and UDFs.
- Adaptive execution (Spark AQE, Postgres extended stats) repairs bad estimates.

## Related

- [[wiki/data-storage/cost-based-query-optimization|Cost-Based Query Optimization]] — optimizer foundations
- [[wiki/data-storage/query-planning-and-optimization|Query Planning And Optimization]] — planning
- [[wiki/data-storage/statistics-and-optimizer-hints|Statistics And Optimizer Hints]] — stats input
- [[wiki/data-storage/adaptive-query-execution|Adaptive Query Execution]] — runtime correction
- [[wiki/data-storage/data-engineering-fundamentals|Data Engineering Fundamentals]] — core data engineering concepts
