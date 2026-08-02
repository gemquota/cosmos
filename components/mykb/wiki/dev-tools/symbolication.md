---
type: "concept"
title: "Symbolication"
description: "Mapping crash-time addresses back to function names and source lines"
tags: ["debugging", "symbols", "crashes", "tooling"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Symbolication

## Summary
Symbolication translates raw addresses and mangled names in a crash report into readable function names, file names, and line numbers. Without it, a stack trace is just hex addresses.

## Details
- Debug symbols (DWARF, PDB) map addresses to source; strip them from release binaries but keep them for analysis.
- Upload symbol files to the crash reporter at release time so reports symbolize automatically.
- Mismatched symbol versions produce garbage stacks — tag builds and symbols with the same hash.
- mykb relevance: symbolicated agent crash stacks make debugging a failed tool invocation tractable.

## Related
- [[wiki/dev-tools/crash-reports|Crash Reports]]
- [[wiki/dev-tools/core-dumps|Core Dumps]]
- [[wiki/dev-tools/error-tracking-tools|Error Tracking Tools]]
- [[wiki/software-engineering/debugging-methodology|Debugging Methodology]]
- [[wiki/dev-tools/breakpoint-debugging|Breakpoint Debugging]]
