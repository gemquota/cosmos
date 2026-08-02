---
type: "concept"
title: "Kernel Rewriting"
description: "Replacing or rewriting the core layer of a system while it runs"
tags: ["kernel", "rewriting", "systems", "self-modification"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://en.wikipedia.org/wiki/Kernel_(operating_system)", "https://en.wikipedia.org/wiki/Microkernel"]
---

# Kernel Rewriting

## Summary
Kernel rewriting replaces the core — OS kernel, framework runtime, or agent's control layer — with a new implementation, often live. It is the deepest form of self-modification: change the foundation, and every layer above changes with it.

## Details
- **Live patching** — Linux kpatch and similar mechanisms update kernels without reboot, minimizing downtime and risk windows.
- **Why hard** — the kernel manages the resources used to perform the update; state must be preserved and errors must be recoverable.
- **Self-improvement angle** — a system that rewrites its own foundation can improve its entire stack, but a bug propagates everywhere.
- **Safety practices** — shadow deployments, staged rollouts, and rollback kernels.
- **RSIS3 parallel** — schema migrations and practice-checker rewrites are kernel-rewriting for the knowledge graph.

## Related
- [[wiki/concepts/self-modifying-systems|Self-Modifying Systems]] — the substrate
- [[wiki/decisions/auto-update-mechanisms|Auto-Update Mechanisms]] — the delivery channel
- [[wiki/syntheses/update-regression|Update Regression]] — the risk
- [[wiki/agent-systems/rollback-and-recovery|Rollback and Recovery]] — the safety net
- [[wiki/decisions/bootstrapping-compilers|Bootstrapping Compilers]] — the software sibling
- [[wiki/agent-systems/rollback-and-recovery|Rollback and Recovery]] — recovery practice
- [[wiki/decisions/checkpoint-selection|Checkpoint Selection]] — choosing states
