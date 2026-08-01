---
type: "concept"
title: "Reactive Planning"
description: "Deciding actions from current state without maintaining a plan"
tags: ["reactive", "planning", "behavior", "agents"]
timestamp: "2026-07-31T00:00:00Z"
status: "stub"
---

# Reactive Planning

## Summary
Reactive planning chooses actions directly from the current situation using rules or behaviors, without building or maintaining an explicit plan. It matters because it is fast, robust to surprises, and cheap — at the cost of foresight. It is the complement to deliberative planning systems.

## Details
- Implementations: production rules, behavior trees, subsumption.
- Strengths: low latency, graceful degradation under change.
- Weaknesses: no lookahead, hard to optimize sequences.
- Hybrids interleave reactive reflexes with periodic deliberation.

## Related
- [[wiki/agent-systems/planning-systems|Planning Systems]] — the deliberative counterpart
- [[wiki/agent-systems/behavior-trees|Behavior Trees]] — a reactive control structure
- [[wiki/concepts/production-rules|Production Rules]] — condition-action reactivity
- [[wiki/agent-systems/agent-loop|Agent Loop]] — the loop reactive control drives
- [[wiki/concepts/bounded-rationality|Bounded Rationality]] — why reactive is often enough
