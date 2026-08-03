---
type: "concept"
title: "Startup Probes & Graceful Shutdown"
description: "Slow-start handling and draining connections on shutdown"
tags: ["startup-probe", "shutdown", "kubernetes", "lifecycle"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Startup Probes & Graceful Shutdown

## Summary
Startup probes protect slow-booting containers from premature restarts, and graceful shutdown gives containers time to finish work before termination. Together they make pod lifecycles safe: the startup probe tells the kubelet when the process is actually ready to be checked, and preStop plus terminationGracePeriod lets the app drain connections and persist state.

## Details
- Startup probe mechanics: startupProbe (HTTP, TCP, or exec) runs until it succeeds once, after which liveness takes over; it replaces the old trick of long liveness failureThresholds for slow starts — the process gets the whole startup window without being killed for not responding.
- Graceful shutdown mechanics: on termination, the kubelet runs preStop hooks, sends SIGTERM, waits terminationGracePeriodSeconds (default 30s), then SIGKILLs; a well-behaved app traps SIGTERM, stops accepting new work, drains in-flight requests, flushes state, and exits before the grace period ends.
- Concrete example: a Java service that needs 90s to warm caches has a startup probe with a generous period and failureThreshold, then liveness with tight thresholds; preStop calls a /shutdown endpoint and sleeps 5s so the load balancer deregisters the pod before the process exits; the service drains requests and flushes the buffer.
- Failure modes: no startup probe, so slow starts get killed in a restart loop; preStop hooks that exceed the grace period, so the process is SIGKILLed mid-drain; grace periods too short for real work, causing data loss; SIGTERM handlers that do not exit, hanging until the kill; readiness and preStop racing so new traffic arrives while the pod is draining.
- Tradeoffs: startup probes and grace periods trade orchestration simplicity for application-specific timing knowledge; too-generous values slow rollouts and node drains; too-tight values cause restarts and data loss; the design rule is to make the app drain fast and tell the orchestrator the real numbers.
- Operational notes: log shutdown progress, monitor forced-kill events (a signal of too-tight grace), and test termination in game days.
- RSIS3 relevance: the wiki daemon's startup (open the store, build indexes) and shutdown (flush state, drain requests) map directly to startup probes and preStop — a graceful daemon makes RSIS3's restarts safe.

## Related
- [[wiki/infrastructure/startup-probes|Startup Probes]]
- [[wiki/infrastructure/graceful-termination|Graceful Termination]]
