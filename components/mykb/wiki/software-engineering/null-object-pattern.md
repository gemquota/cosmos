---
type: "concept"
title: "Null Object Pattern"
description: "Using a do-nothing object instead of null to avoid null checks"
tags: ["null-object", "patterns", "design", "optional"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Null Object Pattern

## Summary
The null object pattern replaces null with an object that implements the interface by doing nothing, eliminating repeated null checks. It simplifies code but can hide real errors by making absence look like success.

## Details
- Null objects are safe defaults: no-op methods, empty collections, zero values.
- Prefer Option/Maybe types in modern languages — null objects are the OOP-era fix.
- Distinguish legitimate absence from error; a null object for an error hides a bug.
- mykb relevance: an empty-article fallback keeps graph queries from crashing on missing slugs.

## Related
- [[wiki/dev-tools/fallback-values|Fallback Values]]
- [[wiki/software-engineering/type-systems|Optional Types]]
- [[wiki/software-engineering/strategy-pattern|Strategy Pattern]]
- [[wiki/software-engineering/type-systems|Type Systems]]
- [[wiki/software-engineering/software-design-principles|Software Design Principles]]
