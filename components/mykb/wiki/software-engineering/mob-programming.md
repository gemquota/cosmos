---
type: "concept"
title: "Mob Programming"
description: "The whole team working together on one task at one screen"
tags: ["collaboration", "practice", "team", "learning"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
---
# Mob Programming

## Summary

Mob programming puts the whole team on one task, one screen: a driver types while others direct, review continuously, and share context in real time. It is the strongest form of knowledge transfer and review — and the most expensive, so it is reserved for the highest-value work.

## Details
- Mechanism: a rotating driver role (timer-based) while the rest of the mob navigates: they design, catch errors as they happen, and keep the codebase in everyone's head; sessions are timeboxed with explicit goals and breaks; the driver types, the navigators decide — the ratio of thinking to typing inverts.
- Concrete example: a team mobs a gnarly migration that touches every module — one week of mobbing transfers the architecture to everyone and produces review-free code (it was reviewed continuously); a new hire's onboarding mobs a real feature instead of reading docs. The anti-pattern: mobbing simple, well-understood work that one person could do faster.
- Failure modes: mob fatigue and diminished returns beyond a few hours; dominant voices reducing participation; mobbing everything, starving parallel work; and sessions without a goal becoming unproductive meetings.
- Operational tradeoffs: mobbing trades throughput for shared understanding and quality — the right tool for complex, cross-cutting, or high-risk work; the pattern is mob the spikes and migrations, pair the features, solo the trivia. Rotate drivers and timebox religiously.
- RSIS3/mykb relevance: the wiki's hardest refactors are mobbed in real-time sessions, and the resulting decisions land in syntheses so the knowledge outlives the session.
- Session design: define the goal and the exit criteria before starting; mobbing without a target turns into a long meeting with a keyboard.
- Participation hygiene: enforce rotating drivers on a timer and invite the quiet voices in; the value is the collective review, which only exists if everyone contributes.

## Related
- [[wiki/software-engineering/pair-programming|Pair Programming]] — the two-person version of the same idea
- [[wiki/software-engineering/code-ownership|Code Ownership]] — mobbing makes ownership collective
- [[wiki/agent-systems/multi-agent-orchestration|Multi-Agent Orchestration]] — many agents, one goal
- [[wiki/software-engineering/onboarding-docs|Onboarding Docs]] — mobbing is the fastest onboarding there is
- [[wiki/software-engineering/code-review|Code Review]] — mobbing is review at team scale
- [[wiki/concepts/metacognition|Metacognition]] — team reflection is collective metacognition
