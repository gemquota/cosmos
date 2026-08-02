---
type: "concept"
title: "Agent Testing Strategies"
description: "Testing agents across unit, integration, simulation, and production levels"
tags: ["agents", "testing", "evaluation", "quality"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://arxiv.org/abs/2308.08155", "https://arxiv.org/abs/2310.06770"]
---

# Agent Testing Strategies

## Summary
Agent testing validates behavior at multiple levels: prompt/unit tests, tool integration tests, scenario simulations, and production canaries. Agents are stochastic, so tests assert on distributions and invariants rather than exact outputs. The goal is confidence that an agent change improves, not regresses, real behavior.

## Details
- **Levels** — unit tests on isolated decisions, integration tests on tool contracts, scenario tests on full runs, and shadow/canary tests in production.
- **Assertion styles** — golden outputs, rubrics, LLM-as-judge scoring, and invariant checks (no double payment, correct schema).
- **Determinism** — seeding and deterministic replay make flaky agent tests debuggable; nondeterminism itself is tested with variance runs.
- **Worked example** — a coding agent's test suite runs three attempts per scenario, asserting the final diff applies and tests pass, and fails if the agent loops.
- **Tooling** — evals harnesses, agent benchmarks like SWE-bench, and simulation environments with injected faults.
- **mykb relevance** — mykb documents testing agents and offline agent testing; RSIS3 already gates its own changes with full-loop tests.

## Related
- [[wiki/testing/agent-evaluations|Agent Evaluations]] — evaluating agent behavior
- [[wiki/agent-systems/offline-agent-testing|Offline Agent Testing]] — testing without live services
- [[wiki/agent-systems/simulation-environments-agents|Simulation Environments for Agents]] — scenario sandboxes
- [[wiki/testing/golden-test-sets|Golden Test Sets]] — golden scenarios
- [[wiki/agent-systems/shadow-mode-evaluation|Shadow Mode Evaluation]] — testing in production shadows
- [[wiki/concepts/agent-benchmarks|Agent Benchmarks]] — benchmark suites for agents
- [[wiki/syntheses/knowledge-system|Knowledge System Overview]] — the KB loop this work feeds
- [[wiki/concepts/triad-architecture|Triad Architecture]] — the RSIS3/mykb architecture it serves
