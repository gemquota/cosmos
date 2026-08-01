---
type: "concept"
title: "Static Site Generation"
description: "Pre-rendering pages at build time into static HTML, CSS, and JS served from any CDN"
tags: ["ssg", "frontend", "jamstack", "hosting", "performance"]
timestamp: "2026-07-31T00:00:00Z"
status: "growing"
source: ["https://nextjs.org/docs/app/building-your-application/rendering"]
---

# Static Site Generation

## Summary
Static Site Generation (SSG) renders pages to plain HTML at build time rather than per request. The output — HTML, CSS, JavaScript, and assets — is served from object storage or a CDN with no application server, giving extreme performance, security, and scale. Frameworks like Next.js, Astro, and Eleventy generate static exports; the cosmos dashboard is hosted exactly this way on GitHub Pages.

## Details
- Build-time rendering: data is fetched during the build, so runtime has zero data-fetch latency; incremental builds (ISR) re-render changed pages on schedule.
- Hosting: static files work anywhere — GitHub Pages, Netlify, Vercel, S3, Cloudflare; no servers to patch or scale.
- Performance: CDN caching at the edge, no origin round trips; perfect Lighthouse scores are achievable.
- Trade-offs: content changes require a rebuild (or ISR/webhook-triggered regeneration); highly personalized pages need client-side rendering or edge functions.
- Hybrid models: Next.js blends SSG, server-side rendering, and client components per page; Astro ships zero JS by default.
- Worked example: the unified dashboard's `index.html` (Tailwind + Chart.js) is static; regenerating it from `data.json` on each RSIS3 pulse would keep the deployed hub fresh without a server.

## Related
- [[wiki/frontend/edge-functions|Edge Functions]] — dynamic behavior at the CDN edge
- [[wiki/frontend/serverless|Serverless]] — on-demand compute alternative
- [[wiki/frontend/vercel|Vercel]] — SSG-first hosting platform
- [[wiki/frontend/netlify|Netlify]] — build-and-host SSG pipelines
- [[wiki/api-protocols/http-caching|HTTP Caching]] — static assets are trivially cacheable
- [[wiki/concepts/mykb-implementation-report|Mykb Implementation Report]] — dashboard deployment notes
- [[wiki/ops/gap-report|Gap Analysis Report]] — static regeneration gaps
