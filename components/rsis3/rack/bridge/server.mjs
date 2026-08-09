#!/usr/bin/env node
/**
 * COSMOS Bridge — LLM ↔ Cosmos framework gateway (multitiered goal T3).
 *
 * Serves the chat UI (dashboard/bridge.html) and the bridge APIs:
 *   GET  /api/cosmos  — dense cosmos context envelope (pulses, KG,
 *                       strategies, syntheses, active drives/goal stack,
 *                       artifact refs)
 *   GET  /api/events  — SSE live feed: telemetry.* loop events, state.*
 *                       file changes, cycle.complete summaries (Phase 1)
 *   GET  /api/cycles  — archived per-cycle summary cards (JSONL archive)
 *   POST /api/chat    — LLM proxy: system prompt = bridge persona + goal
 *                       tiers + cosmos context + attached artifacts.
 *                       Replies stream as NDJSON (cosmos-envelope/1,
 *                       Phase 2) when the client sends
 *                       `Accept: application/x-ndjson` (or `stream: true`),
 *                       otherwise a legacy JSON reply is returned.
 *
 * Phase 2 hardening (cosmos-envelope/1 · v1.1):
 *   - typed structured artifacts: JSON/YAML/TOML parsed to schema blocks
 *   - multimodal: audio inline_data, PDF text extraction, video rejection
 *   - server-side caps: text preview 8 KB, media 4 MB, body 6 MB
 *   - explicit ref allowlist: rack/bridge/allowlist.json (defaults to
 *     root+mykb containment)
 *   - in-memory rate limit on /api/chat (20 req/min, Retry-After header)
 *   - origin guard: non-localhost origins refused unless
 *     RSIS_BRIDGE_ALLOW_ORIGIN is set
 *
 * The API key lives only here (server-side); the client never sees it.
 * If no key is configured (or the provider is unreachable) the bridge
 * answers with a deterministic cosmos-state envelope so the UI still works.
 *
 * Phase 3 product surface:
 *   - conversations persist to rack/bridge/sessions/<id>.jsonl and resume
 *     via GET /api/sessions[/:id]
 *   - sessions reaching RSIS_BRIDGE_MEMORY_N exchanges are distilled into
 *     an OKF synthesis note in MyKB (chat memory loop)
 *   - optional bearer-token auth (RSIS_BRIDGE_TOKEN) for /api/*
 *
 * Usage:
 *   cd components/rsis3 && node rack/bridge/server.mjs
 * Env:
 *   RSIS_BRIDGE_PORT          (default 8787)
 *   RSIS_BRIDGE_MODEL         (default gemini-2.5-flash)
 *   GEMINI_API_KEY            (required for LLM mode)
 *   RSIS_BRIDGE_ALLOW_ORIGIN  (comma-separated extra allowed origins)
 *   RSIS_BRIDGE_RATE_LIMIT    (req/min per client, default 20)
 *   RSIS_BRIDGE_RATE_WINDOW_MS (default 60000)
 *   RSIS_BRIDGE_TOKEN         (optional bearer token for /api/* when set)
 *   RSIS_BRIDGE_SESSIONS_DIR  (override conversation archive dir)
 *   RSIS_BRIDGE_MEMORY_DIR    (override MyKB synthesis output dir)
 *   RSIS_BRIDGE_MEMORY_N      (exchanges before distillation, default 6)
 */
import { createServer } from 'node:http';
import { appendFile, mkdir, readFile, readdir, stat, writeFile } from 'node:fs/promises';
import { randomBytes, createHmac, timingSafeEqual as tse } from 'node:crypto';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import * as env from './envelope.mjs';
import * as ev from './events.mjs';

const PORT = Number(process.env.RSIS_BRIDGE_PORT || 8787);
const MODEL = process.env.RSIS_BRIDGE_MODEL || 'gemini-2.5-flash';
const KEY = process.env.GEMINI_API_KEY || '';
const ALLOW_ORIGIN = (process.env.RSIS_BRIDGE_ALLOW_ORIGIN || '')
  .split(',').map((s) => s.trim()).filter(Boolean);
const RATE_MAX = Number(process.env.RSIS_BRIDGE_RATE_LIMIT || 20);
const RATE_WINDOW_MS = Number(process.env.RSIS_BRIDGE_RATE_WINDOW_MS || 60000);
const TIMEOUT_MS = 30000;

const HERE = path.dirname(fileURLToPath(import.meta.url));
const ROOT = path.resolve(HERE, '..', '..');            // components/rsis3
const REPO = path.resolve(ROOT, '..', '..');            // repo root
const DASH = path.join(ROOT, 'dashboard');
const PULSES = path.join(ROOT, 'rack', 'pulses');
const RSIS_STATE = path.join(ROOT, '.rsis');
const MYKB = path.resolve(ROOT, '..', 'mykb');
const CYCLES_DIR = path.join(ROOT, 'rack', 'bridge', 'cycles');
const ALLOWLIST_FILE = path.join(ROOT, 'rack', 'bridge', 'allowlist.json');
const TOKEN = process.env.RSIS_BRIDGE_TOKEN || '';
const USERS_FILE = process.env.RSIS_USERS_FILE || path.join(RSIS_STATE, 'users.json');
const USERS_SECRET = process.env.RSIS_USERS_SECRET || '';
const SESSIONS_DIR = process.env.RSIS_BRIDGE_SESSIONS_DIR || path.join(ROOT, 'rack', 'bridge', 'sessions');
const MEMORY_DIR = process.env.RSIS_BRIDGE_MEMORY_DIR || path.join(MYKB, 'wiki', 'syntheses');
const MEMORY_N = Number(process.env.RSIS_BRIDGE_MEMORY_N || 6);

