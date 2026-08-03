---
type: "concept"
title: "State Machines on the Web"
description: "Explicit states and transitions for complex UI flows"
tags: ["state-machines", "frontend", "patterns", "state"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# State Machines on the Web

## Summary
State machines on the web model UI and application flows as explicit states with defined transitions: a machine declares `states`, `events`, `transitions`, `guards`, and `actions`, and the UI renders from the current state. The payoff is that impossible states cannot exist — no "loading and error at once" — and complex flows become inspectable, testable, and portable between client and server.

## Details
- Mechanism: a finite state machine (or extended statechart) is a directed graph: nodes are states (`idle`, `submitting`, `success`, `error`), edges are transitions labeled with events (`SUBMIT`, `RETRY`), guards conditionally allow transitions (validation passes), and actions fire on entry/exit (send the request, log analytics). The machine holds exactly one active state, so the UI's condition is always unambiguous. Statecharts add hierarchy (parallel/child states), history states, and delayed transitions, which is where libraries like XState earn their keep.
- Concrete examples: an auth flow with `signedOut | signingIn | signedIn | error` states and guarded transitions (only retry when the failure is transient); a checkout wizard where each step is a state and `NEXT`/`BACK` events move between them, with `deepLink` events jumping directly to a step; a realtime sync client with `disconnected | connecting | connected | syncing` states and delayed reconnection transitions; a form with `idle | validating | submitting | success | error` and effects attached to each entry.
- Failure modes: the classic failures are state explosion (modeling every combination of independent flags as a single flat machine, when orthogonal or parallel states fit better), over-modeling trivial flows (a statechart for a checkbox adds ceremony without benefit), and hiding work in event handlers instead of transitions (side effects then run on unexpected paths). Machines also fail silently when components bypass them with imperative `setState` calls, so enforcement requires discipline or tooling.
- Operational tradeoffs: state machines trade upfront modeling effort for long-term correctness and clarity: flows are documented in code, every transition is testable, and the same machine can run on the client and server (validation parity). The costs are a learning curve, a new abstraction, and the overhead of defining states that simple boolean flags handled informally. The practice guidance: reach for machines when a flow has multiple states, retries, or business rules (auth, onboarding, checkout, realtime sync); keep plain state for simple toggles, and use a statechart library when hierarchy or delayed transitions are needed.
- RSIS3/mykb relevance: RSIS3's loops are state machines by design — phases, guarded transitions, and entry actions — and the dashboard's connection status (loading, live, degraded, offline) should be modeled the same way, so the UI can never claim "live and offline" simultaneously.

## Related
- [[wiki/frontend-frameworks/react-ecosystem|React Ecosystem]] — related coverage in the same cluster
- [[wiki/frontend-frameworks/xstate-practice|XState in Practice]] — related coverage in the same cluster
- [[wiki/frontend-frameworks/finite-state-uis|Finite State UIs]] — related coverage in the same cluster
- [[wiki/frontend-frameworks/immutable-state|Immutable State]] — related coverage in the same cluster
- [[wiki/web-platforms/state-management|State Management]] — related coverage in the same cluster
- [[wiki/frontend-frameworks/declarative-ui|Declarative UI]] — related coverage in the same cluster
- [[wiki/software-engineering/reactive-programming|Reactive Programming]] — related coverage in the same cluster
