/**
 * COSMOS Bridge — shared chat surface (Phase 3 native embed).
 *
 * Extracted from bridge.html so the unified dashboard can mount the chat
 * widget directly (no iframe) while the standalone page stays available.
 *
 * Usage:
 *   initCosmosBridge(document.getElementById('bridge-app'), { api, token });
 *
 * Conversation state persists per browser origin in localStorage
 * (`cosmos.bridge.session`); the server archives exchanges to
 * `rack/bridge/sessions/<id>.jsonl` and resumes via GET /api/sessions/:id.
 */
(function () {
  'use strict';

  var INST = 0;

  function esc(s) {
    return String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
  }

  function el(tag, cls, html) {
    var e = document.createElement(tag);
    if (cls) e.className = cls;
    if (html != null) e.innerHTML = html;
    return e;
  }

  // markdown-lite: code fences, inline code, bold, italic, lists, links
  function render(md) {
    var out = esc(md);
    var blocks = [];
    out = out.replace(/```(\w*)\n([\s\S]*?)```/g, function (_, lang, code) {
      blocks.push('<pre><code>' + esc(code.trim()) + '</code></pre>');
      return '\u0000B' + (blocks.length - 1) + '\u0000';
    });
    out = out.replace(/\*\*([^*]+)\*\*/g, '<strong>$1</strong>')
      .replace(/\*([^*\n]+)\*/g, '<em>$1</em>')
      .replace(/`([^`]+)`/g, '<code>$1</code>')
      .replace(/\[([^\]]+)\]\((https?:\/\/[^)]+)\)/g, '<a href="$2" target="_blank" rel="noopener">$1</a>');
    out = out.split('\n').map(function (l) {
      if (/^\s*[-*] /.test(l)) return '<li>' + l.replace(/^\s*[-*] /, '') + '</li>';
      if (/^\s*\d+\. /.test(l)) return '<li>' + l.replace(/^\s*\d+\. /, '') + '</li>';
      return l;
    }).join('\n');
    out = out.replace(/(<li>[\s\S]*?<\/li>)/g, function (m) { return '<ul>' + m + '</ul>'; });
    out = out.replace(/\u0000B(\d+)\u0000/g, function (_, i) { return blocks[+i]; });
    return out.replace(/\n{3,}/g, '\n\n');
  }

  function newSessionId() {
    var rand = Math.random().toString(36).slice(2, 8);
    return 's-' + Date.now().toString(36) + '-' + rand;
  }

  function fmtSize(n) {
    return n >= 1024 * 1024 ? (n / 1024 / 1024).toFixed(1) + ' MB' : Math.max(1, Math.round(n / 1024)) + ' KB';
  }

  function fmtDur(ms) {
    if (ms == null) return '—';
    if (ms < 1000) return ms + 'ms';
    return (ms / 1000).toFixed(1) + 's';
  }

  function fmtTime(iso) {
    var d = iso ? new Date(iso) : new Date();
    return d.toTimeString().slice(0, 8);
  }

  function initCosmosBridge(root, opts) {
    if (!root) throw new Error('initCosmosBridge: missing root element');
    opts = opts || {};
    var API = opts.api || '';
    var TOKEN = opts.token || '';
    var inst = 'cb' + (INST++);
    var sessionKey = 'cosmos.bridge.session';
    var sessionId = localStorage.getItem(sessionKey) || newSessionId();
    localStorage.setItem(sessionKey, sessionId);
    var hist = [];
    var attach = [];
    var ATTACH_BUDGET = 4 * 1024 * 1024; // raw bytes; base64 inflates ~1.33x, server caps POST at 6 MB
    var liveOpen = false;
    var cycleIds = {};
    var FEED_MAX = 80;

    // ── styles (once per document) ─────────────────────────────────────
    if (!document.getElementById('cb-style')) {
      var st = el('style', '', [
        '#cb-style::-webkit-scrollbar{width:8px;height:8px}',
        '.cosmos-bridge .hide{display:none !important}',
        '.cosmos-bridge ::-webkit-scrollbar{width:8px;height:8px}',
        '.cosmos-bridge ::-webkit-scrollbar-thumb{background:#334155;border-radius:8px}',
        '.cosmos-bridge .msg p{margin:0 0 .5rem}',
        '.cosmos-bridge .msg pre{background:#0f172a;border:1px solid #334155;border-radius:.5rem;padding:.6rem .75rem;overflow-x:auto;font-size:.75rem;margin:.4rem 0}',
        '.cosmos-bridge .msg code{font-family:ui-monospace,monospace;font-size:.8em;background:#1e293b;padding:.1rem .3rem;border-radius:.3rem}',
        '.cosmos-bridge .msg pre code{background:transparent;padding:0}',
        '.cosmos-bridge .msg ul,.cosmos-bridge .msg ol{margin:.3rem 0 .5rem 1.2rem;list-style:disc}',
        '.cosmos-bridge .msg ol{list-style:decimal}',
        '.cosmos-bridge .msg a{color:#818cf8;text-decoration:underline}',
        '.cosmos-bridge .msg h1,.cosmos-bridge .msg h2,.cosmos-bridge .msg h3{font-weight:700;margin:.5rem 0 .3rem}',
        '.cosmos-bridge .msg h1{font-size:1rem}.cosmos-bridge .msg h2{font-size:.9rem}.cosmos-bridge .msg h3{font-size:.85rem}',
      ].join('\n'));
      st.id = 'cb-style';
      (document.head || document.documentElement).appendChild(st);
    }

    // ── layout ─────────────────────────────────────────────────────────
    root.classList.add('cosmos-bridge');
    root.style.cssText = 'display:flex;flex-direction:column;height:100%;min-height:480px;';
    root.innerHTML = [
      '<div class="flex items-center justify-between gap-3 mb-3 flex-wrap">',
      '  <div class="flex items-center gap-2">',
      '    <span class="text-lg">🌉</span>',
      '    <h1 class="text-base sm:text-lg font-bold">COSMOS Bridge</h1>',
      '    <span id="' + inst + '-st-bridge" class="text-[10px] font-bold px-2 py-0.5 rounded-full bg-amber-500/15 text-amber-400 border border-amber-500/25 uppercase">checking…</span>',
      '  </div>',
      '  <div class="flex items-center gap-2 flex-wrap">',
      '    <button id="' + inst + '-new" title="Start a new session (Ctrl+Shift+N)" class="text-[10px] font-semibold px-2 py-1 rounded-lg bg-slate-800/60 border border-slate-700/50 text-slate-300 hover:border-indigo-500/50 hover:text-indigo-300 transition">↺ new</button>',
      '    <span id="' + inst + '-st-model" class="text-[10px] font-mono text-slate-400 bg-slate-800/60 border border-slate-700/50 rounded-lg px-2 py-1">—</span>',
      '    <span id="' + inst + '-st-kg" class="text-[10px] font-mono text-slate-400 bg-slate-800/60 border border-slate-700/50 rounded-lg px-2 py-1">—</span>',
      '    <span id="' + inst + '-st-strat" class="text-[10px] font-mono text-slate-400 bg-slate-800/60 border border-slate-700/50 rounded-lg px-2 py-1">—</span>',
      '    <span id="' + inst + '-st-art" class="text-[10px] font-mono text-slate-400 bg-slate-800/60 border border-slate-700/50 rounded-lg px-2 py-1">📎 —</span>',
      '  </div>',
      '</div>',
      '<div class="flex items-center gap-2 mb-2">',
      '  <button id="' + inst + '-live-btn" class="text-[10px] sm:text-[11px] font-semibold px-2.5 py-1.5 rounded-lg bg-slate-800/60 border border-slate-700/50 text-slate-300 hover:border-indigo-500/50 hover:text-indigo-300 transition">🟢 <span id="' + inst + '-live-label">Show live</span></button>',
      '  <span id="' + inst + '-st-live" class="text-[9px] font-bold px-2 py-0.5 rounded-full border uppercase bg-slate-600/20 text-slate-400 border-slate-500/30">idle</span>',
      '  <span id="' + inst + '-live-hint" class="text-[10px] text-slate-500">telemetry → events → cards</span>',
      '</div>',
      '<div id="' + inst + '-live" class="hide mb-2 flex flex-col gap-2">',
      '  <div id="' + inst + '-live-cycles" class="flex gap-2 overflow-x-auto pb-1"></div>',
      '  <div id="' + inst + '-live-feed" class="bg-slate-900/50 border border-slate-800 rounded-xl overflow-y-auto text-[10px] font-mono leading-relaxed" style="max-height:24vh"></div>',
      '</div>',
      '<div id="' + inst + '-drives" class="mb-3"></div>',
      '<div id="' + inst + '-chat" class="flex-1 overflow-y-auto space-y-3 pr-1 pb-3"></div>',
      '<div id="' + inst + '-sugg" class="flex flex-wrap gap-1.5 mb-3"></div>',
      '<div id="' + inst + '-attachbar" class="flex flex-wrap gap-1.5 mb-2"></div>',
      '<form id="' + inst + '-form" class="flex items-end gap-2">',
      '  <label class="flex items-center gap-1.5 text-[10px] sm:text-xs text-slate-400 select-none shrink-0 pb-2 cursor-pointer hover:text-indigo-300 transition" title="Attach files — text/JSON/YAML/TOML inlined (8 KB preview), images/audio sent to the model (4 MB cap), PDFs text-extracted, video rejected">',
      '    <input id="' + inst + '-file" type="file" multiple class="hide" />📎 Attach',
      '  </label>',
      '  <label class="flex items-center gap-1.5 text-[10px] sm:text-xs text-slate-400 select-none shrink-0 pb-2 cursor-pointer" title="Include the live Cosmos snapshot in the prompt">',
      '    <input id="' + inst + '-ctx" type="checkbox" checked class="accent-indigo-500 h-3.5 w-3.5" />Cosmos ctx',
      '  </label>',
      '  <textarea id="' + inst + '-inp" rows="1" placeholder="Ask the bridge — system state, drives, plans, or a build task… (Ctrl+Enter send, Ctrl+K focus)"',
      '    class="flex-1 resize-none bg-slate-800/60 border border-slate-700/50 rounded-xl px-3 py-2.5 text-sm outline-none focus:border-indigo-500/60 placeholder:text-slate-500"',
      '    style="max-height:140px"></textarea>',
      '  <button type="submit" class="shrink-0 bg-indigo-500 hover:bg-indigo-400 text-white text-sm font-semibold rounded-xl px-4 py-2.5 transition">Send ↵</button>',
      '</form>',
    ].join('\n');

    var chat = document.getElementById(inst + '-chat');
    var sugg = document.getElementById(inst + '-sugg');
    var attachbar = document.getElementById(inst + '-attachbar');
    var inp = document.getElementById(inst + '-inp');
    var form = document.getElementById(inst + '-form');
    var fileInput = document.getElementById(inst + '-file');
    var ctxCheck = document.getElementById(inst + '-ctx');

    function scroll() { chat.scrollTop = chat.scrollHeight; }

    function addMsg(role, text, chips, push) {
      if (push !== false) hist.push({ role: role, content: text });
      var wrap = el('div', 'flex ' + (role === 'user' ? 'justify-end' : 'justify-start'));
      var cls = role === 'user'
        ? 'max-w-[85%] bg-indigo-500/20 border border-indigo-500/40 text-indigo-50 rounded-2xl rounded-br-md px-3.5 py-2.5 text-sm'
        : 'max-w-[92%] bg-slate-800/60 border border-slate-700/50 text-slate-200 rounded-2xl rounded-bl-md px-3.5 py-2.5 text-sm msg';
      var b = el('div', cls);
      if (role === 'assistant') b.innerHTML = render(text);
      else b.textContent = text;
      if (chips && chips.length) {
        var row = el('div', 'flex flex-wrap gap-1 mt-1.5');
        chips.forEach(function (n) {
          row.appendChild(el('span', 'text-[9px] px-1.5 py-0.5 rounded bg-slate-900/70 border border-slate-600/40 text-slate-300', '📎 ' + esc(n)));
        });
        b.appendChild(row);
      }
      wrap.appendChild(b);
      chat.appendChild(wrap);
      scroll();
      return b;
    }

    function attachTotal() { return attach.reduce(function (s, a) { return s + a.size; }, 0); }

    function renderAttach() {
      attachbar.innerHTML = '';
      attach.forEach(function (a, i) {
        var c = el('span', 'inline-flex items-center gap-1 text-[10px] px-2 py-1 rounded-lg bg-slate-800/80 border border-slate-600/40 text-slate-200');
        c.innerHTML = '📎 ' + esc(a.name) + ' <span class="text-slate-400">' + fmtSize(a.size) + '</span>';
        var x = el('button', 'text-slate-400 hover:text-rose-400 ml-0.5 cursor-pointer', '✕');
        x.onclick = function () { attach.splice(i, 1); renderAttach(); };
        c.appendChild(x);
        attachbar.appendChild(c);
      });
      if (attachTotal() > ATTACH_BUDGET) {
        attachbar.appendChild(el('span', 'text-[10px] text-rose-400', '⚠ ' + fmtSize(attachTotal()) + ' over the ' + fmtSize(ATTACH_BUDGET) + ' bridge budget — remove attachments or send in parts.'));
      }
    }

    function chip(label) {
      var c = el('button', 'text-[10px] sm:text-[11px] px-2.5 py-1.5 rounded-lg bg-slate-800/60 border border-slate-700/50 text-slate-300 hover:border-indigo-500/50 hover:text-indigo-300 transition', esc(label));
      c.onclick = function () { inp.value = label; autosize(); send(); };
      sugg.appendChild(c);
    }

    function setStatus(id, text, color) {
      var e = document.getElementById(inst + '-' + id);
      if (!e) return;
      e.textContent = text;
      e.className = 'text-[10px] font-bold px-2 py-0.5 rounded-full border uppercase ' + (color || 'bg-slate-600/20 text-slate-400 border-slate-500/30');
    }

    function autosize() {
      inp.style.height = 'auto';
      inp.style.height = Math.min(140, inp.scrollHeight) + 'px';
    }

    // ── live state streaming (Phase 1) ─────────────────────────────────
    function setLiveDot(state) {
      var b = document.getElementById(inst + '-st-live');
      b.textContent = state === 'live' ? '● live' : state === 'connecting' ? '… conn' : 'offline';
      b.className = 'text-[9px] font-bold px-2 py-0.5 rounded-full border uppercase ' +
        (state === 'live' ? 'bg-emerald-500/15 text-emerald-400 border-emerald-500/25'
          : state === 'connecting' ? 'bg-amber-500/15 text-amber-400 border-amber-500/25'
            : 'bg-rose-500/15 text-rose-400 border-rose-500/25');
    }

    function toggleLive() {
      var panel = document.getElementById(inst + '-live');
      liveOpen = !liveOpen;
      panel.classList.toggle('hide', !liveOpen);
      document.getElementById(inst + '-live-label').textContent = liveOpen ? 'Hide live' : 'Show live';
      document.getElementById(inst + '-live-hint').textContent = liveOpen ? 'streaming ●' : 'telemetry → events → cards';
    }

    function cycleCard(c) {
      var kg = c.kg ? c.kg.nodes + 'n/' + c.kg.edges + 'e' : 'KG —';
      var strat = c.strategies ? 'gen ' + c.strategies.generation + ' · fit ' + (c.strategies.best_fitness != null ? c.strategies.best_fitness : '—') : 'strat —';
      var l3 = c.l3 ? 'L3 #' + (c.cycle != null ? c.cycle : '?') + ' · ' + (c.l3.insights != null ? c.l3.insights + ' ins' : '') + (c.l3.strategies != null ? ' / ' + c.l3.strategies + ' strat' : '') : 'L3 —';
      var row = el('div', 'shrink-0 w-52 rounded-xl bg-slate-800/60 border border-slate-700/50 p-2 space-y-0.5');
      row.innerHTML =
        '<div class="flex items-center justify-between text-[10px] font-bold">' +
        '<span class="text-indigo-300">#' + esc(c.id || c.cycle || '?') + '</span>' +
        '<span class="text-[9px] text-slate-400">' + fmtTime(c.ts) + '</span></div>' +
        '<div class="text-[9px] text-slate-300">' + esc(l3) + '</div>' +
        '<div class="text-[9px] text-slate-400">' + esc(kg) + '</div>' +
        '<div class="text-[9px] text-slate-400">' + esc(strat) + '</div>' +
        '<div class="flex items-center justify-between text-[9px] text-slate-500">' +
        '<span>' + fmtDur(c.duration_ms) + ' · rc ' + (c.rc != null ? c.rc : '—') + '</span>' +
        '<span class="text-emerald-400">●</span></div>';
      return row;
    }

    function addCycle(c) {
      if (!c || cycleIds[c.id]) return;
      cycleIds[c.id] = true;
      var box = document.getElementById(inst + '-live-cycles');
      box.insertBefore(cycleCard(c), box.firstChild);
      while (box.children.length > 8) box.removeChild(box.lastChild);
    }

    function addActivity(rec) {
      if (!rec) return;
      var feed = document.getElementById(inst + '-live-feed');
      var d = rec.data || {};
      var what = rec.event.replace(/^telemetry\./, '');
      var extra = '';
      if (rec.event === 'cycle.complete') extra = ' · L3 #' + (d.cycle != null ? d.cycle : '?') + ' · KG ' + (d.kg ? d.kg.nodes + 'n' : '—');
      else if (rec.event.indexOf('state.') === 0) {
        var k = rec.event.slice(6);
        if (k === 'kg') extra = ' · ' + d.nodes + 'n/' + d.edges + 'e';
        else if (k === 'strategies') extra = ' · gen ' + d.generation + ' · fit ' + d.best_fitness;
        else if (k === 'goals') extra = ' · ' + (d.status || '');
        else if (k === 'pulses') extra = ' · #' + d.pulse + ' ' + (d.type || '');
      } else if (rec.event.indexOf('telemetry.') === 0) {
        if (what === 'l3_complete') extra = ' · cycle ' + d.cycle + ' · ' + (d.insights != null ? d.insights + ' ins' : '');
        else if (what === 'l5_complete') extra = ' · gen ' + d.generation + ' · fit ' + d.avg_fitness;
        else if (what === 'sa_complete') extra = ' · health ' + d.health_score;
        else if (what === 'l2_complete') extra = ' · success=' + d.success;
        else if (what === 'l1_complete') extra = ' · success=' + d.success;
      }
      var line = el('div', 'px-2 py-0.5 border-b border-slate-800/50 flex gap-2');
      line.innerHTML = '<span class="text-slate-600 shrink-0">' + fmtTime(rec.ts) + '</span>' +
        '<span class="' + (rec.event.indexOf('cycle.complete') === 0 ? 'text-emerald-400' : rec.event.indexOf('state.') === 0 ? 'text-amber-300' : 'text-indigo-300') + ' shrink-0">' + esc(what) + '</span>' +
        '<span class="text-slate-400 truncate">' + esc(extra || '') + '</span>';
      feed.insertBefore(line, feed.firstChild);
      while (feed.children.length > FEED_MAX) feed.removeChild(feed.lastChild);
    }

    function openSSE() {
      if (!window.EventSource) return;
      var url = API + '/api/events';
      if (TOKEN) url += (url.indexOf('?') >= 0 ? '&' : '?') + 'token=' + encodeURIComponent(TOKEN);
      var es = new EventSource(url);
      setLiveDot('connecting');
      es.onopen = function () { setLiveDot('live'); };
      es.onerror = function () { setLiveDot('offline'); };
      es.onmessage = function (m) {
        try { addActivity(JSON.parse(m.data)); } catch (e) { /* ignore */ }
      };
      ['cycle.complete', 'state.goals', 'state.strategies', 'state.kg', 'state.pulses'].forEach(function (evt) {
        es.addEventListener(evt, function (m) {
          var rec;
          try { rec = JSON.parse(m.data); } catch (e) { return; }
          addActivity(rec);
          if (evt === 'cycle.complete') addCycle(rec.data);
          if (evt === 'state.kg') {
            var d = rec.data || {};
            document.getElementById(inst + '-st-kg').textContent = 'KG ' + d.nodes + 'n/' + d.edges + 'e';
          }
          if (evt === 'state.strategies') {
            var d2 = rec.data || {};
            document.getElementById(inst + '-st-strat').textContent = 'gen ' + d2.generation + ' · fit ' + (d2.best_fitness != null ? d2.best_fitness : '—');
          }
        });
      });
    }

    async function loadCycles() {
      try {
        var r = await fetch(API + '/api/cycles?limit=12', authHeaders());
        if (!r.ok) return;
        var d = await r.json();
        (d.cycles || []).forEach(addCycle);
      } catch (e) { /* bridge may be offline */ }
    }

    async function loadCosmos() {
      try {
        var r = await fetch(API + '/api/cosmos', authHeaders());
        if (!r.ok) throw new Error('HTTP ' + r.status);
        var c = await r.json();
        setStatus('st-bridge', c.llm === 'connected' ? '● live' : '● offline-fallback',
          c.llm === 'connected' ? 'bg-emerald-500/15 text-emerald-400 border-emerald-500/25' : 'bg-amber-500/15 text-amber-400 border-amber-500/25');
        document.getElementById(inst + '-st-model').textContent = c.model || '—';
        document.getElementById(inst + '-st-kg').textContent = 'KG ' + (c.kg ? c.kg.nodes + 'n/' + c.kg.edges + 'e' : '—');
        document.getElementById(inst + '-st-strat').textContent = 'gen ' + (c.strategies ? c.strategies.generation : '—') + ' · fit ' + (c.strategies && c.strategies.best_fitness != null ? c.strategies.best_fitness : '—');
        document.getElementById(inst + '-st-art').textContent = '📎 ' + (c.artifacts ? c.artifacts.length : 0) + ' refs';
        var dr = document.getElementById(inst + '-drives');
        if (c.drives && c.drives.tiers && c.drives.tiers.length) {
          dr.innerHTML = '<div class="bg-slate-800/60 border border-slate-700/50 rounded-xl p-2.5 sm:p-3">' +
            '<div class="flex items-center gap-2 mb-1.5"><span class="text-[10px] font-bold text-indigo-400 uppercase">🧭 Active drives</span>' +
            '<span class="text-[9px] font-bold px-1.5 py-0.5 rounded-full bg-indigo-500/15 text-indigo-400 border border-indigo-500/25 uppercase">' + esc(c.drives.status) + '</span></div>' +
            '<div class="flex flex-wrap gap-1.5">' + c.drives.tiers.map(function (t) {
              return '<span class="text-[10px] px-2 py-1 rounded-lg bg-slate-700/40 border border-slate-600/40 text-slate-300">T' + t.tier + ' ' + esc(t.name) + '</span>';
            }).join('') + '</div></div>';
          c.drives.tiers.forEach(function (t) { chip('T' + t.tier + ' — ' + t.name); });
        }
        chip('Summarize current system state');
        chip('What are the active drives and next steps?');
        chip('Explain the goal stack');
        return c;
      } catch (e) {
        setStatus('st-bridge', 'offline', 'bg-rose-500/15 text-rose-400 border-rose-500/25');
        addMsg('assistant', '⚠ Bridge API unreachable (' + esc(e.message) + ').\n\nStart it with:\n\n```bash\ncd components/rsis3 && node rack/bridge/server.mjs\n```');
        return null;
      }
    }

    function authHeaders(extra) {
      var h = Object.assign({ 'Content-Type': 'application/json' }, extra || {});
      if (TOKEN) h['Authorization'] = 'Bearer ' + TOKEN;
      return h;
    }

    // ── session persistence / resume (Phase 3) ─────────────────────────
    async function resumeSession() {
      try {
        var r = await fetch(API + '/api/sessions/' + encodeURIComponent(sessionId), authHeaders());
        if (!r.ok) return;
        var sess = await r.json();
        if (!sess || !sess.messages || !sess.messages.length) return;
        chat.innerHTML = '';
        hist = [];
        sess.messages.forEach(function (m) {
          addMsg(m.role, m.content, (m.artifacts || []).map(function (a) { return a.name || a.ref; }).filter(Boolean), false);
        });
        addMsg('assistant', 'Resumed session `' + sess.id + '` (' + sess.count + ' exchanges). Ask away.');
      } catch (e) { /* first visit or bridge offline */ }
    }

    function newSession() {
      sessionId = newSessionId();
      localStorage.setItem(sessionKey, sessionId);
      hist = [];
      chat.innerHTML = '';
      attach = [];
      renderAttach();
      addMsg('assistant', 'New session started (`' + sessionId + '`).');
      inp.focus();
    }

    // ── chat send (streaming NDJSON, Phase 2) ───────────────────────────
    async function send() {
      var q = inp.value.trim();
      var total = attachTotal();
      if (!q && !attach.length) return;
      if (total > ATTACH_BUDGET) { alert('Attachments exceed the bridge budget (' + fmtSize(ATTACH_BUDGET) + '). Remove some and retry.'); return; }
      inp.value = '';
      autosize();
      addMsg('user', q, attach.map(function (a) { return a.name; }));
      var typing = addMsg('assistant', '…');
      typing.innerHTML = '<span class="text-slate-400">thinking…</span>';
      var payload = { messages: hist, cosmos: ctxCheck.checked, session_id: sessionId };
      if (attach.length) payload.artifacts = attach.map(function (a) { return { name: a.name, type: a.type, size: a.size, dataUrl: a.dataUrl }; });
      attach = [];
      renderAttach();
      function settle(reply) {
        typing.innerHTML = render(reply);
        hist = hist.filter(function (x) { return x.role === 'assistant' && x.content !== '…'; });
        hist.push({ role: 'assistant', content: reply });
        scroll();
      }
      try {
        var r = await fetch(API + '/api/chat', {
          method: 'POST',
          headers: authHeaders({ 'Accept': 'application/x-ndjson' }),
          body: JSON.stringify(payload),
        });
        if (!r.ok) {
          var errText = 'HTTP ' + r.status;
          try { var e = await r.json(); errText = e.error || errText; } catch (e2) { /* non-JSON error */ }
          if (r.status === 429) errText += ' — retry in ' + (r.headers.get('Retry-After') || '60') + 's';
          throw new Error(errText);
        }
        var ctype = (r.headers.get('Content-Type') || '').split(';')[0].trim();
        if (ctype === 'application/x-ndjson') {
          var acc = '';
          var buf = '';
          var settled = false;
          var reader = r.body.getReader();
          var dec = new TextDecoder();
          for (;;) {
            var res = await reader.read();
            if (res.done) break;
            buf += dec.decode(res.value, { stream: true });
            var nl;
            while ((nl = buf.indexOf('\n')) >= 0) {
              var line = buf.slice(0, nl);
              buf = buf.slice(nl + 1);
              if (!line.trim()) continue;
              var m;
              try { m = JSON.parse(line); } catch (e3) { continue; }
              if (m.type === 'delta') { acc += m.text; typing.innerHTML = render(acc); scroll(); }
              else if (m.type === 'done') { acc = m.reply || acc; if (!settled) { settled = true; settle(acc); } }
              else if (m.type === 'error') { throw new Error(m.message || 'stream error'); }
            }
          }
          if (!acc) throw new Error('empty stream reply');
          if (!settled) settle(acc);
        } else {
          var d = await r.json();
          settle(d.reply);
        }
      } catch (e) {
        typing.innerHTML = render('⚠ Request failed: ' + esc(e.message));
        hist = hist.filter(function (x) { return x.role === 'assistant' && x.content !== '…'; });
        scroll();
      }
    }

    // ── events ─────────────────────────────────────────────────────────
    form.addEventListener('submit', function (e) { e.preventDefault(); send(); });
    inp.addEventListener('input', autosize);
    document.getElementById(inst + '-live-btn').addEventListener('click', toggleLive);
    document.getElementById(inst + '-new').addEventListener('click', newSession);
    fileInput.addEventListener('change', function () {
      var files = Array.prototype.slice.call(this.files || []);
      var pending = attach.slice();
      files.forEach(function (f) {
        if (f.size > 4 * 1024 * 1024) { alert(f.name + ' exceeds the 4 MB per-file limit.'); return; }
        if (attachTotal() + f.size > ATTACH_BUDGET) { alert(f.name + ' would exceed the bridge budget (' + fmtSize(ATTACH_BUDGET) + '). Remove attachments or send in parts.'); return; }
        var reader = new FileReader();
        reader.onload = (function (file) {
          return function (evt) {
            attach.push({ name: file.name, type: file.type || 'application/octet-stream', size: file.size, dataUrl: evt.target.result });
            renderAttach();
          };
        })(f);
        reader.readAsDataURL(f);
      });
      this.value = '';
    });
    inp.addEventListener('keydown', function (e) {
      if (e.key === 'Enter' && (e.ctrlKey || e.metaKey)) { e.preventDefault(); send(); }
      else if (e.key === 'Enter' && !e.shiftKey) { e.preventDefault(); send(); }
    });
    document.addEventListener('keydown', function (e) {
      if ((e.ctrlKey || e.metaKey) && (e.key === 'k' || e.key === 'K') && !e.shiftKey) { e.preventDefault(); inp.focus(); }
    });

    // ── boot ───────────────────────────────────────────────────────────
    loadCycles();
    openSSE();
    loadCosmos().then(function (c) {
      resumeSession();
      if (c && c.llm !== 'connected') {
        addMsg('assistant', 'Bridge is in **offline-fallback** mode (no `GEMINI_API_KEY` on the server). Replies are deterministic cosmos envelopes — start the server with a key for real LLM answers.');
      } else if (c) {
        addMsg('assistant', 'Bridge online — I can read the live Cosmos snapshot (KG, strategies, pulses, syntheses) and the active drive stack. Ask about system state, plan the next tier, or describe a build task.');
      }
    });

    return {
      api: API,
      sessionId: sessionId,
      newSession: newSession,
      send: send,
    };
  }

  if (typeof window !== 'undefined') window.initCosmosBridge = initCosmosBridge;
  if (typeof module !== 'undefined' && module.exports) module.exports = { initCosmosBridge: initCosmosBridge };
})();
