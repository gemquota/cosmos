---
type: "concept"
title: "Harmless AI"
description: "Systems that avoid causing harm"
tags: ["harmless", "safety", "assistants"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Harmless AI

## Summary
Harmless AI avoids causing harm: it refuses harmful requests and avoids unintended side effects. Harmlessness is one leg of the helpful, honest, harmless triad, and it conflicts with helpfulness at the margins, which is why the trade-offs need principled resolution rather than ad-hoc judgment.

## Details
- **Scope of harm** — direct harm (refusing dangerous requests), indirect harm (unintended consequences of helpful actions), and systemic harm (eroding trust or safety norms).
- **The tension with helpfulness** — a maximally helpful assistant will help with anything; harmlessness carves out refusals, and the boundary is a policy decision with documented reasons.
- **Operationalization** — red-teaming, safety training, and content policies translate the principle into behavior; each method covers a different failure surface.
- **Measurement** — harmlessness is evaluated with refusal tests, harmful-request suites, and side-effect audits; both over-refusal (too restrictive) and under-refusal (too permissive) are measured.
- **RSIS3 relevance** — check gates make the loop harmless to the wider wiki: mutations are validated before they land, so the system cannot damage the knowledge base it runs on.
- **Failure modes** — harmlessness that is trained but not tested generalizes poorly; harmlessness without helpfulness becomes useless; and harmlessness policies that are vague become inconsistently applied.

- **Layered defenses** — harmlessness is enforced at multiple layers: policy in the prompt, guardrails at the tool boundary, and evaluation gates before deployment; any single layer can fail, so none is trusted alone.
- **Over-refusal costs** — excessive caution refuses legitimate requests, eroding usefulness and driving users to workarounds; the refusal boundary is tuned with both sides of the error measured.
- **Side-effect auditing** — beyond request refusal, harmlessness covers unintended side effects of helpful actions; deployment reviews check what the assistance actually changed in the world.
## Related
- [[wiki/agent-systems/helpful-ai|Helpful AI]] — the tension
- [[wiki/agent-systems/honest-ai|Honest AI]] — the truthfulness leg
- [[wiki/agent-systems/hha-standards|HHH Standards]] — the triad
- [[wiki/concepts/restraint-training|Restraint Training]] — the method
- [[wiki/decisions/content-policy-ai|Content Policy for AI]] — the rules
- [[wiki/concepts/conservative-ai|Conservative AI]] — the cautious extreme
