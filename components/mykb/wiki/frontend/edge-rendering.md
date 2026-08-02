---
type: "concept"
title: "Edge Rendering"
description: "Executing rendering logic at CDN edge nodes for low latency"
tags: [edge", "rendering", "serverless", "cdn", "performance"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://developers.cloudflare.com/workers/concepts/how-workers-works/", "https://vercel.com/docs/functions"]
---

# Edge Rendering

## Summary
Edge rendering moves page generation from a central origin to CDN edge nodes physically close to the visitor. The server renders HTML — or rewrites and personalizes a cached page — inside a lightweight runtime such as a Worker, cutting network round trips to milliseconds. It sits between fully static files and regional server rendering.

## Details
- Proximity: executing in the nearest datacenter reduces connection latency compared with a distant origin region.
- Cold starts are small: edge runtimes boot in milliseconds and cap CPU time, memory, and bundle size tightly.
- Typical work: HTML streaming, header manipulation, A/B variants, geolocation personalization, and token checks before serving.
- Caching synergy: edge renderers set cache-control headers and can serve cached responses when logic does not need to run.
- Limits: no long-lived connections or local disk; heavy computation belongs in regional functions or workers.
- Use case: a cosmos dashboard could render its telemetry shell at the edge, injecting fresh chart data while static assets stay cached.

## Related
- [[wiki/frontend/edge-functions|Edge Functions]] — the runtime edge rendering executes on
- [[wiki/frontend/server-side-rendering|Server-Side Rendering]] — regional rendering alternative
- [[wiki/frontend/ssg|Static Site Generation]] — the fully static baseline
- [[wiki/cloud-infra/edge-computing|Edge Computing]] — infrastructure behind edge nodes
- [[wiki/cloud-infra/latency-optimization|Latency Optimization]] — the goal edge rendering serves
- [[wiki/cloud-infra/content-delivery-networks|Content Delivery Networks]] — the network edge runs on
