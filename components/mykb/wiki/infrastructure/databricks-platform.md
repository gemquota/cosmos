---
type: "entity"
title: "Databricks Platform"
description: "Unified lakehouse platform built on Spark with Delta Lake and managed ML"
tags: ["databricks", "spark", "lakehouse", "delta"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Databricks Platform

## Summary

Databricks is the reference implementation of the lakehouse pattern: a managed platform that runs Apache Spark clusters on cloud VMs, stores data in Delta Lake (an open table format over object storage), and layers governance (Unity Catalog), SQL warehouses, and ML tooling (MLflow) on top. Its bet is that one platform with open APIs can serve the full data lifecycle — ingestion, transformation, warehousing, and machine learning — without the warehouse/lake split.

## Details

- Databricks runs managed Spark clusters on cloud VMs with Unity Catalog governance and Delta Lake storage. The platform manages the cluster lifecycle (provisioning, autoscaling, spot usage, termination) so users write notebooks and jobs instead of managing Spark. Data lives in Delta Lake — Parquet files plus a transaction log — on the customer's own cloud storage (S3/ADLS/GCS), which keeps the data portable and the platform replaceable. Unity Catalog provides centralized governance: data discovery, lineage, and access control across all workspaces, the layer that made Databricks credible for enterprise adoption.
- The workspace model covers batch, structured streaming, SQL warehouses, notebooks, and MLflow. Batch jobs (Spark) handle transformations; Structured Streaming handles near-real-time ingestion; SQL warehouses are provisioned compute for BI queries over Delta tables; notebooks are the interactive development surface; MLflow manages the ML lifecycle (experiment tracking, model registry, deployment). The coverage is the point: teams do not leave the platform to move data from the lake to a warehouse or to operationalize models.
- Photonic engine and Delta performance features accelerate lakehouse queries. Photonic is Databricks' native vectorized execution engine that replaces the JVM Spark execution path for faster SQL; Delta adds performance features — data skipping via statistics, Z-ORDER clustering, liquid clustering, and optimized writes — that make the lakehouse competitive with traditional warehouses on query speed while keeping the lake's flexibility.
- It is the reference implementation of the lakehouse pattern with open APIs on top. The important architectural choice: Delta Lake, Spark, and MLflow are open (the formats are not lock-in), so the platform competes on managed experience rather than proprietary formats — and the tradeoff is that open formats mean the performance features are mostly open too, which is what makes the comparison with Snowflake (proprietary engine, managed warehouse) a real design choice.
- For mykb: the node anchors the lakehouse branch — connecting lakehouse architecture, open table formats, and SQL-on-lakehouse to a concrete platform.


## Related
- [[wiki/data-storage/lakehouse-architecture|Lakehouse Architecture]] — lakehouse pattern in practice
- [[wiki/data-storage/open-table-formats|Open Table Formats]] — Delta as an open format
- [[wiki/data-storage/delta-lake-and-merge-operations|Delta Lake And Merge Operations]] — Delta Lake specifics
- [[wiki/data-storage/sql-on-lakehouse|Sql On Lakehouse]] — SQL on the lakehouse
- [[wiki/data-storage/data-engineering-fundamentals|Data Engineering Fundamentals]] — core data engineering concepts
