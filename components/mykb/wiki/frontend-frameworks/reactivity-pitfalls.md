---
type: "concept"
title: "Reactivity Pitfalls"
description: "Lost tracking, stale closures, and mutation mistakes in reactive UIs"
tags: ["reactivity", "state", "frontend", "debugging"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# Reactivity Pitfalls

## Summary
Reactivity pitfalls are the recurring ways reactive UIs break: lost tracking (reading a reactive value through a non-reactive path), stale closures (capturing an old value because a dependency was missed), and mutation mistakes (updating state in place so nothing notices). They are the debugging tax on fine-grained reactivity, and recognizing the pattern is half the fix.

## Details
- Mechanism: reactive systems (Vue's refs/computed, MobX observables, signals) track dependencies at *read time*: a computed or effect records every reactive value it reads and re-runs when one changes. The trap is that the tracking is invisible — destructure a ref (`const { count } = toRefs(state)` is fine, but `const count = state.count` on a plain object loses the proxy), read through a non-tracked helper, or pass a raw value instead of the reactive one, and the dependency never registers, so the UI goes stale with no error. Closures add a second axis: a handler or effect that captured `count` before an update still holds the old value unless the reactive read happens inside the reactive context.
- Concrete examples: in Vue, `const value = props.obj.count` in `setup` copies once and never updates, while `computed(() => props.obj.count)` stays live; in MobX, `store.items.map(...)` inside a component that is not an `observer` tracks nothing; in React, an effect with a missing dep reads the stale `count` forever. Destructuring a reactive object into plain variables, serializing a ref by accident (`JSON.stringify(count)` where count is a ref), and writing to a computed are the everyday variants.
- Failure modes: the classic failures are silent staleness (worst kind — no error, just wrong UI), reactivity loops (an effect writes a value it also reads, re-triggering itself), and over-subscription (reading an object property at render subscribes to the whole object in some frameworks, causing needless updates). Tooling is catching up — Vue's devtools highlight missing dependencies and React's lint rules catch stale closures — but each framework's failure signature differs, so teams need framework-specific debugging skills.
- Operational tradeoffs: the cure is discipline plus tooling: keep reactive reads inside reactive contexts (computed/effect/render), avoid destructuring reactive proxies, declare all dependencies (array or automatic tracking), and prefer `toRefs`/`storeToRefs` style helpers over manual unwrapping. The tradeoff is that fine-grained reactivity buys precision at the cost of invisible mechanics; explicit systems (Redux selectors, props) are more verbose but fail loudly. Teams adopting signals should treat "did I read this reactively?" as a review question.
- RSIS3/mykb relevance: the pitfalls are a warning against hidden dependencies in any reactive system, including RSIS3 loops: reads of registry state that bypass the declared dependency map silently freeze derived outputs, which is why RSIS3 check-practices verifies that telemetry and checkpoints derive from declared inputs.

## Related
- [[wiki/frontend-frameworks/vue-ecosystem|Vue Ecosystem]]
- [[wiki/frontend-frameworks/vue-composition-api|Vue Composition API]]
- [[wiki/frontend-frameworks/vue-reactivity|Vue Reactivity]]
- [[wiki/frontend-frameworks/declarative-ui|Declarative UI]]
- [[wiki/web-platforms/state-management|State Management]]
- [[wiki/web-platforms/web-frameworks|Web Frameworks]]
