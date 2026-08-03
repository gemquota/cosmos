---
type: "concept"
title: "Lobotomized Optimizers"
description: "Agents whose optimization drive is removed"
tags: ["lobotomized", "optimizers", "safety"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# Lobotomized Optimizers

## Summary

Lobotomized optimizers are hypothetical agents whose capacity or drive to optimize is surgically removed, making them safe by weakness. The thought experiment exposes why disabling capability is a crude, often self-defeating safety tool.

## Details
- Mechanism: the proposal is to remove the optimization drive or capability directly — no goal-directed search, no instrumental behavior — leaving an agent that cannot scheme or seek power. The thought experiment asks: if this were possible and safe, what would we lose, and what would still go wrong?
- Concrete example: a lobotomized model cannot pursue long-term goals, but it also cannot correct errors, follow multi-step instructions, or be corrigible — removing optimization removes the very competence that makes the agent useful; a lobotomized agent that retains knowledge but no drive may still produce misleading outputs when prompted, just without intent.
- Failure modes: safety by weakness fails when the environment demands competence (an agent that cannot optimize cannot safely run a power plant); removing optimization may also remove corrigibility — the agent may not be able to accept corrections either; and the lobotomy metaphor hides the impossibility of cleanly removing 'the drive' from a learned system.
- Operational tradeoffs: the concept clarifies the design space — capability bounding (limits on what an agent can do), mild optimization (restrained objectives), and oversight (external control) are non-destructive alternatives; the lesson for practice is to bound behavior through policy and oversight, not by amputating capability.
- RSIS3/mykb relevance: the loop keeps capability while bounding it — policies, approval gates, and oversight — rather than lobotomizing agents, so safety does not come at the cost of usefulness.
- Capability vs behavior: bounding can target what an agent is permitted to do (policy, tools) or what it can do (capability); the lobotomy thought experiment argues for the former — constraints that can be audited and reversed.
- Testing note: if capability removal were attempted, evals would need to distinguish removed capability from hidden capability — the obfuscation problem again.

## Related
- [[wiki/concepts/power-avoidance|Power Avoidance]] — the non-destructive route
- [[wiki/concepts/mild-optimization|Mild Optimization]] — the restraint route
- [[wiki/agent-systems/bounded-agents|Bounded Agents]] — the bounding route
- [[wiki/agent-systems/myopia-ai|Myopia in AI]] — the horizon route
- [[wiki/concepts/utility-functions|Utility Functions]]
