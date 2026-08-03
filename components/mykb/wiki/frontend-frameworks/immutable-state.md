---
type: "concept"
title: "Immutable State"
description: "Never-mutate updates that make change detection and undo tractable"
tags: ["state", "immutability", "frontend", "patterns"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# Immutable State

## Summary
Immutable state is the discipline of never mutating existing state objects: every update produces a new object that shares unchanged substructure with the old one. Because state objects are never changed in place, reference equality becomes a reliable change signal, undo/redo becomes a list of snapshots, and concurrent reads are always safe.

## Details
- Mechanism: an update copies the parts that change and reuses the rest — `setUser({ ...user, name: newName })` creates a new user object whose unchanged fields (and unchanged nested objects) are shared by reference. This structural sharing keeps copying cheap even for deep trees. React's re-render model depends on it: a component re-renders when its props reference changes, and immutability guarantees a changed value means a new reference while an unchanged value keeps its old reference, so `React.memo` and `shouldComponentUpdate` comparisons are sound. State-machine and event-sourced models (Redux reducers, XState) rely on the same property: each action produces a new state value from the previous one.
- Concrete examples: a Redux reducer returns `{ ...state, todos: state.todos.map(t => t.id === id ? { ...t, done: true } : t) }`; an undo stack pushes each new state snapshot and pops to revert; a statechart treats its state value as immutable so the same machine instance can be serialized, persisted, and time-travel-debugged; a list editor records the diff between snapshots for optimistic UI rollback.
- Failure modes: the classic failure is accidental mutation hiding in an "immutable" update — `todos.push(...)` or `obj.field = x` inside a reducer, which produces a new top-level reference with shared mutable internals, so reference checks pass while two snapshots silently share corrupted data. Libraries like Immer exist to make immutable updates ergonomic, but they add a proxy layer whose pitfalls (frozen objects, performance on huge structures, misuse of `draft` outside producers) create their own failure modes. Deep immutability also costs boilerplate and can hurt performance when entire large structures are copied per keystroke.
- Operational tradeoffs: immutability buys predictability (change detection, undo, time travel, memoization) at the cost of allocation and a stricter coding style. The modern synthesis is signals: a signal holds one mutable cell internally but exposes immutable snapshots, giving granular reactivity without copying large trees — the question is how far the signal's internal mutability can replace the outer object's. The practical rule: keep the state boundary immutable (updates produce new values), use Immer or immutable data structures where ergonomics hurt, and keep mutations inside isolated cells (refs, signals) where they are intentional.
- RSIS3/mykb relevance: MyKB's knowledge graph and RSIS3's registry are event-sourced: each write appends a new state, and rebuilds replay history — the immutable-state discipline is what makes snapshot generation and rollback correct without locks.

## Related
- [[wiki/frontend-frameworks/react-ecosystem|React Ecosystem]] — related coverage in the same cluster
- [[wiki/frontend-frameworks/state-machines-web|State Machines on the Web]] — related coverage in the same cluster
- [[wiki/frontend-frameworks/xstate-practice|XState in Practice]] — related coverage in the same cluster
- [[wiki/frontend-frameworks/finite-state-uis|Finite State UIs]] — related coverage in the same cluster
- [[wiki/web-platforms/state-management|State Management]] — related coverage in the same cluster
- [[wiki/frontend-frameworks/declarative-ui|Declarative UI]] — related coverage in the same cluster
- [[wiki/software-engineering/reactive-programming|Reactive Programming]] — related coverage in the same cluster
