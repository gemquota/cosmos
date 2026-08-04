---
type: "entity"
title: "FOV"
resource: ""
---
description: "Field of view — the angular region an agent, camera, or sensor can perceive"
tags: ["acronym", "angular", "api", "ast", "auth", "authentication", "entity", "perception"]
timestamp: "2026-07-19T22:41:42Z"

# FOV

## Summary
Field of view, or FOV, is the angular extent of the world that an agent, camera, or sensor can perceive at a given moment. It determines what can be seen, detected, or rendered, and it directly shapes behavior in games, robotics, and simulations. Getting FOV right balances realism against performance and gameplay fairness.

## Details
- **Definition** — FOV is usually measured as horizontal and vertical angles from the observer's direction; a wider angle sees more but with less detail per unit area.
- **Distance falloff** — perception weakens with range, so FOV alone is incomplete without a maximum distance and attenuation curve.
- **Occlusion** — walls and other geometry block line of sight even inside the FOV, so visibility checks must combine angles with raycasts or shadow maps.
- **Rendering use** — cameras use FOV with near and far planes to build a perspective projection, directly affecting the view frustum and culling.
- **Gameplay use** — stealth and detection systems compute enemy FOV to decide when a player is spotted, usually with a reaction delay attached.
- **Tuning** — too-wide FOV makes detection trivial; too-narrow makes it exploitable; designers tune both angle and falloff to hit the intended tension.
- **Common failure modes** — checking only angles and ignoring occlusion, or letting FOV extend through floors and ceilings.
- **Worked example** — a camera with a 90-degree FOV renders only objects inside its frustum; an enemy with the same angle sees the player only when no wall blocks the line of sight.
- **Practical relevance** — FOV is the primitive behind visibility culling, sensor simulation, and believable agent perception.

## Related
- [[wiki/web-platforms/webgl-basics|WebGL Basics]] — perspective projection and frustums
- [[wiki/web-platforms/canvas-2d|Canvas 2D]] — drawing visible geometry
- [[wiki/agent-systems/behavior-trees|Behavior Trees]] — perception-driven decisions
- [[wiki/agent-systems/action-observation-loop|Action-Observation Loop]] — sensing before acting
- [[wiki/agent-systems/simulation-environments-agents|Simulation Environments for Agents]] — agents with limited sight
- [[wiki/web-platforms/browser-rendering-pipeline|Browser Rendering Pipeline]] — how scenes become pixels
