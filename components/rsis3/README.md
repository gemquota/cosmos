# RSIS — Recursive Self-Improvement System

A three-loop recursive self-improvement system implementing the architecture
defined by an RRP session (11 locked decisions, 0 contradictions).

## Architecture

```
L5 ─ Strategy Evolution (days)
  ├─ Population-based evolution of L2 improvement params + focus
  └─ Seeded from L3 KG strategies, evaluator-gated

L4 ─ Meta-Parameter Optimizer (hours)
  ├─ Fast-feedback tuning of L1 execution params (retries, tool calls)
  └─ Evaluator-gated, checkpointed, persisted state

L3 ─ Cross-Session Evolution (hours/days)
  ├─ Memory consolidation (git → KG → vectors)
  ├─ Strategy & meta-parameter evolution
  └─ Redundancy refinement pruning

L2 ─ Per-Session Improvement (minutes)
  ├─ Code generation & architecture modification
  ├─ Prompt/tool tuning
  └─ Validated by IMMUTABLE AI evaluator

L1 ─ Per-Task Action Loop (seconds)
  ├─ Tool calls, observations, retries
  ├─ Workspace telemetry collection
  └─ Checkpoint rollback on failure
```

## Loop Status

The engine was conceived as **nine nested loops** (L1–L9), all of which are
now implemented as bounded, evaluator-gated cycles: L1–L3 are the original
three-loop stack (`loop_l1.py` … `loop_l3.py`); L4 (`loop_l4.py`, Optimizer),
L5 (`loop_l5.py`, Evolution), L6 (`loop_l6.py`, Identity), L7 (`loop_l7.py`,
Meta-Cog), L8 (`loop_l8.py`, Meta-Meta) and L9 (`loop_l9.py`, MMM). See
`RSIS_SPEC.md` §1.1 for the full hierarchy.

Run them with `python -m rsis optimize` (L4), `python -m rsis strategies` (L5),
`python -m rsis identity` (L6), `python -m rsis metacog` (L7),
`python -m rsis metameta` (L8) and `python -m rsis mmm` (L9).
Persisted tuning is applied at startup by `load_config()`, so L1/L2 consume it
automatically. Topology (nested / parallel / overlapping) and the ownership
partition are specified in `RSIS_SPEC.md` §1.4.

## Key Invariants

- **Evaluator is immutable** — never in-scope for self-improvement
- **Checkpoint before every mutation** — rollback is always possible
- **Loops terminate** — no unbounded recursion within a level
- **Failure cascades up** — L1→L2→L3 for adaptive retry
- **Memory is hierarchical** — git (truth) → KG (insight) → vectors (retrieval)
- **Risk is accepted** — no artificial scope limits, only practical resource bounds

## Quick Start

```bash
# Install
pip install -r requirements.txt

# Initialise a workspace
python -m rsis init

# Run a self-improvement session
python -m rsis run --goal "add error handling to utils.py"

# Fan out N parallel L2 candidates (DAG multi-agent)
python -m rsis run --goal "add error handling to utils.py" --parallel 3
# ...with a per-candidate retry budget (transient failures back off & retry)
python -m rsis run --goal "add error handling to utils.py" --parallel 3 --parallel-retries 2

# Run an L3 evolution cycle
python -m rsis evolve

# Scheduler / DAG demos
python -m rsis scheduler
python -m rsis pipeline

# Check system status
python -m rsis status
```

## Drive Loops Until Satisfied

The one-shot commands above run a single cycle. To keep a loop running
automatically until its completion requirement is met (or until a safety
budget runs out), use `drive`:

```bash
# Keep running L2 improvement sessions until one applies a change
python -m rsis drive --loop l2 --goal "add error handling to utils.py"

# Tune L4 until the observed success rate lands inside its target band
python -m rsis drive --loop l4 --max-cycles 12

# Evolve L3 until consolidation plateaus (no new insights/focus strategies)
python -m rsis drive --loop l3 --timeout 86400 --sleep 60
```

