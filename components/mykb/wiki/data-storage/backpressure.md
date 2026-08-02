---
type: "concept"
title: "Backpressure"
description: "Flow control when consumers lag producers"
tags: ["streaming", "flow-control", "consumer-lag", "message-queues"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://kafka.apache.org/documentation/#consumerconfigs", "https://nightlies.apache.org/flink/flink-docs-stable/docs/ops/debugging/back_pressure/"]
---

# Backpressure

## Summary
Backpressure is the flow-control mechanism that keeps a fast producer from overwhelming a slow consumer. When downstream stages cannot keep up, the system either buffers, drops, or signals upstream to slow down — otherwise memory fills, queues grow without bound, and latency spikes.

## Details
- **Where it matters** — any pipeline with finite buffers: message brokers, stream processors, log shippers, and database replication. Without backpressure, a lagging consumer creates unbounded queue growth or lost records.
- **Pull vs push** — pull-based consumers request work when ready, which naturally applies backpressure; push-based producers need explicit signals such as TCP windowing, credit-based flow control, or broker-side quotas.
- **Kafka consumers** — `max.poll.records`, `fetch.max.bytes`, and `max.poll.interval.ms` bound how much a consumer fetches; consumer lag (`kafka.consumer:type=consumer-fetch-manager-metrics`) exposes how far behind the log a consumer has fallen.
- **Flink** — streaming operators propagate backpressure through checkpoint barriers; the web UI's back-pressure tab samples task idle/busy ratios to identify bottlenecks, and buffered-in-memory metrics show where data accumulates.
- **Failure modes** — retry storms make things worse when consumers crash and replay; dead-letter queues and circuit breakers break the cycle by parking bad records or shedding load.
- **Design guidance** — prefer bounded queues, monitor lag, and choose explicit drop or blocking policies per workload rather than letting memory blow up silently.

## Related
- [[wiki/data-storage/message-queues|Message Queues]] — bounded work distribution where lag first appears
- [[wiki/data-storage/dead-letter-queues|Dead Letter Queues]] — parking records that cannot be processed
- [[wiki/data-storage/event-streaming-platforms|Event Streaming Platforms]] — consumer lag and partition assignment
- [[wiki/data-storage/stream-processing-engines|Stream Processing Engines]] — operator-level flow control
- [[wiki/data-storage/exactly-once-semantics|Exactly-Once Semantics]] — replay behavior under load
- [[wiki/devops-infra/observability|Observability]] — measuring consumer lag in production
