---
type: "concept"
title: "Formal Verification of Agents"
description: "Mathematically proving properties of agent behavior"
tags: ["formal-verification", "agents", "safety", "guarantees"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://en.wikipedia.org/wiki/Formal_verification", "https://en.wikipedia.org/wiki/Model_checking"]
---

# Formal Verification of Agents

## Summary
Formal verification of agents uses model checking, theorem proving, and specification languages to prove properties such as termination, safety, and goal consistency before deployment. It provides the strongest available guarantees, at the cost of tractability for large learned systems.

## Details
- **Techniques** — model checking finite state spaces, Hoare-style proofs for programmatic agents, and type systems as lightweight verification.
- **What can be verified today** — scaffold logic, permission guards, and protocol properties; model internals are harder.
- **Bridging learning and logic** — verifiers, monitors, and tripwires attach formal checks to learned behavior.
- **Limits** — specification correctness is itself a challenge (the spec can be wrong), and learned components resist abstraction.
- **RSIS3 relevance** — check-practices is a lightweight formal verification: the workspace checker mechanically proves hygiene invariants hold.

## Related
- [[wiki/concepts/control-protocols|Control Protocols]] — verified constraints
- [[wiki/syntheses/assurance-cases|Assurance Cases]] — argument structure around proofs
- [[wiki/concepts/first-principles-ai|First-Principles AI]] — derivation culture
- [[wiki/concepts/specification-problems|Specification Problems]] — when the spec is the bug
- [[wiki/concepts/formal-verification-of-agents|formal-verification-of-agents]] — technique
- [[wiki/concepts/immutable-evaluator|Immutable Evaluator]] — verified evaluator
- [[wiki/agent-systems/agent-sandboxing|Agent Sandboxing]] — sandboxing agents in the existing graph
