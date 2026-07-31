---
type: "concept"
title: "RSIS3 Identity System"
description: "Self-model with genesis hash, layer scores, crisis detection, and value reinforcement"
tags: ["identity", "self-model", "genesis", "crisis", "values", "rsis3"]
timestamp: "2026-07-21T10:02:00Z"
---


## Identity System

# Identity System

RSIS3's identity system is a structured self-model that persists personality across restarts and guides decision-making.

## Components

### SelfModel
- **Genesis hash** — SHA-256 of the first SelfModel initialization. Stored in `.genesis_hash`. Mismatch detection on reload.
- **Layer scores** — 6 capability layers (L1-L6) scored 0-100
- **Narrative** — Self-description of current state and goals
- **Value axioms** — Hard constraints derived from reinforcement

### CrisisMonitor
- Detects anomalies: sudden layer score drops, repeated test failures, identity drift
- Triggers crisis mode when thresholds exceeded
- Crisis resolution is highest-priority goal

### ValueReinforcementTracker
- Tracks which values are reinforced or violated by decisions
- Extracts axioms from repeated reinforcement patterns
- Axioms become locked constraints in RRP

### Snapshot System
- Periodic snapshots of full identity state
- Stored in mykb wiki (wiki/identity/) and SQLite
- Enables rollback to previous identity state

## Layer Architecture

| Layer | Name | Purpose |
|-------|------|---------|
| L1 | Blue | Foundation — half width |
| L2 | Green | Top priority |
| L3 | Yellow | Visible — self-direction |
| L4 | Red | Hidden — settings |
| L5 | Purple | Visible |
| L6 | Teal | Visible |

## mykb Integration

Identity continuously writes to mykb:
- Decisions → wiki/decisions/
- Snapshots → wiki/identity/
- Crisis events → wiki/decisions/ with crisis tag
- Value axioms → wiki/concepts/

**Domain:** Concepts

## Related

- [[wiki/concepts/mykb-analysis|Mykb Analysis]]
- [[wiki/concepts/mykb-research-report|Mykb Research Report]]
- [[wiki/concepts/mykb-implementation-report|Mykb Implementation Report]]
- [[wiki/concepts/triad-architecture|Triad Architecture]]
- [[wiki/concepts/pulse-cycle|Pulse Cycle]]
- [[wiki/concepts/project-lineage|Project Lineage]]
