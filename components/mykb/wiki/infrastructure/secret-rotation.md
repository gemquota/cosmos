---
type: "concept"
title: "Secret Rotation"
description: "Replacing credentials on a schedule so leaked or compromised secrets have a short useful life"
tags: ["secrets", "rotation", "security", "automation"]
timestamp: "2026-08-01T00:00:00Z"
status: "stub"
---

# Secret Rotation

## Summary
Secret rotation periodically replaces credentials — API keys, passwords, certificates — so exposure windows stay short and old secrets cannot be reused forever.

## Details
- Rotation cadence should match risk: high-value, widely-distributed secrets rotate more often.
- Dual-lifetime schemes (valid old + new during transition) keep services running through the swap.
- Central stores (Vault, cloud secret managers) with leases automate rotation and distribution.
- Open question: how to rotate secrets across third-party integrations that do not support dual keys.

## Related
- [[wiki/infrastructure/configuration-management|Configuration Management]] — distributing rotated secrets
- [[wiki/security/secrets-management|Secrets Management]] — the storage layer rotation builds on
- [[wiki/security/zero-trust|Zero Trust Architecture]] — short-lived credentials principle
- [[wiki/security/rbac|RBAC]] — permissions for rotation automation
