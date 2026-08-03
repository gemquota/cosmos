---
type: "concept"
title: "Latency Optimization"
description: "Techniques to reduce request latency: caching, edge placement, protocols, and tracing-driven tuning"
tags: ["latency", "performance", "caching", "tuning"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
---
# Latency Optimization

## Summary

Latency optimization is the systematic reduction of end-to-end response time: fewer round trips, shorter distances, less queueing, and faster processing. It is a budget exercise — every millisecond is spent somewhere, and the best wins come from architecture, not tuning knobs.

## Details
- Mechanism: the response-time budget splits into network RTTs (DNS, TCP, TLS, HTTP), server processing, and rendering; optimizations attack each: DNS caching/prefetch, connection reuse and preconnect, TLS 1.3/0-RTT, HTTP/3, edge caching, CDN placement, and server-side work reduction (caching, prefetching, parallelism). Each technique has a measurable cost-benefit on a specific path.
- Concrete example: an API that needs 4 sequential backend calls can be cut to 1 by fan-out (parallel calls) or to 0 by caching — the difference is often 100ms+; moving a service to the user's region or an edge removes 100ms of propagation; HTTP/2 pooling removes handshake RTTs on repeat requests.
- Failure modes: optimizing the wrong layer (tuning TLS when the bottleneck is a sequential backend chain); micro-optimizations with unmeasured impact; adding complexity (caching layers, edge logic) that creates staleness or failure modes for unproven gains; and measuring lab latency while field conditions (mobile, shared links) dominate.
- Operational tradeoffs: the discipline is budget-first: instrument each hop, identify the biggest spend, fix it, re-measure; cache and placement beat protocol tweaks almost always. Keep the architecture simple enough that the latency model stays visible.
- RSIS3/mykb relevance: the wiki's API latency budgets per route are recorded here; the loop's improvement cycles target the largest measured hop, not the easiest knob.
- Technique menu: DNS prefetch and preconnect trim connection setup; CDN/edge caching removes origin trips; HTTP/3 and TLS 1.3 cut handshake RTTs; server push/preload hide discovery latency; keep the menu ordered by expected impact per path.
- Field vs lab: synthetic probes measure the path, but field data (RUM, traces) captures the user's real network; optimize what the field shows is slow, and re-validate after each change.

## Related
- [[wiki/devops-infra/distributed-tracing|Distributed Tracing]] — finds where latency goes
- [[wiki/cloud-infra/content-delivery-networks|Content Delivery Networks]] — edge caching for static content
- [[wiki/api-protocols/http-caching|HTTP Caching]] — cache semantics
