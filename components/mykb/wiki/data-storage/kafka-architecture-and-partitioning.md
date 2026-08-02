---
type: "concept"
title: "Kafka Architecture and Partitioning"
description: "Brokers, topics, partitions, and replication inside Kafka"
tags: ["kafka", "architecture", "partitioning", "replication"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://kafka.apache.org/documentation/", "https://en.wikipedia.org/wiki/Apache_Kafka"]
---

# Kafka Architecture and Partitioning

## Summary

Kafka clusters are composed of brokers storing partitioned topics.
Partitions are the unit of parallelism, ordering, and replication.
Understanding partitioning is key to Kafka performance and semantics.
Partition count and key design are the decisions you live with; changes mean rebalancing.

## Details

- Each partition is an ordered log replicated across brokers (leader/followers).
- Keys hash to partitions, preserving per-key order.
- Partition count bounds parallelism and consumer scale-out.
- Replication factor trades durability against storage cost.
- KRaft replaced ZooKeeper for metadata in modern Kafka.
- Replication factor 3 with min-isr settings is the common production baseline.
- Monitor leader balance and under-replicated partitions.
- Capacity planning for Kafka starts with partition throughput and retention, not with node count.

## Related

- [[wiki/data-storage/kafka-and-event-streams|Kafka and Event Streams]] — platform
- [[wiki/data-storage/consumer-groups-and-offsets|Consumer Groups and Offsets]] — consumers
- [[wiki/data-storage/compaction-and-retention-kafka|Compaction And Retention Kafka]] — retention
- [[wiki/data-storage/event-streaming-platforms|Event Streaming Platforms]] — platforms
- [[wiki/data-storage/consistent-hashing-and-ring-topology|Consistent Hashing And Ring Topology]] — distribution ideas
- [[wiki/data-storage/data-warehouse|Data Warehouse]] — warehouse reference

