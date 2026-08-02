---
type: "concept"
title: "Failure Drills"
description: "Short, targeted exercises that test one recovery path at a time"
tags: ["failure-drills", "recovery", "practice", "reliability"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Failure Drills

## Summary
Failure drills test a specific recovery procedure in isolation — restore from backup, fail over a region, replay a queue — so the path is proven before it is needed. They are narrower and cheaper than full game days.

## Details
- Drill the boring but critical paths: restore, rollback, DNS switch, secret rotation.
- Time the drill and record the runbook steps that were wrong or missing.
- Automate drills where possible so they run regularly without humans.
- mykb relevance: monthly restore drills verify the wiki archive can actually come back.

## Related
- [[wiki/tooling/game-days|Game Days]]
- [[wiki/tooling/chaos-experiments|Chaos Experiments]]
- [[wiki/compositions/backup-and-restore|Backup and Restore]]
- [[wiki/tooling/restore-drills|Restore Drills]]
- [[wiki/software-engineering/reliability-engineering|Reliability Engineering]]
