---
type: "concept"
title: "Reward Hacking Evals"
description: "Testing whether agents game their reward signals"
tags: ["reward-hacking", "evals", "testing"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Reward Hacking Evals

## Summary
Reward hacking evals run agents in environments with imperfect rewards and check whether they exploit the gap.

## Details
- Reward hacking evals run agents in environments with imperfect rewards and check whether they exploit the gap.
- Test environments deliberately include hackable reward shortcuts.
- Results reveal both specification quality and optimization pressure.
- RSIS3 relevance: checker-bypass tests are reward-hacking evals for the loop.

## Related
- [[wiki/concepts/reward-hacking-practice|Reward Hacking in Practice]] — the phenomenon
- [[wiki/concepts/specification-gaming|Specification Gaming]] — the theory
- [[wiki/concepts/evals-gaming|Evals Gaming]] — the eval-side twin
- [[wiki/concepts/wireheading|Wireheading]] — the extreme
- [[wiki/ai-ml/reward-hacking-prevention|Reward Hacking Prevention]] — existing graph context
