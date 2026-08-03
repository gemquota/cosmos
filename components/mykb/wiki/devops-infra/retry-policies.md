---
type: "concept"
title: "Retry Policies"
description: "Retrying failures with backoff, jitter, and limits"
tags: ["retry", "backoff", "resilience", "networking"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Retry Policies

## Summary
Retry policies define when, how often, and with what backoff a failed operation is retried — and when it stops. Correct retries mask transient failures (timeouts, connection resets); incorrect ones turn small outages into cascades, so retries need budgets, jitter, and integration with circuit breakers and dead-lettering.

## Details
- Mechanism: a retry policy specifies max attempts, delay strategy (fixed, exponential), jitter (randomization to avoid synchronized retry storms), and which errors are retryable (network and 5xx, not 4xx or idempotency-violating cases); retries belong at one layer — client, proxy, or service — not all three.
- Concrete example: a client retries a PUT 3 times with exponential backoff (1s, 2s, 4s) plus jitter, giving up after 7 seconds and surfacing the error; a message consumer retries with a backoff queue and moves poison messages to a dead-letter queue after N attempts; Envoy retries with per-try timeouts and retry-on conditions.
- Failure modes: retry storms — every client retrying a down service at the same moment, multiplying load (mitigate with jitter and circuit breakers); retrying non-idempotent operations, duplicating side effects (use idempotency keys); unbounded retries masking an outage and delaying alerting; retry after deadline, so the caller has already timed out; retries that succeed against a stale or degraded replica.
- Tradeoffs: retries buy resilience to transient failures at the cost of latency, load, and complexity; too few retries fail fast on blips, too many amplify outages; the mature pattern is bounded, jittered retries plus a circuit breaker that stops retrying a failing dependency and a fallback that degrades gracefully.
- Operational notes: centralize retry policy in config, monitor retry rates and effectiveness, and rehearse dependency-failure scenarios.
- RSIS3 relevance: RSIS3's calls to the wiki daemon and LLM providers need the same policy — bounded jittered retries with an explicit give-up so loop telemetry reflects real failures instead of retry storms.

## Related
- [[wiki/devops-infra/ingress-egress-policies|Ingress & Egress Policies]]
- [[wiki/devops-infra/network-policies-kubernetes|Kubernetes Network Policies]]
- [[wiki/devops-infra/escalation-policies|Escalation Policies]]
- [[wiki/cloud-infra/snapshot-lifecycle-policies|Snapshot Lifecycle Policies]]
- [[wiki/devops-infra/kubernetes-control-plane|Kubernetes Control Plane]]
- [[wiki/devops-infra/observability-pillars|Observability Pillars]]
