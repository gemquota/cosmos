---
type: "concept"
title: "Health Checks"
description: "Endpoints and probes that report process status so orchestrators and load balancers can act"
tags: ["health-checks", "monitoring", "kubernetes", "reliability"]
timestamp: "2026-07-31T00:00:00Z"
status: "stub"
---

# Health Checks

## Summary
Health checks expose a process's status over HTTP (`/healthz`, `/readyz`) so load balancers, orchestrators, and monitors can route around or restart unhealthy instances.

## Details
- Distinguish liveness (is the process alive?) from readiness (can it serve traffic?).
- Check real dependencies (DB, cache) but avoid cascading failures from unrelated services.
- Return structured status and latency so health itself is observable.

## Related
- [[wiki/api-protocols/liveness-probes|Liveness Probes]] — process-level aliveness
- [[wiki/api-protocols/readiness-probes|Readiness Probes]] — traffic-eligibility
- [[wiki/devops-infra/kubernetes|Kubernetes]] — kubelet probes and restarts
- [[wiki/devops-infra/observability|Observability]] — health as telemetry
- [[wiki/devops-infra/nginx|Nginx]] — upstream health checks
