---
type: "concept"
title: "Inbox Pattern"
description: "Deduplicating incoming messages by persisting processed message IDs"
tags: ["inbox", "deduplication", "messages", "patterns"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Inbox Pattern

## Summary
The inbox pattern stores the IDs of processed messages so a consumer can detect and skip duplicates — the mirror of the outbox on the receiving side. It converts at-least-once delivery into effectively-once processing.

## Details
- Record (message_id, status) in the same transaction as the side effect it triggers.
- The inbox table doubles as a replay log: reprocess unprocessed rows after crashes.
- Idempotent handlers can replace inboxes, but inboxes work even for non-idempotent effects.
- mykb relevance: the wiki ingestion consumer uses an inbox to ignore re-delivered captures.

## Related
- [[wiki/software-engineering/outbox-table|Outbox Table]]
- [[wiki/software-engineering/deduplication-queues|Deduplication Queues]]
- [[wiki/tooling/idempotency-design|Idempotency Design]]
- [[wiki/software-engineering/exactly-once-claims|Exactly-Once Claims]]
- [[wiki/api-protocols/message-queues|Message Queues]]
