# 21 — Configuration Analysis

**Doc ID:** COSMOS-AUDIT-21 | **Version:** 1.0 | **Generation date:** 2026-08-04
**Cross-references:** [02 Architecture](02_ARCHITECTURE_ANALYSIS.md) · [03 System Spec](03_SYSTEM_ARCHITECTURE_SPECIFICATION.md) · [33 Engineering Spec](33_ENGINEERING_SPECIFICATION.md)

---

## 1. Configuration Architecture (Observed)

`components/rsis3/rsis/config.py`:

- Per-loop dataclasses: `L1Config` (tools per step, step timeout, max_retries),
  `L2Config` (attempts, session timeout, `parallel_candidates`, `parallel_retries`,
  D2 knobs `priority_aging` / `preemption_threshold` / `shared_memory`), `L3Config`
  (plateau), `L4Config` (outcome window), `L5Config` (population size), plus workspace,
  telemetry, tools, evaluator, budget sections. [O]
- Tunable registries (`L1_TUNABLES`, `L6_TUNABLES`, etc.) map `"loop.param"` keys to
  `(min, max, (section, attr), type)` for L4+ meta-parameter tuning. [O]
- `_apply_tuned_state(cfg)` persists tuned values so tuning loops can override defaults
  across sessions. [O]
- Environment overrides use a consistent `RSIS_*` prefix, e.g. `RSIS_L2_PARALLEL`,
  `RSIS_L2_PARALLEL_RETRIES`, `RSIS_L2_PRIORITY_AGING`, `RSIS_L2_PREEMPTION_THRESHOLD`,
  `RSIS_L2_SHARED_MEMORY`, `RSIS_SANDBOX_BACKEND`, `RSIS_SANDBOX_TIMEOUT`,
  `RSIS_HITL_ENABLED`, `RSIS_APPROVAL_MODE`, `RSIS_APPROVAL_THRESHOLD`,
  `RSIS_TOOLS_ENABLED`, `RSIS_COST_LOG`. [O]
- CLI (`main.py`) mirrors the most user-facing knobs (`--parallel`, `--parallel-retries`,
  `--budget-cap`). [O]

## 2. Configuration Coverage Matrix

| Concern | Config surface | Default (observed) |
|---|---|---|
| L2 parallelism | `parallel_candidates` | 0 (sequential) |
| Retry budget | `parallel_retries` / `l1.max_retries` | 0 / 3 |
| D2 priority aging | `priority_aging` | 0.2 |
| D2 preemption margin | `preemption_threshold` | 5.0 |
| Shared memory | `shared_memory` | True (parallel path) |
| Sandbox | `tools.sandbox_backend`, `timeout` | env-driven |
| HITL / approvals | `hitl_enabled`, `approval_mode`, `approval_threshold` | env-driven |
| Budget | `budget_cap_usd` (+ cost ledger) | env/CLI |
| Checkpointing | `checkpoint_before_mutation` | on |

## 3. Findings

| # | Finding | Severity |
|---|---|---|
| C-1 | Configuration is env/CLI only — no file-based config; complex deployments must export many vars | Low |
| C-2 | Tunable registries lack documentation of each parameter's effect on the dashboard | Low |
| C-3 | `RSIS_*` env parsing is duplicated in `main.py` (subset) and `config.py` (full) → drift risk | Med |
| C-4 | No config validation at load (e.g. negative `parallel_candidates` is clamped only at use site) | Low |
| C-5 | MyKB/SPACE have no runtime config surface (static files); only the daemon uses argv | Info |

## 4. Recommendations

1. Add `CONFIG.validate()` at load: ranges per tunable registry, positive budgets, sane
   timeout ordering (step ≤ session).
2. Generate a `config-reference.md` from the dataclasses/tunables (single source of truth).
3. Centralize `RSIS_*` parsing in `config.py` and have `main.py` delegate, removing the
   duplicated subset.
4. Document D2 knobs on the dashboard Configuration/telemetry tab.
