---
type: "concept"
title: "Client-Side Rendering (CSR)"
description: "Rendering pages in the browser from JavaScript, with SEO and first-load tradeoffs"
tags: [rendering", "spa", "javascript", "performance", "seo"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://web.dev/articles/rendering-on-the-web", "https://developer.mozilla.org/en-US/docs/Glossary/SPA"]
---

# Client-Side Rendering (CSR)

## Summary
Client-side rendering builds the page in the browser: the server returns a minimal HTML shell plus a JavaScript bundle, and the script fetches data, renders UI, and attaches behavior after load. Single-page-application frameworks such as React, Vue, and Svelte use this model by default. CSR shines after the first load, because subsequent navigations reuse the running app and exchange only data.

## Details
- Bootstrap flow: empty root node, bundle execution, data fetching, then first paint; users see a blank or loading state until JS runs.
- Metrics: Time to First Byte is fast, but Largest Contentful Paint depends on bundle download, parsing, and API latency.
- SEO cost: crawlers execute JS today, but critical content can be missed on slow networks; SSR, SSG, or prerendering fixes this.
- Bundle weight is the main lever; code splitting and route-level lazy loading keep initial payloads small.
- No hydration step is needed because the DOM is created client-side, which simplifies some race conditions.
- Fit: authenticated dashboards, tools, and highly interactive apps where first-load freshness matters less than app feel.

## Related
- [[wiki/frontend/server-side-rendering|Server-Side Rendering]] — server pre-renders HTML for faster first load
- [[wiki/frontend/hydration|Hydration]] — attaching interactivity to pre-rendered HTML
- [[wiki/frontend/core-web-vitals|Core Web Vitals]] — metrics CSR must manage
- [[wiki/frontend/virtual-dom|Virtual DOM]] — the in-memory UI model frameworks use
- [[wiki/frontend/code-splitting|Code Splitting]] — keeping the CSR bootstrap bundle small
- [[wiki/web-platforms/web-frameworks|Web Frameworks]] — ecosystem context for CSR apps