const json = (s) => { try { return JSON.parse(s); } catch { return null; } };
const read = async (p, fb = null) => {
  try { return JSON.parse(await readFile(p, 'utf8')); } catch { return fb; }
};

// ── allowlist (cosmos-envelope/1 Phase 2) ───────────────────────────────

let _allow = null;
/** Load rack/bridge/allowlist.json; default to root+mykb containment. */
async function allowlist() {
  if (_allow) return _allow;
  try {
    const raw = json(await readFile(ALLOWLIST_FILE, 'utf8'));
    if (raw && Array.isArray(raw.roots) && raw.roots.length) {
      const roots = raw.roots.map((r) => path.resolve(REPO, r));
      const deny = (raw.deny || []).map((d) => String(d));
      _allow = { roots, deny, base: REPO };
      return _allow;
    }
  } catch { /* fall through to default */ }
  _allow = { roots: [ROOT, MYKB], deny: [], base: null };
  return _allow;
}

// ── cost telemetry (Phase 5: daily LLM cost visibility) ──────────────────

async function costSummary(hours = 24) {
  const file = path.join(RSIS_STATE, 'costs.jsonl');
  let total = 0;
  let tokensIn = 0;
  let tokensOut = 0;
  let traces = 0;
  const byAgent = {};
  const byDay = {};
  try {
    const cutoff = Date.now() - hours * 3600 * 1000;
    for (const line of (await readFile(file, 'utf8')).split(/\r?\n/)) {
      if (!line.trim()) continue;
      const rec = json(line);
      if (!rec) continue;
      const ts = Number(rec.ts || 0) * 1000;
      if (!ts || ts < cutoff) continue;
      const cost = Number(rec.cost || 0);
      total += cost;
      tokensIn += Number(rec.tokens_in || 0);
      tokensOut += Number(rec.tokens_out || 0);
      traces += 1;
      const agent = rec.agent || 'unknown';
      byAgent[agent] = (byAgent[agent] || 0) + cost;
      const day = new Date(ts).toISOString().slice(0, 10);
      byDay[day] = (byDay[day] || 0) + cost;
    }
  } catch { /* no cost ledger yet */ }
  const agentRows = Object.entries(byAgent)
    .map(([agent, cost]) => ({ agent, cost: Math.round(cost * 1e6) / 1e6 }))
    .sort((a, b) => b.cost - a.cost);
  const trend = Object.entries(byDay)
    .map(([day, cost]) => ({ day, cost: Math.round(cost * 1e6) / 1e6 }))
    .sort((a, b) => a.day.localeCompare(b.day));
  let budget = null;
  try {
    const budgets = json(await readFile(path.join(RSIS_STATE, 'budgets.json'), 'utf8'));
    if (budgets && budgets.ceiling_usd) {
      budget = {
        ceiling: Number(budgets.ceiling_usd),
        remaining: Math.round((Number(budgets.ceiling_usd) - total) * 1e6) / 1e6,
      };
    }
  } catch { /* no budgets.json yet */ }
  return {
    traces,
    tokens_in: tokensIn,
    tokens_out: tokensOut,
    cost: Math.round(total * 1e6) / 1e6,
    window_hours: hours,
    by_agent: agentRows,
    trend_7d: trend,
    budget,
  };
}

// ── cosmos context envelope (tier 2: dense messaging wrapper) ───────────

async function cosmosSnapshot(projectName) {
  const [dd, goals, strategies, kg, profile] = await Promise.all([
    read(path.join(PULSES, 'dashboard-data.json'), {}),
    read(path.join(ROOT, 'rack', 'goals_stack.json'), null),
    read(path.join(RSIS_STATE, 'strategies.json'), {}),
    read(path.join(RSIS_STATE, 'knowledge_graph.json'), { nodes: [], edges: [] }),
    projectName && projectName !== 'cosmos'
      ? read(path.join(ROOT, 'rack', 'projects', projectName + '.json'), null)
      : Promise.resolve(null),
  ]);
  let syntheses = [];
  try {
    const dir = path.join(MYKB, 'wiki', 'syntheses');
    const files = (await readdir(dir))
      .filter((f) => f.endsWith('.md') && !f.startsWith('00-'))
      .sort()
      .slice(-5);
    syntheses = files;
  } catch { /* mykb not present — omit */ }
  const pop = strategies.population || [];
  const best = pop.reduce((b, s) => (s.fitness > (b?.fitness ?? -1) ? s : b), null);
  const artifacts = await env.listArtifactRefs({ root: ROOT, mykb: MYKB });
  const costs = await costSummary();
  return {
    ts: new Date().toISOString(),
    model: MODEL,
    llm: KEY ? 'connected' : 'offline-fallback',
    project: profile ? { name: profile.name, repo: profile.repo, goals: profile.goals } : (projectName || 'cosmos'),
    costs,
    drives: goals ? {
      id: goals.id,
      title: goals.title,
      status: goals.status,
      tiers: (goals.tiers || []).map((t) => ({ tier: t.tier, name: t.name, goal: t.goal })),
    } : null,
    pulses: { count: (dd.pulses || []).length, summary: dd.summary || {} },
    kg: { nodes: (kg.nodes || []).length, edges: (kg.edges || []).length },
    strategies: { generation: strategies.generation || 0, best_fitness: best?.fitness ?? null },
    syntheses,
    artifacts,
  };
}

/** Enrich a derived telemetry summary with live KG + strategy state, then archive it. */
async function handleCycleComplete(summary) {
  const [kg, strategies] = await Promise.all([
    read(path.join(RSIS_STATE, 'knowledge_graph.json'), { nodes: [], edges: [] }),
    read(path.join(RSIS_STATE, 'strategies.json'), {}),
  ]);
  const pop = strategies.population || [];
  const best = pop.reduce((b, s) => (s.fitness > (b?.fitness ?? -1) ? s : b), null);
  summary.kg = { nodes: (kg.nodes || []).length, edges: (kg.edges || []).length };
  summary.strategies = {
    generation: strategies.generation || 0,
    best_fitness: best?.fitness ?? null,
  };
  await ev.appendCycle(CYCLES_DIR, summary);
  return summary;
}

