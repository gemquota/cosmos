---
type: "decision"
title: "Copyright and AI"
description: "How copyright law interacts with AI training and outputs"
tags: ["copyright", "ai", "legal"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Copyright and AI

## Summary
Copyright and AI spans three questions: training on copyrighted works, ownership of model outputs, and derivative-works liability. Jurisdictions differ, and litigation and licensing deals are reshaping the norms as fast as the technology moves.

## Details
- Mechanism: training on copyrighted works raises fair-use and licensing questions that courts are still resolving; output ownership depends on jurisdiction and on how derivative the output is of training data; liability attaches when outputs reproduce protected expression; technical mitigations (filters, provenance) complement legal ones.
- Concrete example: a model trained on a corpus including copyrighted books; an output that closely reproduces a passage triggers a takedown; a platform adds an output filter that detects near-verbatim reproduction; a licensing deal gives one vendor clean rights while others litigate.
- Failure modes: assuming output is always original (verbatim reproduction happens); ignoring jurisdiction differences (what is fair use in one country is infringement in another); relying on filters as complete protection; unclear ownership terms in contracts; training on data whose rights were never cleared.
- Tradeoffs: respecting copyright costs licensing, filtering, and legal overhead; ignoring it risks litigation and platform takedowns; the mature pattern is documented training provenance, output filters for near-verbatim content, and clear ownership terms in contracts.
- Operational notes: keep provenance records, monitor for reproduced content, and track jurisdiction changes.
- RSIS3 relevance: the wiki's sources and reproductions should respect copyright — provenance and licensing notes are the practical hygiene.

## Practice
- Record provenance at ingestion and output, since the ability to demonstrate where content came from is the core defense.
- Keep jurisdiction in mind when distributing outputs, since the same action is legal in one country and infringing in another.
## Related
- [[wiki/decisions/ip-and-ai|Intellectual Property and AI]] — the broad frame
- [[wiki/decisions/data-license-issues|Data License Issues]] — the data side
- [[wiki/concepts/attribution-ai|Attribution for AI]] — the credit mechanism
- [[wiki/concepts/open-source-ai|Open Source AI]] — the alternative model
- [[wiki/syntheses/knowledge-synthesis-pipelines|Knowledge Synthesis Pipelines]]
- [[wiki/infrastructure/data-license-and-usage|Data License And Usage]]
