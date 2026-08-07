---
type: "concept"
title: "Agent Runtime Security"
description: "Securing the environment agents execute in, including sandboxes, secrets, and tools"
tags: ["agents", "security", "sandboxing", "runtime"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://github.com/firecracker-microvm/firecracker", "https://docs.anthropic.com/en/docs/build-with-claude/tool-use"]
---

# Agent Runtime Security

## Summary
Agent runtime security isolates what an agent can touch: filesystem, network, credentials, and side effects. Because agents chain tool calls autonomously, a single compromised prompt can trigger dangerous actions. The runtime must enforce the agent's permissions even when the model is manipulated.

## Details
- **Sandboxing** — containers, VM-based isolation like Firecracker, or OS-level sandboxes (nsjail, seccomp) constrain the agent's blast radius.
- **Secrets** — API keys and credentials live in a secrets manager, injected per-call with scoped permissions, never in prompts or logs.
- **Tool permissions** — each tool declares its sensitivity; the runtime enforces allowlists, and approval gates cover destructive tools.
- **Prompt injection defense** — untrusted content is treated as data; the runtime validates tool calls against schemas before execution.
- **Worked example** — a browser agent runs in a container without write access to the host, with network egress allowlisted and credentials injected per session.
- **mykb relevance** — agent sandboxing and the permission model are existing mykb topics; RSIS3's code generation uses sandboxed execution for the same reason.

- **Defense in depth** — sandbox, tool permissions, secret scoping, and egress controls compose; any single layer can fail, so each layer must be independent.
- **Audit trail** — every tool invocation, permission decision, and denial is logged; the trail is what makes post-incident analysis possible.
- **Least privilege by default** — agents start with minimal permissions and escalate only through explicit gates, reversing the default as trust is earned.
- **Supply chain** — the runtime itself must be verifiable: pinned images, signed tools, and reproducible builds prevent compromise before the agent even starts.
## Related
- [[wiki/agent-systems/agent-sandboxing|Agent Sandboxing]] — sandboxing agents
- [[wiki/agent-systems/agent-sandboxing-variants|Agent Sandboxing Variants]] — sandbox approaches
- [[wiki/llm-agents/permissioning-and-approvals|Permissioning and Approvals]] — enforcing permissions
- [[wiki/llm-agents/api-key-management-llm|API Key Management for LLMs]] — credential handling
- [[wiki/prompt-engineering/prompt-injection-defense|Prompt Injection Defense]] — defending the runtime from prompt attacks
- [[wiki/agent-systems/code-execution-environments|Code Execution Environments]] — safe code execution
- [[wiki/testing/secure-enclaves-inference|Secure Enclaves for Inference]] — hardened execution
- [[wiki/security/secrets-management|Secrets Management]] — secret storage patterns
