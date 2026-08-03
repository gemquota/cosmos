---
type: "concept"
title: "Graceful Shutdown"
description: "Draining traffic and finishing work before a process exits"
tags: ["ops", "reliability", "process", "http"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# Graceful Shutdown

## Summary
Graceful shutdown is the sequence of stopping new work, finishing in-flight work, and then exiting when a process receives a termination signal. It turns deploys and restarts from error-generating events into zero-downtime operations.

## Details
The lifecycle: the orchestrator sends SIGTERM; the process stops accepting new connections (or the load balancer marks it unhealthy and drains), waits for in-flight requests to complete up to a deadline, closes connection pools and message queue subscriptions cleanly, flushes state, and exits. SIGKILL is the failure mode — what happens when the process doesn't exit in time — so the whole sequence is bounded by a grace period.

The mechanism: readiness probes drop to "not ready" the moment shutdown starts, so the load balancer stops routing new traffic; the server stops listening on new sockets; active requests get a bounded drain window (configurable, typically 10-30 seconds); persistent connections (WebSockets, long polls) get explicit close frames or are allowed to finish; then the process flushes and exits. Anything not finished after the deadline is cut, so in-flight work must be designed to be resumable or idempotent.

Concrete example: a wiki API runs in Kubernetes with terminationGracePeriodSeconds: 30. On rollout, the pod's readiness probe fails immediately, the endpoint is removed from the service, the container receives SIGTERM, the web server stops accepting and finishes the ~40 in-flight requests in under five seconds, the connection pool drains, and the process exits with code 0. Users see zero failed requests.

Failure modes: ignoring SIGTERM and letting the orchestrator escalate to SIGKILL loses in-flight writes; long-lived requests that never finish eat the whole grace period; workers that aren't drained (cron jobs, queue consumers) drop messages unless they ack or re-queue on shutdown; and shutting down a replica without a readiness drop causes the load balancer to route into a dead socket.

Operational tradeoffs: longer grace periods reduce lost work but slow rollouts and pile up during cascading restarts; readiness-based draining requires the orchestrator and probe configuration to agree. The robust pattern: signal handling that starts drain immediately, a hard deadline, idempotent work items so kills are safe, and health checks that reflect drain state.

RSIS3/mykb relevance: RSIS3's own long-running loops should implement the same drain-on-SIGTERM contract; documenting it here keeps loop restarts from dropping mid-cycle telemetry.

## Related
- [[wiki/api-protocols/health-checks|Health Checks]] — readiness drops during drain
- [[wiki/api-protocols/message-queues|Message Queues]] — ack or re-queue in-flight messages
- [[wiki/devops-infra/kubernetes|Kubernetes]] — pod termination lifecycle
- [[wiki/devops-infra/connection-pooling|Connection Pooling]] — close pooled connections cleanly
- [[wiki/devops-infra/replication|Replication]] — avoid split-brain on shutdown
- [[wiki/api-protocols/websockets|WebSockets]] — draining active connections on shutdown
