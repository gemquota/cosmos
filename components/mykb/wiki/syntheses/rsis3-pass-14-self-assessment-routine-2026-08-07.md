---
type: "synthesis"
title: "RSIS3 Pass 14 — self-assessment routine: deterministic-first KB health, gaps, trends"
description: "Durable rules from pass 14: `python -m rsis self-assess` runs six deterministic phases (health scan, gap analysis, trend detection, artifact writers, backlog filing, optional fail-closed LLM narrative) that read the KB and telemetry read-only, write create-only OKF notes under wiki/assessments, wiki/reflections, and wiki/backlog, and can never be overturned by the LLM"
tags: ["rsis3", "passes", "self-assessment", "knowledge-management", "telemetry", "fail-closed", "okf", "backlog"]
timestamp: "2026-08-07T16:01:39Z"
status: "growing"
---

# RSIS3 Pass 14 — Self-Assessment Routine

## Summary

Added a standing self-assessment command (`python -m rsis self-assess`)
that turns the KB, telemetry, and git history into durable OKF artifacts.
It composes six deterministic phases behind a single `SelfAssessment`
orchestrator: P1 KB health scan (links, orphans, stubs, content depth with
a weighted score), P2 coverage-gap analysis against recent syntheses, P3
trend detection from telemetry JSONL + git log, P4 assessment/reflection
writers, P5 create-only backlog filing with a guidance-queue mirror, and
P6 an optional fail-closed LLM narrative. The routine is read-only on
existing wiki content; all writes are new notes in new areas.

## Details

- **Phase order and artifacts**: `SelfAssessment.run()` records
  `sa_start`, scans health, loads the previous score, analyzes gaps, and
  detects trends before writing `wiki/assessments/self-assessment-<date>.md`
  and `wiki/reflections/reflection-<date>.md`; backlog notes land in
  `wiki/backlog/<slug>.md` (create-only, deduped by slug) and open gaps
  mirror into `.wiki-daemon/buffers/guidance-queue.json` (daemon shape
  `{"items": [...]}`) so downstream inference passes can consume them.
- **Deterministic-first**: every phase is stdlib-only and hermetic;
  subprocess tools (`kb_linter.py --json`) are timeout-bounded and
  fail-soft. A missing wiki, stub index, telemetry dir, or git repo
  degrades to notes, never to a crash. Malformed telemetry lines are
  skipped; malformed guidance buffers are no-ops.
- **Fail-closed LLM**: `enrich_llm` only runs with
  `RSIS_EVALUATOR_API_KEY`/`OPENAI_API_KEY` set and appends narrative
  after deterministic artifacts exist; any LLM failure is logged and
  ignored. Scores, gaps, trends, and backlog are final.
- **Wiring**: `SelfAssessConfig` (window, artifact dirs, daemon timeout),
  telemetry events `sa_start`/`sa_complete`/`sa_error`, CLI flags
  `--days/--no-backlog/--json`, and a `run-batch.sh` step after each
  scheduled batch. Version bumped to 0.4.4. First real run: health 0.837,
  0 gaps, 3 trends; 39 new tests; full rsis3 suite 159 passed;
  `check-practices` OK.

## Rules

- Self-assessment artifacts are OKF notes with frontmatter
  (`type`/`title`/`description`/`tags`/`timestamp`/`status`) — same
  convention as syntheses; the reflections index is refreshed by
  `build_index_pages.py`, never edited by hand.
- Artifact writers take the wiki root (`mykb/wiki`); the guidance-queue
  mirror takes the mykb root — keep those root semantics when adding
  phases.
- Backlog filing is create-only: an existing slug is never overwritten;
  dedupe on title in the guidance queue.
- Trends require ≥3 data points in the window; loop-completion, evaluator
  fail-rate, and commit cadence are the three default signals.
- Never run the LLM pass without a key; never let it alter deterministic
  findings — mirror the pass-13 evaluator's fail-closed contract.

## Related

- [[wiki-self-improvement]]
- [[guardrails]]
- [[rsis3-pass-13-deterministic-evaluator-gate-2026-08-07]]
