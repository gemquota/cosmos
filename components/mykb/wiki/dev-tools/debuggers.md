---
type: "concept"
title: "Debuggers"
description: "Tools that pause and inspect a running program to understand its state at a specific moment"
tags: ["debugging", "tools", "breakpoints", "state"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://en.wikipedia.org/wiki/Debugger", "https://sourceware.org/gdb/", "https://lldb.llvm.org/"]
---

# Debuggers

## Summary
A debugger runs a program under inspection, letting you set breakpoints, step through code, and examine variables and call stacks. It turns 'why is this wrong?' into a question answerable from live state.

## Details
- Modern debuggers support conditional breakpoints, watch expressions, and remote attach.
- Logging and debuggers complement each other: logs tell history, debuggers tell present state.
- RSIS3 relevance: replaying agent sessions through a trace debugger is a roadmap for mykb.
- A debugger lets you pause a program at breakpoints, inspect state, and step through execution to find where behavior diverges from intent.
- Core operations — breakpoints, watch expressions, call stacks, and variable inspection — turn a mystery into an experiment.
- Debuggers shine on logical errors; they help less with race conditions, which need tracing and reproduction, and with production issues that need post-mortem tooling.
- The modern form is interactive and language-rich (IDE integration, remote debugging, REPL inspection).
- **Worked example / comparison** — Worked example — a wiki export fails on one article; a breakpoint at the parser shows the malformed frontmatter value, and stepping through confirms the exact failing branch.
- For mykb, debuggers are documented as the interactive complement to git-bisect and logging in the debugging toolkit.

## Related
- [[wiki/dev-tools/git-bisect|Git Bisect]]
- [[wiki/dev-tools/repl-driven-development|Repl-Driven Development]]
- [[wiki/llm-agents/traceability|Traceability]]
- [[wiki/software-engineering/code-review|Code Review]]
- [[wiki/devops-infra/observability|Observability]]
- [[wiki/concepts/promotion-readiness|Promotion Readiness]]
- [[wiki/dev-tools/global-link-check|Global Link Check]]
- [[wiki/concepts/explainers|Explainers]]
