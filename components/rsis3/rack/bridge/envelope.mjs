/**
 * COSMOS Bridge — T2 dense multimodal messaging wrapper.
 *
 * Spec: cosmos-envelope/1
 *
 * A dense envelope is the canonical wire shape between Cosmos components
 * and the LLM bridge. It carries:
 *   - header   (spec, kind, sender, timestamp)
 *   - text     (the human/agent message)
 *   - ctx      (compact cosmos snapshot: kg, strategies, pulses, drives,
 *               syntheses)
 *   - artifacts (ordered list of file/data refs with mime, size, sha256;
 *               text artifacts can carry an inline preview, image artifacts
 *               are passed to the LLM as inline_data)
 *
 * Pure Node stdlib — no dependencies.
 */
import { createHash } from 'node:crypto';
import { readFile, readdir, stat } from 'node:fs/promises';
import path from 'node:path';

export const ENVELOPE_SPEC = 'cosmos-envelope/1';

const TEXT_MIME = /^(text\/|application\/(json|yaml|toml|xml|javascript|typescript|markdown)|.*\/(json|xml|yaml|toml|javascript|typescript|md))$/;
const IMAGE_MIME = /^image\//;

const MIME_BY_EXT = {
  '.md': 'text/markdown',
  '.json': 'application/json',
  '.jsonl': 'application/jsonl',
  '.yaml': 'text/yaml',
  '.yml': 'text/yaml',
  '.toml': 'text/toml',
  '.txt': 'text/plain',
  '.log': 'text/plain',
  '.py': 'text/x-python',
  '.mjs': 'text/javascript',
  '.js': 'text/javascript',
  '.ts': 'text/typescript',
  '.html': 'text/html',
  '.css': 'text/css',
  '.png': 'image/png',
  '.jpg': 'image/jpeg',
  '.jpeg': 'image/jpeg',
  '.gif': 'image/gif',
  '.webp': 'image/webp',
  '.svg': 'image/svg+xml',
  '.pdf': 'application/pdf',
};

export function mimeOf(name) {
  return MIME_BY_EXT[path.extname(String(name || '')).toLowerCase()] || 'application/octet-stream';
}

export const isText = (mime) => TEXT_MIME.test(mime || '');
export const isImage = (mime) => IMAGE_MIME.test(mime || '');

export function sha256(buf) {
  return createHash('sha256').update(buf).digest('hex');
}

/** Build a normalized artifact ref object. */
export function artifactRef({ ref, name, mime, size, sha, kind = 'file', inline = false, preview = null, data = null, status = null, truncated = false }) {
  return {
    kind,
    ref: ref ?? null,
    name: name ?? (ref ? path.basename(ref) : 'unnamed'),
    mime: mime ?? mimeOf(name || ref),
    size: size ?? null,
    sha,
    inline,
    preview,
    data, // base64 (images only) — never echoed back to the client
    status,
    truncated,
  };
}

/** Resolve an artifact ref against a set of allowed roots; reject traversal. */
export function resolveRef(ref, roots) {
  const clean = String(ref || '').replace(/\\/g, '/');
  if (!clean || clean.startsWith('/') || /^[a-zA-Z]:/.test(clean)) return null;
  for (const r of roots) {
    const base = path.resolve(r);
    const abs = path.resolve(base, clean);
    if (abs === base || abs.startsWith(base + path.sep)) return abs;
  }
  return null;
}

const SKIP_PARTS = /^(\.|__)/;

/**
 * Scan known Cosmos artifact locations and return up to `limit` refs
 * (newest first). Never inlines content — refs only.
 */
