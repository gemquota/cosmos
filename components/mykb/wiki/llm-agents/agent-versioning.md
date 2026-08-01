---
type: "concept"
title: "Agent Versioning"
description: "Tracking versions of agent code, prompts, policies, and identity"
tags: ["agent-versioning", "versioning", "config", "agents"]
timestamp: "2026-07-31T00:00:00Z"
status: "stub"
---

# Agent Versioning

## Summary
Agent versioning treats the whole agent — code, prompts, tool configs, policies, persona — as a versioned artifact. It matters because agents drift silently, and reproducibility requires knowing exactly what ran. Versioning is the precondition for rollback and comparison.

## Details
- Version the full bundle, not just the model weights.
- Tag every run with its agent version for telemetry.
- Enables A/B comparison and safe rollback.
- Open questions: semantic versioning rules for prompt changes.

## Related
- [[wiki/agent-systems/rollback-and-recovery|Rollback and Recovery]] — reverting to a version
- [[wiki/llm-agents/deterministic-replay|Deterministic Replay]] — replay needs version fidelity
- [[wiki/agent-systems/identity-and-continuity|Identity and Continuity]] — versioned identity changes
- [[wiki/llm-agents/agent-logs|Agent Logs]] — logs record the version
- [[wiki/llm-agents/traceability|Traceability]] — linking outcomes to versions
