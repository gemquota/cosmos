---
type: "concept"
title: "Debuggers"
description: "Tools that pause and inspect a running program to understand its state at a specific moment"
tags: ["debugging", "tools", "breakpoints", "state"]
timestamp: "2026-08-01T00:00:00Z"
status: "stub"
---

# Debuggers

## Summary
A debugger runs a program under inspection, letting you set breakpoints, step through code, and examine variables and call stacks. It turns 'why is this wrong?' into a question answerable from live state.

## Details
- Modern debuggers support conditional breakpoints, watch expressions, and remote attach.
- Logging and debuggers complement each other: logs tell history, debuggers tell present state.
- RSIS3 relevance: replaying agent sessions through a trace debugger is a roadmap for mykb.

## Related
- [[wiki/dev-tools/git-bisect|Git Bisect]] — bisect finds the change; the debugger finds the bug
- [[wiki/dev-tools/repl-driven-development|Repl-Driven Development]] — REPLs blur the line between running and debugging
- [[wiki/llm-agents/traceability|Traceability]] — agent traceability is debugging for LLM pipelines
- [[wiki/software-engineering/code-review|Code Review]] — review catches bugs before debugging is needed
- [[wiki/devops-infra/observability|Observability]] — debugging uses observable system state
