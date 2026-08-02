---
type: "concept"
title: "Extreme Programming"
description: "The agile methodology that takes engineering practices to their limits"
tags: ["xp", "agile", "practices", "methodology"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://en.wikipedia.org/wiki/Extreme_programming", "https://agilemanifesto.org/"]
---

# Extreme Programming

## Summary
Extreme programming (XP) is an agile methodology that pushes good practices to extremes — continuous integration, test-driven development, pair programming, and small releases, all done relentlessly. It is built on five values: communication, simplicity, feedback, courage, and respect.

## Details
- XP's core loop is tight: write a failing test, make it pass, refactor, integrate — many times a day.
- Pair programming and collective ownership spread knowledge and keep quality high at the cost of pairing overhead.
- A simple design, the planning game, and small releases deliver working software early and often.
- The on-site customer keeps requirements grounded in real usage, which is the original form of modern product ownership.
- XP's practices reinforce each other: TDD makes refactoring safe, refactoring keeps design simple, and CI makes integration cheap.
- Teams adopt XP incrementally; even two practices (TDD plus CI) change a team's risk profile dramatically.

Worked example — a wiki team on XP writes a failing test for the link-checker, implements the check, refactors the parser, and integrates the change within the same hour, then pairs on the next feature.

## Related
- [[wiki/software-engineering/agile-methodology|Agile Methodology]]
- [[wiki/software-engineering/unit-testing-practice|Unit Testing Practice]]
- [[wiki/dev-tools/continuous-integration|Continuous Integration]]
- [[wiki/software-engineering/pair-programming|Pair Programming]]
- [[wiki/software-engineering/refactoring-techniques|Refactoring Techniques]]
- [[wiki/communities/standup-practices|Standup Practices]]
- [[wiki/dev-tools/code-coverage-tools|Code Coverage Tools]]
- [[wiki/tooling/smoke-tests|Smoke Tests]]
- [[wiki/software-engineering/mob-programming|Mob Programming]]
