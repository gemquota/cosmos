# RSIS3 Self-Assessment Routine — Design

**Document:** COSMOS Self-Assessment Design
**Doc ID:** COSMOS-SELF-ASSESS-001 | **Version:** 1.0 | **Date:** 2026-08-07
**Approach:** A — phase-based self-contained module in RSIS3
**Cross-references:** [Architecture Spec](../../ARCHITECTURE-SPEC.md) ·
[Pass 13 synthesis](../../../components/mykb/wiki/syntheses/rsis3-pass-13-deterministic-evaluator-gate-2026-08-07.md)

---

## 1. Context & goals

RSIS3 runs nine loops that mutate code, memory, and tuning state, and it
consolidates durable rules into MyKB. What it never does is look at its own
house: read the KB, review its health, curate it, find gaps, acquire new
knowledge, and reflect on goals / recent actions / trends. This design adds a
routine self-assessment capability as a self-contained command:

`python -m rsis self-assess`

Goals:
1. **KB review & curation** — deterministic health checks (links, orphans,
   stubs, content metrics) with deltas vs. the previous assessment.
2. **Gap assessment** — missing topics / thin coverage relative to recent
   syntheses, pulses, and active goals; surfaced as backlog items.
3. **Research & acquisition** — gaps file into `wiki/backlog/` and mirror
   into the existing guidance-queue buffer so downstream inference passes can
   expand / seed pages.
4. **Meta-assessment** — review recent actions (telemetry, `log.md`, git),
   active goals, and loop state; identify trends and patterns.
5. **Reflection expansion** — write a prose reflection note per run so the
   `wiki/reflections/` area grows and stays linked.

Design stance (matches the evaluator gate, pass 13): deterministic-first,
stdlib-only core, optional fail-closed LLM enrichment.

## 2. Scope

### In scope
- New `rsis/self_assess.py` module + `SelfAssessConfig` + CLI subcommand.
- Deterministic phases 1–5 (health, gaps, actions/trends, artifacts, backlog).
- Optional LLM enrichment phase (phase 6) gated on an API key.
- `wiki/assessments/`, `wiki/reflections/`, `wiki/backlog/` artifacts.
- `infra/loops/run-batch.sh` hook (scheduled) + on-demand CLI.
- Telemetry (`sa_start` / `sa_complete` / `sa_error`), tests, docs, MyKB
  consolidation after first real run.

### Out of scope (future)
- Automatic KB mutation (link auto-fixes, stub expansion) — report + backlog
  only; the daemon's `--fix` tools stay manual.
- Dashboard UI for assessments (the wiki browser picks up the new areas
  automatically once snapshots regenerate).
- LLM-driven research execution — backlog items are the handoff, not the
  researcher.

## 3. Architecture

Phase-based single module (Approach A). Each phase is a pure function taking
context and returning a typed result; the orchestrator composes them:

```
self-assess
 ├─ P1 KB health scan      → HealthReport
 ├─ P2 gap analysis        → GapList
 ├─ P3 actions & trends    → TrendReport
 ├─ P4 artifacts           → AssessmentNote + ReflectionNote
 ├─ P5 backlog             → BacklogWrite
 └─ P6 LLM enrichment      → optional narrative (fail-closed)
```

- Deterministic phases run first and produce the complete report; the LLM
  phase (if a key exists) only appends narrative. No API key → fully
  functional offline.
- All daemon tool invocations are `subprocess` with a timeout, captured
  output, and graceful degradation (tool missing/failing → score 0 + note,
  never a crash).

## 4. CLI & config

```
python -m rsis self-assess [--days N] [--no-backlog] [--json]
```

- `--days N` — analysis window (default 7).
- `--no-backlog` — suppress backlog filing (dry-run style).
- `--json` — print the machine-readable report summary to stdout.

`SelfAssessConfig` (new dataclass in `config.py`):
- `window_days: int = 7`
- `assessments_dir: str = "wiki/assessments"`
- `reflections_dir: str = "wiki/reflections"`
- `backlog_dir: str = "wiki/backlog"`
- `daemon_timeout_s: int = 60`
- `llm_enabled: bool = True` (respects API-key presence)

Telemetry events follow the loop convention: `sa_start`, `sa_complete`
(metadata: health score, gaps found, trends, artifacts written), `sa_error`.

## 5. Data sources

| Source | Path / command | Used by |
|--------|----------------|---------|
| KB health | `kb_linter.py --json`, stub index, `build_stats.py` | P1 |
| Wiki content | `wiki/**/*.md`, frontmatter (via daemon `frontmatter.py`) | P1/P2 |
| Syntheses/pulses | `wiki/syntheses/`, `wiki/pulses/` | P2 |
| Coverage search | `MyKBGateway` (token-overlap search) | P2 |
| Telemetry | `.rsis/telemetry/*.jsonl` | P3 |
| Log | `components/mykb/log.md` | P3 |
| Git history | `git log --since=<window>` | P3 |
| Goals/state | `.rsis/*_state.json`, `dashboard/loops.json`-style snapshots | P3 |
| Backlog mirror | `.wiki-daemon/buffers/guidance-queue.json` (when present) | P5 |

