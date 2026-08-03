---
type: "concept"
title: "Remote Development: VS Code & SSH"
description: "Editing code on remote hosts with VS Code Remote and SSH"
tags: ["vscode", "ssh", "remote-development", "tooling"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Remote Development: VS Code & SSH

## Summary
Remote development with VS Code SSH attaches a full editor experience — IntelliSense, debugging, terminals, extensions — to code running on a remote machine or container, while files stay where the compute is. It separates the editing environment from the execution environment, making large repos, powerful servers, and consistent toolchains practical.

## Details
- Mechanism: the VS Code client connects over SSH; the server component installs on the remote, runs extensions remotely, and synchronizes UI state locally; port forwarding exposes remote services locally; settings can differ per remote; devcontainers extend the idea by defining the remote environment in the repo.
- Concrete example: a developer edits the cosmos repo on a remote workstation or VM with the full Python toolchain, while the wiki daemon runs on the same host; a large monorepo is cloned once remotely, and a local laptop only renders the editor; a devcontainer defines the remote toolchain, so every developer gets the same environment.
- Failure modes: latency — every keystroke and file operation crosses the network, so a bad connection makes the editor unusable (use reliable networks or an intermediary jump host); SSH key and agent-forwarding issues blocking auth; extension incompatibilities between local and remote versions; workspace sync conflicts when the same folder is opened from multiple places; remote toolchain divergence from local assumptions.
- Tradeoffs: remote dev centralizes compute and environment consistency at the cost of network dependence and latency; the alternative — local dev with setup scripts — is responsive but drifts and burdens contributors; the middle path is devcontainers plus remote hosting for heavy workloads and local fallback for light edits.
- Operational notes: pin the remote toolchain, document the SSH setup, and keep the repo's devcontainer the single source of truth.
- RSIS3 relevance: cosmos's multi-component repo benefits from a defined remote dev setup so any contributor's loop runs against the same toolchain as CI.

## Related
- [[wiki/cloud-infra/remote-access-methods|Remote Access Methods]]
- [[wiki/infrastructure/ssh-tunneling-and-port-forwarding|SSH Tunneling & Port Forwarding]]
- [[wiki/os-shell/ssh-and-remote-access|SSH & Remote Access]]
- [[wiki/infrastructure/ssh-key-management|SSH Key Management]]
- [[wiki/devops-infra/kubernetes-control-plane|Kubernetes Control Plane]]
- [[wiki/devops-infra/observability-pillars|Observability Pillars]]
- [[wiki/syntheses/knowledge-acquisition-workflow|Knowledge Acquisition Workflow]] — how stubs grow into full articles in mykb
- [[wiki/syntheses/mykb-acquisition-curation-and-practices|Acquisition, Curation & Practices]] — the curation loop this stub belongs to
