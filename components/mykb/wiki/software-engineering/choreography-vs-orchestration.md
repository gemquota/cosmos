---
type: "concept"
title: "Choreography vs Orchestration"
description: "Two coordination styles for multi-step workflows: distributed responsibility vs a central conductor"
tags: ["workflow", "architecture", "events", "saga"]
timestamp: "2026-08-01T00:00:00Z"
status: "stub"
---

# Choreography vs Orchestration

## Summary
Orchestration uses a central coordinator that tells each step what to do, while choreography lets each service react to events and decide its own next move. Both are valid for sagas and event-driven workflows; they differ in coupling and observability.

## Details
- Orchestration is easier to reason about and trace, but the coordinator becomes a bottleneck and a coupling point.
- Choreography is more decoupled and scalable, but flow logic is spread out and harder to debug.
- Mixed styles are common: orchestrate the skeleton, choreograph within it.

## Related
- [[wiki/software-engineering/event-driven-architecture|Event-Driven Architecture]] — choreography is the natural event-driven style
- [[wiki/software-engineering/process-manager-pattern|Process Manager Pattern]] — a stateful orchestrator that resumes flows
- [[wiki/api-protocols/saga-pattern|Saga Pattern]] — the workflow both styles implement
- [[wiki/agent-systems/multi-agent-orchestration|Multi-Agent Orchestration]] — agents face the same coordination choice
