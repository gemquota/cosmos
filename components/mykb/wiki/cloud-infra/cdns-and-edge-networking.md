---
type: "concept"
title: "CDNs & Edge Networking"
description: "Distributed caches and compute that move content closer to users"
tags: ["cdn", "edge", "caching", "networking"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: [
  "https://en.wikipedia.org/wiki/Edge_computing",
  "https://en.wikipedia.org/wiki/Content_delivery_network",
]
---

# CDNs & Edge Networking

## Summary
CDNs and edge networks distribute content and compute across many locations close to users. Caching at the edge cuts latency and origin load; edge compute runs application logic there too. CDN architecture is a core part of modern web performance.

## Details
- A CDN caches static and dynamic responses at edge locations, keyed by URL and cache headers.
- Anycast routing lets many edge locations share an IP so users reach the nearest one automatically.
- Origin shielding and cache hierarchies prevent thundering herds when caches miss.
- Edge compute platforms run functions and applications at PoPs, moving logic closer to users.
- Cache invalidation and purging must be designed into the workflow, not bolted on after a bad deploy.
- In the mykb graph, CDNs connect to caching directives, anycast routing, edge locations, and content hashing articles.
- Provider consoles and CLI workflows differ, so the provider-specific articles in this cluster record the concrete steps and gotchas.

## Related
- [[wiki/cloud-infra/edge-locations|Edge Locations]]
- [[wiki/cloud-infra/multicast-networking|Multicast Networking]]
- [[wiki/cloud-infra/edge-computing|Edge Computing]]
- [[wiki/cloud-infra/vpc-networking|VPC Networking]]
