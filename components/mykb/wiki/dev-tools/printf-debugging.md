---
type: "concept"
title: "Printf Debugging"
description: "Inserting print statements to observe program state at chosen points"
tags: ["debugging", "technique", "basics"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Printf Debugging

## Summary
Printf debugging — scattering print statements through code to see values and flow — is the oldest debugging technique and often the fastest first move. It works anywhere and requires no tooling, at the cost of code churn, noise, and its blindness to timing and concurrency.

## Details
- Mechanism: insert prints at function entry, at key values, and at branch outcomes; label output so it is greppable; run, observe, and remove or gate the prints; the technique is essentially a manual trace of the program's state over time.
- Concrete example: a generated article looks wrong — printf the template variables at each stage to find the first divergence between expected and actual values; a parse failure — print the input and the parser's intermediate state; a script misbehaving — print each command's exit status.
- Failure modes: prints in hot loops, flooding output and slowing the run; printing to the wrong stream or interleaving across threads, scrambling the story; leaving prints behind, polluting logs and code; printf being useless for timing (timestamps needed), deep recursion (volume), and concurrency (ordering); prints that mutate state or formatting that changes behavior.
- Tradeoffs: printf is universally available and zero-setup, making it the fastest first probe; the alternative, a debugger, gives richer inspection and no code churn but requires setup and interactive time; the mature pattern is printf for the first hypothesis and a debugger or logging for the deep dive.
- Operational notes: prefer labeled logging calls over raw prints so the instrumentation survives, and gate temporary output behind a flag.
- RSIS3 relevance: when a generated article looks wrong, printf the template variables to find the first divergence — the simplest tool in the debugging ladder RSIS3 uses.

- Pair prints with unique sentinel labels so the debug output is greppable and removable in one pass.
## Related
- [[wiki/dev-tools/debug-logging|Debug Logging]]
- [[wiki/dev-tools/breakpoint-debugging|Breakpoint Debugging]]
- [[wiki/dev-tools/debuggers|Debuggers]]
- [[wiki/software-engineering/debugging-methodology|Debugging Methodology]]
- [[wiki/dev-tools/repl-driven-development|REPL-Driven Development]]
