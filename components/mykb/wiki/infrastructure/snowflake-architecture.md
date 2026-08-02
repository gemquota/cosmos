---
type: "concept"
title: "Snowflake Architecture"
description: "Three-layer warehouse: storage, compute, and cloud services"
tags: ["snowflake", "warehouse", "cloud", "saas"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Snowflake Architecture

## Summary

A stub to be expanded into a full article; frames the concept and open questions.

## Details

- Snowflake separates storage (compressed columnar files in object storage), compute (virtual warehouses), and services (metadata, optimization).
- Virtual warehouses scale independently and can be suspended, making compute pay-as-you-go.
- Time travel and fail-safe use retained snapshots; cloning is metadata-only.
- Shared-nothing engines query external stages, making Snowflake a data-cloud hub for structured data.

## Related

- [[wiki/data-storage/data-warehouse|Data Warehouse]] — warehouse fundamentals
- [[wiki/infrastructure/warehouse-clusters-and-virtual-warehouses|Warehouse Clusters And Virtual Warehouses]] — the virtual warehouse model
- [[wiki/data-storage/data-warehouse-benchmarks|Data Warehouse Benchmarks]] — how Snowflake performs in benchmarks
- [[wiki/data-storage/warehouse-optimization|Warehouse Optimization]] — tuning Snowflake workloads
- [[wiki/data-storage/data-engineering-fundamentals|Data Engineering Fundamentals]] — core data engineering concepts
