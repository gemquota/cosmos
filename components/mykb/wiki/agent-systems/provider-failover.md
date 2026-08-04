---
type: "concept"
title: "Provider Failover"
description: "Automatic switching between LLM providers when one becomes unavailable"
tags: ["failover", "providers", "reliability", "routing"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Provider Failover

## Summary
Provider failover automatically switches between LLM providers when one becomes unavailable or degraded, keeping service alive through outages. It matters because single-provider dependence creates a single point of failure for everything an agent does. Multi-provider failover trades a little complexity for much higher availability. Failover is a promise that must be rehearsed, not just configured.

## Details
- **Definition** — failover is the automatic redirection of requests from an unhealthy provider to a healthy alternative.
- **Triggers** — health checks, error rates, latency thresholds, and quota exhaustion signal when a provider should be considered unavailable.
- **Semantics** — failover must preserve request semantics: same payload, retry counts, and idempotency, so the switch is invisible to callers.
- **Budget awareness** — failover across providers must respect budgets and rate limits on the destination, which may differ from the primary.
- **Chains** — provider failover operates alongside model-fallback-chains, which switch models, and routing rules, which pick the best default provider.
- **Worked example** — a gateway sees repeated 503s from provider A, marks it unhealthy for sixty seconds, and sends new requests to provider B while A recovers.
- **Failure modes** — failover storms when many clients switch at once, stale health data, and inconsistent model quality across providers can all cause problems.
- **Observability** — failover events should be logged and measured so availability improvements are visible and provable.
- **Practical relevance** — failover is a cornerstone of llm-gateway-and-routing reliability and reduces single-vendor risk.
- **Rehearsal** — teams should regularly test failover by deliberately marking the primary unhealthy.
- **Cost** — failover to a more expensive provider should be budget-aware.
- **Failure example** — failover that does not copy request metadata breaks features that depend on it.

## Related
- [[wiki/llm-agents/llm-gateway-and-routing|LLM Gateway and Routing]] — the gateway layer where failover lives
- [[wiki/agent-systems/endpoint-health-checks|Endpoint Health Checks]] — the health signal that triggers failover
- [[wiki/agent-systems/model-fallback-chains|Model Fallback Chains]] — model-level fallback
- [[wiki/agent-systems/retry-and-backoff-patterns|Retry and Backoff Patterns]] — client retry policy around failover
- [[wiki/agent-systems/degraded-mode-operations|Degraded Mode Operations]] — reduced service when no provider is healthy
