---
type: "concept"
title: "Process Manager Pattern"
description: "A stateful component that coordinates a workflow by routing messages between participants"
tags: ["workflow", "messaging", "saga", "state-machine"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
---
# Process Manager Pattern

## Summary

A process manager (workflow/saga coordinator) is a component that tracks the state of a multi-step business process across services and drives it to completion — issuing commands, awaiting events, and executing compensations. It is orchestration's reference implementation.

## Details
- Mechanism: the manager persists process state (order id, step, collected data), listens for events, and issues commands to participants; it decides the next step from its state machine and handles failures (retries, timeouts, compensation); it is itself a service, so it must be idempotent and replayable from its persisted state.
- Concrete example: an order saga manager: receives OrderPlaced, commands payment, awaits PaymentCompleted (with timeout → cancel), then inventory, then shipping, compensating backward on failure; a provisioning manager walks create-VM → configure → register steps, retrying each with backoff and recording progress.
- Failure modes: the manager as a god service accumulating every rule (keep participants responsible for their domain); state and command mismatch after schema changes (version the process state); lost events or duplicates (idempotent handlers, outbox); and managers that block on synchronous calls, defeating the async design.
- Operational tradeoffs: process managers make complex flows explicit and auditable at the cost of a central component to operate; the alternative (choreography) hides the flow but decouples better. Persist the state, test failure injection, and keep the state machine visible.
- RSIS3/mykb relevance: the wiki's multi-step agent workflows are driven by persisted process managers, so loop runs resume after crashes and compensate on failure.
- Timeout policy: every awaited event needs a deadline with a defined consequence (retry, escalate, compensate); a process that waits forever is the classic latent bug.
- Versioning: version the process-state schema and the command/event contracts so long-running processes survive deployments across versions.

## Related
- [[wiki/software-engineering/choreography-vs-orchestration|Choreography vs Orchestration]] — the process manager is the orchestration implementation
- [[wiki/software-engineering/compensating-transactions|Compensating Transactions]] — managers trigger compensations on failure
- [[wiki/agent-systems/session-state-machine|Session State Machine]] — stateful flows in the agent world
- [[wiki/api-protocols/message-queues|Message Queues]] — the transport that feeds the manager
- [[wiki/software-engineering/event-driven-architecture|Event-Driven Architecture]] — managers coordinate event-driven flows
