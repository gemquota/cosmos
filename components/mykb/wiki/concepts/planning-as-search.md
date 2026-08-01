---
type: "concept"
title: "Planning as Search"
description: "Treating planning as a search problem over states and actions"
tags: ["planning", "search", "algorithms", "agents"]
timestamp: "2026-07-31T00:00:00Z"
status: "stub"
---

# Planning as Search

## Summary
Planning as search frames planning as searching a state space: nodes are states, edges are actions, and the plan is the path to a goal state. It matters because it imports the whole toolkit of search algorithms — BFS, A*, iterative deepening — into planning. It is the classical backbone of planning systems.

## Details
- Search strategies trade completeness, optimality, and memory.
- Heuristics (e.g., admissible estimates) make search practical.
- LLM planners use search over generated options rather than enumerated states.
- Open questions: learned heuristics for open-ended agent tasks.

## Related
- [[wiki/agent-systems/planning-systems|Planning Systems]] — the architecture that uses search
- [[wiki/concepts/means-ends-analysis|Means-Ends Analysis]] — a heuristic search strategy
- [[wiki/concepts/monte-carlo-tree-search|Monte Carlo Tree Search]] — sampling-based search
- [[wiki/concepts/forward-chaining|Forward Chaining]] — search forward from the start
- [[wiki/concepts/goal-regression|Goal Regression]] — search backward from the goal
