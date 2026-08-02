---
type: "concept"
title: "Active-Active"
description: "Running and serving traffic from multiple sites simultaneously"
tags: ["active-active", "multi-region", "availability", "architecture"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Active-Active

## Summary
Active-active architectures serve real traffic from two or more sites at once, spreading load and letting any site fail without downtime. The price is distributed state: writes must replicate and conflicts must be resolved.

## Details
- Read-heavy workloads go active-active easily; multi-writer active-active needs conflict resolution.
- Split-brain protection matters: partitions must not let both sides serve stale authority.
- Health-based steering routes around a failed site automatically.
- mykb relevance: wiki mirrors can be active-active for reads with a single writer.

## Related
- [[wiki/tooling/active-passive|Active-Passive]]
- [[wiki/tooling/multi-region|Multi-Region]]
- [[wiki/tooling/geo-redundancy|Geo-Redundancy]]
- [[wiki/tooling/distributed-consistency|Distributed Consistency]]
- [[wiki/compositions/conflict-resolution-strategies|Conflict Resolution Strategies]]
