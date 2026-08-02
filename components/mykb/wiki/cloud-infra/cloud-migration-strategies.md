---
type: "concept"
title: "Cloud Migration Strategies"
description: "The seven Rs of moving workloads to the cloud: rehost, replatform, refactor, and beyond"
tags: ["migration", "cloud", "strategy", "legacy"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://docs.aws.amazon.com/whitepapers/latest/aws-migration-whitepaper/6-strategies-for-migrating-applications-to-the-cloud.html", "https://cloud.google.com/architecture/migration-to-gcp-getting-started"]
---

# Cloud Migration Strategies

## Summary
Cloud migration strategies are the archetypal paths for moving workloads to the cloud — from lift-and-shift to full rewrite. Choosing the right one balances speed, cost, and long-term fit.

## Details
- The seven Rs: rehost (lift-and-shift), replatform, refactor (re-architect), repurchase, retire, retain, and relocate.
- Speed vs benefit trade-off: rehost is fastest, refactor delivers the most value but costs the most.
- A migration factory pattern — repeatable waves with templates — beats bespoke per-app projects.
- Open question: how to sequence migrations when dependencies (databases, identity) are intertwined.
- Cloud migration strategies are the six R's: rehost (lift-and-shift), replatform, repurchase, refactor, retire, and retain, each with a different effort and payoff profile.
- The strategy choice follows the workload's characteristics: legacy apps rehost first, custom apps refactor to cloud-native patterns over time.
- Migration is a portfolio decision, not a per-app decision — the roadmap sequences workloads by dependency, risk, and business value.
- Every migration needs rollback and cutover planning, because the costliest failure mode is getting stranded mid-migration.
- **Worked example / comparison** — Worked example — a wiki's batch jobs are replatformed to managed runtimes while its database moves through a rehost-then-refactor path, sequenced to avoid a big-bang cutover.
- For mykb, migration strategies are documented as the roadmap framework for moving workloads, paired with the finops lens.

## Related
- [[wiki/cloud-infra/lift-and-shift|Lift-and-Shift]]
- [[wiki/cloud-infra/re-platforming|Re-platforming]]
- [[wiki/cloud-infra/multi-cloud-strategy|Multi-Cloud Strategy]]
- [[wiki/concepts/promotion-readiness|Promotion Readiness]]
- [[wiki/ai-ml/article-health-scores|Article Health Scores]]
- [[wiki/concepts/decision-guides|Decision Guides]]
