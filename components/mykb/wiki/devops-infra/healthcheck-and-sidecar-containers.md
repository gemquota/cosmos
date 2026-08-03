---
type: "concept"
title: "Healthcheck & Sidecar Containers"
description: "Sidecars that proxy, sync, or check the health of the main container"
tags: ["sidecar", "healthcheck", "kubernetes", "patterns"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Healthcheck & Sidecar Containers

## Summary
Health checks tell the orchestrator whether a container is alive and ready; sidecar containers run supporting processes alongside the main app in the same pod — log shippers, proxies, config reloaders, secrets providers. Together they form the pattern of a self-describing, self-managing pod: the sidecar prepares or observes, and health checks decide its fate.

## Details
- Health check mechanics: livenessProbe restarts a dead-locked process; readinessProbe removes an unready pod from service endpoints; startupProbe protects slow-starting apps from premature liveness failures; probes run exec, TCP, or HTTP checks on a schedule with failure thresholds.
- Sidecar mechanics: a pod declares additional containers sharing the network namespace, volumes, and lifecycle; sidecars can start before the app (init-style), run alongside (log shipping, metrics, proxies), or gate startup via the new sidecar readiness gates.
- Concrete example: a pod with an app container, an Envoy sidecar for mTLS, a Fluent Bit sidecar for logs, and an init container that renders config; the app's readinessProbe checks the DB; when the DB is down, traffic stops while the pod stays alive for recovery.
- Failure modes: probes that restart healthy pods (liveness thresholds too tight with slow GC pauses) causing crash-loop flapping; readiness checks that share fate with the main app (a sidecar polling the same endpoint the app depends on); sidecars that consume the pod's resource budget and get OOM-killed, degrading the main app; sidecar update rollouts restarting the whole pod.
- Tradeoffs: sidecars encapsulate cross-cutting concerns cleanly and are rolled out with the app, but multiply image, resource, and security surface per pod; health checks trade orchestrator simplicity for careful threshold tuning; multi-container pods complicate debugging and cost accounting.
- Operational notes: keep probes cheap and idempotent, set distinct liveness/readiness thresholds, and monitor restart counts and ready-gate timing.
- RSIS3 relevance: if the wiki daemon runs with sidecars (logging, TLS), the same health contract tells RSIS3's monitoring when retrieval is truly available versus merely alive.

## Related
- [[wiki/os-shell/containers-vs-vms|Containers vs VMs]]
- [[wiki/devops-infra/init-containers-and-hooks|Init Containers & Hooks]]
- [[wiki/infrastructure/sidecar-pattern|Sidecar Pattern]]
- [[wiki/devops-infra/kubernetes-control-plane|Kubernetes Control Plane]]
- [[wiki/syntheses/knowledge-acquisition-workflow|Knowledge Acquisition Workflow]] — how stubs grow into full articles in mykb
- [[wiki/syntheses/mykb-acquisition-curation-and-practices|Acquisition, Curation & Practices]] — the curation loop this stub belongs to
