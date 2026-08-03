---
type: "concept"
title: "Change Detection"
description: "How frameworks discover and apply state updates to the DOM"
tags: ["change-detection", "frameworks", "reactivity", "frontend"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# Change Detection

## Summary
Change detection is the mechanism by which a UI framework discovers that state changed and applies those changes to the DOM. Frameworks sit on a spectrum: React diffs a virtual tree on every render pass, Angular historically walked component trees with zone-driven dirty checks, and signal-based systems track dependencies so precisely that only the affected bindings update.

## Details
- Mechanism: the spectrum is about granularity and timing. React re-renders a component (and by default its children) when state or props change, producing a new virtual DOM that is diffed against the previous one to compute minimal DOM mutations. Angular's default mode uses zone.js to detect any async activity, then runs change detection over the component tree comparing bindings, with `OnPush` restricting checks to components whose inputs changed. Signal-based systems (Angular signals, Solid, Preact signals) maintain a dependency graph: a write marks only the computations that read it, and the DOM update is targeted to those bindings.
- Concrete examples: a large React list where one item toggles causes the whole list component to re-render unless items are memoized (`React.memo`) or state is colocated; an Angular page with many components runs a full tree pass after any timer tick unless `OnPush` is used; a Solid counter updates exactly the text node it owns while the rest of the page is untouched — the difference is visible in profilers as "renders" versus "component checks" versus "dependency invalidations".
- Failure modes: the common failures are stale closures and memoization bugs (React), missed change detection when state mutates outside the framework's knowledge (Angular's zone can miss `requestAnimationFrame` and native APIs), and over-broad invalidation that makes "optimized" code slower than a naive tree diff. Debugging is the hidden cost: stack traces and profiler views differ wildly per granularity model, and teams often fight their framework's model instead of designing state to match it.
- Operational tradeoffs: fine-grained reactivity wins on runtime cost and predictability but raises the bar for correctness (every dependency must be tracked, including non-reactive data like arrays passed by reference); tree-diffing is forgiving and simple to reason about but pays a per-render cost and invites memoization complexity as apps grow. The industry trend is compile-time or fine-grained detection (Svelte, Solid, Angular signals), where the compiler generates direct DOM updates instead of diffing.
- RSIS3/mykb relevance: change detection is the UI counterpart of RSIS3's dependency tracking: knowing what to invalidate when state changes is the same problem as knowing which loop outputs depend on which registry entries, and fine-grained invalidation is the discipline MyKB's graph views rely on.

## Related
- [[wiki/frontend-frameworks/solid-js-signals|Solid.js Signals]]
- [[wiki/frontend-frameworks/signal-based-state|Signal-Based State]]
- [[wiki/frontend-frameworks/observable-pattern|Observable Pattern]]
- [[wiki/frontend-frameworks/rxjs-practice|RxJS in Practice]]
- [[wiki/frontend-frameworks/declarative-ui|Declarative UI]]
- [[wiki/web-platforms/state-management|State Management]]
- [[wiki/web-platforms/web-frameworks|Web Frameworks]]
