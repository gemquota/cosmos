---
type: "concept"
title: "Probe Design"
description: "Designing liveness, readiness, and startup probes so orchestration makes the right decisions"
tags: ["probes", "kubernetes", "health", "design"]
timestamp: "2026-08-01T00:00:00Z"
status: "stub"
---

# Probe Design

## Summary
Probe design decides what liveness, readiness, and startup checks report and how they are implemented. Good probes make orchestration decisions (restart, route traffic, delay liveness) match reality.

## Details
- Liveness answers 'should this container be restarted?'; readiness 'should this pod receive traffic?'; startup 'has the app finished booting?'
- Probes should check the application, not the sidecar or the host.
- Tune thresholds to boot time and GC pauses to avoid flapping.
- Open question: when readiness should depend on downstream dependencies.

## Related
- [[wiki/infrastructure/startup-probes|Startup Probes]] — the slow-boot protection
- [[wiki/infrastructure/containerization|Containerization]] — probes gate containerized apps
- [[wiki/infrastructure/health-check-patterns|Health Check Patterns]] — the broader family
- [[wiki/api-protocols/liveness-probes|Liveness Probes]] — restart semantics
- [[wiki/api-protocols/readiness-probes|Readiness Probes]] — traffic-gating semantics
