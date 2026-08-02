---
type: "concept"
title: "Eval Contamination"
description: "Any leakage that corrupts evaluation validity"
tags: ["eval", "contamination", "evals"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Eval Contamination

## Summary
Eval contamination covers all ways evaluation validity is corrupted: leaked data, gamed metrics, or feedback loops from eval to training.

## Details
- Eval contamination covers all ways evaluation validity is corrupted: leaked data, gamed metrics, or feedback loops from eval to training.
- It is the Goodhart dynamic applied to benchmarks.
- Healthy eval practice treats contamination as a standing risk, not a one-time fix.
- RSIS3 relevance: the pass verifier is designed to be ungameable by the generator.

## Related
- [[wiki/concepts/benchmark-contamination|Benchmark Contamination]] — the specific form
- [[wiki/concepts/evals-gaming|Evals Gaming]] — the deliberate form
- [[wiki/concepts/train-test-contamination|Train-Test Contamination]] — the data form
- [[wiki/pulses/improvement-metrics|Improvement Metrics]] — the Goodhart context
- [[wiki/agent-systems/self-evaluation|Self-Evaluation]] — the full treatment of this theme
- [[wiki/ai-ml/data-contamination|Data Contamination]] — existing graph context
