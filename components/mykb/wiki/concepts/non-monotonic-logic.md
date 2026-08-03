---
type: "concept"
title: "Non-Monotonic Logic"
description: "Logics where adding premises can invalidate earlier conclusions"
tags: ["non-monotonic-logic", "logic", "reasoning", "knowledge-representation"]
timestamp: "2026-07-31T00:00:00Z"
status: "growing"
---

# Non-Monotonic Logic

## Summary
Non-monotonic logic formalizes reasoning where new information can retract previous conclusions — unlike classical logic, where adding premises never removes theorems. It matters because agent reasoning in open worlds is inherently non-monotonic. It underpins default logic, circumscription, and answer-set programming.

## Details
- The classical property being abandoned is monotonicity: in classical logic, if a conclusion follows from a set of premises, it follows from every superset of those premises. Real reasoning violates this constantly — "birds fly" until we learn Tweety is a penguin; "the file is safe to open" until we learn it came from an untrusted sender. Non-monotonic logics build in the possibility that later evidence retracts earlier conclusions, which is exactly the structure of belief revision.
- The formal mechanisms include default rules, the closed-world assumption, and autoepistemic reasoning. Default logic adds rules of the form "if X is true and Y is consistent with everything we know, conclude Z" — the consistency check is what makes the logic non-monotonic, because learning Y's negation invalidates the conclusion. The closed-world assumption (everything not known to be true is false) is non-monotonic because learning a new fact can defeat a negative conclusion. Circumscription minimizes the extension of predicates to prefer normal situations; autoepistemic logic reasons about the agent's own knowledge ("if I don't know X, assume not-X"). Each captures a different slice of the same phenomenon: conclusions held provisionally, subject to revision.
- ASP is a practical, computational embodiment. Answer set programming gives non-monotonic reasoning a solver-based implementation: a program's answer sets are its stable models, and adding a constraint can remove answer sets — the non-monotonicity made machine-checkable. This is why ASP is the workhorse for realistic non-monotonic reasoning tasks rather than an intellectual curiosity.
- Agents revise beliefs exactly because inference is non-monotonic: an agent that never retracted conclusions could not function in a changing world. Every belief update is a non-monotonic operation, which is why the logic's vocabulary (defaults, defeat, closed-world assumptions) is the right language for describing agent memory and self-correction.
- Open question: integrating non-monotonic rules with LLM inference — LLMs reason non-monotonically in practice (they revise with new context) but without the guarantees or semantics of the formal systems.
- RSIS3 relevance: synthesis consolidation is non-monotonic — a new synthesis can retract or qualify an earlier one, and the wiki's revision history is the formal record of that non-monotonic process.


## Related
- [[wiki/concepts/defeasible-reasoning|Defeasible Reasoning]] — the applied counterpart
- [[wiki/concepts/answer-set-programming|Answer Set Programming]] — the computational embodiment
- [[wiki/concepts/abductive-reasoning|Abductive Reasoning]] — non-monotonic hypothesis inference
- [[wiki/concepts/belief-states|Belief States]] — revising what is believed
- [[wiki/llm-agents/self-reflection-agents|Self-Reflection Agents]] — belief revision drives reflection
