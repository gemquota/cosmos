---
type: "concept"
title: "Bounded Agents"
description: "Agents designed with explicit limits on resources, impact, and authority"
tags: ["bounded", "agents", "limits", "safety"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://en.wikipedia.org/wiki/Bounded_rationality", "https://en.wikipedia.org/wiki/Satisficing"]
---

# Bounded Agents

## Summary
A bounded agent operates under explicit caps: compute budgets, action horizons, scope restrictions, and approval requirements. Bounds are a safety feature — they make an agent's worst case small and its behavior predictable — and a realism feature, since real agents face resource limits anyway.

## Details
- **Kinds of bounds** — compute (test-time budget), horizon (plan depth), scope (allowed actions), and impact (world-change caps).
- **Why bounds help safety** — a bounded optimizer cannot 'optimize everything'; mild optimization and satisficing are objective-level bounds.
- **Design tension** — bounds that are too tight cripple capability; adaptive bounds (raise after verification) preserve both.
- **Relation to bounded rationality** — classical study of decision-making under resource limits informs agent design.
- **RSIS3 relevance** — scope discipline (write only your files, no git, no shared-dir edits) is a bound on the acquisition workers.

## Related
- [[wiki/agent-systems/satisficing-agents|Satisficing Agents]] — stop-when-good-enough bound
- [[wiki/concepts/mild-optimization|Mild Optimization]] — objective-level bound
- [[wiki/concepts/bounded-rationality|Bounded Rationality]] — cognitive limits
- [[wiki/agent-systems/approval-based-agents|Approval-Based Agents]] — authority bound
- [[wiki/agent-systems/test-time-compute|Test-Time Compute]] — compute bound
- [[wiki/agent-systems/risk-bounded-agents|Risk-Bounded Agents]] — risk budgets
- [[wiki/pulses/self-evaluation-scores|Self-Evaluation Scores]] — self-scored telemetry
- [[wiki/pulses/self-benchmarking|Self-Benchmarking]] — internal benchmarks
