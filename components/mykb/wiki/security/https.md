---
type: "concept"
title: "HTTPS"
description: "HTTP over TLS: encrypting web traffic end to end and authenticating servers"
tags: ["https", "tls", "web", "security", "http"]
timestamp: "2026-07-31T00:00:00Z"
status: "stub"
---

# HTTPS

## Summary
HTTPS is HTTP layered on TLS: it encrypts requests/responses, authenticates the server via certificate, and ensures integrity. It is mandatory for modern web properties and APIs.

## Details
- Every site and API endpoint should serve HTTPS; browsers mark plain HTTP as insecure.
- Certificates come from public CAs (Let's Encrypt) or private CAs for internal services.
- HSTS and secure cookie flags harden deployments further.

## Related
- [[wiki/security/tls|TLS]] — the underlying protocol
- [[wiki/security/lets-encrypt|Let's Encrypt]] — free certificates
- [[wiki/security/certbot|Certbot]] — automated issuance
- [[wiki/devops-infra/nginx|Nginx]] — TLS termination
- [[wiki/devops-infra/caddy|Caddy]] — automatic HTTPS
- [[wiki/api-protocols/rest-apis|REST APIs]] — API security baseline
