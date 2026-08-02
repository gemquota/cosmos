---
type: "concept"
title: "Iterator Pattern"
description: "Providing sequential access to a collection's elements without exposing its structure"
tags: ["iterator", "patterns", "design", "collections"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Iterator Pattern

## Summary
The iterator pattern exposes sequential element access behind a uniform interface, decoupling algorithms from the underlying collection — arrays, trees, or lazy streams. Generators and language iteration protocols are its modern form.

## Details
- Iterators are lazy: infinite and streaming sequences become possible.
- Fail-fast or snapshot semantics decide what happens when the collection mutates mid-iteration.
- Generators (yield) collapse iterator state machines into plain functions.
- mykb relevance: iterate the wiki graph lazily to stream link checks without loading everything.

## Related
- [[wiki/software-engineering/composite-pattern|Composite Pattern]]
- [[wiki/software-engineering/visitor-pattern|Visitor Pattern]]
- [[wiki/software-engineering/functional-programming|Functional Programming]]
- [[wiki/software-engineering/event-loops|Event Loops]]
- [[wiki/software-engineering/software-design-principles|Software Design Principles]]
