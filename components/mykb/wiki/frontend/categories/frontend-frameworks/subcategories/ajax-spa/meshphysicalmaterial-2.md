---
status: "growing"
type: "entity"
title: "MeshPhysicalMaterial"
description: "Referenced in session 019f40da"
tags: ["ajax", "android", "api", "ast", "auth", "aws", "entity"]
timestamp: "2026-07-19T22:41:40Z"
resource: ""
---


## Meshphysicalmaterial 2

MeshPhysicalMaterial appears in 2 session(s) categorized as API, Cloud, Mobile, Security. Related topics: ajax, android, api, auth, aws.

**Domain:** Web Platforms › [[wiki/web-platforms/supercategories/frontend/index|Frontend]] › [[wiki/web-platforms/supercategories/frontend/categories/frontend-frameworks/index|Frontend Frameworks]] › Meshphysicalmaterial 2

## Overview

MeshPhysicalMaterial is Three.js's physically based rendering (PBR) material. It extends the standard material with advanced surface effects such as clearcoat, sheen, transmission, and iridescence, which makes it the default choice when realism matters. PBR works by describing how a surface interacts with light using a small set of physically meaningful parameters rather than ad hoc shader code. The material builds on the energy-conserving shading model shared with `MeshStandardMaterial`, using a microfacet BRDF with GGX distribution so that parameters stay close to measurable real-world properties.

## Key Parameters

- `metalness` and `roughness` define the base conductor and dielectric response.
- Maps — albedo, normal, roughness, metalness, and ambient occlusion — supply per-texel variation.
- `clearcoat` adds a glossy layer on top (paint, lacquer); `transmission` allows see-through materials such as glass.
- `envMap` provides image-based lighting so metallic and glossy surfaces have something to reflect.
- `sheen` and `sheenRoughness` model cloth-like coatings; `iridescence` and `iridescenceIOR` simulate thin-film interference on surfaces such as soap films and oil sheen.
- `anisotropy` stretches highlights along a direction for brushed metal; `specularIntensity` and `specularColor` tune the base specular response.

## Lighting and Color

PBR results depend on the lighting environment. Recent Three.js releases use physical light units and expose a `useLegacyLights` switch, so light intensity, falloff, and color management matter as much as material parameters. Output is expected in sRGB with a tone mapping curve such as `ACESFilmicToneMapping`, and `envMapIntensity` scales how strongly image-based lighting contributes. Without proper image-based lighting, PBR surfaces look flat or too dark, and metallic surfaces lose the reflections that make them read as metal. An environment map or a simple `HemisphereLight` provides the diffuse and reflection base that PBR needs.

## Rendering Notes

- Transmission requires a transmission render target and is the most expensive feature; clearcoat, sheen, and iridescence each add shader instructions that scale with pixel count.
- Quality settings should scale by device: cap `pixelRatio` on mobile, reduce transmission samples on low-end hardware, and share materials across many meshes to cut draw calls.
- Tune parameters one at a time, because they interact — raising `roughness` reduces the visible effect of both clearcoat highlights and environment reflections.

## Related Concepts

- [[wiki/frontend/categories/frontend-frameworks/subcategories/bootstrap/webglrenderer-2|WebGLRenderer]] — the material pipeline
- [[wiki/frontend/categories/frontend-frameworks/subcategories/ajax-spa/bufferattribute|BufferAttribute]] — geometry data the material shades
- [[wiki/frontend/categories/frontend-frameworks/subcategories/angular/webgl-10|WebGL]] — the rendering context behind the material
- [[wiki/frontend/categories/frontend-frameworks/subcategories/ajax-spa/canvastexture|CanvasTexture]] — a common source of texture maps
- [[wiki/frontend/animation-performance|Animation Performance]] — keeping real-time PBR rendering smooth

## Related Entities

- [[wiki/web-platforms/supercategories/frontend/categories/frontend-frameworks/subcategories/ajax-spa/ace-10|Ace 10]]
- [[wiki/web-platforms/supercategories/frontend/categories/frontend-frameworks/subcategories/ajax-spa/aa|Aa]]
- [[wiki/web-platforms/supercategories/frontend/categories/frontend-frameworks/subcategories/ajax-spa/insecurerequestwarning-2|Insecurerequestwarning 2]]
- [[wiki/web-platforms/supercategories/frontend/categories/frontend-frameworks/subcategories/ajax-spa/jetbrains-10|Jetbrains 10]]
- [[wiki/web-platforms/supercategories/frontend/categories/frontend-frameworks/subcategories/ajax-spa/csv-10|Csv 10]]
- [[wiki/web-platforms/supercategories/frontend/categories/frontend-frameworks/subcategories/ajax-spa/dataframe-2|Dataframe 2]]
- [[wiki/web-platforms/supercategories/frontend/categories/frontend-frameworks/subcategories/ajax-spa/invalid-login-2|Invalid Login 2]]
- [[wiki/web-platforms/supercategories/frontend/categories/frontend-frameworks/subcategories/ajax-spa/langchain-2|Langchain 2]]
