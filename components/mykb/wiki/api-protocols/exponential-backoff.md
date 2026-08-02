---
type: "concept"
title: "Exponential Backoff"
description: "Doubling retry delays (1s, 2s, 4s...) so load on recovering services recedes over time"
tags: ["backoff", "retries", "reliability", "networking", "algorithms"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://aws.amazon.com/blogs/architecture/exponential-backoff-and-jitter/", "https://cloud.google.com/iot/docs/how-tos/exponential-backoff"]
---

# Exponential Backoff

## Summary
Exponential backoff multiplies the delay between retries by a constant factor each attempt (e.g. 1s, 2s, 4s, 8s), capped at a maximum. It gives failing services time to recover while still retrying.

## Details
- Formula: `delay = base * 2^attempt` with optional cap and full-jitter randomization.
- AWS and Google SDKs implement it natively for throttling responses.
- Pair with a retry budget (max attempts or total elapsed time) to avoid infinite loops.
- Exponential backoff grows the wait between retries multiplicatively — 1s, 2s, 4s, 8s — instead of retrying on a fixed schedule.
- It prevents retry storms: without it, a failed batch of clients synchronized on the same interval amplifies load on the failing service.
- The cap on the maximum delay and the choice of multiplier (often 2) set the aggressiveness of the recovery curve.
- It is the default retry policy in most cloud SDKs and pairs with jitter to break client synchronization.
- **Worked example / comparison** — Worked example — five failed attempts at 1s, 2s, 4s, 8s, 16s give the upstream 31 seconds of recovery room instead of five hits within 5 seconds.
- For mykb, exponential-backoff is documented as the core of the retry-backoff family, with jitter as its essential companion.

## Related
- [[wiki/api-protocols/retry-backoff|Retry & Backoff]]
- [[wiki/api-protocols/jitter|Jitter]]
- [[wiki/api-protocols/timeouts|Timeouts]]
- [[wiki/api-protocols/rate-limiting|Rate Limiting]]
- [[wiki/concepts/promotion-readiness|Promotion Readiness]]
- [[wiki/dev-tools/global-link-check|Global Link Check]]
- [[wiki/concepts/explainers|Explainers]]
