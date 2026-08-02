---
type: "concept"
title: "Stream Processing Libraries"
description: "Library-level stream processing vs full platforms"
tags: ["streaming", "libraries", "kafka-streams", "processing"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Stream Processing Libraries

## Summary

A stub to be expanded into a full article; frames the concept and open questions.

## Details

- Libraries like Kafka Streams embed processing in your application; platforms like Flink run as clusters.
- Kafka Streams offers local state stores, exactly-once with transactions, and a familiar DSL.
- Libraries are easier to operate; platforms scale out and manage state/failover centrally.
- Choice depends on team, state size, and whether you want a separate processing tier.

## Related

- [[wiki/data-storage/stream-processing-engines|Stream Processing Engines]] — platform engines
- [[wiki/data-storage/exactly-once-semantics|Exactly-Once Semantics]] — guarantee spectrum
- [[wiki/data-storage/kafka-streams-and-ksql|Kafka Streams And Ksql]] — Kafka Streams specifics
- [[wiki/data-storage/flink-stream-processing|Flink Stream Processing]] — platform alternative
- [[wiki/data-storage/data-engineering-fundamentals|Data Engineering Fundamentals]] — core data engineering concepts
