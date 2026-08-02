---
type: "concept"
title: "CSS Modules"
description: "Build-time scoped class names for local styling"
tags: [css", "css-modules", "build-tools", "styling", "scoping"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://github.com/css-modules/css-modules", "https://vitejs.dev/guide/features.html#css-modules"]
---

# CSS Modules

## Summary
CSS Modules scope styles per file at build time: class names in a stylesheet become locally unique hashes, so the same class name in two components never collides. They give teams the mental model of plain CSS with component-local guarantees and zero runtime cost.

## Details
- Mechanics: the bundler transforms .module.css files, rewriting selectors to names like _title_hash and exporting a mapping object.
- Local by default: every class and animation name is scoped unless marked :global(); composition across files uses composes.
- Interop: React and Vue access styles as an object — styles.title — and TypeScript types can be generated for autocomplete.
- Zero runtime: unlike CSS-in-JS, there is no JavaScript executing to inject styles; output is plain linked CSS.
- Tooling: supported natively by Vite, webpack via css-loader, and frameworks from Next.js to Svelte.
- Trade-offs: dynamic class application is manual, and highly themeable components need custom properties or global tokens.

## Related
- [[wiki/frontend/css-in-js|CSS-in-JS]] — the runtime alternative
- [[wiki/frontend/utility-css|Utility-First CSS]] — the composition alternative
- [[wiki/frontend/bem|BEM]] — naming convention solving collisions manually
- [[wiki/frontend/module-bundlers|Module Bundlers]] — where the transformation runs
- [[wiki/frontend/vite|Vite]] — first-class CSS Modules support
- [[wiki/js-ts-ecosystem/entities/typescript-patterns|TypeScript Patterns]] — typed style objects
