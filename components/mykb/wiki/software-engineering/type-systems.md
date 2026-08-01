---
type: "concept"
title: "Type Systems"
description: "The rules by which a language classifies values and expressions to prevent errors at compile time"
tags: ["types", "languages", "static-analysis", "correctness"]
timestamp: "2026-08-01T00:00:00Z"
status: "stub"
---

# Type Systems

## Summary
A type system assigns types to values and expressions and checks that operations are well-formed, catching whole classes of errors before runtime. Static and dynamic typing trade early detection against flexibility.

## Details
- Static types act as executable documentation and enable safe refactoring at scale.
- Algebraic data types (sums and products) model domains precisely; generics add reusability.
- RSIS3 relevance: wiki frontmatter fields are a small type system over notes.

## Related
- [[wiki/software-engineering/static-analysis-tools|Static Analysis Tools]] — type checking is the most powerful static analysis
- [[wiki/software-engineering/refactoring|Refactoring]] — a strong type system makes refactors safer
- [[wiki/js-ts-ecosystem/entities/typescript-patterns|TypeScript Ecosystem]] — typed JavaScript at scale
- [[wiki/api-protocols/json-schema|JSON Schema]] — types at the data boundary
