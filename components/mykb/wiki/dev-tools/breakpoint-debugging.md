---
type: "concept"
title: "Breakpoint Debugging"
description: "Pausing execution at chosen lines to inspect state interactively"
tags: ["debugging", "breakpoints", "debuggers", "interactive"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Breakpoint Debugging

## Summary
Breakpoint debugging pauses a program at a line or condition so you can inspect variables, step through code, and evaluate expressions. It turns a crash or wrong value into a conversation with the running program — the highest-bandwidth debugging technique for logic errors.

## Details
- Mechanism: the debugger (gdb, lldb, pdb, IDE debuggers) inserts a trap at the target line; when hit, execution suspends; the developer inspects locals, evaluates expressions, and steps — over (next line), into (function body), out (return to caller); watch expressions re-evaluate after every step; conditional breakpoints fire only when a predicate is true.
- Concrete example: a conditional breakpoint on a loop that only fires when the value is null; a watch expression tracking a variable across iterations; stepping into a library call to confirm the argument it receives; post-mortem debugging with pdb/gdb on a core dump or with the crash state loaded.
- Failure modes: breakpoints in hot loops slowing execution to a crawl; conditional expressions with side effects mutating state; debugging optimized builds where variables are optimized out; breakpoints on code that never runs (wrong branch, dead code), wasting time; relying on breakpoints when the bug is in another process or machine.
- Tradeoffs: breakpoints are interactive and powerful but hard to automate and expensive in production — they require a live session or a dump; the alternative, logging and tracing, scales to production but is lower bandwidth; the mature mix is breakpoints locally, structured logging and core dumps remotely.
- Operational notes: pair breakpoint debugging with reproducible tests, and know the post-mortem path for production crashes.
- RSIS3 relevance: interactive breakpoints are how an agent debugs a failing tool call in the loop — pause at the call, inspect inputs, step into the tool.

## Practice
- Operational notes: keep debugger and build in sync (same source revision and symbols), and script breakpoint sessions for reproducible repros instead of relying on memory.
## Related
- [[wiki/dev-tools/debuggers|Debuggers]]
- [[wiki/dev-tools/printf-debugging|Printf Debugging]]
- [[wiki/dev-tools/watchpoints|Watchpoints]]
- [[wiki/dev-tools/core-dumps|Core Dumps]]
- [[wiki/software-engineering/debugging-methodology|Debugging Methodology]]
