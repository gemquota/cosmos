---
type: "concept"
title: "Selector Libraries"
description: "Subscribing to slices of state to avoid broad re-renders"
tags: ["state", "selectors", "react", "performance"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# Selector Libraries

## Summary
Selector libraries let components subscribe to slices of shared state instead of the whole store: a `useSelector(fn)` hook runs the selector on every store change and re-renders the component only when the selected slice changes. Combined with memoized derived selectors, they are the standard mechanism for keeping large stores performant and components decoupled from state shape.

## Details
- Mechanism: the store keeps one state object; a selector is a pure function `(state) -> slice`. `useSelector` subscribes the component to the store, runs the selector after each dispatch, compares the result with the previous one (default `===` reference equality, or a custom `equalityFn`), and re-renders only on inequality. Memoized selectors (`createSelector` in Redux Toolkit, Zustand's `useShallow`, Jotai's derived atoms) cache the slice per input combination, so ten components reading `visibleTodos` share one computation and one equality check. The reference-equality rule is the crux: a selector that returns a new object each time defeats the comparison and causes infinite re-renders or constant re-renders.
- Concrete examples: a header reads `useSelector(s => s.user.name)` and re-renders only when the name changes, not when the todos change; a list uses `createSelector([selectTodos, selectFilter], (todos, filter) => todos.filter(...))` so filtering happens once per change and every consumer shares the cached result; Zustand's `useStore(store, s => s.cart.items)` with `useShallow` compares shallowly so array contents changes are detected without new-array churn.
- Failure modes: the classic failures are selectors returning fresh objects or arrays (new reference per run, so equality never matches — fixed with `createSelector` memoization or `useShallow`), selectors with side effects or nondeterminism (breaks memoization and causes inconsistent renders), and over-wide selectors that subscribe to more than the component needs. Deeply nested state selects are also brittle: `s.a.b.c` breaks when the shape changes, which is why selectors are supposed to be the single place that knows the shape.
- Operational tradeoffs: selectors buy precise re-render boundaries and reusable derivations at the cost of an extra concept and the discipline that selectors stay pure and memoized. They pair with derived-state principles: selectors ARE derived state with caching. The modern interplay with signals: signal frameworks make selectors nearly obsolete for local derivation (the framework tracks dependencies), but selectors still matter at the store boundary where many components share state. The practice rule: keep selectors pure and memoized, prefer narrow selects, and let selector libraries handle equality so components render exactly as often as their data changes.
- RSIS3/mykb relevance: the dashboard's telemetry views are the selector use case: memoized slices (success rate per loop, pulse counts per window) computed once from raw state and subscribed narrowly — the same derived-metric discipline RSIS3 uses, where aggregates are recomputed from raw telemetry and cached until inputs change.

## Related
- [[wiki/frontend-frameworks/react-ecosystem|React Ecosystem]] — related coverage in the same cluster
- [[wiki/frontend-frameworks/derived-state|Derived State]] — related coverage in the same cluster
- [[wiki/frontend-frameworks/selectors-practice|Selectors in Practice]] — related coverage in the same cluster
- [[wiki/frontend-frameworks/memoization-practice|Memoization Practice]] — related coverage in the same cluster
- [[wiki/frontend-frameworks/declarative-ui|Declarative UI]] — related coverage in the same cluster
- [[wiki/web-platforms/state-management|State Management]] — related coverage in the same cluster
- [[wiki/web-platforms/web-performance-optimization|Web Performance Optimization]] — related coverage in the same cluster
