---
type: "concept"
title: "Goal Regression"
description: "Planning backward from the goal to the initial state"
tags: ["goal-regression", "planning", "backward", "search"]
timestamp: "2026-07-31T00:00:00Z"
status: "stub"
---

# Goal Regression

## Summary
Goal regression plans backward: start from the goal conditions and find the last action that could produce them, regressing the goal through that action until reaching the initial state. It matters because backward search avoids irrelevant forward branches. It underlies STRIPS planning and partial-order planning.

## Details
- Regress: compute weakest preconditions of an action given the goal.
- Handles interacting subgoals cleanly via least-commitment.
- Symmetric complement to forward search in the same state space.
- Open questions: regression heuristics for LLM planning.

## Related
- [[wiki/agent-systems/planning-systems|Planning Systems]] — the planning family
- [[wiki/agent-systems/goal-decomposition|Goal Decomposition]] — goals split during regression
- [[wiki/concepts/backward-chaining|Backward Chaining]] — the logic-inference analog
- [[wiki/concepts/operator-subgoaling|Operator Subgoaling]] — precondition subgoals
- [[wiki/concepts/planning-as-search|Planning as Search]] — the search framing
