---
type: "concept"
title: "Exponential Backoff"
description: "Doubling retry delays (1s, 2s, 4s...) so load on recovering services recedes over time"
tags: ["backoff", "retries", "reliability", "networking", "algorithms"]
timestamp: "2026-07-31T00:00:00Z"
status: "stub"
---

# Exponential Backoff

## Summary
Exponential backoff multiplies the delay between retries by a constant factor each attempt (e.g. 1s, 2s, 4s, 8s), capped at a maximum. It gives failing services time to recover while still retrying.

## Details
- Formula: `delay = base * 2^attempt` with optional cap and full-jitter randomization.
- AWS and Google SDKs implement it natively for throttling responses.
- Pair with a retry budget (max attempts or total elapsed time) to avoid infinite loops.

## Related
- [[wiki/api-protocols/retry-backoff|Retry & Backoff]] — the enclosing pattern
- [[wiki/api-protocols/jitter|Jitter]] — randomizes the schedule
- [[wiki/api-protocols/timeouts|Timeouts]] — bounds total retry duration
- [[wiki/api-protocols/rate-limiting|Rate Limiting]] — why throttling happens
