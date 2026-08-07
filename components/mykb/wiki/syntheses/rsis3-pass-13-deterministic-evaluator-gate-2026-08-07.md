---
type: "synthesis"
title: "RSIS3 Pass 13 — deterministic evaluator gate: fail-closed quality gating without an API"
description: "Durable rules from pass 13: the immutable evaluator now runs a deterministic stdlib-only gate (path safety, compile, AST safety scan, regression, style/efficiency) before any optional LLM refinement; JSON/config candidates from L8/L9 bypass Python gates; diff fragments are dedent-checked; a hard FAIL can never be overturned by the LLM"
tags: ["rsis3", "passes", "evaluator", "quality-gate", "safety", "fail-closed", "llm-agents", "okf"]
timestamp: "2026-08-07T08:00:00Z"
status: "growing"
---

# RSIS3 Pass 13 — Deterministic Evaluator Gate

## Summary
The evaluator was a pure stub — it always returned PASS with perfect
scores, so every L2 candidate sailed through the quality gate and the
gate's telemetry was fiction. Pass 13 replaced the stub with a
deterministic, stdlib-only gate that runs in the immutable evaluator
process: validate the candidate shape, check target paths stay inside the
workspace, compile the code, scan the AST for unsafe patterns, and score
regression / style / efficiency heuristics. An LLM refinement pass is
optional (`RSIS_EVALUATOR_API_KEY`) and strictly fail-closed: it can only
downgrade a PASS or refine scores, never overturn a deterministic hard
FAIL. No API key means no network call at all — the gate is fully
functional offline and in CI.

## Details
- **Gate stages** (`evaluator/evaluator.py`, kept out of `rsis/` so the
  immutable subprocess stays a separate artifact): path safety rejects
  absolute, `..`, and Windows-form targets; compile is the correctness
  hard gate; the AST scan hard-fails on dynamic execution (`eval`/`exec`/
  `compile`), `shell=True`, destructive process/filesystem calls
  (`os.system`, `shutil.rmtree`, `pickle.loads`, ...), out-of-workspace
  writes, and destructive shell strings; regression hard-fails on removed
  definitions. Style/efficiency are heuristic soft scores with notes that
  surface as suggestions.
- **Candidate shapes matter.** L2 sends full module content (create-only
  scaffolds); L8/L9 send JSON tuning deltas. JSON/config candidates skip
  the Python gates (shape + destructive-string scan only) — otherwise
  every meta-tuning proposal would fail `compile`. This is the
  integration rule that keeps the L1–L9 batch green.
- **Diff fragments are dedent-checked.** Unified-diff added lines are
  fragments of an enclosing block; the gate strips the common indent
  before compile/AST checks, so a valid partial diff passes without
  silently skipping the safety scan (an unsafe indented fragment still
  fails).
- **Fail-closed LLM merge.** When the deterministic decision is FAIL the
  LLM cannot change it and cannot inflate scores; when PASS, the LLM may
  downgrade to FAIL or refine sub-scores. Determinism is the source of
  truth; the LLM is an optional refinement layer.
- **Tests** — `tests/test_evaluator_gate.py` (45 cases) loads the exact
  `evaluator/evaluator.py` artifact by path, exercises the CLI
  (`--verify` digest, stdin round-trip), and patches out API keys so the
  suite is hermetic.

## Rules
- A quality gate must fail closed without an API call; an LLM may refine
  a PASS but never rescue a FAIL. Score telemetry is only truthful when
  the gate actually gates.
- Know the candidate shapes that flow through the gate (full modules vs
  JSON deltas vs diffs) before writing checks — a gate that fails the
  system's own legitimate traffic is a bug, not a safeguard.
- Keep the evaluator stdlib-only and digest-verifiable; the deterministic
  path must run identically offline and in CI. See [[guardrails]] and
  [[wiki-self-improvement]] for the surrounding system-design rules, and
  [[rsis3-pass-12-improvement-engine-2026-08-07]] for the generate → gate
  → apply chain this gate completes.
