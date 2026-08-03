---
type: "concept"
title: "Choreography vs Orchestration"
description: "Two coordination styles for multi-step workflows: distributed responsibility vs a central conductor"
tags: ["workflow", "architecture", "events", "saga"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
---
# Choreography vs Orchestration

## Summary

Orchestration centralizes workflow control in a conductor that calls participants; choreography distributes it — each service reacts to events and knows only its part. Orchestration is easier to reason about; choreography scales and decouples but makes the whole harder to see.

## Details
- Mechanism: orchestration has an explicit controller (a saga orchestrator, workflow engine, or process manager) that issues commands and tracks state — the flow is readable in one place; choreography publishes domain events that interested services consume, each advancing its own part with no central state machine.
- Concrete example: order fulfillment as orchestration: an order saga calls payment, inventory, shipping, and compensates on failure — the flow is auditable in the saga; as choreography: OrderPlaced events trigger payment service, which emits PaymentSucceeded, which triggers inventory, and so on — decoupled, but no single view of the order lifecycle.
- Failure modes: choreography's hidden dependencies — services coupling through event schemas, implicit ordering, and missing handlers cause silent stalls; orchestration's central bottleneck and coupling — the conductor becomes the single point of failure and a god service; both suffer when error handling is not explicit (retries, dead-letter queues, compensation).
- Operational tradeoffs: start with orchestration for business-critical, auditable flows; use choreography where decoupling and scale matter and the event contract is stable; many systems blend them — orchestrated sagas with choreographed internal steps. Event-driven visibility (outbox, tracing) is mandatory either way.
- RSIS3/mykb relevance: the wiki's agent workflows record which pattern each loop uses, so multi-agent passes are either centrally steered or event-decoupled by design.
- Schema governance: event contracts are APIs — version them, test consumers, and treat schema changes as breaking changes even in choreography.
- Observability: both patterns need end-to-end tracing and saga state persistence; choreography without a queryable event history is undebuggable.

## Related
- [[wiki/software-engineering/event-driven-architecture|Event-Driven Architecture]] — choreography is the natural event-driven style
- [[wiki/software-engineering/process-manager-pattern|Process Manager Pattern]] — a stateful orchestrator that resumes flows
- [[wiki/api-protocols/saga-pattern|Saga Pattern]] — the workflow both styles implement
- [[wiki/agent-systems/multi-agent-orchestration|Multi-Agent Orchestration]] — agents face the same coordination choice
