---
type: "entity"
title: "Testing Patterns"
tags: ["testing", "pytest", "jest", "unittest"]
source: ["rsis3/", "space/", "sessions/"]
---

# Testing Patterns

Testing strategies across the ecosystem.

## Coverage by Project
| Project | Framework | Tests | Status |
|---------|-----------|-------|--------|
| RSIS3 | pytest | 38/38 | ✅ All pass |
| SPACE | Vitest | 92/92 | ✅ All pass |
| Golf | pytest | 24 | Active |
| VEPA2 | node | 8 | Light |

## Patterns
- **Test isolation** — Clean state per test
- **Test absolutism** — Zero broken tests allowed (RSIS3 constitution)
- **Integration at boundaries** — Test interfaces between modules
- **Property-based** — SPACE template interpolation verification

See also: [[wiki/testing/index|Testing]], [[wiki/software-engineering/index|Software Engineering]]
