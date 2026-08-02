---
type: "concept"
title: "Technical Debt Management"
description: "Tracking, prioritizing, and paying down shortcuts in the codebase"
tags: ["technical-debt", "quality", "maintenance", "planning"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://martinfowler.com/bliki/TechnicalDebt.html", "https://en.wikipedia.org/wiki/Technical_debt"]
---

# Technical Debt Management

## Summary
Technical debt is the gap between the code that exists and the code you would write now — deliberate shortcuts and accidental rot, both with interest. Management means making debt visible, priced, and scheduled instead of pretending it does not exist.

## Details
- Ward Cunningham's original metaphor: shipping fast borrows from the future; the interest is the extra cost of every later change.
- Debt has types: deliberate shortcuts, accidental complexity, outdated dependencies, and missing tests — each needs a different payoff.
- Make debt visible: an inventory with owners, impact, and a rough payoff estimate beats an unspoken shame list.
- Pay down in the work you touch: refactor-as-you-go (boy scout rule) compounds faster than big rewrites.
- Debt is not always bad: it is rational when the interest is lower than the cost of paying it now.
- For the mykb bundle, debt includes unverified sources, duplicate concepts, and stale links — inventory and schedule them.

Worked example — the wiki has 200 unverified source links. Each month they age, and every link-check pass grows slower. The team budgets 10% of capacity to verification and tracks the debt in the backlog with a burn-down.

## Related
- [[wiki/software-engineering/refactoring-techniques|Refactoring Techniques]]
- [[wiki/software-engineering/code-smells|Code Smells]]
- [[wiki/software-engineering/legacy-code-strategies|Legacy Code Strategies]]
- [[wiki/software-engineering/technical-debt|Technical Debt]]
- [[wiki/communities/engineering-management|Engineering Management]]
- [[wiki/tooling/flag-debt|Flag Debt]]
- [[wiki/tooling/flag-cleanup|Flag Cleanup]]
- [[wiki/software-engineering/refactoring|Refactoring]]
