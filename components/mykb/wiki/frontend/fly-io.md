---
type: "concept"
title: "Fly.io"
description: "Platform running containers close to users across global regions with wireguard private networking"
tags: ["fly-io", "hosting", "containers", "edge", "deploy"]
timestamp: "2026-07-31T00:00:00Z"
status: "stub"
---

# Fly.io

## Summary
Fly.io deploys containers to global regions with per-region scaling, private WireGuard networking, and proximity routing. Apps run as normal containers with optional edge behavior.

## Details
- `fly launch` / `fly deploy` push Dockerfile apps; machines scale per region.
- Well suited to stateful apps (SQLite, Postgres with Litestream) that Vercel-style platforms don't run.
- A pragmatic middle path between plain containers and serverless platforms.

## Related
- [[wiki/frontend/serverless|Serverless]] — scale-to-zero comparison
- [[wiki/devops-infra/sqlite|SQLite]] — Litestream-backed state
- [[wiki/devops-infra/docker-compose|Docker Compose]] — container app shape
- [[wiki/frontend/vercel|Vercel]] — static/serverless alternative
- [[wiki/api-protocols/websockets|WebSockets]] — region-pinned connections
