---
type: "concept"
title: "Bulkhead Pattern"
description: "Failure isolation between dependencies"
tags: ["bulkhead", "failure-isolation", "reliability", "resilience", "architecture"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://learn.microsoft.com/en-us/azure/architecture/patterns/bulkhead", "https://martinfowler.com/bliki/Bulkhead.html"]
---

# Bulkhead Pattern

## Summary
The bulkhead pattern isolates failures by partitioning resources: each downstream dependency gets its own connection pool, thread pool, or queue, so one slow or failing dependency cannot exhaust shared capacity. Named after ship compartments, it trades total capacity for bounded blast radius.

## Details
- Mechanism: split the shared resource pool (threads, connections, semaphores) into per-dependency (or per-tenant) partitions with separate limits.
- Example: three upstream services each get a 10-thread pool instead of one shared 30-thread pool; service A hanging cannot starve B and C.
- Why it beats a single pool: shared pools let one misbehaving dependency consume everything, degrading the whole service (the thundering herd of threads).
- Variants: connection pools per host, thread pools per client, semaphores per queue, and per-tenant partitions for multi-tenant isolation.
- Trade-off: partitioning reduces utilization — idle partitions cannot lend capacity to busy ones — so size partitions from real traffic ratios.
- Combines with: circuit breakers (stop calls to dead dependencies), timeouts (bound partition wait), and concurrency limits.
- Kubernetes notes: pod-level limits plus per-dependency bulkheads give both horizontal and vertical isolation.

## Related
- [[wiki/api-protocols/circuit-breaker|Circuit Breaker]] — failing fast when a partition is saturated
- [[wiki/api-protocols/concurrency-limits|Concurrency Limits]] — per-partition in-flight caps
- [[wiki/api-protocols/timeouts|Timeouts]] — bounding wait inside a partition
- [[wiki/infrastructure/bulkhead-pattern|Bulkhead Pattern (Infra)]] — the infrastructure-side variant
- [[wiki/api-protocols/load-shedding|Load Shedding]] — rejecting work instead of queueing forever
