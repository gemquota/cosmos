---
type: "concept"
title: "Non-Monotonic Logic"
description: "Logics where adding premises can invalidate earlier conclusions"
tags: ["non-monotonic-logic", "logic", "reasoning", "knowledge-representation"]
timestamp: "2026-07-31T00:00:00Z"
status: "stub"
---

# Non-Monotonic Logic

## Summary
Non-monotonic logic formalizes reasoning where new information can retract previous conclusions — unlike classical logic, where adding premises never removes theorems. It matters because agent reasoning in open worlds is inherently non-monotonic. It underpins default logic, circumscription, and answer-set programming.

## Details
- Default rules, closed-world assumption, and autoepistemic reasoning.
- ASP is a practical, computational embodiment.
- Agents revise beliefs exactly because inference is non-monotonic.
- Open questions: integrating non-monotonic rules with LLM inference.

## Related

- [[wiki/concepts/defeasible-reasoning|Defeasible Reasoning]] — the applied counterpart
- [[wiki/concepts/answer-set-programming|Answer Set Programming]] — the computational embodiment
- [[wiki/concepts/abductive-reasoning|Abductive Reasoning]] — non-monotonic hypothesis inference
- [[wiki/concepts/belief-states|Belief States]] — revising what is believed
- [[wiki/llm-agents/self-reflection-agents|Self-Reflection Agents]] — belief revision drives reflection
