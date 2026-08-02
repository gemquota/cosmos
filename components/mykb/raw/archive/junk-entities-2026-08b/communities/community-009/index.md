# Community 10

12 entities.

## Entities

- **ambientlight** (ambientlight-2) — connected to error, water simulation, perspectivecamera, directionallight
- **boxgeometry** (boxgeometry-2) — connected to meshbasicmaterial
- **directionallight** (directionallight-2) — connected to meshbasicmaterial, perspectivecamera, meshphysicalmaterial, doubleside, ambientlight
- **doubleside** (doubleside-2) — connected to instancedmesh, perspectivecamera, directionallight
- **error** (error-2) — connected to ambientlight, water simulation, perspectivecamera, directionallight, regexp
- **instancedmesh** (instancedmesh-2) — connected to doubleside, perspectivecamera, directionallight
- **meshbasicmaterial** (meshbasicmaterial-2) — connected to perspectivecamera, directionallight, boxgeometry, meshstandardmaterial
- **meshphysicalmaterial** (meshphysicalmaterial-2) — connected to perspectivecamera, directionallight
- **meshstandardmaterial** (meshstandardmaterial-2) — connected to meshbasicmaterial, perspectivecamera, directionallight
- **perspectivecamera** (perspectivecamera-2) — connected to meshbasicmaterial, directionallight, meshphysicalmaterial, doubleside, ambientlight
- **regexp** (regexp-2) — connected to error
- **water simulation** (water-simulation-2) — connected to ambientlight, error, perspectivecamera, directionallight
