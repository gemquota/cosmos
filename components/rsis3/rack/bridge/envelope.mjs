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
 * CHANGELOG (cosmos-envelope/1 — additive only):
 *   1.1 (2026-08-08) Phase 2 hardening:
 *     - typed structured artifacts (JSON/YAML/TOML → schema block, not raw
 *       strings)
 *     - audio passthrough (inline_data when LLM online), PDF text
 *       extraction, video rejection
 *     - server-side per-type caps: text preview 8 KB, media 4 MB, total
 *       6 MB
 *     - explicit allowlist (rack/bridge/allowlist.json) for ref traversal
 *
 * Pure Node stdlib — no dependencies.
 */
import { createHash } from 'node:crypto';
import { readFile, readdir, stat } from 'node:fs/promises';
import { inflateSync } from 'node:zlib';
import path from 'node:path';

export const ENVELOPE_SPEC = 'cosmos-envelope/1';
export const ENVELOPE_VERSION = '1.1';

// Per-type byte caps (server-side, Phase 2)
export const TEXT_PREVIEW_MAX = 8 * 1024;          // text preview cap
export const MEDIA_MAX_BYTES = 4 * 1024 * 1024;    // image / audio inline cap
export const TOTAL_MAX_BYTES = 6 * 1024 * 1024;    // request body cap
export const STRUCTURED_READ_MAX = 256 * 1024;     // schema-parse read cap

const TEXT_MIME = /^(text\/[a-z0-9+._-]+|application\/(javascript|typescript|xml|markdown))$/i;
const IMAGE_MIME = /^image\//;
const AUDIO_MIME = /^audio\//;
const VIDEO_MIME = /^video\//;
const PDF_MIME = /^application\/pdf$/;
const STRUCTURED_MIME = /(^|\/)(json|jsonl|yaml|yml|toml)$/;

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
export const isAudio = (mime) => AUDIO_MIME.test(mime || '');
export const isVideo = (mime) => VIDEO_MIME.test(mime || '');
export const isPdf = (mime) => PDF_MIME.test(mime || '');
export const isStructured = (mime) => STRUCTURED_MIME.test(mime || '');

export function sha256(buf) {
  return createHash('sha256').update(buf).digest('hex');
}

/** Build a normalized artifact ref object. */
export function artifactRef({ ref, name, mime, size, sha, kind = 'file', inline = false, preview = null, data = null, status = null, truncated = false, parsed = false, schema = null, reason = null }) {
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
    parsed,
    schema,
    reason,
  };
}

/**
 * Resolve an artifact ref against an explicit allowlist (roots + deny
 * prefixes, cosmos-envelope/1 Phase 2). Rejects absolute/rooted refs,
 * traversal outside every root, and any path under a deny prefix.
 *
 * @param {string} ref     client-supplied relative ref
 * @param {string[]|object} rootsOrAllow  array of root dirs, or
 *   `{ roots: [], deny: [], base: '' }` (deny paths relative to base)
 */