// ── artifact processing (cosmos-envelope/1 · v1.1) ─────────────────────

/** Parse a `data:` URL payload into `{ mime, buf }`. */
function parseDataUrl(dataUrl, fallbackName) {
  const comma = dataUrl.indexOf(',');
  const meta = dataUrl.slice(5, comma < 0 ? dataUrl.length : comma);
  const data = comma >= 0 ? dataUrl.slice(comma + 1) : '';
  const mime = (/^([^;]+)/.exec(meta) || [])[1] || env.mimeOf(fallbackName);
  return { mime, buf: Buffer.from(data, 'base64') };
}

/**
 * Normalize client-supplied artifacts (dataUrl payloads from the UI, or
 * server-side refs resolved against the explicit allowlist) into envelope
 * artifact refs. Images and audio are returned separately as base64
 * candidates for Gemini inline_data.
 */
async function processArtifacts(bodyArtifacts) {
  const allow = await allowlist();
  const processed = [];
  const media = [];
  for (const a of bodyArtifacts || []) {
    if (!a || typeof a !== 'object') continue;
    const name = String(a.name || a.ref || a.path || '');
    // 1. client-inlined payload (chat UI file picker)
    if (typeof a.dataUrl === 'string' && a.dataUrl.startsWith('data:')) {
      const { mime, buf } = parseDataUrl(a.dataUrl, name);
      if (env.isImage(mime) || env.isAudio(mime)) {
        if (buf.length > env.MEDIA_MAX_BYTES) {
          processed.push(env.artifactRef({ name, mime, size: buf.length, status: 'too-large', reason: 'media exceeds 4 MB inline cap' }));
          continue;
        }
        media.push({ name, mime, data: buf.toString('base64') });
        processed.push(env.artifactRef({ name, mime, size: buf.length, sha: env.sha256(buf), status: env.isImage(mime) ? 'image' : 'audio' }));
      } else if (env.isVideo(mime)) {
        processed.push(env.artifactRef({ name, mime, size: buf.length, status: 'unsupported', reason: 'video-frame rejection' }));
      } else if (env.isPdf(mime)) {
        const pdf = env.extractPdfTextFromBuffer(buf);
        processed.push(env.artifactRef({
          name, mime, size: buf.length, sha: env.sha256(buf),
          inline: pdf.ok, preview: pdf.ok ? pdf.text : undefined, truncated: pdf.ok ? pdf.truncated : undefined,
          status: pdf.ok ? 'pdf-text' : 'unsupported', reason: pdf.ok ? undefined : pdf.reason,
        }));
      } else if (env.isStructured(mime)) {
        const text = buf.subarray(0, env.TEXT_PREVIEW_MAX).toString('utf8');
        const { parsed, schema } = env.parseStructured(mime, text);
        processed.push(env.artifactRef({
          name, mime, size: buf.length, sha: env.sha256(buf), inline: true,
          truncated: buf.length > env.TEXT_PREVIEW_MAX, parsed, schema,
          status: parsed ? 'schema' : 'inlined',
        }));
      } else {
        const preview = buf.subarray(0, env.TEXT_PREVIEW_MAX).toString('utf8');
        processed.push(env.artifactRef({
          name, mime, size: buf.length, sha: env.sha256(buf), inline: true,
          preview, truncated: buf.length > env.TEXT_PREVIEW_MAX, status: 'inlined',
        }));
      }
      continue;
    }
    // 2. server-side ref (resolved against the explicit allowlist)
    const ref = String(a.ref || a.path || '');
    const abs = env.resolveRef(ref, allow);
    if (!abs) {
      processed.push(env.artifactRef({ ref, name, status: 'denied', reason: 'outside allowlist' }));
      continue;
    }
    const mime = String(a.type || env.mimeOf(ref));
    if (env.isStructured(mime)) {
      const r = await env.readStructured(abs);
      if (r.ok) {
        const { parsed, schema } = env.parseStructured(mime, r.text);
        processed.push(env.artifactRef({
          ref, name, mime, size: r.size, sha: r.sha, inline: true, truncated: r.truncated,
          parsed, schema, status: parsed ? 'schema' : 'inlined',
        }));
      } else {
        processed.push(env.artifactRef({ ref, name, mime, status: 'missing' }));
      }
    } else if (env.isText(mime)) {
      const t = await env.inlineText(abs);
      if (t.ok) {
        processed.push(env.artifactRef({ ref, name, mime, size: t.size, sha: t.sha, inline: true, preview: t.preview, truncated: t.truncated, status: 'inlined' }));
      } else {
        processed.push(env.artifactRef({ ref, name, mime, status: 'missing' }));
      }
    } else if (env.isImage(mime) || env.isAudio(mime)) {
      const m = await env.readMedia(abs);
      if (m.ok) {
        media.push({ name, mime, data: m.data });
        processed.push(env.artifactRef({ ref, name, mime, size: m.size, sha: m.sha, status: env.isImage(mime) ? 'image' : 'audio' }));
      } else {
        processed.push(env.artifactRef({ ref, name, mime, size: null, status: m.reason === 'too-large' ? 'too-large' : 'missing', reason: m.reason }));
      }
    } else if (env.isPdf(mime)) {
      const pdf = await env.extractPdfText(abs);
      processed.push(env.artifactRef({
        ref, name, mime,
        inline: pdf.ok, preview: pdf.ok ? pdf.text : undefined, truncated: pdf.ok ? pdf.truncated : undefined,
        status: pdf.ok ? 'pdf-text' : 'unsupported', reason: pdf.ok ? undefined : pdf.reason,
      }));
    } else if (env.isVideo(mime)) {
      const s = await stat(abs).catch(() => null);
      processed.push(env.artifactRef({ ref, name, mime, size: s ? s.size : null, status: 'unsupported', reason: 'video-frame rejection' }));
    } else {
      const s = await stat(abs).catch(() => null);
      processed.push(env.artifactRef({ ref, name, mime, size: s ? s.size : null, status: s ? 'attached' : 'missing' }));
    }
  }
  return { processed, media };
}

