---
type: "concept"
title: "T-Shirt Sizing and Resource Models"
description: "Choosing warehouse sizes without precise demand forecasts"
tags: ["sizing", "capacity-planning", "warehouse", "resource-model"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# T-Shirt Sizing and Resource Models

## Summary

A stub to be expanded into a full article; frames the concept and open questions.

## Details

- T-shirt tiers (XS-XXL) map to node counts, memory, and concurrency.
- Right-size by workload type: dashboard queries need concurrency, ETL needs throughput.
- Measure utilization, queue wait, and latency before resizing.
- Reserved capacity discounts favor stable tiers; serverless suits variable load.

## Related

- [[wiki/data-storage/massively-parallel-processing|Massively Parallel Processing]] — compute model
- [[wiki/infrastructure/warehouse-clusters-and-virtual-warehouses|Warehouse Clusters And Virtual Warehouses]] — cluster model
- [[wiki/infrastructure/on-demand-vs-reserved-compute|On Demand Vs Reserved Compute]] — pricing
- [[wiki/data-storage/data-warehouse-benchmarks|Data Warehouse Benchmarks]] — benchmark data
- [[wiki/data-storage/data-engineering-fundamentals|Data Engineering Fundamentals]] — core data engineering concepts
