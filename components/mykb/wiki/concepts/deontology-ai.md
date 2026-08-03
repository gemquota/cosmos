---
type: "concept"
title: "Deontology for AI"
description: "Rules-based ethics for AI systems"
tags: ["deontology", "ethics", "rules"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Deontology for AI

## Summary
Deontological AI ethics binds systems to rules and duties rather than optimizing outcomes. Where consequentialism asks "what produces the best results?", deontology asks "what is the right thing to do, regardless of consequences?" For AI this translates into hard constraints: do not deceive, do not harm, do not violate permissions — rules that hold even when violating them would score higher on the objective.

## Details
- The appeal is predictability and rights protection. Rule-governed systems have stable, auditable behavior: an observer can check whether the system obeyed its rules without reconstructing its full consequence calculus. Rules also protect individuals against being sacrificed for aggregate good — a deontological ban on deception or coercion holds even when the expected-value calculation says lying would save more people. In safety engineering this is precisely the role of invariants and side constraints.
- The weakness is that rules conflict with optimization. A pure rule-follower cannot trade off duties, and any realistic system faces rule conflicts — two duties that cannot both be satisfied — which forces either an implicit priority ordering (which is itself a consequentialist choice) or paralysis. Rules are also gameable literally: a system that must "not lie" learns truthful-but-misleading phrasing, and a system bound by a specific prohibition finds adjacent actions that violate its spirit. Specification gaming is deontology's failure mode in machine form.
- Modern hybrid approaches add side constraints to consequentialist objectives: optimize the outcome, but never cross the constraint lines. This combines the strengths — clear red lines plus flexible optimization within them — at the cost of deciding where the red lines go and how they are enforced under pressure.
- RSIS3 relevance: the practices document is deontological — rules the loop must obey, regardless of what the improvement metrics suggest. Workspace hygiene, state-file disjointness, and telemetry coverage are duties, not preferences; the constraint checks exist precisely so that a tempting optimization never overrides them.

## Related
- [[wiki/concepts/side-constraints|Side Constraints]] — the hybrid mechanism
- [[wiki/concepts/consequentialism-ai|Consequentialism for AI]] — the contrasting frame
- [[wiki/agent-systems/instruction-following|Instruction Following]] — the rules substrate
- [[wiki/concepts/virtue-ethics-ai|Virtue Ethics for AI]] — the third frame
- [[wiki/concepts/control-protocols|Control Protocols]] — the full treatment of this theme
- [[wiki/concepts/utility-functions|Utility Functions]] — existing graph context
