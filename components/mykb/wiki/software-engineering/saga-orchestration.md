---
type: "concept"
title: "Saga Orchestration"
description: "Coordinating a distributed transaction through a central orchestrator"
tags: ["saga", "orchestration", "distributed-transactions", "patterns"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# Saga Orchestration

## Summary

Saga orchestration runs a distributed transaction as a sequence of local transactions coordinated by a central saga: each step commits, and on failure, preceding steps are compensated. It is the standard way to get atomicity-like guarantees across services without distributed locks.

## Details
- Mechanism: the saga manager (a process manager) issues commands in order, awaits results/events, and on failure executes compensations in reverse; each participant's step is a local ACID transaction; the saga itself persists its state so crashes resume or compensate correctly. Contrast with choreographed sagas, where services coordinate peer-to-peer via events.
- Concrete example: a travel booking saga: book flight → book hotel → book car; if the car fails, cancel hotel and flight — each cancellation is a compensating local transaction; a payment saga charges, reserves inventory, and refunds + releases on failure. The saga must handle partial failures at every step, including compensation failures (retries, escalations).
- Failure modes: non-idempotent commands (a retried charge double-charges — require idempotency keys); compensations that cannot run (external partner down — persist for retry, escalate); sagas that block on synchronous calls and lose the async resilience; and state-machine bugs from unhandled event ordering.
- Operational tradeoffs: orchestration centralizes visibility and control (easy to audit, hard to hide) at the cost of a coordinating component and per-step compensation work; the discipline is persisted saga state, timeout policies per step, idempotent participants, and failure-injection testing.
- RSIS3/mykb relevance: the wiki's provisioning and multi-step agent operations run as orchestrated sagas, so partial failures leave the system compensated, not half-deployed.
- Contract-first: define command and event schemas per step before wiring the saga; schema drift between steps is the most common source of saga bugs.
- Operational visibility: expose saga state (step, status, age) as metrics and a dashboard; sagas that stall silently are the classic failure of orchestration.

## Related
- [[wiki/software-engineering/saga-choreography|Saga Choreography]]
- [[wiki/software-engineering/compensating-transactions|Compensating Transactions]]
- [[wiki/software-engineering/choreography-vs-orchestration|Choreography vs Orchestration]]
- [[wiki/software-engineering/process-manager-pattern|Process Manager Pattern]]
- [[wiki/software-engineering/outbox-pattern|Outbox Pattern]]
