---
type: "concept"
title: "Finite State UIs"
description: "Modeling UI conditions as bounded states with defined edges"
tags: ["state-machines", "ui", "frontend", "patterns"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# Finite State UIs

## Summary
Finite state UIs model every condition a screen can be in as a named state with a bounded set of transitions: a dialog is `closed` or `open`, a fetch is `idle`, `loading`, `success`, or `error`, a wizard is on one of its steps. Replacing ad-hoc booleans with explicit states eliminates impossible combinations like "loading and error at the same time" and makes the UI's behavior testable and visualizable.

## Details
- Mechanism: a finite state machine declares states, events, and transitions — `from: 'loading', on: { SUCCESS: 'success', ERROR: 'error' }` — and the UI renders from the current state. Events are the only way to move between states, so the machine cannot reach an undeclared combination; guard functions can restrict transitions, and effects (fetch on entering `loading`, analytics on `success`) attach to states. Libraries like XState formalize this with statecharts, but the pattern is implementable with a discriminated union and a reducer.
- Concrete examples: a login form modeled as `idle | submitting | success | error` makes the retry flow explicit (error → submitting on RESUBMIT); a data table with `loading | empty | error | populated` states means the "empty" view is a real state instead of `data.length === 0` nested in a success branch; a multi-step checkout has one state per step with `NEXT` and `BACK` events, making deep links and browser-back handling declarative. Data fetching is a natural fit: the async lifecycle is a small machine with a retry edge.
- Failure modes: the common failures are over-engineering (a full statechart for a checkbox), state explosion (a separate state for every combination of independent conditions, when orthogonal machines or parallel states would do), and transitions that carry hidden work (side effects buried in event handlers rather than attached to state entry, so the same effect runs on unexpected paths). The pattern also fails when components bypass the machine with imperative calls, silently mutating UI state outside the declared edges.
- Operational tradeoffs: finite-state modeling costs a new abstraction and a steeper design discipline, and it pays back in correctness — impossible states cannot render, flows are documented in code, and tests can drive the machine through every transition. For small screens, a discriminated union is enough; for complex flows (auth, onboarding, checkout, realtime sync), a statechart library earns its keep, especially when the same machine needs to run on the server or in tests.
- RSIS3/mykb relevance: RSIS3's loops are state machines in spirit — each loop has phases with guarded transitions; modeling the dashboard's views (loading, live, degraded, offline) as finite states keeps the UI honest about the system's actual condition, the same way the registry tracks loop state explicitly.

## Related
- [[wiki/frontend-frameworks/react-ecosystem|React Ecosystem]]
- [[wiki/frontend-frameworks/immutable-state|Immutable State]]
- [[wiki/frontend-frameworks/state-machines-web|State Machines on the Web]]
- [[wiki/frontend-frameworks/xstate-practice|XState in Practice]]
- [[wiki/web-platforms/state-management|State Management]]
- [[wiki/frontend-frameworks/declarative-ui|Declarative UI]]
- [[wiki/software-engineering/reactive-programming|Reactive Programming]]
