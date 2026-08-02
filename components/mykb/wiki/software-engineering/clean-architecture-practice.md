---
type: "concept"
title: "Clean Architecture Practice"
description: "Layering a system so business rules stay independent of frameworks, UI, and databases"
tags: ["clean-architecture", "architecture", "layering", "ddd"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html", "https://en.wikipedia.org/wiki/Software_architecture"]
---

# Clean Architecture Practice

## Summary
Clean architecture organizes concentric layers — entities, use cases, adapters, and frameworks — with dependencies pointing inward toward business rules. The core knows nothing about databases, HTTP, or UIs, so those can be swapped without touching the domain.

## Details
- The dependency rule is the whole pattern: source-code dependencies point inward; nothing in an inner circle knows about an outer one.
- Entities and use cases hold the business rules; controllers, gateways, and presenters translate between the core and the world.
- Frameworks and databases live at the outermost ring as interchangeable details, chosen late and replaced easily.
- Practice notes: keep use cases thin, model the domain in the core, and let interfaces at boundaries define what the outside must provide.
- The tradeoff is indirection: clean architecture costs mapping layers, so apply it where the business rules are the asset, not for throwaway scripts.
- It aligns with hexagonal and onion architectures; the wiki pipeline uses ports for storage and sources with a framework-free core.

Worked example — the wiki link-checker core defines a SourcePort with fetch(url); a curl adapter implements it. When a new source type appears, only an adapter is added; the core logic stays untouched.

## Related
- [[wiki/software-engineering/ports-and-adapters|Ports and Adapters]]
- [[wiki/software-engineering/onion-architecture|Onion Architecture]]
- [[wiki/software-engineering/hexagonal-architecture|Hexagonal Architecture]]
- [[wiki/software-engineering/use-case-layer|Use Case Layer]]
- [[wiki/software-engineering/clean-architecture|Clean Architecture]]
- [[wiki/software-engineering/software-design-principles|Software Design Principles]]
