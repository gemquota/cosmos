---
type: "concept"
title: "Liveness Probes"
description: "Checks whether a process is alive and healthy enough to keep running, triggering restarts on failure"
tags: ["liveness", "probes", "kubernetes", "reliability"]
timestamp: "2026-07-31T00:00:00Z"
status: "stub"
---

# Liveness Probes

## Summary
Liveness probes determine whether a process is stuck — deadlocked, out of memory, wedged. A failing liveness probe makes the orchestrator kill and restart the container.

## Details
- Keep liveness checks cheap and independent of downstream services to avoid restart loops during outages.
- Distinguish from readiness: liveness restarts, readiness just removes traffic.
- Set initial-delay and failure thresholds to tolerate legitimate startup time.

## Related
- [[wiki/api-protocols/readiness-probes|Readiness Probes]] — traffic vs process health
- [[wiki/api-protocols/health-checks|Health Checks]] — umbrella concept
- [[wiki/devops-infra/kubernetes|Kubernetes]] — kubelet restart policy
- [[wiki/security/container-hardening|Container Hardening]] — healthy base images
