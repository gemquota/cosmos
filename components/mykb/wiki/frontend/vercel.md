---
type: "entity"
title: "Vercel"
description: "Frontend cloud platform optimized for static and serverless Next.js-style deployments"
tags: ["vercel", "hosting", "frontend", "jamstack", "nextjs"]
timestamp: "2026-07-31T00:00:00Z"
status: "stub"
---

# Vercel

## Summary
Vercel is a frontend deployment platform built around Next.js: git-push deploys, preview URLs per branch, edge functions, and a global CDN. It popularized the modern SSG/serverless frontend workflow.

## Details
- Automatic builds from Git providers; preview deployments per pull request.
- Edge middleware, ISR, and serverless functions cover dynamic needs over static output.
- The cosmos hub pattern (static redirect to dashboard) mirrors Vercel's static hosting model.

## Related
- [[wiki/frontend/static-site-generation|Static Site Generation]] — core Vercel workflow
- [[wiki/frontend/edge-functions|Edge Functions]] — Vercel edge runtime
- [[wiki/frontend/serverless|Serverless]] — function support
- [[wiki/frontend/netlify|Netlify]] — competing platform
- [[wiki/devops-infra/github-actions|GitHub Actions]] — alternative deploy pipeline
