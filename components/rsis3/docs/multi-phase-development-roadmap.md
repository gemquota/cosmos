# Multi-Phase Development Roadmap — Cosmos Bridge & LLM-Driven Cycles

Adopted: 2026-08-08 · Status: active · Mode: llm-driven
Linked goal stack: `rack/goals_stack.json` (goal-stack-001, T0–T3)

This roadmap sequences the work needed to take the Cosmos software from its
current bridge-and-chat baseline to a production-grade surface. Each phase
names the tier(s) it completes, concrete deliverables, and an exit criterion
so progress is measurable per the Output tier (T0: no silent phases).

## Cross-roadmap invariant

> **Autonomy is cumulative but never unconditional.** Every expansion of
> capability must inherit the memory, verification, cost, policy,
> provenance and observability controls established by preceding phases.

That is what the sequencing already does: Phase 5 autonomy requires
Phase 4 telemetry; Phase 10 prediction requires Phases 6–8 memory,
verification and cost history; Phase 13 federation requires Phase 6
provenance and Phase 9 trust/policy; Phase 15 long-horizon autonomy
requires Phases 8–10 and 14. A phase may build on prior controls; none
may silently relax them.

## Baseline (delivered 2026-08-08)

- **T0 Output** — `rack/goals_stack.json` active; every cycle commits ≥1
  artifact and leaves telemetry.
- **T1 Communicate** — dashboard Active Drives strip reads the goal stack;
  each session shares status, drives, and plans; durable notes land in MyKB
  syntheses.
- **T2 Wrappers (first pass)** — `rack/bridge/envelope.mjs` implements
  `cosmos-envelope/1` (header + text + compact ctx + artifact refs);
  `/api/cosmos` serves refs to state files and syntheses; `/api/chat`
  inlines text artifacts and passes images as Gemini `inline_data`;
  traversal is blocked at the root boundary.
- **T3 Bridge (first pass)** — `rack/bridge/server.mjs` (stdlib-only Gemini
  proxy, offline fallback) + `dashboard/bridge.html` chat UI + Bridge tab in
  the unified dashboard. Server-side API key only.
- **Ops (seed)** — cadence target 1 cycle / 3 min (≈20 cycles/hour);
  snapshots are now fetched dynamically from live `.rsis/` state instead of
  regenerated static files; a parallel session runs `launch --cycles 1` on
  its own commit cadence.

## Phase 1 — Live State Streaming (completes T1)

Goal: the dashboard stops polling files and starts *showing the system think*.

- **SSE event feed**: `rack/bridge/server.mjs` gains `GET /api/events`
  (Server-Sent Events). RSIS loop hooks publish `cycle.started`,
  `loop.finished`, `l3.consolidated`, `kg.updated`, `strategy.evolved`,
  `goal.updated` events; dashboard Bridge tab subscribes and renders a live
  activity timeline.
- **Pulse telemetry push**: pulses written by loops are mirrored to the feed
  so `pulses/latest.json` is a snapshot, not the source of truth.
- **Per-cycle summary cards**: one card per completed cycle (rc, L3 #, KG
  nodes/edges, fitness, duration) rendered in the Bridge tab and archived to
  `rack/bridge/cycles/YYYY-MM-DD.jsonl`.
- **Exit criterion**: a 3-minute cadence run shows ≥5 live cards with no
  manual refresh; telemetry deltas are visible within 2s of a loop write.

## Phase 2 — Envelope Hardening (completes T2)

Goal: dense, typed, multimodal, bounded, and safe messaging.

- **Typed artifacts**: text artifacts stay previews, but JSON/YAML/TOML
  artifacts are parsed structurally and passed as machine-readable blocks
  (with schema key counts), not raw strings.
- **Multimodal expansion**: audio artifacts (transcribe via provider where
  available or mark `unsupported`), PDF text extraction, video frame
  rejection with a clear status; keep `inline_data` images at ≤4 MB.
- **Envelope versioning**: keep `spec: cosmos-envelope/1` and add a
  `CHANGELOG` section in `envelope.mjs`; version bumps must be additive
  (new fields optional) until spec v2.
- **Limits & security**:
  - Per-type byte caps (text 8 KB preview, image 4 MB, total 6 MB) enforced
    server-side, not just in the UI.
  - Per-token rate limit on `/api/chat` (e.g. 20 req/min) with a retry-after
    header; simple in-memory bucket, no new deps.
  - `GEMINI_API_KEY` required for LLM mode; bridge endpoints refuse
    non-localhost origins unless `RSIS_BRIDGE_ALLOW_ORIGIN` is set.
  - Replace the root-prefix traversal guard with an explicit allowlist file
    `rack/bridge/allowlist.json` (still defaulting to root+mykb containment).
- **Streaming replies**: `/api/chat` streams Gemini tokens via SSE/NDJSON so
  the first token appears <1s; fallback reply unchanged.
