---
type: "concept"
title: "Production Rules"
description: "Condition-action rules that fire when their conditions match state"
tags: ["production-rules", "rules", "expert-systems", "inference"]
timestamp: "2026-07-31T00:00:00Z"
status: "stub"
---

# Production Rules

## Summary
Production rules are IF condition THEN action rules evaluated against working memory; when a condition matches, the action fires, possibly changing state and enabling other rules. They matter because they model reactive, modular behavior and are the substrate of classic expert systems. They are also how agents can encode policies.

## Details
- Rule engines (e.g., RETE) match many rules efficiently.
- Conflict resolution decides which matching rule fires first.
- Strengths: modular, explainable; weakness: interaction surprises.
- RSIS3 relevance: constraint and policy rules bound tool use.

## Related
- [[wiki/agent-systems/action-observation-loop|Action-Observation Loop]] — the loop rule firing drives
- [[wiki/concepts/forward-chaining|Forward Chaining]] — the inference strategy
- [[wiki/concepts/expert-systems|Expert Systems]] — the classic host
- [[wiki/concepts/procedural-memory|Procedural Memory]] — rules as compiled skill
- [[wiki/agent-systems/behavior-trees|Behavior Trees]] — a structured alternative
