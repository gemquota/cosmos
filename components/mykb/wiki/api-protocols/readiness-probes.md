---
type: "concept"
title: "Readiness Probes"
description: "Checks whether a service can accept traffic right now, controlling load-balancer membership"
tags: ["readiness", "probes", "kubernetes", "reliability"]
timestamp: "2026-07-31T00:00:00Z"
status: "stub"
---

# Readiness Probes

## Summary
Readiness probes answer "can this instance serve requests?" — if not, the orchestrator stops sending traffic but does not restart the pod. They gate rollouts and draining.

## Details
- Fail readiness when dependencies (DB, config, warmup) are unavailable; succeed once the service is truly ready.
- Kubernetes `readinessProbe` controls endpoint membership; failed probes remove the pod from Service backends.
- Readiness dropping before shutdown enables [[wiki/api-protocols/graceful-shutdown|graceful draining]].

## Related
- [[wiki/api-protocols/liveness-probes|Liveness Probes]] — restart vs drain distinction
- [[wiki/api-protocols/health-checks|Health Checks]] — the umbrella concept
- [[wiki/devops-infra/kubernetes|Kubernetes]] — probe-driven lifecycle
- [[wiki/api-protocols/graceful-shutdown|Graceful Shutdown]] — drain flow on stop
- [[wiki/devops-infra/observability|Observability]] — probe outcomes feed health telemetry
