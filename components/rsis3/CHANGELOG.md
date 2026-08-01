
## [0.4.0] — 2026-08-01

### Added
- L8 Meta-Meta loop (`rsis/loop_l8.py`, `python -m rsis metameta`): observes
  L5 generation-fitness history (`.rsis/strategies.json`) and raises
  `l5.mutation_rate` on stagnation / shrinks `l5.population_size` on
  volatility; persisted to `.rsis/metameta_state.json`
- L9 MMM loop (`rsis/loop_l9.py`, `python -m rsis mmm`): observes L6 tuning
  history (`.rsis/identity_state.json`) and widens the
  `l6.shrink_below`/`l6.grow_above` band on oscillation / narrows it on
  stall; persisted to `.rsis/mmm_state.json`
- `L5_TUNABLES` + `L6_TUNABLES` registries; `load_config()` now injects
  L8/L9 state at startup (all nine loops consume tuned params)
- L5 records generation-fitness history for L8
- Dashboard **Loops tab**: `dashboard/loops.json` emitted by
  `gen-static-data.py` (state + telemetry, graceful never-run defaults),
  rendered as a nine-loop stack with targets, tuned params, signals, run
  counts; `--check` validates the snapshot

### Changed
- RSIS_SPEC §1.1/§1.2/§1.4: L8/L9 marked implemented; termination rows and
  arbitration table extended; topology text corrected (L7–L9 are parallel
  observers)
- `rsis` package version bumped to 0.4.0

### Verified
- L8: stagnating L5 fitness → `l5.mutation_rate` 0.2 → 0.25 (raise_mutation);
  oscillating best-fitness → population 8 → 6 (shrink_population)
- L9: alternating L6 shrink/grow → band [0.5, 0.8] → [0.45, 0.85] (widen);
  stalled L6 + low success → [0.55, 0.75] (narrow); gap-collapse no-op
- Fresh-process startup injection of `l5.*`/`l6.*` confirmed
- Dashboard Loops tab renders 10 cards; MyKB/SPACE integration checks pass

## [0.3.0] — 2026-07-31

### Added
- L6 Identity loop (`rsis/loop_l6.py`, `python -m rsis identity`): tunes
  `l3.plateau_timeout_s` from outcome stats + regression trends (shrink on
  regression/low success, grow on stability), evaluator-gated, persisted to
  `.rsis/identity_state.json`
- L7 Meta-Cog loop (`rsis/loop_l7.py`, `python -m rsis metacog`): observes
  L4's tuning history and widens the success deadband on oscillation /
  narrows it on stall, persisted to `.rsis/metacog_state.json`
- Tunable registry now supports float kinds; `L3_TUNABLES` (L6 target) and
  `L4_TUNABLES` (L7 target) added; startup `load_config()` applies L6/L7 state

### Changed
- RSIS_SPEC §1.1/§1.4: L6/L7 marked implemented (L8–L9 hypothetical)

### Verified
- L6: success 0.4 → plateau timeout 86400 → 82800s (shrink), state + startup
  injection confirmed
- L7: oscillating L4 history → deadband [0.5, 0.85] → [0.45, 0.90] (widen),
  state + startup injection confirmed

## [0.2.3] — 2026-07-31

### Changed
- L0 defined as the workspace substrate (not a loop); nothing tunes it — the
  +3 diagonal terminates at L1 (L9 → L6 → L3 → substrate)
- L1/L2 documented as pure consumers of tuned params with no tuning targets;
  intra-cycle retry/refinement is self-adaptation, not cross-loop tuning

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
