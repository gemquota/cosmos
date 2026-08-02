---
type: "concept"
title: "Solid.js Signals"
description: "Fine-grained reactivity: signals, memos, and effects with no virtual DOM"
tags: ["solid", "signals", "reactivity", "frontend", "javascript"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://www.solidjs.com/", "https://www.solidjs.com/docs/latest/api#createsignal"]
---
# Solid.js Signals

## Summary
Solid.js builds UIs from fine-grained reactivity: signals hold state, memos derive values, and effects run side effects only when dependencies change. Components execute once; the compiled DOM updates react to signal reads directly, with no re-render of whole trees.

## Details
- **Signals** — `createSignal` returns a getter/setter pair; reads inside effects and memos subscribe automatically.
- **Memos and effects** — derived values cache with `createMemo`; `createEffect` reacts to tracked reads.
- **Ownership and cleanup** — `onCleanup` runs when owners dispose, making resource management deterministic.
- **Compared with React** — no reconciliation or re-render cycles; updates are surgical, but the mental model differs from hooks.
- **Worked example** — a live telemetry panel in Solid updates only the value nodes that changed, staying smooth on low-end devices.
- **Relevance** — the signals model informs RSIS3's UI reactivity and its data-flow documentation.
- **Fine-grained batching** — signal writes batch effects into one update cycle, and `batch()` groups multiple writes; the pattern keeps derived DOM updates minimal without manual memoization.

## Related
- [[wiki/frontend-frameworks/signal-based-state|Signal-Based State]] — adjacent concept in this wiki
- [[wiki/frontend-frameworks/observable-pattern|Observable Pattern]] — adjacent concept in this wiki
- [[wiki/frontend-frameworks/rxjs-practice|RxJS in Practice]] — adjacent concept in this wiki
- [[wiki/frontend-frameworks/angular-signals|Angular Signals]] — adjacent concept in this wiki
- [[wiki/frontend-frameworks/declarative-ui|Declarative UI]] — existing coverage
- [[wiki/web-platforms/state-management|State Management]] — existing coverage
- [[wiki/web-platforms/web-frameworks|Web Frameworks]] — existing coverage
