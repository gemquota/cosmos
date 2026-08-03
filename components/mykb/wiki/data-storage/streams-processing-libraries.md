---
type: "concept"
title: "Stream Processing Libraries"
description: "Library-level stream processing vs full platforms"
tags: ["streaming", "libraries", "kafka-streams", "processing"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Stream Processing Libraries

## Summary
Stream processing libraries like Kafka Streams embed processing inside your application, while platforms like Flink run as separate clusters. Libraries offer local state stores, exactly-once with transactions, and a familiar DSL; platforms scale out and manage state and failover centrally.

## Details
- Mechanism: Kafka Streams runs as a library in your service — topology DSL (map, filter, aggregate) connects processors; state stores live locally with changelog topics for recovery; exactly-once is achieved via transactional producers and consumer offsets committed atomically; Flink runs a cluster of task managers with distributed checkpointed state and central job management.
- Concrete example: an app embeds Kafka Streams to aggregate wiki events into per-article counters with a local state store; a Flink cluster runs the same aggregation at higher scale with checkpointing; a team chooses the library to avoid operating a processing tier, or the platform when state and parallelism outgrow one service.
- Failure modes: library-side state recovery mishandled (changelog lag after restart); scaling a library horizontally requires re-partitioning and careful state management; platform operations (checkpoint tuning, backpressure, job restarts) becoming the burden; mixing both paradigms in one pipeline and losing consistency guarantees.
- Tradeoffs: libraries are easier to operate and integrate (one deployable, one language) but bound state and parallelism to the application; platforms scale and manage state/failover centrally at the cost of a cluster to run; the choice depends on team, state size, and whether a separate processing tier is welcome.
- Operational notes: monitor consumer lag and state store size, test exactly-once behavior under restarts, and document the processing topology.
- RSIS3 relevance: RSIS3's event processing (pulse aggregation, curation counts) fits a library-level stream processor — embedded, easy to operate, exactly-once where it matters.

## Related

- [[wiki/data-storage/stream-processing-engines|Stream Processing Engines]] — platform engines
- [[wiki/data-storage/exactly-once-semantics|Exactly-Once Semantics]] — guarantee spectrum
- [[wiki/data-storage/kafka-streams-and-ksql|Kafka Streams And Ksql]] — Kafka Streams specifics
- [[wiki/data-storage/flink-stream-processing|Flink Stream Processing]] — platform alternative
- [[wiki/data-storage/data-engineering-fundamentals|Data Engineering Fundamentals]] — core data engineering concepts
