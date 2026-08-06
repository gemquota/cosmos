---
type: "concept"
title: "Exponential Backoff for LLMs"
description: "Retry strategy that grows delay between attempts on transient failures"
tags: ["backoff", "retries", "reliability", "api"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Exponential Backoff for LLMs

## Summary
Exponential backoff is a retry strategy that grows the delay between attempts on transient failures, typically doubling the wait each time. For LLM APIs it smooths load, respects rate limits, and prevents cascades during provider outages.

## Details
- **Mechanics** — base delay doubles per attempt (1s, 2s, 4s) up to a cap, with jitter added so synchronized clients do not stampede the provider at the same moment.
- **Rate-limit awareness** — when the provider returns a Retry-After header, backoff honors it; respecting explicit signals beats guessing.
- **Which failures to retry** — transient errors (429, 5xx, timeouts, connection resets) are retryable; permanent errors (400, 401, invalid input) must not be retried because they will never succeed.
- **Cap and budget** — a maximum delay and a total retry budget bound the cost; unbounded backoff on a dying provider wastes tokens and time.
- **Relationship to other patterns** — backoff is one member of the retry-and-backoff pattern family, sits alongside retry jitter for load smoothing, and pairs with provider failover when the outage is provider-wide.
- **Cascade prevention** — during an outage, coordinated retries can amplify load on the provider and downstream systems; jittered exponential backoff spreads the recovery wave.
- **Measurement** — track retry rates, time-to-success, and abandoned attempts per provider so the policy is tuned from data rather than defaults.

- **Jitter function** — full jitter (randomize the delay between zero and the backoff value) spreads retries best under load; equal jitter (perturb around the backoff value) is a compromise that preserves more spacing.
- **Multi-provider context** — with several providers, backoff per provider keeps one provider's outage from burning the shared budget; failover is triggered when the backoff ceiling is reached.
- **Timeouts interplay** — the retry budget is the product of attempts and delays; timeout values and backoff caps are tuned together so a slow provider does not double-charge the budget.
## Related
- [[wiki/agent-systems/retry-jitter|Retry Jitter]] — jitter addition
- [[wiki/agent-systems/retry-and-backoff-patterns|Retry and Backoff Patterns]] — pattern family
- [[wiki/agent-systems/retry-strategies|Retry Strategies]] — when to retry
- [[wiki/ml-frameworks/rate-limit-engineering|Rate Limit Engineering]] — limit awareness
- [[wiki/agent-systems/provider-failover|Provider Failover]] — failover alternative
- [[wiki/agent-systems/partial-failure-handling|Partial Failure Handling]] — failure handling
