---
type: "concept"
title: "Breakpoint Debugging"
description: "Pausing execution at chosen lines to inspect state interactively"
tags: ["debugging", "breakpoints", "debuggers", "interactive"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Breakpoint Debugging

## Summary
Breakpoint debugging pauses a program at a line or condition so you can inspect variables, step through code, and evaluate expressions. It turns a crash or wrong value into a conversation with the running program.

## Details
- Conditional breakpoints fire only when an expression is true — essential for loops and hot paths.
- Step over, step into, and step out navigate the call stack; watch expressions track changing values.
- Post-mortem debugging (pdb on a core dump, lldb) applies breakpoint techniques to already-crashed runs.
- RSIS3 relevance: interactive breakpoints are how an agent debugs a failing tool call in the loop.

## Related
- [[wiki/dev-tools/debuggers|Debuggers]]
- [[wiki/dev-tools/printf-debugging|Printf Debugging]]
- [[wiki/dev-tools/watchpoints|Watchpoints]]
- [[wiki/dev-tools/core-dumps|Core Dumps]]
- [[wiki/software-engineering/debugging-methodology|Debugging Methodology]]
