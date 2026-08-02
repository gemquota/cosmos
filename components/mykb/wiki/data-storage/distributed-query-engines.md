---
type: "concept"
title: "Distributed Query Engines"
description: "Querying data across many sources and nodes"
tags: ["distributed-query", "trino", "presto", "engines"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://trino.io/docs/current/", "https://prestodb.io/docs/current/"]
---

# Distributed Query Engines

## Summary

Distributed query engines run SQL across large clusters and many data sources.
They federate warehouses, lakes, and operational stores.
Separation of compute from storage makes them elastic.
Separation of compute from storage makes query engines the flexible hub of the data platform.

## Details

- Engines like Trino and Presto split queries into distributed tasks.
- Connectors expose sources as SQL tables.
- Pushdown keeps work close to data where possible.
- They shine for ad-hoc analytics over lakes.
- Not designed for OLTP write workloads.
- Connector quality varies; test pushdown support per source.
- Use them for analytics, not for OLTP traffic.
- Query engines give analysts one SQL surface over the entire data estate.

## Related

- [[wiki/data-storage/presto-and-trino|Presto And Trino]] — flagship engines
- [[wiki/data-storage/sql-on-lakehouse|Sql On Lakehouse]] — lake queries
- [[wiki/data-storage/federated-queries-across-sources|Federated Queries Across Sources]] — federation
- [[wiki/data-storage/sql-engines|SQL Engine Architecture]] — engines
- [[wiki/data-storage/mpp-engines-and-distributed-sql|Mpp Engines And Distributed Sql]] — MPP family
- [[wiki/data-storage/data-quality-dimensions|Data Quality Dimensions]] — quality dimensions
- [[wiki/data-storage/data-observability-and-monitoring|Data Observability and Monitoring]] — observability
- [[wiki/data-storage/data-testing-frameworks|Data Testing Frameworks]] — testing
- [[wiki/data-storage/feature-stores-and-ml-features|Feature Stores And Ml Features]] — ML features
- [[wiki/data-storage/data-contracts-and-agreements|Data Contracts and Agreements]] — data contracts
- [[wiki/data-storage/incremental-loading-strategies|Incremental Loading Strategies]] — incremental loading
- [[wiki/data-storage/schema-evolution-in-streams|Schema Evolution In Streams]] — schema evolution
- [[wiki/data-storage/data-warehouse|Data Warehouse]] — warehouse reference

