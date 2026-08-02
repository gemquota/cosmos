---
type: "concept"
title: "Data Engineering Fundamentals"
description: "The discipline of building systems that collect, store, and process data"
tags: ["data-engineering", "pipelines", "architecture", "fundamentals"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://en.wikipedia.org/wiki/Data_engineering", "https://en.wikipedia.org/wiki/Data_pipeline"]
---

# Data Engineering Fundamentals

## Summary

Data engineering is the practice of designing, building, and operating the systems that move, store, and prepare data for analysis and machine learning.
It sits between source systems and consumers: analysts, dashboards, data scientists, and applications.
Core concerns are reliability, correctness, freshness, and cost, which together make data trustworthy enough to act on.
Good data engineering is invisible when it works: consumers get fresh, correct data without thinking about the machinery behind it.

## Details

- The stack spans ingestion, storage, transformation, orchestration, and serving layers.
- Batch pipelines (scheduled SQL/spark jobs) and streaming pipelines (Kafka/Flink) are the two dominant processing models.
- Storage choices range from OLTP databases to warehouses, lakes, and lakehouses, each tuned for different workloads.
- Data quality, lineage, and observability are first-class concerns, not afterthoughts.
- In the mykb context, the knowledge graph is itself a data pipeline: sources, extraction, curation, and graph storage.
- Bottlenecks are usually organizational before technical: unclear ownership, missing SLAs, and unmeasured quality.
- A personal knowledge base like mykb applies the same discipline to its own pipelines, from raw notes to curated graph entries.
- The field rewards breadth: databases, distributed systems, SQL, and software engineering all meet in production data platforms.

## Related

- [[wiki/data-storage/pipelines|Pipelines]] — the core unit of data work
- [[wiki/data-storage/data-warehousing-concepts|Data Warehousing Concepts]] — warehouse layer
- [[wiki/data-storage/data-lake-architecture|Data Lake Architecture]] — lake layer
- [[wiki/data-storage/data-pipeline-orchestration|Data Pipeline Orchestration]] — orchestration
- [[wiki/data-storage/data-quality-checks|Data Quality Checks]] — quality
- [[wiki/infrastructure/data-eng-skills-matrix|Data Eng Skills Matrix]] — skills for the role
- [[wiki/data-storage/data-quality-dimensions|Data Quality Dimensions]] — quality dimensions
- [[wiki/data-storage/data-observability-and-monitoring|Data Observability And Monitoring]] — observability
- [[wiki/data-storage/data-testing-frameworks|Data Testing Frameworks]] — testing
- [[wiki/data-storage/feature-stores-and-ml-features|Feature Stores And Ml Features]] — ML features
- [[wiki/data-storage/data-contracts-and-agreements|Data Contracts and Agreements]] — data contracts
- [[wiki/data-storage/incremental-loading-strategies|Incremental Loading Strategies]] — incremental loading
- [[wiki/data-storage/schema-evolution-in-streams|Schema Evolution In Streams]] — schema evolution

