---
type: "concept"
title: "Hydration Strategies"
description: "Making server-rendered HTML interactive: full, partial, islands, and streaming hydration"
tags: ["hydration", "ssr", "performance", "frameworks", "frontend"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://react.dev/reference/react-dom/client/hydrateRoot", "https://docs.astro.build/en/concepts/islands/"]
---
# Hydration Strategies

## Summary
Hydration attaches client-side interactivity to server-rendered HTML. Full hydration re-runs the whole app on the client; partial and islands strategies hydrate only interactive regions; progressive hydration defers non-critical parts. Choosing a strategy trades first-paint speed against interactivity complexity.

## Details
- **Full hydration** — the server sends HTML; the client renders the same tree and attaches listeners; mismatch between server and client HTML breaks it.
- **Islands** — only interactive components hydrate (Astro, Fresh); static HTML ships without JS, cutting payload and main-thread work.
- **Progressive and selective** — React's selective hydration starts with user-interacting parts; streaming lets HTML arrive before the full app renders.
- **Trade-offs** — faster loads versus server costs and duplicate rendering; resumability (Qwik) avoids re-running the app entirely.
- **Worked example** — a wiki reader could server-render article bodies and hydrate only search and theme toggles.
- **Relevance** — RSIS3's reports are mostly static knowledge; islands-style hydration keeps them fast on low-end devices.

## Related
- [[wiki/frontend-frameworks/suspense-practice|Suspense in Practice]] — adjacent concept in this wiki
- [[wiki/frontend-frameworks/concurrent-rendering|Concurrent Rendering]] — adjacent concept in this wiki
- [[wiki/frontend-frameworks/starttransition|startTransition]] — adjacent concept in this wiki
- [[wiki/js-ts-ecosystem/dynamic-import|Dynamic Import]] — adjacent concept in this wiki
- [[wiki/web-platforms/web-frameworks|Web Frameworks]] — existing coverage
- [[wiki/frontend-frameworks/declarative-ui|Declarative UI]] — existing coverage
- [[wiki/frontend-frameworks/hot-reload|Hot Reload]] — existing coverage
