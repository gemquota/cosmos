---
type: "concept"
title: "Exponential Backoff for LLMs"
description: "Retry strategy that grows delay between attempts on transient failures"
tags: ["backoff", "retries", "reliability", "api"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Exponential Backoff for LLMs

## Summary
Retry strategy that grows delay between attempts on transient failures

## Details
- Base delay doubles per attempt with jitter to avoid thundering herds.
- Combines with retry-jitter for load smoothing.
- Respects rate-limit headers when present.
- Prevents cascade during provider outages.

## Related
- [[wiki/agent-systems/retry-jitter|Retry Jitter]] — jitter addition
- [[wiki/agent-systems/retry-and-backoff-patterns|Retry and Backoff Patterns]] — pattern family
- [[wiki/ml-frameworks/rate-limit-engineering|Rate Limit Engineering]] — limit awareness
- [[wiki/agent-systems/provider-failover|Provider Failover]] — failover alternative
- [[wiki/agent-systems/partial-failure-handling|Partial Failure Handling]] — failure handling
