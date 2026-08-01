---
type: "concept"
title: "Edge Computing"
description: "Running compute close to users at CDN points of presence instead of centralized regions"
tags: ["edge", "compute", "cdn", "latency"]
timestamp: "2026-08-01T00:00:00Z"
status: "stub"
---

# Edge Computing

## Summary
Edge computing executes logic at network edge locations near users — in front of CDN caches or even on devices.

## Details
- Edge workers (Cloudflare Workers, Lambda@Edge) run small functions at PoPs with cold-start and size limits.
- Best for: header-based routing, A/B decisions, authentication checks, and cache augmentation — not heavy compute.
- State lives far from the edge, so consistency and storage must stay in the origin or a shared store.

## Related
- [[wiki/cloud-infra/content-delivery-networks|Content Delivery Networks]] — the platform edge compute extends
- [[wiki/cloud-infra/latency-optimization|Latency Optimization]] — the goal of edge placement
- [[wiki/cloud-infra/function-as-a-service|Function-as-a-Service]] — the execution model edge uses
- [[wiki/devops-infra/cloudflare|Cloudflare]] — edge compute provider
