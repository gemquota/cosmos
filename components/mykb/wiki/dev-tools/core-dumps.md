---
type: "concept"
title: "Core Dumps"
description: "Snapshot files of a crashed process's memory for post-mortem debugging"
tags: ["debugging", "core-dumps", "crashes", "forensics"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Core Dumps

## Summary
A core dump captures the full memory of a process at the moment it crashed, letting you inspect stack traces, variables, and heap state later. It is the gold standard for bugs that only reproduce in production.

## Details
- Enable core dumps deliberately (ulimit -c, systemd coredump) and protect them from leaking secrets.
- Symbols and the matching binary are needed to make a dump readable — keep debug symbols in sync.
- Analyze with gdb/lldb post-mortem: bt for the stack, frame n for locals, info registers for state.
- mykb relevance: crash dumps from the Termux wiki tooling can be mailed to dev builds for symbolication.

## Related
- [[wiki/dev-tools/crash-reports|Crash Reports]]
- [[wiki/dev-tools/symbolication|Symbolication]]
- [[wiki/dev-tools/breakpoint-debugging|Breakpoint Debugging]]
- [[wiki/shell-environment/shell-scripting-robustness|Shell Scripting Robustness]]
- [[wiki/software-engineering/debugging-methodology|Debugging Methodology]]
