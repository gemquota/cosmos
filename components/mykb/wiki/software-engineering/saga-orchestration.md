---
type: "concept"
title: "Saga Orchestration"
description: "Coordinating a distributed transaction through a central orchestrator"
tags: ["saga", "orchestration", "distributed-transactions", "patterns"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Saga Orchestration

## Summary
Orchestrated sagas use a central coordinator that tells each participant what to do and invokes compensating actions when a step fails. The orchestrator holds the workflow state and sequence — easy to understand, with a single point of coordination.

## Details
- Steps call the orchestrator back (or the orchestrator drives them); compensations undo completed steps.
- The orchestrator persists its state so the saga survives restarts; make it idempotent.
- Contrast with choreography, where services react to events with no central brain.
- mykb relevance: a curation saga orchestrates fetch, verify, and publish steps with compensations.

## Related
- [[wiki/software-engineering/saga-choreography|Saga Choreography]]
- [[wiki/software-engineering/compensating-transactions|Compensating Transactions]]
- [[wiki/software-engineering/choreography-vs-orchestration|Choreography vs Orchestration]]
- [[wiki/software-engineering/process-manager-pattern|Process Manager Pattern]]
- [[wiki/software-engineering/outbox-pattern|Outbox Pattern]]
