---
type: "concept"
title: "Use Case Layer"
description: "The application-level layer that expresses what the system does for its users"
tags: ["use-cases", "architecture", "ddd", "design"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Use Case Layer

## Summary
The use case layer sits between interfaces and the domain, containing one unit per user goal — Place Order, Publish Article, Link Sources. It names what the system accomplishes and keeps infrastructure out of the story.

## Details
- Each use case is a class or function with inputs, outputs, and a clear business outcome.
- Use cases own orchestration and transaction boundaries; the domain owns rules.
- Naming matters: use cases should read like requirements, not like plumbing.
- mykb relevance: the wiki's commands (curate, link, verify) map one-to-one to use cases.

## Related
- [[wiki/software-engineering/application-services|Application Services]]
- [[wiki/software-engineering/domain-services|Domain Services]]
- [[wiki/software-engineering/clean-architecture|Clean Architecture]]
- [[wiki/software-engineering/domain-services|Use Case Layer]]
- [[wiki/software-engineering/requirements-engineering|Requirements Engineering]]