/** Render attached artifacts into the user-turn prompt block. */
function artifactPrompt(processed) {
  const lines = ['', '[Attached artifacts — cosmos-envelope/1]'];
  for (const a of processed) {
    if (a.status === 'missing' || a.status === 'denied' || a.status === 'unsupported' || a.status === 'too-large') {
      lines.push(`- ${a.name || a.ref}: ${a.status}${a.reason ? ` (${a.reason})` : ''}`);
      continue;
    }
    lines.push(`- ${a.name} (${a.mime}, ${a.size ?? '?'} B, sha ${(a.sha || '').slice(0, 12) || 'n/a'}) [${a.status}]`);
    if (a.parsed && a.schema) {
      lines.push('  schema: ' + JSON.stringify({ keys: a.schema.keys, depth: a.schema.depth, types: a.schema.types }));
    } else if (a.preview) {
      lines.push('  ```');
      lines.push(a.preview.slice(0, 2500));
      if (a.truncated) lines.push('  …(truncated)');
      lines.push('  ```');
    }
  }
  return lines.join('\n');
}

function driveLines(drives) {
  if (!drives || !drives.tiers) return '';
  return drives.tiers
    .map((t) => `T${t.tier} ${t.name}: ${t.goal}`)
    .join('\n');
}

function systemPrompt(ctx) {
  return [
    'You are the COSMOS Bridge — the communicative front end of the RSIS3',
    'self-improvement framework (MyKB memory, SPACE ideation, L1–L9 loops,',
    'GitHub-pushed cadence). Be concrete: cite files, metrics, and artifacts.',
    '',
    'Active multitiered goal stack:',
    driveLines(ctx.drives) || '—',
    '',
    `Cosmos snapshot (${ctx.ts}):`,
    `- KG: ${ctx.kg.nodes} nodes / ${ctx.kg.edges} edges`,
    `- Strategies: generation ${ctx.strategies.generation}, best fitness ${ctx.strategies.best_fitness ?? 'n/a'}`,
    `- Pulses: ${ctx.pulses.count}`,
    ctx.syntheses.length ? `- Latest syntheses: ${ctx.syntheses.slice(-3).join(', ')}` : '',
  ].filter(Boolean).join('\n');
}

// ── LLM call (Gemini REST, stdlib-only) ─────────────────────────────────

function buildGeminiBody(system, messages, media = []) {
  const contents = [];
  const lastUser = [...messages].reverse().find((m) => m.role === 'user' && m.content);
  for (const m of messages) {
    if (!m || !m.content) continue;
    if (m.role === 'user' || m.role === 'assistant') {
      const parts = [{ text: m.content }];
      if (m === lastUser) {
        for (const md of media) parts.push({ inline_data: { mime_type: md.mime, data: md.data } });
      }
      contents.push({ role: m.role === 'user' ? 'user' : 'model', parts });
    }
  }
  return {
    system_instruction: { parts: [{ text: system }] },
    contents,
    generationConfig: { temperature: 0.6, maxOutputTokens: 2048 },
  };
}

async function fetchGemini(url, body) {
  const res = await fetch(url, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(body),
    signal: AbortSignal.timeout(TIMEOUT_MS),
  });
  if (!res.ok) {
    const err = await res.text();
    throw new Error(`Gemini ${res.status}: ${err.slice(0, 300)}`);
  }
  return res;
}

/** Legacy single-shot Gemini call (non-streaming). */
async function callGemini(system, messages, media = []) {
  const res = await fetchGemini(
    `https://generativelanguage.googleapis.com/v1beta/models/${encodeURIComponent(MODEL)}:generateContent?key=${encodeURIComponent(KEY)}`,
    buildGeminiBody(system, messages, media),
  );
  const data = await res.json();
  const text = (data.candidates?.[0]?.content?.parts || [])
    .map((p) => p.text || '').join('');
  if (!text) throw new Error('Gemini returned empty reply');
  return text.trim();
}

/**
 * Streaming Gemini call. Consumes the `:streamGenerateContent?alt=sse`
 * response and emits decoded text chunks to `onDelta`. Returns the full
 * trimmed reply.
 */
async function streamGemini(system, messages, media = [], onDelta) {
  const res = await fetchGemini(
    `https://generativelanguage.googleapis.com/v1beta/models/${encodeURIComponent(MODEL)}:streamGenerateContent?alt=sse&key=${encodeURIComponent(KEY)}`,
    buildGeminiBody(system, messages, media),
  );
  const reader = res.body.getReader();
  const dec = new TextDecoder();
  let buf = '';
  let full = '';
  for (;;) {
    const { done, value } = await reader.read();
    if (done) break;
    buf += dec.decode(value, { stream: true });
    let idx;
    while ((idx = buf.indexOf('\n')) >= 0) {
      const line = buf.slice(0, idx).trim();
      buf = buf.slice(idx + 1);
      if (!line.startsWith('data:')) continue;
      const payload = line.slice(5).trim();
      if (!payload || payload === '[DONE]') continue;
      try {
        const evt = json(payload);
        const parts = evt?.candidates?.[0]?.content?.parts || [];
        for (const part of parts) {
          if (part.text) { full += part.text; onDelta?.(part.text); }
        }
      } catch { /* skip malformed SSE frame */ }
    }
  }
  if (!full.trim()) throw new Error('Gemini returned empty reply');
  return full.trim();
}

