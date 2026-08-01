---
type: "concept"
title: "Event Streaming"
description: "Continuously publishing and consuming ordered event logs as the source of truth for state"
tags: ["event-streaming", "kafka", "events", "data-pipelines"]
timestamp: "2026-08-01T00:00:00Z"
status: "stub"
---

# Event Streaming

## Summary
Event streaming treats events as an append-only, replayable log: producers write facts, consumers read them at their own pace and position.

## Details
- The log is ordered and retained; consumers track offsets, enabling replay and late-joining consumers.
- Event sourcing and CQRS patterns build on the same log idea.
- Schema evolution and partitioning keys decide ordering and scaling properties.
- Open question: how far to push the log-as-database idea for complex state.

## Related
- [[wiki/devops-infra/pub-sub-messaging|Pub/Sub Messaging]] — delivery vs log model
- [[wiki/cloud-infra/function-as-a-service|Function-as-a-Service]] — consumers of event streams
- [[wiki/devops-infra/stream-processing|Stream Processing]] — consuming the log live
- [[wiki/api-protocols/kafka|Apache Kafka]] — the reference stream broker
- [[wiki/api-protocols/event-sourcing|Event Sourcing]] — state from the event log
