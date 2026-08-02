---
type: "concept"
title: "Minification"
description: "Removing whitespace and renaming to shrink payloads"
tags: [minification", "performance", "javascript", "css", "build-tools"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://developer.mozilla.org/en-US/docs/Glossary/Minification", "https://terser.org/"]
---

# Minification

## Summary
Minification reduces file size by stripping whitespace, comments, and long identifiers, and by rewriting code to shorter forms. Terser is the standard JavaScript minifier, while CSS tools like cssnano and Lightning CSS handle stylesheets. Combined with compression, minification typically cuts payloads by half or more.

## Details
- What it removes: whitespace, comments, newlines, unused code branches, and redundant syntax such as semicolons.
- Name mangling: local variables and functions shorten to one or two characters; careful mangling preserves behavior.
- Dead code: minifiers drop unreachable branches and constant-fold expressions, complementing bundler tree shaking.
- Output trade-offs: minified code is unreadable, which is what source maps restore for debugging.
- Compression interplay: gzip and brotli compress minified output further; measure gzip size, not raw bytes.
- HTML and assets: HTML minifiers and image/asset tools round out the pipeline; always keep a source-map sidecar.

## Related
- [[wiki/frontend/tree-shaking|Tree Shaking]] — removes unused exports before minifying
- [[wiki/frontend/source-maps|Source Maps]] — restoring readability of minified output
- [[wiki/frontend/module-bundlers|Module Bundlers]] — where minification runs
- [[wiki/frontend/performance-budgets|Performance Budgets]] — the weight limits involved
- [[wiki/frontend/transpilation|Transpilation]] — the stage before minification
- [[wiki/frontend/browser-caching|Browser Caching]] — hashed minified filenames
