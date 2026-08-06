---
type: "concept"
title: "Backward Chaining"
description: "Reasoning from a goal backward to known facts"
tags: ["backward-chaining", "reasoning", "inference", "goals"]
timestamp: "2026-07-31T00:00:00Z"
status: "stub"
---

# Backward Chaining

## Summary
Backward chaining starts from a goal and works backward, finding rules that could prove it and recursively proving their premises. It matters because it focuses inference on what is relevant to the goal. It powers Prolog and many explanation-capable expert systems.

## Details
- Goal-driven: only rules relevant to the current goal fire.
- Produces explanations: the derivation tree is the why.
- Contrast with forward chaining (data-driven).
- Open questions: backward chaining over LLM-generated rules.

## Related
- [[wiki/agent-systems/agent-planning-systems|Agent Planning Systems]] — goal-directed reasoning
- [[wiki/concepts/goal-regression|Goal Regression]] — the planning analog
- [[wiki/concepts/forward-chaining|Forward Chaining]] — the data-driven counterpart
- [[wiki/concepts/abductive-reasoning|Abductive Reasoning]] — backward inference to explanations
- [[wiki/concepts/expert-systems|Expert Systems]] — the classic consumer
