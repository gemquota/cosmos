---
type: "concept"
title: "Unidirectional Data Flow"
description: "One-way data flow and store architecture"
tags: [state-management", "architecture", "redux", "flux", "data-flow"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://redux.js.org/tutorials/fundamentals/part-2-concepts-data-flow", "https://facebook.github.io/flux/docs/in-depth-overview/"]
---

# Unidirectional Data Flow

## Summary
Unidirectional data flow means state changes travel one way: a view dispatches an action, a reducer computes a new state, and the store notifies views that re-render from that state. Nobody mutates state out of band. Flux introduced the pattern and Redux popularized it; React's model and most signals frameworks follow the same loop.

## Details
- Cycle: action → reducer → new state → view; views never write to the store directly.
- Predictability: with pure reducers, the same action sequence always produces the same state, enabling time-travel debugging.
- Testability: reducers are plain functions, trivially unit-testable without UI or network.
- Selectors: derived data is computed from state rather than stored redundantly, keeping one source of truth.
- Costs: boilerplate and indirection grow with complexity; lighter tools (Zustand, Jotai) keep the direction but trim ceremony.
- Fit: large apps with interdependent state; small apps can manage with local state and context.

## Related
- [[wiki/frontend/state-management-patterns|State Management Patterns]] — where the pattern fits
- [[wiki/frontend/reactive-state|Reactive State]] — the reactivity model downstream
- [[wiki/frontend/component-composition|Component Composition]] — views built from state
- [[wiki/web-platforms/state-management|State Management]] — platform context
- [[wiki/frontend/frontend-testing|Frontend Testing]] — testing pure reducers
- [[wiki/software-engineering/functional-programming|Functional Programming]] — the reducer philosophy
