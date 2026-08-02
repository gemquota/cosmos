---
type: "concept"
title: "Bulkhead Isolation"
description: "Partitioning resources so failure in one pool cannot starve another"
tags: ["bulkhead", "isolation", "resilience", "concurrency"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Bulkhead Isolation

## Summary
Bulkheads split capacity into independent pools — connection pools per tenant, thread pools per workload — so one overloaded consumer cannot exhaust shared resources. The name comes from ship compartments that contain flooding.

## Details
- Apply at the resource layer: per-dependency connection pools, per-queue workers, per-tenant quotas.
- Decide pool sizes from worst-case need: too small causes false scarcity, too large defeats the purpose.
- Bulkheading pairs with timeouts and circuit breakers for defense in depth.
- mykb relevance: separate agent quota pools per task class so one long article run cannot starve all work.

## Related
- [[wiki/api-protocols/bulkhead-pattern|Bulkhead Pattern]]
- [[wiki/dev-tools/concurrency-limiters|Concurrency Limiters]]
- [[wiki/software-engineering/thread-pools|Thread Pools]]
- [[wiki/dev-tools/timeout-policy|Timeout Policy]]
- [[wiki/software-engineering/reliability-engineering|Reliability Engineering]]
