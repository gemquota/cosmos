---
type: "concept"
title: "Streaming Rendering"
description: "Sending HTML in chunks as data becomes ready, so first paint happens before the whole page renders"
tags: ["streaming", "ssr", "performance", "rendering", "web"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://nextjs.org/docs/app/building-your-application/rendering", "https://react.dev/reference/react/Suspense"]
---
# Streaming Rendering

## Summary
Streaming rendering sends HTML progressively instead of waiting for the full page. The server flushes shells and placeholders immediately, then streams in content as data resolves. Users see and interact with the page earlier, and slow regions no longer block the whole response.

## Details
- **Mechanics** — HTTP chunked transfer or Web Streams carry partial HTML; browsers parse and paint as chunks arrive.
- **Suspense boundaries** — framework-level fallbacks mark where streaming pauses; resolved boundaries flush their content in order.
- **Benefits** — faster TTFB and LCP, perceived performance, and graceful degradation when a slow data source lags.
- **Costs** — server hold time, duplicated rendering between server and client, and SEO/crawl considerations for streamed content.
- **Worked example** — the mykb dashboard streams the shell and header immediately, then article lists and pulse charts as queries return.
- **Relevance** — RSIS3's report generation can stream sections to readers while later sections still compute.

## Related
- [[wiki/frontend-frameworks/suspense-practice|Suspense in Practice]] — adjacent concept in this wiki
- [[wiki/js-ts-ecosystem/dynamic-import|Dynamic Import]] — adjacent concept in this wiki
- [[wiki/web-platforms/render-blocking|Render Blocking]] — adjacent concept in this wiki
- [[wiki/web-platforms/content-visibility|content-visibility CSS]] — adjacent concept in this wiki
- [[wiki/web-platforms/web-performance-optimization|Web Performance Optimization]] — existing coverage
- [[wiki/web-platforms/progressive-web-apps|Progressive Web Apps]] — existing coverage
- [[wiki/web-platforms/web-standards|Web Standards]] — existing coverage