Per-loop completion requirements (all configurable via `rsis/config.py` or
the tunable state files in `.rsis/`):

| Loop | Completion requirement | Relevant config |
|---|---|---|
| L2 | an improvement candidate passes the evaluator and is applied | `l2.max_improvement_attempts`, `l2.session_timeout_s` |
| L3 | consolidation plateau — no new insights, focus strategies, or pruned redundancies | `l3.plateau_sessions`, `l3.plateau_timeout_s` |
| L4 | success rate inside `[target_success_low, target_success_high]` (no deltas proposed) | `l4.min_outcomes`, `l4.outcome_window`, `l4.target_success_*` |
| L5 | best strategy fitness plateaus (no improvement over the previous generation) | `l5.population_size`, `l5.mutation_rate` |
| L6–L9 | no tuning signal — the target band is stable | `l6..l9` `cycle_timeout_s`, band config |

`drive` exit codes: `0` requirement satisfied · `1` error · `2` time budget
exhausted · `3` max cycles reached · `4` terminally stuck (e.g. L4 needs
more outcomes, L2 exhausted its attempts) — so it composes cleanly with
cron/systemd/shell scripts.

To run unattended until done:

```bash
# Shell: keep retrying until satisfied (exit 0), cap wall time
timeout 6h python -m rsis drive --loop l4 --sleep 60   || [ $? -eq 4 ] && echo "stuck — inspect .rsis/optimizer_state.json"

# cron: every 30 min, stop as soon as the requirement is met
*/30 * * * * cd /path/to/components/rsis3 && \
  python -m rsis drive --loop l4 --max-cycles 1 --timeout 1200
```

Every cycle writes `l{N}_start`/`l{N}_complete` telemetry, so the dashboard's
Loops tab flips from IDLE to RECENT after a drive finishes.

## Tool Layer (L1 sandbox + approvals)

L1 executes tools through a sandboxed layer (`rsis/tools/`, ported from the
Agent OS project — see `docs/ao-assessment.md`):

- **Sandbox** — `run_code` evaluates untrusted Python via RestrictedPython
  (subprocess or Docker backends available via `sandbox_backend`); all child
  processes get resource limits, a minimal env, and a hard timeout.
- **Allowlists** — every tool declares `agent_allowlist`; calls outside it are
  denied. `write_file` is restricted to implementing agents (`l1`, `coder`),
  `reviewer` is read-only.
- **Path containment** — file tools resolve paths inside the workspace and
  deny traversal.
- **HITL approvals** — a 5-level risk classifier (SAFE→CRITICAL) gates calls
  at/above the configured threshold. Modes: `auto`, `interactive` (console
  y/N), `api` (operator resolution, fail-closed timeout), `deny`.
- **Audit** — every call is logged redacted to `.rsis/audit.jsonl` (HITL
  decisions to `.rsis/hitl.jsonl`); secrets are masked in outputs.

Config (env-overridable, `rsis/config.py` → `ToolConfig`):

| Env var | Default | Meaning |
|---|---|---|
| `RSIS_TOOLS_ENABLED` | `1` | master switch (0 = pre-port behaviour) |
| `RSIS_SANDBOX_BACKEND` | `auto` | `auto`/`restricted`/`subprocess`/`docker` |
| `RSIS_SANDBOX_TIMEOUT` | `30` | seconds per tool call |
| `RSIS_HITL_ENABLED` | `0` | enable operator approval for risky tools |
| `RSIS_APPROVAL_MODE` | `interactive` | `auto`/`interactive`/`api`/`deny` |
| `RSIS_APPROVAL_THRESHOLD` | `high` | risk level requiring approval |

## LLM Cost Ledger & Budget Cap

Every evaluator LLM call is accounted in a persistent ledger
(`.rsis/costs.jsonl`) with a local price table ($/1M tokens) — no provider
billing API needed. The ledger replays on startup so budget caps hold across
separate loop processes (`run`, `evolve`, `optimize`, ...).

