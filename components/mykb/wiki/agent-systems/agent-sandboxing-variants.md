---
type: "concept"
title: "Agent Sandboxing Variants"
description: "Different containment strategies for safely executing agent actions"
tags: ["sandboxing", "sandbox", "security", "agents"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Agent Sandboxing Variants

## Summary
Agent sandboxing variants are the different containment strategies used to execute agent actions safely, from full containers to capability-based restrictions. They matter because agents that can run code, browse the web, or touch the filesystem are only as safe as the boundaries around them. The right variant matches containment strength to the risk of the tools being used. Sandbox choice is a risk decision: stronger containment costs more but shrinks the blast radius.

## Details
- **Definition** — sandboxing confines an agent's actions to a controlled environment so that mistakes or malicious behavior cannot escape.
- **Variants** — common options include lightweight containers, full virtual machines, network-restricted sandboxes, and capability-based systems that limit individual permissions.
- **Trade-offs** — stronger isolation costs more overhead and friction; weaker isolation is cheaper but expands the blast radius of any failure.
- **Scope matching** — read-only agents need little isolation, while code-writing agents need full isolation for execution, review, and disposal.
- **Escape testing** — sandboxes should be periodically tested for escape paths as part of agent-runtime-security, because containment failures are critical.
- **Worked example** — a code-repair agent runs tests in a disposable container with no network and a read-only copy of the repository, then discards the container.
- **Failure modes** — shared secrets leaking across sandboxes, resource exhaustion inside containers, and overly permissive default policies are common pitfalls.
- **Evaluation context** — evaluation-sandboxes apply the same idea to offline testing so models can be probed without real-world consequences.
- **Practical relevance** — sandboxing underpins code-execution-environments and is a precondition for trusting agents with powerful tools.
- **Resource limits** — CPU, memory, disk, and network quotas inside the sandbox prevent runaway agents from exhausting host resources.
- **Disposal** — ephemeral sandboxes should be destroyed after runs so secrets and artifacts do not persist.
- **Failure example** — a sandbox with shared network egress lets one compromised agent reach internal services.

## Related
- [[wiki/agent-systems/code-execution-environments|Code Execution Environments]] — the concrete sandbox for running code
- [[wiki/agent-systems/agent-runtime-security|Agent Runtime Security]] — enforcing containment at runtime
- [[wiki/ai-ml/capability-controls|Capability Controls]] — the policy layer above the sandbox
- [[wiki/ai-ml/evaluation-sandboxes|Evaluation Sandboxes]] — sandboxing for evaluation runs
- [[wiki/agent-systems/browser-and-computer-agents|Browser and Computer Agents]] — sandboxing UI-level actions
