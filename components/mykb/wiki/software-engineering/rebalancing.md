---
type: "concept"
title: "Rebalancing"
description: "Redistributing partitions among consumers when the group changes"
tags: ["rebalancing", "consumer-groups", "kafka", "operations"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Rebalancing

## Summary
Rebalancing happens when consumers join, leave, or fail: the group coordinator reassigns partitions so work is shared again. During rebalance, consumption pauses and offsets can shift, so frequent rebalances hurt throughput.

## Details
- Eager rebalancing stops all consumers; incremental rebalancing (cooperative) moves fewer partitions.
- Long processing times cause rebalances on heartbeat expiry — tune timeouts and max poll.
- Watch rebalance frequency as a metric: churn often signals a stuck consumer.
- mykb relevance: parallel curation workers rebalance cleanly because each article is independent.

## Related
- [[wiki/software-engineering/consumer-groups|Consumer Groups]]
- [[wiki/software-engineering/partitioning-strategies|Partitioning Strategies]]
- [[wiki/software-engineering/offset-management|Offset Management]]
- [[wiki/api-protocols/kafka|Kafka]]
- [[wiki/software-engineering/lag-monitoring|Lag Monitoring]]
