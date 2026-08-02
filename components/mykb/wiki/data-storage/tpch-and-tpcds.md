---
type: "concept"
title: "TPC-H and TPC-DS"
description: "The standard OLAP benchmark suites"
tags: ["tpch", "tpcds", "benchmarks", "olap"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# TPC-H and TPC-DS

## Summary

A stub to be expanded into a full article; frames the concept and open questions.

## Details

- TPC-H models ad-hoc decision support with 22 queries over a star-ish schema.
- TPC-DS adds a realistic 7-table schema, more query templates, and skew.
- Scale factors (SF1 = 1GB) scale data; results include timings and cost.
- Use them as comparability baselines, not guarantees for your workload.

## Related

- [[wiki/data-storage/olap-vs-oltp|OLAP vs OLTP]] — OLAP context
- [[wiki/data-storage/data-warehouse-benchmarks|Data Warehouse Benchmarks]] — benchmark practice
- [[wiki/data-storage/benchmarking-and-tuned-queries|Benchmarking And Tuned Queries]] — tuning queries
- [[wiki/data-storage/data-sampling-and-approximate-queries|Data Sampling And Approximate Queries]] — scale considerations
- [[wiki/data-storage/data-engineering-fundamentals|Data Engineering Fundamentals]] — core data engineering concepts
