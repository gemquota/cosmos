---
type: "concept"
title: "Vue Reactivity"
description: "Proxy-based dependency tracking in Vue 3"
tags: ["vue", "reactivity", "proxies", "frontend"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# Vue Reactivity

## Summary
Vue 3's reactivity system is Proxy-based dependency tracking: `reactive()` and `ref()` wrap state in Proxies that record which effects read which properties, and when a property is written, exactly those effects re-run. Computeds layer caching and laziness on top, and a scheduler batches updates so the DOM never sees intermediate states.

## Details
- Mechanism: reading a property through the Proxy triggers a `get` trap that registers the currently-running effect as a dependent of that property; writing triggers a `set` trap that marks dependents dirty. Effects (`watchEffect`, computed getters, render functions) run inside a tracking context, so the dependency set is discovered automatically — no dependency arrays to maintain. Computeds cache their result and re-evaluate lazily only when a dependency changed *and* they are read. Updates are batched through a microtask scheduler: multiple writes in one tick schedule one effect run, which prevents redundant renders and "flash" intermediate values.
- Concrete examples: a `reactive({ user: { name: '' } })` object where a template reading `user.name` updates only that binding when the name changes; `ref(0)` for primitives with `.value` access; a `computed(() => items.value.filter(...))` that recomputes once per relevant change even if three components read it; `watch(() => store.token, fn)` that fires only when the token changes; `shallowRef`/`markRaw` to opt out of deep reactivity for performance or for objects with native state.
- Failure modes: the classic pitfalls are destructuring reactive state (`const { name } = reactiveObj` copies a plain string — reactivity lost; use `toRefs`), replacing a reactive object with a new plain object (the proxy identity changes and watchers miss it unless `deep: true` or the object is wrapped), and `Vue.set`-style thinking from Vue 2 (in Vue 3, adding properties is reactive automatically because the Proxy intercepts them — but array-index writes and `length` changes need care). Effect bugs: a `watchEffect` that writes what it reads creates loops, and tracking inside async callbacks is lost unless the reactive read happens synchronously.
- Operational tradeoffs: Vue 3's Proxy model is more precise than Vue 2's `Object.defineProperty` approach (property additions are reactive, arrays are handled natively) at a small proxy-construction cost for deeply nested objects, which is what `shallowRef` and `markRaw` are for. Compared with signals, Vue's system is functionally similar — automatic dependency tracking with computed caching — but operates through proxies on plain objects rather than explicit cell APIs, which is more ergonomic and slightly more opaque. The practice rule: keep reactive reads inside computed/effects/render, use `toRefs` when destructuring, prefer `ref` for primitives, and reserve `shallowRef` for large, infrequently-mutated structures.
- RSIS3/mykb relevance: Vue's automatic dependency graph is the exact model RSIS3 aspires to for loop outputs — invalidate precisely what changed, lazily and in batches — and MyKB's dashboard components benefit from the same auto-tracked derivation discipline.

## Related
- [[wiki/frontend-frameworks/vue-ecosystem|Vue Ecosystem]]
- [[wiki/frontend-frameworks/reactivity-pitfalls|Reactivity Pitfalls]]
- [[wiki/frontend-frameworks/vue-composition-api|Vue Composition API]]
- [[wiki/frontend-frameworks/declarative-ui|Declarative UI]]
- [[wiki/web-platforms/state-management|State Management]]
- [[wiki/web-platforms/web-frameworks|Web Frameworks]]
