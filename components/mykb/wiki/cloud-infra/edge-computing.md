---
type: "concept"
title: "Edge Computing"
description: "Running compute close to users at CDN points of presence instead of centralized regions"
tags: ["edge", "compute", "cdn", "latency"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://en.wikipedia.org/wiki/Edge_computing", "https://aws.amazon.com/edge/"]
---

# Edge Computing

## Summary
Edge computing executes logic at network edge locations near users — in front of CDN caches or even on devices.

## Details
- Edge workers (Cloudflare Workers, Lambda@Edge) run small functions at PoPs with cold-start and size limits.
- Best for: header-based routing, A/B decisions, authentication checks, and cache augmentation — not heavy compute.
- State lives far from the edge, so consistency and storage must stay in the origin or a shared store.
- Edge computing moves computation close to data sources and users — devices, local gateways, or provider edge locations — instead of a distant central cloud.
- It cuts latency for interactive workloads, reduces bandwidth for data-heavy pipelines, and keeps sensitive data local.
- The tradeoffs are constrained resources, distributed management, and a more complex update and security surface.
- Edge and cloud form a continuum: edge nodes handle the latency-critical work while the cloud provides coordination and heavy compute.
- **Worked example / comparison** — Worked example — a mobile wiki client runs local indexing and embeddings on-device (edge), syncing only deltas to the cloud graph service.
- For mykb, edge computing is documented as the latency-driven counterpart to the cloud-infra cluster, with the mobile bundle as its local edge.

## Related
- [[wiki/cloud-infra/content-delivery-networks|Content Delivery Networks]]
- [[wiki/cloud-infra/latency-optimization|Latency Optimization]]
- [[wiki/cloud-infra/function-as-a-service|Function-as-a-Service]]
- [[wiki/devops-infra/cloudflare|Cloudflare]]
- [[wiki/concepts/promotion-readiness|Promotion Readiness]]
- [[wiki/ai-ml/article-health-scores|Article Health Scores]]
- [[wiki/concepts/explainers|Explainers]]
