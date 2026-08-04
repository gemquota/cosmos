---
type: "decision"
title: "License Compliance for AI"
description: "Practices for honoring AI software and data licenses"
tags: ["license", "compliance", "practice"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# License Compliance for AI

## Summary
License compliance for AI tracks the terms attached to models, code, and data and ensures usage stays within them. It requires inventory, review, and automation — license scanners for code, provenance records for data, and policy checks before deployment.

## Details
- Mechanism: an inventory records every dependency, model, and dataset with its license; scanners (license-checker, FOSSA-style tools) flag violations automatically in CI; review resolves ambiguous terms; deployment gates enforce the policy — a research-only model cannot enter production.
- Concrete example: CI fails a build when a new dependency carries an incompatible license; a dataset with a no-commercial term is excluded from the training pipeline; a model with a source-available license is reviewed before commercial use; the inventory is audited quarterly.
- Failure modes: inventory drift — new dependencies added without review; scanners that misclassify licenses or miss transitive dependencies; ambiguous terms resolved by guesswork; compliance checked once at onboarding and never again; generated content whose license status is unclear.
- Tradeoffs: compliance processes cost review time and may block convenient dependencies; the alternative, ignoring terms, carries legal and reputational risk; the mature pattern is automated scanning plus human review for the ambiguous 5%.
- Operational notes: automate scanning in CI, keep the inventory current, and document decisions for ambiguous licenses. Scan generated code and bundled assets too, since they carry their own obligations.
- RSIS3 relevance: the bundle's dependencies and generated content should be license-audited — the same inventory-and-gate discipline applied to its stack.

## Practice
- Gate the pipeline on the inventory: an unlisted dependency or dataset should fail the build, not sail through.
- Escalate ambiguous terms to a documented decision rather than guessing, so the interpretation is repeatable.
## Related
- [[wiki/decisions/model-license-risks|Model License Risks]] — the risk side
- [[wiki/decisions/data-license-issues|Data License Issues]] — the data terms
- [[wiki/concepts/open-source-ai|Open Source AI]] — the open side
- [[wiki/concepts/attribution-ai|Attribution for AI]] — the credit side
- [[wiki/concepts/responsible-scaling|Responsible Scaling]]
- [[wiki/infrastructure/data-license-and-usage|Data License And Usage]]
