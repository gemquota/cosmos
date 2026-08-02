---
type: "concept"
title: "Planning Poker"
description: "The consensus-based estimation game for relative sizing"
tags: ["planning-poker", "estimation", "agile", "sizing"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://en.wikipedia.org/wiki/Planning_poker", "https://en.wikipedia.org/wiki/Story_point"]
---

# Planning Poker

## Summary
Planning poker estimates backlog items by relative size: everyone privately picks a card (Fibonacci or powers of two), reveals together, and discusses the outliers until consensus. It surfaces differing assumptions without groupthink and is fast enough to repeat often.

## Details
- The deck (0, 1, 2, 3, 5, 8, 13, 21) forces coarse, comparable sizes instead of false precision.
- Outlier discussion is the value: the person who said 3 and the one who said 13 usually disagree about scope.
- Anchor with reference items the team has sized before to keep scale consistent.
- Estimate in points, not hours: points are relative and stable across a team's experience.
- Keep sessions short and moderated; poker is for the backlog, not for commitment theater.
- For the mykb bundle, planning poker sizes curation features: link-verification automation vs a new capture source.
- Worked example — a wiki feature gets cards of 3, 5, 5, 8; the 8 comes from someone who remembers an integration gotcha, the discussion surfaces it, and the team settles on 5.

Worked example — a wiki feature gets cards of 3, 5, 5, 8; the 8 comes from someone who remembers an integration gotcha, the discussion surfaces it, and the team settles on 5.

## Related
- [[wiki/software-engineering/software-estimation|Software Estimation]]
- [[wiki/software-engineering/story-points|Story Points]]
- [[wiki/software-engineering/velocity-metrics|Velocity Metrics]]
- [[wiki/software-engineering/sprint-planning|Sprint Planning]]
- [[wiki/software-engineering/user-stories|User Stories]]
- [[wiki/software-engineering/backlog-grooming|Backlog Grooming]]
- [[wiki/software-engineering/estimation-techniques|Estimation Techniques]]
- [[wiki/software-engineering/agile-ceremonies|Agile Ceremonies]]
- [[wiki/communities/git-hooks|Git Hooks]]
- [[wiki/communities/bisect-workflows|Bisect Workflows]]
