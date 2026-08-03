---
type: "concept"
title: "Connection Pools"
description: "Reusing connections to amortize handshake and socket costs"
tags: ["connection-pools", "networking", "performance", "clients"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Connection Pools

## Summary
Connection pools reuse a bounded set of TCP connections to a backend (database, HTTP service) across many requests, amortizing handshake cost and preventing connection storms. Pool sizing, timeouts, and health checks determine whether the pool helps or becomes the bottleneck under load.

## Details
- Mechanism: a pool holds idle connections, hands them to callers, checks them out and back in with a mutex or queue, and creates or destroys connections as demand changes. Sizing rules matter: too few connections serialize requests; too many exhaust backend resources — Postgres has a hard connection ceiling.
- Concrete example: an app with 100 concurrent requests against a Postgres pool of 20 — the pool queues excess requests; pgbouncer in transaction mode multiplexes many client sessions over a few server connections; an HTTP pooler keeps keep-alive connections warm to a gateway.
- Failure modes: pool exhaustion when a backend slows down — requests pile up on held connections and acquisition timeouts cascade; stale connections after a backend restart — the pool hands out dead sockets until health-checked; unbounded growth from connection leaks where callers forget to release; the pool-shrink problem where idle connections are closed under memory pressure just as load returns.
- Operational notes: set acquire and lease timeouts, validate connections on borrow (SELECT 1 or a TCP probe), size pools from peak concurrency rather than average, add jitter to connection creation to avoid thundering-herd reconnects after an outage, and monitor wait time and utilization.
- Tradeoffs: pooling trades complexity for latency and backend protection; connection-per-request is simpler but cannot survive high fan-out; pooling per process versus a centralized pooler (pgbouncer) is a resource-versus-ops tradeoff.
- RSIS3 relevance: RSIS3 agents issuing parallel mykb queries benefit from a shared pool so bursts of retrieval do not exhaust the wiki daemon's connection budget.

## Related
- [[wiki/cloud-infra/connection-multiplexing|Connection Multiplexing]] — related coverage in the same cluster
- [[wiki/devops-infra/connection-pooling|Connection Pooling]] — related coverage in the same cluster
- [[wiki/devops-infra/worker-pools|Worker Pools]] — related coverage in the same cluster
- [[wiki/infrastructure/node-pools|Node Pools]] — related coverage in the same cluster
- [[wiki/devops-infra/kubernetes-control-plane|Kubernetes Control Plane]] — related coverage in the same cluster
- [[wiki/devops-infra/observability-pillars|Observability Pillars]] — related coverage in the same cluster
- [[wiki/syntheses/knowledge-acquisition-workflow|Knowledge Acquisition Workflow]] — how stubs grow into full articles in mykb
- [[wiki/syntheses/mykb-acquisition-curation-and-practices|Acquisition, Curation & Practices]] — the curation loop this stub belongs to
