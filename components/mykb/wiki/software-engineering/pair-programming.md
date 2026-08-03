---
type: "concept"
title: "Pair Programming"
description: "Two developers working together at one workstation, alternating driver and navigator roles"
tags: ["collaboration", "practice", "quality", "team"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
---
# Pair Programming

## Summary

Pair programming is two engineers on one task — one drives, one navigates — producing continuous review, shared understanding, and fewer defects. It is the most flexible collaboration mode: cheaper than mobbing, stronger than solo, and best deployed selectively, not as a mandate.

## Details
- Mechanism: the driver implements while the navigator reviews, designs, and catches mistakes in real time; roles rotate; sessions are task-scoped and timeboxed. The value is not two people typing — it is the second pair of eyes on every line and the transfer of context as it is created.
- Concrete example: a senior pairs with a junior on a tricky integration — the junior drives and learns the codebase's unwritten rules while the senior catches design traps; two engineers pair on a security-sensitive change so no line ships unreviewed; a pair untangles a bug by narrating the failure hypothesis out loud.
- Failure modes: pairing on trivial work (wasteful); an imbalanced pair where one watches (swap drivers, set the navigator's job); pairing fatigue without breaks; and treating pairing as review-replacement — paired code still benefits from a fresh reviewer.
- Operational tradeoffs: pairing halves typing throughput per feature but raises quality and knowledge sharing; the pattern is pair the complex/risky/learning-rich work and solo the rest, with the ratio tuned per team. Remote pairing works with good tooling; the discipline is the same.
- RSIS3/mykb relevance: the wiki's loop reviews often pair a fresh reader with the author of a synthesis, catching the assumptions solo review misses.
- Tooling: remote pairing works with shared cursors, screen share, and low-friction switching; the tooling should not add friction to the driver/navigator rhythm.
- Session shape: scope pairs to a commit-sized chunk and switch pairs across the task so knowledge spreads beyond the original pair.

## Related
- [[wiki/software-engineering/mob-programming|Mob Programming]] — pairing scaled to a whole team
- [[wiki/software-engineering/code-review|Code Review]] — pairing is continuous real-time review
- [[wiki/software-engineering/code-ownership|Code Ownership]] — pairing spreads ownership beyond the author
- [[wiki/llm-agents/human-in-the-loop|Human-in-the-Loop]] — agents and humans pairing on tasks
- [[wiki/agent-systems/agent-evaluation|Agent Evaluation]] — continuous paired review mirrors agent evals
