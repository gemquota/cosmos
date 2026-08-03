---
type: "concept"
title: "Agent Sandboxing"
description: "Isolating agent execution to contain mistakes and hostile input"
tags: ["sandbox", "security", "isolation", "agents", "execution"]
timestamp: "2026-07-31T00:00:00Z"
status: "growing"
source: ["https://gvisor.dev/docs/"]
---

# Agent Sandboxing

## Summary
Sandboxing is the practice of running agent actions in an isolated environment — separate filesystem, network, and process boundaries — so that a buggy or malicious action cannot damage the host. It matters because agents execute arbitrary commands, and containment is the backstop when permission checks fail. Lightweight runtimes like gVisor provide strong isolation with near-native performance.

## Details
- **Isolation layers**: containers, user namespaces, seccomp filters, read-only filesystems, network egress control.
- **Least privilege**: the sandbox grants only the resources the task needs, plus logging of everything it does.
- **Reproducibility**: clean sandboxes make runs deterministic and replayable.
- Trade-off: isolation costs setup time and can break tools that need real credentials — solved with scoped secrets.
- RSIS3 runs shell work through bounded tools with restricted paths (its wiki write scope is itself a sandbox rule).
- Worked example: a code-generation agent executes tests inside a container with network off; the host stays untouched.

## Related

- [[wiki/llm-agents/permission-model|Permission Model]] — authorization that complements isolation
- [[wiki/llm-agents/approval-gates|Approval Gates]] — human review for sandboxed high-risk actions
- [[wiki/llm-agents/policy-enforcement|Policy Enforcement]] — runtime checks inside the sandbox
