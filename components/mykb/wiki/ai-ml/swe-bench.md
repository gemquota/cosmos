---
type: "concept"
title: "SWE-bench"
description: "Benchmark that evaluates models on resolving real GitHub issues with full repositories"
tags: ["benchmarks", "code", "agents"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# SWE-bench

## Summary
Benchmark that evaluates models on resolving real GitHub issues with full repositories

## Details
- Each task pairs an issue report with a repository snapshot and failing tests.
- Measures end-to-end software engineering, not just codegen.
- Agent frameworks report SWE-bench scores as a headline metric.
- Hard because it requires navigation, reasoning, and testing.

## Related
- [[wiki/ai-ml/code-benchmarks|Code Benchmarks]] — code eval family
- [[wiki/agent-systems/code-repair-agents|Code Repair Agents]] — typical solver pattern
- [[wiki/testing/agent-evaluations|Agent Evaluations]] — agent-level scoring
- [[wiki/agent-systems/testing-agents|Testing Agents]] — test-first strategies
- [[wiki/testing/benchmark-design-agent-contracts|Benchmark Design and Agent Contracts]] — contract design
