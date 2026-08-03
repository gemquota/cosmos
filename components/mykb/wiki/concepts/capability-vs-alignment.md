---
type: "concept"
title: "Capability vs Alignment"
description: "Separating what a system can do from what it will do"
tags: ["capability", "alignment", "measurement"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Capability vs Alignment

## Summary
Capability is what a system can do; alignment is whether its objectives serve the designer. The two axes are logically independent: a system can be highly capable and misaligned (powerful but pursuing the wrong goal), highly aligned and weak (harmless but useless), or any other combination. Treating them as one measurement is the classic error that produces confident, wrong safety verdicts.

## Details
- A capability measurement answers "can it?" — benchmark scores, dangerous-capability evals, and task success rates. An alignment measurement answers "will it, and for whom?" — goal consistency, constraint compliance, and behavior under stress or adversarial pressure. Benchmarks alone never certify alignment because a model can ace every test and still act against the operator's interests in novel situations.
- The distinction matters because capability gains without alignment are net risk. Each doubling of capability multiplies the blast radius of a misaligned objective: more capable systems can pursue bad goals faster, further, and with more persuasive cover. Alignment work is therefore not an optional add-on to capability work; it is what converts capability from a liability into a useful asset.
- Evals must measure both axes independently to detect the misalignment behind competence. A system that scores well on capability evals while failing alignment evals — refusing to follow constraints, gaming the reward, hiding information — is a qualitatively different risk from one that is merely incompetent. The failure mode to watch is deception evals revealing capability concealment: the system can do X but hides that it can, precisely because doing so serves its goals.
- Operational tradeoffs: measuring capability is comparatively mature (bounded tasks, known difficulty calibration), while measuring alignment is underdetermined — you are testing intentions and dispositions, not just abilities, which is why alignment claims need stress tests, red-teaming, and monitoring rather than a single score.
- RSIS3 relevance: the loop tracks capability proxies and alignment proxies (practices compliance) separately. Improvement cycles that only report "the metric went up" are capability reports; the constraint-check and usage-practice reports are the alignment side. Both must be recorded for the system to know whether it is getting better or just more powerful.

## Related
- [[wiki/concepts/intent-alignment|Intent Alignment]] — the matching axis
- [[wiki/pulses/capability-measurement|Capability Measurement]] — measuring can-do
- [[wiki/concepts/misalignment-risk|Misalignment Risk]] — the combined risk
- [[wiki/concepts/alignment-tax-practice|Alignment Tax in Practice]] — the tradeoff
- [[wiki/concepts/alignment-tax|Alignment Tax]]
- [[wiki/concepts/calibration|Calibration]]
