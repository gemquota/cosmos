# ADR 002: No Inheritance in Entity Types

## Status

Accepted

## Date

2024-01-01

## Context

The system has 10 entity types (Framework, Series, Round, Question, Choice, Answer, Artifact, Session, Project, Export) that share some common properties (id, name, description, timestamps).

Options:
1. Base class with inheritance
2. Standalone interfaces (current)
3. Mixins/trait composition

## Decision

Use standalone interfaces without inheritance. Each entity type declares its own properties independently.

## Consequences

### Positive
- Simpler type definitions (no abstract base class to maintain)
- No diamond inheritance issues
- Each entity can evolve independently
- Clear, explicit type boundaries

### Negative
- Some code duplication (id, name, description appear in multiple types)
- Adding a new shared property requires updating multiple interfaces
- No compile-time enforcement of common structure

### Risks
- Divergence over time (entities may drift apart structurally)

## Alternatives Considered

### Base Class Inheritance
- Reduces duplication but adds complexity
- Can lead to "fat" base classes that try to do too much
- Makes it harder to understand individual entity types

### Mixins
- More flexible than inheritance
- Not natively supported in TypeScript (requires class-based approach)
- Added complexity for marginal benefit

## References

- `src/types/index.ts` — All entity type definitions
