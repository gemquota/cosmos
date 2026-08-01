---
type: "concept"
title: "SSRF Prevention"
description: "Preventing server-side requests to internal or unintended targets"
tags: ["ssrf", "server-side", "defense", "network"]
timestamp: "2026-08-01T00:00:00Z"
status: "stub"
source: ["https://cheatsheetseries.owasp.org/cheatsheets/Server_Side_Request_Forgery_Prevention_Cheat_Sheet.html"]
---

# SSRF Prevention

- Server-side request forgery (SSRF) lets an attacker make the server fetch URLs of the attacker's choosing — cloud metadata, internal services, or localhost.
- Prevention: allowlist protocols and hosts, validate and canonicalize URLs, block internal IP ranges, and deny cloud metadata endpoints.
- Fetching with no redirects, explicit DNS resolution checks, and network segmentation contain the damage.
- For mykb: any URL-fetching tool (link previews, scrapers, webhooks) must implement SSRF guardrails.

## Related

- [[wiki/security-auth/xml-external-entities|XML External Entities]] — XXE can trigger SSRF
- [[wiki/security-auth/network-segmentation|Network Segmentation]] — limiting internal reachability
- [[wiki/api-protocols/webhooks|Webhooks]] — inbound URL-driven requests need validation
- [[wiki/api-services/cloud-security-posture|Cloud Security Posture]] — metadata endpoints as targets
- [[wiki/security-auth/least-privilege|Least Privilege]] — SSRF guardrails are outbound least privilege
