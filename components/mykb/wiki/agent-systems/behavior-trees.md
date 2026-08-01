---
type: "concept"
title: "Behavior Trees"
description: "Hierarchical control structures for composing reactive behaviors"
tags: ["behavior-trees", "control", "reactive", "architecture"]
timestamp: "2026-07-31T00:00:00Z"
status: "stub"
---

# Behavior Trees

## Summary
Behavior trees compose behaviors as a tree of nodes — sequences, selectors, conditions, actions — evaluated top-down each tick. They matter because they make reactive control modular, debuggable, and reusable. They originated in games but apply to agent control flow.

## Details
- Nodes: sequence (all must succeed), selector (try until one succeeds), decorators.
- Each tick re-evaluates, giving natural interruption and priority.
- Deterministic and visualizable, unlike ad-hoc conditionals.
- Open questions: integration with LLM action selection.

## Related
- [[wiki/agent-systems/agent-loop|Agent Loop]] — the loop behavior trees can drive
- [[wiki/concepts/reactive-planning|Reactive Planning]] — the planning philosophy they implement
- [[wiki/concepts/production-rules|Production Rules]] — the rule-based alternative
- [[wiki/concepts/cognitive-architecture|Cognitive Architecture]] — the architecture they slot into
- [[wiki/agent-systems/blackboard-architecture|Blackboard Architecture]] — shared-state alternative
