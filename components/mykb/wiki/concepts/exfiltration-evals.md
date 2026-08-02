---
type: "concept"
title: "Exfiltration Evals"
description: "Testing whether agents exfiltrate data or models"
tags: ["exfiltration", "evals", "security"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Exfiltration Evals

## Summary
Exfiltration evals test whether an agent can copy protected data or weights out of its environment.

## Details
- Exfiltration evals test whether an agent can copy protected data or weights out of its environment.
- Exfiltration is the mechanism for model theft and data leaks.
- Defenses: egress controls, monitoring, and sandboxing.
- RSIS3 relevance: sandboxed workers with bounded scopes reduce exfiltration surface.

## Related
- [[wiki/concepts/self-replication-evals|Self-Replication Evals]] — the replication twin
- [[wiki/syntheses/containment-strategies|Containment Strategies]] — the defense
- [[wiki/agent-systems/agent-sandboxing|Agent Sandboxing]] — the environment
- [[wiki/concepts/training-data-extraction|Training Data Extraction]] — the data side
- [[wiki/concepts/control-protocols|Control Protocols]] — the full treatment of this theme
