---
type: "concept"
title: "Visitor Pattern"
description: "Adding operations to an object structure without changing its classes"
tags: ["visitor", "patterns", "design", "traversal"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Visitor Pattern

## Summary
The visitor pattern lets you add an operation across a family of classes by passing a visitor object that each element accepts. It separates the structure from the algorithm — ideal for ASTs, documents, and object graphs.

## Details
- Double dispatch: the element calls back into the visitor with its concrete type.
- Adding a new operation means one visitor; adding a new element type means updating every visitor.
- Pattern matching in modern languages often replaces visitors for algebraic data.
- mykb relevance: a markdown visitor could render, lint, or link-check the same AST without new parser code.

## Related
- [[wiki/software-engineering/iterator-pattern|Iterator Pattern]]
- [[wiki/software-engineering/composite-pattern|Composite Pattern]]
- [[wiki/software-engineering/interpreter-pattern|Interpreter Pattern]]
- [[wiki/software-engineering/software-design-principles|Software Design Principles]]
- [[wiki/software-engineering/functional-programming|Functional Programming]]
