---
type: "concept"
title: "Netlify"
description: "All-in-one web hosting platform with git-based builds, forms, functions, and CDN"
tags: ["netlify", "hosting", "frontend", "jamstack", "cd"]
timestamp: "2026-07-31T00:00:00Z"
status: "stub"
---

# Netlify

## Summary
Netlify builds and hosts static sites from Git with continuous deployment, preview deploys, and add-ons like forms, identity, and functions. It was an early driver of the JAMstack movement.

## Details
- Build pipeline runs any SSG; atomic deploys keep the site consistent.
- Netlify Functions add serverless logic; redirects/headers configurable in `netlify.toml`.
- Comparable to Vercel; often chosen for Astro/Eleventy/Gatsby sites.

## Related
- [[wiki/frontend/static-site-generation|Static Site Generation]] — the hosted artifact
- [[wiki/frontend/vercel|Vercel]] — main competitor
- [[wiki/frontend/serverless|Serverless]] — Netlify Functions
- [[wiki/devops-infra/github-actions|GitHub Actions]] — alternative CI/CD
- [[wiki/api-protocols/http-caching|HTTP Caching]] — CDN headers
