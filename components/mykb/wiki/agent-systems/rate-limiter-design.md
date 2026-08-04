---
type: "concept"
title: "Rate Limiter Design"
description: "Designing token and request rate limits for LLM APIs and gateways"
tags: ["rate-limiter", "rate-limits", "design", "api"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Rate Limiter Design

## Summary
Rate limiter design is the engineering of token and request limits for LLM APIs and gateways, protecting both providers and consumers. It matters because model calls are expensive and bursty, and unbounded traffic causes cost spikes and provider throttling. A well-designed limiter shapes traffic into a sustainable pattern. Rate limiting is negotiation between provider protection and consumer needs.

## Details
- **Definition** — a rate limiter constrains how many requests or tokens a client can send within a window, enforcing an agreed traffic contract.
- **Algorithms** — fixed-window, sliding-window, and token-bucket algorithms differ in burstiness: token buckets allow controlled bursts while fixed windows clamp hard.
- **Scope** — limits apply per API key, user, route, or global pool, each protecting a different resource or cost center.
- **Signaling** — limit responses should tell clients what to do via headers, such as retry-after and remaining-quota values, so they can back off correctly.
- **Integration** — rate limiting complements budget-and-quota-control for cost and concurrency-limits for parallelism.
- **Worked example** — a gateway allows one thousand requests per minute per key with a token bucket; a bursty client exhausts its bucket and receives retry-after guidance.
- **Failure modes** — limits set too high fail to protect, limits set too low throttle legitimate work, and inconsistent limiter state breaks distributed behavior.
- **Practical relevance** — rate limiter design is a core skill for gateway engineering and a prerequisite for retry-jitter discipline downstream.
- **Distributed state** — shared limit state needs consistency, or global limits leak under sharded deployments.
- **Grace** — small overage tolerances and burst allowances keep legitimate traffic flowing.
- **Worked example** — a token-bucket limiter grants a burst of ten requests then throttles to a steady rate.
- **Failure example** — a limiter that rejects without guidance makes clients retry blindly, amplifying load.

## Related
- [[wiki/ml-frameworks/rate-limit-engineering|Rate Limit Engineering]] — the engineering umbrella
- [[wiki/api-protocols/concurrency-limits|Concurrency Limits]] — capping parallelism
- [[wiki/agent-systems/budget-and-quota-control|Budget and Quota Control]] — cost quotas
- [[wiki/agent-systems/retry-jitter|Retry Jitter]] — how clients behave around limits
- [[wiki/api-protocols/load-shedding|Load Shedding]] — server-side drops under overload
