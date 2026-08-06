---
type: "concept"
title: "Agent Planning Systems"
description: "Components that decompose goals into ordered, executable plans"
tags: ["agents", "planning", "decomposition", "goals"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://arxiv.org/abs/2210.03629", "https://arxiv.org/abs/2305.10601"]
---

# Agent Planning Systems

## Summary
Planning systems turn a high-level goal into a structured sequence of actions or subgoals an agent can execute. Planning can be internal (the model reasons about steps) or external (a planner module, HTN, or state-machine expands the plan). Good planning bounds search and makes agent behavior auditable.

## Details
- **Approaches** — single-shot plan generation, plan-execute-observe loops, hierarchical task networks, and reactive replanning.
- **Plan representation** — ordered steps, DAGs with dependencies, or goal trees; the representation determines what can be validated.
- **Replanning** — plans must be revised when observations diverge; the plan-execute-observe pattern makes this explicit.
- **Worked example** — a migration agent plans: audit schema → scaffold migration → run tests → rollback on failure, each step with a success criterion.
- **Failure modes** — overplanning (analysis paralysis), underplanning (missing dependencies), and stale plans after context changes.
- **mykb relevance** — RSIS3's L3 self-direction layer generates and prioritizes its own goals, making planning the engine of recursion.

- **Validation before execution** — a plan is only as good as its preconditions; validating steps, dependencies, and resource requirements before acting catches errors cheaply.
- **Contingency planning** — robust plans carry fallback branches for likely failures such as tool errors and missing data, rather than assuming the happy path.
- **Auditability** — a recorded plan makes agent behavior explainable after the fact: reviewers can check why a sequence of actions was chosen.
- **Plan representation depth** — the representation determines what can be validated and resumed; a machine-checkable plan supports replanning, while free-text plans only support human review.
## Related
- [[wiki/agent-systems/goal-decomposition|Goal Decomposition]] — breaking goals into subgoals
- [[wiki/agent-systems/plan-execute-observe|Plan-Execute-Observe]] — the loop that executes plans
- [[wiki/concepts/hierarchical-task-network|Hierarchical Task Network]] — structured planning formalism
- [[wiki/agent-systems/hierarchical-agents|Hierarchical Agents]] — planners at multiple levels
- [[wiki/agent-systems/agent-prioritization|Agent Prioritization]] — ordering tasks within a plan
- [[wiki/agent-systems/task-scheduling-agents|Task Scheduling for Agents]] — related concept in this cluster
- [[wiki/agent-systems/agent-loop|Agent Loop]] — the loop agents execute
- [[wiki/syntheses/knowledge-system|Knowledge System Overview]] — the KB loop this work feeds
