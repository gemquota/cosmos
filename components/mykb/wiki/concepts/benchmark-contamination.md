---
type: "concept"
title: "Benchmark Contamination"
description: "Benchmark data leaking into training corpora"
tags: ["benchmark", "contamination", "evals"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Benchmark Contamination

## Summary
Benchmark contamination is the presence of benchmark examples in training data, inflating leaderboard scores.

## Details
- Benchmark contamination is the presence of benchmark examples in training data, inflating leaderboard scores.
- LLM-scale web corpora make it near-inevitable for public benchmarks.
- Mitigations: hidden benchmarks, contamination audits, and reporting per-sample provenance.
- RSIS3 relevance: graph-health metrics are 'contaminated' if the checker and generator share assumptions.

## Related
- [[wiki/concepts/eval-contamination|Eval Contamination]] — the umbrella
- [[wiki/concepts/train-test-contamination|Train-Test Contamination]] — the mechanism
- [[wiki/concepts/evals-gaming|Evals Gaming]] — the deliberate form
- [[wiki/decisions/test-set-discipline|Test Set Discipline]] — the norm
- [[wiki/agent-systems/self-evaluation|Self-Evaluation]] — the full treatment of this theme
- [[wiki/ai-ml/data-contamination|Data Contamination]] — existing graph context
