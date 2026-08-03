---
type: "concept"
title: "Composition APIs"
description: "Function-based component composition versus options and class APIs"
tags: ["react", "vue", "composition", "frontend"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# Composition APIs

## Summary
Composition APIs organize component logic as functions rather than scattering it across lifecycle slots or class methods. Vue 3's Composition API and React Hooks are the two prominent examples: related behavior — state, derived values, effects, and subscriptions for one feature — lives together in a reusable function, which improves readability, testability, and code sharing compared with options objects or class components.

## Details
- Mechanism: an options API (Vue 2) spreads one feature's logic across `data`, `computed`, `methods`, `watch`, and lifecycle hooks, so a component that owns three features interleaves three sets of concerns in five sections; a class API (Angular, React classes) does the same across methods and lifecycle callbacks. A composition API collects each feature into a function: `setup()` in Vue returns reactive bindings, and Hooks in React attach state and effects to the component instance in call order. Because these functions are plain functions, the logic is extractable, testable in isolation, and composable — you can call one composable inside another.
- Concrete examples: a `useUserProfile` hook (or `useUserProfile` composable) owns fetching, loading state, error handling, and a retry action, so three different screens reuse it with one call; a Vue component's `setup()` can compose `useCart`, `useAuth`, and `useNotifications` side by side, each self-contained; an Angular standalone function `inject()` plus signals achieves the same shape. The win is that a feature's lifecycle (mount, update, cleanup) is enclosed in one function instead of spread across the component skeleton.
- Failure modes: the classic failures are rules-of-hooks violations (calling hooks conditionally or in loops, which breaks call-order identity), stale closures over state that was captured once, and dependency arrays that are wrong — too short (stale data), too long (effect churn), or missing (recreated subscriptions). Composition APIs also tempt over-abstraction: extracting a composable for every three lines of logic creates indirection that hides the data flow, and mixing reactive primitives with imperative values (Vue's refs/unwrapping, React's refs) confuses newcomers and even veterans.
- Operational tradeoffs: composition APIs are a clear ergonomic and testing win — logic is shareable without render props, mixins, or HOC wrapping, and tests can call the composable with a harness. The costs are a steeper learning curve, new tooling (eslint-plugin-react-hooks) and a shift in mental model from "component = object with lifecycle" to "component = composition of functions". Teams migrating from options/class APIs should map each lifecycle concern to its composable equivalent and keep composables small and single-purpose.
- RSIS3/mykb relevance: composable, single-responsibility functions mirror RSIS3's L1 loop discipline: each capability (fetch, derive, persist) as an independent, reusable unit with explicit inputs and outputs, so the dashboard UI and the knowledge layer both stay modular as features accumulate.

## Related
- [[wiki/frontend-frameworks/react-ecosystem|React Ecosystem]]
- [[wiki/frontend-frameworks/hooks-practice|Hooks in Practice]]
- [[wiki/frontend-frameworks/hoc-patterns|Higher-Order Components]]
- [[wiki/frontend-frameworks/context-api|Context API]]
- [[wiki/frontend-frameworks/declarative-ui|Declarative UI]]
- [[wiki/web-platforms/state-management|State Management]]
- [[wiki/web-platforms/web-frameworks|Web Frameworks]]
