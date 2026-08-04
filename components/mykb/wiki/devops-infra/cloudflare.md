---
type: "entity"
title: "Cloudflare"
description: "CDN, DNS, edge-compute, and security platform sitting in front of web properties"
tags: ["cloudflare", "cdn", "dns", "edge", "security"]
timestamp: "2026-07-31T00:00:00Z"
status: "stub"
---

# Cloudflare

## Summary
Cloudflare operates a global CDN plus DNS, WAF, DDoS protection, and edge compute (Workers). It fronts a large share of the web, including many static and API deployments.

## Details
- Free tier covers DNS, CDN caching, TLS, and bot protection; Workers adds edge functions.
- The `gemquota.github.io` hub could sit behind Cloudflare for caching and analytics.
- Terraform providers manage zones, rules, and Workers as code.

## Related
- [[wiki/frontend/edge-functions|Edge Functions]] — Cloudflare Workers platform
- [[wiki/frontend/static-site-generation|Static Site Generation]] — CDN-served output
- [[wiki/devops-infra/terraform|Terraform]] — DNS/CDN as code
- [[wiki/api-protocols/http-caching|HTTP Caching]] — edge cache control
- [[wiki/security/zero-trust|Zero Trust Architecture]] — Cloudflare Access
