---
type: "concept"
title: "Behavior Trees"
description: "Hierarchical control structures for composing reactive behaviors"
tags: ["behavior-trees", "control", "reactive", "architecture"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://en.wikipedia.org/wiki/Behavior_tree_(artificial_intelligence,_robotics_and_control)", "https://arxiv.org/abs/1709.00084"]
---

# Behavior Trees

## Summary
Behavior trees compose behaviors as a tree of nodes — sequences, selectors, conditions, actions — evaluated top-down each tick. They matter because they make reactive control modular, debuggable, and reusable. They originated in games but apply to agent control flow.

## Details
- Nodes: sequence (all must succeed), selector (try until one succeeds), decorators.
- Each tick re-evaluates, giving natural interruption and priority.
- Deterministic and visualizable, unlike ad-hoc conditionals.
- Open questions: integration with LLM action selection.
- A behavior tree organizes behaviors as a tree of control nodes (sequence, selector, parallel) and leaf actions/conditions, executing by tick and returning success/failure/running.
- Trees compose modularly: subtrees can be reused and recombined, which makes them easier to reason about and edit than monolithic finite-state machines.
- The main costs are the tick discipline (every node re-evaluated each tick) and the risk of deep trees becoming hard to debug without good visualization.
- **Worked example / comparison** — Worked example — an agent's daily routine as a tree: a selector tries 'review queue' first, falls back to 'write stubs' when the queue is empty, with a condition checking health-dashboard metrics at the root.
- For mykb, behavior trees describe how curation workflows branch: the same tree of checks (freshness, links, sources) runs against every article batch.

## Related
- [[wiki/agent-systems/agent-loop|Agent Loop]]
- [[wiki/concepts/reactive-planning|Reactive Planning]]
- [[wiki/concepts/production-rules|Production Rules]]
- [[wiki/concepts/cognitive-architecture|Cognitive Architecture]]
- [[wiki/agent-systems/blackboard-architecture|Blackboard Architecture]]
- [[wiki/concepts/promotion-readiness|Promotion Readiness]]
- [[wiki/ai-ml/article-health-scores|Article Health Scores]]
- [[wiki/concepts/decision-guides|Decision Guides]]
