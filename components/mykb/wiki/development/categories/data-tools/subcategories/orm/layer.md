---
type: "concept"
title: "Layer"
description: "Layer: horizontal architecture slices and the dependency rules that keep them clean"
tags: ["entity", "cli", "ide", "orm", "architecture"]
timestamp: "2026-07-19T22:41:43Z"
resource: ""
---

# Layer

## Summary

A layer is a horizontal slice of a system with a single responsibility, such as presentation, application logic, or persistence. Layered architecture keeps concerns separated so each part can change independently. It matters because the boundary discipline determines how maintainable a codebase is. Layering is a decision-type problem: the boundaries chosen determine how the architecture ages.

## Details

- **Definition** — Layering partitions a system into tiers with defined responsibilities and one-directional dependencies between them.
- **Typical layers** — Presentation, application, domain, and infrastructure layers are the common four, each depending on the one below.
- **Dependency rule** — Dependencies point inward: outer layers may use inner ones, but inner layers must not reach outward or the separation collapses.
- **Persistence layer** — An ORM sits in the infrastructure tier, translating domain objects to database rows so business logic stays database-agnostic.
- **Benefits** — Layers localize change, enable testing of each tier in isolation, and let teams swap implementations behind stable interfaces.
- **Leaky abstractions** — When SQL, HTTP, or UI details bleed across tiers, layers become decoration and the coupling returns.
- **Failure modes** — Cyclic dependencies, god objects spanning layers, and shortcut bypasses turn clean architecture into spaghetti.
- **Practical relevance** — Naming an ORM as its own layer clarifies where mappings, migrations, and queries belong in the codebase.
- **Testing impact** — Isolated layers can be tested with fakes at their interfaces, which is why clean boundaries enable fast suites.
- **Evolution** — New requirements usually land in one layer; clear ownership tells developers where to put the change.
- **Over-abstraction** — Too many layers with no added value create indirection; the right number is the minimum that keeps dependencies acyclic.
- **Boundary documentation** — Recording each layer's contract and its allowed dependencies keeps new developers and agents from crossing boundaries by accident.

## Related

- [[wiki/development/categories/data-tools/subcategories/orm/platform|Platform]] — the foundation beneath layers
- [[wiki/development/categories/data-tools/subcategories/orm/integrity|Integrity]] — rules enforced at the persistence layer
- [[wiki/development/categories/data-tools/subcategories/orm/analyzing|Analyzing]] — cross-layer data analysis
- [[wiki/development/categories/data-tools/subcategories/orm/experiment|Experiment]] — instrumentation across layers
