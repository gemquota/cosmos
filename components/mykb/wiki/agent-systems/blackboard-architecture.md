---
type: "concept"
title: "Blackboard Architecture"
description: "Multiple specialists coordinating through a shared, inspectable state"
tags: ["blackboard", "architecture", "multi-agent", "coordination"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://en.wikipedia.org/wiki/Blackboard_system", "https://en.wikipedia.org/wiki/Blackboard_(design_pattern)"]
---

# Blackboard Architecture

## Summary
Blackboard architecture has independent specialists read and write a shared working area — the blackboard — until a solution emerges. It matters because it decouples contributors: no one owns the whole problem. It is the classic shared-state alternative to hierarchical orchestration.

## Details
- Specialists watch for conditions they can advance; whoever can, acts.
- The blackboard is inspectable and auditable at every step.
- Risks: control is emergent, so deadlocks and thrashing are possible.
- Open questions: scheduling and conflict resolution among specialists.
- The blackboard holds the shared problem state; independent knowledge sources watch it and contribute when their specialty applies, with a control component deciding whose contribution runs next.
- It suits problems with no single decomposition — speech understanding, diagnosis — where solutions emerge from many partial contributions rather than a fixed pipeline.
- The tradeoff is control: without good scheduling, knowledge sources thrash or starve, and the shared blackboard becomes a contention bottleneck.
- **Worked example / comparison** — Comparison — a blackboard is the flat alternative to hierarchical agents: hierarchies route work top-down, blackboards let any specialist pick up the problem from a shared state.
- For mykb, the blackboard metaphor maps to the shared wiki index and link graph: many specialized passes (link checks, tag audits) contribute to one evolving knowledge state.

## Related
- [[wiki/agent-systems/multi-agent-orchestration|Multi-Agent Orchestration]]
- [[wiki/agent-systems/hierarchical-agents|Hierarchical Agents]]
- [[wiki/llm-agents/expert-consultation|Expert Consultation]]
- [[wiki/concepts/production-rules|Production Rules]]
- [[wiki/concepts/cognitive-architecture|Cognitive Architecture]]
- [[wiki/concepts/promotion-readiness|Promotion Readiness]]
- [[wiki/dev-tools/global-link-check|Global Link Check]]
- [[wiki/concepts/connector-articles|Connector Articles]]
