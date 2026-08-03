---
type: "concept"
title: "Zustand in Practice"
description: "Minimal external store hooks for React state"
tags: ["zustand", "state", "react", "frontend"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# Zustand in Practice

## Summary
Zustand is a minimal state library: a store is created with `create((set) => ({ ... }))`, lives outside React as a plain object with `getState`/`setState`, and components subscribe through a selector hook (`useStore(store, (s) => s.count)`). It offers Redux-style central state without actions/reducers ceremony, and its selector-based subscription model keeps re-renders narrow.

## Details
- Mechanism: `create` builds a store with state and actions; actions are plain functions that call `set` (partial merge by default) or `setState`, and can also call `get` for cross-slice logic. `useStore(store, selector)` subscribes the component and re-renders only when the selector's result changes (default reference equality; `useShallow` for shallow comparison of objects/arrays). Because the store is external, it works outside React (event handlers, plain modules, non-React code), supports `subscribe` for imperative listeners, and persists via the `persist` middleware (localStorage/sessionStorage with versioned migrations). Middleware (`devtools`, `immer`, `subscribeWithSelector`) bolt on features without changing the core.
- Concrete examples: a cart store with `items`, `addItem`, `removeItem` and a `total` selector used by the header badge and checkout page; a UI store holding theme, sidebar state, and modals that non-React code (a router hook) can read; a persisted settings store that rehydrates on load; a store composed from slices (`create(...({ ...userSlice, ...cartSlice }))` or `createStore` + slices).
- Failure modes: the classic failures are selectors returning new references each call (`(s) => ({ a: s.a })` re-renders every time unless `useShallow` is used), over-fetching whole stores (subscribing to the entire state object when one field is needed), and mutating state outside `set` (in-place changes bypass subscribers). The `persist` middleware has its own traps: stale persisted state crashing on load unless migrations are declared, and SSR hydration mismatches.
- Operational tradeoffs: Zustand sits between Context (built-in, but broad re-render blast radius and provider nesting) and Redux (full ceremony, DevTools, time-travel). It wins on minimalism — no providers, no actions boilerplate, framework-agnostic store, precise subscriptions — and is the recommended default for shared client state in modern React apps, with server state delegated to TanStack Query. The tradeoffs: no built-in time-travel, less structure for huge teams (nothing forces action discipline), and selector patterns that must be learned. The rule: use Zustand for client state shared across many components, Context for rarely-changing values, and a data-fetching library for server state.
- RSIS3/mykb relevance: the dashboard's shared UI state (active view, filters, daemon status) is a natural Zustand store — selectable slices keep embedded widgets re-rendering precisely, mirroring RSIS3's separation of shared configuration from per-loop working state.

## Related
- [[wiki/frontend-frameworks/react-ecosystem|React Ecosystem]] — related coverage in the same cluster
- [[wiki/frontend-frameworks/jotai-practice|Jotai in Practice]] — related coverage in the same cluster
- [[wiki/frontend-frameworks/recoil-practice|Recoil in Practice]] — related coverage in the same cluster
- [[wiki/frontend-frameworks/mobx-practice|MobX in Practice]] — related coverage in the same cluster
- [[wiki/web-platforms/state-management|State Management]] — related coverage in the same cluster
- [[wiki/frontend-frameworks/state-management-mobile|State Management Mobile]] — related coverage in the same cluster
- [[wiki/frontend-frameworks/declarative-ui|Declarative UI]] — related coverage in the same cluster
