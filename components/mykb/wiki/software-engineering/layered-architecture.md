---
type: "concept"
title: "Layered Architecture"
description: "Organizing code into stacked layers with one-directional dependencies"
tags: ["layered-architecture", "architecture", "design", "structure"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Layered Architecture

## Summary
Layered architecture stacks responsibilities — presentation, business logic, persistence — and lets each layer depend only on the one below. It is the default architecture for most applications, with the database at the bottom and the UI at the top.

## Details
- Classic stack: presentation → application → domain → infrastructure (or data).
- Dependency direction is the discipline; a presentation layer reaching straight into the DB is a leak.
- Risk: the pattern degrades into a god-layer or business-logic-in-persistence swamp.
- mykb relevance: the wiki CLI, pipeline, and storage layer follow this stack naturally.

## Related
- [[wiki/software-engineering/onion-architecture|Onion Architecture]]
- [[wiki/software-engineering/ports-and-adapters|Ports and Adapters]]
- [[wiki/software-engineering/clean-architecture|Clean Architecture]]
- [[wiki/software-engineering/pipeline-architecture|Pipeline Architecture]]
- [[wiki/software-engineering/software-design-principles|Software Design Principles]]
