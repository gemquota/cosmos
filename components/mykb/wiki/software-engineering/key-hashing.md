---
type: "concept"
title: "Key Hashing"
description: "Mapping keys to partitions via a hash function for even distribution"
tags: ["partitioning", "hashing", "sharding", "design"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Key Hashing

## Summary
Key hashing sends each message or row to the partition hash(key) % N, giving even load when keys are diverse. It preserves per-key ordering and lets consumers scale by partition, at the price of no cross-key grouping.

## Details
- Use stable hashes (consistent hashing for resizing) so repartitioning does not scatter everything.
- Hot keys still skew: hash the key but detect and split hot keys deliberately.
- Hash collisions are fine for routing; they are the mechanism, not a bug.
- mykb relevance: article slugs hash to shards, keeping per-area reads local.

## Related
- [[wiki/software-engineering/partitioning-strategies|Partitioning Strategies]]
- [[wiki/software-engineering/consumer-groups|Consumer Groups]]
- [[wiki/software-engineering/rebalancing|Rebalancing]]
- [[wiki/tooling/consensus-algorithms|Consensus Algorithms]]
- [[wiki/api-protocols/kafka|Kafka]]
