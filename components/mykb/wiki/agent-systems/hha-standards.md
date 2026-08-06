---
type: "concept"
title: "HHH Standards"
description: "Helpful, Honest, Harmless as assistant standards"
tags: ["hha", "standards", "alignment"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# HHH Standards

## Summary
HHH standards are Anthropic's formulation of assistant goals: be helpful, honest, and harmless. The triad operationalizes values into training data and evals, and each leg needs its own measurement because the three trade off against each other at the edges.

## Details
- **The three legs** — helpful (competently advance user goals), honest (report what is true, including uncertainty), and harmless (avoid causing harm, including refusing harmful requests).
- **Operationalization** — the triad is converted into training data (preference labels reflecting the three values), model behavior (refusals and hedged answers), and eval suites that score each leg.
- **The trade-offs** — helpfulness and harmlessness collide on refusal boundaries; honesty and helpfulness collide when the true answer is unwelcome; each boundary is a documented policy decision, not a hidden preference.
- **Measurement per leg** — each leg is scored separately because a single blended score hides which leg failed; the eval report shows the three scores independently.
- **Relationship to instruction hierarchy** — instruction hierarchy is the mechanism that makes the triad robust: higher-authority instructions constrain how the assistant applies helpfulness, honesty, and harmlessness.
- **RSIS3 relevance** — the bundle's practices mirror HHH for knowledge work: the loop is useful (helpful), its records are verifiable (honest), and its check gates bound its effects (harmless).
- **Limits** — HHH is a starting frame, not a complete alignment theory; it says what assistant behavior should look like, not how to guarantee it under pressure.

- **Policy boundary documentation** — every refusal boundary (where harmlessness overrides helpfulness) is documented with its rationale, so the boundary can be reviewed and revised like any other policy.
- **Trade-off review cadence** — the boundary cases (refusals, hedges, helpful-but-risky) are reviewed periodically against real traffic, because the distribution moves and yesterday's boundary may no longer fit.
- **Robustness** — the standards are only useful if they hold under pressure: adversarial evals probe whether helpful, honest, and harmless behavior survives attempts to break each leg.
## Related
- [[wiki/agent-systems/helpful-ai|Helpful AI]] — the leg
- [[wiki/agent-systems/honest-ai|Honest AI]] — the leg
- [[wiki/agent-systems/harmless-ai|Harmless AI]] — the leg
- [[wiki/agent-systems/instruction-hierarchy|Instruction Hierarchy]] — the substrate
- [[wiki/agent-systems/agent-evaluation|Agent Evaluation]] — measuring the legs
