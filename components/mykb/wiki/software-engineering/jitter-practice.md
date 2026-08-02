---
type: "concept"
title: "Jitter Practice"
description: "Adding randomness to retry timing to prevent synchronized retry storms"
tags: ["jitter", "retry", "backoff", "practice"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Jitter Practice

## Summary
Jitter randomizes retry delays so many clients do not retry in lockstep and slam a recovering service. Full jitter (random between 0 and the backoff interval) is the common recipe; without it, backoff can be worse than no backoff.

## Details
- Full jitter: sleep(random(0, cap * 2^attempt)); equal jitter keeps a floor of half the interval.
- Jitter helps any fan-out: batch jobs, DNS retries, cache stampedes.
- Also jitter scheduled jobs so cron-like waves do not align.
- mykb relevance: multiple wiki workers re-checking links need jittered schedules.

## Related
- [[wiki/software-engineering/exponential-backoff-practice|Exponential Backoff Practice]]
- [[wiki/software-engineering/backoff-cap|Backoff Cap]]
- [[wiki/tooling/cache-stampede|Cache Stampede]]
- [[wiki/api-protocols/jitter|Jitter]]
- [[wiki/software-engineering/retry-patterns|Retry Patterns]]
