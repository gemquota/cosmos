# Contributing to SPACE

Thank you for your interest in contributing to SPACE (Superb Prompt Automatic Creation Engine).

## Quick Start

```bash
# Clone the repository
git clone https://github.com/gemquota/space.git
cd space

# Install dependencies
npm install

# Build
npm run build

# Run tests
npm test
```

## Development Workflow

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/my-feature`)
3. Make your changes with tests
4. Run `npm test` to verify
5. Run `npm run build` to ensure compilation
6. Submit a pull request

## Code Style

- TypeScript strict mode — no `any` types unless absolutely necessary
- Use interfaces over types for object shapes
- Prefer named exports over default exports
- Use `snake_case` for variables and functions, `PascalCase` for types and classes
- Keep functions under 50 lines; extract helpers for longer logic
- Write JSDoc comments for public APIs

## Testing

- All new features must include tests
- Tests go in `tests/unit/` (co-located by feature)
- Use vitest for testing
- Aim for >80% coverage on new code
- Run `npm test` before committing

## Architecture

See `docs/adr/` for Architecture Decision Records documenting key design choices.

### Key Modules

- `src/engine/` — Core orchestration (question routing, session management, artifact extraction)
- `src/storage/` — Persistence layer (filesystem, SQLite)
- `src/llm/` — LLM provider integration (OpenAI, Anthropic, Gemini, Mistral, Ollama)
- `src/export/` — Multi-format export (JSON, Markdown, YAML, HTML, prompt)
- `src/data/` — Framework loading, artifact mapping, key validation
- `src/config/` — Configuration validation and environment variable wiring
- `src/cli/` — CLI interface and commands
- `src/intelligence/` — Adaptive routing, analytics, quality scoring
- `src/integration/` — External integrations (Git)
- `web/` — Web UI (single-file HTML + server)

### Data Flow

```
Framework JSON → FrameworkLoader → QuestionRouter → SessionManager
                                                          ↓
                                                    AnswerEntry
                                                          ↓
                                                  ArtifactExtractor → ArtifactDictionary
                                                          ↓
                                                  ExportCompiler → ExportResult
```

## Adding a New LLM Provider

1. Create `src/llm/providers/your-provider.ts`
2. Implement the `LLMProvider` interface from `src/llm/types.ts`
3. Add the provider to `src/llm/factory.ts`
4. Add tests in `tests/unit/llm-providers.test.ts`
5. Document the provider in this file

## Adding a New Export Format

1. Create `src/export/formatters/your-format-exporter.ts`
2. Implement the exporter returning `ExportResult`
3. Register it in `src/export/index.ts`
4. Add tests

## Architecture Decision Records (ADRs)

We use ADRs to document significant design decisions. See `docs/adr/` for existing records.

To propose a new ADR:
1. Copy `docs/adr/000-template.md`
2. Fill in the template
3. Submit as part of your PR

## Reporting Issues

- Use GitHub Issues for bug reports and feature requests
- Include: OS, Node.js version, SPACE version, steps to reproduce
- For security issues, email privately (see SECURITY.md)

## License

By contributing, you agree that your contributions will be licensed under the MIT License.
