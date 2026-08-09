# COSMOS Bridge — Vercel deployment template

The COSMOS dashboard is a static front end; the LLM bridge is a Node
stdlib server that holds the API key. This template is the static
front-end home for the telemetry dashboard; the bridge runs as a hosted
function/process and is reached by the dashboard over HTTP.

## Layout

- `index.html` / `app.json` / `icon.svg` — static dashboard (also shipped
  to GitHub Pages at https://gemquota.github.io/cosmos/)
- `components/rsis3/dashboard/bridge.js` — shared chat widget (native
  embed, no iframe)
- `components/rsis3/rack/bridge/server.mjs` — the bridge process

## Deploying the bridge (hosted function)

Run the bridge wherever your environment variables live (a VPS, a
container, or a serverless function wrapper around `server.mjs`):

```bash
cd components/rsis3
GEMINI_API_KEY=... \
RSIS_BRIDGE_ALLOW_ORIGIN=https://gemquota.github.io \
RSIS_BRIDGE_TOKEN=change-me \
RSIS_BRIDGE_RATE_LIMIT=20 \
node rack/bridge/server.mjs
```

Required for LLM mode: `GEMINI_API_KEY`. For anything other than
localhost clients, set `RSIS_BRIDGE_ALLOW_ORIGIN` (comma-separated) and
`RSIS_BRIDGE_TOKEN`.

## Deploying the dashboard (static front end)

1. Set `BRIDGE_URL` in `components/rsis3/dashboard/config.js` to the
   hosted bridge origin (default `http://localhost:8787`).
2. Optional: set `BRIDGE_TOKEN` next to `BRIDGE_URL` so the widget sends
   `Authorization: Bearer <token>` (leave undefined for localhost).
3. Deploy the repo root as a static site (GitHub Pages or Vercel). The
   repo root `index.html` redirects to the unified dashboard.

## Security notes

- The API key never leaves `server.mjs` — the client only ever talks to
  the bridge.
- `RSIS_BRIDGE_TOKEN` gates every `/api/*` route; `/health` and the
  static shell stay public.
- Conversations are archived server-side to
  `rack/bridge/sessions/<id>.jsonl`; reaching `RSIS_BRIDGE_MEMORY_N`
  (default 6) exchanges distills the session into a MyKB synthesis note.
- Origin guard: non-localhost `Origin` headers are refused unless listed
  in `RSIS_BRIDGE_ALLOW_ORIGIN`.
