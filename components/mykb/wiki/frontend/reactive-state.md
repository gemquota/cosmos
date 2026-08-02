---
type: "concept"
title: "Reactive State"
description: "Observables and signals as reactivity primitives"
tags: [reactivity", "signals", "observables", "state", "javascript"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://vuejs.org/guide/extras/reactivity-in-depth.html", "https://solidjs.com/docs/latest/api"]
---

# Reactive State

## Summary
Reactive state is state that automatically tracks its own dependencies and re-runs effects when values change. Signals and observables are the two main primitives: signals hold a value with read/write functions that record subscribers, while observables stream values over time. Frameworks like Solid, Vue, Svelte, and Angular build UI updates on this model.

## Details
- Signals: reading inside an effect subscribes it; writing notifies subscribers, enabling fine-grained updates with no diffing.
- Derived values: computed signals memoize transformations, recomputing lazily only when dependencies change.
- Effects: effects run on dependency change — the basis for DOM updates, logging, and side-effect coordination.
- Observables: RxJS models streams with operators; signals are pull-based, observables are push-based.
- Framework integration: Angular switched to signals, Vue's refs are signals, and Preact and React are experimenting.
- Performance: fine-grained reactivity avoids whole-tree re-renders, competing with virtual-DOM reconciliation.

## Related
- [[wiki/frontend/state-management-patterns|State Management Patterns]] — where reactive state fits
- [[wiki/frontend/unidirectional-data-flow|Unidirectional Data Flow]] — the state change discipline
- [[wiki/frontend/virtual-dom|Virtual DOM]] — the reconciliation alternative
- [[wiki/web-platforms/state-management|State Management]] — platform notes
- [[wiki/frontend/component-composition|Component Composition]] — reactive components
- [[wiki/software-engineering/reactive-programming|Reactive Programming]] — the broader paradigm
