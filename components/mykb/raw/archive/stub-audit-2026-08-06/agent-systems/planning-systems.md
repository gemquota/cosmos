---
type: "concept"
title: "Planning Systems"
description: "Architectures that separate the deliberation about what to do from the doing"
tags: ["planning", "architecture", "search", "agents", "llm"]
timestamp: "2026-07-31T00:00:00Z"
status: "growing"
source: ["https://arxiv.org/abs/2304.11477"]
---

# Planning Systems

## Summary
A planning system generates a course of action before (or while) executing it, typically as a sequence of steps or a search over candidate plans. It matters because planning converts hard search problems into executable action lists and gives agents foresight beyond greedy reaction. Modern systems often hybridize LLM heuristics with classical planners, as in LLM+P.

## Details
- **Plan-then-execute**: the plan is produced up front, then an executor follows it; replanning handles surprises.
- **Search-based planning**: planning-as-search explores a state space; means-ends analysis and goal regression are classical strategies.
- **Hierarchical planning** decomposes goals into subgoals (HTN) so planners scale to large tasks.
- LLM planners add common sense and flexibility; classical planners add soundness and optimality.
- RSIS3's executive planner sits between goals and the L1 loop, choosing sequences of tool actions and contingencies.
- Worked example: a deployment plan is generated, validated against constraints, then executed step by step with checkpoints.

## Related

- [[wiki/concepts/planning-as-search|Planning as Search]] — the search view of planning
- [[wiki/concepts/hierarchical-task-network|Hierarchical Task Network]] — decomposition-based planning
- [[wiki/concepts/goal-regression|Goal Regression]] — planning backward from the goal
- [[wiki/concepts/means-ends-analysis|Means-Ends Analysis]] — reducing differences between state and goal
- [[wiki/concepts/reactive-planning|Reactive Planning]] — the no-upfront-plan alternative
- [[wiki/ops/gap-report|Gap Analysis Report]] — planning gaps identified by evaluation
- [[wiki/syntheses/knowledge-system|Knowledge System Overview]] — how plans and outcomes become knowledge