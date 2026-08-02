---
type: "concept"
title: "Materialize and Differential Dataflow"
description: "Incremental view maintenance as a streaming engine"
tags: ["materialize", "differential-dataflow", "incremental", "sql"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Materialize and Differential Dataflow

## Summary

A stub to be expanded into a full article; frames the concept and open questions.

## Details

- Differential dataflow computes and maintains query results incrementally as inputs change.
- Materialize exposes SQL over this engine, materializing views that stay fresh.
- It suits low-latency operational analytics over frequently changing data.
- Complexity shifts to data volumes and join fan-out.

## Related

- [[wiki/data-storage/materialized-views|Materialized Views]] — materialization
- [[wiki/data-storage/stream-processing-engines|Stream Processing Engines]] — streaming
- [[wiki/data-storage/continuous-aggregates-and-materialized-views|Continuous Aggregates And Materialized Views]] — analog
- [[wiki/data-storage/stream-table-duality|Stream Table Duality]] — dynamic tables
- [[wiki/data-storage/data-engineering-fundamentals|Data Engineering Fundamentals]] — core data engineering concepts
