---
type: "concept"
title: "Feature Double-Counting"
description: "The same concept appearing as multiple separate features"
tags: ["features", "sae", "interpretability"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Feature Double-Counting

## Summary
Feature double-counting is when a concept is split across several dictionary features, so the decomposition over-counts it.

## Details
- Feature double-counting is when a concept is split across several dictionary features, so the decomposition over-counts it.
- It distorts interpretability claims and any downstream use of feature attributions.
- Detection and merging of duplicate features is an open research problem.
- RSIS3 relevance: duplicate graph nodes are the knowledge-graph analogue.

## Related
- [[wiki/concepts/sae-research|SAE Research]] — where it is observed
- [[wiki/concepts/dictionary-learning-ai|Dictionary Learning for AI]] — the framework
- [[wiki/syntheses/orphan-detection|Orphan Detection]] — graph analogue
- [[wiki/concepts/activation-analysis|activation-analysis]] — the distortion risk
- [[wiki/ai-ml/sparse-autoencoders|Sparse Autoencoders]] — existing graph context