function fallbackReply(ctx, question, processed = []) {
  const drives = ctx.drives;
  const lines = [
    `Bridge offline (no LLM key/model configured) — deterministic cosmos reply:`,
    '',
    `State: KG ${ctx.kg.nodes} nodes / ${ctx.kg.edges} edges · strategies gen ${ctx.strategies.generation} (best fitness ${ctx.strategies.best_fitness ?? 'n/a'}) · ${ctx.pulses.count} pulses.`,
  ];
  if (drives) {
    lines.push('');
    lines.push('Active drives:');
    for (const t of drives.tiers) lines.push(`- T${t.tier} ${t.name}: ${t.goal}`);
  }
  if (ctx.syntheses.length) {
    lines.push('');
    lines.push(`Latest syntheses: ${ctx.syntheses.join(', ')}`);
  }
  if (processed.length) {
    lines.push('');
    lines.push(`Attached artifacts: ${processed.map((a) => `${a.name} [${a.status}]`).join(', ')}`);
  }
  lines.push('');
  lines.push(`Your question: "${question}" — start the bridge with a configured GEMINI_API_KEY for full LLM answers.`);
  return lines.join('\n');
}

// ── rate limiting (in-memory bucket, no deps) ───────────────────────────

function createRateLimiter({ max = RATE_MAX, windowMs = RATE_WINDOW_MS } = {}) {
  const hits = new Map();
  return {
    check(key) {
      const now = Date.now();
      const rec = hits.get(key) || { start: now, count: 0 };
      if (now - rec.start >= windowMs) { rec.start = now; rec.count = 0; }
      rec.count += 1;
      hits.set(key, rec);
      if (rec.count > max) {
        return { allowed: false, retryAfter: Math.max(1, Math.ceil((rec.start + windowMs - now) / 1000)) };
      }
      if (hits.size > 2000) {
        for (const [k, v] of hits) if (now - v.start > windowMs * 2) hits.delete(k);
      }
      return { allowed: true };
    },
  };
}

function clientKey(req) {
  const fwd = (req.headers['x-forwarded-for'] || '').split(',')[0].trim();
  return fwd || req.socket.remoteAddress || 'unknown';
}

// ── origin guard ────────────────────────────────────────────────────────

function originAllowed(req) {
  const o = req.headers.origin;
  if (!o) return { allowed: true };
  let host;
  try { host = new URL(o).hostname; } catch { return { allowed: false, reason: 'malformed origin' }; }
  if (host === 'localhost' || host === '127.0.0.1' || host === '::1') return { allowed: true };
  if (ALLOW_ORIGIN.includes(o)) return { allowed: true, echoed: o };
  return { allowed: false, reason: 'origin not allowed' };
}

// ── conversation persistence + chat memory loop (Phase 3) ──────────────

const SESSION_ID_RE = /^[A-Za-z0-9_-]{1,128}$/;

function newSessionId() {
  return 's-' + Date.now().toString(36) + '-' + randomBytes(4).toString('hex');
}

function exchangeRecord({ sessionId, role, content, artifacts = [], model, llm }) {
  return {
    spec: env.ENVELOPE_SPEC,
    kind: 'exchange',
    ts: new Date().toISOString(),
    session_id: sessionId,
    role,
    content,
    artifacts: artifacts.map((a) => ({
      ref: a.ref, name: a.name, mime: a.mime, size: a.size, status: a.status,
    })),
    model,
    llm,
  };
}

async function appendExchange(sessionId, rec) {
  if (!SESSION_ID_RE.test(String(sessionId || ''))) return null;
  await mkdir(SESSIONS_DIR, { recursive: true });
  const file = path.join(SESSIONS_DIR, path.basename(sessionId) + '.jsonl');
  await appendFile(file, JSON.stringify(rec) + '\n', 'utf8');
  return file;
}

/** Read a session archive into `{ id, created, updated, count, messages }`. */
async function readSession(sessionId) {
  if (!SESSION_ID_RE.test(String(sessionId || ''))) return null;
  const file = path.join(SESSIONS_DIR, path.basename(sessionId) + '.jsonl');
  let text;
  try { text = await readFile(file, 'utf8'); } catch { return null; }
  const messages = [];
  let created = null;
  let updated = null;
  for (const line of text.split(/\r?\n/)) {
    if (!line.trim()) continue;
    const r = json(line);
    if (!r || r.kind !== 'exchange') continue;
    if (r.role === 'user' || r.role === 'assistant') {
      messages.push({ role: r.role, content: r.content, ts: r.ts, artifacts: r.artifacts || [] });
      if (!created || (r.ts || '') < created) created = r.ts || null;
      if (!updated || (r.ts || '') > updated) updated = r.ts || null;
    }
  }
  return { id: path.basename(sessionId), created, updated, count: messages.length, messages };
}

async function listSessions(limit = 20) {
  let files = [];
  try { files = (await readdir(SESSIONS_DIR)).filter((f) => f.endsWith('.jsonl')); } catch { return []; }
  const out = [];
  for (const f of files.sort().reverse().slice(0, limit)) {
    const sess = await readSession(f.replace(/\.jsonl$/, ''));
    if (!sess) continue;
    const lastUser = [...sess.messages].reverse().find((m) => m.role === 'user');
    out.push({
      id: sess.id,
      created: sess.created,
      updated: sess.updated,
      count: sess.count,
      preview: lastUser ? String(lastUser.content).slice(0, 120) : '',
    });
  }
  return out;
}

