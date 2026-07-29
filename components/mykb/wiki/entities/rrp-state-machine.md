---
type: "entity"
title: "RRP State Machine"
description: "2,025-line Recursive Refinement Protocol engine with constraint extraction, ambiguity analysis, and session lifecycle"
tags: ["rrp", "state-machine", "protocol", "refinement", "rsis3"]
timestamp: "2026-07-21T10:07:00Z"
---


## Rrp State Machine

# RRP State Machine

**Source:** `rsis3/src/rrp/state_machine.py` (2,025 LOC)

The RRP (Recursive Refinement Protocol) state machine is RSIS3's largest single module. It manages the full lifecycle of a refinement session.

### Public API (85 items)
- **57 externally used** — core session operations
- **20 unused API items** — documented in AUDIT.md
- **9 unused classes** — internal data structures (TypedDicts, dataclasses)

### Wired Functions (from audit resolution)
- `detect_contradictions` + `resolve_contradiction` → ReflectionEngine
- `check_convergence_stall` + `compute_decay_rates` → PulseEngine auto-mode
- `extract_constraints` → PulseEngine auto-mode (phase 3)
- `ambiguity_rating_from_text` → PulseEngine auto-mode (phase 4)

### Key Capabilities
- Constraint extraction with Unicode-aware pattern matching
- Ambiguity vector tracking across 4 dimensions
- Session fork/merge for parallel refinement
- Checkpoint/rollback with state diff
- Validation prompt generation for L2 outputs
- Token budget tracking and consumption limits

**Domain:** Entities

## Related

- [[wiki/entities/identity-snapshot-0001|Identity Snapshot 0001]]
- [[wiki/entities/memory-client|Memory Client]]
- [[wiki/entities/pulse-engine|Pulse Engine]]
- [[wiki/entities/llm-proxy-agent|Llm Proxy Agent]]
- [[wiki/entities/e2e-test-001|E2E Test 001]]
- [[wiki/entities/e2e-entity|E2E Entity]]
