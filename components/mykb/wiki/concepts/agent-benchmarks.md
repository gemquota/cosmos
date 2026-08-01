---
type: "concept"
title: "Agent Benchmarks"
description: "Standardized task suites for comparing agent performance"
tags: ["benchmarks", "evaluation", "agents", "testing", "measurement"]
timestamp: "2026-07-31T00:00:00Z"
status: "growing"
source: ["https://arxiv.org/abs/2308.03688"]
---

# Agent Benchmarks

## Summary
Agent benchmarks are fixed environments and task sets used to measure and compare agents — from web navigation and coding to tool use and reasoning. They matter because agents must be evaluated on trajectories, not just final answers, and benchmarks provide the shared yardstick. AgentBench introduced a broad set of interactive environments for exactly this purpose.

## Details
- **Environments**: sandboxed worlds (shells, browsers, code repos) where agents act and receive observations.
- **Task design**: goals with objective success criteria, plus budgets and constraint checks.
- **Scoring**: success rate, efficiency, cost, and safety incidents; trajectories are audited, not just outcomes.
- **Limitations**: benchmarks overfit and age; results must be paired with live evaluation on real workflows.
- RSIS3 pairs benchmarks with its own pulse telemetry so improvements are measured in the field, not only in the lab.
- Worked example: an agent is run against 100 repository-fix tasks and scored on patch correctness and test pass rate.

## Related
- [[wiki/llm-agents/success-criteria|Success Criteria]] — the per-task objectives benchmarks encode
- [[wiki/llm-agents/traceability|Traceability]] — trajectory auditing under the hood
- [[wiki/llm-agents/agent-telemetry-schema|Agent Telemetry Schema]] — the measurements benchmarks collect
- [[wiki/concepts/calibration|Calibration]] — keeping benchmark claims honest
- [[wiki/ops/gap-report|Gap Analysis Report]] — where benchmark coverage is missing
- [[wiki/questions/open-questions|Open Questions]] — open problems in agent measurement
- [[wiki/concepts/mykb-analysis|Mykb Analysis]] — analysis methods for benchmark results
