import { createServer } from 'http';
import { readFileSync, writeFileSync, existsSync, mkdirSync, readdirSync } from 'fs';
import { join, dirname } from 'path';
import { fileURLToPath } from 'url';
import { createSpace } from '../dist/engine/core.js';
import { exportSession, exportToFiles } from '../dist/export/index.js';
import { FileSystemStorage } from '../dist/storage/filesystem.js';
import { DEFAULT_CONFIG } from '../dist/config/defaults.js';

const __dirname = dirname(fileURLToPath(import.meta.url));
const PORT = parseInt(process.argv[2] || '8888');
const PROJECTS_DIR = DEFAULT_CONFIG.projects_dir;

// Initialize engine and storage
const space = createSpace();
const storage = new FileSystemStorage(PROJECTS_DIR);

// CORS headers
function cors(res) {
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'GET, POST, OPTIONS');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type');
}

// JSON response
function json(res, data, status = 200) {
  cors(res);
  res.writeHead(status, { 'Content-Type': 'application/json' });
  res.end(JSON.stringify(data));
}

// Read request body
function readBody(req) {
  return new Promise((resolve) => {
    let body = '';
    req.on('data', chunk => body += chunk);
    req.on('end', () => {
      try { resolve(JSON.parse(body)); }
      catch { resolve({}); }
    });
  });
}

// Route matching
function matchRoute(method, url, pattern) {
  if (req_method !== method) return null;
  const patternParts = pattern.split('/');
  const urlParts = url.split('/');
  if (patternParts.length !== urlParts.length) return null;
  const params = {};
  for (let i = 0; i < patternParts.length; i++) {
    if (patternParts[i].startsWith(':')) {
      params[patternParts[i].slice(1)] = decodeURIComponent(urlParts[i]);
    } else if (patternParts[i] !== urlParts[i]) return null;
  }
  return params;
}

let req_method = '';

