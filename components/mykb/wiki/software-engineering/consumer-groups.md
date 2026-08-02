---
type: "concept"
title: "Consumer Groups"
description: "Partitioning message consumption across a set of cooperating consumers"
tags: ["consumer-groups", "kafka", "messaging", "scaling"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Consumer Groups

## Summary
Consumer groups split a topic's partitions among members so each message goes to exactly one group member, letting teams scale processing horizontally. Kafka and similar brokers use groups for load distribution and failover.

## Details
- Reassignments (rebalances) happen on join/leave; they pause processing — keep them rare.
- Order is per partition, not per topic: keyed messages route to the same partition.
- Group lag is the health metric: monitor lag per group, not per consumer.
- mykb relevance: parallel wiki ingestion can run N consumers over one topic with a group.

## Related
- [[wiki/software-engineering/partitioning-strategies|Partitioning Strategies]]
- [[wiki/software-engineering/lag-monitoring|Lag Monitoring]]
- [[wiki/software-engineering/rebalancing|Rebalancing]]
- [[wiki/api-protocols/kafka|Kafka]]
- [[wiki/software-engineering/offset-management|Offset Management]]
