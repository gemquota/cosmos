---
type: "concept"
title: "Architecture Decision Records"
description: "Short, numbered documents that record significant architectural decisions and their context"
tags: ["architecture", "adr", "documentation", "decisions"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
---
# Architecture Decision Records

## Summary

Architecture Decision Records (ADRs) capture significant technical decisions — context, decision, consequences — in a lightweight, versioned document. They turn architectural memory into a first-class artifact that reviews, onboarding, and future architects can consult.

## Details
- Mechanism: an ADR is a dated note with status (proposed/accepted/superseded), context (forces and constraints), decision, and consequences (positive and negative tradeoffs); lightweight formats (Markdown in the repo) win over heavyweight documents; numbering and links (supersedes, related) build a decision history. Decisions qualify when they are hard to reverse and shape the codebase.
- Concrete example: a team adopts Postgres over a new NoSQL store and writes an ADR documenting the consistency requirements and operational constraints; six months later, a proposal to switch is evaluated against the original context instead of re-litigating; a new hire reads ADRs to learn why the architecture looks the way it does.
- Failure modes: ADRs that describe what without why (unreviewable); decisions recorded after the fact with rewritten history; ADR sprawl — trivial decisions drowning the significant ones; and accepted ADRs never revisited, so superseded decisions quietly diverge from reality.
- Operational tradeoffs: ADRs cost writing discipline and review time; they pay in continuity, onboarding speed, and better reversibility (consequences are explicit). The practice is to require an ADR for decisions that are costly to reverse and to link it to the code that implements it.
- RSIS3/mykb relevance: the wiki's syntheses serve as ADRs for loop-level architecture changes, preserving the why alongside the what for future sessions.
- Review integration: put ADRs in the same review flow as code so decisions are debated at proposal time with the context fresh, and link the merge to the implementing PR.
- Lifecycle hygiene: re-read accepted ADRs during major refactors and mark superseded ones so the decision history reflects current reality.

## Related
- [[wiki/software-engineering/documentation-as-code|Documentation as Code]] — ADRs are decisions written and reviewed like code
- [[wiki/software-engineering/domain-driven-design|Domain-Driven Design]] — boundary decisions are classic ADR material
- [[wiki/memory/provenance|Provenance]] — ADRs record why a design was chosen
- [[wiki/sources/index|Sources]] — decision provenance belongs with source records
