---
type: "concept"
title: "Quantilizers"
description: "Optimizers that sample from the top quantile instead of the max"
tags: ["quantilizers", "optimization", "theory"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Quantilizers

## Summary
A quantilizer chooses randomly among actions in the top q-quantile of expected value rather than taking the argmax.

## Details
- A quantilizer chooses randomly among actions in the top q-quantile of expected value rather than taking the argmax.
- Randomization bounds worst-case performance loss while preserving most gains.
- Quantilization is a formal candidate for mild optimization.
- RSIS3 relevance: sampling among passing configurations is a quantilizer pattern.

## Related
- [[wiki/concepts/mild-optimization|Mild Optimization]] — the motivation
- [[wiki/concepts/quantilizer-concepts|Quantilizer Concepts]] — the variations
- [[wiki/concepts/bounded-optimization|Bounded Optimization]] — the family
- [[wiki/concepts/satisficing-research|Satisficing Research]] — the relative
- [[wiki/concepts/utility-functions|Utility Functions]] — existing graph context
