# SPACE — RSI Pass 009 Audit Report

**Project:** Superb Prompt Automatic Creation Engine (SPACE) · COSMOS integration arc
**Date:** 2026-08-06
**Pass:** RSI Pass 009 — Spec link (SPACE spec data → L2 ideation, live Guide)
**Scope:** SPACE spec → L2 goal mapping + live Guide Direction state + full L1–L9 batch

---

## Executive Summary

Pass 009 wired the SPACE specification into the loop pipeline and the Guide.
A new `SpaceSpec` gateway maps the exported 326-probe spec artifacts (67
artifacts in `recursive-self-improvement-specification.json`) to candidate
L2 goals — `python -m rsis run --goal from-space` now sources the goal from
a spec artifact, so telemetry traces reference it. The Guide Direction tab
gained a **live loop & memory state** panel: the RSIS3 loop stack, SPACE
spec goal traces, and recent MyKB syntheses now ride on the same guidance
payload (daemon `scan_guidance()` + static `guidance.json`). The standing
batch ran **+5 net starts per loop, 0 errors**, and one L2 run's goal trace
references a SPACE spec artifact — the pass verification criterion.

## Spec Link Delivered

| Piece | Mechanism | Where |
|-------|-----------|-------|
| Spec → goals | `SpaceSpec.artifacts()` flattens exported artifacts (id, value, source series/question, confidence); `candidate_goals()` ranks them into goal strings embedding `spec artifact <id>` | `components/rsis3/rsis/space_spec.py` |
| Goal sourcing | `run`/`drive --goal from-space` (alias `from-spec`) resolves via `_resolve_goal`; spec path from `RSIS_SPACE_SPEC` else `<cosmos>/components/space/exports/recursive-self-improvement-specification.json` | `components/rsis3/rsis/main.py` |
| Guide live state | `scan_guidance()` gained a `live` section: loop stack (`loops.json`), per-loop telemetry starts, spec-backed L2 goal traces, recent syntheses; served by `/api/v2/guidance` and the static `guidance.json` | `components/mykb/.wiki-daemon/build_stub_audit.py` |
| Guide panel | Direction tab renders "Live loop & memory state" (loop cells, spec traces, synthesis links) | `components/mykb/index.html` |

## Loop Batch

- 5 cycles × L1–L9 = 40 executions, **+5 net starts per loop, 0 errors**.
- `run` cycle 3 used `--goal from-space` → L2 goal trace:
  `Implement the abstraction_level spec artifact: … (SPACE spec artifact
  abstraction_level, series 1, question 1.1.1)`.
- Telemetry after pass: L1=26, L2=26, L3=24, L4=24, L5=28, L6=25, L7=23,
  L8=23, L9=22 (180 files / 602 events / 0 malformed).
- L3 self-wrote cycles 6–10 (`rsis3-l3-cycle-6..10-…md`) + 5 `log.md`
  entries — the pass-8 durable-ordinal fix produced clean distinct titles.

## Durable Rules

- SPACE spec exports are a first-class ideation source: artifacts map to
  L2 goals with traceable `spec artifact <id>` references.
- Guide surfaces should prefer one shared payload (scan_guidance + live
  section) over parallel ad-hoc lists, so daemon and static pages agree.
- Cross-component reads (mykb reading rsis3 loops.json/telemetry) stay
  optional and degrade to empty state when files are absent.