export function resolveRef(ref, rootsOrAllow) {
  const clean = String(ref || '').replace(/\\/g, '/');
  if (!clean || clean.startsWith('/') || /^[a-zA-Z]:/.test(clean)) return null;
  const roots = Array.isArray(rootsOrAllow) ? rootsOrAllow : (rootsOrAllow?.roots || []);
  const deny = Array.isArray(rootsOrAllow) ? [] : (rootsOrAllow?.deny || []);
  const base = Array.isArray(rootsOrAllow) ? null : (rootsOrAllow?.base || null);
  // Deny prefixes may be root-relative ('.rsis/telemetry') or repo-relative
  // ('components/rsis3/.rsis/telemetry'); check both against the ref and the
  // resolved path so a denied ref cannot fall through to another root.
  const blocked = (rel) => rel && deny.some((d) => rel === d || rel.startsWith(d + '/'));
  if (blocked(clean)) return null;
  for (const r of roots) {
    const rootAbs = path.resolve(r);
    const abs = path.resolve(rootAbs, clean);
    if (abs !== rootAbs && !abs.startsWith(rootAbs + path.sep)) continue;
    if (deny.length) {
      const rel = base ? path.relative(base, abs).replace(/\\/g, '/') : null;
      if (blocked(rel)) continue;
    }
    return abs;
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

/** Read a media artifact (image/audio) for Gemini inline_data. */
export async function readMedia(absPath, maxBytes = MEDIA_MAX_BYTES) {
  try {
    const buf = await readFile(absPath);
    if (buf.length > maxBytes) return { ok: false, reason: 'too-large' };
    return { ok: true, data: buf.toString('base64'), size: buf.length, sha: sha256(buf) };
  } catch {
    return { ok: false, reason: 'unreadable' };
  }
}

/** Backward-compatible alias. */
export const readImage = readMedia;

/** Read a structured (JSON/YAML/TOML) artifact for schema parsing. */
export async function readStructured(absPath, maxBytes = STRUCTURED_READ_MAX) {
  try {
    const buf = await readFile(absPath);
    const text = buf.subarray(0, maxBytes).toString('utf8');
    return { ok: true, text, size: buf.length, sha: sha256(buf), truncated: buf.length > maxBytes };
  } catch {
    return { ok: false };
  }
}

/**
 * Structural summary of a structured artifact. JSON is parsed with the
 * stdlib; YAML/TOML use a minimal top-level-key scanner (honest subset).
 * Returns `{ parsed, schema }` — schema is `{keys, types, depth}` when
 * parseable, else `{ parsed: false }`.
 */
export function parseStructured(mime, text) {
  const m = String(mime || '');
  const s = String(text || '');
  if (!s.trim()) return { parsed: false };
  if (/json/.test(m)) {
    try {
      const cand = /jsonl/.test(m)
        ? (s.split(/\r?\n/).find((l) => l.trim()) || s)
        : s;
      return { parsed: true, schema: schemaOf(JSON.parse(cand)) };
    } catch {
      return { parsed: false, schema: null };
    }
  }
  const keys = topLevelKeys(s);
  if (keys && keys.length) {
    const types = Object.fromEntries(keys);
    const depth = Object.values(types).some((t) => t === 'object' || t === 'section') ? 2 : 1;
    return { parsed: true, schema: { keys: keys.length, types, depth } };
  }
  return { parsed: false, schema: null };
}

function schemaOf(v, depth = 0) {
  if (Array.isArray(v)) return { kind: 'array', keys: v.length, depth: depth + 1 };
  if (v && typeof v === 'object') {
    const types = {};
    let maxDepth = depth + 1;
    for (const [k, val] of Object.entries(v)) {
      if (val && typeof val === 'object') {
        types[k] = Array.isArray(val) ? 'array' : 'object';
        maxDepth = Math.max(maxDepth, schemaOf(val, depth + 1).depth);
      } else {
        types[k] = typeof val;
      }
    }
    return { kind: 'object', keys: Object.keys(v).length, types, depth: maxDepth };
  }
  return { kind: typeof v, depth: depth + 1 };
}

function topLevelKeys(s) {
  const out = new Map();
  let inBlock = false;
  for (const raw of s.split(/\r?\n/)) {
    const line = raw.trim();
    if (!line || line.startsWith('#') || line.startsWith('---') || line.startsWith('...')) continue;
    if (inBlock) {
      if (/^\S/.test(line) && !line.startsWith('-')) inBlock = false;
      else continue;
    }
    const section = /^\[([^\]]+)\]$/.exec(line);
    if (section) { out.set(section[1].trim(), 'section'); inBlock = false; continue; }
    const m = /^([^:=]+?):\s*(.*)$/.exec(line) || /^([^=]+?)=\s*(.*)$/.exec(line);
    if (m) {
      const key = m[1].trim().replace(/^["']|["']$/g, '');
      if (!key) continue;
      const val = m[2].trim();
      if (!val || val === '|' || val === '>') { out.set(key, 'object'); inBlock = true; }
      else out.set(key, valueType(val));
      continue;
    }
    if (line.startsWith('- ')) inBlock = true;
  }
  return [...out.entries()];
}

function valueType(v) {
  const t = String(v).trim();
  if (/^[-+]?\d+(\.\d+)?$/.test(t)) return 'number';
  if (/^(true|false)$/i.test(t)) return 'boolean';
  if (/^(null|~)$/i.test(t)) return 'null';
  if (/^[\[{].*[\]}]$/.test(t)) return 'collection';
  if (/^\d{4}-\d{2}-\d{2}/.test(t)) return 'date';
  return 'string';
}

/** Minimal PDF text extraction (FlateDecode + raw content streams). */
export function extractPdfTextFromBuffer(buf, maxBytes = TEXT_PREVIEW_MAX) {
  try {
    const src = buf.subarray(0, Math.min(buf.length, 2 * STRUCTURED_READ_MAX));
    const re = /stream\r?\n([\s\S]*?)endstream/g;
    const out = [];
    let m;
    while ((m = re.exec(src)) !== null && out.join(' ').length < maxBytes) {
      let raw = null;
      try { raw = inflateSync(Buffer.from(m[1], 'binary')); } catch { raw = null; }
      const chunk = raw ? raw.toString('utf8') : m[1].toString('binary');
      const btRe = /BT([\s\S]*?)ET/g;
      const tre = /\((?:[^()\\]|\\.)*\)/g;
      const ops = [];
      let bm;
      while ((bm = btRe.exec(chunk)) !== null) {
        let tm;
        while ((tm = tre.exec(bm[1])) !== null) {
          const s = tm[0].slice(1, -1).replace(/\\([()\\])/g, '$1').replace(/\\n/g, ' ').replace(/\\r/g, ' ');
          if (s.trim()) ops.push(s);
        }
      }
      if (!ops.length) {
        // Fallback: only pull parenthesized strings from texty chunks.
        let tm;
        while ((tm = tre.exec(chunk)) !== null) {
          const s = tm[0].slice(1, -1).replace(/\\([()\\])/g, '$1').replace(/\\n/g, ' ').replace(/\\r/g, ' ');
          if (s.trim() && /^[\x20-\x7e]{2,}$/.test(s)) ops.push(s);
        }
      }
      if (ops.length) out.push(ops.join(' '));
    }
    const text = out.join(' ').replace(/\s+/g, ' ').trim();
    if (!text) return { ok: false, reason: 'no-text' };
    return { ok: true, text: text.slice(0, maxBytes), truncated: text.length > maxBytes };
  } catch {
    return { ok: false, reason: 'unreadable' };
  }
}

export async function extractPdfText(absPath, maxBytes = TEXT_PREVIEW_MAX) {
  try {
    return extractPdfTextFromBuffer(await readFile(absPath), maxBytes);
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
      parsed: a.parsed || undefined,
      schema: a.schema || undefined,
      status: a.status || undefined,
      reason: a.reason || undefined,
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
