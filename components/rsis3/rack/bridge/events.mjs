/**
 * COSMOS Bridge — Phase 1 live state streaming (completes tier T1).
 *
 * SSE event hub + poll-based watchers that turn RSIS loop writes into typed
 * events:
 *   - telemetry lines  → `telemetry.<type>`  (e.g. telemetry.l3_complete)
 *   - state-file edits → `state.<key>`       (goals / strategies / kg / pulses)
 *   - finished cycles  → `cycle.complete`    (derived summary, archived)
 *
 * Pure Node stdlib — no dependencies. Poll interval is 2 s so telemetry
 * deltas appear in the dashboard within the Phase-1 exit criterion (<2 s).
 */
import { readFile, readdir, stat, appendFile, mkdir } from 'node:fs/promises';
import path from 'node:path';

export const POLL_MS = 2000;
const HISTORY_MAX = 200;
const HEARTBEAT_MS = 15000;

const json = (s) => { try { return JSON.parse(s); } catch { return null; } };

// ── SSE hub ─────────────────────────────────────────────────────────────

export class EventHub {
  constructor() {
    this.clients = new Set();
    this.history = [];
    this.seq = 0;
  }

  emit(event, data) {
    const rec = { id: ++this.seq, ts: new Date().toISOString(), event, data };
    this.history.push(rec);
    if (this.history.length > HISTORY_MAX) this.history.shift();
    const frame = `id: ${rec.id}\nevent: ${event}\ndata: ${JSON.stringify(rec)}\n\n`;
    for (const res of this.clients) {
      try { res.write(frame); } catch { this.clients.delete(res); }
    }
    if (event === 'cycle.complete' || event.startsWith('state.')) {
      console.log(`[bridge:events] ${event}`, JSON.stringify(data).slice(0, 200));
    }
    return rec;
  }

  addClient(req, res) {
    res.writeHead(200, {
      'Content-Type': 'text/event-stream',
      'Cache-Control': 'no-store',
      Connection: 'keep-alive',
      'Access-Control-Allow-Origin': '*',
      'X-Accel-Buffering': 'no',
    });
    res.write('retry: 3000\n\n');
    for (const rec of this.history) {
      res.write(`id: ${rec.id}\nevent: ${rec.event}\ndata: ${JSON.stringify(rec)}\n\n`);
    }
    this.clients.add(res);
    const hb = setInterval(() => { try { res.write(': ping\n\n'); } catch {} }, HEARTBEAT_MS);
    hb.unref?.();
    const drop = () => { clearInterval(hb); this.clients.delete(res); };
    req.on('close', drop);
    res.on('close', drop);
    return res;
  }
}

// ── state-file watchers ─────────────────────────────────────────────────

const STATE_FILES = [
  {
    key: 'goals',
    rel: ['rack', 'goals_stack.json'],
    pick: (o) => ({
      id: o.id,
      title: o.title,
      status: o.status,
      tiers: (o.tiers || []).map((t) => ({ tier: t.tier, name: t.name })),
    }),
  },
  {
    key: 'strategies',
    rel: ['.rsis', 'strategies.json'],
    pick: (o) => {
      const pop = o.population || [];
      const best = pop.reduce((b, s) => (s.fitness > (b?.fitness ?? -1) ? s : b), null);
      return {
        generation: o.generation || 0,
        population: pop.length,
        best_fitness: best?.fitness ?? null,
      };
    },
  },
  {
    key: 'kg',
    rel: ['.rsis', 'knowledge_graph.json'],
    pick: (o) => ({ nodes: (o.nodes || []).length, edges: (o.edges || []).length }),
  },
  {
    key: 'pulses',
    rel: ['rack', 'pulses', 'latest.json'],
    pick: (o) => ({ pulse: o.pulse, type: o.type, protocol: o.protocol }),
  },
];

/** Emit `state.<key>` whenever a tracked state file changes (mtime+size). */
export function startStateWatchers({ root, hub }) {
  const last = new Map();
  let running = false;
  const timer = setInterval(async () => {
    if (running) return; // never overlap ticks
    running = true;
    try {
      for (const f of STATE_FILES) {
        const abs = path.join(root, ...f.rel);
        try {
          const [s, raw] = await Promise.all([stat(abs), readFile(abs, 'utf8')]);
          const sig = `${s.mtimeMs}:${s.size}`;
          if (last.get(f.key) === sig) continue;
          last.set(f.key, sig);
          const o = json(raw);
          if (!o) continue;
          hub.emit('state.' + f.key, { file: f.rel.join('/'), ...f.pick(o) });
        } catch { /* file absent or mid-write — try next tick */ }
      }
    } catch (e) { console.error('[bridge] state watcher:', e.message); }
    finally { running = false; }
  }, POLL_MS);
  timer.unref?.();
  return timer;
}

// ── telemetry watcher + cycle derivation ────────────────────────────────

const CYCLE_END_TYPES = new Set(['l3_complete', 'sa_complete']);

/**
 * Derive a compact per-cycle summary from one telemetry file. rc is 0 once
 * the file contains a completion marker (l3_complete / sa_complete) — the
 * RSIS engine only writes those on successful completion.
 */
