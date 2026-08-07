# SPACE — Pass 009 Roadmap

**Date:** 2026-08-06
**Status:** ✅ Completed

---

## Objectives

1. Map SPACE spec artifacts to candidate L2 goals with traceable references.
2. Wire `--goal from-space` into `run`/`drive`.
3. Make the Guide Direction tab render live loop + memory + spec state.
4. Run the full batch and verify an L2 goal trace references a spec artifact.

## Work Delivered

- `rsis/space_spec.py` — `SpaceSpec` gateway (load export, flatten 67
  artifacts, rank candidate goals, token-overlap search; `RSIS_SPACE_SPEC`
  override + default cosmos export path).
- `rsis/main.py` — `_resolve_goal` handles `from-space`/`from-spec`; help
  text updated on `run` and `drive`.
- `.wiki-daemon/build_stub_audit.py` — `scan_live_state()` merged into
  `scan_guidance()` as the `live` payload (loops, telemetry, spec traces,
  syntheses); regenerated `guidance.json`.
- `components/mykb/index.html` — Direction tab "Live loop & memory state"
  panel (loop stack cells, spec goal traces, recent synthesis links) +
  CSS + render JS.
- `tests/test_space_spec.py` — 4 tests (load/artifacts, goal references,
  search ranking, missing-file fallback). Full suite: 57 passed.
- Batch: 40 executions, +5 per loop, 0 errors; `run` cycle 3 spec-sourced.

## Outcome

`check-practices: all PASS` · `contracts: OK (0 FAIL)` ·
`gen-static-data --check: OK` · wiki link check 5,417 files / 0 unresolved ·
L2 goal trace references `spec artifact abstraction_level`.
