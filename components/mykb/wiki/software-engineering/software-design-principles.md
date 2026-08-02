---
type: "concept"
title: "Software Design Principles"
description: "Enduring rules of thumb that guide the structure of maintainable software"
tags: ["design", "principles", "architecture", "quality"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://en.wikipedia.org/wiki/Software_design_pattern", "https://en.wikipedia.org/wiki/Separation_of_concerns"]
---

# Software Design Principles

## Summary
Software design principles are the durable rules of thumb — separation of concerns, single responsibility, DRY, least surprise, dependency inversion — that keep code maintainable as it grows. They are not laws: they are tradeoff heuristics that become valuable when applied with judgment and context.

## Details
- Separation of concerns splits a system by what each part is responsible for, so changes to one concern do not ripple through the others.
- The single responsibility principle keeps each unit with one reason to change, which makes units understandable and testable.
- DRY (don't repeat yourself) pushes shared knowledge into one place, but over-application creates premature abstraction.
- The principle of least surprise says code should behave the way a reader reasonably expects — consistent naming and structure matter.
- YAGNI (you are not gonna need it) counters speculative generality: build for today's requirements and refactor as real needs appear.
- These principles trade against each other; a good design is an explicit record of which tradeoff was chosen and why.

Worked example — a wiki sync module built with separation of concerns has one module for fetching, one for parsing, and one for writing; each changes for its own reason. When the source format changes, only the parser moves.

## Related
- [[wiki/software-engineering/solid-principles|SOLID Principles]]
- [[wiki/software-engineering/clean-architecture-practice|Clean Architecture Practice]]
- [[wiki/software-engineering/composition-over-inheritance|Composition Over Inheritance]]
- [[wiki/software-engineering/code-smells|Code Smells]]
- [[wiki/software-engineering/technical-debt-management|Technical Debt Management]]
- [[wiki/communities/software-craftsmanship|Software Craftsmanship]]
- [[wiki/software-engineering/service-locator|Service Locator]]
- [[wiki/software-engineering/clean-architecture|Clean Architecture]]
- [[wiki/software-engineering/refactoring|Refactoring]]
