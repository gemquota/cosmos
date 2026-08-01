---
type: "concept"
title: "Success Criteria"
description: "Verifiable conditions that define when a task is done correctly"
tags: ["success-criteria", "evaluation", "goals", "agents"]
timestamp: "2026-07-31T00:00:00Z"
status: "stub"
---

# Success Criteria

## Summary
Success criteria are the verifiable conditions a task must meet to count as done — tests pass, constraints respected, artifacts produced. They matter because agents optimize what they are checked against, and vague criteria invite both premature stops and reward hacking. They are the evaluation contract for a task.

## Details
- Should be objective, verifiable, and testable by the agent.
- Break large tasks into per-subgoal criteria.
- Poor criteria cause gaming; review them like code.
- Open questions: criteria synthesis for open-ended tasks.

## Related
- [[wiki/agent-systems/agent-evaluation|Agent Evaluation]] — the measurement of success
- [[wiki/llm-agents/stop-conditions|Stop Conditions]] — success as a stop condition
- [[wiki/concepts/agent-benchmarks|Agent Benchmarks]] — criteria at benchmark scale
- [[wiki/llm-agents/traceability|Traceability]] — verifying the evidence
- [[wiki/agent-systems/goal-decomposition|Goal Decomposition]] — criteria per subgoal
