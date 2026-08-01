---
type: "concept"
title: "Graceful Shutdown"
description: "Smoothly draining in-flight work and closing resources when a process receives a stop signal"
tags: ["shutdown", "reliability", "processes", "devops", "signals"]
timestamp: "2026-07-31T00:00:00Z"
status: "stub"
---

# Graceful Shutdown

## Summary
Graceful shutdown handles SIGTERM/SIGINT by stopping new work, draining in-flight requests and queue messages, closing connections, and then exiting — instead of dying mid-write.

## Details
- Typical sequence: deregister from load balancers, stop accepting work, wait for active tasks with a deadline, flush state, close pools.
- Critical for databases and queues: unacked messages or half-written notes corrupt state.
- Orchestrators (Kubernetes) send SIGTERM and wait for the pod to exit before SIGKILL.

## Related
- [[wiki/api-protocols/health-checks|Health Checks]] — readiness drops during drain
- [[wiki/api-protocols/message-queues|Message Queues]] — ack or re-queue in-flight messages
- [[wiki/devops-infra/kubernetes|Kubernetes]] — pod termination lifecycle
- [[wiki/devops-infra/connection-pooling|Connection Pooling]] — close pooled connections cleanly
- [[wiki/devops-infra/replication|Replication]] — avoid split-brain on shutdown
- [[wiki/api-protocols/websockets|WebSockets]] — draining active connections on shutdown
