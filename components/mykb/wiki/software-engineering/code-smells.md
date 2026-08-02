---
type: "concept"
title: "Code Smells"
description: "Surface signs in code that hint at deeper design problems"
tags: ["code-smells", "design", "quality", "refactoring"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://martinfowler.com/bliki/CodeSmell.html", "https://refactoring.com/catalog/"]
---

# Code Smells

## Summary
Code smells are recognizable symptoms — long methods, god classes, feature envy, duplicated code — that usually indicate design problems. They are not bugs; they are heuristics that name where refactoring will pay off.

## Details
- Common smells: long method, large class, primitive obsession, switch statements, speculative generality, and message chains.
- Smells point to remedies: extract method for long methods, extract class for god classes, replace conditional with polymorphism for switch storms.
- Smells are probabilistic: context matters, and some are intentional tradeoffs (a long method in a hot path).
- Smell detection is the first step of the refactoring workflow; tools and review checklists help find them.
- For the mykb bundle, wiki content has smells too: overlong articles, duplicate concepts, and stub rot.
- Worked example — a curator review finds three articles repeating the same definition; the smell is duplication, and the fix consolidates into one concept with links.

Worked example — a curator review finds three articles repeating the same definition; the smell is duplication, and the fix consolidates into one concept with links.

## Related
- [[wiki/software-engineering/refactoring-techniques|Refactoring Techniques]]
- [[wiki/software-engineering/software-design-principles|Software Design Principles]]
- [[wiki/software-engineering/technical-debt-management|Technical Debt Management]]
- [[wiki/software-engineering/static-analysis|Static Analysis]]
- [[wiki/tooling/flag-debt|Flag Debt]]
- [[wiki/software-engineering/coding-standards|Coding Standards]]
- [[wiki/software-engineering/singleton-pitfalls|Singleton Pitfalls]]
- [[wiki/software-engineering/service-locator|Service Locator]]
- [[wiki/software-engineering/refactoring|Refactoring]]
- [[wiki/software-engineering/technical-debt|Technical Debt]]
