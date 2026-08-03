---
type: "concept"
title: "Core Dumps"
description: "Snapshot files of a crashed process's memory for post-mortem debugging"
tags: ["debugging", "core-dumps", "crashes", "forensics"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Core Dumps

## Summary
A core dump captures the full memory of a process at the moment it crashed, letting you inspect stack traces, variables, and heap state later. It is the gold standard for bugs that only reproduce in production — the crash becomes a file you can load into a debugger at leisure.

## Details
- Mechanism: the kernel writes the process image (code, heap, stacks, registers) on crash when enabled (ulimit -c, systemd-coredump, Windows WER); analysis loads the dump with a debugger (gdb, lldb, WinDbg) using the matching binary and debug symbols; the dump contains the exact call stack, local variables, and heap contents at the moment of death.
- Concrete example: a production service segfaults at 3am; systemd stores the coredump; the developer downloads it and runs gdb: bt shows the crashing frame, frame N shows locals, and info registers shows the faulting address; a use-after-free that never reproduced locally becomes reproducible from the dump.
- Failure modes: dumps disabled by default or by the environment, so nothing is captured; dumps containing secrets (tokens, user data) shipped carelessly — sanitize and protect them; missing or mismatched debug symbols making the dump unreadable; huge dumps exhausting disk; core_pattern misconfigurations that overwrite or drop dumps.
- Tradeoffs: core dumps give perfect crash fidelity at the cost of storage, privacy risk, and setup discipline; the alternative — crash reports with stack traces only — is cheaper and privacy-friendlier but loses heap state; the mature pattern is dumps for critical services, with symbols stored and symbolication automated.
- Operational notes: verify dump capture in staging, keep symbol stores in sync with releases, and automate symbolication in the triage pipeline.
- RSIS3 relevance: crash dumps from the Termux wiki tooling can be mailed to dev builds for symbolication — post-mortem debugging turns rare crashes into fixable bugs.

## Related
- [[wiki/dev-tools/crash-reports|Crash Reports]]
- [[wiki/dev-tools/symbolication|Symbolication]]
- [[wiki/dev-tools/breakpoint-debugging|Breakpoint Debugging]]
- [[wiki/shell-environment/shell-scripting-robustness|Shell Scripting Robustness]]
- [[wiki/software-engineering/debugging-methodology|Debugging Methodology]]
