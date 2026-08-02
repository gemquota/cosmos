---
type: "concept"
title: "State Machines"
description: "Modeling UI flows as finite state machines"
tags: [state-machines", "statecharts", "xstate", "architecture", "ui"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://xstate.js.org/docs/", "https://stately.ai/docs"]
---

# State Machines

## Summary
State machines model UI flows as finite sets of states, events, and transitions with explicit rules about what can happen when. Statecharts add hierarchy, parallelism, and guards, letting XState and similar tools express complex flows — forms, wizards, media players, async loading — without drifting into impossible states.

## Details
- Core model: a machine declares states, the events that trigger transitions, and initial state; invalid transitions are impossible by construction.
- Guards: transition conditions gate whether an event is allowed, keeping business rules out of component logic.
- Actions: entry, exit, and transition actions run side effects; actor model and interpreters execute the machine.
- Hierarchical and parallel states: statecharts nest and fork states, modeling real-world complexity cleanly.
- Visualization: machines render as diagrams, making flows reviewable by non-developers.
- Fit: any UI with many distinct states benefits; trivial toggles stay simpler as plain booleans.

## Related
- [[wiki/frontend/state-management-patterns|State Management Patterns]] — the taxonomy this extends
- [[wiki/frontend/form-validation|Form Validation]] — wizard and form flows as machines
- [[wiki/frontend/reactive-state|Reactive State]] — signals as the runtime underneath
- [[wiki/frontend/frontend-testing|Frontend Testing]] — testing machine transitions
- [[wiki/web-platforms/state-management|State Management]] — platform context
- [[wiki/frontend/unidirectional-data-flow|Unidirectional Data Flow]] — event-driven state change
