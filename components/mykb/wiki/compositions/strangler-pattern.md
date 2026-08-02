---
type: "concept"
title: "Strangler Pattern"
description: "Incrementally replacing a legacy system piece by piece"
tags: ["strangler-pattern", "legacy", "migration", "architecture"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Strangler Pattern

## Summary
The strangler pattern replaces a legacy system gradually: new functionality routes to new services while old paths keep working, and the legacy system shrinks like a vine-strangled tree until it dies. It de-risks big rewrites.

## Details
- Route by feature or traffic share; keep old and new running until the new is proven.
- Each strangler step is independently releasable and reversible.
- Watch for the half-strangled state: two systems serving one behavior need clear ownership.
- mykb relevance: the wiki curation pipeline stranglers the old manual workflow feature by feature.

## Related
- [[wiki/software-engineering/legacy-code-strategies|Legacy Code Strategies]]
- [[wiki/cloud-infra/strangler-fig-pattern|Strangler Fig Pattern]]
- [[wiki/compositions/monolith-to-microservices|Monolith to Microservices]]
- [[wiki/software-engineering/refactoring-techniques|Refactoring Techniques]]
- [[wiki/dev-tools/continuous-delivery|Continuous Delivery]]
