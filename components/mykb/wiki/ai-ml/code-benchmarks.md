---
type: "concept"
title: "Code Benchmarks"
description: "Evaluation suites measuring model performance on programming tasks"
tags: ["code", "evaluation", "benchmarks"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Code Benchmarks

## Summary
Code benchmarks measure model performance on programming tasks, from short function generation to repository-scale repairs. They matter because coding is one of the highest-value model capabilities and a strong proxy for agentic tool use. Benchmark design directly shapes how coding agents are trained and evaluated. Code benchmarks measure what models can build when the tests are honest.

## Details
- **Definition** — a code benchmark presents programming problems and scores solutions by execution against hidden tests, not just textual similarity.
- **Suites** — popular suites include HumanEval, MBPP, LiveCodeBench, and repository-scale tasks like swe-bench that require real-world changes.
- **Task coverage** — benchmarks span generation, repair, test generation, and explanation, reflecting the breadth of developer work.
- **Sampling metrics** — pass@k rewards generating multiple candidate solutions and succeeding within k attempts, capturing the value of sampling.
- **Agentic signal** — strong code ability correlates with effective tool use, making code benchmarks a leading indicator for agent capability.
- **Worked example** — a team evaluates a repair agent on a repository suite, measuring how many failing issues receive test-passing patches.
- **Failure modes** — test leakage, benchmark contamination, and tasks that underrepresent real engineering context distort scores.
- **Practical relevance** — code benchmarks drive code-generation-agents and code-repair-agents development and track the model-capabilities-frontier.
- **Hidden tests** — execution against held-out tests prevents overfitting to visible cases.
- **Repo realism** — repository-scale tasks capture the context and tooling of real development.
- **Worked example** — a benchmark run counts how many issues a repair agent resolves with tests passing.
- **Failure example** — a benchmark with weak hidden tests over-rewards memorized solutions.
- **Usage note** — benchmark results should be reported with pass@1 and pass@k together, since they measure different deployment strategies.

## Related
- [[wiki/ai-ml/swe-bench|SWE-bench]] — the real-world repository benchmark
- [[wiki/agent-systems/code-generation-agents-revisited|Code Generation Agents]] — agentic code tasks
- [[wiki/agent-systems/code-repair-agents|Code Repair Agents]] — repair evaluation
- [[wiki/agent-systems/testing-agents|Testing Agents]] — test generation evaluation
- [[wiki/ai-ml/model-capabilities-frontier|Model Capabilities Frontier]] — capability tracking
