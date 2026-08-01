# RSIS3 — Usage Practices

*Defining* the practices for working with RSIS3 workspaces and loops, and
*enforcing* them with `python -m rsis check-practices` (or
`python3 ops/check_practices.py [WORKSPACE]`). The checker runs against a
workspace and exits non-zero on any violation — run it in CI or after a
loop session.

## 1. Workspace Model

- A **workspace** is a directory with its own `.rsis/` (state, telemetry,
  memory) and its own git history. Run `python -m rsis init` to create one.
- Loop state lives in `.rsis/*_state.json`; telemetry in
  `.rsis/telemetry/*.jsonl`; memory in `.rsis/knowledge_graph.json` +
  `.rsis/vectors/`.
- The repo's dashboard snapshot reads the *committed* `.rsis/` state. After
  a meaningful run, commit the state files and telemetry, then regenerate
  `dashboard/loops.json` with `gen-static-data.py` (repo root).

## 2. Loop Cadence

| Loop | Command | When |
|---|---|---|
| L1 | (internal, `L1ActionLoop`) | every task/tool call |
| L2 | `python -m rsis run --goal "..."` | per session |
| L3 | `python -m rsis evolve` | per consolidation window (hours–days) |
| L4 | `python -m rsis optimize` | after ≥ `l4.min_outcomes` new outcomes |
| L5 | `python -m rsis strategies` | per evolution window (days) |
| L6 | `python -m rsis identity` | when L3 signals appear |
| L7 | `python -m rsis metacog` | when L4 history shows oscillation/stall |
| L8 | `python -m rsis metameta` | when L5 generations stagnate/oscillate |
| L9 | `python -m rsis mmm` | when L6 history shows oscillation/stall |

Rules: never run two cycles of the **same loop** concurrently (state files
are per-loop and unsynchronized); different loops may run in parallel only
because their state files are disjoint (see §4).

## 3. Telemetry Expectations

Every loop writes at least `l{N}_start` and `l{N}_complete`; evaluator-gated
loops also write `l{N}_evaluation` with the decision; failures write
`l{N}_error`. A loop with persisted state but **no** start/complete events is
a violation. `check-practices` reports the per-loop event matrix.

## 4. Ownership & Mutation Hygiene

- Tuning follows the **+3 ownership diagonal**: L4→`l1.*`, L5→`l2.*`,
  L6→`l3.*`, L7→`l4.*`, L8→`l5.*`, L9→`l6.*`. The registry in `config.py`
  is the single source of truth; the checker verifies prefixes, disjoint
  keys, and that the top three loops (L7–L9) are untuned fixed points.
- **Never hand-edit `.rsis/*_state.json` while a loop is running.** Loops
  checkpoint before mutation; manual edits bypass the evaluator and the
  checkpoints.
- The evaluator is immutable — never modify `evaluator/`; the checker does
  not cover this because the digest verification at startup does.

## 5. Checkpoint Hygiene

A workspace with loop state must be a git repo with at least one
`rsis-checkpoint:` commit (the `CheckpointManager` creates these before every
mutation). `check-practices` verifies this so rollback is always possible.

## 6. Dashboard & Snapshot Practice

- After a run: commit `.rsis/` state + telemetry, run
  `gen-static-data.py` (regenerates `dashboard/loops.json` +
  `ecosystem.json`), verify with `gen-static-data.py --check`, and commit
  the snapshots. The Loops tab then reflects real runs, tuned params, and
  last signals.
- `check-practices` marks loops that have never run as WARN (never-run is
  allowed; inconsistent state is not).

## 7. Anti-Patterns

- Running loops in the repo root instead of a dedicated workspace (pollutes
  tracked state with throwaway runs).
- Two same-loop processes at once (state-file race).
- Editing registry bounds to "make a signal fire" — tuning bounds are spec
  (§1.4) and changing them is a spec change.
- Committing telemetry/state without regenerating the dashboard snapshot
  (the Loops tab goes stale).

## 8. Invariants (unconditional)

1. Evaluator is immutable.
2. Checkpoint before every mutation.
3. Loops terminate (bounded budgets).
4. Failures cascade up.
5. Memory is hierarchical (git → KG → vectors).
6. Risk is accepted — no artificial scope limits, only practical resource
   bounds.
