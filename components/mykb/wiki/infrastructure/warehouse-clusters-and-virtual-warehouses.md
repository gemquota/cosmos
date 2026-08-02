---
type: "concept"
title: "Warehouse Clusters and Virtual Warehouses"
description: "Compute units that scale independently of storage"
tags: ["warehouse", "clusters", "virtual-warehouses", "snowflake"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Warehouse Clusters and Virtual Warehouses

## Summary

A stub to be expanded into a full article; frames the concept and open questions.

## Details

- Virtual warehouses are isolated compute pools over shared storage (Snowflake model).
- Clusters in Redshift/Databricks tie compute to a fixed or elastic footprint.
- Scaling up (bigger nodes) vs out (more nodes) changes concurrency and cost.
- Auto-suspend/resume and auto-scaling cut idle cost.

## Related

- [[wiki/data-storage/data-warehouse|Data Warehouse]] — warehouse model
- [[wiki/infrastructure/snowflake-architecture|Snowflake Architecture]] — virtual warehouse example
- [[wiki/infrastructure/on-demand-vs-reserved-compute|On Demand Vs Reserved Compute]] — pricing models
- [[wiki/infrastructure/t-shirt-sizing-and-resource-models|T Shirt Sizing And Resource Models]] — sizing
- [[wiki/data-storage/data-engineering-fundamentals|Data Engineering Fundamentals]] — core data engineering concepts
