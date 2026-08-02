---
type: "concept"
title: "Jitter"
description: "Randomized delay variation that prevents synchronized retry storms across many clients"
tags: ["jitter", "retries", "resilience", "distributed-systems"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://aws.amazon.com/blogs/architecture/exponential-backoff-and-jitter/", "https://en.wikipedia.org/wiki/Jitter"]
---

# Jitter

## Summary
Jitter adds random variation to retry timing so that many clients retrying simultaneously do not collide in synchronized waves. Full jitter randomizes within the current backoff window.

## Details
- Without jitter, thousands of clients doubling in lockstep create thundering herds that worsen the outage.
- AWS's "full jitter" strategy: `sleep = random(0, min(cap, base * 2^attempt))`.
- Apply jitter to cron workers, cache refresh, and any shared retry schedule.
- Jitter adds random variation to backoff delays so synchronized clients do not retry in lockstep and hammer the recovering service together.
- Full jitter randomizes the delay between zero and the backoff value; equal jitter keeps a floor; both break thundering-herd retries.
- The AWS recommendation of exponential backoff with full jitter is the widely used formula for distributed retry policies.
- Jitter costs a little latency on average and buys a large reduction in worst-case load spikes during outages.
- **Worked example / comparison** — Worked example — a fleet of devices retrying after a network drop picks delays of 0.4s, 3.1s, 9.7s instead of every device retrying at 1s, 2s, 4s.
- For mykb, jitter is documented as the finishing touch on exponential backoff for the wiki's distributed sync clients.

## Related
- [[wiki/api-protocols/exponential-backoff|Exponential Backoff]]
- [[wiki/api-protocols/retry-backoff|Retry & Backoff]]
- [[wiki/api-protocols/timeouts|Timeouts]]
- [[wiki/devops-infra/observability|Observability]]
- [[wiki/concepts/promotion-readiness|Promotion Readiness]]
- [[wiki/ai-ml/article-health-scores|Article Health Scores]]
- [[wiki/concepts/explainers|Explainers]]
