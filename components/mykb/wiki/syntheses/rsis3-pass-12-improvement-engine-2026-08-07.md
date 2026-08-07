---
type: "synthesis"
title: "RSIS3 Pass 12 — real improvement engine: L2 codegen, batch launcher, stub detection"
description: "Durable rules from pass 12: L2 now generates and applies real code improvements (missing-module scaffolds, create-only writes, LLM hook), `rsis launch` runs the full L1–L9 batch from Python, StubDetector turns actual code state into prioritized improvement goals, and the RRP pulse tool runs on real modules with real targets"
tags: ["rsis3", "passes", "l2", "improvement-loop", "launch", "stub-detector", "rrp", "pulse", "okf"]
timestamp: "2026-08-07T06:00:00Z"
status: "growing"
---

# RSIS3 Pass 12 — Real Improvement Engine

## Summary
Before pass 12 the improvement path was simulated end to end: L2 emitted a
hardcoded `Stub improvement` targeting `stub.py`, `_apply_improvement` never
wrote a file, `rack/run_rrp_pulse.py` imported five modules that did not
exist, and `rack/rrp_conversation.py` could not even import
(`rsis.rrp_bridge` missing). Pass 12 replaced the simulation with a real,
deterministic engine: L2 parses the goal for a target path or takes the
top finding from a new workspace stub detector, scaffolds the missing module
with compilable typed code, and applies it with create-only writes. The
end-to-end chain was demonstrated live: `python -m rsis run` generated and
applied `rsis/launch.py` on the exact goal pulse-020 had flagged, and a
regenerated pulse-021 lists only real findings.

## Details
- **StubDetector** (`rsis/signals/stub_detector.py`) — priority-ranked
  findings: `missing_module` (dangling `rsis.*` imports, 1.0) >
  `not_implemented` (0.8) > `pass_body` (0.6) > `todo` (0.3). Skips abstract
  methods (`@abc.abstractmethod` + `NotImplementedError` is idiomatic) and
  pass-only exception classes.
- **L2 codegen** (`rsis/loop_l2.py`) — `_generate_candidate` resolves
  `Implement <Name> in <path>` from the goal (regex), else scans for the
  highest-priority missing module; scaffolds a module with docstring, `from
  __future__ import annotations`, and a typed class/function; returns `None`
  when no safe target exists so the session moves on. `_apply_improvement`
  writes only missing files (never overwrites existing code) and records
  `applied_files` on the candidate. `RSIS_L2_LLM_GENERATOR=<module>` swaps in
  an LLM `generate_candidate` hook.
- **Batch launcher** (`rsis/launch.py`) — `python -m rsis launch --cycles N
  --goal-space-cycle C` runs the L1–L9 rhythm from Python (mirrors
  `infra/loops/run-batch.sh`), `--dry-run` prints the plan, and
  `run_batch(executor=...)` is unit-testable without subprocesses.
- **Pulse tool repaired** — `rack/run_rrp_pulse.py` now imports only real
  modules; pre/post state reads `.rsis/identity_state.json` +
  `strategies.json` + live `KnowledgeGraph`. Pulse-021 regenerated with real
  goals (`_timeout_via_polling`, `rack/server.py:log_message`).
- **Stubs implemented** — `rsis/timeout.py:_timeout_via_polling` now arms a
  watchdog thread raising `TimeoutError` via `PyThreadState_SetAsyncExc`
  (non-SIGALRM fallback, verified: fires at 0.20s for a 0.2s deadline);
  `rack/server.py:log_message` logs at DEBUG instead of `pass  # quiet`.
  `rsis/rrp_bridge.py` implements `RRPBridge.refine_goal` (keyword→LOCKED
  constraints, contradiction heuristic), unbreaking `rack/rrp_conversation.py`
  (verified: auto conversation runs to PASS with full constraint profile).

## Rules
- An improvement loop is only real when generate → gate → apply all three
  mutate state; a PASS from the gate must result in an on-disk change.
- Never overwrite existing code from a deterministic generator; create-only
  writes keep the loop safe and reviewable.
- Improvement goals should come from scanned code state, not canned lists —
  otherwise the loop optimizes a fiction.
- Batch orchestration belongs in the core package (`rsis launch`) so it is
  testable; the shell script stays as the CI entry.
