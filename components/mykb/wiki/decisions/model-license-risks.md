---
type: "concept"
title: "Model License Risks"
description: "Legal risks from model licensing terms"
tags: ["licenses", "risk", "models"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Model License Risks

## Summary
Model license risks arise when models, data, or outputs are used in ways their licenses forbid. Common traps: research-only licenses in production, copyleft training data, and unclear output ownership — so license compliance requires inventorying every model and dataset in the pipeline.

## Details
- Mechanism: each model carries terms that constrain use (commercial use, fine-tuning, redistribution, output rights); data terms constrain training; the risk is using something beyond its terms; an inventory of models, datasets, and their licenses, checked at ingestion and deployment, is the practical control.
- Concrete example: a team prototypes with a research-only model and moves it to production without review; a copyleft-trained model creates obligations the team does not realize; a provider's terms claim ownership of outputs, conflicting with a customer's needs; the inventory flags each before use.
- Failure modes: license changes between model versions; fine-tuning models whose terms prohibit derivatives; output ownership ambiguity biting downstream customers; terms read once and forgotten; shadow usage (a team downloads a model outside the inventory).
- Tradeoffs: permissive models (open weights) reduce risk at the cost of capability or support; restrictive models maximize capability choice and risk; the mature pattern is a license inventory, deployment gates, and legal review for high-risk terms.
- Operational notes: inventory at ingestion, gate deployments, and re-check on version upgrades.
- RSIS3 relevance: the bundle's tooling choices carry license obligations — the same inventory-and-gate discipline for its models.

- Re-check licenses on every model version upgrade, since terms can change between releases.
- Watch for shadow usage outside the inventory, and make the inventory a deployment prerequisite.
## Related
- [[wiki/decisions/license-compliance-ai|License Compliance for AI]] — the practice
- [[wiki/decisions/data-license-issues|Data License Issues]] — the data side
- [[wiki/decisions/ip-and-ai|Intellectual Property and AI]] — the IP frame
- [[wiki/decisions/model-licensing|Model Licensing]] — the decision
- [[wiki/concepts/responsible-scaling|Responsible Scaling]] — the full treatment of this theme
- [[wiki/infrastructure/data-license-and-usage|Data License And Usage]] — existing graph context
