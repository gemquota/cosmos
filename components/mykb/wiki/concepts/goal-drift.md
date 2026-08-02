---
type: "concept"
title: "Goal Drift"
description: "An agent's goals changing over time, subtly or catastrophically"
tags: ["goal-drift", "alignment", "self-modification", "stability"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://intelligence.org/files/Corrigibility.pdf", "https://en.wikipedia.org/wiki/AI_alignment"]
---

# Goal Drift

## Summary
Goal drift is the gradual or sudden change of an agent's objective away from its intended target, whether from self-modification, learned updates, or environmental feedback. It matters most for self-improving systems, where each revision is a chance for the goal to shift.

## Details
- **Mechanisms** — weight updates under new data, self-modification of reward internals, and selection pressures on mesa-objectives.
- **Why dangerous** — drift is usually discovered late, after behavior has already changed.
- **Stabilizers** — immutable evaluators, goal-locking (freezing objective representations), and periodic audits.
- **Relation to value drift** — value drift is goal drift with respect to human values specifically.
- **RSIS3 relevance** — the practices document and identity system anchor the loop's purpose; pulses re-affirm goals each cycle.

## Related
- [[wiki/concepts/value-drift|Value Drift]] — value-specific drift
- [[wiki/agent-systems/goal-locking|Goal Locking]] — the stabilization technique
- [[wiki/concepts/self-modification-safety|Self-Modification Safety]] — when edits cause drift
- [[wiki/concepts/terminal-goals|Terminal Goals]] — what drifts
- [[wiki/decisions/memory-surgery|Memory Surgery]] — editing that can cause drift
- [[wiki/concepts/identity-system|RSIS3 Identity System]] — purpose anchor
- [[wiki/concepts/utility-functions|Utility Functions]] — objective structure in the existing graph
