---
type: "concept"
title: "Sharding"
description: "Splitting data across multiple database instances by key to scale write and storage capacity"
tags: ["sharding", "database", "scaling", "distributed-systems", "data"]
timestamp: "2026-07-31T00:00:00Z"
status: "stub"
---

# Sharding

## Summary
Sharding distributes rows across multiple database nodes by a shard key, scaling beyond a single node's limits. Each shard serves a subset; queries must route by key or fan out.

## Details
- Choose a high-cardinality, evenly distributed shard key; bad keys cause hot spots.
- Cross-shard joins and transactions get expensive — design aggregates to live on one shard.
- Reach for sharding late: replication, partitioning, and caching solve most scale problems first.

## Related
- [[wiki/devops-infra/replication|Replication]] — scale reads before sharding
- [[wiki/devops-infra/partitioning|Partitioning]] — intra-node data layout
- [[wiki/devops-infra/mongodb|MongoDB]] — native sharding
- [[wiki/devops-infra/acid|ACID]] — cross-shard consistency limits
- [[wiki/devops-infra/postgresql|PostgreSQL]] — sharding approaches
- [[wiki/devops-infra/observability|Observability]] — hot-shard and skew monitoring
