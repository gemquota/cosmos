---
type: "concept"
title: "Data Architecture Layers"
description: "The staging, storage, processing, and serving layers of a data platform"
tags: ["layers", "architecture", "staging", "serving"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://www.databricks.com/glossary/medallion-architecture", "https://en.wikipedia.org/wiki/Data_lake"]
---

# Data Architecture Layers

## Summary

Data platforms are commonly described as layers: ingestion, storage, processing, and serving.
Each layer has distinct concerns, failure modes, and scaling behaviors.
Clear layer boundaries make platforms easier to operate and evolve.
Each layer has its own failure modes and scaling levers, which is why separating them simplifies operations.

## Details

- Ingestion moves data from sources into the platform (batch files, CDC, streaming).
- Storage holds data at rest: object stores, warehouses, and lakehouse tables.
- Processing transforms: orchestrated SQL, Spark, Flink, or dbt models.
- Serving delivers results: BI, APIs, feature stores, and ML inference.
- Governance and observability cut across every layer.
- Ownership per layer prevents blame games when incidents cross boundaries.
- Observability must span layers to trace a symptom to its root.
- Document each layer's SLAs, owners, and failure modes so operations can respond quickly when something breaks.

## Related

- [[wiki/data-storage/data-engineering-fundamentals|Data Engineering Fundamentals]] — layer overview
- [[wiki/data-storage/staging-vs-mart-tables|Staging Vs Mart Tables]] — staging vs serving
- [[wiki/data-storage/data-lake-zones-and-layouts|Data Lake Zones And Layouts]] — storage zones
- [[wiki/data-storage/data-pipeline-orchestration|Data Pipeline Orchestration]] — processing
- [[wiki/data-storage/data-observability|Data Observability]] — cross-cutting

