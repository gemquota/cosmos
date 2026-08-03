---
type: "concept"
title: "Graceful Termination"
description: "Shutting down processes cleanly so in-flight work completes and clients see no errors"
tags: ["termination", "graceful-shutdown", "containers", "reliability"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
---

# Graceful Termination

## Summary
Graceful termination gives processes time to finish in-flight requests, close connections, and flush state before exit. It is what turns routine restarts and deploys from user-visible errors into non-events — the difference between "the service restarted" and "users saw 502s during the restart".

## Details
- SIGTERM triggers graceful handling; SIGKILL is the ungraceful end — orchestration waits a grace period between them. The Unix contract: a well-behaved process installs a SIGTERM handler that stops accepting new work, drains what is in flight, and exits with code 0; the orchestrator (systemd, Kubernetes, a process supervisor) sends SIGTERM, waits a configured grace period, and only then sends SIGKILL to the unresponsive process. The whole art of graceful termination is in that window: what the process does between SIGTERM and exit. The common failures are the two extremes — a process that exits immediately on SIGTERM (dropping in-flight work) and a process that ignores SIGTERM until the SIGKILL (no graceful phase at all).
- PreStop hooks and connection draining coordinate with load balancers so traffic stops before the pod does. In Kubernetes, the endpoint-removal dance is: the pod is marked terminating, the Service's endpoints are updated to exclude it, the PreStop hook runs (often `sleep 5` — the infamous but pragmatic way to let the load balancer converge), then SIGTERM is sent. The purpose of the sequence is ordering: traffic must stop arriving before the process stops serving it, and the grace period must cover both the load-balancer propagation and the in-flight drain. The failure mode is the race: if the process exits before the load balancer stops sending, requests hit a dead pod — which is exactly what readiness probes and longer PreStop sleeps exist to prevent.
- Watchdogs, queues, and external state must be flushed or checkpointed. A graceful shutdown is also a data-integrity event: in-flight work (a message being processed, a transaction open, a file being written) must be completed, rolled back, or durably checkpointed before exit — otherwise the "graceful" restart silently loses work that was acknowledged but not completed. This is why message consumers must process with exactly-once semantics or re-queue on shutdown, and why databases flush WAL before exiting.
- Open question: how long a grace period is enough for the longest legitimate request — the tension between fast deploys (short grace) and in-flight completion (long grace), where the answer is usually "make requests bounded so the grace period can be".
- For mykb: graceful termination is the process-level half of zero-downtime deploys — the sibling nodes cover the deployment mechanics at fleet scale.

## Related
- [[wiki/infrastructure/zero-downtime-deploys|Zero-Downtime Deploys]] — termination is the risky half
- [[wiki/infrastructure/containerization|Containerization]] — the lifecycle being terminated
- [[wiki/infrastructure/rolling-restarts|Rolling Restarts]] — termination at fleet scale
