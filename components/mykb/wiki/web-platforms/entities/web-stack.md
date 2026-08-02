---
type: "entity"
title: "Web Technology Stack"
tags: ["web", "http", "frontend", "backend", "fullstack"]
source: ["sessions/"]
status: "growing"
---

# Web Technology Stack

Web technologies used across the ecosystem.

## Backend
- **FastAPI** — Primary API framework (RSIS3 dashboard, WW bridge)
- **Uvicorn** — ASGI server
- **Jinja2** — HTML templating
- **SQLite** — Database

## Frontend
- **React 19** + TypeScript
- **Vite** — Build tool
- **Chart.js** — Dashboards
- **Tailwind CSS** — Styling
- **Zustand** — State management

## API Patterns
- **REST** + JSON primary
- **WebSocket** for real-time
- **OpenAPI** auto-docs from FastAPI

## Stack Rationale

The stack is deliberately small and coherent. FastAPI provides typed request handling and generates OpenAPI documentation from Python type hints, so the API contract stays in sync with the code. Uvicorn serves the ASGI application with async support, and Jinja2 renders server-side HTML where a full SPA is overkill. SQLite stores structured state without requiring a database server, which fits single-machine deployments and the embedded tooling this ecosystem produces.

## Frontend Choices

React 19 with TypeScript gives the dashboards a typed component model, while Vite keeps the build fast and the dev server instant. Chart.js covers the telemetry charts the dashboards need, Tailwind CSS provides utility-first styling without a heavyweight design system, and Zustand offers minimal global state. The pairing of a Python backend with a TypeScript frontend is the consistent pattern across the ecosystem's UIs, from the RSIS3 dashboard to the wiki viewer. This same division appears in the component repositories that make up the ecosystem, where a Python core serves data and a self-contained web UI renders it.

## Operational Patterns

Deployments follow the API patterns above: REST with JSON for most interactions, WebSockets for live telemetry, and OpenAPI for discoverability. [[wiki/api-protocols/index|API Protocols]] documents the transport conventions, [[wiki/data-storage/entities/database-schema-audit|database schema audit]] covers keeping the SQLite schema consistent, and [[wiki/devops-infra/observability|observability]] records how the running stack is monitored. The [[wiki/devops-infra/index|DevOps Infrastructure]] tree holds the deployment and container material for shipping this stack.

See also: [[wiki/web-platforms/index|Web Platforms]], [[wiki/frontend/index|Frontend]], [[wiki/api-services/index|API Services]]
