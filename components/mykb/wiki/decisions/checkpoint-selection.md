---
type: "decision"
title: "Checkpoint Selection"
description: "Choosing which training states to keep and use"
tags: ["checkpoints", "training", "selection"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Checkpoint Selection

## Summary
Checkpoint selection decides which saved model states to evaluate, keep, and deploy.

## Details
- Checkpoint selection decides which saved model states to evaluate, keep, and deploy.
- Selection by validation metrics is standard; selection by downstream evals is safer.
- Bad selection ships overfit or contaminated checkpoints.
- RSIS3 relevance: choosing which pass snapshot to consolidate is checkpoint selection.

## Related
- [[wiki/concepts/early-stopping|Early Stopping]] — the timing decision
- [[wiki/decisions/model-selection-practice|Model Selection in Practice]] — the broader choice
- [[wiki/concepts/checkpoint-rollback|Checkpoint & Rollback]] — the rollback twin
- [[wiki/decisions/eval-splits|Eval Splits]] — the evaluation basis
- [[wiki/concepts/continual-self-improvement|Continual Self-Improvement]] — the full treatment of this theme
