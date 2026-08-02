---
type: "concept"
title: "Read Replicas and Scaling"
description: "Scaling read throughput with replica databases"
tags: ["read-replicas", "scaling", "replication", "databases"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ReadRepl.html", "https://www.postgresql.org/docs/current/hot-standby.html"]
---

# Read Replicas and Scaling

## Summary

Read replicas serve read traffic from copies of the primary.
They scale analytical and reporting load off the writer.
Replication lag bounds how fresh replica reads are.
Read replicas scale reads but not writes; pair them with caching and sharding for full scale-out.

## Details

- Replicas reduce contention on the primary for read-heavy workloads.
- Route read-only traffic explicitly; mixed traffic breaks semantics.
- Lag causes stale reads; monitor lag as a top metric.
- Failover can promote a replica in managed services.
- Replica count is bounded by replication cost and lag.
- Route by statement type to keep consistency guarantees.
- Monitor replica lag as a first-class health metric.
- Read scaling is the first and cheapest step in database scale-out.

## Related

- [[wiki/data-storage/replication-mechanisms|Replication Mechanisms]] — mechanics
- [[wiki/api-services/read-your-writes-and-consistency-apis|Read Your Writes And Consistency Apis]] — consistency
- [[wiki/data-storage/cache-aside-and-write-through|Cache-Aside and Write-Through]] — caching alternative
- [[wiki/data-storage/replication-strategies|Replication Strategies]] — strategies
- [[wiki/data-storage/database-replication-revisited|Database Replication Revisited]] — deep dive
- [[wiki/data-storage/data-quality-dimensions|Data Quality Dimensions]] — quality dimensions
- [[wiki/data-storage/data-observability-and-monitoring|Data Observability and Monitoring]] — observability
- [[wiki/data-storage/data-testing-frameworks|Data Testing Frameworks]] — testing
- [[wiki/data-storage/feature-stores-and-ml-features|Feature Stores and ML Features]] — ML features
- [[wiki/data-storage/data-contracts-and-agreements|Data Contracts and Agreements]] — data contracts
- [[wiki/data-storage/incremental-loading-strategies|Incremental Loading Strategies]] — incremental loading
- [[wiki/data-storage/schema-evolution-in-streams|Schema Evolution In Streams]] — schema evolution
- [[wiki/data-storage/data-warehouse|Data Warehouse]] — warehouse reference

