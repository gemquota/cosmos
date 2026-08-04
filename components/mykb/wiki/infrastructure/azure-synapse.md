---
type: "entity"
title: "Azure Synapse Analytics"
description: "Microsoft's unified analytics service spanning SQL pools, Spark, and Pipelines"
tags: ["synapse", "azure", "warehouse", "lakehouse"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Azure Synapse Analytics

## Summary

Azure Synapse Analytics is Microsoft's unified analytics platform, combining dedicated SQL pools (the classic data warehouse), serverless SQL over data lakes, Apache Spark, and orchestration pipelines in one workspace. Its design goal is to remove the boundary between warehouse and lake: query the same data with either a provisioned MPP engine or a serverless engine, and move data between the two without a separate ETL tool.

## Details

- Synapse combines dedicated/pool SQL, serverless SQL over data lakes, Apache Spark, and orchestration. A Synapse workspace is a control plane over all four: SQL pools for warehousing workloads, a serverless SQL endpoint for ad-hoc queries over files in ADLS Gen2, Spark pools for data engineering and ML preprocessing, and Pipelines (built on Azure Data Factory) for orchestration. The integration means one identity model, one monitoring surface, and one metadata catalog (via the lake database) across all engines.
- Dedicated SQL pools are MPP engines with distributions; serverless SQL reads files directly. A dedicated pool shards each table across distributions (hash- or round-robin) and parallelizes queries across compute nodes — the classic massively parallel processing architecture, with the familiar tuning surface: distribution keys, partition schemes, and clustered columnstore indexes. Serverless SQL is the opposite model: no provisioning, pay-per-byte-scanned, and queries execute directly against Parquet/CSV/delta files in the lake, with the query engine pushing filters and projections down to the file format's metadata.
- Synapse Link enables near-real-time replication from operational stores like Cosmos DB. Instead of batch ETL, Synapse Link streams changes from operational databases into the analytical store continuously, so dashboards and reports see data minutes old rather than hours or days old. The tradeoff is cost and complexity: the link pipeline consumes throughput on the source store and adds a replication layer to reason about.
- It competes as Azure's hub for lakehouse and warehouse workloads with tight Microsoft ecosystem integration. If the stack is already Microsoft-centric (Entra ID, Power BI, Purview governance, ADLS storage), Synapse's integration is its moat; against Snowflake or Databricks, the comparison is about engine flexibility, cost model, and ecosystem fit rather than raw capability.
- For mykb: the node anchors the Azure branch of the warehouse/lakehouse cluster and connects MPP, lakehouse, and migration concepts to a concrete implementation.


## Related
- [[wiki/data-storage/data-warehouse|Data Warehouse]] — warehouse fundamentals
- [[wiki/data-storage/massively-parallel-processing|Massively Parallel Processing]] — MPP model used by SQL pools
- [[wiki/data-storage/sql-on-lakehouse|Sql On Lakehouse]] — serverless SQL over lake files
- [[wiki/infrastructure/warehouse-migration|Warehouse Migration]] — moving into Synapse
- [[wiki/data-storage/data-engineering-fundamentals|Data Engineering Fundamentals]] — core data engineering concepts
