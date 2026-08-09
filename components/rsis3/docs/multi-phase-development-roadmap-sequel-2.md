# Multi-Phase Development Roadmap — Sequel II (Phases 6–10): Horizons

Adopted: 2026-08-09 · Status: active · Mode: llm-driven
Continues: [`multi-phase-development-roadmap.md`](multi-phase-development-roadmap.md) (Phases 1–5 ✅)
Linked goal stack: `rack/goals_stack.json` (goal-stack-001, T0–T3)
Maturity arc: Phases 6–10 — **Governed Intelligence** (remember
collectively → verify → measure economics → govern → predict).

The first roadmap took Cosmos from baseline to a production-grade surface
(T0–T3) and into sustained, self-maintaining operation (Phases 4–5).
Sequel II turns the running system into a *learning organization*: shared
distributed memory, verified outcomes, governed costs, human oversight,
and a system that models its own improvement. Each phase keeps the Output
tier contract — visible artifacts, telemetry, and a measurable exit.

## Phase 6 — Distributed Memory & Multi-Session Coordination

Goal: MyKB stops being a single-workspace store and becomes the shared
nervous system for parallel sessions and agents.

- **Memory API**: `.wiki-daemon` gains `GET /api/search`, `GET /api/notes`,
  `POST /api/notes` (write-only, create-only unless owner session) so any
  component — bridge, daemon, CI, future agents — reads/writes durable
  knowledge over HTTP, not by touching files.
- **Vector index**: TF-IDF search is promoted to a persistent vector index
  (stdlib hashing + cosine over tokens; no new deps) with incremental
  rebuild hooks after each L3 consolidation.
- **Session memory**: every bridge session and daemon run attaches a
  `session_id`; distilled syntheses carry provenance (sessions → sources),
  and `/api/sessions` surfaces cross-session links.
- **Coordination lock**: MyKB note writes move behind an advisory
  lockfile/merge marker so two parallel `launch` sessions consolidating
  simultaneously never clobber each other (extends the daemon lock
  pattern to memory).
- **Exit criterion**: two parallel sessions (daemon + manual bridge chat)
  can both read and write MyKB without conflict; a new session resumes
  with context sourced from the shared index; `check-practices` stays
  green with parallel writes.

## Phase 7 — Verification Mesh

Goal: every applied change ships with verified evidence, not just a gate.

- **Evaluator-as-a-service**: `evaluator/evaluator.py` becomes a callable
  service (`python -m rsis verify-server`) with the same deterministic
  gates (path safety, compile, AST scan, regression) exposed over HTTP;
  the daemon and CI both hit one implementation.
- **Property checks**: candidates may carry optional property tests
  (round-trip, idempotency, invariant) executed in a sandboxed subprocess;
  results become part of the apply record.
- **Regression ledger**: `rack/verification/YYYY-MM-DD.jsonl` records every
  gate run (candidate sha, gates, scores, artifacts) so any applied change
  can be replayed and re-verified.
- **Contract gating**: contracts (`contracts/validate.py`) run as a step of
  the apply pipeline, not only CI; a contract FAIL blocks the commit.
- **Evidence substrate**: the regression ledger accumulates replayable
  records of *why* an autonomous change was allowed (candidate sha, gates,
  scores, artifacts). Phase 7 establishes the verification/evidence
  substrate that Phase 14 later extends into continual invariant
  attestation.
- **Exit criterion**: 100% of applied L2 candidates in a 24h window carry
  a replayable verification record; a deliberate regression injection is
  caught by the mesh before reaching main.

## Phase 8 — Observability & Cost Governance

Goal: the system knows what it did, why, and what it cost — per loop,
per cycle, per dollar.

- **Structured telemetry pipeline**: telemetry gains a retention policy
  (rolling window with compressed archives), per-loop dashboards in the
  unified dashboard (latency, success, no-op rates), and anomaly markers
  emitted as events the live feed already renders.
- **Cost budgets**: `.rsis/costs.jsonl` rolls into a budget ledger with
  per-loop and per-day allocations; crossing a budget emits
  `cost.budget_hit` and fail-closes LLM enrichment for that loop until
  reviewed.
