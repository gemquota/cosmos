---
type: synthesis
title: "MyKB Acquisition/Curation Pass & RSIS3 Usage-Practice Enforcement"
description: "Durable rules for acquiring concept notes into MyKB, curating hash-named junk entity pages, and enforcing RSIS3 workspace hygiene with check-practices"
tags: [synthesis, mykb, curation, acquisition, rsis3, practices, telemetry, checkpoints]
timestamp: "2026-08-01T00:00:00Z"
status: stable
source: []
---

# MyKB Acquisition/Curation Pass & RSIS3 Usage-Practice Enforcement

## Context

Two complementary passes: (1) acquire durable concept knowledge into MyKB and
curate its wiki of low-utility auto-generated junk; (2) add structural
documents that explain mykb conceptually to a human reader and that define +
enforce usage practices for RSIS3 workspaces. Rules here are the durable
conclusions from that session.

## Patterns

1. **Acquisition is typed, link-verified, and template-shaped.** New
   knowledge enters `wiki/concepts/` as OKF `type: concept` notes
   (`timestamp`, `status: growing`, `## Summary` / `## Details` /
   `## Related`). Every `[[wikilink]]` target must exist at write time; the
   linter catches strays, but a broken link is cheaper to fix before commit.
   This keeps the concept graph dense: new notes cross-link existing
   concepts (`tuning-ownership-diagonal`, `deadband-control`,
   `checkpoint-rollback`, …) so future sessions inherit the vocabulary.

2. **Hash-named entity pages are junk unless proven otherwise.** Pages whose
   stem is a long alnum blob (12+ chars, contains a digit) are almost always
   auto-generated entities with no durable content. Archive them with
   `git mv` to `raw/archive/junk-entities-<date>/` (preserving category
   paths) rather than deleting — provenance is kept and rollback is trivial.
   A page with real content (e.g. `beautifulsoup4-2.md`) is a false
   positive: inspect before archiving, keep on doubt.

3. **Structural docs pay for themselves as pointers.** A conceptual guide
   (`ops/conceptual-guide.md`, "mykb for Humans") with a layer model
   (raw → sources → notes → syntheses), a navigation walkthrough, and an
   RSIS3-consumption section converts an implicit knowledge model into
   onboarding material — and it is cross-linked from `README.md`,
   `Home.md`, and `ops/index.md`. Similarly, `rsis3/docs/usage-practices.md`
   plus a checker turns hygiene conventions into testable invariants.

4. **Enforcement lives in the code, not just prose.** `check-practices`
   (`rsis/practices.py`, exposed as `python -m rsis check-practices` and
   `ops/check_practices.py [WORKSPACE]`) verifies: the +3 ownership diagonal
   (L4→`l1.*` … L9→`l6.*`), disjoint registry keys, top-3 loops as untuned
   fixed points, disjoint state files, telemetry start+complete coverage
   with no errors, and `rsis-checkpoint:` git commits. It exits non-zero on
   FAIL and reports WARN for never-run loops — so a full-loop run becomes
   mechanically auditable (17/17 PASS on `.rsirrp/work/full-loop`).

5. **Snapshots and consolidation are part of the loop, not afterthoughts.**
   After a run: commit `.rsis/` state + telemetry, regenerate
   `dashboard/loops.json` + `ecosystem.json`, `--check` them, then write
   the synthesis note + `log.md` entry and rebuild the graph. Regeneration
   scripts that count via `git ls-files` require staging new files *before*
   running them.

## Related

- [[wiki/syntheses/nine-loop-stack-implementation|Nine-Loop Stack Implementation]]
- [[wiki/concepts/tuning-ownership-diagonal|Tuning Ownership Diagonal]]
- [[wiki/concepts/checkpoint-rollback|Checkpoint & Rollback]]
- [[wiki/concepts/telemetry|Telemetry]]
- [[wiki/ops/conceptual-guide|mykb for Humans — Conceptual Guide]]
- [[wiki/index|Wiki Index]]