## 6. Artifacts (OKF)

### 6.1 Assessment note — `wiki/assessments/self-assessment-YYYY-MM-DD.md`
Frontmatter: `type: assessment`, `title`, `description`, `tags`,
`timestamp`, `status: stable`, `window_days`, `health_score`, `prev_note`.

Body sections: health summary (links/orphans/stubs/metrics + deltas),
gaps found, trends/patterns, action/reflection cross-refs, backlog refs
(`[[wikilinks]]` to each new backlog note).

### 6.2 Reflection note — `wiki/reflections/reflection-YYYY-MM-DD.md`
Frontmatter: `type: reflection`, `title`, `description`, `tags`,
`timestamp`, `status: growing`.

Body: surprises, belief changes, open questions, and a link to the
assessment note. The reflections index (`00-index.md`) is refreshed by the
existing `build_index_pages.py` during snapshot regeneration — no manual
index edits.

### 6.2a Gap algorithm (P2)

For each recent synthesis / pulse / active-goal topic, extract keywords
(title + description tokens, filtered). A topic is **covered** when the
token-overlap search (reusing the `MyKBGateway` search) finds a wiki page
sharing ≥2 significant tokens; otherwise it becomes a gap item. Thin
coverage (page exists but body words < 320 floor) is filed as a
`priority: medium` gap; missing topics as `priority: high`.

### 6.3 Backlog note — `wiki/backlog/<slug>.md`
Frontmatter: `type: backlog`, `title`, `description`, `tags`,
`timestamp`, `status: open`, `source: gap|research|trend`,
`priority: high|medium|low`, `assess_ref`.

Deduplication rule: a gap is filed only if no open backlog note with the
same slug exists. Create-only writes; existing notes are never overwritten.
Open items are mirrored (append-if-absent) into
`.wiki-daemon/buffers/guidance-queue.json` when the buffer exists.

## 7. Health scoring (P1)

- Link health: `1 - broken_links/total_links` (weight 0.25)
- Orphan health: `1 - orphans/total_pages` (weight 0.15)
- Stub health: `1 - stubs/total_pages` (weight 0.30)
- Content depth: min(1, body_words_per_page / 320-floor) (weight 0.30)
- Overall = weighted sum, 0.0–1.0, reported with per-metric deltas vs. the
  previous assessment note.

## 8. Trend detection (P3) — heuristics

- Per-loop event counts and completion ratios from telemetry JSONL
  (`l*_start` vs `l*_complete`); failures surface as patterns.
- Evaluator decision mix (PASS/FAIL ratio) over the window.
- Success-rate / signal series for tuned loops (L4–L9) if present.
- Git commit frequency and reverted/`fix`-prefixed commit share.
- `log.md` entry cadence (KB activity).
- Each trend is a `{name, direction, magnitude, evidence}` tuple; only
  trends with ≥3 data points in the window are reported.

## 9. LLM enrichment (P6, optional)

- Enabled only when `RSIS_EVALUATOR_API_KEY` or `OPENAI_API_KEY` is set and
  the `openai` package imports.
- Appends narrative to the assessment note (trend interpretation, research
  leads) after deterministic artifacts are written.
- Fail-closed: deterministic report, scores, gaps, and backlog are final;
  LLM text is additive only. LLM failure → note recorded, exit code 0.

## 10. Wiring

- `main.py`: `add_parser("self-assess", ...)` + `cmd_self_assess`.
- `infra/loops/run-batch.sh`: add a `self-assess` step to the post-batch
  gates (after `check-practices`), so the scheduled batch produces one
  assessment + reflection per run.
- Version bump to `0.4.4`; CHANGELOG entry.

## 11. Guardrails

- Read-only on existing wiki content: writes only new files
  (assessments/reflections/backlog), never overwrites, never touches
  uncommitted user edits.
- Daemon subprocesses: timeout-bounded, fail-soft.
- Hermetic by default: no network, no API calls without a key.
- Bounded runtime: single pass, fixed phases, no loops.

## 12. Testing

- `tests/test_self_assess.py`:
  - Health scoring against a small fixture wiki (broken link, orphan, stub).
  - Gap detection from fixture syntheses + stub index.
  - Trend detection from fixture telemetry JSONL + a fixture git repo
    (temp repo with dated commits).
  - Artifact writing (create-only, dedupe, frontmatter shape).
  - Backlog mirroring into a fixture guidance-queue buffer.
  - CLI subcommand round-trip (`--days`, `--no-backlog`, `--json`).
  - LLM phase disabled without a key (hermetic env).
- Full suite: all existing rsis3 tests keep passing.

## 13. MyKB & snapshot practice

After the first real run: dated `log.md` entry, synthesis note for the
pass, then `build_graph.py` → `gen-static-data.py` → `--check`, commit per
AGENTS.md.
