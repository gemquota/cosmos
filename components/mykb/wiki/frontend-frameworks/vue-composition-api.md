---
type: "concept"
title: "Vue Composition API"
description: "setup()-based logic organization in Vue 3"
tags: ["vue", "composition", "reactivity", "frontend"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# Vue Composition API

## Summary
The Vue Composition API organizes component logic inside a `setup()` function (or `<script setup>`), where state is declared with `ref`/`reactive`, derived values with `computed`, and side effects with `watchEffect`/`watch`. Instead of spreading one feature across the options object's `data`, `computed`, `methods`, and lifecycle slots, each feature lives in a reusable composable function.

## Details
- Mechanism: `<script setup>` is the modern form — top-level declarations are compiled into `setup()` automatically. `ref(value)` wraps a value in a reactive cell (accessed as `.value` in JS, unwrapped in templates), `reactive(obj)` makes a plain object deeply reactive via Proxy, `computed(() => ...)` derives a value that recomputes when its reactive dependencies change, and `watch`/`watchEffect` run side effects. Composables are plain functions that call these primitives and return bindings, so `useUser()` can be called in any component and share logic without mixins, render props, or prop drilling.
- Concrete examples: a `useCart` composable owns `items`, `total` (computed), `addItem` (a plain function), and `persist` (a `watch` that writes localStorage); a component calls it in one line and uses `cart.items` in the template; a `useDebouncedRef` wraps a ref and a `watch` to debounce its value; a `useFetch(url)` composable returns `data`, `error`, and `retry`, reusable across screens. Lifecycle composables (`onMounted`, `onUnmounted`) let each feature manage its own lifecycle inside its composable.
- Failure modes: the classic pitfalls are losing reactivity by destructuring reactive objects (`const { count } = reactive({ count: 0 })` copies once — use `toRefs`), forgetting `.value` in JS (or over-applying it in templates), and calling composables conditionally (like React hooks, their internal `watch`/lifecycle registration assumes consistent call order). Options-API-style thinking leaks in when teams keep using `this` or split one feature across multiple composables, and SSR setups must avoid composables that touch `window` at setup time.
- Operational tradeoffs: the Composition API is strictly more powerful and flexible than the Options API — better TypeScript inference, logic reuse without mixin name-collisions, and feature-colocated code — at the cost of a steeper learning curve and a less "declarative-at-a-glance" component skeleton. Compared with React hooks, Vue composables are freer: no rules about exhaustive deps for `watch` (deps are tracked automatically) and no render-coupling, which removes a whole class of stale-closure bugs, though it also means fewer guardrails. Teams migrating from Options API should map each `data`/`computed`/`watch` section to composables gradually.
- RSIS3/mykb relevance: composables are the frontend version of RSIS3's modular loop functions — self-contained units that own their state, derivation, and lifecycle, composable in any order — and the same single-responsibility rule applies to both layers of the stack.

## Related
- [[wiki/frontend-frameworks/vue-ecosystem|Vue Ecosystem]] — related coverage in the same cluster
- [[wiki/frontend-frameworks/vue-reactivity|Vue Reactivity]] — related coverage in the same cluster
- [[wiki/frontend-frameworks/reactivity-pitfalls|Reactivity Pitfalls]] — related coverage in the same cluster
- [[wiki/frontend-frameworks/vue-composition-api|Vue Composition API]] — related coverage in the same cluster
- [[wiki/frontend-frameworks/declarative-ui|Declarative UI]] — related coverage in the same cluster
- [[wiki/web-platforms/state-management|State Management]] — related coverage in the same cluster
- [[wiki/web-platforms/web-frameworks|Web Frameworks]] — related coverage in the same cluster
