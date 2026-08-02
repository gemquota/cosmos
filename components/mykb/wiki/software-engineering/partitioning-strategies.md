---
type: "concept"
title: "Partitioning Strategies"
description: "Choosing how to split a topic or table across shards"
tags: ["partitioning", "sharding", "messaging", "databases"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Partitioning Strategies

## Summary
Partitioning strategies decide the shard key and count: hash on a key for even distribution, range for locality, or business key for grouping related records. The choice determines ordering, hotspots, and rebalance cost.

## Details
- Hash keys balance load but scatter related records; range keys cluster but skew under hot ranges.
- Cardinality and skew matter: a key with few values makes useless partitions.
- Partition count is mostly fixed early — choose with headroom and rebalance costs in mind.
- mykb relevance: articles partition by top-level dir, giving natural per-area shards.

## Related
- [[wiki/software-engineering/key-hashing|Key Hashing]]
- [[wiki/software-engineering/consumer-groups|Consumer Groups]]
- [[wiki/software-engineering/rebalancing|Rebalancing]]
- [[wiki/devops-infra/partitioning|Partitioning]]
- [[wiki/api-protocols/kafka|Kafka]]
