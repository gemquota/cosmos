---
type: "entity"
title: "Next 2"
---

# Next 2

## Summary

Next.js is a React framework that adds file-based routing, server-side rendering, static site generation, and API routes to React applications. It matters because it turns a component library into a full-stack application platform with unified deployment. Its conventions — the pages and app routers, server components, and build-time data loading — shape how modern web apps are structured.

## Details

- **Definition** — Next.js builds on React with a file-system router, hybrid rendering strategies, and first-class deployment targets.
- **Rendering modes** — Pages can be statically generated at build time, server-rendered per request, or hydrated as client components, mixable within one app.
- **Routing** — Files in the pages or app directory map to URLs; dynamic segments, layouts, and route groups express complex navigation hierarchies.
- **API routes** — Server-side route handlers and API routes let one codebase serve backend logic without a separate service.
- **Data fetching** — Server components fetch near the data, reducing client round trips; caching and revalidation policies control freshness.
- **Worked example** — A marketing page is statically generated at build, a dashboard route server-renders per user, and an API route proxies a legacy backend.
- **Common failure modes** — Accidental client-side data fetching, hydration mismatches from nondeterministic rendering, and stale caches are frequent issues.
- **Practical relevance** — Next.js dominates modern React deployments, so its conventions appear throughout frontend and API telemetry.
- **Telemetry note** — The stub body already describes Next.js accurately; this note preserves that definition under the session that recorded it.
- **Deployment** — Next.js apps deploy to Node servers, edge runtimes, or static hosts; the rendering modes chosen determine which targets are viable.
- **Performance** — Image optimization, incremental static regeneration, and streaming responses are built-in levers for perceived speed.
- **Worked example** — A storefront statically renders product pages, revalidates them on a schedule, and server-renders the cart for each signed-in user.

## Related

- [[wiki/frontend/localization|Localization]] — i18n routing in Next.js
- [[wiki/api-protocols/rest-api-design|REST API Design]] — designing its API routes
- [[wiki/api-services/categories/api-rest/subcategories/rest-http/frontend-logic|Frontend Logic]] — client vs server behavior
- [[wiki/web-platforms/browser-rendering-pipeline|Browser Rendering Pipeline]] — hydration and rendering
- [[wiki/api-services/categories/api-rest/subcategories/rest-http/flip|FLIP]] — animating Next.js UI
- [[wiki/concepts/concept-formation|Concept Formation]] — framework concepts as categories
