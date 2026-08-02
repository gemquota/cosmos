---
type: "concept"
title: "Poison Messages"
description: "Messages that crash or stall consumers and block the queue"
tags: ["poison-messages", "queues", "failures", "messaging"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Poison Messages

## Summary
A poison message is one a consumer can never process successfully — malformed payload, impossible state — so it fails or retries forever and stalls the queue. Dead-letter queues and poison handling exist to quarantine them.

## Details
- Move repeatedly failing messages to a dead-letter queue after N attempts.
- Track why messages die: format errors, schema drift, missing dependencies.
- Alert on DLQ growth; replay fixed messages after schema or data repair.
- mykb relevance: a corrupt capture file lands in the wiki DLQ instead of blocking ingestion.

## Related
- [[wiki/software-engineering/retry-queues|Retry Queues]]
- [[wiki/dev-tools/error-codes|Error Codes]]
- [[wiki/software-engineering/at-least-once|At-Least-Once]]
- [[wiki/api-protocols/message-queues|Message Queues]]
- [[wiki/software-engineering/deduplication-queues|Deduplication Queues]]
