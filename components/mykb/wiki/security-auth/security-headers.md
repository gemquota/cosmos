---
type: "concept"
title: "Security Headers"
description: "HTTP response headers that harden browser-side security behavior"
tags: ["security-headers", "http", "browsers", "defense"]
timestamp: "2026-08-01T00:00:00Z"
status: "stub"
source: ["https://owasp.org/www-project-secure-headers/"]
---

# Security Headers

- Security headers steer browser defenses: Content-Security-Policy, X-Content-Type-Options, Referrer-Policy, HSTS, and frame/cross-origin controls.
- The OWASP Secure Headers Project maintains the reference list and recommended values.
- Headers are cheap, high-leverage hardening but must be validated against actual app behavior (CSP especially).
- For mykb: a single edge layer (nginx/traefik) should enforce a consistent header baseline across services.

## Related

- [[wiki/security-auth/content-security-policy|Content Security Policy]] — the most powerful header
- [[wiki/security-auth/cors-policy|CORS Policy]] — cross-origin access control
- [[wiki/security/https|HTTPS]] — HSTS requires HTTPS
- [[wiki/devops-infra/nginx|Nginx]] — edge layer for header enforcement
- [[wiki/security-auth/tls-encryption|TLS Encryption]] — headers and TLS form transport hardening
