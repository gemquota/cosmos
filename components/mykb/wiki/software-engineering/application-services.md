---
type: "concept"
title: "Application Services"
description: "The layer that orchestrates use cases: transactions, auth, and coordination"
tags: ["ddd", "application-services", "use-cases", "design"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Application Services

## Summary
Application services execute use cases: they fetch aggregates, invoke domain logic, manage transactions, and return results. They are the thin coordination layer between the outside world and the domain.

## Details
- One application service method per use case, named after the business action.
- They own transaction boundaries and security checks but not business rules.
- Keep them thin: logic belongs in the domain, orchestration belongs here.
- mykb relevance: PublishArticleUseCase coordinates validation, repository writes, and link refresh.

## Related
- [[wiki/software-engineering/domain-services|Domain Services]]
- [[wiki/software-engineering/use-case-layer|Use Case Layer]]
- [[wiki/software-engineering/repositories-pattern|Repositories Pattern]]
- [[wiki/software-engineering/clean-architecture|Clean Architecture]]
- [[wiki/software-engineering/software-design-principles|Software Design Principles]]
