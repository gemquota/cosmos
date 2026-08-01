---
type: "concept"
title: "Pod Lifecycle"
description: "The states and events a Kubernetes pod passes through: pending, running, terminating, and beyond"
tags: ["kubernetes", "pods", "lifecycle", "containers"]
timestamp: "2026-08-01T00:00:00Z"
status: "stub"
---

# Pod Lifecycle

## Summary
A pod's lifecycle spans creation, scheduling, running, and termination, with health probes and termination hooks at each stage. Understanding it is the key to safe rolling operations.

## Details
- Phases: Pending (scheduling), Running (containers up), Succeeded/Failed, plus ContainerCreating and Terminating.
- Readiness gates traffic, liveness restarts, and startup probes delay liveness during slow boots.
- Termination is graceful: SIGTERM, preStop hook, grace period, then SIGKILL.
- Open question: how lifecycle events should map to observability and alerting.

## Related
- [[wiki/infrastructure/containerization|Containerization]] — pods contain the containers
- [[wiki/infrastructure/startup-probes|Startup Probes]] — protect slow-booting containers
- [[wiki/infrastructure/container-scheduling|Container Scheduling]] — how pods get placed
- [[wiki/api-protocols/liveness-probes|Liveness Probes]] — restart decisions in the lifecycle
