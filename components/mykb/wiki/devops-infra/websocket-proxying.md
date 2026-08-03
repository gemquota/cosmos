---
type: "concept"
title: "WebSocket Proxying"
description: "Upgrading and long-lived connection handling behind proxies"
tags: ["websocket", "proxy", "upgrade", "networking"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# WebSocket Proxying

## Summary
WebSocket proxying lets a reverse proxy terminate or forward the WebSocket upgrade (HTTP/1.1 Upgrade plus the long-lived, bidirectional stream) to backend servers. Proxies must handle the upgrade handshake, connection timeout differences, and load balancing of long-lived connections — the patterns differ from ordinary HTTP.

## Details
- Mechanism: the client sends an HTTP GET with Upgrade: websocket and Connection: Upgrade; the proxy either forwards the upgrade to a backend (tunneling, with nginx/Envoy/Traefik support) or terminates and re-originates the connection; after the handshake, the connection is a raw bidirectional stream, so proxy timeouts, buffering, and retries must be adapted or disabled.
- Concrete example: an nginx config with proxy_set_header Upgrade and Connection set to upstream, long read/write timeouts, and HTTP/1.1 for upstream; Envoy with an upstream cluster configured for TCP or WebSocket; a chat or live-telemetry dashboard behind a gateway that must keep idle connections alive through proxy idle timeouts.
- Failure modes: proxy timeouts killing idle connections (configure large proxy_read_timeout or use ping frames); buffering interference — proxies that buffer or compress WebSocket frames break the protocol (disable gzip on upgrades); load balancers without sticky sessions routing reconnects to a different backend that lacks session state; upgrade headers stripped by misconfigured middleware; IPv4/IPv6 or SNI issues on the proxy.
- Tradeoffs: proxying WebSockets centralizes TLS, auth, and routing but adds a hop whose timeouts and buffers can break the stream; direct connections are simpler and more reliable but lose the gateway's policies; the mature pattern is proxy-terminated TLS with WebSocket-aware config (upgrade headers, long timeouts, ping support).
- Operational notes: test idle and reconnect behavior, monitor connection counts and upgrade success rates, and size proxy connection limits for long-lived streams.
- RSIS3 relevance: the dashboard's live views (if they stream telemetry over WebSockets) depend on proxy WebSocket support — the failure modes above are exactly what RSIS3's monitoring should watch.

## Related
- [[wiki/devops-infra/mirroring-and-proxying-registries|Mirroring & Proxying Registries]] — related coverage in the same cluster
- [[wiki/devops-infra/kubernetes-control-plane|Kubernetes Control Plane]] — related coverage in the same cluster
- [[wiki/devops-infra/observability-pillars|Observability Pillars]] — related coverage in the same cluster
- [[wiki/syntheses/knowledge-acquisition-workflow|Knowledge Acquisition Workflow]] — how stubs grow into full articles in mykb
- [[wiki/syntheses/mykb-acquisition-curation-and-practices|Acquisition, Curation & Practices]] — the curation loop this stub belongs to