const server = createServer(async (req, res) => {
  req_method = req.method;
  // CORS preflight: respond 204 with the allow headers so cross-origin
  // embeds (e.g. the Cosmos dashboard iframe) can POST/OPTIONS.
  if (req.method === 'OPTIONS') {
    cors(res);
    res.writeHead(204);
    res.end();
    return;
  }
  const url = req.url.split('?')[0];
  
  try {
    // ── Framework ──
    if (req.method === 'GET' && url === '/api/framework') {
      const fw = space.framework;
      return json(res, {
        meta: fw.meta,
        series: fw.series.map(s => ({
          id: s.id,
          name: s.name,
          description: s.description,
          depends_on: s.depends_on,
          rounds: s.rounds.length,
          total_open_ended: s.total_open_ended,
          total_multi_choice: s.total_multi_choice,
        })),
      });
    }

    // ── Framework detail (full questions) ──
    if (req.method === 'GET' && url === '/api/framework/full') {
      const fw = space.framework;
      return json(res, {
        meta: fw.meta,
        series: fw.series.map(s => ({
          id: s.id,
          name: s.name,
          description: s.description,
          depends_on: s.depends_on,
          rounds: s.rounds.map(r => ({
            round: r.round,
            focus: r.focus,
            open_ended: r.open_ended.map(q => ({
              id: q.id,
              text: q.text,
              follow_up_choices: q.follow_up_choices,
            })),
          })),
        })),
      });
    }

    // ── Projects ──
    if (req.method === 'GET' && url === '/api/projects') {
      const projectsDir = PROJECTS_DIR;
      if (!existsSync(projectsDir)) return json(res, []);
      const dirs = readdirSync(projectsDir, { withFileTypes: true }).filter(e => e.isDirectory());
      const projects = [];
      for (const d of dirs) {
        const metaPath = join(projectsDir, d.name, '.space.json');
        if (!existsSync(metaPath)) continue;
        const meta = JSON.parse(readFileSync(metaPath, 'utf-8'));
        // Count sessions
        const sessionsDir = join(projectsDir, d.name, 'sessions');
        let sessionCount = 0;
        let completedCount = 0;
        if (existsSync(sessionsDir)) {
          const sessions = readdirSync(sessionsDir, { withFileTypes: true }).filter(e => e.isDirectory());
          sessionCount = sessions.length;
          for (const s of sessions) {
            const statePath = join(sessionsDir, s.name, 'state.json');
            if (existsSync(statePath)) {
              const state = JSON.parse(readFileSync(statePath, 'utf-8'));
              if (state.session?.status === 'completed') completedCount++;
            }
          }
        }
        projects.push({
          id: meta.id,
          name: meta.name,
          description: meta.description,
          created_at: meta.created_at,
          updated_at: meta.updated_at,
          session_count: sessionCount,
          completed_sessions: completedCount,
        });
      }
      return json(res, projects);
    }

    // ── Create project ──
    if (req.method === 'POST' && url === '/api/projects') {
      const body = await readBody(req);
      const name = body.name?.trim();
      if (!name) return json(res, { error: 'Name required' }, 400);
      
      const projectDir = join(PROJECTS_DIR, name);
      if (existsSync(projectDir)) return json(res, { error: 'Project already exists' }, 409);
      
      mkdirSync(projectDir, { recursive: true });
      mkdirSync(join(projectDir, 'sessions'), { recursive: true });
      mkdirSync(join(projectDir, 'exports'), { recursive: true });
      
      const project = {
        id: `proj_${Date.now().toString(36)}`,
        name,
        description: body.description || '',
        created_at: new Date().toISOString(),
        updated_at: new Date().toISOString(),
        framework_version: '2.0.0',
        sessions: [],
        tags: [],
      };
      writeFileSync(join(projectDir, '.space.json'), JSON.stringify(project, null, 2));
      return json(res, { ok: true, project }, 201);
    }

    // ── Project detail ──
    const projectMatch = url.match(/^\/api\/projects\/([^/]+)$/);
    if (req.method === 'GET' && projectMatch) {
      const name = projectMatch[1];
      const metaPath = join(PROJECTS_DIR, name, '.space.json');
      if (!existsSync(metaPath)) return json(res, { error: 'Not found' }, 404);
      const meta = JSON.parse(readFileSync(metaPath, 'utf-8'));
      
      const sessionsDir = join(PROJECTS_DIR, name, 'sessions');
      const sessions = [];
      if (existsSync(sessionsDir)) {
        for (const d of readdirSync(sessionsDir, { withFileTypes: true })) {
          if (!d.isDirectory()) continue;
          const statePath = join(sessionsDir, d.name, 'state.json');
          if (!existsSync(statePath)) continue;
          const state = JSON.parse(readFileSync(statePath, 'utf-8'));
          sessions.push({
            id: d.name,
            status: state.session?.status,
            completion_pct: state.session?.estimated_completion_pct || 0,
            answers_count: Object.keys(state.answers || {}).length,
            created_at: state.session?.created_at,
            updated_at: state.session?.updated_at,
          });
        }
      }
      return json(res, { ...meta, sessions });
    }

    // ── Delete project ──
    if (req.method === 'DELETE' && projectMatch) {
      const name = projectMatch[1];
      const projectDir = join(PROJECTS_DIR, name);
      if (!existsSync(projectDir)) return json(res, { error: 'Not found' }, 404);
      const { rmSync } = await import('fs');
      rmSync(projectDir, { recursive: true, force: true });
      return json(res, { ok: true });
    }

    // ── Start session ──
    const startSessionMatch = url.match(/^\/api\/projects\/([^/]+)\/sessions$/);
    if (req.method === 'POST' && startSessionMatch) {
      const projectName = startSessionMatch[1];
      const body = await readBody(req);
      
      const session = space.startSession(projectName);
      
      // Save to disk
      const sessionsDir = join(PROJECTS_DIR, projectName, 'sessions');
      mkdirSync(join(sessionsDir, session.session.id), { recursive: true });
      writeFileSync(join(sessionsDir, session.session.id, 'state.json'), JSON.stringify(session, null, 2));
      
      // Get first question
      const question = space.getCurrentQuestion(session.session.id);
      
      return json(res, {
        session_id: session.session.id,
        question,
        progress: space.getProgress(session.session.id),
      }, 201);
    }

    // ── Resume session ──
    const resumeMatch = url.match(/^\/api\/projects\/([^/]+)\/sessions\/([^/]+)\/resume$/);
    if (req.method === 'POST' && resumeMatch) {
      const [, projectName, sessionId] = resumeMatch;
      const statePath = join(PROJECTS_DIR, projectName, 'sessions', sessionId, 'state.json');
      if (!existsSync(statePath)) return json(res, { error: 'Session not found' }, 404);
      
      const state = JSON.parse(readFileSync(statePath, 'utf-8'));
      space.loadSession(JSON.stringify(state));
      
      const question = space.getCurrentQuestion(sessionId);
      return json(res, {
        session_id: sessionId,
        question,
        progress: space.getProgress(sessionId),
      });
    }

    // ── Get current question ──
    const questionMatch = url.match(/^\/api\/sessions\/([^/]+)\/question$/);
    if (req.method === 'GET' && questionMatch) {
      const sessionId = questionMatch[1];
      const question = space.getCurrentQuestion(sessionId);
      if (!question) return json(res, { question: null, complete: true });
      return json(res, { question, progress: space.getProgress(sessionId) });
    }

    // ── Submit answer ──
    const answerMatch = url.match(/^\/api\/sessions\/([^/]+)\/answer$/);
    if (req.method === 'POST' && answerMatch) {
      const sessionId = answerMatch[1];
      const body = await readBody(req);
      
      const result = space.submitAnswer(sessionId, body.question_id, body.open_ended, body.choice_id);
      
      // Get next question and progress
      const nextQuestion = space.getCurrentQuestion(sessionId);
      const progress = space.getProgress(sessionId);
      
      return json(res, {
        ...result,
        next_question: nextQuestion,
        progress,
      });
    }

    // ── Skip question ──
    const skipMatch = url.match(/^\/api\/sessions\/([^/]+)\/skip$/);
    if (req.method === 'POST' && skipMatch) {
      const sessionId = skipMatch[1];
      const body = await readBody(req);
      space.skipQuestion(sessionId, body.question_id, body.reason || 'skipped');
      
      const nextQuestion = space.getCurrentQuestion(sessionId);
      const progress = space.getProgress(sessionId);
      
      return json(res, { ok: true, next_question: nextQuestion, progress });
    }

    // ── Get progress ──
    const progressMatch = url.match(/^\/api\/sessions\/([^/]+)\/progress$/);
    if (req.method === 'GET' && progressMatch) {
      const sessionId = progressMatch[1];
      const progress = space.getProgress(sessionId);
      return json(res, { progress });
    }

    // ── Get artifacts ──
    const artifactsMatch = url.match(/^\/api\/sessions\/([^/]+)\/artifacts$/);
    if (req.method === 'GET' && artifactsMatch) {
      const sessionId = artifactsMatch[1];
      const artifacts = space.getArtifacts(sessionId);
      return json(res, { artifacts });
    }

    // ── Export session ──
    const exportMatch = url.match(/^\/api\/sessions\/([^/]+)\/export$/);
    if (req.method === 'POST' && exportMatch) {
      const sessionId = exportMatch[1];
      const body = await readBody(req);
      
      // Find session state
      const sessionJson = space.saveSession(sessionId);
      const sessionState = JSON.parse(sessionJson);
      const artifacts = space.getArtifacts(sessionId);
      
      const formats = body.formats || ['markdown', 'json'];
      const projectName = body.project_name || 'export';
      
      const results = [];
      for (const format of formats) {
        const result = exportSession(sessionState, artifacts, space.framework, format, projectName);
        results.push({
          format,
          content: result.content,
          filename: result.filename,
          mime_type: result.mime_type,
          size_bytes: result.content.length,
        });
      }
      
      return json(res, { exports: results });
    }

    // ── Save session to disk ──
    const saveMatch = url.match(/^\/api\/sessions\/([^/]+)\/save$/);
    if (req.method === 'POST' && saveMatch) {
      const sessionId = saveMatch[1];
      const body = await readBody(req);
      const projectName = body.project_name;
      
      if (!projectName) return json(res, { error: 'project_name required' }, 400);
      
      const sessionJson = space.saveSession(sessionId);
      const sessionState = JSON.parse(sessionJson);
      
      const sessionsDir = join(PROJECTS_DIR, projectName, 'sessions');
      mkdirSync(join(sessionsDir, sessionId), { recursive: true });
      writeFileSync(join(sessionsDir, sessionId, 'state.json'), sessionJson);
      
      return json(res, { ok: true });
    }

    // ── Serve static files ──
    if (req.method === 'GET') {
      let filePath;
      if (url === '/' || url === '/index.html') {
        filePath = join(__dirname, 'index.html');
      } else {
        filePath = join(__dirname, url);
      }
      
      if (existsSync(filePath)) {
        const ext = filePath.split('.').pop();
        const types = { html: 'text/html', css: 'text/css', js: 'application/javascript', json: 'application/json' };
        res.writeHead(200, { 'Content-Type': types[ext] || 'text/plain' });
        res.end(readFileSync(filePath));
        return;
      }
    }

    json(res, { error: 'Not found' }, 404);
    
  } catch (err) {
    console.error('Error:', err.message);
    json(res, { error: err.message }, 500);
  }
});

server.listen(PORT, () => {
  console.log(`\n🚀 SPACE Web UI`);
  console.log(`   http://localhost:${PORT}`);
  console.log(`   Projects dir: ${PROJECTS_DIR}`);
  console.log(`   Framework: ${space.framework.meta.name} v${space.framework.meta.version}`);
  console.log(`   ${space.framework.meta.total_open_ended} questions, ${space.framework.meta.total_series} series\n`);
});
