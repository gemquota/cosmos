---
type: "concept"
title: "Explain Plans and Profiling"
description: "Reading query plans and finding bottlenecks"
tags: ["explain", "query-plan", "profiling", "debugging"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Explain Plans and Profiling

## Summary

A stub to be expanded into a full article; frames the concept and open questions.

## Details

- EXPLAIN shows the plan: joins, scans, filters, and estimated costs.
- EXPLAIN ANALYZE adds actual timings and row counts for comparison.
- Look for scans larger than needed, bad join order, and spills.
- Profiling tools (UI stages, per-operator metrics) localize the bottleneck.

## Related

- [[wiki/data-storage/query-tuning|Query Tuning]] — tuning workflow
- [[wiki/data-storage/cost-based-query-optimization|Cost-Based Query Optimization]] — plan theory
- [[wiki/data-storage/query-planning-and-optimization|Query Planning And Optimization]] — plan generation
- [[wiki/data-storage/data-observability-and-monitoring|Data Observability And Monitoring]] — observability
- [[wiki/data-storage/data-engineering-fundamentals|Data Engineering Fundamentals]] — core data engineering concepts
