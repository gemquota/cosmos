---
type: "entity"
title: "Kafka and Event Streams"
description: "The distributed log that became the standard for event streaming"
tags: ["kafka", "event-streaming", "log", "messaging"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://kafka.apache.org/documentation/", "https://en.wikipedia.org/wiki/Apache_Kafka"]
---

# Kafka and Event Streams

## Summary

Apache Kafka is a distributed, partitioned, replicated commit log.
It decouples producers and consumers with durable, replayable event streams.
Kafka is the de facto backbone of modern event-driven architectures.
Kafka's log model made replay and reprocessing standard capabilities rather than afterthoughts.

## Details

- Topics partition events for parallelism and ordering per key.
- Consumers track offsets, enabling replay and exactly-once patterns.
- Log compaction retains the latest value per key.
- Kafka Streams and ksqlDB process events inside the ecosystem.
- Managed options (MSK, Confluent) reduce operations burden.
- Topic design (partition keys, retention) determines most operational outcomes.
- The ecosystem spans connectors, stream processing, and schema governance.
- Kafka's durability and replay semantics make it the substrate for both messaging and stream processing.

## Related

- [[wiki/data-storage/kafka-architecture-and-partitioning|Kafka Architecture And Partitioning]] — internals
- [[wiki/data-storage/consumer-groups-and-offsets|Consumer Groups and Offsets]] — consumption
- [[wiki/data-storage/exactly-once-processing|Exactly-Once Processing]] — guarantees
- [[wiki/data-storage/event-streaming-platforms|Event Streaming Platforms]] — platform
- [[wiki/data-storage/message-queues|Message Queues]] — queue vs log
- [[wiki/data-storage/data-quality-dimensions|Data Quality Dimensions]] — quality dimensions
- [[wiki/data-storage/data-observability-and-monitoring|Data Observability and Monitoring]] — observability
- [[wiki/data-storage/data-testing-frameworks|Data Testing Frameworks]] — testing
- [[wiki/data-storage/feature-stores-and-ml-features|Feature Stores and ML Features]] — ML features
- [[wiki/data-storage/data-contracts-and-agreements|Data Contracts and Agreements]] — data contracts
- [[wiki/data-storage/incremental-loading-strategies|Incremental Loading Strategies]] — incremental loading
- [[wiki/data-storage/schema-evolution-in-streams|Schema Evolution In Streams]] — schema evolution
- [[wiki/data-storage/streaming-sinks-and-sources|Streaming Sinks And Sources]] — streams