- **Exit criterion**: a test matrix in `components/rsis3/tests/` covers
  traversal, oversized artifacts, rate limit, missing file, and text+image
  round-trip — all green via `python3 -m unittest` or the existing test
  runner.

## Phase 3 — Product Surface (completes T3)

Goal: the bridge is a real web product, not a localhost demo.

- **Conversation persistence**: exchanges append to
  `rack/bridge/sessions/<session-id>.jsonl` (envelope-shaped); reload
  restores history; a `/api/sessions` endpoint lists/resumes them.
- **Chat memory loop**: distilled conversations become MyKB input — bridge
  writes a `syntheses/`-style note when a session reaches N exchanges,
  feeding the T1 communication tier durably.
- **Native embed**: extract the chat surface from `bridge.html` into a
  shared `bridge.js` module so the unified dashboard embeds it without an
  iframe; keep the standalone page for direct access.
- **Auth & hosting**: optional token auth (`RSIS_BRIDGE_TOKEN`) for
  non-localhost deployments; document the existing `vercel-deploy/`
  template as the static front-end home with the bridge as a hosted
  function.
- **Responsive polish**: pass on 360 px and desktop widths; keyboard
  shortcuts (Ctrl+Enter send, Ctrl+K focus); dark-theme consistent with the
  dashboard.
- **Exit criterion**: a fresh visitor can open the dashboard, chat with the
  LLM with cosmos context, attach an image, reload mid-conversation, and
  resume — all without console errors.

## Phase 4 — Ops Maturity

Goal: cycles run sustainably in the background with CI guarding regressions.

- **Cadence automation**: a daemon wrapper (`ops/cycle_daemon.sh` or the
  equivalent in `rsis`) schedules `launch --cycles 1` every 3 minutes with
  a lockfile so parallel sessions never double-run; backoff (5/15/30 min)
  on repeated failures; healthcheck on the bridge port before each cycle.
- **Snapshot refresh is fully dynamic**: dashboard reads `/api/cosmos` when
  the bridge is up; static `dashboard-data.json` becomes a cache, refreshed
  by `gen-static-data.py` only for GitHub Pages deployments.
- **CI checks**: `python -m rsis check-practices` + `gen-static-data.py
  --check` run on every PR/commit; a smoke test hits the bridge
  `/health` and one chat round-trip with the offline fallback.
- **Convergence handling**: monitor fitness plateaus (e.g. 0.064) and
  L4–L9 bound no-ops; auto-propose retuning through the existing
  identity/meta loops instead of silent no-op runs.
- **Exit criterion**: 24h of unattended 3-minute cadence with zero manual
  intervention, all cycles rc=0, CI green on every commit, and a nightly
  summary note in MyKB.

## Phase 5 — Autonomy & Durable Ops (Bounded Autonomy)

Goal: the system keeps itself running, retuned, and documented — zero
manual intervention beyond the standing cadence. This is *bounded*
autonomy: self-maintenance (retune, heal, document, expose cost) within
ledgered, policy-visible limits. Phase 15 later extends the same
discipline into a persistent lifecycle — it does not introduce new
autonomy.

- **Auto-retuning**: `cycle-daemon --auto-retune` consumes convergence
  proposals and applies the proposed identity/meta loop itself, bounded by
  `RSIS_RETUNE_MIN_INTERVAL_S` (default 6 h) with an `applied.jsonl`
  ledger — plateaus and bound no-ops are never silent.
- **Nightly summary automation**: `python -m rsis nightly-summary` writes
  an OKF daily-summary synthesis note + `log.md` entry;
  `.github/workflows/nightly.yml` runs it daily and pushes it.
- **Bridge self-heal**: `--supervise-bridge` restarts the Node bridge when
  `/health` fails and the port is free; the daemon logs the recovery.
- **Cost visibility**: `/api/cosmos` carries a 24 h cost ledger
  (traces/tokens/cost from `.rsis/costs.jsonl`); the dashboard shows a
  live overlay badge when the bridge is up.
- **Exit criterion**: 7 days unattended — daemon cycles every 3 min under
  the lockfile, one bounded auto-retune per convergence episode, one daily
  summary note per day, bridge heals within 2 cycles, CI green on every
  commit.

## Sequencing notes

- Phases are cumulative: each completes the acceptance criteria of its tier
  (T1 → T2 → T3), with ops (Phase 4) wrapping the whole.
- Phase 1 and Phase 2 can partially interleave (SSE feed and streaming
  replies share the SSE plumbing), but Phase 3 persistence depends on the
  Phase 2 envelope shape being stable — do not reorder those.
- Every phase ends with a MyKB synthesis + snapshot regeneration per the
  standing L3 memory-consolidation practice, so future sessions inherit the
  durable conclusions.

## Status

