---
status: "growing"
type: "entity"
title: "ASK"
description: "Flask"
tags: ["entity", "acronym", "android", "api", "ast", "auth"]
timestamp: "2026-07-19T22:41:44Z"
resource: ""
---

## Ask

Flask — a lightweight Python WSGI web framework for simpler API endpoints and prototypes.

**Related topics:** android, api, auth

**Domain:** Mobile Platform › [[wiki/mobile-platform/supercategories/android-core/index|Android Core]] › [[wiki/web-platforms/supercategories/api-services/categories/api-rest/index|Api Clients › Ask

## Overview

Flask is a micro-framework for Python that ships a small core and lets developers add features through extensions. It is a common choice for API endpoints and prototypes because a working service needs only a few lines: a route decorator, a function, and a return value. The development server reloads on code changes, which shortens the iteration loop during prototyping.

## Core Features

- **Routing**: `@app.route` decorators map URLs to handler functions, with variable rules and HTTP method constraints.
- **Requests and responses**: request objects expose JSON bodies, headers, and query parameters; responses can be dicts or JSON strings.
- **Templating**: Jinja2 renders HTML pages and email templates server-side.
- **Extensions**: Flask-SQLAlchemy, Flask-Login, and Flask-Migrate add ORM, auth, and migrations without changing the core.

## API Prototyping Patterns

- Organize endpoints into blueprints to keep routes modular.
- Use an application factory so test fixtures and configurations can create isolated app instances.
- Register global error handlers that return consistent JSON error shapes.

## Request Lifecycle

A Flask request travels from the WSGI server through the app object to a view function, with a request context that makes headers, body, and query parameters available. The view returns a response, or the framework renders one from a template. Production deployments typically run Flask behind gunicorn or uWSGI, which handle concurrency and socket management, with a reverse proxy terminating TLS and serving static assets.

## When to Reach for Flask

Flask suits small services, internal tools, and prototypes where a few routes and a database handle the job. It is also a common teaching framework because the core is small enough to read entirely. When an application needs heavy async I/O, websockets at scale, or automatic OpenAPI generation, an ASGI framework such as FastAPI or Quart is often a better fit; Flask remains a dependable baseline for request-response APIs.

## Related Concepts

- [[wiki/api-protocols/rest-apis|REST APIs]] — the interface Flask services expose
- [[wiki/api-services/categories/api-rest/subcategories/rest-http/flask|Flask]] — companion entity page
- [[wiki/api-protocols/http-methods|HTTP Methods]] — the verbs routes handle
- [[wiki/api-protocols/http-status-codes|HTTP Status Codes]] — response semantics

## Related Entities

- [[wiki/web-platforms/supercategories/api-services/categories/api-rest/subcategories/rest-api/aap-2|Aap 2
- [[wiki/web-platforms/supercategories/api-services/categories/api-rest/subcategories/rest-api/aar|Aar
- [[wiki/web-platforms/supercategories/api-services/categories/api-rest/subcategories/rest-api/aarrr|Aarrr
- [[wiki/web-platforms/supercategories/api-services/categories/api-rest/subcategories/rest-api/abi|Abi
- [[wiki/web-platforms/supercategories/api-services/categories/api-rest/subcategories/rest-api/accr-2|Accr 2
- [[wiki/web-platforms/supercategories/api-services/categories/api-rest/subcategories/rest-api/ace-core|Ace Core
- [[wiki/web-platforms/supercategories/api-services/categories/api-rest/subcategories/rest-api/acid|Acid
- [[wiki/web-platforms/supercategories/api-services/categories/api-rest/subcategories/rest-api/acli|Acli
