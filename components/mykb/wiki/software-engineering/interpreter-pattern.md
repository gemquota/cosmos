---
type: "concept"
title: "Interpreter Pattern"
description: "Evaluating expressions of a small language using object structure and recursion"
tags: ["interpreter", "patterns", "design", "languages"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Interpreter Pattern

## Summary
The interpreter pattern implements a language's grammar as a hierarchy of expression objects, each knowing how to evaluate itself. It suits small, well-specified DSLs; larger languages deserve parser generators and proper VMs.

## Details
- Grammar rules map to classes; evaluation is recursive over the expression tree.
- Pair with the visitor pattern to add operations (pretty-print, typecheck) without new classes.
- Performance is weak for hot paths — compile or transform instead of interpreting leaf-by-leaf.
- mykb relevance: a tiny filter DSL could interpret wiki queries like tag:stub and status:growing.

## Related
- [[wiki/software-engineering/visitor-pattern|Visitor Pattern]]
- [[wiki/software-engineering/composite-pattern|Composite Pattern]]
- [[wiki/software-engineering/functional-programming|Functional Programming]]
- [[wiki/software-engineering/software-design-principles|Software Design Principles]]
- [[wiki/software-engineering/state-pattern|State Pattern]]
