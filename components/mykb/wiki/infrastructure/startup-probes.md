---
type: "concept"
title: "Startup Probes"
description: "Kubernetes probes that give slow-starting containers time before liveness checks begin"
tags: ["kubernetes", "probes", "startup", "containers"]
timestamp: "2026-08-01T00:00:00Z"
status: "stub"
---

# Startup Probes

## Summary
A startup probe delays liveness checks until an application has finished initializing, so slow boots are not killed as failures. It replaces the old trick of generous liveness thresholds.

## Details
- While the startup probe fails, liveness is not evaluated; when it succeeds, liveness takes over.
- Set success threshold and failure budget to the worst-case boot time.
- Common causes of slow boots: model loading, cache warming, JVM/classpath warmup.
- Open question: whether startup probes belong in the app or the deployment manifest.

## Related
- [[wiki/infrastructure/probe-design|Probe Design]] — where startup probes fit
- [[wiki/infrastructure/containerization|Containerization]] — slow boots in containerized apps
- [[wiki/infrastructure/pod-lifecycle|Pod Lifecycle]] — the phase startup probes gate
- [[wiki/api-protocols/liveness-probes|Liveness Probes]] — what startup probes defer
