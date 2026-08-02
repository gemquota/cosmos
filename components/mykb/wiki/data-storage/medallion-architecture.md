---
type: "concept"
title: "Medallion Architecture"
description: "The bronze-silver-gold layering pattern for lakehouses"
tags: ["medallion", "bronze-silver-gold", "lakehouse", "layers"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://www.databricks.com/glossary/medallion-architecture", "https://en.wikipedia.org/wiki/Data_lakehouse"]
---

# Medallion Architecture

## Summary

Medallion architecture organizes lakehouse data into bronze (raw), silver (cleansed), and gold (business-ready) layers.
Each layer is a physical, queryable dataset rather than a logical view, with clear ownership.
It gives teams a common vocabulary for data maturity inside the lake.
The medallion pattern makes data maturity explicit: everyone knows what bronze, silver, and gold mean.

## Details

- Bronze: append-only ingestion of source data with minimal transformation.
- Silver: deduplicated, typed, conformed data ready for analysis.
- Gold: aggregated marts and feature tables serving dashboards and ML.
- Layers are usually Delta/Iceberg tables, enabling time travel and re-processing.
- The pattern scales governance: access and quality tighten per layer.
- Automation should move data between layers; manual promotion is where quality leaks.
- Cost and freshness requirements can differ per layer, so treat them as separate tiers.
- Treat the boundaries between layers as contracts: changes to a layer's schema or semantics should be versioned and reviewed.

## Related

- [[wiki/data-storage/bronze-silver-gold|Bronze, Silver, Gold Layers]] — layer details
- [[wiki/data-storage/data-lake-zones-and-layouts|Data Lake Zones And Layouts]] — zone mapping
- [[wiki/data-storage/sql-on-lakehouse|Sql On Lakehouse]] — querying layers
- [[wiki/data-storage/lakehouse-architecture|Lakehouse Architecture]] — lakehouse note
- [[wiki/data-storage/open-table-formats|Open Table Formats]] — formats
- [[wiki/data-storage/data-quality-dimensions|Data Quality Dimensions]] — quality dimensions
- [[wiki/data-storage/data-observability-and-monitoring|Data Observability and Monitoring]] — observability
- [[wiki/data-storage/data-testing-frameworks|Data Testing Frameworks]] — testing
- [[wiki/data-storage/feature-stores-and-ml-features|Feature Stores and ML Features]] — ML features
- [[wiki/data-storage/data-contracts-and-agreements|Data Contracts and Agreements]] — data contracts
- [[wiki/data-storage/incremental-loading-strategies|Incremental Loading Strategies]] — incremental loading
- [[wiki/data-storage/schema-evolution-in-streams|Schema Evolution In Streams]] — schema evolution

