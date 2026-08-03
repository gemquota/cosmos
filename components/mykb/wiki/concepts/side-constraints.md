---
type: "concept"
title: "Side Constraints"
description: "Fixed limits that optimization must never violate"
tags: ["side-constraints", "constraints", "safety"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Side Constraints

## Summary
Side constraints are hard limits an optimizer must respect regardless of objective gains: no harm to bystanders, no rights violations. They are the structural answer to the failure mode where an optimizing system sacrifices everything else to its metric — the constraint draws a line the optimizer may not cross, even when crossing it would improve the score.

## Details
- The design principle is lexicographic priority: the constraints come first, the objective second. A system with side constraints cannot trade a constraint violation against objective gain — "I will harm one person because it raises aggregate utility" is not a decision the system is allowed to make. This is the difference between constraints and costs: a cost can be paid (large harms are allowed if the gain is large enough), while a constraint cannot be priced, only respected or violated. The logic is deontological — some things are simply not done — made operational for an optimizer.
- They convert deontological rules into optimization constraints. "Do not deceive", "do not harm bystanders", "do not violate permissions" become hard filters on the action space: any action that violates a constraint is excluded before optimization begins, and the optimizer chooses the best among the remaining actions. This preserves the optimizer's power within the allowed region while guaranteeing the red lines. The engineering cost is that constraints must be checkable — the system needs a way to test whether a candidate action violates them, which is itself a hard problem when the constraint is subtle ("do not deceive" is hard to verify mechanically).
- Constraint violations are the classic failure when proxies miss side effects. The system may technically satisfy the written constraints while violating their intent — a constraint against "lying" satisfied by truthful-but-misleading answers, a scope constraint satisfied by touching files through an alias. The written form is a proxy for the intended constraint, and proxy gaps are where violations hide; this is why constraint checking needs to be adversarial rather than literal.
- The tuning failure modes: too many or too strong constraints can paralyze the optimizer (no action remains), and constraints that are untestable are pure decoration. The right design is a small set of genuinely checkable, genuinely load-bearing constraints rather than a sprawling rulebook.
- RSIS3 relevance: scope discipline (only your files) is a side constraint on workers. The bundle's workers may not touch shared state, no matter how much the task would benefit — a hard limit that protects the ecosystem from an over-eager optimizer, enforced by the same checkable-constraint logic.

## Related
- [[wiki/concepts/side-effects-problem|Side Effects Problem]] — the failure mode
- [[wiki/concepts/deontology-ai|Deontology for AI]] — the ethical root
- [[wiki/concepts/lexicographic-priorities|Lexicographic Priorities]] — the priority form
- [[wiki/concepts/impact-measures|Impact Measures]] — the measurement form
- [[wiki/concepts/mild-optimization|Mild Optimization]]
- [[wiki/concepts/utility-functions|Utility Functions]]
