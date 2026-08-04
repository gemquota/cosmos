# 09 — Control Flow Analysis

**Doc ID:** COSMOS-AUDIT-09 | **Version:** 1.0 | **Generation date:** 2026-08-04
**Cross-references:** [10 Data Flow](10_DATA_FLOW_ANALYSIS.md) · [17 Concurrency](17_CONCURRENCY_ANALYSIS.md) · [19 Reliability](19_RELIABILITY_ANALYSIS.md)

---

## 1. Startup Sequence

1. **Static launcher** (`start.sh`): create `.cosmos-pids/`, `fuser -k` ports 9000/8765, start
   `python3 -m http.server 9000 --bind 0.0.0.0`, start `mykb/server.py 8765`, write pid files, install
   SIGINT/SIGTERM trap → `stop_all()`. [O]
2. **Optional heartbeat** (`cli/cosmos start`): `heartbeat.mjs --interval 30 --restart` → polls
   `watches.json`. [O]
3. **RSIS3 module** (`python -m rsis …`): `main.py` builds argparse, `cmd_*` calls `_init_subsystems()`
   → enforcer + telemetry threads → loop. [O]

```
start.sh → http.server:9000 (static, 0.0.0.0)
        → mykb/server.py:8765 (static+search+history)
cli/cosmos → heartbeat.mjs --interval 30 --restart → watches.json (3 services)
python -m rsis run --goal X → _init_subsystems → enforcer.start() → telemetry.start() → L1.run → finally stop()
python3 rsis/rack/server.py → ThreadingTCPServer(0.0.0.0:8765) → static dashboard
```

## 2. Configuration Loading (RSIS3, observed)

```
import rsis.config -> CONFIG = load_config()
  RSISConfig() defaults
  → env overrides (RSIS_*)
  → _apply_tuned_state(): L4..L9 state files → clamp → setattr
  (each state file: if exists+valid, apply param map; else warn+skip)
```

**Import-time side effect:** `CONFIG = load_config()` runs at import; tests must reload/reset module state
to test alternate configs [I, Med].

## 3. Dependency Initialization Order

`_init_subsystems()` constructs, in order: TelemetryCollector → CheckpointManager → MemoryManager →
EvaluatorClient → RecoveryManager(checkpoint) → ResourceEnforcer. Loops then receive these via
constructor/params. No service locator; explicit DI at the CLI boundary only [O].

## 4. One RSIS Pulse — Sequence Diagram (text)

```
main.cmd_run
  ├─ enforcer.start()          (thread, resource gate)
  ├─ telemetry.start()         (thread, flush interval)
  ├─ boot budget/ledger (budget_cap_usd, budget_exceeded)
  ├─ L1 run(goal, budget, tools)
  │     loop until goal-or-budget:
  │       emit action → ToolManager.run()
  │         → Sandbox.run_python / subprocess (tiers)
  │         → sandbox_result (ok|error|timeout)
  │       on error → error_classifier → retry logic (max_retries)
  │       evaluate outcome → ledger.record
  ├─ if timeout: raise TimeoutError (deadline ctx)
  └─ finally: telemetry.stop(); enforcer.stop()
```

## 5. Error / Retry / Cancellation Flow (observed)

- **Timeout:** `timeout.py` — `Budget`, `deadline(seconds,label)` context manager raising `TimeoutError`;
  every `cmd_*` wraps loop calls in `with deadline(...)` and catches `TimeoutError` → prints ✗, returns 1.
- **Retry:** L1 tool-call retries bounded by `CONFIG.l1.max_retries`; pipeline retry in `pipeline.py`
  (tested by `test_pipeline_retry.py`). Error classification in `error_classifier.py` chooses retry vs
  fail-fast categories.
- **Failure injection & recovery:** `recovery.py` — `FailureInjector` forces failures; `RecoveryManager`
  re-runs a failed command via `subprocess.run` and restores from checkpoint on crash.
- **Checkpoints:** `checkpoint.py` commits git checkpoints between steps; recovery can roll back.
- **Cancellation:** SIGINT/SIGTERM in `start.sh` stops pid-file-managed children; RSIS3 loops rely on
  `deadline` rather than signal-based cancel. **No explicit cooperative-cancel token on L2 parallel
  candidates** [I, Med].

## 6. Concurrency Model (summary — details in [17](17_CONCURRENCY_ANALYSIS.md))

- Threads: `ResourceEnforcer`, `TelemetryCollector` (background), `ThreadingTCPServer` (rack), MyKB
  `HTTPServer` default threading, heartbeat poll loop.
- Optional parallel candidates: L2 `parallel_candidates=N` uses a DAG fan-out; `SharedMemoryManager`
  shares context; a `queue.Queue` exists in a few modules.
- No async/await in Python core; SPACE is single-threaded synchronous Node (ESM) with no worker threads.

## 7. Shutdown

- Launcher: trap → kill each pid file, rm pid files, exit.
- RSIS3 loops: `finally` stops telemetry/enforcer; recovery runs before exit on failures.
- SPACE servers: no graceful shutdown; killed by pid/`fuser` (web/server.mjs documented to need PM2). [O]

## 8. Flow Diagrams (ASCII)

**RSIS loop stack (as-built):**
```
        ┌────────────────────────────────────────────┐
   L6──▶L3 (evolution)   ◀──tunes── L9 (MMM)
        L3 ─▶ memory consolidation → MyKB syntheses
        L2 (improvement) ◀──tunes── L5 (strategies)
        L1 (action)      ◀──tunes── L4 (optimizer)
                     L7 tunes L4 · L8 tunes L5
        substrate (loops write .rsis/* files)
        └────────────────────────────────────────────┘
```

**Dashboard data path:**
```
loops/loops.json ─┐
rack/pulses/*.json─┼─ gen-static-data.py ──► dashboard-data.json ──► dashboard app.js (fetch) ──► index.html
gen-static-data.py ─► files.json / ecosystem.json
```

## 9. Findings

- **F1** — No cancellation tokens for parallel candidate branches; a killed process mid-DAG leaves
  partial state. [I, Med]
- **F2** — `TimeoutError` is caught broadly; a timeout mid-telemetry-flush could drop metrics. [I, Low]
- **F3** — SPACE web server responses are synchronous; a long export blocks the event loop
  (single-threaded Node). [O, Med]
- **F4** — `fuser -k` in `start.sh` is destructive on shared hosts; binds 0.0.0.0. [O, High]

---
*End of document 09. Next: [10 Data Flow Analysis](10_DATA_FLOW_ANALYSIS.md).*
