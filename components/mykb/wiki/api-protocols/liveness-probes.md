---
type: "concept"
title: "Liveness Probes"
description: "Checks whether a process is alive and healthy enough to keep running, triggering restarts on failure"
tags: ["liveness", "probes", "kubernetes", "reliability"]
timestamp: "2026-07-31T00:00:00Z"
status: "growing"
---

# Liveness Probes

## Summary
Liveness probes determine whether a process is stuck — deadlocked, out of memory, wedged. A failing liveness probe makes the orchestrator kill and restart the container.

## Details
- Keep liveness checks cheap and independent of downstream services to avoid restart loops during outages.
- Distinguish from readiness: liveness restarts, readiness just removes traffic.
- Set initial-delay and failure thresholds to tolerate legitimate startup time.

## Configuration Guidance

- Keep the probe endpoint cheap: a handler that checks an in-process flag or heartbeat file, not a full dependency scan.
- Use `initialDelaySeconds` and `failureThreshold` generously so slow-starting containers are not killed during boot.
- Prefer HTTP or TCP probes over `exec` where possible; exec probes spawn processes and add overhead.
- A startup probe can protect applications with long or variable initialization times while liveness and readiness tune steady-state behavior.

## Failure Semantics

- When the kubelet observes consecutive liveness failures equal to `failureThreshold`, it kills the container and applies the restart policy.
- Repeated failures lead to `CrashLoopBackOff` with exponential backoff, which keeps a wedged container from consuming cluster resources.
- A common failure mode is a deadlock or goroutine leak that stops the main loop while the process stays alive; liveness catches this where process-level monitors cannot.
- Pair liveness with [[wiki/api-protocols/graceful-shutdown|Graceful Shutdown]] so restarts drain in-flight work instead of dropping connections.

## Operational Notes

- Treat probe timeouts, thresholds, and endpoints as deployment configuration that must be reviewed during rollout and incident postmortems.
- Monitor probe failure rates as a golden signal; a sudden rise usually precedes wider instability.


## Design Checklist

- A liveness endpoint should return 200 only when the process can make forward progress; return 500 on wedged internal state.
- Never place authentication in front of the kubelet's probe, and keep the handler dependency-free so it cannot deadlock with the very subsystem it checks.
- Record probe timing and failure history so tuning decisions are based on observed startup curves rather than guesses.
- Use separate readiness endpoints to gate traffic during deploys, keeping liveness purely about process health.


## Related
- [[wiki/api-protocols/readiness-probes|Readiness Probes]] — traffic vs process health
- [[wiki/api-protocols/health-checks|Health Checks]] — umbrella concept
- [[wiki/devops-infra/kubernetes|Kubernetes]] — kubelet restart policy
- [[wiki/security/container-hardening|Container Hardening]] — healthy base images