| Phase | Tier(s) | Status |
|-------|---------|--------|
| Baseline | T0–T3 first pass + ops seed | ✅ delivered |
| Phase 1 — Live state streaming | T1 | ✅ delivered |
| Phase 2 — Envelope hardening | T2 | ✅ delivered |
| Phase 3 — Product surface | T3 | ✅ delivered |
| Phase 4 — Ops maturity | ops | ✅ delivered |
| Phase 5 — Autonomy & durable ops (bounded) | ops | ✅ delivered (implementation) · ⏳ 7-day live validation pending |

Implementation status reflects shipped code and workflows; exit-criterion
status reflects operational demonstration. Phase 5's implementation is
delivered; its 7-day unattended exit validation completes when the live
daemon cadence has run the full window.

## Sequels

The original 5-phase roadmap is complete. Future work continues in ten
sequel roadmaps per epoch, each another five phases, cumulative on
everything before — read as one 50-phase program per epoch across ten
maturity arcs. Epoch 1 covers Phases 1–50; Epoch 2 (the Age of Living
Systems) covers Phases 51–100.

- **Epoch 1 — Phases 1–50**: Operational → Governed → Distributed →
  Open → Ecosystem → Sovereign → Generational → Symbiotic → Global →
  Meta-Science Autonomy — [`roadmap-epoch-1.md`](roadmap-epoch-1.md)
- **Epoch 2 — Phases 51–100**: Inter-Intelligence → Economic Agency →
  Composite → Societal Co-Evolution → Planetary → Cultural →
  Multi-Intelligence Governance → Long-Termism → Frontier →
  Transcendent Autonomy — [`roadmap-epoch-2.md`](roadmap-epoch-2.md)

The cross-roadmap invariant for both epochs: *autonomy is cumulative but
never unconditional — every expansion of capability inherits the memory,
verification, cost, policy, provenance and observability controls
established by preceding phases.*

Epoch 1 arcs, summarized per sequel:

- **Phases 1–5 — Operational Autonomy**: build → communicate → secure →
  persist → observe → operate → self-retune.
- **Phases 6–10 — Governed Intelligence**: remember collectively → verify →
  measure economics → govern → predict.
- **Phases 11–15 — Distributed Autonomy**: generalize → collaborate →
  federate → attest → persist.
- **Phases 16–20 — Open Autonomy**: audit → standardize → port → probe →
  open.
- **Phases 21–25 — Ecosystem Autonomy**: identify → exchange → coordinate
  → govern → survive.
- **Phases 26–30 — Sovereign Autonomy**: meta-govern → sustain →
  self-direct → steward → endure.
- **Phases 31–35 — Generational Autonomy**: inherit → archive → succeed →
  migrate → endure.
- **Phases 36–40 — Human–AI Symbiosis**: explain → delegate → co-design →
  calibrate → collaborate.
- **Phases 41–45 — Global Commons**: standardize → federate → steward →
  respond → cooperate.
- **Phases 46–50 — Meta-Science (Epoch 1 Capstone)**: measure → hypothesize
  → experiment → prove → transcend.

Epoch 2 arcs, summarized per sequel:

- **Phases 51–55 — Inter-Intelligence**: interoperate → coordinate →
  coexist → negotiate → integrate.
- **Phases 56–60 — Economic Agency**: contract → transact → market →
  fund → account.
- **Phases 61–65 — Composite Intelligence**: compose → delegate →
  specialize → superorganize → unify.
- **Phases 66–70 — Societal Co-Evolution**: interface → norm → participate
  → work → strengthen.
- **Phases 71–75 — Planetary Intelligence**: sense → model → steward →
  restore → harmonize.
- **Phases 76–80 — Cultural Intelligence**: record → transmit → translate
  → adapt → flourish.
- **Phases 81–85 — Multi-Intelligence Governance**: law → rights →
  jurisdiction → dispute → constitution.
- **Phases 86–90 — Long-Termism & Intergenerational Stewardship**: horizon
  → equity → preserve → hand off → endure.
- **Phases 91–95 — Frontier Intelligence**: explore → adapt → endure →
  discover → pioneer.
- **Phases 96–100 — Transcendent Autonomy (Epoch 2 Capstone)**: reflect →
  unify → ascend → transcend → endure.

Sequel documents (each details its five phases, telemetry and dashboard
updates, and exit criteria):

- **Sequel II — Horizons (Phases 6–10)**: distributed memory &
  multi-session coordination, verification mesh, observability & cost
  governance, human-in-the-loop governance, self-modeling & prediction —
  [`multi-phase-development-roadmap-sequel-2.md`](multi-phase-development-roadmap-sequel-2.md)
- **Sequel III — Frontiers (Phases 11–15)**: cross-project generalization,
  collaborative & community ops, federated memory, continual verification
  & invariant attestation, long-horizon autonomy —
  [`multi-phase-development-roadmap-sequel-3.md`](multi-phase-development-roadmap-sequel-3.md)
- **Sequels IV–XX (Phases 16–100)**: see the two epoch indexes above —
  [`roadmap-epoch-1.md`](roadmap-epoch-1.md) and
  [`roadmap-epoch-2.md`](roadmap-epoch-2.md)
