---
type: "concept"
title: "Health Checks"
description: "Endpoints and probes that report process status so orchestrators and load balancers can act"
tags: ["health-checks", "monitoring", "kubernetes", "reliability"]
timestamp: "2026-07-31T00:00:00Z"
status: "growing"
---

# Health Checks

## Summary
Health checks expose a process's status over HTTP (`/healthz`, `/readyz`) so load balancers, orchestrators, and monitors can route around or restart unhealthy instances.

## Details
- Distinguish liveness (is the process alive?) from readiness (can it serve traffic?).
- Check real dependencies (DB, cache) but avoid cascading failures from unrelated services.
- Return structured status and latency so health itself is observable.

## Design Guidance

Probe endpoints should fail fast and return a decision, not a diagnostic essay. A liveness probe answers "is this process still running," while a readiness probe answers "can this instance serve traffic right now." Readiness should check the dependencies the instance actually needs — database connectivity, cache reachability, essential background workers — but should avoid deep checks on unrelated services, because a transient problem in one dependency can then be reported as unhealthy by every caller and cascade into a fleet-wide restart.

The check itself should be cheap. Expensive validation belongs in tests or startup, not in a probe that runs every few seconds across many instances. Structured responses that include status, latency, and a small machine-readable reason make health observable in dashboards and alerting, while keeping the payload small enough to be safe under load.

## Failure Semantics

- Liveness failure means the process is wedged and should be restarted by the orchestrator.
- Readiness failure means traffic should be drained from the instance without killing it.
- Startup probes are useful for services that take a while to become ready, so the orchestrator does not kill them during warm-up.
- Distinguish "not ready" (HTTP 503) from "ready" (HTTP 200) so load balancers and monitors can act correctly.
- Health endpoints should be cheap, non-authenticated where exposure is internal, and protected from public abuse.

## Related

- [[wiki/api-protocols/liveness-probes|Liveness Probes]] — process-level aliveness
- [[wiki/api-protocols/readiness-probes|Readiness Probes]] — traffic-eligibility
- [[wiki/devops-infra/kubernetes|Kubernetes]] — kubelet probes and restarts
- [[wiki/devops-infra/observability|Observability]] — health as telemetry
- [[wiki/devops-infra/nginx|Nginx]] — upstream health checks
- [[wiki/api-protocols/api-gateway|API Gateway]] — where aggregated health is often exposed
- [[wiki/api-protocols/circuit-breaker|Circuit Breaker]] — complements probes for dependency failure
