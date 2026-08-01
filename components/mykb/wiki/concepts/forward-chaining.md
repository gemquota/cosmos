---
type: "concept"
title: "Forward Chaining"
description: "Reasoning from known facts toward a goal by applying rules"
tags: ["forward-chaining", "reasoning", "inference", "rules"]
timestamp: "2026-07-31T00:00:00Z"
status: "stub"
---

# Forward Chaining

## Summary
Forward chaining starts with known facts and repeatedly applies rules whose conditions are satisfied, deriving new facts until the goal is reached or no rule applies. It matters because it is complete, data-driven, and easy to implement — the engine of many expert systems. It is also how agents can reason from observations.

## Details
- Data-driven: all rules fire as their conditions become true.
- Used in production-rule systems and RETE-based engines.
- Contrast with backward chaining, which is goal-driven.
- Open questions: scaling forward chaining with learned rules.

## Related
- [[wiki/agent-systems/action-observation-loop|Action-Observation Loop]] — observations feed forward reasoning
- [[wiki/concepts/production-rules|Production Rules]] — the rule formalism
- [[wiki/concepts/backward-chaining|Backward Chaining]] — the goal-driven counterpart
- [[wiki/concepts/expert-systems|Expert Systems]] — the classic consumer
- [[wiki/concepts/constraint-satisfaction|Constraint Satisfaction]] — propagation as forward inference
