---
type: "concept"
title: "SSH Key Management"
description: "Generating, distributing, rotating, and auditing authorized keys"
tags: ["ssh", "keys", "security", "access"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# SSH Key Management

## Summary
SSH key management covers the full lifecycle of public-key authentication: generating key pairs, distributing public keys to `authorized_keys` files, rotating keys on a schedule, and auditing who can reach what. Keys are the default way humans and automation log into servers, which makes their lifecycle a security boundary rather than a one-time setup task.

## Details
- Generation: use modern algorithms with adequate key sizes — Ed25519 or RSA 3072/4096 — and protect the private key with a passphrase or, better, store it on a hardware security key or agent. Never reuse a private key across hosts or identities; one compromise should not unlock everything.
- Distribution: public keys travel to `authorized_keys` on the target; manage this with configuration management or a short-lived certificate system (SSH certificates via a CA) so that onboarding and offboarding do not require editing files by hand. Certificates also let you encode validity periods and principals.
- Rotation: revoke old keys on a schedule or on suspected compromise, regenerate pairs, and re-propagate. Track key fingerprints centrally and alert on unknown keys appearing in `authorized_keys`, which is a classic persistence signal after a breach.
- Concrete example: an attacker who plants a key in a backup admin's `authorized_keys` gains silent re-entry; without a central inventory and fingerprint baselining, the planted key can survive for months.
- Failure modes: passphraseless keys on laptops and CI runners, keys with no expiry in cloud metadata, over-broad `authorized_keys` propagation to every host, and orphaned keys left behind by departed staff or decommissioned automation.
- Tradeoffs: per-user static keys are simple but spread trust broadly; SSH certificates centralize trust in a CA but add infrastructure and a new compromise target; hardware-backed keys resist theft but complicate headless automation.
- RSIS3/mykb relevance: self-improvement loops that provision agents need this lifecycle so that ephemeral automation does not accumulate permanent credentials; this node supplies the rotation and audit rules retrievals should attach to any key.

## Related
- [[wiki/os-shell/logical-volume-management|Logical Volume Management]]
- [[wiki/devops-infra/helm-and-chart-management|Helm & Chart Management]]
- [[wiki/infrastructure/ssh-tunneling-and-port-forwarding|SSH Tunneling & Port Forwarding]]
- [[wiki/infrastructure/security-information-and-event-management|SIEM]]
- [[wiki/syntheses/knowledge-acquisition-workflow|Knowledge Acquisition Workflow]] — how stubs grow into full articles in mykb
- [[wiki/syntheses/mykb-acquisition-curation-and-practices|Acquisition, Curation & Practices]] — the curation loop this stub belongs to
