---
type: "concept"
title: "Probe Design"
description: "Designing liveness, readiness, and startup probes so orchestration makes the right decisions"
tags: ["probes", "kubernetes", "health", "design"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
---

# Probe Design

## Summary
Probe design decides what liveness, readiness, and startup checks report and how they are implemented. Probes are the sensor layer of orchestration: Kubernetes (or any orchestrator) makes its decisions — restart this container, route traffic away from it, delay liveness checks — based entirely on what the probes report, so a probe that measures the wrong thing makes the orchestrator do the wrong thing with perfect reliability.

## Details
- Liveness answers 'should this container be restarted?'; readiness 'should this pod receive traffic?'; startup 'has the app finished booting?'. The three probe types map to three decisions: liveness failure → kill and restart (the recovery action for deadlocked or corrupted processes); readiness failure → remove from service (stop routing traffic, but do not restart — for overloaded or warming-up instances); startup failure → treat the container as still booting and suppress liveness checks (the protection for slow-booting apps, so a slow start does not get killed by an impatient liveness probe). The design error is conflating them — using readiness as liveness (a pod that is never ready is never restarted) or liveness as readiness (a restart loop that also flaps traffic).
- Probes should check the application, not the sidecar or the host. The probe endpoint must exercise the application's own ability to serve: the health endpoint that the application serves, not the sidecar's status, not the container's process existence, not the host's health. The classic failures: a liveness probe that checks "process is running" (a deadlocked process is still running — no restart), a readiness probe that checks only the health endpoint without dependencies (the pod is "ready" while its database is down — traffic arrives and fails), and the proxy trap: the probe goes through the sidecar (Envoy, Istio), so the sidecar's health is measured instead of the app's, and a dead app with a healthy sidecar is "ready" forever.
- Tune thresholds to boot time and GC pauses to avoid flapping. The probe parameters (initialDelay/startup, periodSeconds, timeoutSeconds, failureThreshold) define the envelope: the startup probe must exceed the worst-case boot time; the failure threshold must exceed the worst-case GC pause or transient slow period. The failure mode is flapping: thresholds too tight make a healthy-but-slow app oscillate between ready and not-ready (traffic flaps) or between restarts (a restart loop), which is worse than the failure the probe was trying to catch.
- Open question: when readiness should depend on downstream dependencies — readiness that includes the database catches the dependency outage early but can mark every replica not-ready simultaneously (and then nothing serves), whereas readiness that excludes dependencies lets traffic arrive and fail per-request; the answer is a design choice about where failures are absorbed.
- For mykb: probe design is the health-check node of the orchestration cluster — startup probes, containerization, and health-check patterns connect here.

## Related
- [[wiki/infrastructure/startup-probes|Startup Probes]] — the slow-boot protection
- [[wiki/infrastructure/containerization|Containerization]] — probes gate containerized apps
- [[wiki/infrastructure/health-check-patterns|Health Check Patterns]] — the broader family
- [[wiki/api-protocols/liveness-probes|Liveness Probes]] — restart semantics
- [[wiki/api-protocols/readiness-probes|Readiness Probes]] — traffic-gating semantics
