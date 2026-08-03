---
type: "concept"
title: "Planning as Search"
description: "Treating planning as a search problem over states and actions"
tags: ["planning", "search", "algorithms", "agents"]
timestamp: "2026-07-31T00:00:00Z"
status: "growing"
---

# Planning as Search

## Summary
Planning as search frames planning as searching a state space: nodes are states, edges are actions, and the plan is the path to a goal state. It matters because it imports the whole toolkit of search algorithms — BFS, A*, iterative deepening — into planning. It is the classical backbone of planning systems.

## Details
- The mapping is direct: the initial state is the start node, goal states are target nodes, each action is an edge to a successor state, and a plan is a path from start to goal. Once the problem is framed this way, every search algorithm becomes a planning algorithm, and the theory of search — completeness, optimality, complexity — applies to planning directly. This unification is why classical planning (STRIPS-style) is studied as state-space search: the domain may be symbolic, but the structure is a graph.
- Search strategies trade completeness, optimality, and memory. Breadth-first search is complete and finds shortest paths but explodes in memory; depth-first search uses little memory but can wander into infinite branches; iterative deepening gets BFS's optimality with DFS's memory; bidirectional search meets in the middle when both the start and goal are known. The choice is an engineering decision about which property matters most for the task, and every planner is a bet on that tradeoff.
- Heuristics (e.g., admissible estimates) make search practical. A heuristic estimates the remaining distance from a state to the goal, and A* uses it to focus the search: admissible heuristics (never overestimating) guarantee optimality while exploring far fewer nodes than blind search. In planning, admissible heuristics are derived automatically from problem relaxations — ignoring delete effects or solving subgoals independently — which is how modern planners handle large state spaces. The catch is that heuristics are domain engineering: a good one requires understanding the structure of the problem.
- LLM planners use search over generated options rather than enumerated states. Language models cannot enumerate the state space, so they use the same search skeleton at a coarser granularity — generate candidate plan steps, evaluate them, branch on the promising ones (tree-of-thought, MCTS with LLM policies) — which trades the classical guarantees for coverage of open-ended domains.
- Failure modes: state-space explosion when actions compose, heuristics that mislead (overestimating or deceptive), and goal specifications that omit what must not change — search finds the path, but the path can wreck the world if side effects are not modeled.
- Open question: learned heuristics for open-ended agent tasks — replacing hand-authored relaxations with heuristics learned from experience.
- RSIS3 relevance: an improvement pass that enumerates candidate changes, evaluates their predicted effect, and picks the best path to a target state is planning as search over the space of passes.

## Related
- [[wiki/agent-systems/planning-systems|Planning Systems]] — the architecture that uses search
- [[wiki/concepts/means-ends-analysis|Means-Ends Analysis]] — a heuristic search strategy
- [[wiki/concepts/monte-carlo-tree-search|Monte Carlo Tree Search]] — sampling-based search
- [[wiki/concepts/forward-chaining|Forward Chaining]] — search forward from the start
- [[wiki/concepts/goal-regression|Goal Regression]] — search backward from the goal
