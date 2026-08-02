---
type: "concept"
title: "Backoff Cap"
description: "The maximum delay an exponential backoff strategy will reach"
tags: ["backoff", "retry", "bounded-delay", "reliability"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Backoff Cap

## Summary
A backoff cap bounds the maximum retry delay, keeping recovery time predictable — no infinite doubling to absurd sleeps. Caps pair with attempt budgets to define total retry duration.

## Details
- Choose the cap from your SLO: how long may recovery take before humans get involved?
- Cap the delay, the attempts, or both; state the policy in one place.
- Very long retries are usually a scheduling problem — hand off to a queue instead.
- mykb relevance: link re-checks cap at a day, then report to the curation queue.

## Related
- [[wiki/software-engineering/exponential-backoff-practice|Exponential Backoff Practice]]
- [[wiki/software-engineering/jitter-practice|Jitter Practice]]
- [[wiki/software-engineering/retry-after|Retry-After]]
- [[wiki/software-engineering/retry-patterns|Retry Patterns]]
- [[wiki/software-engineering/retry-queues|Retry Queues]]
