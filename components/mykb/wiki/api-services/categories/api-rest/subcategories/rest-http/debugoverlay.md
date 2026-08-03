---
type: "entity"
title: "DebugOverlay"
description: "An on-screen overlay that exposes debug information during development"
tags: ["entity", "debugging", "overlay", "frontend", "tooling"]
timestamp: "2026-07-19T22:41:41Z"
resource: ""
---

# DebugOverlay

## Summary

A debug overlay is an on-screen panel that surfaces runtime information — state, layout bounds, network calls, or performance metrics — while an app is being developed. It matters because it shows what is happening in context, without switching tools or adding log statements. Overlays are a standard fixture of browser devtools and mobile debug builds.

## Details

- **Definition** — DebugOverlay renders diagnostic data over the live UI: coordinates, element trees, network activity, or custom state inspectors.
- **Why it helps** — Seeing state next to the pixels that depend on it speeds up diagnosis of layout, styling, and data-flow bugs.
- **Implementation** — Overlays are separate layers — DOM or native views — that observe app state and redraw without disturbing the app's own rendering.
- **Worked example** — A mobile debug build shows a draggable FPS graph and touch coordinates; toggling a flag surfaces the current navigation stack.
- **Common failure modes** — Overlays intercepting input, leaking into release builds, and showing stale state when they do not subscribe to updates.
- **Practical relevance** — Release builds should exclude overlays by build flag, both for performance and to avoid exposing internals to users.
- **Variants** — DOM-inspector overlays, network panels, and accessibility tree viewers each expose a different slice of runtime truth.
- **Telemetry note** — Recorded in API and cloud sessions with a Go tag, consistent with CLI and web debugging tools surfaced as overlays.
- **Build gating** — Feature flags or build flavors control overlay presence so debug code never ships to production builds.
- **Data sources** — Overlays subscribe to stores, profilers, or log buffers; the subscription design determines whether the overlay shows truth or a snapshot.
- **Worked example** — A web debug overlay highlights element bounds on hover and prints the component's props and state beside it for instant inspection.

## Related

- [[wiki/dev-tools/debuggers|Debuggers]] — the deeper inspection tools
- [[wiki/dev-tools/debug-logging|Debug Logging]] — log-based diagnosis
- [[wiki/api-services/categories/api-rest/subcategories/rest-http/mockcanvas|MockCanvas]] — stubbing drawing in tests
- [[wiki/web-platforms/browser-rendering-pipeline|Browser Rendering Pipeline]] — what overlays visualize
- [[wiki/api-services/categories/api-rest/subcategories/rest-http/frontend-logic|Frontend Logic]] — state the overlay exposes
- [[wiki/testing/characterization-testing|Characterization Testing]] — locking in observed behavior
