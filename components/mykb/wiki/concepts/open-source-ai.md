---
type: "concept"
title: "Open Source AI"
description: "AI systems released with source and weights under open licenses"
tags: ["open-source", "ai", "licenses"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Open Source AI

## Summary
Open source AI publishes source code and often weights under permissive licenses, enabling inspection and modification. The term covers a spectrum from code-only releases to fully open stacks, and the frontier debate is whether "open" is a safety asset, a safety liability, or both depending on the capability level.

## Details
- The classical open-source definition (OSI) applies to code: anyone may inspect, modify, and redistribute. AI systems complicate it because the weights are the artifact that matters — a model with open code but closed weights offers transparency into training and inference code but not into the trained system itself, which limits inspection, fine-tuning, and reproducibility. This is why the open-weights question dominates the field.
- 'Open' spans a spectrum: code-only, weights-with-restrictions, and fully open. Code-only releases give the training and inference stack but not the model. Weights-with-restrictions releases (the common "open weights" tier) provide the weights under license terms that may prohibit commercial use, redistribution, or fine-tuning — which protects the developer's business but violates the spirit of open source and can leave researchers unable to study or modify the model. Fully open releases publish weights, code, data (when feasible), and documentation under permissive terms, maximizing inspection and modification.
- The benefits are real and well-documented: transparency (auditors can inspect weights for backdoors, training-data issues, and capability surprises), decentralization (no single gatekeeper controls access to capable AI), reproducibility (independent verification of claimed results), and innovation (the ecosystem builds on open models faster than closed ones).
- Debates center on whether open release is safe at frontier scale. The safety case: openness enables the external auditing and red-teaming that closed labs may not do, and prevents a concentration of power that itself is a risk. The danger case: open weights cannot be recalled, so a frontier model in the open is permanently accessible for misuse (bioweapons, cyber offense, disinformation), no matter how dangerous it becomes or how it is used later. The empirical questions — how much misuse open models actually enable, whether red-teaming value outweighs misuse risk — are unsettled, which is why release decisions remain contested.
- RSIS3 relevance: the bundle's markdown-first, scripted wiki is an open artifact — its practices, constraints, and memory are inspectable, which is the small-scale version of the transparency argument.

## Related
- [[wiki/decisions/open-weights|Open Weights]] — the weights question
- [[wiki/concepts/open-source-safety|Open Source AI Safety]] — the safety debate
- [[wiki/concepts/open-source-governance-ai|Open Source AI Governance]] — the governance
- [[wiki/decisions/model-licensing|Model Licensing]] — the terms
- [[wiki/concepts/compute-governance|Compute Governance]]
- [[wiki/ai-ml/open-weights-models|Open Weights Models]]
