---
type: "concept"
title: "Latency Optimization"
description: "Techniques to reduce request latency: caching, edge placement, protocols, and tracing-driven tuning"
tags: ["latency", "performance", "caching", "tuning"]
timestamp: "2026-08-01T00:00:00Z"
status: "stub"
---

# Latency Optimization

## Summary
Latency optimization systematically reduces the time between a user action and the response: caching, closer compute, faster protocols, and data-driven bottlenecks. Distributions matter more than averages.

## Details
- Measure first: p95/p99 and tracing identify the real slow path before any tuning (see distributed tracing).
- Cache aggressively at every layer — CDN, HTTP caches, application caches — while keeping invalidation correct.
- Move compute closer (edge) and data closer (regional placement, read replicas) to cut round trips.
- Protocols: HTTP/2, HTTP/3, TLS 1.3, and connection reuse shave handshake and head-of-line delays.

## Related
- [[wiki/devops-infra/distributed-tracing|Distributed Tracing]] — finds where latency goes
- [[wiki/cloud-infra/content-delivery-networks|Content Delivery Networks]] — edge caching for static content
- [[wiki/api-protocols/http-caching|HTTP Caching]] — cache semantics
