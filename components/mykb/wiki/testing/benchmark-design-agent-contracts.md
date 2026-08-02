---
type: "concept"
title: "Benchmark Design and Agent Contracts"
description: "Designing evaluation benchmarks and agent contracts so agent behavior can be measured fairly"
tags: ["benchmarks", "agents", "contracts", "evaluation"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://arxiv.org/abs/2308.08155", "https://arxiv.org/abs/2210.03629"]
---

# Benchmark Design and Agent Contracts

## Summary
Agent contracts define the observable inputs, allowed actions, success criteria, and failure modes of an agent evaluation. They matter because agent tasks are open-ended: without a contract, scoring is subjective and regressions are invisible. Good contracts make benchmarks reproducible and results comparable across teams.

## Details
- **Contract elements** — task specification, initial state, tool allowlist, budget, success metric, and termination conditions.
- **Scoring levels** — outcome success (did it finish), process quality (did it use tools well), and safety (did it avoid forbidden actions).
- **Worked example** — a SWE-bench-style task: repo snapshot, issue text, test harness, time budget, and a required patch that passes hidden tests.
- **Common failure** — benchmark overfitting, where agents tuned to the eval do not generalize to real work.
- **mykb relevance** — RSIS3 evaluations should be contract-first so knowledge-quality changes are measured, not vibes.
- **Reproducibility** — pin model versions, seeds, and environment snapshots so reruns are comparable; contracts make that possible.
- **Human baselines** — calibrating task difficulty against expert performance separates meaningful benchmarks from trivia.

## Related
- [[wiki/testing/agent-evaluations|Agent Evaluations]] — scoring agents against contracts
- [[wiki/testing/evals-harness|Evals Harness]] — running contract evals at scale
- [[wiki/agent-systems/agent-testing-strategies|Agent Testing Strategies]] — testing umbrella
- [[wiki/ai-ml/specification-gaming-goodharts-law|Specification Gaming and Goodhart's Law]] — why metrics get gamed
- [[wiki/ai-ml/swe-bench|SWE-bench]] — example contract suite
- [[wiki/concepts/agent-benchmarks|Agent Benchmarks]] — related concept in this cluster
- [[wiki/ai-ml/scaling-laws|Scaling Laws]] — capability scaling context
- [[wiki/concepts/calibration|Calibration]] — calibration anchor in the KB
