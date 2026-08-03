---
type: "concept"
title: "Answer Set Programming"
description: "Declarative problem solving via stable-model semantics"
tags: ["logic-programming", "answer-set-programming", "declarative"]
timestamp: "2026-07-31T00:00:00Z"
status: "growing"
---

# Answer Set Programming

## Summary
Answer set programming (ASP) is a declarative programming paradigm for solving hard combinatorial search problems. You write a description of what a valid solution looks like — rules and constraints — and an ASP solver computes the answer sets, which are the stable models satisfying the program. The programmer specifies the problem, not the algorithm.

## Details
- A program consists of facts, rules, and constraints. A rule has the form `head :- body`, meaning the head holds when the body holds; constraints are rules with an empty head that forbid certain combinations; and choice rules let the solver decide a range of truth values. The stable-model semantics resolve negation: an atom is false unless a rule deriving it can be supported by an acyclic derivation, which eliminates the self-referential cycles that plague naive negation handling in logic programming.
- This makes ASP naturally non-monotonic. Adding a constraint can remove answer sets, which is the opposite of classical logic and exactly what you want when modeling defaults ("birds fly unless penguin") or closed-world reasoning. Solvers like clingo and DLV ground the program into a propositional form and then search for stable models, using conflict-driven learning, unfounded-set pruning, and heuristics to tame exponential blowup.
- The sweet spot is NP-complete problems in configuration, scheduling, planning, diagnosis, and bioinformatics: graph problems such as Hamiltonian paths, constraint satisfaction, and combinatorial optimization all have compact, readable ASP encodings. The tradeoff is that grounding cost explodes with data size, so ASP is strongest when the problem structure is rich but the instance domain is bounded.
- Failure modes include runaway grounding (a small rule can generate a huge propositional program), non-termination from recursive rules with unguarded variables, and debugging difficulty because an unexpected answer set may mean the model is wrong in subtle ways rather than the solver.
- RSIS3 relevance: constraint tracking in the RSIS3 loops is a natural ASP target. Invariants such as "no two active improvement proposals may modify the same state file" or "telemetry must be recorded for every loop pass" can be expressed as constraints and checked with an ASP solver, giving declarative enforcement of registry invariants.

## Related
- [[wiki/concepts/constraint-logic-programming|Constraint Logic Programming]] — neighboring paradigm
- [[wiki/concepts/non-monotonic-logic|Non-Monotonic Logic]] — the underlying semantics
- [[wiki/concepts/production-rules|Production Rules]] — rule systems with different execution model
- [[wiki/concepts/expert-systems|Expert Systems]] — classic rule-based reasoning
- [[wiki/concepts/forward-chaining|Forward Chaining]] — alternative inference strategy
- [[wiki/concepts/constraint-satisfaction|Constraint Satisfaction]]
- [[wiki/concepts/probabilistic-programming|Probabilistic Programming]]