export async function listArtifactRefs({ root, mykb, limit = 12 }) {
  const out = [];
  const jobs = [];
  const add = async (p) => {
    try {
      const s = await stat(p);
      if (!s.isFile()) return;
      out.push({
        kind: 'file',
        ref: path.relative(root, p),
        name: path.basename(p),
        mime: mimeOf(p),
        size: s.size,
        sha: null, // hashed lazily on inline to keep snapshot cheap
      });
    } catch { /* skip */ }
  };

  // explicit state/telemetry files (committed, small)
  jobs.push(
    add(path.join(root, 'rack', 'goals_stack.json')),
    add(path.join(root, 'rack', 'pulses', 'latest.json')),
    add(path.join(root, 'rack', 'pulses', 'dashboard-data.json')),
    add(path.join(root, '.rsis', 'strategies.json')),
    add(path.join(root, '.rsis', 'knowledge_graph.json')),
  );

  // latest syntheses
  try {
    const dir = path.join(mykb, 'wiki', 'syntheses');
    const files = (await readdir(dir))
      .filter((f) => f.endsWith('.md') && !SKIP_PARTS.test(f))
      .sort()
      .slice(-5);
    for (const f of files) jobs.push(add(path.join(dir, f)));
  } catch { /* mykb not present */ }

  await Promise.all(jobs);
  const seen = new Set();
  return out.filter((a) => (seen.has(a.ref) ? false : (seen.add(a.ref), true)))
    .slice(-limit)
    .reverse();
}

/** Inline a text artifact (preview only, truncated). Returns null on failure. */
export async function inlineText(absPath, maxBytes = 8000) {
  try {
    const buf = await readFile(absPath);
    const truncated = buf.length > maxBytes;
    const preview = buf.subarray(0, maxBytes).toString('utf8');
    return { ok: true, truncated, preview, sha: sha256(buf), size: buf.length };
  } catch {
    return { ok: false };
  }
}

/** Read an image artifact for Gemini inline_data. Returns null on failure. */
export async function readImage(absPath, maxBytes = 4 * 1024 * 1024) {
  try {
    const buf = await readFile(absPath);
    if (buf.length > maxBytes) return { ok: false, reason: 'too-large' };
    return { ok: true, data: buf.toString('base64'), size: buf.length, sha: sha256(buf) };
  } catch {
    return { ok: false, reason: 'unreadable' };
  }
}

/** Compact subset of the cosmos snapshot carried inside every envelope. */
export function compactCtx(ctx) {
  return {
    ts: ctx.ts,
    drives: ctx.drives
      ? {
          id: ctx.drives.id,
          status: ctx.drives.status,
          tiers: (ctx.drives.tiers || []).map((t) => ({ tier: t.tier, name: t.name })),
        }
      : null,
    kg: ctx.kg,
    strategies: ctx.strategies,
    pulses: ctx.pulses.count,
    syntheses: (ctx.syntheses || []).slice(-3),
  };
}

/**
 * Build a dense envelope (cosmos-envelope/1).
 *
 * @param {object} o
 * @param {string} o.kind        'chat' | 'state' | 'artifact' | 'system'
 * @param {string} o.text        message text
 * @param {object} o.ctx         compact cosmos context (see compactCtx)
 * @param {object[]} o.artifacts normalized artifact refs
 * @param {object} [o.state]     optional bridge state (model, llm, cost)
 */
export function buildEnvelope({ kind = 'chat', text = '', ctx = null, artifacts = [], state = null }) {
  return {
    spec: ENVELOPE_SPEC,
    kind,
    ts: new Date().toISOString(),
    sender: 'cosmos-bridge',
    text,
    ctx,
    artifacts: artifacts.map((a) => ({
      kind: a.kind || 'file',
      ref: a.ref,
      name: a.name,
      mime: a.mime,
      size: a.size,
      sha: a.sha || null,
      inline: !!a.inline,
      preview: a.inline && a.preview ? a.preview.slice(0, 4000) : undefined,
    })),
    state,
  };
}

/** Tolerant parse of a serialized envelope; returns null on garbage. */
export function parseEnvelope(str) {
  try {
    const o = JSON.parse(String(str || ''));
    return o && o.spec === ENVELOPE_SPEC ? o : null;
  } catch {
    return null;
  }
}

export function serializeEnvelope(env) {
  return JSON.stringify(env, null, 2);
}
