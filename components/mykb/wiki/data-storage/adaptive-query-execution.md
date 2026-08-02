---
type: "concept"
title: "Adaptive Query Execution"
description: "Runtime query plan adjustment based on observed data statistics"
tags: ["spark", "aqe", "query-optimization", "runtime"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Adaptive Query Execution

## Summary

A stub to be expanded into a full article; frames the concept and open questions.

## Details

- AQE re-optimizes the plan mid-query using statistics from completed stages.
- Features: dynamic join strategy selection, skew join handling, and partition coalescing.
- It recovers plan quality when statistics were missing or stale.
- Enabled by default in modern Spark; visible in explain plans and UI.

## Related

- [[wiki/data-storage/cost-based-query-optimization|Cost-Based Query Optimization]] — optimizer concepts
- [[wiki/data-storage/query-tuning|Query Tuning]] — tuning practice
- [[wiki/data-storage/query-planning-and-optimization|Query Planning And Optimization]] — planning
- [[wiki/data-storage/data-skew-and-salting|Data Skew And Salting]] — skew handling
- [[wiki/data-storage/data-engineering-fundamentals|Data Engineering Fundamentals]] — core data engineering concepts
