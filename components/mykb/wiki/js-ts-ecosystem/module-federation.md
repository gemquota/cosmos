---
type: "concept"
title: "Module Federation"
description: "Sharing code across separately built applications at runtime"
tags: ["module-federation", "bundlers", "micro-frontends", "architecture"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# Module Federation

## Summary
Module Federation shares code across separately built applications at runtime: a remote exposes modules, a host consumes them, and shared dependencies negotiate versions on load. It enables micro-frontends and plugin architectures where teams deploy independently yet compose at runtime.

## Details
- Mechanism: each build declares exposes (what it shares) and remotes (what it consumes); at runtime, remote containers are fetched and their modules loaded on demand; shared modules (React, utilities) are deduplicated through version negotiation — compatible versions resolve to one copy; the host orchestrates the graph.
- Concrete example: app A exposes a header component and shares React; app B (the shell) consumes the remote and renders it; app A deploys independently — the shell picks up the new build without redeploying; a plugin registry lists remotes at runtime.
- Failure modes: shared-dependency mismatches duplicating React (breaking hooks); remote entry failures cascading into the shell (error boundaries required); version negotiation picking incompatible builds silently; integrity and security — remote code runs with host privileges; debugging across build boundaries.
- Tradeoffs: federation trades deployment independence and runtime composition for coupling, integrity risk, and complexity; the alternative, a single build, is simpler and safer; the mature pattern is few stable remotes, explicit sharing, and robust failure handling.
- Operational notes: pin shared versions, monitor remote load failures, and keep remotes' public surfaces versioned.
- RSIS3 relevance: the unified dashboard could federate the component views (RSIS3, MyKB, SPACE) so each team ships independently — with shared-dependency and integrity discipline.

## Related
- [[wiki/js-ts-ecosystem/bundlers-and-build-tools|Bundlers and Build Tools]] — related coverage in the same cluster
- [[wiki/js-ts-ecosystem/federated-components|Federated Components]] — related coverage in the same cluster
- [[wiki/js-ts-ecosystem/module-federation|Module Federation]] — related coverage in the same cluster
- [[wiki/js-ts-ecosystem/federated-components|Federated Components]] — related coverage in the same cluster
- [[wiki/web-platforms/web-frameworks|Web Frameworks]] — related coverage in the same cluster
- [[wiki/web-platforms/component-architecture|Component Architecture]] — related coverage in the same cluster
- [[wiki/web-platforms/web-components|Web Components]] — related coverage in the same cluster
