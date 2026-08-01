---
type: "concept"
title: "Constraint Logic Programming"
description: "Logic programming extended with constraint solving over domains"
tags: ["clp", "logic-programming", "constraints", "reasoning"]
timestamp: "2026-07-31T00:00:00Z"
status: "stub"
---

# Constraint Logic Programming

## Summary
Constraint logic programming (CLP) embeds constraint solving into logic programming: variables can be constrained over domains (integers, reals, booleans) and the solver prunes search. It matters because it cleanly combines declarative rules with efficient domain reasoning. Prolog systems like SWI-Prolog and SICStus ship CLP libraries.

## Details
- Programs state relationships; the solver finds satisfying assignments.
- Propagators reduce domains as constraints accumulate.
- Strong for scheduling, timetabling, and verification tasks.
- Open questions: CLP with LLM-generated constraint models.

## Related
- [[wiki/concepts/constraint-satisfaction|Constraint Satisfaction]] — the underlying problem class
- [[wiki/concepts/answer-set-programming|Answer Set Programming]] — the sibling paradigm
- [[wiki/concepts/probabilistic-programming|Probabilistic Programming]] — uncertainty in programs
- [[wiki/concepts/production-rules|Production Rules]] — rule-based reasoning alternative
- [[wiki/concepts/forward-chaining|Forward Chaining]] — propagation-style inference
