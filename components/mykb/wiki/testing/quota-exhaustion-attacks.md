---
type: "concept"
title: "Quota Exhaustion Attacks"
description: "Deliberately consuming an account quota to deny service or force spending"
tags: ["quota-attacks", "security", "abuse", "denial"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Quota Exhaustion Attacks

## Summary
Deliberately consuming an account quota to deny service or force spending

## Details
- Attackers flood endpoints to exhaust budgets.
- Impact: availability loss or financial damage.
- Defenses: rate limiting, budgets, and anomaly alerts.
- Related to load-shedding on the serving side.

## Related
- [[wiki/agent-systems/budget-and-quota-control|Budget and Quota Control]] — enforcement
- [[wiki/ml-frameworks/rate-limit-engineering|Rate Limit Engineering]] — throttling
- [[wiki/testing/api-key-theft|API Key Theft]] — credential abuse
- [[wiki/api-protocols/load-shedding|Load Shedding]] — availability response
- [[wiki/ml-frameworks/token-accounting-and-cost|Token Accounting and Cost]] — metering
