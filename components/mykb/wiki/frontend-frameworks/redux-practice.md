---
type: "concept"
title: "Redux in Practice"
description: "Single-store unidirectional state with actions and reducers"
tags: ["redux", "state", "frontend", "architecture"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# Redux in Practice

## Summary
Redux is the archetypal unidirectional state architecture: a single store holds the whole application state, actions describe what happened, and pure reducers compute the next state from the previous state and the action. Predictability is the product — the entire state transition log can be replayed, serialized, and time-travel debugged — and Redux Toolkit is now the standard way to write it.

## Details
- Mechanism: the store holds one state object; `dispatch(action)` sends a plain object (`{ type: 'todos/add', payload: {...} }`) through the reducer chain; reducers are pure functions `(state, action) -> newState` that never mutate state; and components read state via `useSelector` (which subscribes to slices) and dispatch via `useDispatch`. Middleware sits between dispatch and the reducer — Redux Thunk and Redux Toolkit's `createAsyncThunk` handle async logic there, and custom middleware handles logging, analytics, or cross-cutting concerns. Selectors (`createSelector`) memoize derived reads shared by many components.
- Concrete examples: a cart store with `addItem`/`removeItem` reducers and a memoized `cartTotal` selector; an async data flow where `createAsyncThunk('users/fetch', ...)` dispatches `pending/fulfilled/rejected` actions that drive a slice's status fields; time-travel debugging where the Redux DevTools replays every action to reproduce a bug; a multi-window app where the same store is serialized and restored from `localStorage` on reload.
- Failure modes: the classic failures are impure reducers (mutating state, calling APIs, or using `Math.random()` inside a reducer, which breaks replay and time-travel), over-centralization (every keystroke and UI toggle in the global store, producing enormous actions and re-renders), and selector misuse (selectors that return new objects each call defeat memoization and cause render loops). Async thunks that mutate state outside reducers and actions that carry non-serializable payloads (functions, class instances) break persistence and debugging.
- Operational tradeoffs: Redux's strength is explicit, auditable state — the action log is documentation, and debugging large apps is genuinely easier — at the cost of ceremony: actions, reducers, selectors, and middleware for even small features. Redux Toolkit removed most boilerplate (slices, `createAsyncThunk`, RTK Query) and is the recommended entry point, but the model still favors apps with complex, shared, or replayable state; for simple apps, Zustand or Jotai are lighter. The modern rule: Redux (Toolkit) for serious shared state with audit needs, lightweight stores for the rest, and server state in TanStack Query rather than the store.
- RSIS3/mykb relevance: Redux's event-sourced store is the closest frontend analog to RSIS3's registry: every mutation is a logged, replayable transition, and derived metrics come from memoized selectors over the raw state — the same append-only discipline MyKB uses for its knowledge graph.

## Related
- [[wiki/frontend-frameworks/react-ecosystem|React Ecosystem]] — related coverage in the same cluster
- [[wiki/frontend-frameworks/zustand-practice|Zustand in Practice]] — related coverage in the same cluster
- [[wiki/frontend-frameworks/jotai-practice|Jotai in Practice]] — related coverage in the same cluster
- [[wiki/frontend-frameworks/recoil-practice|Recoil in Practice]] — related coverage in the same cluster
- [[wiki/web-platforms/state-management|State Management]] — related coverage in the same cluster
- [[wiki/frontend-frameworks/state-management-mobile|State Management Mobile]] — related coverage in the same cluster
- [[wiki/frontend-frameworks/declarative-ui|Declarative UI]] — related coverage in the same cluster
