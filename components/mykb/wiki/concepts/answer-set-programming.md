---
type: "concept"
title: "Answer Set Programming"
description: "Declarative programming where solutions are stable models of logic programs"
tags: ["asp", "logic-programming", "reasoning", "constraints"]
timestamp: "2026-07-31T00:00:00Z"
status: "stub"
---

# Answer Set Programming

## Summary
Answer set programming (ASP) expresses problems as logic programs with negation-as-failure, and solvers find stable models that satisfy the rules. It matters because it handles hard combinatorial problems declaratively, including those with exceptions and defaults. It is a cousin of constraint solving.

## Details
- Negation-as-failure gives non-monotonicity for free.
- Model finding is done by dedicated solvers (e.g., clingo).
- Strong for scheduling, configuration, and reasoning tasks.
- Open questions: coupling ASP solvers with LLM problem formulation.

## Related
- [[wiki/concepts/constraint-satisfaction|Constraint Satisfaction]] — the constraint-solving family
- [[wiki/concepts/non-monotonic-logic|Non-Monotonic Logic]] — the logical foundation
- [[wiki/concepts/constraint-logic-programming|Constraint Logic Programming]] — the sister paradigm
- [[wiki/concepts/production-rules|Production Rules]] — rule-based alternative
- [[wiki/concepts/probabilistic-programming|Probabilistic Programming]] — the probabilistic sibling
