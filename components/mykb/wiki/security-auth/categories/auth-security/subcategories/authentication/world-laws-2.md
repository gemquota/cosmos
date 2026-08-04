---
type: "concept"
title: "World Laws"
resource: ""
---
description: "The invariant rules that govern a simulation or game world"
tags: ["android", "api", "ast", "auth", "authentication", "entity", "simulation", "rules"]
timestamp: "2026-07-19T22:41:43Z"

# World Laws

## Summary
World laws are the invariant rules that govern a simulation or game world: gravity, conservation, collision, and the game rules that entities must obey. They matter because a world without enforced invariants drifts into nonsense and exploits. Explicit laws keep simulations coherent, fair, and testable, which is what makes them trustworthy.

## Details
- **Definition** — world laws are the rules every entity and system in the world must satisfy, from physics to gameplay constraints.
- **Physics laws** — gravity, momentum, and collision rules define how objects move and interact, typically updated each tick.
- **Gameplay rules** — win conditions, resource limits, and ability restrictions shape what players and agents can do.
- **Invariant enforcement** — state checks at boundaries catch violations early rather than letting corruption propagate.
- **Determinism** — laws applied in fixed order with fixed timesteps keep behavior reproducible across runs.
- **Configurability** — tuning law parameters such as gravity or limits creates different worlds from the same engine.
- **Common failure modes** — laws that contradict each other, entities that bypass rules, and edge cases that violate invariants silently.
- **Worked example** — a physics world enforces that no two solid objects overlap; the collision pass resolves overlaps each frame, and a test asserts the invariant after every tick.
- **Practical relevance** — explicit world laws make simulations predictable, fair, and safe to extend.

- **Consistency** — laws are applied in a consistent order every tick so results do not depend on evaluation order.
- **Bounds** — enforcing minimum and maximum values prevents numeric drift and runaway states.
- **Testing** — invariant checks in the test suite catch law violations the moment they are introduced.
## Related
- [[wiki/agent-systems/simulation-environments-agents|Simulation Environments for Agents]] — worlds with rules
- [[wiki/web-platforms/canvas-2d|Canvas 2D]] — rendering the world
- [[wiki/agent-systems/behavior-trees|Behavior Trees]] — rule-driven behavior
- [[wiki/agent-systems/agent-state-machines|Agent State Machines]] — state transitions
- [[wiki/web-platforms/webgl-basics|WebGL Basics]] — rendering laws visually
- [[wiki/testing/property-based-testing|Property-Based Testing]] — checking invariants
