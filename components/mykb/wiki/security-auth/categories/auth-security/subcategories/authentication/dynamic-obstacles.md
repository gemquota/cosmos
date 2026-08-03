---
type: "entity"
title: "Dynamic Obstacles"
resource: ""
---
description: "Moving or changing obstacles that pathfinding and simulation systems must avoid or adapt to"
tags: ["entity", "android", "api", "ast", "auth", "authentication", "pathfinding", "simulation"]
timestamp: "2026-07-19T22:41:41Z"

# Dynamic Obstacles

## Summary
Dynamic obstacles are objects that move or change over time and must be avoided or accounted for by navigation and simulation systems. They matter because static pathfinding assumptions fail the moment the environment changes. Agents, robots, and simulations need replanning and prediction to stay safe around them.

## Details
- **Definition** — a dynamic obstacle is any obstruction whose position, shape, or existence varies over time, such as a moving vehicle, a closing door, or a shifting hazard zone.
- **Perception** — systems detect dynamic obstacles through sensors, simulation state, or event streams; stale perception is a leading cause of collisions.
- **Replanning** — algorithms like D* Lite or dynamic A* repair only the affected parts of a path instead of recomputing from scratch, which keeps replanning fast.
- **Prediction** — assuming obstacles follow predictable motion lets planners plan time-indexed paths through spaces that will be clear later.
- **Time windows** — paths can be annotated with valid time intervals, turning a spatial problem into a space-time problem with explicit scheduling.
- **Local avoidance** — potential fields and velocity-obstacle methods adjust motion locally, complementing global planners when obstacles appear at short range.
- **Common failure modes** — oscillation between routes, over-correction from noisy sensor data, and planners that treat transient obstacles as permanent.
- **Worked example** — an NPC navigating a corridor replans when a hazard zone activates, waits for a moving platform to pass, then resumes its original route once the way is clear.
- **Practical relevance** — handling dynamic obstacles robustly separates toy demos from dependable navigation in games, robotics, and agent simulations.

## Related
- [[wiki/agent-systems/simulation-environments-agents|Simulation Environments for Agents]] — environments with moving hazards
- [[wiki/agent-systems/agent-planning-systems|Agent Planning Systems]] — planning with changing state
- [[wiki/agent-systems/behavior-trees|Behavior Trees]] — reactive behavior selection
- [[wiki/agent-systems/action-observation-loop|Action-Observation Loop]] — sensing before acting
- [[wiki/agent-systems/agent-timeouts|Agent Timeouts]] — bounding replanning cost
- [[wiki/testing/chaos-engineering|Chaos Engineering]] — testing under dynamic conditions
