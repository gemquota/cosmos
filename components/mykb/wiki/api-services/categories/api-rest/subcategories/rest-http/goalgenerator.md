---
type: "entity"
title: "GoalGenerator"
description: "A component that produces goals for agents from context and constraints"
tags: ["entity", "goals", "agents", "generation", "planning"]
timestamp: "2026-07-19T22:41:42Z"
resource: ""
---

# GoalGenerator

## Summary

A goal generator is a component that produces agent goals from context: given the current situation, available capabilities, and constraints, it emits objectives the agent should pursue. It matters because goal quality determines everything downstream — planning, tool choice, and evaluation. Generators range from static templates to learned models that propose novel objectives.

## Details

- **Definition** — Goal generation converts a task request or environment state into explicit, structured goals that an agent can plan against.
- **Inputs** — Context, user intent, constraints, and success criteria feed the generator; the more precise the inputs, the more tractable the goals.
- **Output shape** — Goals may be plain text, typed goal objects, or nested trees with priorities and dependencies.
- **Worked example** — A research agent receives a question and budget; the generator produces a top-level goal, sub-goals per subtopic, and a verification goal.
- **Common failure modes** — Vague goals that leave planning ambiguous, contradictory goals that waste budget, and goal proliferation that fragments attention.
- **Practical relevance** — In Cosmos, goal generation interacts with goal decomposition and evaluation, so generated goals must be checkable.
- **Variants** — Template-based generators are predictable; LLM-based generators are flexible but need validation that outputs are realizable.
- **Telemetry note** — The stub pairs GoalGenerator with backend and API tags; the agent-goal reading matches the session context better than the Go-language tag.
- **Constraints** — Budget, deadline, and safety constraints should be part of generation so goals are born feasible rather than trimmed later.
- **Evaluation** — Generated goals are only useful if checkable; pairing each goal with success criteria makes downstream evaluation mechanical.
- **Worked example** — Given a user request and a tool list, the generator emits three candidate goals with priorities, and the planner selects one to expand.
- **Failure modes** — Generators can over-produce goals that exhaust context, or under-produce and miss the user's actual intent; both need review gates.

## Related

- [[wiki/agent-systems/goal-decomposition|Goal Decomposition]] — breaking goals into work
- [[wiki/agent-systems/goal-disclosure|Goal Disclosure]] — transparency about objectives
- [[wiki/api-services/categories/api-rest/subcategories/rest-http/goaltype|GoalType]] — the typed goal shapes
- [[wiki/llm-agents/success-criteria|Success Criteria]] — defining goal completion
- [[wiki/concepts/functional-instrumental-goals|Functional Instrumental Goals]] — means toward ends
- [[wiki/agent-systems/hidden-goals|Hidden Goals]] — undisclosed objectives
