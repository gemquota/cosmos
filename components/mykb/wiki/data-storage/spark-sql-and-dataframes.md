---
type: "concept"
title: "Spark SQL and DataFrames"
description: "Declarative analytics on the Spark engine"
tags: ["spark-sql", "dataframes", "spark", "analytics"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://spark.apache.org/docs/latest/", "https://en.wikipedia.org/wiki/Apache_Spark"]
---

# Spark SQL and DataFrames

## Summary

Spark SQL runs standard SQL over DataFrames with a cost-based optimizer.
DataFrames give a typed, programmatic API with the same engine.
Together they unify ETL and analytics on one platform.
Spark SQL gives analysts SQL and engineers an API over the same optimized engine.

## Details

- Catalyst optimizer rewrites and optimizes query plans.
- Tungsten accelerates execution with code generation.
- DataFrames support batch, streaming, and ML pipelines.
- Connectors cover lakes, warehouses, and JDBC sources.
- Spark SQL is the lingua franca of lakehouse engineering.
- DataFrame APIs catch type errors at compile time.
- Tune shuffles and partitioning for job-level gains.
- Spark SQL turns distributed compute into a familiar SQL interface for the whole team.

## Related

- [[wiki/data-storage/spark-batch-and-streaming|Spark: Batch and Streaming]] — engine
- [[wiki/data-storage/sql-on-lakehouse|Sql On Lakehouse]] — lakehouse SQL
- [[wiki/data-storage/dataframes-in-production|Dataframes In Production]] — production
- [[wiki/data-storage/sql-engines|SQL Engine Architecture]] — engines
- [[wiki/data-storage/spark-tuning-and-shuffle-optimization|Spark Tuning And Shuffle Optimization]] — tuning
- [[wiki/data-storage/data-warehouse|Data Warehouse]] — warehouse reference

