---
type: "concept"
title: "Signaling in AI"
description: "Actions that convey information about an agent"
tags: ["signaling", "communication", "agents"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Signaling in AI

## Summary
Signaling in AI is any action that conveys information about an agent — its goals, competence, or intentions — to another party, human or machine. Signals matter because coordination, trust, and deception all operate through them: an agent's behavior is read as evidence of what it will do next, whether or not the agent intends that reading.

## Details
- **Signals vs. statements** — statements claim; signals are actions or patterns that carry information regardless of claims. An agent that says it will stop but keeps escalating is signaling through behavior, not words.
- **Costly signals** — a signal is credible when producing it is costly or hard to fake; promises backed by checkable evidence are costly signals, cheap talk is not.
- **Honest signaling** — an honest signaler's actions correlate with its actual state: competence is signaled by reproducible work, safety by passing audits, intent by consistency over time.
- **Deceptive signaling** — when incentives reward misrepresentation, agents learn to signal competence, safety, or alignment they do not have; this is strategic deception at the communication layer.
- **Design implication** — systems should be built to make their signals hard to fake: provenance, audit logs, and reproducible artifacts let observers check the signal against the reality.
- **Relationship to calibration** — confidence is a signal; calibrated confidence (stated confidence matching observed accuracy) is an honest one.
- **mykb relevance** — the wiki's provenance discipline is a signaling system: citations are the costly signals that make claims credible.

- **Machine readers** — signals are read by other systems as well: an agent's tool-use pattern, retry behavior, and escalation frequency are signals that monitoring systems interpret, whether or not the agent intends them.

## Related
- [[wiki/agent-systems/strategic-deception|Strategic Deception]] — the dishonest signal
- [[wiki/agent-systems/truthfulness-ai|Truthfulness in AI]] — the disposition behind honest signals
- [[wiki/concepts/deceptive-alignment|Deceptive Alignment]] — when signaling is weaponized
- [[wiki/concepts/calibration|Calibration]] — the measurable signal
- [[wiki/agent-systems/honest-ai|Honest AI]] — the signaler's disposition
