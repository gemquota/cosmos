
## [0.4.4] — 2026-08-07

### Added
- Self-assessment routine: `python -m rsis self-assess` — deterministic
  KB health scan (links, orphans, stubs, content depth with weighted
  score), gap analysis against recent syntheses (backlog items filed
  create-only in `wiki/backlog/`), trend detection from telemetry + git,
  and per-run `wiki/assessments/` + `wiki/reflections/` OKF notes
- Optional fail-closed LLM enrichment (`RSIS_EVALUATOR_API_KEY`) that can
  only add narrative, never alter deterministic findings
- `SelfAssessConfig` (window, artifact dirs, daemon timeout); `sa_start` /
  `sa_complete` / `sa_error` telemetry; `infra/loops/run-batch.sh` runs
  the routine after each scheduled batch

### Verified
- `tests/test_self_assess.py` — 39 cases; full rsis3 suite passes
- `gen-static-data.py --check` OK after first real run

## [0.4.3] — 2026-08-07

### Added
- Deterministic evaluator gate (`evaluator/evaluator.py`): the immutable
  evaluator now validates candidates instead of always passing — target-path
  safety (relative workspace paths only; no absolute / `..` / Windows
  forms), compile check, AST safety scan (dynamic execution, shell=True,
  destructive process/filesystem calls, out-of-workspace writes),
  regression scan (removed definitions fail closed), and
  style/efficiency heuristics
- Config/data candidate support: JSON payloads (e.g. L8/L9 tuning deltas)
  skip the Python gates and are validated for shape and destructive shell
  strings, so meta-tuning loops keep passing without code checks
- Diff-fragment tolerance: unified-diff added lines are dedent-recompiled
  and AST-scanned, so partial in-block diffs pass compile without skipping
  the safety scan
- Optional fail-closed LLM refinement: with `RSIS_EVALUATOR_API_KEY` or
  `OPENAI_API_KEY` set, the LLM can only downgrade a PASS or refine scores
  — a deterministic hard FAIL is final and its scores cannot be inflated
- `tests/test_evaluator_gate.py` — 45 cases: PASS/FAIL paths, path safety,
  diff parsing, data candidates, fail-closed LLM merge, `--verify` digest

### Verified
- rsis3 suite: 120 passed (45 new); evaluator byte-compiles
- Evaluator smoke via stdin: clean module PASS, `os.system("rm -rf /")`
  FAIL, syntax error FAIL, JSON delta PASS, unsafe diff fragment FAIL
- `check-practices` all PASS; `gen-static-data.py --check` OK

## [0.4.2] — 2026-08-04

### Added
- Phase D1 (Agent OS wave 2): `rsis/error_classifier.py` — transient /
  rate-limit / fatal classification (`classify_error`, `classify_error_text`,
  `is_retryable`), ported from AO and stdlib-only
- `DAGWorkerPool` retry support (`rsis/pipeline.py`): per-task retry budget
  (`max_retries`, default 0 = fail fast), exponential backoff with full
  jitter (base/max delay caps), retryable-vs-fatal gating via the error
  classifier, `dag_task_retrying` traceability events, retry-aware deadlock
  guard, and retry counts in `dag_complete`
- L1 retry policy: `l1.max_retries` is now enforced — consecutive retry
  beats stop at the budget, and non-retryable (fatal) tool failures fail
  fast instead of spinning retry beats
- Parallel L2: `l2.parallel_retries` config (env `RSIS_L2_PARALLEL_RETRIES`,
  CLI `--parallel-retries`) feeds the DAG pool's per-candidate retry budget

### Verified
- `python -m rsis pipeline` demo now asserts retry recovery (transient
  failure recovers after budgeted retries) and fatal fail-fast
- All changed modules byte-compile; error classifier semantics match the AO
  reference (`kernel/error_classifier.py`)

## [0.4.1] — 2026-08-01

### Added
- Usage-practice enforcement: `rsis/practices.py` with 17 checks (the +3
  ownership diagonal L4→`l1.*` … L9→`l6.*`, disjoint registry keys, top-3
  loops untuned, disjoint state files, telemetry start+complete coverage,
  `rsis-checkpoint:` git hygiene), exposed as `python -m rsis check-practices`
  and `ops/check_practices.py [WORKSPACE]`; exits non-zero on any FAIL
- `docs/usage-practices.md`: workspace model, loop cadence (incl. L8/L9
  commands), telemetry expectations, ownership/mutation hygiene, checkpoint
  practice, dashboard snapshot practice, anti-patterns, and the six
  invariants the checker verifies

### Changed
- `rsis` package version bumped to 0.4.1
- AGENTS.md now points to the usage-practices doc + checker

### Verified
- Full-loop workspace (`.rsirrp/work/full-loop`): 17/17 checks PASS —
  registry ownership prefixes, 12 unique keys, 6 disjoint state files,
  26 `rsis-checkpoint` commits, and per-loop telemetry (L1–L3 1/1,
  L4 2/2, L5 6/6, L6 3/3, L7–L9 1/1, zero errors)

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
