---
type: "concept"
title: "Bulkhead Pattern"
description: "Isolating failure domains by partitioning resources so one bad tenant or service cannot exhaust the rest"
tags: ["bulkhead", "resilience", "isolation", "patterns"]
timestamp: "2026-08-01T00:00:00Z"
status: "stub"
---

# Bulkhead Pattern

## Summary
The bulkhead pattern partitions resources — connection pools, threads, queues — by workload so a failure in one partition cannot starve the others.

## Details
- Separate pools per dependency, tenant, or priority class instead of one shared pool.
- Bulkheads bound blast radius: one partition exhausting its quota degrades only that partition.
- Costs: underutilized pools and tuning overhead across many partitions.
- Open question: how many partitions balance isolation against utilization.

## Related
- [[wiki/devops-infra/site-reliability-engineering|Site Reliability Engineering]] — isolation as a reliability tool
- [[wiki/devops-infra/chaos-engineering|Chaos Engineering]] — testing partition behavior
- [[wiki/infrastructure/circuit-breaker-pattern|Circuit Breaker Pattern]] — failing fast inside partitions
- [[wiki/infrastructure/retry-with-backoff|Retry with Backoff]] — behavior inside partitions
