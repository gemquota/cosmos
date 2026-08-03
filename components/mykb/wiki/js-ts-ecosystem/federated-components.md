---
type: "concept"
title: "Federated Components"
description: "Composing UI across builds via shared module boundaries"
tags: ["module-federation", "components", "micro-frontends", "architecture"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# Federated Components

## Summary
Federated components compose UI across separately built applications through shared module boundaries: a shell app loads remote components at runtime, and shared dependencies (like React) are kept as singletons so multiple builds do not duplicate or clash. It is the component-level face of micro-frontends.

## Details
- Mechanism: with module federation, a host declares shared modules and remote entry points; remote components load on demand into the host; shared dependencies negotiate versions at runtime — if host and remote use compatible React versions, one copy is used; the shell owns layout, routing, and theming while remotes contribute views.
- Concrete example: a dashboard shell federates a charts component and a wiki-viewer component from separately built apps; both share React and the design system as singletons; a new micro-frontend is added by registering its remote entry, no rebuild of the shell needed; version negotiation picks a compatible shared React.
- Failure modes: duplicate React instances from failed sharing (two copies break hooks and context); version negotiation silently picking an incompatible build; remotes that fail to load taking down the shell without a fallback; theming and styling leaking across federation boundaries; shared state (auth, events) not designed across build boundaries.
- Tradeoffs: federation gives independent deployability and composition at the cost of runtime coupling, integrity concerns, and debugging complexity; the alternative, a single build, is simpler and safer; the mature pattern is a small number of stable remotes, explicit shared-dependency lists, and robust error boundaries.
- Operational notes: pin shared versions, test remote failures, and keep the shell's fallback paths exercised.
- RSIS3 relevance: cosmos's dashboard hosts multiple component UIs — federation is one way to compose them independently, with the shared-dependency discipline that prevents duplicate state.

## Related
- [[wiki/js-ts-ecosystem/bundlers-and-build-tools|Bundlers and Build Tools]] — related coverage in the same cluster
- [[wiki/js-ts-ecosystem/module-federation|Module Federation]] — related coverage in the same cluster
- [[wiki/js-ts-ecosystem/federated-components|Federated Components]] — related coverage in the same cluster
- [[wiki/js-ts-ecosystem/module-federation|Module Federation]] — related coverage in the same cluster
- [[wiki/web-platforms/web-frameworks|Web Frameworks]] — related coverage in the same cluster
- [[wiki/web-platforms/component-architecture|Component Architecture]] — related coverage in the same cluster
- [[wiki/web-platforms/web-components|Web Components]] — related coverage in the same cluster
