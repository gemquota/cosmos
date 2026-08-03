---
type: "concept"
title: "Visitor Pattern"
description: "Adding operations to an object structure without changing its classes"
tags: ["visitor", "patterns", "design", "traversal"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# Visitor Pattern

## Summary

The visitor pattern adds operations to a set of classes without modifying them: a visitor object walks the object structure and dispatches per element type. It centralizes cross-cutting operations (serialization, analysis, code generation) but couples visitor to the element hierarchy's stability.

## Details
- Mechanism: elements accept a visitor (accept(visitor)), calling the overloaded visit(X) method for their type; the visitor implements one method per element class; double dispatch routes to the right method at runtime. It shines when many operations apply to a fixed structure (ASTs, documents, object graphs) and fails when the element hierarchy changes often (every new element breaks every visitor).
- Concrete example: a compiler's AST: a type-checker, an optimizer, and a code generator are visitors over the same nodes without the AST knowing about them; a document model gets an exporter and a validator as visitors; adding a new node type forces every visitor to add a method — the tradeoff in action.
- Failure modes: hierarchy instability — new element types ripple through all visitors; visitors needing state that does not fit the visit signature (workarounds and hacks); and over-use where a simple switch or pattern match would do.
- Operational tradeoffs: visitors keep operations additively extensible (new operation = new visitor) at the cost of making element addition expensive; modern languages often prefer pattern matching (sealed types) for the same job. Use visitors for stable hierarchies with many operations.
- RSIS3/mykb relevance: the wiki's note parser uses visitors over the OKF document tree for export and validation, keeping format handlers separate from the core model.
- Hierarchy stability check: before adopting visitors, confirm the element set is closed in practice; an element hierarchy that changes each release makes every visitor a maintenance tax.
- Modern alternatives: where the language supports sealed types and pattern matching (or exhaustive switch), prefer them — they give the same dispatch with less ceremony.

## Related
- [[wiki/software-engineering/iterator-pattern|Iterator Pattern]]
- [[wiki/software-engineering/composite-pattern|Composite Pattern]]
- [[wiki/software-engineering/interpreter-pattern|Interpreter Pattern]]
- [[wiki/software-engineering/software-design-principles|Software Design Principles]]
- [[wiki/software-engineering/functional-programming|Functional Programming]]
