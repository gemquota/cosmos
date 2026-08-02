---
type: "concept"
title: "Spark: Batch and Streaming"
description: "Unified large-scale processing on one engine"
tags: ["spark", "batch", "streaming", "distributed-compute"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://spark.apache.org/docs/latest/", "https://en.wikipedia.org/wiki/Apache_Spark"]
---

# Spark: Batch and Streaming

## Summary

Apache Spark is a distributed compute engine for large-scale batch and streaming workloads.
Its DataFrame API and SQL unify processing across data sources.
Spark is the workhorse of modern data platforms.
Spark's unified model means one set of skills and code patterns spans batch and streaming.

## Details

- Resilient Distributed Datasets (RDDs) and DataFrames abstract distributed collections.
- Structured Streaming provides micro-batch and continuous modes.
- Catalyst optimizer and Tungsten execution accelerate SQL.
- Runs on standalone, YARN, and Kubernetes clusters.
- Lakehouse integrations (Delta, Iceberg) are first-class.
- Cluster sizing and shuffle tuning dominate real-world Spark performance.
- Lakehouse integrations make Spark the default lake processor.
- Spark remains the default engine for lakehouse ETL because of its maturity and ecosystem.

## Related

- [[wiki/data-storage/spark-sql-and-dataframes|Spark Sql And Dataframes]] — SQL layer
- [[wiki/data-storage/spark-structured-streaming|Spark Structured Streaming]] — streaming
- [[wiki/data-storage/resource-scheduling-in-spark|Resource Scheduling In Spark]] — scheduling
- [[wiki/data-storage/stream-processing-engines|Stream Processing Engines]] — engines
- [[wiki/infrastructure/databricks-platform|Databricks Platform]] — managed Spark
- [[wiki/data-storage/data-warehouse|Data Warehouse]] — warehouse reference

