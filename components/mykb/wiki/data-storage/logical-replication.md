---
type: "concept"
title: "Logical Replication"
description: "Replicating data by logical changes, decoupled from storage format"
tags: ["logical-replication", "postgres", "replication", "streaming"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://www.postgresql.org/docs/current/logical-replication.html", "https://en.wikipedia.org/wiki/Replication_(computing)"]
---

# Logical Replication

## Summary

Logical replication publishes a stream of logical row changes (insert/update/delete) to subscribers.
It is format-agnostic: subscribers can be different database versions or even other systems.
It underpins modern CDC and multi-node Postgres setups.
Logical replication is the bridge between operational databases and the event streaming world.

## Details

- Postgres publishes via replication slots; subscribers apply changes with transactional atomicity.
- Logical decoding is the foundation for tools like Debezium.
- Replication slots must be monitored: unconsumed slots grow WAL.
- Schema changes are not automatically replicated; plan for them.
- It enables selective table replication and version-skewed replicas.
- Replication slots and publication/subscription configuration need capacity planning.
- Conflict resolution policies matter when multiple writers are involved.
- Logical replication bridges databases and streams, so pair it with schema governance to keep both sides compatible.

## Related

- [[wiki/data-storage/change-data-capture|Change Data Capture]] — logical decoding as CDC
- [[wiki/data-storage/replication-mechanisms|Replication Mechanisms]] — mechanism family
- [[wiki/data-storage/read-replicas-and-scaling|Read Replicas And Scaling]] — use cases
- [[wiki/data-storage/multi-leader-replication|Multi-Leader Replication]] — topologies
- [[wiki/data-storage/schema-evolution-in-streams|Schema Evolution In Streams]] — schema change handling
- [[wiki/data-storage/data-quality-dimensions|Data Quality Dimensions]] — quality dimensions
- [[wiki/data-storage/data-observability-and-monitoring|Data Observability and Monitoring]] — observability
- [[wiki/data-storage/data-testing-frameworks|Data Testing Frameworks]] — testing
- [[wiki/data-storage/feature-stores-and-ml-features|Feature Stores and ML Features]] — ML features
- [[wiki/data-storage/data-contracts-and-agreements|Data Contracts and Agreements]] — data contracts
- [[wiki/data-storage/incremental-loading-strategies|Incremental Loading Strategies]] — incremental loading
- [[wiki/data-storage/streaming-sinks-and-sources|Streaming Sinks And Sources]] — streams
- [[wiki/data-storage/data-warehouse|Data Warehouse]] — warehouse reference

