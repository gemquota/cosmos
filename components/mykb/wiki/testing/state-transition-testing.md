---
type: "concept"
title: "State Transition Testing"
description: "Testing flows through finite states and transitions"
tags: ["state-transition", "testing", "state-machines", "technique"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://www.istqb.org/glossary", "https://www.ibm.com/topics/state-transition-testing"]
---

# State Transition Testing

## Summary
State transition testing verifies flows through finite states and transitions, allowed moves, guards, and invalid transitions. It models systems where behavior depends on history rather than just the latest input.

## Details
- Model: states, events, transitions, guards, and entry or exit actions.
- Cover every transition, every state entry and exit, invalid events, and unreachable states.
- Use cases: order lifecycle, session state, workflow engines, and protocol implementations.
- Tooling: model-based testing tools and state machine libraries; visualize with diagrams.
- Pair with negative tests: unexpected events must be handled gracefully.
- Combine with decision tables when transitions depend on conditions.
- Assert both state changes and the side effects of transitions.

## Related
- [[wiki/testing/model-based-testing|Model-Based Testing]] — automatic generation from models
- [[wiki/testing/decision-table-testing|Decision Table Testing]] — condition-driven transitions
- [[wiki/testing/negative-testing|Negative Testing]] — invalid events and guards
- [[wiki/testing/test-oracles|Test Oracles]] — expected transition outcomes
- [[wiki/agent-systems/session-state-machine|Session State Machine]] — a real-world state machine to test
- [[wiki/testing/black-box-testing|Black-Box Testing]] — behavioral testing of states
