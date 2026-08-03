---
type: "concept"
title: "MobX in Practice"
description: "Observable-based state with automatic reactions"
tags: ["mobx", "state", "observables", "frontend"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# MobX in Practice

## Summary
MobX is an observable-based state library: plain objects and arrays are wrapped in observables, `computed` values derive reactively, and `autorun`/`reaction` run side effects automatically when the values they read change. Its model is transparent reactivity — state looks mutable, but every read tracks a dependency and every write schedules the reactions that depend on it.

## Details
- Mechanism: `makeObservable` (or `makeAutoObservable`) converts class fields into observables, actions, and computeds. When a reaction (an `autorun`, a `reaction`, or a React component using `observer()`) reads an observable, MobX records the dependency; when that observable is written inside an action, MobX recomputes the affected computeds and re-runs the reactions in dependency order, batching updates to avoid redundant work. React integration is `observer(Component)` — the component subscribes to exactly the observables it reads during render, so no selector functions or manual `useMemo` are needed.
- Concrete examples: a todo store with `todos` observable, `completedCount` computed, and an `addTodo` action; an `observer` list component re-renders only when the todos it renders change, while the header reading `completedCount` re-renders only when that count changes; a `reaction(() => store.token, token => api.save(token))` persists auth state when it changes; a form store where field values are observables and a `computed isValid` gates the submit button.
- Failure modes: the classic pitfalls are writing observables outside actions (fine functionally, but it defeats batching and can cause multiple intermediate reactions to fire), reading observables inside non-reactive contexts (a plain array method like `map` that does not get tracked, producing stale computed values), and losing reactivity by destructuring or slicing (passing `store.items.map(...)` results rather than the observable itself). `autorun` effects that read and write the same observable create loops; and over-use of `observer` on huge trees re-introduces the re-render costs fine-grained tracking was meant to remove.
- Operational tradeoffs: MobX's ergonomics are its biggest win — nearly invisible state management with automatic, precise updates — and its biggest risk is exactly that transparency: mutation-style state can hide surprising dependencies, and debugging "why did this re-render?" requires tracing the reactive graph rather than reading explicit selectors. It contrasts with Redux (explicit actions/reducers, better time-travel, more ceremony) and signals (similar dependency tracking, framework-integrated). The practice advice: keep mutations in actions, make stores explicit, prefer computeds over manual derivation, and use `observer` at the leaves where the granularity pays.
- RSIS3/mykb relevance: MobX's reaction graph is a miniature RSIS3: state changes propagate through declared dependencies to derived outputs, batched and ordered — the same discipline RSIS3 applies to loop outputs, where a pulse write automatically invalidates every metric that reads it.

## Related
- [[wiki/frontend-frameworks/react-ecosystem|React Ecosystem]] — related coverage in the same cluster
- [[wiki/frontend-frameworks/redux-practice|Redux in Practice]] — related coverage in the same cluster
- [[wiki/frontend-frameworks/zustand-practice|Zustand in Practice]] — related coverage in the same cluster
- [[wiki/frontend-frameworks/jotai-practice|Jotai in Practice]] — related coverage in the same cluster
- [[wiki/web-platforms/state-management|State Management]] — related coverage in the same cluster
- [[wiki/frontend-frameworks/state-management-mobile|State Management Mobile]] — related coverage in the same cluster
- [[wiki/frontend-frameworks/declarative-ui|Declarative UI]] — related coverage in the same cluster
