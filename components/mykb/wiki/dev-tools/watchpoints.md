---
type: "concept"
title: "Watchpoints"
description: "Breakpoints that trigger when a memory location or expression changes value"
tags: ["debugging", "watchpoints", "debuggers", "memory"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Watchpoints

## Summary
Watchpoints pause execution when a variable or memory address changes instead of when a line runs. They catch who-mutated-this mysteries that line breakpoints cannot, because the change can happen anywhere.

## Details
- Hardware watchpoints are fast but limited in number; software watchpoints slow execution but are unlimited.
- Watch a field rather than a whole object to cut noise; scope them to a thread when possible.
- Ideal for null-suddenly-appeared and off-by-one corruption bugs in long loops.
- mykb relevance: a watchpoint on a cache key would reveal which code path overwrites a wiki index entry.

## Related
- [[wiki/dev-tools/breakpoint-debugging|Breakpoint Debugging]]
- [[wiki/dev-tools/debuggers|Debuggers]]
- [[wiki/dev-tools/core-dumps|Core Dumps]]
- [[wiki/software-engineering/debugging-methodology|Debugging Methodology]]
- [[wiki/dev-tools/symbolication|Symbolication]]
