
## [0.2.2] — 2026-07-31

### Changed
- Tuning ownership generalized to the **+3 diagonal**: loop k+3 tunes loop k
  (L4→L1, L5→L2, L6→L3, L7→L4, L8→L5, L9→L6). L6–L9 roles redefined from
  vague meta-labels to concrete tuner slots in RSIS_SPEC §1.1/§1.4
- Top three loops (L7–L9) are untuned fixed points — bounded modification
  depth of 3, matching the SPACE recursive-depth analysis

### Unchanged
- L4/L5 implementations still own l1.* / l2.max_attempts respectively

## [0.2.1] — 2026-07-31

### Added
- Loop topology spec (RSIS_SPEC §1.4): nested (L1–L3 stack), parallel (L4/L5,
  disjoint state), overlapping (shared reads + config writes) with an
  ownership partition and concurrency guardrail
- `load_config()` now applies persisted L4/L5 state at startup — L1/L2 consume
  tuned params without extra plumbing

### Changed
- L4/L5 ownership partition: L4 tunes only `l1.*` (retries, tool calls); L5
  tunes only `l2.max_attempts` + focus. No shared write keys (resolves the
  L4↔L5 overlap on `l2.max_attempts`)

### Verified
- Smoke: L4 tunes L1 params only; L5 seeds population with L2 params; fresh
  process picks up both from persisted state

## [0.2.0] — 2026-07-31

### Added
- L4 Optimizer loop (`rsis/loop_l4.py`, `python -m rsis optimize`): fast-feedback
  meta-parameter tuning from outcome telemetry, evaluator-gated, checkpointed,
  persisted to `.rsis/optimizer_state.json`
- L5 Strategy Evolution loop (`rsis/loop_l5.py`, `python -m rsis strategies`):
  population-based strategy evolution (elitism + mutation/recombination),
  seeded from L3 KG strategies, persisted to `.rsis/strategies.json`
- Nine-loop hierarchy documented in `RSIS_SPEC.md` §1.1 (L1–L5 implemented,
  L6–L9 hypothetical)

### Changed
- `MemoryManager.save()` now persists KG + vectors; improvements and L3
  consolidation survive across processes
- CLI: `optimize` and `strategies` subcommands

### Verified
- L4 tunes params when success rate is low (smoke: 2/5 applied → +1 on
  retries/tool-calls/attempts); L5 evolves generations with stable population

## [0.0.10] — 2026-07-11

### Added
- Self-contained telemetry-dashboard/ with server.py and frontend/ SPA
- Deprecation notices for old scattered dashboard copies
- Fixed missing pf() function that prevented tab rendering

### Changed
- Consolidated all dashboard files into telemetry-dashboard/ as canonical location

### Verified
- Server starts and serves frontend at http://localhost:8080
- All API endpoints functional
