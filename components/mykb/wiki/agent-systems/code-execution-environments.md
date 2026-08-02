---
type: "concept"
title: "Code Execution Environments"
description: "Isolated runtimes where agents execute code safely and observe results"
tags: ["agents", "code-execution", "sandbox", "runtime"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://github.com/e2b-dev/E2B", "https://github.com/firecracker-microvm/firecracker"]
---

# Code Execution Environments

## Summary
Code execution environments let an agent write and run code, then observe output, errors, and side effects inside an isolated runtime. They turn the agent from a text generator into an experimenter. Isolation is the price of safety: untrusted code runs in a sandbox with resource limits and no access to host secrets.

## Details
- **Isolation tiers** — local subprocess with resource limits, container per session, VM sandboxes (Firecracker), or hosted services like E2B.
- **Interactions** — the agent calls the runtime to execute, receives stdout/stderr and exit codes, and can install packages within the session.
- **Persistence** — a session filesystem lets multi-step coding agents keep state between executions.
- **Security** — network egress controls, execution timeouts, memory limits, and read-only host mounts.
- **Worked example** — a data agent uploads a CSV, runs pandas scripts in a container, and returns the rendered chart and notebook.
- **mykb relevance** — RSIS3's AST-aware patching executes tests in sandboxed environments before committing changes.

## Related
- [[wiki/agent-systems/agent-sandboxing-variants|Agent Sandboxing Variants]] — sandbox approaches for agents
- [[wiki/agent-systems/testing-agents|Testing Agents]] — agents that run tests
- [[wiki/agent-systems/code-generation-agents-revisited|Code Generation Agents]] — agents that write code
- [[wiki/agent-systems/code-repair-agents|Code Repair Agents]] — agents that fix failing code
- [[wiki/agent-systems/simulation-environments-agents|Simulation Environments for Agents]] — executing in simulations
- [[wiki/agent-systems/offline-agent-testing|Offline Agent Testing]] — running code tests in sandboxes
- [[wiki/agent-systems/agent-loop|Agent Loop]] — the loop agents execute
- [[wiki/syntheses/knowledge-system|Knowledge System Overview]] — the KB loop this work feeds
