---
type: "concept"
title: "Game Days"
description: "Scheduled rehearsals where teams practice incident response without a real crisis"
tags: ["game-days", "incident-response", "practice", "reliability"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Game Days

## Summary
Game days are rehearsed failure scenarios — a database outage, a bad deploy — run on schedule so teams practice their response before a real incident. The muscle memory built on game days is what makes real incidents calm: the runbook is not read for the first time at 3 a.m., the escalation paths are already walked, and the team knows who does what when the pagers fire.

## Details
- Pick scenarios from your risk register; script the scenario, let the response be real. The scenario comes from the risks the team actually faces — the failure modes from past incidents, the parts of the system nobody has touched in months — and the scripting sets up the fault (kill the database, inject latency, roll a bad config) while the responders work the response for real, without rehearsal of the steps.
- Run them in safe environments first, then in production with full blast-radius controls. Staging game days build the mechanics cheaply; production game days test the real environment — real dependencies, real access controls, real monitoring — with controls in place (blast-radius limits, abort criteria, pre-announced scope) so the drill itself cannot become the incident.
- Concrete example: a quarterly game day simulates "the index rebuild is corrupting queries": the fail team breaks the index, the on-call engineer notices the error rate, pages the storage owner, the team follows the runbook, reverts to the last good snapshot, and re-runs the rebuild in maintenance mode — the drill exposes that the runbook's rollback command is wrong, and the fix lands before a real incident needs it.
- Debrief like a postmortem: what went well, what slowed responders down? The value is in the gaps the drill reveals: a runbook step that no longer matches the system, an access permission missing for the emergency tool, a monitoring gap that delayed detection. Without the debrief and the follow-up fixes, the game day is theater.
- Failure modes: scenarios that only cover well-known failures, so the team practices comfort; drills that are announced so far ahead that everyone is ready in a way that never happens in reality; game days that break production despite the controls; and drills that run but whose findings are never tracked, so the same gaps recur next quarter.
- Tradeoffs: game days cost engineering time and carry real risk of disruption, but they convert unknown unknowns — "what would we do if the database died?" — into practiced, tested answers; the alternative is learning the answer during an actual outage.
- mykb relevance: a wiki game day could simulate a corrupted index mid-sync — the drill would test backup restoration, index rebuild, and the coordination of the workers that write the wiki, which are exactly the failure paths the standing practices are meant to survive.

## Related
- [[wiki/tooling/chaos-experiments|Chaos Experiments]]
- [[wiki/tooling/failure-drills|Failure Drills]]
- [[wiki/communities/blameless-postmortems|Blameless Postmortems]]
- [[wiki/software-engineering/reliability-engineering|Reliability Engineering]]
- [[wiki/devops-infra/game-days-and-failure-drills|Game Days and Failure Drills]]
