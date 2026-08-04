---
type: "entity"
title: "IntentDAG"
resource: ""
---
description: "A directed acyclic graph of intents with dependencies and ordering"
tags: ["android", "api", "ast", "auth", "authentication", "bash", "bug", "entity", "intent", "dag"]
timestamp: "2026-07-19T22:41:43Z"

# IntentDAG

## Summary
An IntentDAG is a directed acyclic graph that models intents and their dependencies, so complex goals can be satisfied in a valid order. It matters because real requests have prerequisites: you cannot confirm an order before identifying the user. A DAG makes those constraints explicit and executable, turning orchestration into data that can be analyzed.

## Details
- **Definition** — nodes are intents or steps; edges say which intents must be completed before others may run.
- **Acyclicity** — the graph must stay acyclic, or execution can loop forever; cycle detection at build time catches this.
- **Topological order** — valid execution follows a topological sort, giving a deterministic sequence that respects dependencies.
- **Parallelism** — independent branches of the DAG can run concurrently, cutting total completion time.
- **Failure handling** — when a node fails, dependent nodes are skipped or placed into a blocked state with clear reasons.
- **Composition** — subtasks can be nested as subgraphs, keeping the top-level DAG readable.
- **Common failure modes** — hidden cycles, missing edges that let steps run too early, and graphs that grow unmanageably.
- **Worked example** — a booking flow graphs identify-user before payment before confirmation; a cancellation intent depends on confirmation and cannot run first.
- **Practical relevance** — an intent DAG turns ad-hoc orchestration into a plan that is analyzable, schedulable, and safe.

- **Observability** — recording node start, end, and outcome per run makes DAG executions traceable and debuggable.
- **Retry semantics** — failed nodes may retry, but retry policies must not rerun expensive side effects more than once.
- **Validation gates** — each node can declare preconditions and postconditions, so the runtime verifies a step really satisfied its contract before successors run.
## Related
- [[wiki/agent-systems/goal-decomposition|Goal Decomposition]] — deriving steps
- [[wiki/agent-systems/agent-planning-systems|Agent Planning Systems]] — planning execution
- [[wiki/agent-systems/task-scheduling-agents|Task Scheduling for Agents]] — ordering work
- [[wiki/llm-agents/agentic-workflows|Agentic Workflows]] — chaining steps
- [[wiki/agent-systems/blackboard-architecture|Blackboard Architecture]] — coordinating experts
- [[wiki/ai-ml/query-decomposition|Query Decomposition]] — splitting queries
