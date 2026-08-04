---
type: "entity"
title: "Design Principle"
resource: ""
---
description: "A durable rule that guides architecture and implementation decisions"
tags: ["entity", "android", "api", "ast", "auth", "authorization", "design", "architecture"]
timestamp: "2026-07-19T22:41:43Z"

# Design Principle

## Summary
A design principle is a durable rule that guides how a team makes architecture and implementation decisions. It matters because principles keep a codebase coherent as people and requirements change, and because decisions made without shared guidance accumulate into inconsistency. Unlike rules enforced by tools, principles shape judgment. To stay useful they must be few, concrete, and genuinely referenced in review.

## Details
- **Definition** — a design principle expresses a preferred approach, such as "fail closed" or "prefer explicit over implicit", that decisions can be checked against.
- **Trade-off guidance** — principles resolve recurring conflicts, such as simplicity versus flexibility, by stating which side to favor and when.
- **Consistency** — teams that share principles produce systems that look like one system instead of a patchwork of individual preferences.
- **Documentation** — principles live in short, accessible documents with rationale and examples, so new members can internalize them quickly.
- **Enforcement** — some principles become automated checks, but most are applied in review, which requires everyone to understand them.
- **Evolution** — principles should be revisited and retired when they no longer serve the system, not treated as permanent law.
- **Common failure modes** — too many vague principles that contradict each other, and principles that drift from actual practice until they are decorative.
- **Worked example** — a team adopts "default-deny for new permissions"; every new capability starts off and requires an explicit, reviewed decision to enable.
- **Practical relevance** — a small set of living principles reduces decision fatigue and keeps security and architecture predictable over time.

## Related
- [[wiki/software-engineering/architecture-decision-records|Architecture Decision Records]] — recording decisions
- [[wiki/software-engineering/refactoring|Refactoring]] — applying principles to old code
- [[wiki/software-engineering/code-review|Code Review]] — where principles are applied
- [[wiki/testing/acceptance-testing|Acceptance Testing]] — verifying principle outcomes
- [[wiki/software-engineering/object-oriented-programming|Object-Oriented Programming]] — common principle source
- [[wiki/software-engineering/architecture-decision-records|Architecture Decision Records]] — rationale capture
