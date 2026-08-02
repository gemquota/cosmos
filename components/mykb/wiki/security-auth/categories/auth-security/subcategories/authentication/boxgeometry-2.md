---
type: "entity"
title: "BoxGeometry"
description: "Referenced in session 019ef7a0"
tags: ["ajax", "android", "api", "ast", "auth", "authentication", "aws", "entity"]
timestamp: "2026-07-19T22:41:40Z"
resource: ""
status: "growing"
---

## Boxgeometry 2

BoxGeometry is the standard box geometry class in Three.js, the JavaScript 3D library. It builds a rectangular box — a cuboid — from width, height, and depth parameters, and generates the vertices, faces, and UV coordinates needed to render it. It is one of the first geometries developers meet, because boxes are the building blocks of countless scenes.

The geometry is defined by its eight corners, and Three.js generates the twelve triangles (two per face) that form its six faces. Optional width, height, and depth segment counts subdivide the box, adding vertices that enable non-uniform effects such as bending or wave deformations. Material assignments can differ per face when an array of materials is provided, which is how boxes get different textures on each side.

In modern Three.js, geometries are built on BufferGeometry, which stores vertex data in typed arrays for efficient GPU upload. The library provides helpers to compute normals and bounding boxes, and geometry can be merged, transformed, and disposed to manage memory. Dispose matters in long-running scenes: geometries and materials hold GPU resources, and leaking them degrades performance over time.

The sessions recorded this entity in API, cloud, mobile, and security contexts, where the geometry was most likely part of a visualization, a game, or a client-side renderer. The related entities below list the neighboring authentication pages observed in the same sessions, giving the component a place in the wider vocabulary of the knowledge base.



Boxes also serve as the primitive for collision detection and spatial partitioning in many engines: a bounding box around an object cheaply tests whether two objects can possibly overlap before any precise calculation runs. The same math powers octrees and bounding volume hierarchies that accelerate rendering and physics. Understanding BoxGeometry is therefore not just about drawing a cube but about a family of techniques that build on the axis-aligned box.
**Domain:** Web Platforms › [[wiki/web-platforms/supercategories/security-auth/index|Security Auth]] › [[wiki/web-platforms/supercategories/security-auth/categories/auth-security/index|Auth Security]] › Boxgeometry 2

## Related Entities

- [[wiki/web-platforms/supercategories/security-auth/categories/auth-security/subcategories/authentication/ab|Ab]]
- [[wiki/web-platforms/supercategories/security-auth/categories/auth-security/subcategories/authentication/automatic-10|Automatic 10]]
- [[wiki/web-platforms/supercategories/security-auth/categories/auth-security/subcategories/authentication/fov-2|Fov 2]]
- [[wiki/web-platforms/supercategories/security-auth/categories/auth-security/subcategories/authentication/selective-chaos|Selective Chaos]]
- [[wiki/web-platforms/supercategories/security-auth/categories/auth-security/subcategories/authentication/rubenverborgh|Rubenverborgh]]
- [[wiki/web-platforms/supercategories/security-auth/categories/auth-security/subcategories/authentication/sim-speed|Sim Speed]]
- [[wiki/web-platforms/supercategories/security-auth/categories/auth-security/subcategories/authentication/missing-content|Missing Content]]
- [[wiki/web-platforms/supercategories/security-auth/categories/auth-security/subcategories/authentication/searchtext|Searchtext]]
