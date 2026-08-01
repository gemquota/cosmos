---
type: "concept"
title: "Means-Ends Analysis"
description: "Reducing the difference between current state and goal step by step"
tags: ["means-ends-analysis", "planning", "search", "classical-ai"]
timestamp: "2026-07-31T00:00:00Z"
status: "stub"
---

# Means-Ends Analysis

## Summary
Means-ends analysis plans by measuring the difference between the current state and the goal, then choosing actions that reduce the largest difference, recursively handling subproblems. It matters because it is a canonical, human-like planning strategy — and the core of the classic STRIPS/GPS systems. Modern LLM planners echo it when they decompose obstacles.

## Details
- Loop: detect salient difference → find operator that reduces it → apply → recurse.
- Subgoals arise when an operator's preconditions are unmet.
- Trade-off: greedy difference-reduction can miss globally better orders.
- Open questions: reincarnating MEA in LLM planning heuristics.

## Related
- [[wiki/agent-systems/goal-decomposition|Goal Decomposition]] — differences become subgoals
- [[wiki/agent-systems/planning-systems|Planning Systems]] — the planning family
- [[wiki/concepts/operator-subgoaling|Operator Subgoaling]] — the subgoal mechanism it uses
- [[wiki/concepts/goal-regression|Goal Regression]] — the backward-looking cousin
- [[wiki/concepts/planning-as-search|Planning as Search]] — the search framing
