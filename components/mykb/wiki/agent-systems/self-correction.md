---
type: "concept"
title: "Self-Correction"
description: "An agent repairing its own errors, with or without external feedback"
tags: ["self-correction", "reflection", "llm", "agents"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://arxiv.org/abs/2310.01798", "https://arxiv.org/abs/2303.11366"]
---

# Self-Correction

## Summary
Self-correction is an agent's ability to fix its own mistakes — from syntax errors after a test run to revised plans after a failed step. The 2023 finding that LLMs cannot reliably self-correct reasoning without external feedback reframed the field toward verifier- or tool-grounded correction.

## Details
- **External vs internal feedback** — correction with a compiler, test suite, or retrieved answer works; 'introspective' correction on open reasoning tasks often does not.
- **Architecture** — generate, check (external tool or verifier), repair, re-check; the loop terminates on pass or budget.
- **Relation to critique** — self-correction consumes self-critique but needs a ground-truth anchor to be trustworthy.
- **Cost** — each iteration spends test-time compute; scheduling is an optimization problem.
- **RSIS3 parallel** — check-practices + git rollback is a self-correction loop with a hard external gate (tests must pass).

## Related
- [[wiki/agent-systems/self-critique|Self-Critique]] — the critique input
- [[wiki/agent-systems/test-time-compute|Test-Time Compute]] — the resource correction spends
- [[wiki/agent-systems/scaffold-loops|Scaffold Loops]] — tool-grounded correction
- [[wiki/decisions/checkpoint-selection|Checkpoint Selection]] — choosing which state to keep
- [[wiki/concepts/immutable-evaluator|Immutable Evaluator]] — the anchor that makes correction sound
- [[wiki/agent-systems/retry-strategies|Retry Strategies]] — retry policy
- [[wiki/pulses/self-evaluation-scores|Self-Evaluation Scores]] — self-scored telemetry
