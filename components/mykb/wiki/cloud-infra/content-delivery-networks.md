---
type: "concept"
title: "Content Delivery Networks"
description: "Geographically distributed proxy networks that cache content at the edge to cut latency and protect origins"
tags: ["cdn", "caching", "edge", "latency", "web-performance"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://developer.mozilla.org/en-US/docs/Glossary/CDN"]
---

# Content Delivery Networks

## Summary
A content delivery network (CDN) replicates and serves content from points of presence close to users, cutting round-trip latency and offloading the origin. CDNs cache static assets, terminate TLS at the edge, and absorb traffic spikes and DDoS floods. They are a standard component of global web platforms.

## Details
- Caching is the core mechanism: edge nodes store responses and serve them until TTL expiry, honoring Cache-Control and ETag semantics from the origin.
- Dynamic acceleration: even uncacheable responses can benefit from optimized routing, TCP tuning, and connection reuse between edge and origin.
- Origin shielding: a CDN collapses many edge cache misses into a single upstream request, protecting the origin from thundering herds.
- Edge compute extends CDNs from static caching to request-time logic (routing, A/B, personalization) without returning to the origin.
- Security features bundle with the edge: WAF rules, bot management, and volumetric DDoS mitigation.
- Worked example: a mykb static wiki served through a CDN would place HTML, CSS, and images at 100+ PoPs with long cache TTLs and cache-busted asset URLs for instant invalidation.
- Trade-offs: stale-content windows, cache-invalidation complexity, and provider lock-in are the main costs; purging APIs and short TTLs for mutable content mitigate them.

## Related
- [[wiki/cloud-infra/edge-computing|Edge Computing]] — moving compute to the CDN edge
- [[wiki/cloud-infra/latency-optimization|Latency Optimization]] — the performance goal CDNs serve
- [[wiki/cloud-infra/dns-management|DNS Management]] — DNS routing steers users to nearby PoPs
- [[wiki/devops-infra/cloudflare|Cloudflare]] — CDN provider with edge compute
- [[wiki/api-protocols/http-caching|HTTP Caching]] — the semantics CDNs rely on
- [[wiki/security/https|HTTPS]] — TLS termination at the edge
