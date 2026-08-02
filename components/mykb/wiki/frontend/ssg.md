---
type: "concept"
title: "Static Site Generation (SSG)"
description: "Build-time HTML pre-rendering and when it fits"
tags: [ssg", "rendering", "static-sites", "performance", "jamstack"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://nextjs.org/docs/app/building-your-application/rendering", "https://www.11ty.dev/docs/"]
---

# Static Site Generation (SSG)

## Summary
Static site generation renders pages to plain HTML, CSS, and JavaScript at build time. The output is deployable anywhere a file can be served — object storage, GitHub Pages, or any CDN — with no application server and no per-request rendering cost. It suits content that changes on deploy cadence rather than per visitor.

## Details
- Build-time data: content and API data are fetched during the build and baked into the output, so runtime has zero data latency.
- Hosting is trivial: static files are cacheable, scalable, and immune to most server-side outages and patching duties.
- Performance ceiling: CDN-cached files make excellent Core Web Vitals scores routine rather than heroic.
- Trade-offs: every content change requires a rebuild (or scheduled/on-demand regeneration), and per-user personalization needs a runtime layer.
- Ecosystem: Next.js, Astro, Eleventy, and Hugo all produce static exports; Astro even ships zero JavaScript by default.
- The cosmos dashboard is itself static: Tailwind plus Chart.js served from GitHub Pages, regenerated from JSON telemetry.

## Related
- [[wiki/frontend/static-site-generation|Static Site Generation]] — hub deployment notes for the same pattern
- [[wiki/frontend/incremental-static-regeneration|Incremental Static Regeneration]] — adding freshness to static output
- [[wiki/frontend/edge-rendering|Edge Rendering]] — dynamic behavior beside static files
- [[wiki/cloud-infra/content-delivery-networks|Content Delivery Networks]] — where static files live
- [[wiki/frontend/netlify|Netlify]] — build-and-host platform for SSG
- [[wiki/frontend/vercel|Vercel]] — SSG-first hosting with ISR support