/** Distill a session into an OKF synthesis note once it passes MEMORY_N. */
async function maybeConsolidateSession(sess) {
  if (!MEMORY_N || MEMORY_N < 1) return;
  const turns = sess.messages.filter((m) => m.role === 'assistant').length;
  if (turns < MEMORY_N) return;
  await mkdir(MEMORY_DIR, { recursive: true });
  const firstUser = sess.messages.find((m) => m.role === 'user');
  const title = firstUser
    ? String(firstUser.content).replace(/\s+/g, ' ').trim().slice(0, 72)
    : `Bridge session ${sess.id}`;
  const body = sess.messages.map((m) => {
    const text = String(m.content || '').replace(/\s+/g, ' ').trim();
    const brief = text.length > 320 ? text.slice(0, 320) + '…' : text;
    const arts = (m.artifacts || []).map((a) => a.name || a.ref).filter(Boolean);
    return `- **${m.role}** (${(m.ts || '').slice(0, 19).replace('T', ' ')}): ${brief || '(empty)'}${arts.length ? ` — artifacts: ${arts.join(', ')}` : ''}`;
  }).join('\n');
  const note = [
    '---',
    'type: "synthesis"',
    `title: "${title}"`,
    `description: "Bridge session ${sess.id} distilled after ${turns} exchange(s) — durable input to the T1 communication tier"`,
    'tags: ["rsis3", "bridge", "session", "chat-memory", "synthesis"]',
    `timestamp: "${new Date().toISOString()}"`,
    'status: "growing"',
    '---',
    '',
    `# ${title}`,
    '',
    `Session \`${sess.id}\` reached ${turns} exchange(s) and was distilled by the COSMOS Bridge chat memory loop.`,
    '',
    body,
    '',
    '## Related',
    '- [[wiki/syntheses/rsis3-phase-2-envelope-hardening-2026-08-08|RSIS3 Phase 2 — envelope hardening]]',
    '',
  ].join('\n');
  const file = path.join(MEMORY_DIR, `rsis3-bridge-session-${sess.id}.md`);
  try {
    await writeFile(file, note, { encoding: 'utf8', flag: 'wx' });
    console.error(`[bridge] memory: distilled session ${sess.id} → ${file}`);
  } catch (e) {
    if (e.code !== 'EEXIST') throw e; // already distilled
  }
}

async function persistChat(sessionId, userContent, artifacts, reply, llm) {
  if (!sessionId || !SESSION_ID_RE.test(String(sessionId))) return;
  await appendExchange(sessionId, exchangeRecord({
    sessionId, role: 'user', content: userContent, artifacts, model: MODEL, llm,
  }));
  await appendExchange(sessionId, exchangeRecord({
    sessionId, role: 'assistant', content: reply, artifacts: [], model: MODEL, llm,
  }));
  const sess = await readSession(sessionId);
  if (sess) await maybeConsolidateSession(sess);
}

// ── HTTP ────────────────────────────────────────────────────────────────
// ── HTTP ────────────────────────────────────────────────────────────────

const send = (res, code, payload, ctype = 'application/json', extra = {}) => {
  res.writeHead(code, { 'Content-Type': ctype, 'Cache-Control': 'no-store', ...extra });
  res.end(ctype === 'application/json' ? JSON.stringify(payload) : payload);
};

