---
type: "entity"
title: "Vite"
resource: ""
---
description: "The modern build tool and dev server for web applications"
tags: ["entity", "android", "api", "ast", "auth", "authentication", "build-tools", "frontend"]
timestamp: "2026-07-19T22:41:42Z"

# Vite

## Summary
Vite is a build tool and development server for web applications, known for fast startup and instant hot module replacement. It matters because slow build tooling wastes developer time at every edit. Vite's approach, native ES modules in development and optimized bundling for production, made it a default choice for new projects.

## Details
- **Definition** — Vite serves source modules natively in development and produces optimized bundles for production using Rollup.
- **Dev server** — browsers load ES modules directly, so startup is nearly instant and edits update without full rebuilds.
- **Hot module replacement** — changed modules are swapped in place, preserving application state during development.
- **Pre-bundling** — dependencies are pre-bundled with esbuild, reducing the number of module requests the browser must make.
- **Production build** — a Rollup-based build applies tree-shaking, minification, and asset optimization.
- **Framework support** — React, Vue, Svelte, and others are supported through official plugins and templates.
- **Configuration** — a Vite config file controls plugins, aliases, and build options, and it is itself an ES module.
- **Common failure modes** — dependency versions that break pre-bundling caches, and dev-only behavior that differs from the production build.
- **Worked example** — a team scaffolds a project, develops with instant reloads, and ships a production build whose assets are hashed and cached.
- **Practical relevance** — Vite's developer experience and build performance made it a mainstream standard for frontend tooling.

- **Plugin system** — Vite's plugin hooks cover dev serving and build transforms, mirroring the Rollup plugin API.
- **Assets** — static assets are imported as URLs and hashed in production builds for cache-friendly output.
- **Troubleshooting** — clearing the dependency cache and restarting the server resolves most stale-state dev issues.
## Related
- [[wiki/js-ts-ecosystem/vite-practice|Vite Practice]] — usage patterns
- [[wiki/frontend/vite|Vite]] — tool notes
- [[wiki/js-ts-ecosystem/bundlers-and-build-tools|Bundlers and Build Tools]] — the landscape
- [[wiki/js-ts-ecosystem/esbuild-practice|esbuild Practice]] — dependency pre-bundling
- [[wiki/js-ts-ecosystem/rollup-practice|Rollup Practice]] — production builds
- [[wiki/js-ts-ecosystem/commonjs-vs-esm|CommonJS vs ESM]] — module formats
