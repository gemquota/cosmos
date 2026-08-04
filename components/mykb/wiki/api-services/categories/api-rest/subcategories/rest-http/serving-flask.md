---
type: "concept"
title: "Serving Flask"
description: "Running Flask applications in production behind a WSGI server"
tags: ["entity", "flask", "wsgi", "deployment", "backend"]
timestamp: "2026-07-19T22:41:41Z"
resource: ""
---

# Serving Flask

## Summary

Serving Flask means running a Flask application in production, typically behind a WSGI server and reverse proxy rather than the built-in development server. It matters because Flask's dev server is single-process and unsuitable for real traffic, while deployment choices control concurrency, reliability, and security. The pattern generalizes to any WSGI framework.

## Details

- **Definition** — Flask is a micro web framework; serving it production-grade requires a WSGI server such as gunicorn or uWSGI to run the application.
- **WSGI contract** — WSGI defines how servers invoke Python web applications; anything WSGI-compliant runs Flask, enabling interchangeable servers and middleware.
- **Development vs production** — Flask's built-in server enables reloading and debugging but lacks production hardening; it should not be exposed to real clients.
- **Workers and threads** — Gunicorn's worker models — sync, threaded, gevent — trade throughput for isolation; CPU-bound work benefits from multiple processes.
- **Reverse proxy** — Nginx or similar fronts the WSGI server for TLS termination, static files, and connection management.
- **Worked example** — A Flask API runs under gunicorn with three workers behind nginx; the proxy terminates TLS, serves static assets, and forwards API traffic.
- **Common failure modes** — Running the dev server in production, worker timeouts on slow requests, and missing gunicorn configuration under load are classic issues.
- **Practical relevance** — Container deployments add health checks and graceful shutdown, which WSGI servers expose via signals and readiness endpoints.
- **Telemetry note** — The stub pairs Serving Flask with API and backend tags, exactly the context where WSGI deployment decisions arise.
- **Graceful shutdown** — SIGTERM handling drains in-flight requests before exit, which orchestration systems rely on for zero-downtime rollouts.
- **Configuration** — Worker counts, timeouts, and preload settings should be tuned to the workload and validated under load, not copied from defaults.
- **Worked example** — A containerized Flask app starts gunicorn with three workers, liveness probes hit a health route, and readiness waits for the database connection pool.

## Related

- [[wiki/api-services/categories/api-rest/subcategories/rest-http/flask|Flask]] — the framework itself
- [[wiki/api-protocols/rest-api-design|REST API Design]] — shaping the served endpoints
- [[wiki/os-shell/daemon-processes|Daemon Processes]] — long-running serving processes
- [[wiki/testing/api-testing|API Testing]] — exercising the deployed app
- [[wiki/dev-tools/debug-logging|Debug Logging]] — observing served requests
- [[wiki/cloud-infra/timeouts-and-deadlines|Timeouts and Deadlines]] — worker request budgets
