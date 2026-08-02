---
type: "concept"
title: "Hot Module Replacement"
description: "Updating modules without full page reloads"
tags: [hmr", "dev-server", "tooling", "vite", "webpack"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://webpack.js.org/concepts/hot-module-replacement/", "https://vitejs.dev/guide/features.html#hot-module-replacement"]
---

# Hot Module Replacement

## Summary
Hot Module Replacement (HMR) swaps changed modules in a running app without a full page reload, preserving state like form input and scroll position. The dev server pushes updates through the module graph; modules declare acceptance boundaries. CSS and template changes apply instantly, while JavaScript updates re-execute only the affected modules.

## Details
- Mechanism: the dev server detects a change, sends the updated module over a WebSocket, and the runtime re-executes it.
- Accept boundaries: module.hot.accept declares what a module can update in place; unmatched changes fall back to a full reload.
- Framework plugins: React Fast Refresh, Vue HMR, and Svelte HMR preserve component state while re-rendering changed components.
- CSS HMR: stylesheet changes replace rules without touching the DOM state.
- State caveats: module-level state resets on update; components must tolerate remounts when boundaries shift.
- Production: HMR is a development-only feature — production bundles are immutable.

## Related
- [[wiki/frontend/dev-server|Dev Server]] — the host of HMR
- [[wiki/frontend/vite|Vite]] — HMR built on native ESM
- [[wiki/frontend/webpack-concepts|Webpack Concepts]] — webpack's HMR model
- [[wiki/frontend/module-bundlers|Module Bundlers]] — the module graph HMR updates
- [[wiki/frontend/es-modules|ES Modules]] — module semantics underneath
- [[wiki/frontend-frameworks/hot-reload|Hot Reload]] — the broader reload family