- `python -m rsis status` prints current spend / budget state.
- `python -m rsis run --goal X --budget-cap 0.50` caps a session in USD.
- `RSIS_BUDGET_CAP_USD` env var sets the global cap; `RSIS_COST_LOG` relocates
  the ledger.

Enforcement is two-stage: a pre-flight `guard_budget` refuses an evaluator
call when the estimate would cross the cap, and a persistent
`budget_exceeded` latch stops new sessions once spend reaches the cap
(fail-closed).

## Agent Scheduler & DAG Pipeline (multi-agent L2)

Two execution primitives ported from the Agent OS kernel
(`kernel/scheduler.py`, `kernel/parallel_pipeline.py`) power optional
multi-agent L2 runs:

- **`rsis/scheduler.py` — AgentScheduler.** Priority-queue scheduling
  (CRITICAL preempts background work; equal priorities stay strictly FIFO via
  a monotonic sequence tie-breaker) with recursion guards: a hard depth cap
  and directed-edge cycle detection (same role/description hand-off repeated
  more than `cycle_limit` times aborts the branch). One failing agent never
  kills the loop — FAILED results are recorded and the queue drains.
- **`rsis/pipeline.py` — DAGWorkerPool.** Fan-out/fan-in over N worker
  threads: a task dispatches only when every `depends_on` task is COMPLETED,
  a concurrency cap bounds in-flight LLM calls, circular/missing dependencies
  raise instead of hanging, and a failed task marks its dependents FAILED.
  Per-task status/latency can be emitted to telemetry via an `on_event` hook.

**Parallel L2 sessions:** `python -m rsis run --parallel N` (or
`RSIS_L2_PARALLEL=N`) runs the L2 loop as a DAG — planner → N parallel
coders → fan-in reviewer. Every candidate still passes through the immutable
evaluator gate (only a PASS candidate is applied), the review wave runs
through the AgentScheduler with depth/cycle guards, and the cost ledger +
budget caps apply per call exactly as in sequential mode. Telemetry records
`l2_parallel_start`, `dag_task`/`dag_complete`, and `l2_complete` events.
The default (`parallel_candidates=0`) remains the sequential L2 loop.

## Project Structure

```
rsis/
├── rsis/                  # Core Python package
│   ├── __init__.py        # Package metadata
│   ├── config.py          # Configuration & resource limits
│   ├── checkpoint.py      # Git-based checkpoint/rollback
│   ├── scheduler.py       # Priority queue + recursion guards (AO port)
│   ├── pipeline.py        # DAG fan-out/fan-in worker pool (AO port)
│   ├── telemetry.py       # Workspace telemetry collection
│   ├── evaluator.py       # Evaluator subprocess client
│   ├── loop_l1.py         # L1 Action Loop
│   ├── loop_l2.py         # L2 Improvement Loop
│   ├── loop_l3.py         # L3 Evolution Loop
│   ├── memory.py          # Three-tier memory hierarchy
│   ├── tools/             # Sandboxed tool layer (L1)
│   │   ├── base.py        # Tool protocol + results
│   │   ├── sandbox.py     # subprocess / RestrictedPython / Docker
│   │   ├── hitl.py        # risk classifier + approval gate
│   │   ├── manager.py     # registry, allowlists, vault, audit
│   │   └── workspace_tools.py
│   └── main.py            # CLI entry point
├── evaluator/             # Immutable evaluator (separate process)
│   ├── evaluator.py       # Evaluator binary
│   └── prompt.txt         # Immutable evaluator system prompt
├── tests/                 # Test suite
├── requirements.txt
└── README.md
```

## Implementation Phases

| Phase | Status | Description |
|-------|--------|-------------|
| 1     | ✅     | Core Loop Engine — L1, L2, immutable evaluator, checkpoints, telemetry |
| 2     | ⏳     | Memory & Persistence — KG, vector store, L3 evolution |
| 3     | 📅     | Autonomy & Refinement — redundancy pruning, extrapolation, dashboard |
| 4     | 📅     | Production Hardening — resource limits, recovery testing, security |

## Spec

The full implementation specification is at `RSIS_SPEC.md`.
