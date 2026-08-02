---
type: "concept"
title: "CDN Practice"
description: "Serving static and edge-computable content from points of presence worldwide"
tags: ["cdn", "caching", "performance", "edge"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# CDN Practice

## Summary
CDNs cache and serve content from points of presence near users, cutting latency and origin load. Practice involves cache invalidation, TTL policy, dynamic-vs-static split, and edge logic where useful.

## Details
- Set Cache-Control correctly; CDN behavior follows it — purge only as an escape hatch.
- Cache static assets aggressively, HTML cautiously, and personalized content never.
- Edge workers (Cloudflare Workers, Lambda@Edge) move logic to the edge for locality.
- mykb relevance: the rendered wiki could CDN-cache article pages by immutable content hash.

## Related
- [[wiki/cloud-infra/content-delivery-networks|Content Delivery Networks]]
- [[wiki/cloud-infra/edge-computing|Edge Computing]]
- [[wiki/tooling/cache-control-headers|Cache-Control Headers]]
- [[wiki/tooling/cache-invalidation|Cache Invalidation]]
- [[wiki/cloud-infra/point-of-presence|Point of Presence]]
