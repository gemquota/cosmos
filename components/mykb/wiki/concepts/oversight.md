---
type: "concept"
title: "Oversight"
description: "Mechanisms for monitoring, reviewing, and correcting AI behavior"
tags: ["oversight", "safety", "governance", "supervision"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://en.wikipedia.org/wiki/Reinforcement_learning_from_human_feedback", "https://arxiv.org/abs/2206.05862"]
---

# Oversight

## Summary
Oversight is the human and institutional practice of watching AI systems: monitoring outputs, reviewing plans, auditing incidents, and intervening. It is the operational complement to alignment — the assumption being that models will sometimes be wrong and someone must catch it.

## Details
- **Levels** — runtime monitoring (telemetry, tripwires), review (audits, red teams), and structural (approval gates, sandboxing).
- **Scalability problem** — humans cannot review every action of fast, parallel agents, motivating scalable oversight.
- **Failure modes** — oversight bottleneck, rubber-stamping, and capture of the overseer by the system's incentives.
- **Evidence** — RLHF and RLAIF both implement oversight over behavior via human or AI feedback.
- **RSIS3 example** — the knowledge daemon logs and the weekly review ritual are oversight layers over automatic acquisition.

## Related
- [[wiki/concepts/scalable-oversight|Scalable Oversight]] — when humans can't keep up
- [[wiki/concepts/oversight-bottleneck|Oversight Bottleneck]] — the constraint
- [[wiki/concepts/human-supervision-limits|Human Supervision Limits]] — why oversight needs help
- [[wiki/syntheses/audit-frameworks-ai|AI Audit Frameworks]] — institutional layer
- [[wiki/agent-systems/telemetry-for-agents|Telemetry for Agents]] — monitoring substrate
- [[wiki/syntheses/weekly-review|Weekly Review]] — RSIS3 review practice
