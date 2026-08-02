---
type: "concept"
title: "At-Most-Once Delivery"
description: "A delivery guarantee where messages may be lost but never duplicated"
tags: ["delivery", "guarantees", "messaging", "telemetry"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# At-Most-Once Delivery

## Summary
At-most-once delivery attempts each message a single time and does not retry, so loss is possible but duplication is not. It suits telemetry, metrics, and non-critical notifications where a dropped sample beats a duplicated one.

## Details
- Choose it when duplicate processing is worse than missing an event, or loss is acceptable.
- It is the cheapest guarantee — no acks, no redelivery state.
- Most real systems mix: at-least-once for commands, at-most-once for analytics.
- mykb relevance: visit counters and read-tracking events tolerate at-most-once.

## Related
- [[wiki/software-engineering/at-least-once|At-Least-Once]]
- [[wiki/software-engineering/exactly-once-claims|Exactly-Once Claims]]
- [[wiki/software-engineering/delivery-guarantees|Delivery Guarantees]]
- [[wiki/software-engineering/event-notification|Event Notification]]
- [[wiki/software-engineering/event-driven-architecture|Event-Driven Architecture]]
