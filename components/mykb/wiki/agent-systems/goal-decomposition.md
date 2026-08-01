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
Goal decomposition splits a vague objective into a graph of concrete subgoals that an agent can execute and verify. It matters because goals like 'improve the system' are unactionable; decomposed tasks with dependencies are not. Systems like HuggingGPT show LLMs decomposing tasks and dispatching them to specialists.

## Details
- **Decomposition**: the goal is parsed into subtasks, each with an owner, inputs, outputs, and success test.
- **Dependency ordering**: subtasks form a DAG; independent branches can run in parallel.
- **Verification per subgoal**: each one is checked before the next starts, catching drift early.
- **Recomposition**: subgoal results are merged into the final deliverable, with conflicts resolved at merge time.
- RSIS3's L3 self-direction generates goals, prioritizes them, and executes them through the L1 loop.
- Worked example: 'ship the dashboard' decomposes into telemetry schema, data endpoint, chart rendering, and deployment.

## Related

- [[wiki/concepts/hierarchical-task-network|Hierarchical Task Network]] — decomposition-based planning formalized
- [[wiki/concepts/goal-regression|Goal Regression]] — decomposing backward from the goal
- [[wiki/concepts/operator-subgoaling|Operator Subgoaling]] — creating subgoals to enable operators
- [[wiki/concepts/means-ends-analysis|Means-Ends Analysis]] — reducing the gap between state and goal
- [[wiki/ops/gap-report|Gap Analysis Report]] — decomposition gaps surfaced by pulse analysis
- [[wiki/syntheses/knowledge-system|Knowledge System Overview]] — knowledge that informs goal setting