---
type: "concept"
title: "Intellectual Property and AI"
description: "The full IP landscape for AI systems"
tags: ["ip", "ai", "legal"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Intellectual Property and AI

## Summary
IP and AI covers patents, copyright, trade secrets, and database rights across models, data, and outputs. Uncertainty is high — courts and regulators are still mapping AI onto old IP categories — so prudent practice documents ownership and license terms explicitly.

## Details
- Mechanism: the four IP pillars apply differently to AI: copyright covers training data and outputs; patents cover model innovations and methods; trade secrets protect weights and proprietary pipelines; database rights cover curated collections; each needs documented ownership, license terms, and usage policies.
- Concrete example: a lab patents a novel training method, keeps its data pipeline as a trade secret, licenses its model under terms that restrict redistribution, and documents the copyright status of outputs; a counterpart that documents nothing discovers its pipeline was exposed by a contractor.
- Failure modes: assuming ownership where contracts are silent; trade-secret leakage through logs, support, or contractors; patent disclosures that forfeit secrecy; database rights ignored for curated corpora; jurisdictions disagreeing on AI inventorship and authorship.
- Tradeoffs: aggressive IP protection (patents, secrecy) protects value at the cost of openness and disclosure; the alternative, open licensing, trades protection for community and adoption; the mature pattern is explicit IP mapping per asset class with documented decisions.
- Operational notes: keep an IP register, document ownership per asset, and review contracts for AI clauses. Review the register on acquisition, contractor changes, and model releases, since each event shifts what is owned.
- RSIS3 relevance: the bundle's provenance and licensing notes are IP hygiene — the same documentation discipline applied to its artifacts.

## Practice
- Document the IP posture per asset so ownership questions never depend on memory or a single person.
## Related
- [[wiki/decisions/copyright-and-ai|Copyright and AI]] — the copyright slice
- [[wiki/decisions/patent-issues-ai|Patent Issues for AI]] — the patent slice
- [[wiki/decisions/trade-secrets-ai|Trade Secrets in AI]] — the secrecy slice
- [[wiki/decisions/model-licensing|Model Licensing]] — the contract layer
- [[wiki/syntheses/knowledge-synthesis-pipelines|Knowledge Synthesis Pipelines]]
- [[wiki/infrastructure/data-license-and-usage|Data License And Usage]]
