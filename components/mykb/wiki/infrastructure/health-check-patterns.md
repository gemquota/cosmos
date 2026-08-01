---
type: "concept"
title: "Health Check Patterns"
description: "Ways to expose and consume application health: endpoints, agents, and passive checks"
tags: ["health-checks", "patterns", "monitoring", "reliability"]
timestamp: "2026-08-01T00:00:00Z"
status: "stub"
---

# Health Check Patterns

## Summary
Health-check patterns define how services expose their health — HTTP endpoints, TCP checks, agent-based — and how balancers and orchestrators consume it.

## Details
- HTTP /healthz-style endpoints are the norm; they should check the app, not just respond 200.
- Active checks probe from outside; passive checks infer health from traffic behavior.
- Dependency-aware checks (DB reachable?) trade availability signal for accuracy.
- Open question: how deep a health check should go before it causes flapping.

## Related
- [[wiki/devops-infra/load-balancing|Load Balancing]] — health decides who gets traffic
- [[wiki/infrastructure/probe-design|Probe Design]] — container-level health checks
- [[wiki/api-protocols/health-checks|Health Checks]] — API-level patterns
- [[wiki/api-protocols/readiness-probes|Readiness Probes]] — orchestrated consumption
