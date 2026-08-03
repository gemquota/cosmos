---
type: "concept"
title: "Backpressure and Flow Control"
description: "Signaling slow consumers so producers or operators slow down instead of overloading the system"
tags: ["backpressure", "streaming", "flow-control", "reliability"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Backpressure and Flow Control

## Summary
Backpressure propagates a slow downstream condition upstream so producers or operators slow down instead of overloading the system. Flow control is the mechanism set that implements it — credit-based windows, bounded queues, polling offsets, or source-side rate limits — and the alternative to letting buffers grow without bound.

## Details
- Mechanism: a slow consumer signals its state upstream; credit-based flow control (Flink, gRPC) grants the sender a window of in-flight messages that shrinks as the consumer lags; Kafka-style polling lets each consumer set its own pace via offsets; bounded queues absorb bursts up to a cap and then apply a policy — block, drop, or reject.
- Concrete example: a Flink job with credit-based flow control never overruns a slow sink; a Kafka consumer that falls behind reads at its own speed while retention holds the backlog; a worker pool with a bounded queue rejects or blocks when the queue is full instead of growing memory; an HTTP client that applies backpressure by refusing new requests when its internal queue is full.
- Failure modes: unbounded buffers — the most common failure, where a slow consumer turns a producer's memory into garbage; backpressure signals that are ignored or absent, so the slow path only manifests as OOM; blocking backpressure that deadlocks (producer waits, consumer waits); dropping policies that silently lose data without DLQ routing; backpressure applied at the wrong layer, protecting one stage while another overflows.
- Tradeoffs: backpressure protects stability at the cost of throughput and latency — the system runs at the speed of its slowest consumer; the alternative, buffering, smooths short bursts but is bounded by memory; the mature pattern is explicit flow control per stage, bounded queues with defined overflow policies, and monitoring of where pressure builds.
- Operational notes: monitor queue depth and consumer lag, define overflow policies per stage, and test slow-consumer scenarios.
- RSIS3 relevance: RSIS3's pipelines (acquisition, sync) need the same flow control — a slow curation stage should throttle ingestion rather than accumulate an unbounded backlog.

## Related

- [[wiki/data-storage/backpressure|Backpressure]] — existing note on the same mechanism
- [[wiki/data-storage/message-queues|Message Queues]] — queues absorb bursts but need limits
- [[wiki/data-storage/dead-letter-queues-and-retries|Dead Letter Queues And Retries]] — overflow behavior once limits are exceeded
- [[wiki/api-services/rate-limiting-data-apis|Rate Limiting Data Apis]] — limiting ingress at the API layer
- [[wiki/data-storage/streaming-data-pipelines|Streaming Data Pipelines]] — where backpressure matters most
