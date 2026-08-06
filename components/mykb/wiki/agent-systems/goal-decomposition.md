---
type: "concept"
title: "Goal Decomposition"
description: "Breaking a high-level goal into ordered, executable subgoals"
tags: ["goals", "decomposition", "planning", "hierarchical", "agents"]
timestamp: "2026-07-31T00:00:00Z"
status: "growing"
source: ["https://arxiv.org/abs/2303.17580"]
---

# Goal Decomposition

## Summary
Goal decomposition splits a vague objective into a graph of concrete subgoals that an agent can execute and verify. It matters because goals like "improve the system" are unactionable; decomposed tasks with dependencies and success tests are not. Systems like HuggingGPT show LLMs decomposing tasks and dispatching them to specialists.

## Details
- **Decomposition** — the goal is parsed into subtasks, each with an owner, inputs, outputs, and a success test; a subgoal without a success test is not actually decomposed.
- **Dependency ordering** — subtasks form a DAG; independent branches run in parallel, dependent ones wait, and the ordering is re-checked when a branch changes.
- **Verification per subgoal** — each subgoal is checked before the next starts, catching drift early and keeping a failure localized.
- **Recomposition** — subgoal results are merged into the final deliverable, with conflicts resolved at merge time against the original goal.
- **Depth and granularity** — decomposition depth is set by the executor's capability: too coarse leaves unactionable steps, too fine multiplies coordination overhead.
- **RSIS3 relevance** — the L3 self-direction layer generates goals, prioritizes them, and executes them through the L1 loop; decomposition is the bridge between the two.
- **Worked example** — "ship the dashboard" decomposes into telemetry schema, data endpoint, chart rendering, and deployment, each with a verification step and a dependency order.
- **Failure modes** — forgotten dependencies, subgoals that no longer serve the parent goal, and decomposed tasks that are still too vague to execute.

- **Traceability** — each subgoal records which part of the parent goal it serves, so a drift in scope is visible when a subgoal no longer maps to the original objective.
## Related
- [[wiki/concepts/hierarchical-task-network|Hierarchical Task Network]] — decomposition-based planning formalized
- [[wiki/concepts/goal-regression|Goal Regression]] — decomposing backward from the goal
- [[wiki/concepts/operator-subgoaling|Operator Subgoaling]] — creating subgoals to enable operators
- [[wiki/concepts/means-ends-analysis|Means-Ends Analysis]] — reducing the gap between state and goal
- [[wiki/agent-systems/agent-planning-systems|Agent Planning Systems]] — planning with decomposed goals
- [[wiki/agent-systems/goal-disclosure|Goal Disclosure]] — making goals checkable
