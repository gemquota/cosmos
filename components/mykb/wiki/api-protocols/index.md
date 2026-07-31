## Overview

API protocols form the backbone of the mykb web domain. Session analysis reveals a REST-first approach that expands into WebSocket for real-time features and GraphQL for complex queries.

### REST
REST is the default API architectural style. FastAPI provides automatic OpenAPI documentation. Sessions show REST endpoints for CRUD operations on entities, concept search, and graph traversal. JSON is the universal interchange format.

### GraphQL
Appears in specific contexts where client-driven queries reduce over-fetching. The session data suggests GraphQL was explored but not adopted as a primary approach — it served specific use cases.

### WebSocket
Used for real-time features in agent tool communication. The LLM wiki daemon context suggests WebSocket bridges between agent processes and the wiki server for live updates.

### HTTP Protocol
HTTP/1.1 is the baseline. Sessions show HTTP servers (SimpleHTTPRequestHandler) embedded in agents for local tool APIs, plus production Nginx configurations.
