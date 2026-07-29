# ADR 003: Environment Variable Configuration

## Status

Accepted

## Date

2024-07-28

## Context

The configuration system (SpaceConfig) accepts values programmatically but doesn't read from environment variables. This means:
- Users must pass config via code or CLI args
- Server deployments require code changes for configuration
- No standard 12-factor app compliance

## Decision

Wire environment variables (SPACE_*) to SpaceConfig fields with a configFromEnv() function. Validate at startup.

## Consequences

### Positive
- Standard deployment pattern (Docker, cloud platforms)
- No code changes needed for configuration
- Environment-specific configs without code changes
- CI/CD can set environment variables per environment

### Negative
- Environment variables are less discoverable than config files
- No type checking at the env var level (all strings)
- Potential for confusion between env vars and config file values

### Risks
- Sensitive values (API keys) in environment variables may be logged
- Env var precedence conflicts with programmatic config

## References

- `src/config/validation.ts` — configFromEnv() implementation
- `src/config/defaults.ts` — Default config values
