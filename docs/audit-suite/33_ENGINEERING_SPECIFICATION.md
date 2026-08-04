# 33 — Engineering Specification

**Doc ID:** COSMOS-AUDIT-33 | **Version:** 1.0 | **Generation date:** 2026-08-04
**Cross-references:** [02 Architecture](02_ARCHITECTURE_ANALYSIS.md) · [03 System Spec](03_SYSTEM_ARCHITECTURE_SPECIFICATION.md) · [35 Appendices](35_APPENDICES.md)

---

## 1. Purpose

Defines the normative engineering rules for COSMOS: the boundaries, invariants, and
standards every change must respect. Derived from observed code plus `AGENTS.md`.

## 2. Architecture Invariants

1. **One memory** — MyKB is the sole persistent knowledge store; no other wiki/memory layer
   may be added.
2. **One dashboard** — the unified dashboard (`components/rsis3/dashboard/index.html`) is the
   only standalone dashboard; repo-root `index.html` redirects to it.
3. **One telemetry** — workspace telemetry flows through `TelemetryCollector` (+ the D2
   `EventBus`); no parallel metric stores.
4. **RSIS3-centric** — RSIS3 is the core; MyKB (memory) and SPACE (ideation) serve it.
5. **Selective AO ports** — AO integration is a port (config-gated, sync-first, defaults
   preserve prior behavior), never a component merge.

## 3. Module Contracts

| Module | Responsibility | Consumers |
|---|---|---|
| `rsis/config.py` | typed config + tunables + env overrides | all loops/CLI |
| `rsis/error_classifier.py` | retry taxonomy | pipeline, priority pool, L1 |
| `rsis/pipeline.py` / `priority_pool.py` | DAG + priority execution | L2 |
| `rsis/event_bus.py` | pub/sub telemetry backbone | pools, dashboard bridge |
| `rsis/shared_memory.py` | race-safe working memory | L2 parallel candidates |
| `rsis/checkpoint.py` / `recovery.py` | mutation safety + triple recovery | L1/L2 |
| `rsis/telemetry.py` | event + cost collection | everything |
| MyKB `build_*.py` | snapshot generation | browser + dashboard |
| `gen-static-data.py` | ecosystem/loops snapshots | dashboard |

## 4. Coding Standards (Normative)

- Python: modern annotations, dataclasses for state, `logging.getLogger(__name__)`.
- Ports: sync-first; new behavior off by default unless it replaces a defect; tests required.
- State files: must be written atomically (temp + `os.replace` + `fsync`) — pending TD-3.
- Frontmatter: single canonical writer with consistent quoting (pending TD-7).
- Commits: checkpoint-before-mutation for destructive ops; L3 consolidation into MyKB for
  significant sessions (AGENTS.md standing practice).
- Deploy: tree sync to `gh-pages` with `Deploy: … (main <sha>)` (pending automation, DP-1).

## 5. Quality Gates (Required Baseline)

1. `pytest components/rsis3` (49 cases) green.
2. `gen-static-data.py --check` green when snapshots change.
3. `python -m rsis check-practices` green.
4. New modules land with tests; loops L3–L9 get smoke coverage incrementally (TD-1/T-1).
