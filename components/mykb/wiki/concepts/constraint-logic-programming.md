---
type: "concept"
title: "Constraint Logic Programming"
description: "Logic programming extended with constraint solving over domains"
tags: ["clp", "logic-programming", "constraints", "reasoning"]
timestamp: "2026-07-31T00:00:00Z"
status: "growing"
---

# Constraint Logic Programming

## Summary
Constraint logic programming (CLP) embeds constraint solving into logic programming: variables can be constrained over domains (integers, reals, booleans) and the solver prunes search. It matters because it cleanly combines declarative rules with efficient domain reasoning. Prolog systems like SWI-Prolog and SICStus ship CLP libraries.

## Details
- The key mechanism is propagation: instead of enumerating values, the program states relationships between variables, and each constraint's propagator removes impossible values from the variables' domains. As constraints accumulate, domains shrink and search space collapses. For example, `X #> 3, X #< 7` on an integer domain narrows X to {4,5,6} before any search occurs — and when only one value remains, the solver assigns it and propagates the consequences.
- Programs state relationships; the solver finds satisfying assignments. The user writes the problem as facts and rules — "meeting A must precede meeting B", "no more than two meetings per room per hour" — and the CLP system handles the combinatorial search, using depth-first search over the pruned domains with constraint propagation at every node. Because the search is separate from the model, changing the constraints does not require rewriting the algorithm.
- The domains give it its power: CLP(FD) handles integers with arithmetic constraints (the workhorse for scheduling and timetabling), CLP(R) handles real arithmetic for numerical problems like circuit analysis and option pricing, and CLP(B) handles boolean formulas for logic puzzles and digital-circuit verification. SWI-Prolog and SICStus ship these as libraries, so Prolog programmers get constraint solving without leaving the logic-programming paradigm.
- Strong application areas are scheduling, timetabling, rostering, resource allocation, and verification, where the constraints are numerous and the search space is astronomical — exactly the cases where naive generate-and-test fails. The tradeoff is that propagation quality depends on the constraint system's design: poorly written constraints propagate weakly and the solver degenerates into blind search, while redundant constraints can dramatically speed up (or slow down) solving depending on the propagation cost.
- RSIS3 relevance: RSIS3's constraint registry is a CLP problem in waiting. Invariants like workspace disjointness and telemetry coverage can be modeled as integer and boolean constraints over loop state, letting the system ask the solver "which states are reachable without violating practices?" before running an experiment.

## Related
- [[wiki/concepts/constraint-satisfaction|Constraint Satisfaction]] — the underlying problem class
- [[wiki/concepts/answer-set-programming|Answer Set Programming]] — the sibling paradigm
- [[wiki/concepts/probabilistic-programming|Probabilistic Programming]] — uncertainty in programs
- [[wiki/concepts/production-rules|Production Rules]] — rule-based reasoning alternative
- [[wiki/concepts/forward-chaining|Forward Chaining]] — propagation-style inference
