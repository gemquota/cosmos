---
type: "concept"
title: "Shortcut Learning"
description: "Models solving tasks via spurious easy features"
tags: ["shortcut-learning", "generalization", "bias"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Shortcut Learning

## Summary
Shortcut learning is models exploiting superficial cues that correlate with labels but not the underlying task.

## Details
- Shortcut learning is models exploiting superficial cues that correlate with labels but not the underlying task.
- Classic cases: snow backgrounds for wolves, watermark artifacts in medical images.
- Shortcut models fail on data without the cue — the usual real-world case.
- RSIS3 relevance: the graph's topic classifiers can shortcut on formatting rather than meaning.

## Related
- [[wiki/concepts/spurious-correlations|Spurious Correlations]] — the statistical form
- [[wiki/concepts/simplicity-bias|Simplicity Bias]] — the learning bias
- [[wiki/concepts/confounder-learning|Confounder Learning]] — the causal form
- [[wiki/concepts/robustness-training|Robustness Training]] — the countermeasure
- [[wiki/concepts/goal-misgeneralization|Goal Misgeneralization]] — the full treatment of this theme
- [[wiki/agent-systems/agent-evaluation|Agent Evaluation]] — existing graph context
