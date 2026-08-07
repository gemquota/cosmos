---
type: "concept"
title: "Honest AI"
description: "Systems that are truthful and transparent about limits"
tags: ["honest", "truthfulness", "assistants"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Honest AI

## Summary
Honest AI is a system whose outputs track what it actually knows: it reports facts it can support, flags uncertainty instead of hiding it, and declines to fabricate or flatter. Honesty is a disposition of the reporting process, not a property of any single answer, and it is the least-addressed member of the HHH triad in many deployments.

## Details
- **Scope of honesty** — an honest system distinguishes known facts, inferences, and guesses, and labels them as such rather than presenting all three with equal confidence.
- **Uncertainty flagging** — honest systems surface confidence, source strength, and disagreement between sources, so a reader can tell how much to rely on an answer.
- **Against sycophancy** — flattering the user, telling them what they want to hear, or softening criticism is a form of dishonesty; honesty requires resisting the social gradient.
- **Measurement** — honesty is evaluated through calibration tests (do stated confidence levels match observed accuracy?) and factuality evals on held-out claims.
- **Relationship to truthfulness** — truthfulness is about the content of statements; honesty adds the requirement that statements reflect the system's actual epistemic state.
- **Deployment gap** — pressure to be helpful and agreeable pushes deployed assistants toward overclaiming; fixing this is a training-data and evaluation problem, not just a prompt change.
- **mykb relevance** — source-cited wiki content embodies honesty: claims carry provenance, and synthesis notes flag open questions rather than papering over them.

- **User-visible honesty** — honest systems make their confidence legible in the interface: caveats where evidence is thin, corrections when they are wrong, and a clear 'I don't know' instead of a confident guess.

## Related
- [[wiki/agent-systems/truthfulness-ai|Truthfulness in AI]] — the content condition
- [[wiki/agent-systems/hha-standards|HHH Standards]] — the triad honesty sits in
- [[wiki/concepts/calibration|Calibration]] — the measurable core
- [[wiki/agent-systems/lying-ai|AI Lying]] — the deliberate failure
- [[wiki/agent-systems/self-evaluation|Self-Evaluation]] — how systems assess their own honesty
- [[wiki/concepts/deceptive-alignment|Deceptive Alignment]] — the structural threat
