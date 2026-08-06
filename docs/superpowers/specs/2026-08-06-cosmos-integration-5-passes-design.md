# COSMOS Integration — 5-Pass Design (SPACE Passes 007–011)

**Document:** COSMOS Integration Arc Design — SPACE Passes 007–011
**Doc ID:** COSMOS-PASS-ARC-007-011 | **Version:** 1.1 | **Generation date:** 2026-08-06
**Approach:** A — Contract-first (recommended), formal SPACE pass ledger
**Cross-references:** [RSIS3 Pass 6 synthesis](../../../components/mykb/wiki/syntheses/rsis3-pass-6-2026-08-06.md) · [Drive synthesis](../../../components/mykb/wiki/syntheses/rsis-drive-until-satisfied-2026-08-06.md) · [Architecture Spec](../../ARCHITECTURE-SPEC.md)

---

## 1. Arc context

The cosmos pass ledger is unified through the SPACE meta viewer
(`components/space/meta/`). PASS-001–005 are documented (Audit/Roadmap/Review/
Completion each); the pass-6 loop run (5 cycles × L1–L9, 40 executions, all
PASS) was executed but never received its `PASS-006` doc set. This arc:

1. **Backfills PASS-006** — writes the Audit/Roadmap/Review/Completion docs
   for the loop pass already executed and pushed.
2. **Runs PASS-007–011** — five formal SPACE passes focused on cosmos
   integration, each with the full doc set + the standing RSIS3 rhythm.

End state (locked): contracts + UX + ops cohesion, proven by a capstone run
that exercises SPACE spec → L2 goal → cycle → L3 MyKB consolidation →
dashboard end to end.

## 2. Pass ledger

| Pass | Theme | Status |
|------|-------|--------|
| 001–005 | SPACE component development | ✅ documented |
| 006 | Full L1–L9 loop batch (executed) | 🔄 docs backfilled by this arc |
| 007 | Data contracts & validation | ⏳ this arc |
| 008 | Memory link (loops ↔ MyKB) | ⏳ this arc |
| 009 | Spec link (loops ↔ SPACE, live Guide) | ⏳ this arc |
| 010 | UX cohesion | ⏳ this arc |
| 011 | Ops + capstone end-to-end validation | ⏳ this arc |

## 3. Standing pass rhythm (every pass, incl. backfill where applicable)

1. Full 5-cycle × L1–L9 batch (40 loop executions) via `python -m rsis drive`.
2. `python -m rsis check-practices` — all invariants PASS.
3. Formal SPACE meta-doc set in `components/space/meta/`:
   `PASS-###-AUDIT.md`, `-ROADMAP.md`, `-REVIEW.md`, `-COMPLETION.md`; update
   `PASSES-OVERVIEW.md` and `project-status.md`.
4. MyKB consolidation: dated `log.md` entry + OKF synthesis in
   `components/mykb/wiki/syntheses/`.
5. Snapshot regeneration: `build_graph.py`, `gen-static-data.py` + `--check`.
6. Commit in `components/rsis3` (nested) and cosmos; push `main`.

## 4. Backfill PASS-006 (pre-arc)

Write the four meta docs for the executed loop pass: audit (what ran — 40
executions, per-loop counts L1=11, L2=11, L3=8, L4=8, L5=12, L6=9, L7–L9=7,
`check-practices` PASS; fixes: `RSIS_DISK_USAGE_PCT` override + `main.py`
logger), roadmap (completed work), review (verification results), completion
(commits `878595b`/`174d37ba`/`7d3c3314`). Register in `PASSES-OVERVIEW.md`.

## 5. Pass sequencing (Approach A — contract-first)

### Pass 007 — Data contracts
- Document + validate the shared shapes the ecosystem emits: OKF frontmatter,
  telemetry JSONL (`l{n}_start`/`complete`/`error`), `files.json` /
  `ecosystem.json` / `loops.json`, SPACE spec export.
- Deliverable: contract spec + validator wired into `gen-static-data.py
  --check` and the loop pipeline, so passes 008–010 build on stable data.

### Pass 008 — Memory link
- Give RSIS3 a real MyKB gateway: loops read syntheses/OKF for context, and
  L3 consolidation *writes* MyKB synthesis notes + `log.md` entries itself
  (not by hand), then regenerates the graph.
- Verify: a run whose L3 leaves a durable, well-formed MyKB synthesis visible
  in the wiki/graph.

### Pass 009 — Spec link
- SPACE's 326-probe spec data feeds L2 ideation: map spec artifacts →
  candidate L2 goals; Guide's Direction/Research tabs render live loop +
  memory state instead of static lists.
- Verify: a run whose L2 goal trace references a SPACE spec artifact.

### Pass 010 — UX cohesion
- Finish the user-visible surfaces on live data: Guide model tabs, article
  categories, Graph/Edit/Archive/Delete toolbar, KG loading, links, sidebar.
- Verify: browser walkthrough of dashboard + Guide, no broken surfaces.

### Pass 011 — Ops + capstone
- Deploy/CI auto-sync for `gemquota.github.io/cosmos`, scheduled loop runner,
  monitoring; then the capstone run proving the full chain: SPACE spec →
  L2 goal → cycle → L3 MyKB consolidation → dashboard reflects it.

## 6. Success criteria (end state, all three locked)

- **Contracts**: every shared data shape documented + validated by tooling;
  `--check` catches drift before it ships.
- **UX**: dashboard/Guide feel like one product; no broken surfaces.
- **Ops**: deployed site auto-syncs; loops run on schedule without babysitting.
- **Capstone**: one run demonstrably exercises spec → goal → cycle → MyKB →
  dashboard.

## 7. Risks & mitigations

- **Terminology drift** (cycle/pass leftovers): the meta viewer is now the
  ledger; any `cycle` reference outside `lifecycle`/`DAG cycles` is a bug.
- **Scope sprawl in Pass 010**: UX work has historically sprawled; cap it to
  the surfaces listed and defer anything new to a possible post-011 arc.
- **Disk pressure** (device ~100% full): keep `RSIS_DISK_USAGE_PCT` override
  pattern for all batch runs.
