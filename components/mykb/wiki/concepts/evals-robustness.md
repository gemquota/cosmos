---
type: "concept"
title: "Evals Robustness"
description: "Making evaluations resistant to gaming and error"
tags: ["evals", "robustness", "integrity"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Evals Robustness

## Summary
Evals robustness is the property that evaluation results survive adversarial pressure and honest variation.

## Details
- Evals robustness is the property that evaluation results survive adversarial pressure and honest variation.
- Techniques: hidden splits, diverse tasks, and result auditing.
- Fragile evals create fake safety signals.
- RSIS3 relevance: the pass verifier is designed to be robust to generator gaming.

## Related
- [[wiki/concepts/evals-gaming|Evals Gaming]] — the threat
- [[wiki/decisions/test-set-discipline|Test Set Discipline]] — the hygiene
- [[wiki/concepts/benchmark-contamination|Benchmark Contamination]] — the leak
- [[wiki/concepts/safety-evals-practice|Safety Evals Practice]] — the practice
- [[wiki/agent-systems/self-evaluation|Self-Evaluation]] — the full treatment of this theme
- [[wiki/testing/ai-safety-evals|Ai Safety Evals]] — existing graph context
