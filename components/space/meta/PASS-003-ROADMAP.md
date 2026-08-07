# SPACE — RSI Pass-003 Improvement Roadmap & Development Plan

**Date:** 2026-07-29
**Based on:** meta/PASS-003-AUDIT.md
**Status:** In Progress — 10 improvements to implement

---

## Phase Overview

| # | Improvement | Area | Files to Create | Files to Modify | Tests |
|:-:|-------------|------|:---------------:|:---------------:|:-----:|
| 1 | Wire ArtifactTracker into engine core | Engine | 0 | 2 | 5 |
| 2 | Wire Config validation into CLI startup | CLI | 0 | 1 | 3 |
| 3 | Implement `space config` CLI command | CLI | 0 | 1 | 3 |
| 4 | Implement `space serve` command for web UI | CLI | 0 | 2 | 3 |
| 5 | Wire SnapshotManager into engine flow | Engine | 0 | 1 | 5 |
| 6 | Implement localization/i18n infrastructure | i18n | 5 | 3 | 7 |
| 7 | Wire Git auto-commit into CLI sessions | Integration | 0 | 2 | 3 |
| 8 | Add staleness markers to export output | Export | 0 | 3 | 3 |
| 9 | Implement adaptive router with real logic | Intelligence | 0 | 1 | 5 |
| 10 | Add session resume framework version check | Engine | 0 | 1 | 3 |

---

## Execution Order

All items executed consecutively with testing after each phase.

