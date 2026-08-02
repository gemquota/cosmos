---
type: "concept"
title: "Graph and Time-Series Databases"
description: "Specialized stores for relationships and timestamped data"
tags: ["graph", "time-series", "databases", "specialized"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://en.wikipedia.org/wiki/Graph_database", "https://en.wikipedia.org/wiki/Time_series_database"]
---

# Graph and Time-Series Databases

## Summary

Graph databases optimize relationship traversal; time-series databases optimize ordered timestamped data.
Both deliver order-of-magnitude gains for their native workloads.
Choosing them is about matching engine strength to query pattern.
Specialized engines win by aligning storage layout with the query shape.

## Details

- Graphs: nodes, edges, and traversal queries (Neo4j, Gremlin, RDF stores).
- Time-series: append-heavy, bucket aggregation, retention (Timescale, InfluxDB, Prometheus).
- Graph workloads: fraud, social, knowledge graphs; mykb's graph is modeled here.
- Time-series workloads: metrics, IoT, financial ticks.
- General engines can do both, but specialized ones do it faster.
- Graph queries traverse relationships; time-series queries scan time ranges.
- Hybrid systems mix both for compound workloads.
- Specialized stores justify their existence by orders-of-magnitude gains on their native workloads.

## Related

- [[wiki/data-storage/timescaledb-and-postgres-extensions|Timescaledb And Postgres Extensions]] — time-series in Postgres
- [[wiki/data-storage/time-bucketing-and-rollups|Time Bucketing And Rollups]] — time aggregation
- [[wiki/data-storage/time-series-databases|Time-Series Databases]] — TSDB note
- [[wiki/data-storage/knowledge-graph|Knowledge Graph]] — graph usage
- [[wiki/data-storage/data-quality-dimensions|Data Quality Dimensions]] — quality dimensions
- [[wiki/data-storage/data-observability-and-monitoring|Data Observability and Monitoring]] — observability
- [[wiki/data-storage/data-testing-frameworks|Data Testing Frameworks]] — testing
- [[wiki/data-storage/feature-stores-and-ml-features|Feature Stores and ML Features]] — ML features
- [[wiki/data-storage/data-contracts-and-agreements|Data Contracts and Agreements]] — data contracts
- [[wiki/data-storage/incremental-loading-strategies|Incremental Loading Strategies]] — incremental loading
- [[wiki/data-storage/schema-evolution-in-streams|Schema Evolution In Streams]] — schema evolution

