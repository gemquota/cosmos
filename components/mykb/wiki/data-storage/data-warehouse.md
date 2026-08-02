---
type: "concept"
title: "Data Warehouse"
description: "Subject-oriented integrated analytical stores"
tags: ["data-warehouse", "olap", "analytics", "business-intelligence"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://en.wikipedia.org/wiki/Data_warehouse", "https://clickhouse.com/docs/en/intro"]
---

# Data Warehouse

## Summary
A data warehouse is a centralized, read-optimized store built for analysis: subject-oriented, integrated, time-variant, and non-volatile data drawn from operational sources. Warehouses favor columnar storage, star schemas, and massive parallel processing so BI queries scan billions of rows quickly.

## Details
- **Design traits** — data is organized by subject (sales, inventory) rather than application, integrated across source systems with consistent codes and keys, versioned over time, and loaded in batches.
- **ETL/ELT pipeline** — source data is extracted, transformed (cleaned, conformed), and loaded; modern warehouses increasingly receive raw data first (ELT) and transform inside the engine with SQL or dbt.
- **Physical design** — columnar compression, zone maps, and projections (ClickHouse) or sort keys and automatic clustering (Snowflake, Redshift) cut I/O; massively parallel engines fan queries across nodes.
- **Modeling** — star and snowflake schemas with fact tables and conformed dimensions; slowly changing dimensions track history; aggregates and materialized views accelerate common reports.
- **Warehouse vs lake** — warehouses enforce schema and SQL semantics with ACID (or snapshot) guarantees; lakes store raw files cheaply. Lakehouses merge the two using open table formats.
- **Operational reality** — freshness, load windows, and transformation DAGs dominate warehouse maintenance; observability on row counts and run times prevents silent data quality decay.

## Related
- [[wiki/data-storage/olap-vs-oltp|OLAP vs OLTP]] — why warehouse engines differ
- [[wiki/data-storage/dimensional-modeling|Dimensional Modeling]] — star schemas inside the warehouse
- [[wiki/data-storage/columnar-storage|Columnar Storage]] — the physical layout
- [[wiki/data-storage/etl-vs-elt|ETL vs ELT]] — how data arrives
- [[wiki/data-storage/data-lake|Data Lake]] — the cheaper raw-storage alternative
- [[wiki/data-storage/lakehouse-architecture|Lakehouse Architecture]] — the warehouse/lake hybrid
