---
type: "concept"
title: "Signal-Based State"
description: "Fine-grained reactive cells that notify only their subscribers"
tags: ["signals", "state", "reactivity", "frontend"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# Signal-Based State

## Summary
Signal-based state is a model where state lives in fine-grained reactive cells — `signal(0)`, `computed(...)`, `effect(...)` — and updates propagate only to the computations and bindings that actually read the changed cell. Adopted by Solid, Preact, Angular, Vue (via `ref`/`computed`), and Qwik, signals deliver the precision of dependency tracking without the overhead of tree diffing or zone patching.

## Details
- Mechanism: a signal holds a value plus a list of subscribers; reading it inside a computed, effect, or render registers the reader as a dependent; writing it marks those dependents dirty and schedules re-execution. Computeds cache and recompute lazily — only when read and only when a dependency changed. Because tracking happens at read time, granularity is per-binding: a Solid component updating one text node does not re-run the whole component, let alone the tree. Framework bindings then map signals to DOM updates (or to component re-renders in Angular's signal-based mode), with the virtual DOM diff often skipped entirely.
- Concrete examples: a counter where only the displayed number re-renders; a derived `double = computed(() => count() * 2)` that recomputes once per count change regardless of how many components read it; an `effect` that persists to localStorage only when its tracked inputs change; Angular's `input()`/`output()` signals replacing `@Input`/`@Output` ceremony with explicit reactive plumbing; Vue's `ref`/`computed` powering the same model inside `setup()`.
- Failure modes: the classic pitfalls are reading signals outside reactive contexts (a snapshot, not a subscription — the UI silently goes stale), writing signals inside derived computeds (feedback loops and spurious invalidations), and losing tracking through destructuring or passing raw values. Interop is the second front: bridging signals to observables, props from non-signal parents, or imperative libraries can double-update or miss updates; and teams new to the model over-subscribe by reading whole objects instead of fields.
- Operational tradeoffs: signals trade a mental-model shift for measurable wins: no full-tree re-renders, no diffing, precise invalidation, and simpler reasoning about which updates happen. The costs are framework-specific APIs (no universal signal standard, though TC39 is exploring one), tooling that still lags (profilers attribute fine-grained updates differently), and migration effort in frameworks where the old model (zones, virtual DOM) is entrenched. The design question they raise — whether signals make virtual DOM diffing obsolete — answers differently per framework: Solid skipped the VDOM; React keeps it but adds compiler-driven memoization; Angular is moving to signals by default.
- RSIS3/mykb relevance: signals are dependency-tracked invalidation, the same primitive RSIS3 uses to decide which derived metrics and checkpoints must refresh when a registry entry changes — a shared conceptual foundation between the dashboard's UI and the loop's state engine.

## Related
- [[wiki/frontend-frameworks/solid-js-signals|Solid.js Signals]]
- [[wiki/frontend-frameworks/observable-pattern|Observable Pattern]]
- [[wiki/frontend-frameworks/rxjs-practice|RxJS in Practice]]
- [[wiki/frontend-frameworks/angular-signals|Angular Signals]]
- [[wiki/frontend-frameworks/declarative-ui|Declarative UI]]
- [[wiki/web-platforms/state-management|State Management]]
- [[wiki/web-platforms/web-frameworks|Web Frameworks]]
