---
type: "concept"
title: "Edge Locations"
description: "PoPs closer to users where CDNs and serverless runtimes cache and execute"
tags: ["edge", "cdn", "latency", "cloud"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# Edge Locations

## Summary

Edge locations are the distributed points where a provider terminates user traffic close to them — CDN caches, DNS anycast, serverless functions, and load balancers. They collapse latency by moving the response, not the data, closer to the user.

## Details
- Mechanism: providers (Cloudflare, Fastly, AWS CloudFront/Lambda@Edge, GCP/Azure edge) run thousands of PoPs; routing (anycast or DNS) lands users on the nearest one; caches serve static and dynamic-content variants; edge compute runs small functions (redirects, auth checks, personalization) without a round trip to origin.
- Concrete example: a wiki page's static assets serve from an edge cache in the user's city (5ms vs 150ms to origin); the edge runs an auth cookie check and rewrites URLs, sending only uncacheable requests to origin; a DDoS is absorbed at the edge, with origin shielded behind an allow-listed IP range.
- Failure modes: treating edge as a cache when dynamic content is uncacheable (origin round-trips anyway); cache invalidation mistakes serving stale content (purge propagation takes time); edge compute limits (runtime, memory, egress) surprising developers; and the edge becoming the single point of failure if origin connectivity or TLS config breaks.
- Operational tradeoffs: edge architecture trades origin control for latency and scale; the model is cache-first with explicit invalidation, origin shielding, and edge-side validation. Measure cache hit ratio and origin RTT per route, and keep a fallback path when the edge degrades.
- RSIS3/mykb relevance: the cosmos/hub deployments serve through edge locations with cache policies documented here; the loop's release notes include purge commands so users never see stale assets.
- Origin shielding: let the edge aggregate and cache origin requests; an edge that forwards every miss to origin is a latency tax, not a CDN.
- Cache keys: set cache keys and TTLs per content class; a default-cacheable edge serves stale assets until the invalidation is practiced.

## Related
- [[wiki/cloud-infra/cdns-and-edge-networking|CDNs & Edge Networking]]
- [[wiki/devops-infra/rate-limiting-at-edge|Rate Limiting at the Edge]]
- [[wiki/cloud-infra/edge-computing|Edge Computing]]
- [[wiki/cloud-infra/networking-fundamentals|Networking Fundamentals]]
- [[wiki/syntheses/knowledge-acquisition-workflow|Knowledge Acquisition Workflow]]
- [[wiki/syntheses/mykb-acquisition-curation-and-practices|Acquisition, Curation & Practices]]
