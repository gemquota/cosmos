---
type: "concept"
title: "Repl-Driven Development"
description: "Building software by exploring behavior interactively in a read-eval-print loop"
tags: ["repl", "workflow", "interactive", "exploration"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
---

# Repl-Driven Development

## Summary
Repl-driven development (RDD) writes code incrementally against a live interpreter: try an expression, inspect results, promote what works into the codebase. It shines for data munging, APIs, and exploratory programming, where the fastest feedback loop wins.

## Details
- Mechanism: a REPL (read-eval-print loop) evaluates expressions against live state; the developer experiments, inspects intermediates, and iterates without a build-test cycle; what works gets promoted into functions and tests; notebooks and `python -i`, `node`, `irb` are the same idea in different skins.
- Concrete example: parsing a new wiki format — load a sample, inspect the parse tree, try transformations, then promote the working snippet into the parser module; debugging an API call — construct the request interactively, inspect the response, then codify it as a test; the shell itself is the original REPL for files and processes.
- Failure modes: REPL state drifting from the codebase — the working snippet depends on REPL-only variables and fails when promoted; long-lived REPL sessions accumulating stale state, leading to wrong conclusions; exploration that never gets promoted, leaving knowledge in a session instead of code; REPL habits (no tests, no types) leaking into production code.
- Tradeoffs: RDD gives the tightest feedback loop for exploratory work at the cost of discipline — the session is ephemeral and must be distilled into code and tests; the alternative, write-then-run, is slower and safer; the mature pattern is REPL for exploration, then immediately promote and test.
- Operational notes: keep sessions reproducible (restart before concluding), and treat any REPL-discovered behavior as a candidate test.
- RSIS3 relevance: agent sessions are REPL-like — act, observe, adapt — and RDD is the human analog of the loop RSIS3 runs.

## Related
- [[wiki/os-shell/command-line-interfaces|Command-Line Interfaces]] — the shell is the original REPL
- [[wiki/dev-tools/profilers|Profilers]] — REPL inspection and profiling combine
- [[wiki/software-engineering/functional-programming|Functional Programming]] — pure functions shine in REPL exploration
- [[wiki/concepts/inner-outer-loop-learning|Inner/Outer Loop Learning]] — the interactive loop analog for agents
- [[wiki/agent-systems/action-observation-loop|Action-Observation Loop]] — REPL is an act-observe loop
