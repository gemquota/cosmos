---
type: "concept"
title: "Scheduled Retries"
description: "Retrying failed work after a planned delay instead of immediately"
tags: ["retry", "scheduling", "reliability", "backoff"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Scheduled Retries

## Summary
Scheduled retries defer the next attempt by a fixed or growing delay, giving transient failures time to clear. Delay queues, cron-like schedulers, and job stores all implement it; the delay choice is the design center.

## Details
- Fixed delays suit maintenance windows; exponential delays suit overload recovery.
- Schedules must survive restarts — persist pending retries in a durable store.
- Cancellation matters: a retry schedule for a deleted job should vanish.
- mykb relevance: link re-checks are scheduled retries for sources that were down.

## Related
- [[wiki/software-engineering/retry-queues|Retry Queues]]
- [[wiki/software-engineering/exponential-backoff-practice|Exponential Backoff Practice]]
- [[wiki/software-engineering/retry-after|Retry-After]]
- [[wiki/software-engineering/retry-patterns|Retry Patterns]]
- [[wiki/agent-systems/retry-strategies|Retry Strategies]]
