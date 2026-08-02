---
type: "concept"
title: "Refactoring Techniques"
description: "Behavior-preserving restructuring of code to improve its design"
tags: ["refactoring", "quality", "maintenance", "techniques"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://refactoring.com/catalog/", "https://martinfowler.com/bliki/CodeSmell.html"]
---

# Refactoring Techniques

## Summary
Refactoring is restructuring code without changing its observable behavior, using small proven steps: extract function, rename, introduce parameter, move field. The catalog of techniques makes improvement mechanical and safe — especially when backed by tests.

## Details
- The catalog (extract, inline, rename, move, replace conditional with polymorphism) names the moves so teams can discuss them.
- Behavior preservation is the contract: tests before and after, ideally with the refactor as a separate commit.
- Small steps compound: a chain of ten two-minute refactorings transforms a module with low risk.
- Refactoring is not rewriting: it preserves behavior; rewriting changes behavior and risks regressions.
- Opportunistic refactoring (improving code you touch) beats dedicated refactor months.
- For the mykb bundle, refactoring applies to build scripts and curation logic: extract the link-resolver, rename the sync stages.
- Worked example — the wiki build script has a 200-line main; extract functions make it testable, then the tests reveal a naming lie that the extract made obvious.

Worked example — the wiki build script has a 200-line main; extract functions make it testable, then the tests reveal a naming lie the extract made obvious.

## Related
- [[wiki/software-engineering/code-smells|Code Smells]]
- [[wiki/software-engineering/technical-debt-management|Technical Debt Management]]
- [[wiki/software-engineering/unit-testing-practice|Unit Testing Practice]]
- [[wiki/software-engineering/legacy-code-strategies|Legacy Code Strategies]]
- [[wiki/software-engineering/software-design-principles|Software Design Principles]]
- [[wiki/tooling/flag-cleanup|Flag Cleanup]]
- [[wiki/compositions/strangler-pattern|Strangler Pattern]]
- [[wiki/software-engineering/refactoring|Refactoring]]
- [[wiki/software-engineering/technical-debt|Technical Debt]]
