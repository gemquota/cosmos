---
type: "concept"
title: "Self-Benchmarking"
description: "Running internal benchmarks to measure one's own capability"
tags: ["benchmarks", "self-evaluation", "measurement"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Self-Benchmarking

## Summary
Self-benchmarking is a system measuring itself against curated tasks before, during, and after changes.

## Details
- Self-benchmarking is a system measuring itself against curated tasks before, during, and after changes.
- It differs from external benchmarking in that the system may influence the benchmark's contents (contamination risk).
- Frozen benchmark sets catch regressions; fresh sets catch overfitting to the frozen ones.
- RSIS3 relevance: check-practices acts as the workspace's internal benchmark suite.

## Related
- [[wiki/agent-systems/self-evaluation|Self-Evaluation]] — the scoring layer
- [[wiki/concepts/benchmark-contamination|Benchmark Contamination]] — the risk
- [[wiki/decisions/eval-splits|Eval Splits]] — keeping benchmarks clean
- [[wiki/decisions/test-set-discipline|Test Set Discipline]] — frozen discipline
- [[wiki/agent-systems/agent-evaluation|Agent Evaluation]] — existing graph context
