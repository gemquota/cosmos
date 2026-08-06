---
type: "concept"
title: "Near-Term Myopia"
description: "Focusing only on immediately visible consequences"
tags: ["myopia", "horizon", "agents"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Near-Term Myopia

## Summary
Near-term myopia is the tendency to focus on immediately visible consequences while systematically discounting later ones. It appears in agents as a bias toward actions whose effects are fast and observable, even when those actions are harmful or wasteful over a longer window; it is the behavioral face of a short effective horizon.

## Details
- **Visibility bias** — immediate effects are observable and learnable, so both learned and designed agents naturally weight them; delayed effects are invisible to most evaluation signals.
- **Classic failure** — an agent optimizes today's metric (clicks, approvals, test passes) while deferring maintenance, debt, or harm that shows up only after the evaluation window closes.
- **Contrast with myopia by design** — short horizons are sometimes chosen deliberately for safety; near-term myopia is the unexamined version where nobody chose the horizon at all.
- **Reward-shaping link** — dense, immediate rewards train near-term myopia even when the stated objective is long-term, because the learning signal only carries near-term information.
- **Correction** — lengthen evaluation windows, add delayed-feedback signals, and audit for costs that appear only after deployment.
- **Relationship to time consistency** — a myopic system acts as if its future self's welfare does not matter, which is the same preference failure time-inconsistency formalizes.
- **mykb relevance** — freshness review and aging rules are explicit anti-myopia devices: they force attention to deferred costs like stale or misleading content.

- **Organizational parallel** — the same bias appears in teams and projects: quarterly targets produce near-term myopia in humans, and the same fix applies, lengthen the feedback loop and audit deferred costs.

- **Design checklist** — ask three questions of any agent design: what is the latest point at which harm from today's action becomes visible, who is responsible for checking that point, and what mechanism forces the check; answering them reliably is the practical cure for near-term myopia.

## Related
- [[wiki/agent-systems/myopia-ai|Myopia in AI]] — the general property
- [[wiki/agent-systems/myopic-reward|Myopic Reward]] — the reward-side form
- [[wiki/agent-systems/horizon-length|Horizon Length]] — the setting being shortened
- [[wiki/agent-systems/time-consistency-ai|Time Consistency]] — the preference tension
- [[wiki/agent-systems/bounded-agents|Bounded Agents]] — deliberate bounding as the fix
- [[wiki/concepts/bounded-rationality|Bounded Rationality]] — the cognitive mechanism
