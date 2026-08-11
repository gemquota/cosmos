---
type: "synthesis"
title: "Dashboard snapshot fallback — never regen from an environment-dependent source"
description: "Root cause of the recurring empty RSIS3 dashboard tabs: gen-static-data.py rebuilt dashboard-data.json only from .rsis/telemetry/*.jsonl, which is untracked and absent in CI/fresh checkouts, so every regen blanked the payload. Durable rule: generated snapshots need a git-tracked source of truth (or fallback) so CI regen can never silently regress the dashboard"
tags: ["synthesis", "dashboard", "rsis3", "snapshots", "regression", "ci", "gen-static-data", "pulses"]
timestamp: "2026-08-11T12:37:08Z"
status: "growing"
---

# Dashboard snapshot fallback — never regen from an environment-dependent source

Root-cause notes from the 2026-08-11 fix for the recurring empty-square RSIS3 tabs:
the dashboard payload kept being blanked by its own snapshot regenerator.

## The regression
- The wrapped RSIS3 tabs rendered as empty squares because
  `rack/pulses/dashboard-data.json` was repeatedly blanked:
  `build_dashboard_payload()` in `gen-static-data.py` derived it only from
  `.rsis/telemetry/*.jsonl` (live loop telemetry). That directory is not
  git-tracked and does not exist on a fresh checkout or in CI.
- Both the nightly snapshot regen and the deploy workflow's self-healing step
  run `gen-static-data.py`; with no telemetry present the payload regenerated as
  `pulses: []`, `goals: []` — a tiny regression payload the dashboard rendered as
  blank tabs. Manual payload fixes were ephemeral: the next regen wiped them.

## Durable rules
- **A generated snapshot's source of truth must exist in every environment that
  regenerates it.** If the live source isn't git-tracked (telemetry, local state,
  secrets), provide a fallback derived from tracked files.
- **Fallback chain**: `build_dashboard_payload()` delegates to
  `_legacy_pulse_payload()` — a mapper over the tracked RRP v2 pipeline files
  `rack/pulses/pulse-*.json` — whenever no telemetry `.jsonl` exists. The legacy
  pulse files carry goals, evaluations, constraints, conversations, and
  `rrp_telemetry_aggregate`, enough to populate the full dashboard schema
  (pulses / goals / score_history / telemetry_aggregates / summary).
- **Invariant**: after any regen, `dashboard-data.json` must be non-empty
  whenever a tracked `pulse-*.json` exists. `gen-static-data.py --check`
  validates files/contracts but not payload depth — always spot-check the
  `pulses` / `goals` counts after a regen, especially in CI-like environments.
- **Deploy is self-healing**: `.github/workflows/deploy.yml` runs
  `build_graph.py` + `gen-static-data.py` + `--check` and commits whatever
  changed, then syncs gh-pages. Environment-dependent generator output therefore
  ships automatically — deterministic, tracked-input-only generation is a
  deploy-safety property, not a nicety.

## Related
- [[wiki/syntheses/cosmos-dashboard-tab-unification-2026-08-11|Cosmos Dashboard Tab Unification — SPACE/MyKB/RSIS3 shell + KG lite mode]]
- [[wiki/syntheses/wiki-stats-hub|Wiki Stats Hub Architecture & Snapshot Hygiene]]
- [[wiki/syntheses/cosmos-dashboard-mykb-integration|Cosmos Dashboard & MyKB Integration Patterns]]
