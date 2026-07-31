# 🚀 SPACE — Superb Prompt Automatic Creation Engine

**Generate complete development specifications through structured prompt elicitation.**

SPACE runs a 326-probe, 7-series question framework that walks you through conceptual depth, ontology, semantics, procedures, technical specs, methodology, and operations — producing a comprehensive specification document in JSON, Markdown, YAML, HTML, or as a system prompt.

---

## Quick Start

```bash
# Install
npm install -g @gemquota/space

# Create a project
space init my-app

# Run the 326-question session
space run my-app

# Export the specification
space export exports/my-app-session.json -f json,markdown,html
```

## Features

- **7-series elicitation framework** — 67 open-ended + 259 multi-choice probes
- **326 total questions** across conceptual depth, ontology, semantics, procedures, technical specs, methodology, and operations
- **6 export formats** — JSON, Markdown, YAML, HTML, prompt template, diff
- **7 LLM providers** — OpenAI, Anthropic, Gemini, Mistral, Ollama, Template, Null
- **CLI + Web UI** — Full terminal TUI and React-based web interface
- **Session persistence** — Filesystem (default) or SQLite storage with snapshot recovery
- **Git integration** — Auto-commit session progress with `--git`
- **Intelligence layer** — Completeness scoring, contradiction detection, adaptive routing
- **i18n** — English, Spanish, and French locales with extensible translation system

---

## CLI Commands

| Command | Description |
|---------|-------------|
| `space init <name>` | Create a new project |
| `space run <project>` | Start an interactive elicitation session |
| `space run <project> --auto` | Auto-answer with generated responses |
| `space run <project> --resume <session-id>` | Resume a previous session |
| `space run <project> --git` | Auto-commit progress to git |
| `space export <session-file>` | Export to specification documents |
| `space list` | List all projects |
| `space config` | View configuration |
| `space config --list` | List all config options |
| `space framework` | Inspect the framework definition |
| `space status [project]` | Show project/session status |
| `space serve -p <port>` | Start the web UI server |

## Configuration

SPACE is configured via `SPACE_*` environment variables:

```bash
export SPACE_LLM_PROVIDER=openai      # openai|anthropic|gemini|mistral|ollama|local|none
export SPACE_LLM_API_KEY=sk-...       # Your API key
export SPACE_LLM_MODEL=gpt-4o         # Model identifier
export SPACE_LOCALE=en                # en|es|fr
export SPACE_PROJECTS_DIR=~/.space/projects  # Data directory
```

## Web UI

```bash
space serve -p 8888
# Open http://localhost:8888
```

Or build and serve manually:
```bash
cd ui && npm run build && cd ..
space serve -p 8888
```

## Development

```bash
git clone https://github.com/gemquota/space
cd space
npm install
npm run build
npm test
```

### Project Structure

```
src/
├── cli/           — CLI entry point and commands
├── config/        — Configuration system
├── data/          — Framework loading, artifact mapping
├── engine/        — Core session/question/answer engine
├── export/        — Multi-format export pipeline
├── i18n/          — Internationalization (en, es, fr)
├── intelligence/  — Completeness, contradictions, routing
├── llm/           — Provider abstraction + 7 implementations
├── storage/       — Filesystem + SQLite storage adapters
├── template/      — Template variable interpolation
├── types/         — TypeScript interfaces
└── integration/   — Git integration
ui/                — React 18 + Vite web app
meta/              — Cycle audit reports and specs
prompt-framework/  — Original framework definition files
tests/             — 142 tests across 13 test files
```

## Architecture

SPACE follows a layered architecture:

```
CLI / Web UI
     │
     ▼
Engine (session, routing, validation)
     │
     ├──► Storage (filesystem / SQLite)
     ├──► LLM (OpenAI, Anthropic, Gemini, etc.)
     ├──► Export (JSON, Markdown, YAML, etc.)
     └──► Intelligence (scoring, contradictions)
```

Each layer depends only on the types layer beneath it. The engine orchestrates all operations through the `SpaceInstance` API.

## LLM Providers

| Provider | Env Value | API Key Required |
|----------|-----------|:----------------:|
| OpenAI | `openai` | Yes |
| Anthropic | `anthropic` | Yes |
| Google Gemini | `gemini` | Yes |
| Mistral | `mistral` | Yes |
| Ollama (local) | `ollama` | No |
| Local fallback | `local` | No |
| Template (offline) | `none` | No |

## Export Formats

| Format | Extension | Use Case |
|--------|-----------|----------|
| JSON | `.json` | Machine-readable, programmatic consumption |
| Markdown | `.md` | Readable documentation, GitHub |
| YAML | `.yaml` | Config-style structured data |
| HTML | `.html` | Styled document for browser viewing |
| Prompt | `.txt` | System prompt for LLM consumption |
| Diff | `.md` | Session comparison (changed/added/removed) |

## Tests

```bash
npm test              # Run all 142 tests
npm run typecheck     # TypeScript strict check
npm run lint          # ESLint
npm run format:check  # Prettier check
```

## License

MIT — see [LICENSE](LICENSE)
