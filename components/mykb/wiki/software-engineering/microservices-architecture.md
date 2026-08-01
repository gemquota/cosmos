---
type: "concept"
title: "Microservices Architecture"
description: "Architectural style that structures an application as a set of small, independently deployable services"
tags: ["architecture", "microservices", "distributed-systems", "scalability"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://martinfowler.com/articles/microservices.html"]
---

# Microservices Architecture

## Summary
Microservices architecture decomposes an application into small services that run their own processes and communicate over a network, each owned by a small team and deployable independently. It is an alternative to the monolithic style, favouring organisational alignment, independent scaling, and technology heterogeneity at the cost of distributed-systems complexity.

## Details
- Independent deployability is the defining property: a service can be released without redeploying its neighbours, which shrinks blast radius and accelerates delivery.
- Services own their data: each service exposes behaviour through a defined API and no other service reads its database directly, which keeps coupling low.
- Communication is typically synchronous HTTP/REST or asynchronous messaging; event-driven collaboration decouples producers and consumers.
- Operational cost rises sharply: teams need service discovery, observability, retries, circuit breakers, and consistent deployment tooling.
- Bounded contexts from domain-driven design are the natural service boundaries; drawing the line badly creates distributed monoliths.
- RSIS3 relevance: mykb's agent subsystems are themselves small services behind the triad architecture, so microservice discipline maps directly onto the memory bridge.
- Worked example: an e-commerce app split into catalog, cart, payment, and inventory services, each with its own schema and CI/CD pipeline.

## Related
- [[wiki/software-engineering/event-driven-architecture|Event-Driven Architecture]] — the dominant collaboration style between microservices
- [[wiki/software-engineering/modular-monoliths|Modular Monoliths]] — the lighter-weight alternative for teams that want modularity without distribution
- [[wiki/software-engineering/service-discovery|Service Discovery]] — how services locate each other's network endpoints at runtime
- [[wiki/api-protocols/rest-apis|REST APIs]] — the common synchronous contract between services
- [[wiki/api-protocols/circuit-breaker|Circuit Breaker]] — failure-handling pattern that prevents cascading outages between services
- [[wiki/devops-infra/observability|Observability]] — the monitoring practice microservices depend on
- [[wiki/devops-infra/kubernetes|Kubernetes]] — the typical platform for deploying and scaling services
