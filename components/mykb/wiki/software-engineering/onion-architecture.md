---
type: "concept"
title: "Onion Architecture"
description: "Layering dependencies inward toward a domain core"
tags: ["onion-architecture", "architecture", "ddd", "design"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Onion Architecture

## Summary
Onion architecture arranges concentric layers — domain in the center, then application, infrastructure, and UI outside — with dependencies always pointing inward. The domain is the most stable, most tested layer.

## Details
- Inner layers define interfaces; outer layers implement them; nothing depends outward.
- It is hexagon-plus: same dependency rule, more explicit layer naming.
- Persistence, UI, and frameworks live on the outside and are swappable.
- mykb relevance: wiki core (linking, curation rules) stays framework-free inside the onion.

## Related
- [[wiki/software-engineering/ports-and-adapters|Ports and Adapters]]
- [[wiki/software-engineering/hexagonal-architecture|Hexagonal Architecture]]
- [[wiki/software-engineering/clean-architecture|Clean Architecture]]
- [[wiki/software-engineering/layered-architecture|Layered Architecture]]
- [[wiki/software-engineering/domain-driven-design|Domain-Driven Design]]
