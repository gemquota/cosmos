# SPACE — Cycle 004 Improvement Roadmap

**Date:** 2026-07-29
**Based on:** `meta/CYCLE-004-AUDIT.md`
**Status:** Complete

---

## Overview

Cycle 004 shifts focus from feature development to **production readiness**. After Cycles 001-003 built the complete engine, CLI, export pipeline, storage, intelligence, and i18n infrastructure, Cycle 004 targets code quality tooling, documentation, testing coverage, developer experience, and infrastructure monitoring.

## Improvement Items

| # | Item | Area | Effort | Priority |
|:-:|------|------|:-----:|:--------:|
| 1 | Create comprehensive README.md | Docs | M | 🔴 High |
| 2 | Configure ESLint with TypeScript rules | Tooling | M | 🔴 High |
| 3 | Configure Prettier | Tooling | S | 🟡 Medium |
| 4 | Rename npm package to `@gemquota/space` | Config | S | 🟡 Medium |
| 5 | Add tsc/lint/test to CI workflow | CI | M | 🔴 High |
| 6 | Fix lint errors across codebase | Quality | L | 🔴 High |
| 7 | Add dev scripts (dev, format, typecheck) | DX | S | 🟡 Medium |
| 8 | Add CLI tests | Testing | M | 🔴 High |
| 9 | Create Sentry heartbeat monitor | Infrastructure | M | 🟡 Medium |
| 10 | Add Sentry Codex skill | Infrastructure | S | 🟢 Low |

## Execution Order

All items executed consecutively with verification after each.
