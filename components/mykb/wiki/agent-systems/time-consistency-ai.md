---
type: "concept"
title: "Time Consistency"
description: "Preferences that do not change with time passage"
tags: ["time-consistency", "preferences", "rationality"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Time Consistency

## Summary
Time consistency is the property that a system's preferences do not change merely because time passes: what it chose for the future, it still wants when the future arrives. Time-inconsistent systems make plans their later selves abandon, which is the formal problem precommitment and commitment devices exist to solve.

## Details
- **Definition** — preferences are time-consistent when a plan chosen at time t for time t+k remains the plan the system chooses when it reaches t+k; violations show up as reversed decisions with no new information.
- **Why it breaks** — discounting and immediacy effects make near rewards more salient than distant ones, so a system that rationally chose a distant plan can rationally abandon it when the distant moment becomes near.
- **Agent manifestation** — an agent that schedules a difficult task for later, then declines to start it later, is time-inconsistent; so is an agent that commits to a safety policy and then renegotiates it mid-run.
- **Formal tools** — exponential discounting preserves time consistency; hyperbolic discounting does not, which is why commitment devices and precommitted rules are needed to restore it.
- **Relationship to myopia** — near-term myopia is the behavioral expression of time-inconsistent discounting: immediate consequences dominate because they are near, not because they are important.
- **Design guidance** — plan for time inconsistency by precommitting: fix the evaluation rules and plan before the run, and make deviation visible and costly.
- **mykb relevance** — precommitted pass specs and frozen check rules are time-consistency devices: they keep later behavior aligned with earlier intentions.

- **Measurement** — time consistency is measurable: compare the plan chosen for a future moment with the plan chosen when that moment arrives, holding information constant; divergence with no new information is the signature of inconsistency.

## Related
- [[wiki/agent-systems/precommitment-ai|Precommitment in AI]] — the fix
- [[wiki/agent-systems/discounting-practice|Discounting in Practice]] — the source of inconsistency
- [[wiki/concepts/preference-drift|Preference Drift]] — the broader change pattern
- [[wiki/agent-systems/commitment-devices-ai|Commitment Devices]] — the mechanism
- [[wiki/agent-systems/near-term-myopia|Near-Term Myopia]] — the behavioral failure
- [[wiki/concepts/utility-functions|Utility Functions]] — the formal setting
