---
type: "concept"
title: "Source Maps"
description: "Mapping bundled and minified output back to source"
tags: [source-maps", "debugging", "build-tools", "javascript", "tooling"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://developer.mozilla.org/en-US/docs/Glossary/Source_map", "https://webpack.js.org/configuration/devtool/"]
---

# Source Maps

## Summary
Source maps link minified or transpiled output back to the original source, so stack traces and debugger breakpoints show readable code. The bundler emits a .map file containing mappings, sources, and optionally sourcesContent. DevTools consume them automatically when the file is served or discovered.

## Details
- Format: a JSON file with version, sources, names, and base64-VLQ encoded mappings between generated and original positions.
- Devtools: browsers fetch the map via the //# sourceMappingURL comment and reconstruct original files in the debugger.
- Devtool modes: webpack and Vite offer eval, source-map, inline-source-map, and hidden variants trading build speed for fidelity.
- Production: maps aid incident debugging but expose source — serve them privately or strip sourcesContent.
- Security: source maps can leak internal code; gate access for authenticated support tooling.
- Framework support: frameworks generate maps for JSX/TS and CSS-in-JS; some tools support style maps for stylesheet debugging.

## Related
- [[wiki/frontend/minification|Minification]] — the transform maps compensate for
- [[wiki/frontend/module-bundlers|Module Bundlers]] — the tools that emit maps
- [[wiki/frontend/dev-server|Dev Server]] — dev-mode source mapping
- [[wiki/frontend/transpilation|Transpilation]] — compiled output mapped to source
- [[wiki/frontend/webpack-concepts|Webpack Concepts]] — devtool configuration
- [[wiki/dev-tools/debuggers|Debuggers]] — consumers of source maps
