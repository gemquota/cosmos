---
type: "concept"
title: "Retry Queues"
description: "Dedicated queues that hold failed work for a later attempt"
tags: ["retry", "queues", "reliability", "messaging"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Retry Queues

## Summary
Retry queues decouple failed work from the live path: a failure moves the message to a retry queue with a delay, then back for another attempt. They bound retry pressure and give operations a visible place to inspect failures.

## Details
- Delay-based retry (SQS delay, RabbitMQ retry exchanges, Kafka retry topics) spaces attempts.
- Retry budgets: cap attempts per message, then route to the dead-letter queue.
- Retries must be idempotent — the queue retries, your handler dedups.
- mykb relevance: failed source fetches retry via a queue with capped attempts.

## Related
- [[wiki/software-engineering/poison-messages|Poison Messages]]
- [[wiki/software-engineering/scheduled-retries|Scheduled Retries]]
- [[wiki/software-engineering/exponential-backoff-practice|Exponential Backoff Practice]]
- [[wiki/software-engineering/retry-patterns|Retry Patterns]]
- [[wiki/api-protocols/message-queues|Message Queues]]
