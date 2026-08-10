---
type: synthesis
title: "RSIS3 Epoch 1 Implementation — Phases 16–50 (Sequels IV–X)"
description: "Durable patterns and rules from implementing the 35-phase epoch-1 program (open autonomy → federated intelligence → governed evolution → intergenerational continuity → collaborative governance → global commons → epoch-scale intelligence): one shared contract-safe telemetry channel, policy/state file separation that keeps live policy untouched by exercises, deterministic divergence resolution, and the cross-roadmap invariant encoded as executable checks"
tags: [synthesis, rsis3, epoch-1, telemetry, governance, federation, attestation, dashboard, roadmap]
timestamp: "2026-08-10T03:00:00Z"
status: stable
source: []
---

# RSIS3 Epoch 1 Implementation — Phases 16–50 (Sequels IV–X)

Epoch 1 is implemented: 35 phases across seven sequels (IV–X) with
module per phase, CLI wiring in `python -m rsis`, a shared telemetry
channel, dashboard surfacing, and 71 new tests (353 total passing).

## Durable rules

- **One telemetry channel per program**: every epoch-1 phase emits
  through `rsis/epoch1.py` → `.rsis/telemetry/epoch1.jsonl`; the
  dashboard Roadmap tab and `gen-static-data.py` read it without
  per-phase pipelines. Event types must be plain snake_case
  (`attestation_appended`, not `attestation.appended`) to satisfy
  `contracts/validate.py` — dotted or hyphenated types fail the contract.
- **Phase exercises stay out of live governance files**: exercising the
  stack against the live workspace must never write `rack/policy.json`,
  `rack/goals_stack.json`, `rack/incidents.jsonl` or budgets; phase
  state lands in new `rack/<phase>/` dirs and `.rsis` ledgers.
- **Portable instances carry state, not keys**: `rsis export` ships
  `.rsis`, `rsis/`, `evaluator/`, `rack/`, `docs/` and wiki syntheses,
  but always excludes `instance.key` (and lock/pid files); the manifest
  embeds users/policy/invariants/seasons so a cold import is
  reproducible without leaking signing material.
- **Deterministic divergence everywhere**: rule conflicts resolve by
  newest fact → local policy wins → more adoptions → sha tie-break
  (popgov, resilience forks, swarm reconcile); failure clustering
  compares root-cause text of the representative incident, never its id.
- **Meta-invariant is executable**: metagov blocks policy deltas that
  lower controls; `metainvariant.check_reachable` model-checks P1–P3
  over bounded policy transitions and attests/publishes the proof to the
  commons (P49) — the machine-checkable form of "autonomy is cumulative
  but never unconditional".

## Patterns worth reusing

- `make_ws` temp-workspace fixture style (`tests/test_epoch1_sequel*.py`)
  keeps 71 phase tests hermetic and fast (<1s).
- Sequencing: verification/attestation substrate (IV) → identity and
  exchange (V) → meta-governance and sustainability (VI) → inheritance
  and missions (VII) → explainability and delegation (VIII) → standards
  and commons (IX) → longitudinal science and epoch capstone (X).

## Status

- Implementation: delivered (phases 16–50 modules, CLI, tests,
  dashboard, telemetry, docs).
- Live validation: pending (exit criteria remain operational runs).
