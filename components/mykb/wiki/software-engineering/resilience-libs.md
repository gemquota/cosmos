---
type: "concept"
title: "Resilience Libraries"
description: "Bundled toolkits for timeouts, retries, breakers, and bulkheads"
tags: ["resilience", "libraries", "tooling", "reliability"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Resilience Libraries

## Summary
Resilience libraries package the standard failure-handling tools — retry, timeout, circuit breaker, bulkhead, rate limiter — behind one API. They remove the temptation to hand-roll half-correct versions.

## Details
- Compose decorators: timeout wraps retry wraps breaker, each with its own config.
- Good libs expose metrics (attempts, trips, rejections) so policy health is observable.
- Defaults are sane but not yours: tune thresholds per dependency profile.
- mykb relevance: a resilience layer around tool calls keeps the agent loop steady under failures.

## Related
- [[wiki/software-engineering/circuit-breaker-libs|Circuit Breaker Libraries]]
- [[wiki/software-engineering/retry-patterns|Retry Patterns]]
- [[wiki/dev-tools/timeout-policy|Timeout Policy]]
- [[wiki/dev-tools/bulkhead-isolation|Bulkhead Isolation]]
- [[wiki/software-engineering/reliability-engineering|Reliability Engineering]]
