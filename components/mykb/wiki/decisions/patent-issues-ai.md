---
type: "concept"
title: "Patent Issues for AI"
description: "How patents apply to AI inventions"
tags: ["patents", "ai", "legal"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Patent Issues for AI

## Summary
Patent issues for AI include patentability of model innovations, infringement by trained systems, and disclosure tensions with secrecy. AI-generated inventions complicate inventorship rules, and labs manage the landscape with portfolio and freedom-to-operate analyses.

## Details
- Mechanism: patentability asks whether a model innovation is novel and non-obvious (and whether AI-aided invention meets inventorship rules); infringement asks whether a trained system or its use practices a patented method; disclosure tensions — patents require publication while trade secrets require secrecy — force a per-invention choice.
- Concrete example: a lab patents a novel retrieval method and keeps its fine-tuning pipeline secret; a competitor's model is accused of practicing the patent; a freedom-to-operate search finds blocking patents before launch; an AI-generated invention faces inventorship rejection in some jurisdictions.
- Failure modes: patenting what should stay secret (or vice versa); infringing without a freedom-to-operate check; inventorship disputes over AI contributions; portfolios that cover the wrong things; jurisdiction differences in AI patentability.
- Tradeoffs: patents protect inventions at the cost of disclosure and cost; trade secrets preserve secrecy at the cost of no protection against independent discovery; the mature pattern is a deliberate per-invention choice, informed by freedom-to-operate analysis.
- Operational notes: track the patent landscape, document disclosure decisions, and review jurisdiction changes.
- RSIS3 relevance: the bundle's novel scripts and methods have patent-adjacent disclosure choices — the same deliberate decision documented in its provenance.

- Do a freedom-to-operate check before shipping anything patentable, and document the decision.
- Coordinate with the secrecy decision per invention, since a public disclosure can forfeit patent rights.
## Related
- [[wiki/decisions/ip-and-ai|Intellectual Property and AI]] — the frame
- [[wiki/decisions/trade-secrets-ai|Trade Secrets in AI]] — the secrecy alternative
- [[wiki/concepts/open-source-ai|Open Source AI]] — the disclosure alternative
- [[wiki/concepts/disclosure-ai|AI Disclosure]] — the transparency angle
- [[wiki/syntheses/knowledge-synthesis-pipelines|Knowledge Synthesis Pipelines]] — the full treatment of this theme
- [[wiki/infrastructure/data-license-and-usage|Data License And Usage]] — existing graph context
