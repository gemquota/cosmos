---
type: "concept"
title: "Agent Evaluation"
description: "Measuring whether an agent behaves correctly, efficiently, and safely"
tags: ["evaluation", "benchmarks", "testing", "agents", "telemetry"]
timestamp: "2026-07-31T00:00:00Z"
status: "growing"
source: ["https://github.com/openai/evals"]
---

# Agent Evaluation

## Summary
Agent evaluation is the discipline of scoring agent behavior against datasets, tasks, and guardrails rather than trusting vibes. It matters because agents are stochastic and tool-driven: a single correct answer can hide wasted steps, rule violations, or lucky shortcuts. RSIS3 treats evaluation as a gate — no change ships unless tests pass and telemetry confirms the intended behavior.

## Details
- **Metric layers**: task success, tool-call correctness, cost and latency, safety incidents, and calibration of the agent's own confidence.
- **Harness design**: fixed task sets with gold answers (like OpenAI Evals), environment rollouts, and adversarial probes.
- **Trajectory evaluation** matters as much as outcome: right answer via forbidden action should fail.
- RSIS3 uses pulse success rate as a headline telemetry metric and gates mutations on test suites.
- Worked example: a refactor agent is evaluated on diff quality, test pass rate, and whether it touched out-of-scope files.
- Evaluation data feeds back into mykb gap analysis to target weak areas.

## Related
- [[wiki/llm-agents/success-criteria|Success Criteria]] — the per-task targets evaluation checks
- [[wiki/llm-agents/traceability|Traceability]] — linking outcomes back to actions for blame
- [[wiki/concepts/calibration|Calibration]] — evaluating the agent's confidence as a signal
- [[wiki/concepts/agent-benchmarks|Agent Benchmarks]] — standardized suites used for comparison
- [[wiki/ops/gap-report|Gap Analysis Report]] — identifies what evaluation is not covering
- [[wiki/questions/open-questions|Open Questions]] — unresolved evaluation questions
- [[wiki/concepts/mykb-analysis|Mykb Analysis]] — analysis techniques applied to agent telemetry
