---
type: "concept"
title: "Functional Programming Principles"
description: "Building software from pure functions and immutable data"
tags: ["functional-programming", "purity", "immutability", "principles"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://en.wikipedia.org/wiki/Functional_programming", "https://en.wikipedia.org/wiki/Type_system"]
---

# Functional Programming Principles

## Summary
Functional programming composes pure functions over immutable data, with effects pushed to the edges. Its principles — purity, immutability, referential transparency, and function composition — make code easier to test, parallelize, and reason about.

## Details
- Pure functions are deterministic and side-effect free; the same input always yields the same output.
- Immutability makes sharing safe: no aliasing bugs, no locks for reads, and cheap structural sharing.
- Higher-order functions and composition build behavior from small, named pieces.
- Effects move to the boundary: I/O and state are isolated so the core stays pure.
- The style transfers to any language — you can write functional Java, Python, or JavaScript.
- For the mykb bundle, the curation core is functional: pure transform functions over immutable article records.
- Worked example — the wiki pipeline is a composition of pure functions: parse -> normalize -> verify -> render, each taking and returning immutable records, with file I/O only at the ends.

Worked example — the wiki pipeline is a composition of pure functions: parse -> normalize -> verify -> render, each taking and returning immutable records, with file I/O only at the ends.

## Related
- [[wiki/software-engineering/pure-functions|Pure Functions]]
- [[wiki/software-engineering/immutability-practice|Immutability Practice]]
- [[wiki/software-engineering/referential-transparency|Referential Transparency]]
- [[wiki/software-engineering/functional-programming|Functional Programming]]
- [[wiki/software-engineering/type-systems-in-practice|Type Systems in Practice]]
- [[wiki/software-engineering/side-effect-isolation|Side Effect Isolation]]
- [[wiki/dev-tools/property-based-testing|Property-Based Testing]]
