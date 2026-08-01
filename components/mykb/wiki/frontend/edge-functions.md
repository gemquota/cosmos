---
type: "concept"
title: "Edge Functions"
description: "Small serverless functions executed at CDN edge nodes close to users for low-latency logic"
tags: ["edge", "serverless", "cdn", "frontend", "compute"]
timestamp: "2026-07-31T00:00:00Z"
status: "growing"
source: ["https://developers.cloudflare.com/workers/"]
---

# Edge Functions

## Summary
Edge functions are lightweight serverless functions that run on CDN edge nodes — geographically close to the user — instead of a central region. They handle request routing, authentication, personalization, and API aggregation with single-digit-millisecond cold starts. Cloudflare Workers, Vercel Edge Functions, and Deno Deploy popularized the model.

## Details
- Execution model: JavaScript/TypeScript (V8 isolates or similar) running per request at the edge; WebAssembly supported for compute-heavy paths.
- Use cases: geolocation routing, A/B split, header rewriting, JWT verification, form validation, and fetching/stitching backend APIs.
- Limits: CPU time, memory, and bundle size caps (typically < 1-10MB); no long-running processes or local disk.
- Caching integration: functions set `Cache-Control` and cache APIs, combining [[wiki/api-protocols/http-caching|HTTP caching]] with dynamic behavior.
- Security: edge auth checks run before requests hit origin, protecting static sites and APIs alike.
- Worked example: a cosmos edge function could rewrite `/cosmos/` requests to the latest dashboard build or inject a version header, while a static GitHub Pages origin stays untouched.
- Comparison: [[wiki/frontend/serverless|serverless]] functions run in regions with more resources; edge functions trade capacity for proximity.

## Related
- [[wiki/frontend/serverless|Serverless]] — regional compute alternative
- [[wiki/frontend/static-site-generation|Static Site Generation]] — static origin, dynamic edge
- [[wiki/devops-infra/cloudflare|Cloudflare]] — Workers platform for edge logic
- [[wiki/frontend/vercel|Vercel]] — edge functions on the Vercel network
- [[wiki/api-protocols/http-caching|HTTP Caching]] — edge caching behavior
- [[wiki/security/jwt|JWT]] — token verification at the edge
- [[wiki/concepts/triad-architecture|Triad Architecture]] — dashboard delivery path
- [[wiki/ops/gap-report|Gap Analysis Report]] — delivery-path gaps noted
