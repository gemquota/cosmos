---
type: "concept"
title: "Quota Exhaustion Attacks"
description: "Deliberately consuming an account quota to deny service or force spending"
timestamp: "2026-08-02T00:00:00Z"
---
tags: ["quota-attacks", "security", "abuse", "denial", "cost"]
status: "growing"

# Quota Exhaustion Attacks

## Summary
Quota exhaustion attacks deliberately consume an account's quota to deny service to legitimate users or to force financial damage. They matter because API products meter usage, and drained quotas translate directly into availability loss and cost. Defending them requires budgets, limits, and anomaly detection rather than trust in honest usage.

## Details
- **Definition** — the attacker floods endpoints or runs expensive operations until the account's quota is spent.
- **Impact** — victims lose service when quotas are exhausted, or face unexpected bills when overage is charged.
- **Attack surface** — public endpoints, trial accounts, and generous default limits are common entry points.
- **Rate limiting** — per-key and per-account limits cap how quickly a single attacker can burn quota.
- **Budgets** — hard budgets with alerts stop runaway spending before it becomes damage.
- **Anomaly detection** — usage patterns that spike beyond baselines flag likely abuse while it is still cheap to stop.
- **Load shedding** — graceful degradation under pressure keeps service for legitimate users.
- **Common failure modes** — limits set high enough to be meaningless, and alerts that arrive after the quota is gone.
- **Worked example** — an attacker scripts expensive model calls against a trial key; per-key limits cap the burn, and a usage anomaly alert freezes the account.
- **Practical relevance** — quota attacks turn metering itself into a target, so controls must assume adversarial usage.

- **Tiering** — default limits for new and trial accounts should be conservative until usage is trusted.
- **Alerting** — budget-consumption alerts with thresholds give operators time to act.
- **Forensics** — usage logs attribute burns to keys and endpoints, enabling post-incident analysis.
## Related
- [[wiki/agent-systems/budget-and-quota-control|Budget and Quota Control]] — enforcement
- [[wiki/ml-frameworks/rate-limit-engineering|Rate Limit Engineering]] — throttling
- [[wiki/testing/api-key-theft|API Key Theft]] — credential abuse
- [[wiki/api-protocols/load-shedding|Load Shedding]] — availability response
- [[wiki/ml-frameworks/token-accounting-and-cost|Token Accounting and Cost]] — metering
- [[wiki/api-protocols/429-handling|429 Handling]] — quota responses