const server = createServer(async (req, res) => {
  const url = new URL(req.url, `http://localhost:${PORT}`);
  const p = url.pathname;
  const cors = { 'Access-Control-Allow-Methods': 'GET, POST, OPTIONS', 'Access-Control-Allow-Headers': 'Content-Type' };

  // Phase 2 origin guard: localhost (or no Origin) allowed; anything else
  // needs RSIS_BRIDGE_ALLOW_ORIGIN. Applies to preflight too.
  const og = originAllowed(req);
  if (!og.allowed) return send(res, 403, { error: og.reason || 'origin not allowed' }, 'application/json', cors);
  cors['Access-Control-Allow-Origin'] = og.echoed || '*';

  if (req.method === 'OPTIONS') { res.writeHead(204, cors); return res.end(); }

  // ── Phase 12 auth ─────────────────────────────────────────────────────
  // Legacy mode: RSIS_BRIDGE_TOKEN guards every /api/* call.
  // Users mode: RSIS_USERS_SECRET enables per-user signed tokens; identity
  // is validated, then role+membership+policy gate each action
  // (observer read · contributor propose · approver approve).
  // Share links (/api/sessions/:id/share) stay read-only and public.
  const ROLE_CAPS = { observer: ['read'], contributor: ['read', 'propose'], approver: ['read', 'propose', 'approve', 'rollback'] };
  const b64url = (buf) => Buffer.from(buf).toString('base64url');
  const b64urlDecode = (s) => Buffer.from(s, 'base64url');
  const pad64 = (s) => s + '='.repeat((4 - (s.length % 4)) % 4);
  const hmac = (key, data) => createHmac('sha256', key).update(data).digest();
  async function loadUsers() {
    const raw = await read(USERS_FILE, null);
    if (raw && Array.isArray(raw.users)) return raw.users;
    return [];
  }
  function verifyUserToken(token) {
    if (!USERS_SECRET) return null;
    const parts = String(token || '').split('.');
    if (parts.length !== 2) return null;
    let payload, sig;
    try {
      payload = b64urlDecode(pad64(parts[0]));
      sig = b64urlDecode(pad64(parts[1]));
    } catch { return null; }
    const expect = hmac(USERS_SECRET, payload);
    if (sig.length !== expect.length || !tse(sig, expect)) return null;
    const text = payload.toString('utf8');
    const dot = text.lastIndexOf('.');
    if (dot < 0) return null;
    const uid = text.slice(0, dot);
    const exp = Number(text.slice(dot + 1));
    if (!exp || Date.now() / 1000 >= exp) return null;
    return uid;
  }
  async function currentUser(req, url) {
    const auth = req.headers.authorization || '';
    const raw = auth.startsWith('Bearer ') ? auth.slice(7)
      : (url.searchParams.get('token') || '');
    if (USERS_SECRET) {
      const uid = verifyUserToken(raw);
      if (!uid) return null;
      const users = await loadUsers();
      return users.find((u) => u.id === uid) || null;
    }
    if (TOKEN && raw === TOKEN) return { id: 'owner', role: 'approver', projects: ['*'] };
    return null;
  }
  function can(user, action, project) {
    if (!user) return false;
    const caps = ROLE_CAPS[user.role] || [];
    if (!caps.includes(action)) return false;
    const projects = user.projects || [];
    if (!projects.includes('*') && !projects.includes(project)) return false;
    return true;
  }
  const usersMode = Boolean(USERS_SECRET);
  if (p.startsWith('/api/') && !p.endsWith('/share') && (TOKEN || usersMode)) {
    const user = await currentUser(req, url);
    if (!user) {
      return send(res, 401, { error: 'unauthorized' }, 'application/json', cors);
    }
    req.user = user;
  } else if (p.startsWith('/api/') && !p.endsWith('/share')) {
    // Public mode (no token configured): implicit owner, all actions allowed.
    req.user = { id: 'public', role: 'approver', projects: ['*'] };
  }

  try {
    if (req.method === 'GET' && p === '/') {
      const html = await readFile(path.join(DASH, 'bridge.html'), 'utf8');
      return send(res, 200, html, 'text/html', cors);
    }
    if (req.method === 'GET' && p === '/bridge.js') {
      const js = await readFile(path.join(DASH, 'bridge.js'), 'utf8');
      return send(res, 200, js, 'application/javascript', cors);
    }
    if (req.method === 'GET' && p === '/health') {
      return send(res, 200, { ok: true, model: MODEL, llm: KEY ? 'connected' : 'offline-fallback' }, 'application/json', cors);
    }
    const project = url.searchParams.get('project') || 'cosmos';
    if (req.method === 'GET' && p === '/api/cosmos') {
      if (!can(req.user, 'read', project)) return send(res, 403, { error: 'forbidden: read on ' + project }, 'application/json', cors);
      return send(res, 200, await cosmosSnapshot(project), 'application/json', cors);
    }
    if (req.method === 'GET' && p === '/api/events') {
      if (!can(req.user, 'read', project)) return send(res, 403, { error: 'forbidden' }, 'application/json', cors);
      return hub.addClient(req, res);
    }
    if (req.method === 'GET' && p === '/api/cycles') {
      if (!can(req.user, 'read', project)) return send(res, 403, { error: 'forbidden' }, 'application/json', cors);
      const limit = Math.min(100, Math.max(1, Number(url.searchParams.get('limit') || 20)));
      return send(res, 200, { cycles: await ev.recentCycles(CYCLES_DIR, limit) }, 'application/json', cors);
    }
    if (req.method === 'GET' && p === '/api/sessions') {
      if (!can(req.user, 'read', project)) return send(res, 403, { error: 'forbidden' }, 'application/json', cors);
      const limit = Math.min(100, Math.max(1, Number(url.searchParams.get('limit') || 20)));
      return send(res, 200, { sessions: await listSessions(limit) }, 'application/json', cors);
    }
    if (req.method === 'GET' && p.startsWith('/api/sessions/') && p.endsWith('/share')) {
      const id = decodeURIComponent(p.slice('/api/sessions/'.length, -'/share'.length));
      const sess = await readSession(id);
      if (!sess) return send(res, 404, { error: 'session not found' }, 'application/json', cors);
      // Read-only public view: no artifacts/private fields, token guard
      // retained for writes.
      return send(res, 200, {
        id: sess.id, created: sess.created, updated: sess.updated,
        count: sess.count, preview: true,
        messages: (sess.messages || []).map((m) => ({ role: m.role, content: m.content })),
      }, 'application/json', cors);
    }
    if (req.method === 'GET' && p.startsWith('/api/sessions/')) {
      if (!can(req.user, 'read', project)) return send(res, 403, { error: 'forbidden' }, 'application/json', cors);
      const id = decodeURIComponent(p.slice('/api/sessions/'.length));
      const sess = await readSession(id);
      if (!sess) return send(res, 404, { error: 'session not found' }, 'application/json', cors);
      return send(res, 200, sess, 'application/json', cors);
    }
    if (req.method === 'GET' && p === '/api/approvals') {
      if (!can(req.user, 'read', project)) return send(res, 403, { error: 'forbidden' }, 'application/json', cors);
      const dir = path.join(ROOT, 'rack', 'approvals');
      let ids = [];
      try { ids = (await readdir(dir)).filter((f) => f.endsWith('.json')).sort(); } catch { /* none */ }
      const approvals = [];
      for (const f of ids.slice(-20)) {
        const rec = await read(path.join(dir, f), null);
        if (rec) approvals.push({
          id: rec.id, status: rec.status, actor: rec.actor, ts: rec.ts,
          reason: rec.reason, description: rec.description,
          goal: rec.goal, target_files: rec.target_files,
          diff: String(rec.diff || '').slice(0, 2000),
        });
      }
      return send(res, 200, { approvals }, 'application/json', cors);
    }
    if ((req.method === 'POST') && p.startsWith('/api/approvals/') && (p.endsWith('/approve') || p.endsWith('/reject'))) {
      if (!can(req.user, 'approve', project)) return send(res, 403, { error: 'forbidden: approve on ' + project }, 'application/json', cors);
      const id = decodeURIComponent(p.split('/')[3]);
      const action = p.endsWith('/approve') ? 'approve' : 'reject';
      const { execFileSync } = await import('node:child_process');
      try {
        const out = execFileSync(process.execPath, ['-m', 'rsis', 'approve', id, ...(action === 'reject' ? ['--reject'] : []), '--actor', req.user.id], { cwd: ROOT, encoding: 'utf8', timeout: 60000 });
        return send(res, 200, { ok: true, action, actor: req.user.id, output: String(out).trim() }, 'application/json', cors);
      } catch (e) {
        return send(res, 400, { error: 'approval action failed', detail: String(e.stderr || e.message).trim() }, 'application/json', cors);
      }
    }
    if (req.method === 'POST' && p === '/api/chat') {
      if (!can(req.user, 'propose', project)) return send(res, 403, { error: 'forbidden: propose on ' + project }, 'application/json', cors);
      const rl = rate.check(clientKey(req));
      if (!rl.allowed) {
        return send(res, 429, { error: 'rate limit exceeded', retry_after: rl.retryAfter }, 'application/json', { ...cors, 'Retry-After': String(rl.retryAfter) });
      }
      const chunks = [];
      let size = 0;
      for await (const c of req) {
        size += c.length;
        if (size > env.TOTAL_MAX_BYTES) {
          return send(res, 413, { error: 'payload too large' }, 'application/json', cors);
        }
        chunks.push(c);
      }
      const body = json(Buffer.concat(chunks).toString('utf8')) || {};
      const sessionId = String(body.session_id || '');
      const messages = Array.isArray(body.messages) ? body.messages : [];
      const ctx = await cosmosSnapshot();
      const { processed, media } = await processArtifacts(body.artifacts);
      const system = body.cosmos === false
        ? 'You are the COSMOS Bridge. Answer directly and concisely.'
        : systemPrompt(ctx);
      if (processed.length) {
        const last = [...messages].reverse().find((m) => m.role === 'user');
        if (last) last.content += artifactPrompt(processed);
      }
      const lastQuestion = messages.filter((m) => m.role === 'user').pop()?.content || '';

      const wantStream = /application\/x-ndjson/.test(req.headers.accept || '') || body.stream === true;
      if (wantStream) {
        const replyMeta = { kind: 'reply', model: MODEL, llm: ctx.llm, ts: ctx.ts, stream: true };
        res.writeHead(200, {
          ...cors,
          'Content-Type': 'application/x-ndjson',
          'Cache-Control': 'no-store',
          'X-Accel-Buffering': 'no',
        });
        const sendLine = (obj) => res.write(JSON.stringify(obj) + '\n');
        sendLine({ type: 'meta', ...replyMeta, artifacts: processed.map(artifactSummary) });
        let streamLlm = ctx.llm;
        let streamReply = '';
        try {
          if (!KEY) throw new Error('GEMINI_API_KEY not set');
          streamReply = await streamGemini(system, messages, media, (delta) => sendLine({ type: 'delta', text: delta }));
          streamLlm = 'connected';
        } catch (e) {
          console.error(`[bridge] LLM call failed (${e.message}); falling back`);
          streamReply = fallbackReply(ctx, lastQuestion, processed);
          sendLine({ type: 'delta', text: streamReply });
        }
        sendLine({ type: 'done', reply: streamReply, llm: streamLlm });
        await persistChat(sessionId, lastQuestion, processed, streamReply, streamLlm).catch((e) => console.error('[bridge] session persist failed:', e.message));
        return res.end();
      }

      // legacy JSON reply
      let reply;
      let llm = ctx.llm;
      try {
        if (!KEY) throw new Error('GEMINI_API_KEY not set');
        reply = await callGemini(system, messages, media);
        llm = 'connected';
      } catch (e) {
        console.error(`[bridge] LLM call failed (${e.message}); falling back`);
        reply = fallbackReply(ctx, lastQuestion, processed);
      }
      await persistChat(sessionId, lastQuestion, processed, reply, llm).catch((e) => console.error('[bridge] session persist failed:', e.message));
      return send(res, 200, {
        reply,
        model: MODEL,
        llm,
        ts: ctx.ts,
        session_id: sessionId || null,
        artifacts: processed.map(artifactSummary),
      }, 'application/json', cors);
    }
    return send(res, 404, { error: 'not found' }, 'application/json', cors);
  } catch (e) {
    console.error('[bridge] error:', e);
    return send(res, 500, { error: String(e.message || e) }, 'application/json', cors);
  }
});

