---
type: "concept"
title: "Agile Ceremonies"
description: "The recurring meetings that structure an agile team's rhythm: planning, standup, review, retrospective"
tags: ["agile", "process", "team", "scrum"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
---
# Agile Ceremonies

## Summary

Agile ceremonies are the recurring meetings — standup, planning, review, retro — that create rhythm, alignment, and learning. They are lightweight coordination rituals, not bureaucratic overhead; their value depends entirely on keeping them short, decision-oriented, and honest.

## Details
- Mechanism: the sprint cycle structures work: planning commits scope and sets goals; standup (daily, 15 min) surfaces blockers and coordination; review demonstrates working software and collects feedback; retro reflects on process and produces concrete action items. Ceremonies should be timeboxed, attended by the people who can act, and produce outputs (committed backlog, demo, action items).
- Concrete example: a team's retro identifies flaky tests as the top waste, produces one action (dedicated flake-fixing timebox), and tracks it next sprint; planning uses velocity (measured, not guessed) to size; the review shows real running features, so stakeholders steer early. The anti-pattern: ceremonies that run long, review only slides, and retros that produce no follow-up.
- Failure modes: ceremony theater — meetings with no decisions; standups that become status reports to a manager; planning without capacity realism; retros without accountability (action items vanish); and over-process that slows small teams (a 2-person team may need only a weekly sync).
- Operational tradeoffs: ceremonies trade meeting time for alignment and early feedback; the discipline is timeboxes, explicit outputs, and continuous tuning of the ceremony set itself. For solo/agent-driven work, the equivalent is a written plan + review cadence rather than meetings.
- RSIS3/mykb relevance: the wiki's loop schedules would mirror these cadences — planning, review, retro as checkpoints — with action items tracked so improvements persist.
- Timeboxing: default to 15/45/60-minute caps and a facilitator who cuts drift; ceremonies that grow are the first sign the team is using meetings instead of artifacts.
- Outputs-first: each ceremony should end with a written output (committed scope, demoed feature, action items); without artifacts, ceremonies evaporate into conversation.

## Related
- [[wiki/software-engineering/estimation-techniques|Estimation Techniques]] — planning ceremonies consume estimates
- [[wiki/software-engineering/pair-programming|Pair Programming]] — a daily collaboration practice that complements ceremonies
- [[wiki/software-engineering/code-review|Code Review]] — the review ceremony's technical twin
- [[wiki/memory/wiki-science|Wiki Science]] — the wiki's own curation cadence
- [[wiki/agent-systems/agent-loop|Agent Loop]] — ceremonies are the human agent loop
