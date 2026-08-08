#!/usr/bin/env node
/**
 * COSMOS Bridge — LLM ↔ Cosmos framework gateway (multitiered goal T3).
 *
 * Serves the chat UI (dashboard/bridge.html) and two APIs:
 *   GET  /api/cosmos  — dense cosmos context envelope (pulses, KG,
 *                       strategies, syntheses, active drives/goal stack)
 *   POST /api/chat    — LLM proxy: system prompt = bridge persona + goal
 *                       tiers + cosmos context; reply streamed back as JSON
 *
 * The API key lives only here (server-side); the client never sees it.
 * If no key is configured (or the provider is unreachable) the bridge
 * answers with a deterministic cosmos-state envelope so the UI still works.
 *
 * Usage:
 *   cd components/rsis3 && node rack/bridge/server.mjs
 * Env:
 *   RSIS_BRIDGE_PORT  (default 8787)
 *   RSIS_BRIDGE_MODEL (default gemini-2.5-flash)
 *   GEMINI_API_KEY    (optional; enables real LLM replies)
 */
import { createServer } from 'node:http';
import { readFile, readdir } from 'node:fs/promises';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const PORT = Number(process.env.RSIS_BRIDGE_PORT || 8787);
const MODEL = process.env.RSIS_BRIDGE_MODEL || 'gemini-2.5-flash';
const KEY = process.env.GEMINI_API_KEY || '';
const TIMEOUT_MS = 30000;

const HERE = path.dirname(fileURLToPath(import.meta.url));
const ROOT = path.resolve(HERE, '..', '..');            // components/rsis3
const DASH = path.join(ROOT, 'dashboard');
const PULSES = path.join(ROOT, 'rack', 'pulses');
const RSIS_STATE = path.join(ROOT, '.rsis');
const MYKB = path.resolve(ROOT, '..', 'mykb');

const json = (s) => { try { return JSON.parse(s); } catch { return null; } };
const read = async (p, fb = null) => {
  try { return JSON.parse(await readFile(p, 'utf8')); } catch { return fb; }
};

// ── cosmos context envelope (tier 2: dense messaging wrapper) ───────────

async function cosmosSnapshot() {
  const [dd, goals, strategies, kg] = await Promise.all([
    read(path.join(PULSES, 'dashboard-data.json'), {}),
    read(path.join(ROOT, 'rack', 'goals_stack.json'), null),
    read(path.join(RSIS_STATE, 'strategies.json'), {}),
    read(path.join(RSIS_STATE, 'knowledge_graph.json'), { nodes: [], edges: [] }),
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
  return {
    ts: new Date().toISOString(),
    model: MODEL,
    llm: KEY ? 'connected' : 'offline-fallback',
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
  };
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

async function callGemini(system, messages) {
  const contents = [];
  let first = true;
  for (const m of messages) {
    if (!m || !m.content) continue;
    if (first && m.role === 'user') {
      contents.push({ role: 'user', parts: [{ text: m.content }] });
      first = false;
    } else if (m.role === 'user' || m.role === 'assistant') {
      contents.push({ role: m.role === 'user' ? 'user' : 'model', parts: [{ text: m.content }] });
    }
  }
  const body = {
    system_instruction: { parts: [{ text: system }] },
    contents,
    generationConfig: { temperature: 0.6, maxOutputTokens: 2048 },
  };
  const res = await fetch(
    `https://generativelanguage.googleapis.com/v1beta/models/${encodeURIComponent(MODEL)}:generateContent?key=${encodeURIComponent(KEY)}`,
    {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(body),
      signal: AbortSignal.timeout(TIMEOUT_MS),
    },
  );
  if (!res.ok) {
    const err = await res.text();
    throw new Error(`Gemini ${res.status}: ${err.slice(0, 300)}`);
  }
  const data = await res.json();
  const text = (data.candidates?.[0]?.content?.parts || [])
    .map((p) => p.text || '').join('');
  if (!text) throw new Error('Gemini returned empty reply');
  return text.trim();
}

function fallbackReply(ctx, question) {
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
  lines.push('');
  lines.push(`Your question: "${question}" — start the bridge with a configured GEMINI_API_KEY for full LLM answers.`);
  return lines.join('\n');
}

// ── HTTP ────────────────────────────────────────────────────────────────

const CORS = {
  'Access-Control-Allow-Origin': '*',
  'Access-Control-Allow-Methods': 'GET, POST, OPTIONS',
  'Access-Control-Allow-Headers': 'Content-Type',
};

const send = (res, code, payload, ctype = 'application/json') => {
  res.writeHead(code, { ...CORS, 'Content-Type': ctype, 'Cache-Control': 'no-store' });
  res.end(ctype === 'application/json' ? JSON.stringify(payload) : payload);
};

const server = createServer(async (req, res) => {
  const url = new URL(req.url, `http://localhost:${PORT}`);
  const p = url.pathname;
  if (req.method === 'OPTIONS') { res.writeHead(204, CORS); return res.end(); }

  try {
    if (req.method === 'GET' && p === '/') {
      const html = await readFile(path.join(DASH, 'bridge.html'), 'utf8');
      return send(res, 200, html, 'text/html');
    }
    if (req.method === 'GET' && p === '/health') {
      return send(res, 200, { ok: true, model: MODEL, llm: KEY ? 'connected' : 'offline-fallback' });
    }
    if (req.method === 'GET' && p === '/api/cosmos') {
      return send(res, 200, await cosmosSnapshot());
    }
    if (req.method === 'POST' && p === '/api/chat') {
      const chunks = [];
      let size = 0;
      for await (const c of req) {
        size += c.length;
        if (size > 1_000_000) { return send(res, 413, { error: 'payload too large' }); }
        chunks.push(c);
      }
      const body = json(Buffer.concat(chunks).toString('utf8')) || {};
      const messages = Array.isArray(body.messages) ? body.messages : [];
      const ctx = await cosmosSnapshot();
      const system = body.cosmos === false
        ? 'You are the COSMOS Bridge. Answer directly and concisely.'
        : systemPrompt(ctx);
      let reply;
      let llm = ctx.llm;
      try {
        if (!KEY) throw new Error('GEMINI_API_KEY not set');
        reply = await callGemini(system, messages);
        llm = 'connected';
      } catch (e) {
        console.error(`[bridge] LLM call failed (${e.message}); falling back`);
        const last = messages.filter((m) => m.role === 'user').pop()?.content || '';
        reply = fallbackReply(ctx, last);
      }
      return send(res, 200, { reply, model: MODEL, llm, ts: ctx.ts });
    }
    return send(res, 404, { error: 'not found' });
  } catch (e) {
    console.error('[bridge] error:', e);
    return send(res, 500, { error: String(e.message || e) });
  }
});

server.listen(PORT, () => {
  console.log(`🌉 COSMOS Bridge listening on http://localhost:${PORT}`);
  console.log(`   model=${MODEL} llm=${KEY ? 'connected' : 'offline-fallback'} root=${ROOT}`);
});
