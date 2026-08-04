---
type: "concept"
title: "Retry Jitter"
description: "Randomized delay added to retries to prevent synchronized retry storms"
tags: ["jitter", "retries", "reliability", "load"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Retry Jitter

## Summary
Retry jitter is the randomized delay added to retries to prevent synchronized retry storms when many clients retry at once. It matters because naive exponential backoff can cause a thundering herd that turns a small outage into a system-wide failure. Jitter spreads retries in time, stabilizing systems under partial outages. Jitter is a small randomization with large reliability returns.

## Details
- **Definition** — jitter is random variation applied to backoff delays so that concurrent clients do not all retry on the same schedule.
- **Variants** — full jitter randomizes the delay across the whole backoff range; equal jitter adds uniform noise around a base delay.
- **Mechanism** — clients combine jitter with exponential-backoff-llm so early retries are quick, later ones are spread out, and total retry load stays bounded.
- **Why it matters** — without jitter, thousands of clients failing at the same instant retry in lockstep, amplifying load exactly when the service is weakest.
- **Worked example** — an API outage recovers at minute three; clients with jittered retries resume gradually over several minutes instead of hammering the service at once.
- **Failure modes** — too little jitter preserves synchronization, while too much adds needless latency; both degrade the retry strategy.
- **Integration** — jitter pairs with rate-limit-engineering and load-shedding for a complete failure-response toolkit.
- **Practical relevance** — jitter is a small change with outsized reliability impact, and it applies to every retrying client in an agent platform.
- **Implementation** — jitter is applied to the backoff calculation, not added after the wait, to preserve its effect.
- **Tuning** — jitter ranges should match the service's recovery time scale.
- **Failure example** — all clients using the same seed and schedule still synchronize their retries.

## Related
- [[wiki/agent-systems/exponential-backoff-llm|Exponential Backoff for LLMs]] — the backoff schedule jitter modifies
- [[wiki/agent-systems/retry-and-backoff-patterns|Retry and Backoff Patterns]] — the pattern family
- [[wiki/ml-frameworks/rate-limit-engineering|Rate Limit Engineering]] — client-side discipline
- [[wiki/api-protocols/load-shedding|Load Shedding]] — server-side protection
- [[wiki/agent-systems/partial-failure-handling|Partial Failure Handling]] — handling the failures that trigger retries
