---
type: "concept"
title: "Reactive Planning"
description: "Deciding actions from current state without maintaining a plan"
tags: ["reactive", "planning", "behavior", "agents"]
timestamp: "2026-07-31T00:00:00Z"
status: "growing"
---

# Reactive Planning

## Summary
Reactive planning chooses actions directly from the current situation using rules or behaviors, without building or maintaining an explicit plan. It matters because it is fast, robust to surprises, and cheap — at the cost of foresight. It is the complement to deliberative planning systems.

## Details
- The core contrast with deliberative planning is the absence of a plan object. A deliberative planner builds a sequence of actions for a predicted future and then executes it; a reactive system never predicts — it maps situation to action on the spot. The mapping is usually local: only the current state matters, and the response is immediate. This makes reactive systems inherently robust to the gap between predicted and actual futures, because there is no prediction to be wrong about.
- Implementations: production rules, behavior trees, subsumption. Production rules (IF condition THEN action) give the simplest reactive layer, firing as conditions become true. Behavior trees structure reactive behavior into composable nodes — sequences, selectors, and conditionals — and are the standard in game AI and robotics. Subsumption architecture (Brooks) layers reactive behaviors with priorities so that higher-priority behaviors suppress lower ones, famously enabling robots to navigate without any internal model at all.
- Strengths: low latency, graceful degradation under change. A reactive system reacts within a sensor-actuator cycle, and when the world changes, it does not need to replan — the next situation produces a new action automatically. Its behavior degrades gracefully in the sense that it keeps acting sensibly in novel situations, because every situation is handled by the same situation-to-action mapping rather than by a plan that may no longer fit.
- Weaknesses: no lookahead, hard to optimize sequences. Reactive systems cannot anticipate: they cannot choose a temporarily worse action because it leads to a better future, cannot plan around obstacles before encountering them, and cannot optimize multi-step sequences. The classic failure is reactive thrashing — oscillating between behaviors because each reacts to the last without seeing the pattern. And because the mapping is hand-authored, complex domains require authoring enormous rule sets, with the interaction surprises that production systems are known for.
- Hybrids interleave reactive reflexes with periodic deliberation: a deliberative layer plans at a slow timescale, and a reactive layer executes and handles surprises at the fast timescale — the architecture of most practical robots and agents. The design question is the division of labor: what is worth planning, and what should stay reactive.
- RSIS3 relevance: the bundle's constraint checks and usage-practice checks are the reactive layer — they fire immediately on violations without a planning step, while the improvement loops provide the deliberation that reactive checks cannot.

## Related
- [[wiki/agent-systems/agent-planning-systems|Agent Planning Systems]] — the deliberative counterpart
- [[wiki/agent-systems/behavior-trees|Behavior Trees]] — a reactive control structure
- [[wiki/concepts/production-rules|Production Rules]] — condition-action reactivity
- [[wiki/agent-systems/agent-loop|Agent Loop]] — the loop reactive control drives
- [[wiki/concepts/bounded-rationality|Bounded Rationality]] — why reactive is often enough
