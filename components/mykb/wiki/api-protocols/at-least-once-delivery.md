---
type: "concept"
title: "At-Least-Once Delivery"
description: "Delivery guarantees and deduplication"
tags: ["delivery-guarantees", "at-least-once", "reliability", "messaging", "distributed-systems"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://www.confluent.io/blog/exactly-once-semantics-are-possible-heres-how-apache-kafka-does-it/", "https://en.wikipedia.org/wiki/Exactly-once_delivery"]
---

# At-Least-Once Delivery

## Summary
At-least-once delivery means a message may be delivered more than once, but never lost: consumers must be prepared for duplicates. It is the pragmatic guarantee of most queues, Kafka consumer groups, webhook retries, and SSE replay — and exactly-once is only achievable by combining at-least-once transport with idempotent processing.

## Details
- The guarantee: every message arrives at least once; duplicates are possible when acks are lost, brokers fail over, or consumers crash mid-processing.
- Why it is the default: exactly-once across networks requires distributed transactions or consensus, which cost latency and complexity; at-least-once plus dedup is usually good enough.
- Deduplication: consumers track processed message ids (in a database unique key, Redis set, or outbox) and skip repeats.
- Idempotent processing: make handlers naturally idempotent — INSERT ... ON CONFLICT DO NOTHING, upserts, or set-based updates instead of appends.
- Acks and offsets: Kafka and AMQP commit offsets/acks only after processing succeeds, which is what creates redelivery on crash.
- Ordering caveats: at-least-once does not guarantee order; combine with per-key ordering (Kafka partitions) when order matters.
- Webhooks and SSE: retry loops and Last-Event-ID replay are at-least-once too — the receiver, not the sender, must dedup.

## Related
- [[wiki/api-protocols/idempotency-keys|Idempotency Keys]] — client-side dedup for POST operations
- [[wiki/api-protocols/webhooks|Webhooks]] — retried webhook deliveries need dedup
- [[wiki/api-protocols/message-queues|Message Queues]] — queues provide at-least-once by default
- [[wiki/api-protocols/server-sent-events|Server-Sent Events]] — Last-Event-ID replay is at-least-once
- [[wiki/api-protocols/retry-policies|Retry Policies]] — retries multiply delivery attempts
