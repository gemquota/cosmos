---
type: "entity"
title: "GoalType"
description: "A typed taxonomy of goals that agents can represent and act on"
tags: ["entity", "goals", "types", "agents", "planning"]
timestamp: "2026-07-19T22:41:42Z"
resource: ""
---

# GoalType

## Summary

GoalType is a typed taxonomy of goals: a schema that classifies objectives by kind — completion, exploration, constraint satisfaction, or instrumental — so agents can plan and compare them uniformly. Typed goals matter because structure enables automation: validation, decomposition, and evaluation all become mechanical. The taxonomy also exposes conflicts between goal kinds early.

## Details

- **Definition** — Goal types attach structured metadata — kind, priority, deadline, and acceptance criteria — to objectives so planning code can handle them generically.
- **Common types** — Achievement goals name a target state; maintenance goals preserve a condition; exploration goals gather information; instrumental goals serve higher goals.
- **Why typing helps** — A typed goal supports checks a string cannot: is it measurable, does it conflict, is it decomposable, and when is it satisfied?
- **Worked example** — An agent represents a goal as type completion with a deadline and a check function; the planner routes it differently than an exploration goal.
- **Common failure modes** — Types so coarse they fit nothing, so fine they fragment into one-offs, and semantics that drift between components.
- **Practical relevance** — In Cosmos, goal types pair with goal generation and decomposition, making the type system a shared contract across loops.
- **Variants** — Enum-based types are simplest; discriminated unions and schemas allow richer validation at boundaries.
- **Telemetry note** — Recorded alongside GoalGenerator in backend sessions; this note fixes the misleading Go-language tag in favor of the goal-domain reading.
- **Validation** — Schema-validated goal objects reject malformed definitions early, keeping planners and evaluators free of defensive parsing.
- **Evolution** — Adding a new goal type is a contract change: all consumers must handle it, so type additions need migration and rollout care.
- **Worked example** — A planner receives a maintenance goal, checks its condition function each step, and reports satisfaction when the invariant holds for a full window.

## Related

- [[wiki/api-services/categories/api-rest/subcategories/rest-http/goalgenerator|GoalGenerator]] — producing typed goals
- [[wiki/agent-systems/goal-decomposition|Goal Decomposition]] — splitting goals by type
- [[wiki/llm-agents/success-criteria|Success Criteria]] — typing completion
- [[wiki/concepts/functional-instrumental-goals|Functional Instrumental Goals]] — instrumental goal kind
- [[wiki/agent-systems/goal-locking|Goal Locking]] — immutable goal commitments
- [[wiki/api-protocols/json-schema|JSON Schema]] — schema-validated goal payloads
