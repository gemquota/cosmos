---
type: "concept"
title: "Certbot"
description: "Automated ACME client for obtaining and renewing Let's Encrypt TLS certificates"
tags: ["certbot", "acme", "tls", "letsencrypt", "automation"]
timestamp: "2026-07-31T00:00:00Z"
status: "stub"
---

# Certbot

## Summary
Certbot is the reference ACME client: it obtains Let's Encrypt certificates and installs them into web servers, with automatic renewal via cron/systemd timers.

## Details
- Challenge types: HTTP-01 (webroot), DNS-01 (wildcards), and TLS-ALPN-01.
- `certbot renew` handles renewal; hooks reload the web server after issuance.
- An alternative is Caddy/nginx configs with built-in ACME clients.

## Related
- [[wiki/security/lets-encrypt|Let's Encrypt]] — the CA Certbot talks to
- [[wiki/security/https|HTTPS]] — certificates enable it
- [[wiki/security/tls|TLS]] — the protocol behind
- [[wiki/devops-infra/nginx|Nginx]] — common install target
- [[wiki/devops-infra/caddy|Caddy]] — automatic ACME alternative
- [[wiki/security/zero-trust|Zero Trust Architecture]] — certificates enable encrypt-everything
