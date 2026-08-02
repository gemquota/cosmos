---
type: "concept"
title: "Printf Debugging"
description: "Inserting print statements to observe program state at chosen points"
tags: ["debugging", "technique", "basics"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Printf Debugging

## Summary
Printf debugging — scattering print statements through code to see values and flow — is the oldest debugging technique and often the fastest first move. It works anywhere and requires no tooling, at the cost of code churn and noise.

## Details
- Print function entry, key values, and branch outcomes; label output so it is greppable.
- Printf is a poor fit for timing, deep recursion, and concurrency — use a debugger there.
- Remove or gate the prints before commit; consider logging calls instead of raw prints.
- mykb relevance: when a generated article looks wrong, printf the template variables to find the first divergence.

## Related
- [[wiki/dev-tools/debug-logging|Debug Logging]]
- [[wiki/dev-tools/breakpoint-debugging|Breakpoint Debugging]]
- [[wiki/dev-tools/debuggers|Debuggers]]
- [[wiki/software-engineering/debugging-methodology|Debugging Methodology]]
- [[wiki/dev-tools/repl-driven-development|REPL-Driven Development]]
