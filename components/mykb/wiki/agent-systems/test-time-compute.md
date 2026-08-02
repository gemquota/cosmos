---
type: "concept"
title: "Test-Time Compute"
description: "Extra computation spent during inference to improve answers"
tags: ["test-time-compute", "inference", "reasoning", "scaling"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://arxiv.org/abs/2305.20050", "https://arxiv.org/abs/2305.10601"]
---

# Test-Time Compute

## Summary
Test-time compute is the budget of inference-time computation an agent spends beyond a single forward pass: chain-of-thought, tree search, verifier loops, and self-refinement. Scaling it has become a first-class axis of capability growth alongside parameters and data.

## Details
- **Forms** — CoT prompting, self-consistency voting, Tree of Thoughts, verifier-guided search, and iterative repair.
- **Evidence** — 'Let's Verify Step by Step' showed process supervision and verifier-guided search improve math reasoning under a compute budget.
- **Trade-off** — more compute buys accuracy up to a ceiling; returns diminish and costs grow.
- **Safety angle** — longer reasoning horizons increase both capability and the surface for hidden reasoning.
- **RSIS3 relevance** — reflection and refinement phases are test-time-compute decisions made by the pulse loop itself.

## Related
- [[wiki/agent-systems/inference-time-reasoning|Inference-Time Reasoning]] — the capability axis
- [[wiki/agent-systems/self-correction|Self-Correction]] — a compute-hungry loop
- [[wiki/llm-agents/self-consistency|Self-Consistency]] — voting variant
- [[wiki/agent-systems/hidden-reasoning|Hidden Reasoning]] — safety surface
- [[wiki/agent-systems/bounded-agents|Bounded Agents]] — budget discipline
- [[wiki/agent-systems/agent-loop|Agent Loop]] — where compute is spent
- [[wiki/pulses/self-evaluation-scores|Self-Evaluation Scores]] — self-scored telemetry
