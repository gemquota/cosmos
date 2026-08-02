---
type: "concept"
title: "Flyweight Pattern"
description: "Sharing immutable fine-grained objects to save memory"
tags: ["flyweight", "patterns", "design", "memory"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Flyweight Pattern

## Summary
The flyweight pattern shares common immutable parts across many objects so memory stays bounded — a text editor sharing glyph data, a game sharing sprite frames. Intrinsic state is shared; extrinsic state is passed per use.

## Details
- Intrinsic (shared, immutable) vs extrinsic (per-use) state split is the whole trick.
- Factories or interning tables manage the shared instances and deduplicate.
- Saves memory at the cost of identity: flyweights compare by value, not by reference.
- mykb relevance: intern repeated source URLs and tag strings in the wiki index to shrink it.

## Related
- [[wiki/software-engineering/object-pool|Object Pool]]
- [[wiki/software-engineering/value-objects|Value Objects]]
- [[wiki/software-engineering/prototype-pattern|Prototype Pattern]]
- [[wiki/software-engineering/immutability-practice|Immutability Practice]]
- [[wiki/software-engineering/performance-engineering|Performance Engineering]]
