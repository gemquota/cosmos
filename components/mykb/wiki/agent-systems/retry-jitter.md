---
type: "concept"
title: "Retry Jitter"
description: "Randomized delay added to retries to prevent synchronized retry storms"
tags: ["jitter", "retries", "reliability", "load"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Retry Jitter

## Summary
Randomized delay added to retries to prevent synchronized retry storms

## Details
- Full jitter randomizes backoff; equal jitter adds variance to the base.
- Jitter stabilizes systems under partial outages.
- Combines with exponential-backoff-llm.
- Reduces thundering-herd failures.

## Related
- [[wiki/agent-systems/exponential-backoff-llm|Exponential Backoff for LLMs]] — backoff base
- [[wiki/agent-systems/retry-and-backoff-patterns|Retry and Backoff Patterns]] — pattern family
- [[wiki/ml-frameworks/rate-limit-engineering|Rate Limit Engineering]] — client discipline
- [[wiki/api-protocols/load-shedding|Load Shedding]] — server protection
- [[wiki/agent-systems/partial-failure-handling|Partial Failure Handling]] — failure handling
