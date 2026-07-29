import { describe, it, expect, beforeEach, afterEach } from 'vitest';
import { SQLiteStorage } from '../../src/storage/sqlite.js';
import { mkdtempSync, rmSync, existsSync } from 'fs';
import { join } from 'path';
import { tmpdir } from 'os';
import type { Project, SessionState, Snapshot } from '../../src/types/index.js';

let tempDir: string;
let dbPath: string;
let storage: SQLiteStorage;

function makeProject(id = 'test-project'): Project {
  return {
    id,
    name: 'Test Project',
    description: 'A test project',
    created_at: new Date().toISOString(),
    updated_at: new Date().toISOString(),
    framework_version: '2.1.0',
  };
}

function makeSession(projectId = 'test-project', sessionId = 'session-1'): SessionState {
  return {
    session: {
      id: sessionId,
      project_id: projectId,
      framework_version: '2.1.0',
      created_at: new Date().toISOString(),
      updated_at: new Date().toISOString(),
      status: 'in_progress',
      estimated_completion_pct: 25,
      total_time_ms: 5000,
    },
    answers: {},
    progress: {
      completed_rounds: [],
      completed_series: [],
      current_series: 1,
      current_round: 1,
    },
    artifacts: {},
  };
}

function makeSnapshot(sessionId = 'session-1', projectId = 'test-project'): Snapshot {
  return {
    id: `snap-${Date.now()}`,
    session_id: sessionId,
    project_id: projectId,
    created_at: new Date().toISOString(),
    session_state: makeSession(projectId, sessionId),
  };
}

beforeEach(async () => {
  tempDir = mkdtempSync(join(tmpdir(), 'space-sqlite-test-'));
  dbPath = join(tempDir, 'test.db');
  storage = await SQLiteStorage.create(dbPath);
});

afterEach(() => {
  storage.close();
  rmSync(tempDir, { recursive: true, force: true });
});

describe('SQLiteStorage', () => {
  describe('Projects', () => {
    it('creates and retrieves a project', () => {
      const project = makeProject();
      storage.createProject(project);
      const retrieved = storage.getProject('test-project');
      expect(retrieved).not.toBeNull();
      expect(retrieved!.id).toBe('test-project');
      expect(retrieved!.name).toBe('Test Project');
    });

    it('returns null for non-existent project', () => {
      expect(storage.getProject('nonexistent')).toBeNull();
    });

    it('lists projects', () => {
      storage.createProject(makeProject('p1'));
      storage.createProject(makeProject('p2'));
      const projects = storage.listProjects();
      expect(projects).toHaveLength(2);
    });

    it('updates a project', () => {
      const project = makeProject();
      storage.createProject(project);
      project.name = 'Updated Name';
      storage.updateProject(project);
      const retrieved = storage.getProject('test-project');
      expect(retrieved!.name).toBe('Updated Name');
    });

    it('deletes a project and its sessions', () => {
      const project = makeProject();
      storage.createProject(project);
      storage.createSession(makeSession());
      storage.deleteProject('test-project');
      expect(storage.getProject('test-project')).toBeNull();
      expect(storage.listSessions('test-project')).toHaveLength(0);
    });
  });

  describe('Sessions', () => {
    beforeEach(() => {
      storage.createProject(makeProject());
    });

    it('creates and retrieves a session', () => {
      const session = makeSession();
      storage.createSession(session);
      const retrieved = storage.getSession('test-project', 'session-1');
      expect(retrieved).not.toBeNull();
      expect(retrieved!.session.id).toBe('session-1');
    });

    it('returns null for non-existent session', () => {
      expect(storage.getSession('test-project', 'nonexistent')).toBeNull();
    });

    it('lists sessions for a project', () => {
      storage.createSession(makeSession('test-project', 's1'));
      storage.createSession(makeSession('test-project', 's2'));
      const sessions = storage.listSessions('test-project');
      expect(sessions).toHaveLength(2);
    });

    it('updates a session', () => {
      const session = makeSession();
      storage.createSession(session);
      session.session.status = 'completed';
      session.session.estimated_completion_pct = 100;
      storage.updateSession(session);
      const retrieved = storage.getSession('test-project', 'session-1');
      expect(retrieved!.session.status).toBe('completed');
    });

    it('deletes a session', () => {
      storage.createSession(makeSession());
      storage.deleteSession('test-project', 'session-1');
      expect(storage.getSession('test-project', 'session-1')).toBeNull();
    });
  });

  describe('Snapshots', () => {
    beforeEach(() => {
      storage.createProject(makeProject());
    });

    it('saves and retrieves a snapshot', () => {
      const snapshot = makeSnapshot();
      storage.saveSnapshot(snapshot);
      const retrieved = storage.getLatestSnapshot('session-1', 'test-project');
      expect(retrieved).not.toBeNull();
      expect(retrieved!.id).toBe(snapshot.id);
    });

    it('returns null for non-existent snapshot', () => {
      expect(storage.getLatestSnapshot('nonexistent', 'test-project')).toBeNull();
    });

    it('gets latest snapshot by created_at', () => {
      const snap1 = makeSnapshot();
      snap1.created_at = '2026-01-01T00:00:00Z';
      const snap2 = makeSnapshot();
      snap2.created_at = '2026-06-01T00:00:00Z';
      storage.saveSnapshot(snap1);
      storage.saveSnapshot(snap2);
      const latest = storage.getLatestSnapshot('session-1', 'test-project');
      expect(latest!.id).toBe(snap2.id);
    });

    it('lists all snapshots', () => {
      storage.saveSnapshot(makeSnapshot());
      storage.saveSnapshot(makeSnapshot());
      const snapshots = storage.listSnapshots('session-1', 'test-project');
      expect(snapshots).toHaveLength(2);
    });
  });

  describe('Exports', () => {
    beforeEach(() => {
      storage.createProject(makeProject());
    });

    it('saves an export', () => {
      const result = { filename: 'spec.md', content: '# Specification' };
      const path = storage.saveExport('session-1', 'test-project', 'markdown', result);
      expect(path).toContain('spec.md');
    });
  });

  describe('Archives', () => {
    it('exports and imports an archive', () => {
      const project = makeProject();
      storage.createProject(project);
      storage.createSession(makeSession());

      const archive = storage.exportArchive('test-project');
      expect(archive).not.toBeNull();
      expect(archive!.project.id).toBe('test-project');
      expect(archive!.sessions).toHaveLength(1);

      // Import into new storage
      const storage2Path = join(tempDir, 'test2.db');
      return SQLiteStorage.create(storage2Path).then((storage2) => {
        storage2.importArchive(archive!);
        const imported = storage2.getProject('test-project');
        expect(imported).not.toBeNull();
        storage2.close();
      });
    });
  });

  describe('Persistence', () => {
    it('persists data to disk and reloads', async () => {
      storage.createProject(makeProject());
      storage.createSession(makeSession());
      storage.close();

      const reloaded = await SQLiteStorage.create(dbPath);
      const project = reloaded.getProject('test-project');
      expect(project).not.toBeNull();
      const session = reloaded.getSession('test-project', 'session-1');
      expect(session).not.toBeNull();
      reloaded.close();

      // Recreate storage for afterEach cleanup
      storage = await SQLiteStorage.create(dbPath);
    });
  });
});
