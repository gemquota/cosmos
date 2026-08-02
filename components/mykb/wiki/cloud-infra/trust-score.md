---
type: "concept"
title: "Trust Score"
description: "The composite rating of how much a source or article should be trusted"
tags: ["score", "trust", "metrics", "quality"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Trust Score

## Summary
The trust score aggregates the trust signals — domain, publisher, author, verification history — into one rating used at citation time.

## Details
- Trust is contextual: the score is per-source-plus-claim, not a global label on a domain.
- Trust scores decay and must be re-evaluated on source-review schedules; a good score is not permanent.
- For mykb, the trust score gates which sources pass source-vetting for promotion.

## Related
- [[wiki/ai-ml/score-components|Score Components]]
- [[wiki/cloud-infra/trust-score|Trust Score]]
- [[wiki/cloud-infra/reputation-score|Reputation Score]]
- [[wiki/cloud-infra/source-vetting|Source Vetting]]
- [[wiki/cloud-infra/domain-trust|Domain Trust]]
- [[wiki/concepts/verifiability-score|Verifiability Score]]
