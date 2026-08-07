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

- **Evidence summary** — LLMs correct code and constraint-satisfying outputs well when given compiler or test feedback, but self-correction of open-ended reasoning without external signal is unreliable.
- **Architecture** — generate, check with an external verifier (tests, compiler, retrieved ground truth), repair, re-check; terminate on pass, budget exhaustion, or no-progress detection.
- **Budget discipline** — each repair iteration costs compute; a no-progress detector (same error twice) stops the loop earlier than a fixed iteration cap alone.
- **Role split** — correction quality improves when the generator and the checker are distinct (different models, or a tool-grounded verifier) rather than the same model judging itself.

- **Safety implication** — an agent that cannot correct its own errors accumulates them; correction capability is therefore a safety property, and its absence should be treated as a deployment risk rather than a quality quirk.

## Related
- [[wiki/agent-systems/self-critique|Self-Critique]] — the critique input
- [[wiki/agent-systems/test-time-compute|Test-Time Compute]] — the resource correction spends
- [[wiki/agent-systems/scaffold-loops|Scaffold Loops]] — tool-grounded correction
- [[wiki/decisions/checkpoint-selection|Checkpoint Selection]] — choosing which state to keep
- [[wiki/concepts/immutable-evaluator|Immutable Evaluator]] — the anchor that makes correction sound
- [[wiki/agent-systems/retry-strategies|Retry Strategies]] — retry policy
- [[wiki/pulses/self-evaluation-scores|Self-Evaluation Scores]] — self-scored telemetry
