---
type: "concept"
title: "Recursive Self-Improvement"
description: "Systems that modify their own code, prompts, and strategies across escalating loops"
tags: ["self-improvement", "rsis3", "metacognition", "architecture", "recursion"]
timestamp: "2026-07-31T00:00:00Z"
status: "growing"
source: ["https://arxiv.org/abs/cs/0309048"]
---

# Recursive Self-Improvement

## Summary
Recursive self-improvement (RSI) is the capability of a system to improve the components that improve it — code, prompts, memory, and strategy. It matters because each improvement can raise the ceiling for the next cycle, but the same recursion amplifies errors, so it must be gated by tests, constraints, and rollback. RSIS3 is built around this idea with three nested loops: L1 per-task action, L2 per-session improvement, and L3 cross-session evolution.

## Details
- The theoretical anchor is Schmidhuber's Gödel machine: a self-referential program that rewrites itself only when a proof shows the rewrite improves expected utility.
- RSIS3's L1 loop improves task execution; L2 improves code and prompt tuning within a session; L3 consolidates memory and evolves strategy across sessions.
- **Safety gates**: no mutation is accepted unless tests pass; git rollback restores the previous state on failure.
- **Memory as substrate**: mykb stores pulse outcomes, decisions, and consolidations so L3 has evidence to improve from.
- Worked example: after a session of failures, L3 writes a synthesis note into the wiki and adjusts the strategy used by the next session.
- Related protocols: RRP (Recursive Refinement Protocol) drives ideation and theory-crafting for improvement cycles.

- **Gating** — improvement must pass external gates (tests, rollback, human review of strategy changes) before it is accepted; ungated self-modification is how errors become permanent.
- **Ceiling** — the recursion's ceiling is set by the evaluator's quality and the diversity of experience; improving those raises the ceiling more than adding cycles.

## Related

- [[wiki/concepts/metacognition|Metacognition]] — the self-observation ability RSI depends on
- [[wiki/concepts/calibration|Calibration]] — accuracy of the self-assessment used to decide improvements
- [[wiki/llm-agents/reflexion|Reflexion]] — verbal self-critique as a lightweight improvement loop
- [[wiki/concepts/mykb-implementation-report|Mykb Implementation Report]] — how the system was built and hardened
- [[wiki/ops/gap-report|Gap Analysis Report]] — gaps that improvement cycles target
- [[wiki/syntheses/recursive-self-improvement-spec-2026-08-06|Recursive Self-Improvement Specification]] — the full SPACE v2 export (67/67 probes) that grounds this page
- [[wiki/concepts/mykb-research-report|Mykb Research Report]] — research basis for the memory layer of RSI