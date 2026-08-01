---
type: "concept"
title: "Jitter"
description: "Randomized delay variation that prevents synchronized retry storms across many clients"
tags: ["jitter", "retries", "resilience", "distributed-systems"]
timestamp: "2026-07-31T00:00:00Z"
status: "stub"
---

# Jitter

## Summary
Jitter adds random variation to retry timing so that many clients retrying simultaneously do not collide in synchronized waves. Full jitter randomizes within the current backoff window.

## Details
- Without jitter, thousands of clients doubling in lockstep create thundering herds that worsen the outage.
- AWS's "full jitter" strategy: `sleep = random(0, min(cap, base * 2^attempt))`.
- Apply jitter to cron workers, cache refresh, and any shared retry schedule.

## Related
- [[wiki/api-protocols/exponential-backoff|Exponential Backoff]] — the schedule jitter modifies
- [[wiki/api-protocols/retry-backoff|Retry & Backoff]] — overall retry policy
- [[wiki/api-protocols/timeouts|Timeouts]] — bounds on total wait
- [[wiki/devops-infra/observability|Observability]] — detecting retry storms
