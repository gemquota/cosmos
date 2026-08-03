---
type: "concept"
title: "Readiness vs Liveness Probes"
description: "Distinguishing restart-worthy failure from not-ready states"
tags: ["probes", "kubernetes", "health", "readiness"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Readiness vs Liveness Probes

## Summary
Liveness and readiness probes answer two different questions: liveness asks whether the process is alive (should it be restarted?), readiness asks whether it can serve traffic (should it be in rotation?). Confusing them is one of the most common causes of avoidable outages — a readiness failure treated as a restart, or a liveness check that passes while the app serves errors.

## Details
- Liveness: a failure restarts the container — appropriate for deadlocks and hangs; inappropriate for slow-but-recovering states (the restart makes it worse).
- Readiness: a failure removes the pod from Service endpoints — appropriate for dependency outages (database down), warm-up, and overload; the pod stays alive and recovers without a restart.
- Mechanism: both are probes (exec, TCP, HTTP) with periodSeconds, timeoutSeconds, failureThreshold, successThreshold; startupProbe protects slow-starting containers from liveness failures during boot; the kubelet enforces the thresholds independently.
- Concrete example: an app whose readiness probe checks the database connection — during a DB outage, traffic stops (503 from the pod) while the process stays alive; liveness probes only process health, so the pod is not restarted; after the DB recovers, the pod re-enters rotation.
- Failure modes: liveness thresholds too tight — a GC pause or slow request restarts the pod repeatedly (crash-loop flapping); readiness probes that share fate with dependencies, taking down capacity during partial outages; readiness depending on liveness (the same endpoint), making both useless; probes that are too expensive, adding load; probe logic that differs from real traffic paths, so readiness passes while users fail.
- Tradeoffs: deep readiness checks protect users but reduce capacity during partial failures; shallow checks keep capacity but pass bad traffic; the design rule is: restart for what restart fixes, drain for what time fixes.
- Operational notes: tune thresholds on real latency data, monitor restart counts and ready transitions, and test probe behavior in game days.
- RSIS3 relevance: the wiki daemon's probes should follow the split — restart on hangs, drain on dependency loss — so RSIS3's monitoring sees availability accurately.

## Related
- [[wiki/devops-infra/kubernetes-control-plane|Kubernetes Control Plane]]
- [[wiki/devops-infra/observability-pillars|Observability Pillars]]
- [[wiki/syntheses/knowledge-acquisition-workflow|Knowledge Acquisition Workflow]] — how stubs grow into full articles in mykb
- [[wiki/syntheses/mykb-acquisition-curation-and-practices|Acquisition, Curation & Practices]] — the curation loop this stub belongs to
