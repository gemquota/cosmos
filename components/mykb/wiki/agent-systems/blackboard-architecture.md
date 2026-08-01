---
type: "concept"
title: "Blackboard Architecture"
description: "Multiple specialists coordinating through a shared, inspectable state"
tags: ["blackboard", "architecture", "multi-agent", "coordination"]
timestamp: "2026-07-31T00:00:00Z"
status: "stub"
---

# Blackboard Architecture

## Summary
Blackboard architecture has independent specialists read and write a shared working area — the blackboard — until a solution emerges. It matters because it decouples contributors: no one owns the whole problem. It is the classic shared-state alternative to hierarchical orchestration.

## Details
- Specialists watch for conditions they can advance; whoever can, acts.
- The blackboard is inspectable and auditable at every step.
- Risks: control is emergent, so deadlocks and thrashing are possible.
- Open questions: scheduling and conflict resolution among specialists.

## Related
- [[wiki/agent-systems/multi-agent-orchestration|Multi-Agent Orchestration]] — coordination topologies
- [[wiki/agent-systems/hierarchical-agents|Hierarchical Agents]] — the tree alternative
- [[wiki/llm-agents/expert-consultation|Expert Consultation]] — specialists in consultation mode
- [[wiki/concepts/production-rules|Production Rules]] — condition-triggered specialist action
- [[wiki/concepts/cognitive-architecture|Cognitive Architecture]] — the architecture family it belongs to
