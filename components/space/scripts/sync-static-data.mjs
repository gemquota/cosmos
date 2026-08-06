#!/usr/bin/env node
// Sync web/projects.json (SPA static GET fallback) from the local SPACE
// projects dir, so the hosted SPA lists real projects when the API server
// is unreachable (e.g. GitHub Pages). Run after creating/renaming projects.
import { existsSync, readdirSync, readFileSync, writeFileSync } from 'fs';
import { homedir } from 'os';
import { join } from 'path';

const PROJECTS_DIR = join(homedir(), '.space', 'projects');
const OUT = new URL('../web/projects.json', import.meta.url);

if (!existsSync(PROJECTS_DIR)) {
  console.error(`No projects dir at ${PROJECTS_DIR}; writing empty fallback.`);
  writeFileSync(OUT, '[]\n');
  process.exit(0);
}

const projects = [];
for (const name of readdirSync(PROJECTS_DIR, { withFileTypes: true })) {
  if (!name.isDirectory()) continue;
  const metaPath = join(PROJECTS_DIR, name.name, '.space.json');
  if (!existsSync(metaPath)) continue;
  const meta = JSON.parse(readFileSync(metaPath, 'utf-8'));
  const sessionsDir = join(PROJECTS_DIR, name.name, 'sessions');
  let sessionCount = 0;
  let completedCount = 0;
  if (existsSync(sessionsDir)) {
    for (const s of readdirSync(sessionsDir, { withFileTypes: true })) {
      if (!s.isDirectory()) continue;
      sessionCount++;
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

writeFileSync(OUT, JSON.stringify(projects, null, 2) + '\n');
console.log(`web/projects.json: ${projects.length} projects synced`);
