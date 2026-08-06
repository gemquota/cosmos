# SPACE — RSI Pass 007 Audit Report

**Project:** Superb Prompt Automatic Creation Engine (SPACE) · COSMOS integration arc
**Date:** 2026-08-06
**Pass:** RSI Pass 007 — Data contracts & validation (Approach A, contract-first)
**Scope:** Ecosystem data contracts + full L1–L9 loop batch

---

## Executive Summary

Pass 007 made the inter-component data shapes explicit and machine-checked.
Six contracts were documented and enforced by a stdlib-only validator, wired
into both gates (`gen-static-data.py --check` and `check-practices`), and the
standing full 5-cycle × L1–L9 batch ran with +5 net starts per loop and zero
errors.

## Data Contracts Delivered

| Shape | Location | Key rules |
|-------|----------|-----------|
| OKF frontmatter | `components/mykb/wiki/**/*.md` | `type`/`title` required, type vocabulary, optional keys WARN |
| files.json | `components/mykb/files.json` | paths resolve, unique, no `components/` prefix |
| ecosystem.json | `components/rsis3/dashboard/ecosystem.json` | telemetry arithmetic `passed+failed+held == total` |
| loops.json | `components/rsis3/dashboard/loops.json` | L0–L9 ids, required keys, status vocabulary |
| Telemetry JSONL | `components/rsis3/.rsis/telemetry/*.jsonl` | one JSON object/line, snake_case `type`, ISO timestamp |
| SPACE framework | `components/space/prompt-framework/framework.json` | series totals sum to meta totals (67+259=326) |

- Spec: `contracts/README.md` · Validator: `contracts/validate.py` (stdlib only).
- Wired into `gen-static-data.py --check` (deploy/CI) and `check-practices`
  (`telemetry contract`: 100 files / 359 events / 0 malformed).

## Loop Batch

- 5 cycles × L1–L9 = 40 executions, +5 net starts per loop, 0 errors.
- Telemetry after pass: L1=16, L2=16, L3=14, L4=14, L5=18, L6=15, L7=13,
  L8=13, L9=12. (The +1 on L3–L8 is one partial aborted cycle from a
  mis-set disk override; the batch proper was +5 per loop.)
- Disk rule learned: `RSIS_DISK_USAGE_PCT` replaces the *limit*, not the
  measured value — use 100 when the device is ~100% full.

## Durable Rules

- New shared data products get a contract section + validator before passes build on them.
- Shape violations fail the gate; snapshot drift is fixed by regeneration, never by editing snapshots.
- `--check` separates contract FAILs from snapshot staleness (caught the
  pass-6 synthesis missing from `files.json`).
