---
type: "concept"
title: "Process Manager Pattern"
description: "A stateful component that coordinates a workflow by routing messages between participants"
tags: ["workflow", "messaging", "saga", "state-machine"]
timestamp: "2026-08-01T00:00:00Z"
status: "stub"
---

# Process Manager Pattern

## Summary
A process manager (or workflow engine) is a stateful message handler that tracks the progress of a business process and routes events to the right participants. It implements orchestration with durable state so flows survive restarts.

## Details
- State is persisted between messages, making the manager resilient to crashes mid-flow.
- It can implement timeouts, retries, and compensation logic centrally.
- RSIS3 relevance: agent session state machines are a close cousin of the pattern.

## Related
- [[wiki/software-engineering/choreography-vs-orchestration|Choreography vs Orchestration]] — the process manager is the orchestration implementation
- [[wiki/software-engineering/compensating-transactions|Compensating Transactions]] — managers trigger compensations on failure
- [[wiki/agent-systems/session-state-machine|Session State Machine]] — stateful flows in the agent world
- [[wiki/api-protocols/message-queues|Message Queues]] — the transport that feeds the manager
- [[wiki/software-engineering/event-driven-architecture|Event-Driven Architecture]] — managers coordinate event-driven flows
