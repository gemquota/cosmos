---
type: "concept"
title: "Priority Weights"
description: "Numeric priorities assigned to goals or instructions"
tags: ["priority", "weights", "goals"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Priority Weights

## Summary
Priority weights assign numeric precedence to competing goals or instructions, so that when they conflict the system can resolve the conflict by comparing weights instead of improvising. They make tradeoffs explicit and auditable, but they are specifications: wrong weights produce wrong tradeoffs, and the numbers are only as good as the process that set them.

## Details
- **Resolution mechanics** — weights can be used directly in optimization (maximize weighted sum) or as gating thresholds (hard rules with priority levels); the choice changes failure behavior.
- **Auditability** — with explicit weights, a choice that surprises a reviewer can be traced to the weights that produced it; without them, conflicts resolve by unexamined habit.
- **Setting weights** — weights should come from a deliberative process (policy, risk analysis, user preferences) and be versioned; ad-hoc weights are just guesswork with numbers attached.
- **Goodhart risk** — optimizing a weighted objective invites gaming the weights; the resolution must be rechecked against the underlying values, not just the computed score.
- **Relationship to instruction hierarchy** — a hierarchy is the lexicographic case: highest priority wins outright rather than trading off; weights generalize to partial tradeoffs.
- **Failure modes** — zero-weight goals are effectively deleted, floating weights drift silently, and over-tuned weights overfit the cases that set them.
- **mykb relevance** — check rules carry explicit priority over convenience, making the wiki's practice violations resolvable without negotiation.

- **Visibility in logs** — when a conflict is resolved, the log should record the weights and the comparison that decided it; that turns an invisible judgment into a reviewable artifact.

- **Review cadence** — weights should be reviewed on a schedule, the same way policies are: stale weights silently encode yesterday's tradeoffs, and the review is what catches them before they produce an embarrassing conflict.

## Related
- [[wiki/agent-systems/instruction-hierarchy|Instruction Hierarchy]] — the structured form
- [[wiki/concepts/goal-prioritization|Goal Prioritization]] — scheduling by priority
- [[wiki/concepts/lexicographic-priorities|Lexicographic Priorities]] — the strict ordering case
- [[wiki/concepts/value-specification|Value Specification]] — where weights come from
- [[wiki/concepts/utility-functions|Utility Functions]] — the optimization context
