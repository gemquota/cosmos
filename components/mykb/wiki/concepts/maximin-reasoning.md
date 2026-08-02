---
type: "concept"
title: "Maximin Reasoning"
description: "Choosing the option with the best worst-case outcome"
tags: ["maximin", "decision", "robustness"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Maximin Reasoning

## Summary
Maximin picks the action whose worst outcome is least bad, prioritizing robustness over average performance.

## Details
- Maximin picks the action whose worst outcome is least bad, prioritizing robustness over average performance.
- It is appropriate under deep uncertainty or catastrophic stakes.
- Critics note it can be paralyzed by implausible worst cases; calibration matters.
- RSIS3 relevance: fallback and rollback designs are maximin moves.

## Related
- [[wiki/concepts/worst-case-reasoning|Worst-Case Reasoning]] — the general stance
- [[wiki/concepts/expected-value-reasoning|Expected Value Reasoning]] — the contrast
- [[wiki/syntheses/fallback-plans|Fallback Plans]] — the applied form
- [[wiki/concepts/conservatism-ai|Conservatism in AI Design]] — the design stance
- [[wiki/concepts/mild-optimization|Mild Optimization]] — the full treatment of this theme
- [[wiki/concepts/calibration|Calibration]] — existing graph context
