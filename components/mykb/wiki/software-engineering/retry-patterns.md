---
type: "concept"
title: "Retry Patterns"
description: "The disciplined ways to re-attempt failed operations safely"
tags: ["retry", "patterns", "reliability", "backoff"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://aws.amazon.com/builders-library/timeouts-retries-and-backoff-with-jitter/", "https://en.wikipedia.org/wiki/Idempotence"]
---

# Retry Patterns

## Summary
Retry patterns govern re-attempting failed work: when to retry, how many times, with what delay, and what to do when retries fail. The discipline — retry only transient failures, back off with jitter, cap attempts — prevents retry storms from turning small failures into outages.

## Details
- Retry classification first: transient failures (timeouts, 5xx, resets) deserve retries; permanent failures (4xx, validation) must not be retried.
- Exponential backoff with jitter spaces attempts; a backoff cap bounds total recovery time.
- Idempotency is the retry prerequisite: a retried operation must be safe to run twice.
- Retries belong at defined boundaries: inside the client, with context propagation and deadline awareness.
- Retry budgets and circuit breakers stop endless loops when a dependency is down.
- For the mykb bundle, the source fetcher retries transient errors with backoff and honors Retry-After.
- Worked example — the wiki fetcher retries a 503 with 1s, 2s, 4s plus jitter, caps at 5 attempts, and honors the server's Retry-After when present.

Worked example — the wiki fetcher retries a 503 with 1s, 2s, 4s plus jitter, caps at 5 attempts, and honors the server's Retry-After when present.

## Related
- [[wiki/software-engineering/exponential-backoff-practice|Exponential Backoff Practice]]
- [[wiki/software-engineering/jitter-practice|Jitter Practice]]
- [[wiki/software-engineering/retry-queues|Retry Queues]]
- [[wiki/software-engineering/backoff-cap|Retry Patterns]]
- [[wiki/dev-tools/circuit-open-state|Circuit Open State]]
- [[wiki/software-engineering/backoff-cap|Backoff Cap]]
- [[wiki/software-engineering/scheduled-retries|Scheduled Retries]]
- [[wiki/api-protocols/retry-backoff|Retry & Backoff]]
- [[wiki/api-protocols/exponential-backoff|Exponential Backoff]]
