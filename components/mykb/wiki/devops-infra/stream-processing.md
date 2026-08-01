---
type: "concept"
title: "Stream Processing"
description: "Computing over live event streams: filtering, aggregating, and joining as data flows"
tags: ["stream-processing", "flink", "kafka", "real-time"]
timestamp: "2026-08-01T00:00:00Z"
status: "stub"
---

# Stream Processing

## Summary
Stream processing runs continuous computations over event streams — filtering, windowed aggregation, joins — with results emitted as events. It turns raw streams into answers without storing everything first.

## Details
- Windowing (tumbling, sliding, session) groups events by time for aggregation.
- Exactly-once semantics and state management are the hard engineering core.
- Stream processors (Kafka Streams, Flink) trade latency against exactly-once guarantees.
- Open question: when batch processing is simpler and good enough.

## Related
- [[wiki/devops-infra/event-streaming|Event Streaming]] — the input and output
- [[wiki/cloud-infra/function-as-a-service|Function-as-a-Service]] — stateless event handlers
- [[wiki/devops-infra/log-aggregation|Log Aggregation]] — streams feeding log analytics
- [[wiki/api-protocols/kafka|Apache Kafka]] — stream transport
