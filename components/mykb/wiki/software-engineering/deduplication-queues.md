---
type: "concept"
title: "Deduplication Queues"
description: "Message queues that drop duplicates by message ID"
tags: ["deduplication", "queues", "messages", "patterns"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Deduplication Queues

## Summary
Deduplication queues track recently seen message IDs so re-delivered messages are dropped before processing. They pair with at-least-once brokers (SQS, Kafka consumers) to approach exactly-once processing.

## Details
- A cache or DB of seen IDs with TTL bounds the dedup window; older duplicates pass through.
- Dedup is per-queue and per-window, not a universal guarantee — design for the window.
- Hash full payloads for content-level dedup; IDs for broker-level dedup.
- mykb relevance: dedup the capture queue so the same RSS item is not ingested twice.

## Related
- [[wiki/software-engineering/inbox-pattern|Inbox Pattern]]
- [[wiki/software-engineering/at-least-once|At-Least-Once]]
- [[wiki/software-engineering/exactly-once-claims|Exactly-Once Claims]]
- [[wiki/tooling/idempotency-design|Idempotency Design]]
- [[wiki/api-protocols/message-queues|Message Queues]]
