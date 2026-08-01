---
type: "concept"
title: "Repl-Driven Development"
description: "Building software by exploring behavior interactively in a read-eval-print loop"
tags: ["repl", "workflow", "interactive", "exploration"]
timestamp: "2026-08-01T00:00:00Z"
status: "stub"
---

# Repl-Driven Development

## Summary
Repl-driven development (RDD) writes code incrementally against a live interpreter: try an expression, inspect results, promote what works into the codebase. It shines for data munging, APIs, and exploratory programming.

## Details
- The REPL is the fastest feedback loop in programming; Lisp, Python, and Clojure cultures embrace it.
- RDD pairs with notebooks and with `python -i`, `node`, and `irb`.
- RSIS3 relevance: agent sessions are REPL-like — act, observe, adapt.

## Related
- [[wiki/os-shell/command-line-interfaces|Command-Line Interfaces]] — the shell is the original REPL
- [[wiki/dev-tools/profilers|Profilers]] — REPL inspection and profiling combine
- [[wiki/software-engineering/functional-programming|Functional Programming]] — pure functions shine in REPL exploration
- [[wiki/concepts/inner-outer-loop-learning|Inner/Outer Loop Learning]] — the interactive loop analog for agents
- [[wiki/agent-systems/action-observation-loop|Action-Observation Loop]] — REPL is an act-observe loop
