import { describe, it, expect, beforeAll, afterAll } from 'vitest';
import { mkdtempSync, rmSync } from 'fs';
import { tmpdir } from 'os';
import { join } from 'path';
import { createApp } from '../../web/server.mjs';

describe('SPACE Web Server (createApp)', () => {
  let projectsDir;
  let server;
  let base;

  beforeAll(async () => {
    projectsDir = mkdtempSync(join(tmpdir(), 'space-web-test-'));
    server = createApp({ projectsDir, port: 0 });
    await new Promise((resolve) => server.listen(0, resolve));
    const addr = server.address();
    base = `http://127.0.0.1:${addr.port}`;
  });

  afterAll(async () => {
    await new Promise((resolve) => server.close(resolve));
    rmSync(projectsDir, { recursive: true, force: true });
  });

  const api = (path, opts = {}) =>
    fetch(base + path, {
      method: opts.method || 'GET',
      headers: { 'Content-Type': 'application/json' },
      body: opts.body ? JSON.stringify(opts.body) : undefined,
    });

  it('answers CORS preflight with 204 + allow headers', async () => {
    const res = await api('/api/projects', {
      method: 'OPTIONS',
      headers: {
        Origin: 'http://localhost:8081',
        'Access-Control-Request-Method': 'POST',
      },
    });
    expect(res.status).toBe(204);
    expect(res.headers.get('access-control-allow-origin')).toBe('*');
    expect(res.headers.get('access-control-allow-methods')).toContain('POST');
  });

  it('serves the framework summary', async () => {
    const res = await api('/api/framework');
    expect(res.status).toBe(200);
    const data = await res.json();
    expect(data.meta.name).toBe('Structured Prompt Creation Framework');
    expect(data.series.length).toBe(7);
  });

  it('lists an empty project set for a fresh dir', async () => {
    const res = await api('/api/projects');
    expect(res.status).toBe(200);
    expect(await res.json()).toEqual([]);
  });

  it('creates, lists, duplicates, and rejects unnamed projects', async () => {
    const created = await api('/api/projects', {
      method: 'POST',
      body: { name: 'pass-005-test', description: 'web server suite' },
    });
    expect(created.status).toBe(201);
    const project = (await created.json()).project;
    expect(project.name).toBe('pass-005-test');

    const listed = await api('/api/projects');
    const names = (await listed.json()).map((p) => p.name);
    expect(names).toContain('pass-005-test');

    const dup = await api('/api/projects', {
      method: 'POST',
      body: { name: 'pass-005-test' },
    });
    expect(dup.status).toBe(409);

    const noName = await api('/api/projects', { method: 'POST', body: {} });
    expect(noName.status).toBe(400);
  });

  it('gets and deletes a project by name', async () => {
    await api('/api/projects', { method: 'POST', body: { name: 'delete-me' } });

    const detail = await api('/api/projects/delete-me');
    expect(detail.status).toBe(200);
    expect((await detail.json()).name).toBe('delete-me');

    const missing = await api('/api/projects/nope');
    expect(missing.status).toBe(404);

    const del = await api('/api/projects/delete-me', { method: 'DELETE' });
    expect(del.status).toBe(200);

    const gone = await api('/api/projects/delete-me');
    expect(gone.status).toBe(404);
  });

  it('serves the SPA index at /', async () => {
    const res = await api('/');
    expect(res.status).toBe(200);
    expect(res.headers.get('content-type')).toContain('text/html');
    expect(await res.text()).toContain('SPACE');
  });

  it('returns JSON 404 for unknown API routes', async () => {
    const res = await api('/api/does-not-exist');
    expect(res.status).toBe(404);
    expect((await res.json()).error).toBe('Not found');
  });
});
