---
type: "concept"
title: "Game Days"
description: "Scheduled rehearsals where teams practice incident response without a real crisis"
tags: ["game-days", "incident-response", "practice", "reliability"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Game Days

## Summary
Game days are rehearsed failure scenarios — a database outage, a bad deploy — run on schedule so teams practice their response before a real incident. The muscle memory built on game days is what makes real incidents calm.

## Details
- Pick scenarios from your risk register; script the scenario, let the response be real.
- Run them in safe environments first, then in production with full blast-radius controls.
- Debrief like a postmortem: what went well, what slowed responders down?
- mykb relevance: a wiki game day could simulate a corrupted index mid-sync.

## Related
- [[wiki/tooling/chaos-experiments|Chaos Experiments]]
- [[wiki/tooling/failure-drills|Failure Drills]]
- [[wiki/communities/blameless-postmortems|Blameless Postmortems]]
- [[wiki/software-engineering/reliability-engineering|Reliability Engineering]]
- [[wiki/devops-infra/game-days-and-failure-drills|Game Days and Failure Drills]]
