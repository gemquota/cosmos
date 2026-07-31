
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
