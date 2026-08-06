---
type: "concept"
title: "Retry and Backoff Patterns"
description: "Repeating failed operations with delays to handle transient failures"
tags: ["agents", "retries", "backoff", "reliability"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://platform.openai.com/docs/guides/error-codes", "https://platform.openai.com/docs/guides/rate-limits"]
---

# Retry and Backoff Patterns

## Summary
Retry-and-backoff is the standard response to transient failures — rate limits, timeouts, and network blips — where repeating the same call will likely succeed. Delays grow between attempts so the system does not hammer a struggling dependency. Retries must be safe for non-idempotent operations.

## Details
- **Backoff schedules** — exponential backoff with jitter avoids synchronized retry storms; fixed delays are simpler but cluster under load.
- **Retry budgets** — a max attempt count, total time, or cost cap turns retries into a bounded loop.
- **Idempotency** — retries of non-idempotent actions (payments, writes) need idempotency keys or must be refused.
- **Worked example** — an agent calling an LLM API on a 429 waits 1s, 2s, 4s (with jitter) and retries up to five times before escalating.
- **Distinction from agent loops** — retries repeat one call; agent loops re-plan whole actions; both need stop conditions.
- **mykb relevance** — RSIS3 sub-agent calls and mykb daemon pipelines both rely on bounded retry with backoff for robustness.

- **Jitter** — full jitter (random delay up to the backoff cap) breaks synchronized retry storms better than fixed or exponential-only schedules.
- **Circuit breaker interaction** — when a circuit breaker has opened, retries must stop until the breaker resets; retrying into an open circuit defeats both mechanisms.
- **Telemetry** — retry counts, backoff durations, and escalation events are first-class telemetry: a rising retry rate is an early warning of a degrading dependency.

- **Respect server guidance** — honor Retry-After headers and rate-limit signals from the dependency; server-provided backoff beats client-guessed schedules and reduces mutual load.

## Related
- [[wiki/agent-systems/exponential-backoff-llm|Exponential Backoff for LLMs]] — backoff for LLM APIs
- [[wiki/agent-systems/retry-jitter|Retry Jitter]] — jitter to avoid thundering herds
- [[wiki/agent-systems/idempotent-agent-actions|Idempotent Agent Actions]] — safe retries
- [[wiki/agent-systems/agent-timeouts|Agent Timeouts]] — timeouts bounding retry loops
- [[wiki/agent-systems/retry-strategies|Retry Strategies]] — existing retry concepts in mykb
- [[wiki/agent-systems/escalation-handling|Escalation Handling]] — what follows retries
- [[wiki/agent-systems/agent-loop|Agent Loop]] — the loop agents execute
- [[wiki/syntheses/knowledge-system|Knowledge System Overview]] — the KB loop this work feeds
