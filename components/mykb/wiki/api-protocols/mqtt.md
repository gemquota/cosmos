---
type: "concept"
title: "MQTT"
description: "Publish/subscribe protocol and QoS levels"
tags: ["mqtt", "pubsub", "iot", "messaging", "protocols"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://mqtt.org/", "https://docs.oasis-open.org/mqtt/mqtt/v5.0/os/mqtt-v5.0-os.html"]
---

# MQTT

## Summary
MQTT is a lightweight publish/subscribe protocol built for constrained networks: clients connect to a broker, publish to topics, and subscribe with wildcard patterns. Its three QoS levels and persistent sessions give IoT and mobile workloads delivery control that raw TCP or HTTP polling cannot.

## Details
- Model: a broker (Mosquitto, EMQX, HiveMQ) routes messages between publishers and subscribers; topics are UTF-8 strings like sensors/room1/temp with + and # wildcards.
- QoS 0 (at most once): fire and forget — fastest, loss allowed; QoS 1 (at least once): broker acknowledges, duplicates possible; QoS 2 (exactly once): four-way handshake, no duplicates.
- Sessions: a persistent session stores subscriptions and queued messages while the client is offline; clean sessions discard everything on disconnect.
- Will messages: a client registers a last-will topic+payload that the broker publishes if it disconnects abnormally — the standard presence mechanism.
- Retained messages: the broker stores the last message per topic and delivers it to new subscribers, giving late joiners the current state.
- MQTT 5.0 additions: reason codes, message expiry, topic aliases, user properties, and request/response correlation.
- Security: brokers support TLS, client certificates, and username/password ACLs; topic access control is the authorization model.

## Related
- [[wiki/api-protocols/event-driven-apis|Event-Driven APIs]] — MQTT is a canonical event transport
- [[wiki/api-protocols/at-least-once-delivery|At-Least-Once Delivery]] — QoS 1 maps to at-least-once semantics
- [[wiki/api-protocols/backpressure|Backpressure]] — QoS and session queues shape flow control
- [[wiki/devops-infra/message-broker-patterns|Message Broker Patterns]] — broker routing vs direct connections
- [[wiki/api-protocols/websocket-broadcast|WebSocket Broadcast]] — topic fan-out in the browser world
