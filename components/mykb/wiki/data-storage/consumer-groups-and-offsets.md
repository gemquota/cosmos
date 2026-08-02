---
type: "concept"
title: "Consumer Groups and Offsets"
description: "How Kafka consumers coordinate to read partitions"
tags: ["kafka", "consumer-groups", "offsets", "streaming"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://kafka.apache.org/documentation/", "https://docs.confluent.io/platform/current/installation/configuration/consumer-configs.html"]
---

# Consumer Groups and Offsets

## Summary

Consumer groups split partitions among members so the group reads each partition once.
Offsets record each consumer's position, enabling resumes and replays.
Group coordination handles member churn via rebalancing.
Offset management is where delivery guarantees are actually implemented.

## Details

- Partition assignment: one partition per consumer at a time within a group.
- Auto-commit is convenient but can lose or duplicate messages.
- Manual commits align processing with side effects.
- Rebalancing redistributes partitions when members join or leave.
- Consumer lag is the key operational metric.
- Automate lag alerts; lag is the earliest signal of consumer trouble.
- Assign processing and commit boundaries deliberately.
- Treat offsets as state: version your consumer logic and commit policies like any other code.

## Related

- [[wiki/data-storage/kafka-architecture-and-partitioning|Kafka Architecture And Partitioning]] — partitions
- [[wiki/data-storage/consumer-rebalancing-and-assignment|Consumer Rebalancing And Assignment]] — rebalances
- [[wiki/data-storage/offset-commits-and-checkpointing|Offset Commits And Checkpointing]] — commit semantics
- [[wiki/data-storage/event-streaming-platforms|Event Streaming Platforms]] — platform
- [[wiki/data-storage/data-warehouse|Data Warehouse]] — warehouse reference

