---
type: "concept"
title: "Goal Regression"
description: "Planning backward from the goal to the initial state"
tags: ["goal-regression", "planning", "backward", "search"]
timestamp: "2026-07-31T00:00:00Z"
status: "growing"
---

# Goal Regression

## Summary
Goal regression plans backward: start from the goal conditions and find the last action that could produce them, regressing the goal through that action until reaching the initial state. It matters because backward search avoids irrelevant forward branches. It underlies STRIPS planning and partial-order planning.

## Details
- The core operation is regressing a condition through an action: given a condition C that must hold after action a, compute the weakest precondition of a with respect to C — the set of conditions that must hold before a so that C holds after. For a STRIPS action with add and delete lists, the regression is clean: delete C from the action's add effects and add back the action's preconditions, handling the case where the action adds C directly (then the precondition is just the action's own preconditions) versus where C is unaffected (then C must already hold before).
- The search proceeds from the goal state backwards through the space of states and actions until the initial state is reached, at which point the sequence of chosen actions is reversed to produce the plan. Because it works backward from the goal, it only ever considers actions that could actually contribute to a goal condition — the irrelevant-branch problem that plagues forward search disappears, since actions that do not affect any goal condition are never candidates.
- Handles interacting subgoals cleanly via least-commitment. When multiple goal conditions must hold together, naive backward search can plan each independently and discover conflicts late; partial-order planning defers ordering decisions, representing the plan as a set of steps with only the necessary ordering constraints, and only commits to an order when forced by threat resolution. This makes goal regression the natural foundation for planners that must handle goals whose subgoals interfere.
- The theoretical relation: backward and forward search explore the same state space from opposite ends, and their efficiency depends on branching factors — regression wins when there are fewer actions relevant to goals than there are actions applicable to states, which is typical in richly populated domains.
- Failure modes: regression can generate infinitely many preconditions without good heuristic guidance, and the least-commitment style can postpone conflicts until the plan is nearly complete. Open question: how LLM-based planners can use regression-style thinking to prune their action search.
- RSIS3 relevance: an improvement pass that starts from the desired outcome ("telemetry complete, constraints satisfied") and works backward to the minimal set of changes is goal regression applied to self-improvement.

## Related
- [[wiki/agent-systems/agent-planning-systems|Agent Planning Systems]] — the planning family
- [[wiki/agent-systems/goal-decomposition|Goal Decomposition]] — goals split during regression
- [[wiki/concepts/backward-chaining|Backward Chaining]] — the logic-inference analog
- [[wiki/concepts/operator-subgoaling|Operator Subgoaling]] — precondition subgoals
- [[wiki/concepts/planning-as-search|Planning as Search]] — the search framing
