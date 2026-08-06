---
type: "concept"
title: "Code Generation Agents"
description: "Agents that plan, write, test, and iterate on code across whole repositories"
tags: ["code-agents", "code", "agents", "generation"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Code Generation Agents

## Summary
Code generation agents plan, write, test, and iterate on code across whole repositories rather than emitting a single file. They use tools for search, execution, and version control, and their success is measured by passing tests and applied diffs, not by the fluency of generated text.

## Details
- **Repo-wide scope** — the agent reads the codebase, finds the right change sites, writes diffs, and runs the relevant tests; single-file completions are a subset of this capability.
- **Tool loop** — search, edit, execute, and version-control tools are composed in an agent loop; each edit is verified before the next is attempted.
- **Verification-first** — success is defined by tests passing and the diff applying cleanly; the agent iterates on failures until the bar is met or the budget is exhausted.
- **Failure modes** — silent breakage elsewhere in the repo, test-only fixes that game the suite, and edits outside the requested scope; CI and diff review catch these.
- **Relationship to other agent types** — code-generation agents are the foundation for code-repair agents (fixing failures) and testing agents (verifying behavior).
- **Safety and execution** — running generated code needs a sandboxed execution environment; the agent never executes arbitrary output on the host.
- **Evaluation** — code benchmarks score patch correctness and test pass rates, and regression suites ensure the agent does not break previously solved tasks.

- **Repository context** — effective agents build a working model of the repo: where things live, conventions, and what depends on what; context quality limits the agent more than model quality.
- **Iteration discipline** — each change is small, verified, and committed separately, so a failing step is isolated and revertible instead of buried in a large diff.
## Related
- [[wiki/agent-systems/code-repair-agents|Code Repair Agents]] — fixing failures
- [[wiki/agent-systems/testing-agents|Testing Agents]] — verification loop
- [[wiki/agent-systems/static-analysis-agents|Static Analysis Agents]] — review layer
- [[wiki/ai-ml/code-benchmarks|Code Benchmarks]] — evaluation
- [[wiki/agent-systems/code-execution-environments|Code Execution Environments]] — safe runtime
- [[wiki/agent-systems/agent-loop|Agent Loop]] — the loop code agents execute
