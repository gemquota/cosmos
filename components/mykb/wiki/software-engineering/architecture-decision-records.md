---
type: "concept"
title: "Architecture Decision Records"
description: "Short, numbered documents that record significant architectural decisions and their context"
tags: ["architecture", "adr", "documentation", "decisions"]
timestamp: "2026-08-01T00:00:00Z"
status: "stub"
---

# Architecture Decision Records

## Summary
An architecture decision record (ADR) is a dated, numbered note capturing a significant decision, its context, and the alternatives considered. ADRs make the 'why' of a codebase readable long after the people involved have moved on.

## Details
- Classic structure: Context, Decision, Status, Consequences; newer formats add alternatives and supersession links.
- ADRs live in the repo, are reviewed like code, and can be superseded by later ADRs, building a decision history.
- RSIS3 relevance: mykb can store ADRs as wiki articles so the graph surfaces related decisions.

## Related
- [[wiki/software-engineering/documentation-as-code|Documentation as Code]] — ADRs are decisions written and reviewed like code
- [[wiki/software-engineering/domain-driven-design|Domain-Driven Design]] — boundary decisions are classic ADR material
- [[wiki/memory/provenance|Provenance]] — ADRs record why a design was chosen
- [[wiki/sources/README|Sources]] — decision provenance belongs with source records
