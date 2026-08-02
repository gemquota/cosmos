---
type: "concept"
title: "Dev Server"
description: "Local serving, proxies, and fast reload"
tags: [dev-server", "tooling", "vite", "webpack", "development"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://vitejs.dev/guide/features.html", "https://webpack.js.org/configuration/dev-server/"]
---

# Dev Server

## Summary
A dev server serves the application locally during development with instant rebuilds, hot module replacement, source maps, and API proxying. Vite's dev server works over native ES modules with esbuild transforms; webpack-dev-server bundles on demand. The dev server simulates production behavior closely enough to iterate, without matching it exactly.

## Details
- Serving: static files and transformed modules are served over HTTP with correct MIME types and module semantics.
- Rebuilds: change detection triggers incremental transforms — near-instant in Vite, configurable in webpack.
- Proxies: /api routes forward to backend servers, avoiding CORS during development; headers and rewrite rules configure targets.
- HTTPS: local TLS certificates (self-signed or mkcert) enable service workers and secure-cookie testing.
- Source maps: dev mode maps transformed code to source for readable debugging.
- Production gap: dev servers skip minification and some optimizations; always validate the production build separately.

## Related
- [[wiki/frontend/hot-module-replacement|Hot Module Replacement]] — the fast-update layer
- [[wiki/frontend/vite|Vite]] — the modern dev server
- [[wiki/frontend/webpack-concepts|Webpack Concepts]] — webpack-dev-server configuration
- [[wiki/frontend/source-maps|Source Maps]] — dev-mode debugging
- [[wiki/frontend/end-to-end-testing|End-to-End Testing]] — testing against the served app
- [[wiki/api-protocols/rest-apis|REST APIs]] — proxied backend targets