function deriveCycle(rec) {
  const ev = rec.events;
  const firstTs = ev[0]?.ts, lastTs = ev[ev.length - 1]?.ts;
  const l3 = ev.find((e) => e.type === 'l3_complete') || null;
  const l5 = ev.find((e) => e.type === 'l5_complete') || null;
  const l2 = ev.find((e) => e.type === 'l2_complete') || null;
  const sa = ev.find((e) => e.type === 'sa_complete') || null;
  return {
    id: (rec.name.split('_')[0] || 'cycle').slice(0, 8),
    file: rec.name,
    ts: lastTs || new Date().toISOString(),
    cycle: l3?.cycle ?? null,
    status: 'complete',
    rc: 0,
    duration_ms: firstTs && lastTs ? Date.parse(lastTs) - Date.parse(firstTs) : null,
    l1_failures: ev.filter((e) => e.type === 'l1_complete' && e.success === false).length,
    l2_success: l2 ? l2.success === true : null,
    l3: l3
      ? {
          insights: l3.insights ?? null,
          strategies: l3.strategies ?? null,
          redundancies: l3.redundancies ?? null,
          trends: l3.trends ?? null,
        }
      : null,
    l5: l5
      ? {
          generation: l5.generation ?? null,
          population: l5.population ?? null,
          avg_fitness: l5.avg_fitness ?? null,
          best: l5.best ?? null,
        }
      : null,
    sa: sa
      ? { health_score: sa.health_score ?? null, assessment: sa.assessment ?? null, gaps: (sa.gaps || []).length }
      : null,
  };
}

/**
 * Watch `.rsis/telemetry/*.jsonl` for appends. Emits `telemetry.<type>` per
 * line and `cycle.complete` once a file contains a completion marker and
 * stops growing for a full poll tick.
 */
export function startTelemetryWatcher({ dir, hub, onCycleComplete }) {
  const files = new Map(); // name -> { offset, events, lastSize, quiet, backlog }
  let boot = true; // first tick = historical backlog: archive silently, no live emit
  let running = false;
  const timer = setInterval(async () => {
    if (running) return; // never overlap ticks (backlog scans take >1 tick)
    running = true;
    try {
    let names;
    try { names = (await readdir(dir)).filter((n) => n.endsWith('.jsonl')).sort(); } catch { running = false; return; }
    for (const name of names) {
      const abs = path.join(dir, name);
      let st;
      try { st = await stat(abs); } catch { continue; }
      let rec = files.get(name);
      if (!rec) { rec = { name, offset: 0, events: [], lastSize: -1, quiet: 0, backlog: boot }; files.set(name, rec); }

      if (st.size > rec.offset) {
        try {
          const buf = await readFile(abs, 'utf8');
          let tail = buf.slice(rec.offset);
          rec.offset = buf.length;
          let lines = tail.split('\n');
          if (!tail.endsWith('\n') && lines.length) rec.offset -= lines.pop().length; // hold back partial line
          for (const line of lines) {
            const o = json(line);
            if (!o || !o.type) continue;
            const evt = { file: name, ts: o.timestamp || new Date().toISOString(), ...o };
            rec.events.push(evt);
            if (!rec.backlog) hub.emit('telemetry.' + o.type, evt);
          }
        } catch { /* partial read — retry next tick */ }
      }

      const hasEnd = rec.events.some((e) => CYCLE_END_TYPES.has(e.type));
      rec.quiet = st.size === rec.lastSize ? rec.quiet + 1 : 0;
      rec.lastSize = st.size;
      if (hasEnd && st.size === rec.offset && rec.quiet >= 1) {
        const summary = deriveCycle(rec);
        if (!rec.backlog) hub.emit('cycle.complete', summary);
        if (onCycleComplete) onCycleComplete(summary);
        rec.sealed = true;
        rec.quiet = -1e9; // seal — never re-emit
      }
    }
    boot = false;
    // bound memory: cap per-file event history. Never delete recs — a deleted
    // rec would be re-created with backlog=false and re-emit its whole file.
    for (const rec of files.values()) {
      if (rec.events.length > 500) rec.events.splice(0, rec.events.length - 500);
    }
    } catch (e) { console.error('[bridge] telemetry watcher:', e.message); }
    finally { running = false; }
  }, POLL_MS);
  timer.unref?.();
  return timer;
}

// ── cycle archive ───────────────────────────────────────────────────────

/** Append a cycle summary to rack/bridge/cycles/<YYYY-MM-DD>.jsonl (idempotent per cycle id). */
export async function appendCycle(cyclesDir, summary) {
  try { await mkdir(cyclesDir, { recursive: true }); } catch {}
  const day = (summary.ts || new Date().toISOString()).slice(0, 10);
  const file = path.join(cyclesDir, day + '.jsonl');
  try {
    let exists = false;
    try {
      const raw = await readFile(file, 'utf8');
      exists = raw.split('\n').some((l) => { const o = json(l); return !!o && o.id === summary.id; });
    } catch { /* new file */ }
    if (!exists) await appendFile(file, JSON.stringify(summary) + '\n');
  } catch (e) { console.error('[bridge] cycle archive write failed:', e.message); }
}

/** Return the most recent cycle summaries across archive files (newest first). */
export async function recentCycles(cyclesDir, limit = 20) {
  const out = [];
  try {
    const files = (await readdir(cyclesDir)).filter((f) => f.endsWith('.jsonl')).sort().reverse().slice(0, 14);
    for (const f of files) {
      const raw = await readFile(path.join(cyclesDir, f), 'utf8');
      for (const line of raw.split('\n')) {
        const o = json(line);
        if (o) out.push(o);
      }
    }
  } catch { /* no archive yet */ }
  out.sort((a, b) => Date.parse(b.ts || 0) - Date.parse(a.ts || 0));
  return out.slice(0, limit);
}
