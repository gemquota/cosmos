---
type: "concept"
title: "Graceful Termination"
description: "Shutting down processes cleanly so in-flight work completes and clients see no errors"
tags: ["termination", "graceful-shutdown", "containers", "reliability"]
timestamp: "2026-08-01T00:00:00Z"
status: "stub"
---

# Graceful Termination

## Summary
Graceful termination gives processes time to finish in-flight requests, close connections, and flush state before exit. It is what turns routine restarts and deploys from user-visible errors into non-events.

## Details
- SIGTERM triggers graceful handling; SIGKILL is the ungraceful end — orchestration waits a grace period between them.
- PreStop hooks and connection draining coordinate with load balancers so traffic stops before the pod does.
- Watchdogs, queues, and external state must be flushed or checkpointed.
- Open question: how long a grace period is enough for the longest legitimate request.

## Related
- [[wiki/infrastructure/zero-downtime-deploys|Zero-Downtime Deploys]] — termination is the risky half
- [[wiki/infrastructure/containerization|Containerization]] — the lifecycle being terminated
- [[wiki/infrastructure/rolling-restarts|Rolling Restarts]] — termination at fleet scale
