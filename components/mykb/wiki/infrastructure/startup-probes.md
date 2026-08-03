---
type: "concept"
title: "Startup Probes"
description: "Kubernetes probes that give slow-starting containers time before liveness checks begin"
tags: ["kubernetes", "probes", "startup", "containers"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
---

# Startup Probes

## Summary
A startup probe delays liveness checks until an application has finished initializing, so slow boots are not killed as failures. It replaces the old trick of generous liveness thresholds, letting readiness and liveness stay strict while the startup window absorbs boot-time variance.

## Details
- Mechanism: while the startup probe is failing, Kubernetes does not evaluate liveness at all; once it succeeds, liveness takes over with its normal (strict) thresholds. Startup checks typically target a lightweight endpoint that becomes healthy only when initialization is complete.
- Configuration: set `periodSeconds` and `failureThreshold` so the total failure budget covers the worst-case boot time — for example 30 checks at 2-second intervals allows 60 seconds — and use a probe command or HTTP GET against a readiness-style endpoint that reflects actual readiness, not just process liveness.
- Common causes of slow boots: model loading and weight initialization, cache warming, JVM and classpath warmup, TLS truststore loading, and lazy database connection pools. These are exactly the cases where a liveness probe with a tight threshold would kill the container mid-boot.
- Concrete example: a machine-learning service that loads a multi-gigabyte model in 90 seconds. A liveness probe with a 5-second timeout restarts it in a crash loop; a startup probe with a 120-second budget lets the load finish, then hands off to a strict liveness check that catches real hangs afterward.
- Failure modes: startup probes that pass before the app is actually ready cause traffic to hit half-initialized pods; probes that never succeed keep the pod in a restart loop while hiding the underlying init failure; and probe endpoints with heavy handlers add load during boot.
- Tradeoffs: putting boot-window logic in the manifest keeps images generic, but probes are deployment concern, not application logic — the endpoint still has to exist in the app. There is also a question of whether the check belongs in the app at all versus the container's entrypoint.
- RSIS3/mykb relevance: probe design is a standing pattern for self-improvement loops that deploy services; this node supplies the ordering rule — startup gates liveness — so retrievals do not conflate boot time with runtime health.

## Related
- [[wiki/infrastructure/probe-design|Probe Design]] — where startup probes fit
- [[wiki/infrastructure/containerization|Containerization]] — slow boots in containerized apps
- [[wiki/infrastructure/pod-lifecycle|Pod Lifecycle]] — the phase startup probes gate
- [[wiki/api-protocols/liveness-probes|Liveness Probes]] — what startup probes defer
