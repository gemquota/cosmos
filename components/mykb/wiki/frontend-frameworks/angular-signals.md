---
type: "concept"
title: "Angular Signals"
description: "Granular reactivity primitives in Angular"
tags: ["angular", "signals", "reactivity", "frontend"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# Angular Signals

## Summary
Angular Signals are the framework's granular reactivity primitives: a `signal()` holds a value, `computed()` derives values reactively, and `effect()` runs side effects when dependencies change. They give Angular fine-grained, synchronous updates that can bypass zone-based change detection, and they are reshaping the framework's idioms around state, inputs, and templates.

## Details
- Mechanism: a signal is a getter plus internal dependency tracking. Reading a signal inside `computed` or `effect` registers a dependency; when the signal is written with `set`, `update`, or `mutate`, the framework marks dependent computations dirty and re-evaluates them lazily and synchronously. This is a pull-based reactive graph: computations recompute only when read and only when a dependency actually changed, which avoids the full-tree change detection passes that the zone-driven model performs.
- Concrete examples: a counter component stores `count = signal(0)` and the template reads `count()` so only that binding updates on click; a derived value `double = computed(() => count() * 2)` caches its result until `count` changes; an `effect` persists a value to localStorage whenever it changes. Angular 17+ lets signals drive component inputs (`input()`), model two-way bindings, and even render in a signal-based change detection mode, so a form field with a signal input no longer needs `ChangeDetectorRef` gymnastics.
- Failure modes: the classic pitfalls are reading a signal outside a reactive context (you get a snapshot, not a subscription), writing to a signal inside an effect that also reads it (feedback loops and "ExpressionChangedAfterItHasBeenChecked" style surprises), and over-eager `mutate` on arrays or objects where identity changes are expected by downstream memoization. Interop with zone-based code can also double-update, and async effects need careful cleanup to avoid writing to destroyed components.
- Operational tradeoffs: signals trade a mental-model shift (reactivity is now explicit) for a real performance and clarity win: fewer change-detection passes, simpler state flow, and a clear dependency graph that tools can visualize. The migration cost is real — existing components that rely on `ngZone`, `async` pipes, and `OnPush` conventions need rework, and mixing signal and non-signal state is a common source of subtle staleness bugs.
- RSIS3/mykb relevance: signal-based state is a concrete instance of the declarative, derived-state discipline MyKB uses in its UI: define the source of truth once, derive everything else, and let the framework propagate invalidation — the same dependency-graph reasoning RSIS3 applies to loop state.

## Related
- [[wiki/frontend-frameworks/solid-js-signals|Solid.js Signals]]
- [[wiki/frontend-frameworks/ng-zone|NgZone]]
- [[wiki/frontend-frameworks/change-detection|Change Detection]]
- [[wiki/frontend-frameworks/signal-based-state|Signal-Based State]]
- [[wiki/frontend-frameworks/declarative-ui|Declarative UI]]
- [[wiki/web-platforms/state-management|State Management]]
- [[wiki/web-platforms/web-frameworks|Web Frameworks]]
