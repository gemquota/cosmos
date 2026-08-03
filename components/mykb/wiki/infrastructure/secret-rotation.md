---
type: "concept"
title: "Secret Rotation"
description: "Replacing credentials on a schedule so leaked or compromised secrets have a short useful life"
tags: ["secrets", "rotation", "security", "automation"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
---

# Secret Rotation

## Summary
Secret rotation periodically replaces credentials — API keys, passwords, certificates — so that leaked or compromised secrets have a short useful life and old credentials cannot be replayed forever. It is a defense-in-depth control: even a fully exfiltrated credential becomes worthless once its successor is live.

## Details
- Rotation cadence should match risk: high-value, widely distributed secrets rotate more often, while low-risk internal tokens can follow a slower schedule. Compliance regimes (PCI DSS, SOC 2) often mandate minimum frequencies that become the floor.
- Dual-lifetime schemes keep old and new values valid during the transition so services can pick up the new secret without a coordinated outage. The standard pattern is to add the new value, propagate it everywhere, cut over, then revoke the old value after a grace period.
- Central stores (HashiCorp Vault, cloud secret managers) with leases automate rotation and distribution: applications fetch short-lived credentials and renew them, shrinking the window in which a stolen secret works.
- Concrete examples: TLS certificate rotation through ACME/Let's Encrypt, database password rotation with two-password acceptance windows in Postgres and MySQL, and cloud IAM key rotation where the old key is disabled only after the new one is confirmed working.
- Failure modes: rotation during an outage makes diagnosis harder; split-brain or partially updated fleets can leave some instances authenticating with revoked secrets; third-party integrations that do not support dual keys force disruptive windows; and a failed rotation that revokes too early can lock out the entire platform.
- Tradeoffs: automated rotation reduces human error but adds moving parts — renewal daemons, caching layers that hold stale values, and clock skew affecting JWT and certificate validity. Weigh cadence against operational cost and blast radius.
- RSIS3/mykb relevance: secret lifecycle is a standing operational constraint for any loop that provisions or persists credentials; this node supplies the rotation ordering rules that keep retrievals from treating rotation as a single "just replace it" step.

## Related
- [[wiki/infrastructure/configuration-management|Configuration Management]] — distributing rotated secrets
- [[wiki/security/secrets-management|Secrets Management]] — the storage layer rotation builds on
- [[wiki/security/zero-trust|Zero Trust Architecture]] — short-lived credentials principle
- [[wiki/security/rbac|RBAC]] — permissions for rotation automation
