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

- **Isolation boundaries** — filesystem (read-only host, tmpfs workdir), network (egress allowlist or none), and process (user namespaces, seccomp) boundaries compose to define the blast radius.
- **Escaping is the threat model** — sandboxes are tested by attempted escapes: path traversal, symlink tricks, environment leakage, and side channels; escape tests belong in CI.
- **State lifecycle** — ephemeral sandboxes are wiped after each run unless artifacts are explicitly exported, preventing cross-run contamination.
- **Verification** — the sandbox config is validated against a checklist before use: no host mounts, no privileged mode, no writable secrets.
- **Approval pairing** — sandboxing contains the damage, but high-impact actions still pass an approval gate so a human decides on the boundary between contained and destructive.
- **Logging inside the sandbox** — capture commands, outputs, and file changes from inside the sandbox so the audit trail survives even when the sandbox is destroyed.
## Related

- [[wiki/llm-agents/permission-model|Permission Model]] — authorization that complements isolation
- [[wiki/llm-agents/approval-gates|Approval Gates]] — human review for sandboxed high-risk actions
- [[wiki/llm-agents/policy-enforcement|Policy Enforcement]] — runtime checks inside the sandbox