function artifactSummary(a) {
  return {
    kind: a.kind,
    ref: a.ref,
    name: a.name,
    mime: a.mime,
    size: a.size,
    sha: a.sha,
    status: a.status,
    reason: a.reason,
    parsed: a.parsed,
    schema: a.schema,
  };
}

const rate = createRateLimiter();
const hub = new ev.EventHub();
ev.startStateWatchers({ root: ROOT, hub });
ev.startTelemetryWatcher({
  dir: path.join(RSIS_STATE, 'telemetry'),
  hub,
  onCycleComplete: (summary) => { handleCycleComplete(summary).catch((e) => console.error('[bridge] cycle enrich failed:', e.message)); },
});
void ev.recentCycles(CYCLES_DIR, 1).then((r) => {
  console.log(`   live streaming: ${r.length} archived cycle(s), watchers on ${ev.POLL_MS}ms`);
}).catch(() => {});

server.listen(PORT, () => {
  console.log(`🌉 COSMOS Bridge listening on http://localhost:${PORT}`);
  console.log(`   model=${MODEL} llm=${KEY ? 'connected' : 'offline-fallback'} root=${ROOT}`);
  console.log(`   events: GET /api/events (SSE) · GET /api/cycles · POST /api/chat (NDJSON streaming)`);
  console.log(`   phase2: rate ${RATE_MAX} req/min · allowlist ${ALLOWLIST_FILE} · origins ${ALLOW_ORIGIN.length ? ALLOW_ORIGIN.join(',') : 'localhost-only'}`);
  console.log(`   phase3: sessions ${SESSIONS_DIR} · memory ${MEMORY_DIR} (N=${MEMORY_N}) · auth ${TOKEN ? 'token required' : 'open (localhost)'}`);
});
