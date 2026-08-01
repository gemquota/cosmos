---
type: "concept"
title: "Let's Encrypt"
description: "Free, automated, nonprofit certificate authority providing 90-day TLS certificates via ACME"
tags: ["letsencrypt", "tls", "certificates", "acme", "security"]
timestamp: "2026-07-31T00:00:00Z"
status: "stub"
---

# Let's Encrypt

## Summary
Let's Encrypt is a free, automated CA run by the Internet Security Research Group. It issues 90-day certificates via the ACME protocol, making HTTPS universal.

## Details
- Short lifetimes force automation; manual renewal is the main operational mistake.
- Clients: Certbot, Caddy, Traefik, and many hosting platforms integrate ACME natively.
- Rate limits apply per domain; wildcard certs need DNS-01 challenges.

## Related
- [[wiki/security/certbot|Certbot]] — the canonical client
- [[wiki/security/https|HTTPS]] — what certificates enable
- [[wiki/security/tls|TLS]] — protocol context
- [[wiki/devops-infra/traefik|Traefik]] — automatic issuance
- [[wiki/devops-infra/caddy|Caddy]] — zero-config HTTPS
- [[wiki/frontend/static-site-generation|Static Site Generation]] — every hosted static site needs TLS
