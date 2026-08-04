---
type: "entity"
title: "Particle Life"
resource: ""
---
description: "A simulation where colored particles attract and repel to form emergent patterns"
tags: ["android", "api", "ast", "auth", "authentication", "entity", "simulation", "particles"]
timestamp: "2026-07-19T22:41:42Z"

# Particle Life

## Summary
Particle Life is a simulation in which colored particles exert attraction or repulsion on particles of other colors, producing striking emergent patterns. It matters because it shows how simple pairwise rules generate complex, lifelike structure. The simulation is also a practical playground for tuning, performance, and rendering techniques in a browser.

## Details
- **Definition** — each particle is a point with a color; pairwise rules define how strongly and how far particles of each color pair interact.
- **Rules matrix** — a matrix of interaction parameters between colors determines the emergent behavior, from clustering to orbiting.
- **Local interaction** — forces apply only within a radius, so computation stays manageable and patterns remain local.
- **Emergence** — stable structures such as membranes, crystals, and colonies arise without any central control.
- **Tuning** — small parameter changes flip the simulation between chaos, stable patterns, and collapse, making it a tuning laboratory.
- **Performance** — spatial hashing or grids keep neighbor lookup fast enough for thousands of particles.
- **Common failure modes** — unstable integration that explodes, parameter sets that collapse everything, and frame drops at scale.
- **Worked example** — a canvas renders thousands of particles, each frame recomputing pairwise forces within a spatial grid, and the scene self-organizes into persistent shapes.
- **Practical relevance** — Particle Life is both a visualization showcase and a gentle introduction to emergent simulation and spatial optimization.

- **Determinism** — fixed update order and a seeded initial state make the same parameters reproduce the same patterns.
- **Controls** — exposing interaction sliders turns the simulation into an interactive tuning instrument.
- **Scaling** — grid-based neighbor queries keep thousands of particles running at interactive frame rates.
## Related
- [[wiki/shell-environment/categories/cli-tools/particle-size-min|Particle Size Min]] — particle parameters
- [[wiki/web-platforms/canvas-2d|Canvas 2D]] — rendering the simulation
- [[wiki/shell-environment/categories/cli-tools/gravity-sim|Gravity Sim]] — force-based simulation
- [[wiki/agent-systems/simulation-environments-agents|Simulation Environments for Agents]] — simulated worlds
- [[wiki/testing/property-based-testing|Property-Based Testing]] — checking invariants
- [[wiki/web-platforms/offscreen-canvas|Offscreen Canvas]] — background rendering
