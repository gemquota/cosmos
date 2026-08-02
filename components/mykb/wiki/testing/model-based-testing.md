---
type: "concept"
title: "Model-Based Testing"
description: "Generating test cases from formal models of system behavior"
tags: ["model-based-testing", "testing", "models", "generation"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://www.ibm.com/topics/model-based-testing", "https://www.istqb.org/glossary"]
---

# Model-Based Testing

## Summary
Model-based testing generates test cases from formal models of system behavior, state machines, decision tables, or contracts, covering paths automatically. Tests stay in sync with the model instead of drifting from hand-written cases.

## Details
- Models: finite state machines, labeled transition systems, and pre- and post-conditions.
- Generation: coverage criteria such as state, transition, and path drive case selection.
- Benefits: broad coverage, model reuse, and regenerated tests on model change.
- Tools: GraphWalker, Spec Explorer, and custom generators for simpler models.
- Cost: model authoring skill, and models drift from implementation if unmaintained.
- Excellent for stateful protocols, workflows, and embedded logic.
- Pair with state-transition testing and property-based checks.

## Related
- [[wiki/testing/state-transition-testing|State Transition Testing]] — the models MBT automates
- [[wiki/testing/grammar-based-testing|Grammar-Based Testing]] — grammar models for inputs
- [[wiki/testing/property-based-testing|Property-Based Testing]] — invariant generation
- [[wiki/testing/test-oracles|Test Oracles]] — expected outputs from models
- [[wiki/testing/decision-table-testing|Decision Table Testing]] — rule models to generate from
- [[wiki/software-engineering/domain-driven-design|Domain-Driven Design]] — models mirroring business rules
