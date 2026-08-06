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
Blackboard architecture has independent specialists read and write a shared working area — the blackboard — until a solution emerges. It decouples contributors: no one owns the whole problem, and every contribution is visible on the board. It is the classic shared-state alternative to hierarchical orchestration.

## Details
- **Parts** — the blackboard holds the shared problem state; knowledge sources (specialists) watch for conditions they can advance; a control component decides whose contribution runs next.
- **When it suits** — problems with no single decomposition — speech understanding, diagnosis, open-ended search — where solutions emerge from many partial contributions rather than a fixed pipeline.
- **Inspectability** — the blackboard is auditable at every step: each contribution is a written record, which supports explanation and replay.
- **Control risk** — without good scheduling, knowledge sources thrash or starve, and the shared board becomes a contention bottleneck; the control component is the real design difficulty.
- **Comparison** — a blackboard is the flat alternative to hierarchical agents: hierarchies route work top-down, blackboards let any specialist pick up the problem from shared state; hybrid systems mix both.
- **For mykb** — the shared wiki index and link graph act as a blackboard: many specialized passes (link checks, tag audits, synthesis) contribute to one evolving knowledge state, with scheduling by priority rather than ownership.
- **Failure modes** — duplicated work when sources overlap, conflicting writes when contributions collide, and no global view when the board state grows beyond comprehension.

- **Scheduling policies** — priority by contribution value, round-robin fairness, and opportunistic batching are the standard policies; the right one depends on whether the bottleneck is contention or starvation.
- **Boundary of fit** — blackboards shine when contributions are partial and order-independent; when the task has a known pipeline, the pipeline wins on predictability and the blackboard loses.
## Related
- [[wiki/agent-systems/multi-agent-orchestration|Multi-Agent Orchestration]] — orchestrated coordination
- [[wiki/agent-systems/hierarchical-agents|Hierarchical Agents]] — the top-down alternative
- [[wiki/concepts/production-rules|Production Rules]] — condition-driven contributions
- [[wiki/agent-systems/behavior-trees|Behavior Trees]] — tree-based control alternative
- [[wiki/data-storage/knowledge-graph|Knowledge Graph]] — the shared-state store
- [[wiki/concepts/cognitive-architecture|Cognitive Architecture]] — architectural home