- **Cost surface**: `/api/cosmos` cost block grows to per-loop breakdown
  and 7-day trend; dashboard shows budget remaining, not just spend.
- **Anomaly policy**: `python -m rsis anomalies` scans the telemetry
  window for regressions (success-rate drop, duration spikes, missing
  telemetry) and files backlog items — the convergence monitor's sibling.
- **Exit criterion**: a 24h run with an injected per-loop budget breach
  stops the offending loop's LLM spend automatically and surfaces a
  dashboard card + backlog note; every loop has a retention-bounded,
  queryable history.

## Phase 9 — Human-in-the-Loop Governance

Goal: the system's autonomy is bounded by policy, auditable, and
reversible. The human is one enforcement mechanism within the policy
architecture — internally this is *policy-controlled autonomy*, with
approval gates as one of several policy instruments.

- **Policy file**: `rack/policy.json` (env-templated) declares what the
  system may do autonomously — allowed loop families, apply rules, budget
  ceilings, approval-required triggers (e.g., candidate touching
  `rack/bridge/server.mjs`, config, or wiki structure).
- **Approval gates**: candidates hitting a policy gate are staged
  (`rack/approvals/`) with a rendered diff; `python -m rsis approve
  <id> [--reject]` completes or discards them; CI treats staged-but-
  unapproved as not-applied.
- **Audit trail replay**: every applied change logs actor, policy
  decision, verification record, and the pre-apply state file digest;
  `python -m rsis audit --since` replays the trail.
- **Rollback**: state files and applied candidates keep the previous
  digest; `python -m rsis rollback <candidate-id>` restores the prior
  versions within the workspace and files a MyKB incident note.
- **Exit criterion**: a policy-gated candidate is rejected by the gate,
  approved manually, applied, then rolled back — all leaving audit
  records; an unauthorized direct write to a gated path is detected on
  the next cycle.

## Phase 10 — Self-Modeling & Prediction

Goal: the system predicts its own next state and schedules work by
forecast, not habit.

- **Cycle forecaster**: `python -m rsis forecast` fits a lightweight model
  over strategies/telemetry history (plateau detection feeds it) and
  predicts next-cycle best fitness, success rate, and cost with a
  tolerance band.
- **Predictive scheduling**: the daemon consumes forecasts —
  `RSIS_CYCLE_INTERVAL_S` becomes adaptive (faster during improvement
  phase, slower at plateau) while staying within policy bounds.
- **Retune timing**: convergence + forecast jointly decide *when* to
  auto-retune (Phase 5 ledger stays the bound), so retunes land on
  predicted inflections instead of fixed intervals.
- **Self-model registry**: forecasts and their hits/misses are stored
  (`rack/forecasts/`) and summarized in the nightly note, making the
  model itself a monitored subsystem.
- **Calibration & uncertainty**: forecast quality is tracked as
  first-class metrics — accuracy, calibration (confidence vs. realized hit
  rate), uncertainty width, systematic bias, and degradation over time —
  not just raw coverage.
- **Exit criterion**: over 7 days, the forecaster's best-fitness band
  covers ≥80% of realized values; cadence adapts on an injected
  improvement event; forecast quality — coverage, calibration, bias,
  degradation — appears in every nightly summary.

## Sequencing notes (Sequel II)

- Phases are cumulative and intentionally ordered: memory (6) and
  verification (7) are prerequisites for governed autonomy (9); cost
  governance (8) must precede forecasting (10) because forecasts need
  cost history.
- Phase 6 reuses the Phase 4/5 lockfile and Phase 3 session patterns —
  do not build new coordination primitives before mining those.
- Every phase ends with a MyKB synthesis + snapshot regeneration per the
  standing L3 memory-consolidation practice.

## Status

| Phase | Area | Status |
|-------|------|--------|
| Phase 6 — Distributed memory & multi-session coordination | memory | ⏳ queued |
| Phase 7 — Verification mesh | verification | ⏳ queued |
| Phase 8 — Observability & cost governance | ops | ⏳ queued |
| Phase 9 — Human-in-the-loop governance | governance | ⏳ queued |
| Phase 10 — Self-modeling & prediction | autonomy | ⏳ queued |
