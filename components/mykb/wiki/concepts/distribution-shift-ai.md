---
type: "concept"
title: "Distribution Shift in AI"
description: "Deployment data differing from training data"
tags: ["distribution-shift", "generalization", "deployment"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Distribution Shift in AI

## Summary
Distribution shift is the mismatch between the data a model saw in training and the data it meets in deployment.

## Details
- Distribution shift is the mismatch between the data a model saw in training and the data it meets in deployment.
- It is the rule, not the exception, and the main source of performance degradation.
- Mitigations: robust training, monitoring, and evals on shifted data.
- RSIS3 relevance: graph queries outside curated topics are distribution shift for the wiki.

## Related
- [[wiki/concepts/out-of-distribution|Out-of-Distribution]] — the test regime
- [[wiki/concepts/distributional-robustness|Distributional Robustness]] — the property
- [[wiki/concepts/brittleness-ai|AI Brittleness]] — the failure mode
- [[wiki/syntheses/monitored-deployment|Monitored Deployment]] — the operational response
- [[wiki/concepts/goal-misgeneralization|Goal Misgeneralization]] — the full treatment of this theme
- [[wiki/agent-systems/agent-evaluation|Agent Evaluation]] — existing graph context
