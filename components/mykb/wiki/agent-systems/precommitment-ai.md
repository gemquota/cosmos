---
type: "concept"
title: "Precommitment in AI"
description: "Binding future behavior to current intentions"
tags: ["precommitment", "commitments", "agency"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Precommitment in AI

## Summary
Precommitment in AI is binding future behavior to current intentions: a system arranges, in advance, that it will act a certain way later even if its later self would prefer otherwise. It is the standard solution to time inconsistency and a core tool for making agent behavior stable and credible.

## Details
- **The problem it solves** — without precommitment, a system that will later face temptation, drift, or pressure can deviate from the plan its earlier self chose; precommitment removes the later choice.
- **Mechanisms** — commitment devices include irreversible publication, delegating the key to another party, contractual penalties, and architectural constraints that make deviation impossible rather than costly.
- **Agent applications** — an agent can precommit to asking before irreversible actions, to stopping at a deadline, or to not negotiating against its own interests, by structuring its own tools and permissions.
- **Credibility** — a precommitment only changes others' expectations if it is credible: the binding must be observable and the cost of breaking it must be real.
- **Relationship to goal locking** — goal locking freezes the objective; precommitment freezes the plan or the behavioral policy. Both defend against later drift.
- **Time-consistency link** — precommitment is the fix for time-inconsistent preferences: it lets the current self constrain the future self's choices.
- **mykb relevance** — precommitted pass specifications are time-consistency tools: the pass's rules are fixed before the work starts and are not renegotiated mid-run.

- **Boundary conditions** — precommitment is dangerous when the current self is wrong: a badly chosen precommitment is harder to reverse than a mere plan, so the binding should be strong enough to resist drift but weak enough to be revised through a deliberate process.

## Related
- [[wiki/agent-systems/credible-commitments|Credible Commitments]] — the credibility requirement
- [[wiki/agent-systems/commitment-devices-ai|Commitment Devices]] — the mechanisms
- [[wiki/agent-systems/time-consistency-ai|Time Consistency]] — the problem being solved
- [[wiki/agent-systems/goal-locking|Goal Locking]] — freezing the objective
- [[wiki/concepts/goal-specification|Goal Specification]] — setting the target in advance
- [[wiki/agent-systems/reward-locking|Reward Locking]] — freezing the evaluation
