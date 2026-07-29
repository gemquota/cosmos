import { describe, it, expect, beforeEach, afterEach } from 'vitest';
import { existsSync, rmSync } from 'fs';
import { join } from 'path';
import { FileSystemStorage, AutoSaveManager } from '../../src/storage/filesystem.js';
import { createSpace } from '../../src/engine/core.js';
import type { Project, SessionState, Snapshot } from '../../src/types/index.js';

const TEST_DIR = '/data/data/com.termux/files/home/dev/space/.test-space-' + Date.now();

describe('Phase 5: Persistence', () => {
  let storage: FileSystemStorage;

  beforeEach(() => {
    storage = new FileSystemStorage(TEST_DIR);
  });

  afterEach(() => {
    if (existsSync(TEST_DIR)) rmSync(TEST_DIR, { recursive: true });
  });

  describe('Project CRUD', () => {
    it('creates and retrieves a project', () => {
      const project: Project = {
        id: 'proj_test1',
        name: 'Test Project',
        description: 'A test',
        created_at: new Date().toISOString(),
        updated_at: new Date().toISOString(),
        framework_version: '2.0.0',
        sessions: [],
        tags: [],
      };
      storage.createProject(project);
      const retrieved = storage.getProject('proj_test1');
      expect(retrieved).not.toBeNull();
      expect(retrieved!.name).toBe('Test Project');
    });

    it('lists projects', () => {
      storage.createProject({
        id: 'p1',
        name: 'Project 1',
        description: '',
        created_at: '',
        updated_at: '',
        framework_version: '2.0.0',
        sessions: [],
        tags: [],
      });
      storage.createProject({
        id: 'p2',
        name: 'Project 2',
        description: '',
        created_at: '',
        updated_at: '',
        framework_version: '2.0.0',
        sessions: [],
        tags: [],
      });
      const projects = storage.listProjects();
      expect(projects).toHaveLength(2);
    });

    it('updates a project', () => {
      storage.createProject({
        id: 'p1',
        name: 'Original',
        description: '',
        created_at: '',
        updated_at: '',
        framework_version: '2.0.0',
        sessions: [],
        tags: [],
      });
      storage.updateProject({
        id: 'p1',
        name: 'Updated',
        description: 'new desc',
        created_at: '',
        updated_at: '',
        framework_version: '2.0.0',
        sessions: [],
        tags: [],
      });
      const p = storage.getProject('p1');
      expect(p!.name).toBe('Updated');
    });

    it('deletes a project', () => {
      storage.createProject({
        id: 'p1',
        name: 'ToDelete',
        description: '',
        created_at: '',
        updated_at: '',
        framework_version: '2.0.0',
        sessions: [],
        tags: [],
      });
      storage.deleteProject('p1');
      expect(storage.getProject('p1')).toBeNull();
    });
  });

  describe('Session CRUD', () => {
    it('creates and retrieves a session', () => {
      storage.createProject({
        id: 'p1',
        name: 'P',
        description: '',
        created_at: '',
        updated_at: '',
        framework_version: '2.0.0',
        sessions: [],
        tags: [],
      });
      const space = createSpace();
      const session = space.startSession('p1');
      storage.createSession(session);

      const retrieved = storage.getSession('p1', session.session.id);
      expect(retrieved).not.toBeNull();
      expect(retrieved!.session.id).toBe(session.session.id);
    });

    it('updates session state', () => {
      storage.createProject({
        id: 'p1',
        name: 'P',
        description: '',
        created_at: '',
        updated_at: '',
        framework_version: '2.0.0',
        sessions: [],
        tags: [],
      });
      const space = createSpace();
      const session = space.startSession('p1');
      storage.createSession(session);

      space.submitAnswer(session.session.id, '1.1.1', 'Test answer', '1.1.1.a');
      storage.updateSession(session);

      const retrieved = storage.getSession('p1', session.session.id);
      expect(retrieved!.answers['1.1.1']).toBeDefined();
    });

    it('lists sessions for a project', () => {
      storage.createProject({
        id: 'p1',
        name: 'P',
        description: '',
        created_at: '',
        updated_at: '',
        framework_version: '2.0.0',
        sessions: [],
        tags: [],
      });
      const space = createSpace();
      const s1 = space.startSession('p1');
      const s2 = space.startSession('p1');
      storage.createSession(s1);
      storage.createSession(s2);

      const sessions = storage.listSessions('p1');
      expect(sessions).toHaveLength(2);
    });
  });

  describe('Snapshots', () => {
    it('saves and retrieves snapshots', () => {
      storage.createProject({
        id: 'p1',
        name: 'P',
        description: '',
        created_at: '',
        updated_at: '',
        framework_version: '2.0.0',
        sessions: [],
        tags: [],
      });
      const space = createSpace();
      const session = space.startSession('p1');
      storage.createSession(session);

      const snapshot: Snapshot = {
        id: 'snap_1',
        session_id: session.session.id,
        created_at: new Date().toISOString(),
        trigger: 'round_complete',
        series_id: 1,
        round: 1,
        state: session,
        size_bytes: 100,
      };
      storage.saveSnapshot(snapshot);

      const latest = storage.getLatestSnapshot(session.session.id, 'p1');
      expect(latest).not.toBeNull();
      expect(latest!.id).toBe('snap_1');
    });
  });

  describe('Exports', () => {
    it('saves export files', () => {
      storage.createProject({
        id: 'p1',
        name: 'P',
        description: '',
        created_at: '',
        updated_at: '',
        framework_version: '2.0.0',
        sessions: [],
        tags: [],
      });
      const path = storage.saveExport('sess1', 'p1', 'json', {
        content: '{"test": true}',
        filename: 'test.json',
        mime_type: 'application/json',
        size_bytes: 15,
      });
      expect(existsSync(path)).toBe(true);
    });
  });

  describe('Archives', () => {
    it('exports and imports archives', () => {
      storage.createProject({
        id: 'p1',
        name: 'Archive Test',
        description: 'desc',
        created_at: '',
        updated_at: '',
        framework_version: '2.0.0',
        sessions: [],
        tags: [],
      });
      const space = createSpace();
      const session = space.startSession('p1');
      storage.createSession(session);

      const archive = storage.exportArchive('p1');
      expect(archive).not.toBeNull();
      expect(archive!.project.name).toBe('Archive Test');
      expect(archive!.sessions).toHaveLength(1);

      // Import to new location
      const storage2 = new FileSystemStorage(TEST_DIR + '-import');
      storage2.importArchive(archive!);
      const imported = storage2.getProject('p1');
      expect(imported).not.toBeNull();
      expect(imported!.name).toBe('Archive Test');

      if (existsSync(TEST_DIR + '-import')) rmSync(TEST_DIR + '-import', { recursive: true });
    });
  });

  describe('AutoSaveManager', () => {
    it('can be created and controlled', () => {
      const session = createSpace().startSession('test');
      const manager = new AutoSaveManager(storage, () => session, 1000);
      manager.start();
      manager.saveNow();
      manager.stop();
      // No assertion needed — just verifying no crashes
      expect(true).toBe(true);
    });
  });
});
