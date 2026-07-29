import { describe, it, expect, beforeEach, afterEach } from 'vitest';
import { existsSync, rmSync } from 'fs';
import { FileSystemStorage } from '../../src/storage/filesystem.js';
import { SnapshotManager } from '../../src/engine/snapshot-manager.js';
import { createSpace } from '../../src/engine/core.js';

const TEST_DIR = '/data/data/com.termux/files/home/dev/space/.test-snap-' + Date.now();

describe('Snapshot Manager', () => {
  let storage: FileSystemStorage;
  let snapMgr: SnapshotManager;

  beforeEach(() => {
    storage = new FileSystemStorage(TEST_DIR);
    snapMgr = new SnapshotManager(storage, true);
  });

  afterEach(() => {
    if (existsSync(TEST_DIR)) rmSync(TEST_DIR, { recursive: true });
  });

  it('creates a snapshot on round completion', () => {
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
    space.submitAnswer(session.session.id, '1.1.1', 'Test answer', '1.1.1.a');
    space.submitAnswer(session.session.id, '1.1.2', 'Test audience', '1.1.2.b');
    storage.createSession(session);

    const snapshot = snapMgr.createSnapshot(session, 'round_complete', 1, 1);
    expect(snapshot.id).toMatch(/^snap_/);
    expect(snapshot.trigger).toBe('round_complete');
    expect(snapshot.series_id).toBe(1);
    expect(snapshot.round).toBe(1);
    expect(snapshot.size_bytes).toBeGreaterThan(0);
  });

  it('restores session from snapshot', () => {
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
    space.submitAnswer(session.session.id, '1.1.1', 'ML systems', '1.1.1.a');
    storage.createSession(session);

    const snapshot = snapMgr.createSnapshot(session, 'series_complete', 1, 3);
    const restored = snapMgr.restoreFromSnapshot(snapshot);

    expect(restored.session.id).toBe(session.session.id);
    expect(restored.answers['1.1.1']).toBeDefined();
    expect(restored.answers['1.1.1'].open_ended_text).toBe('ML systems');
  });

  it('recovers session from latest snapshot', () => {
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
    space.submitAnswer(session.session.id, '1.1.1', 'Test', '1.1.1.a');
    storage.createSession(session);

    snapMgr.createSnapshot(session, 'round_complete', 1, 1);
    const recovered = snapMgr.recover(session.session.id, 'p1');

    expect(recovered).not.toBeNull();
    expect(recovered!.answers['1.1.1']).toBeDefined();
  });

  it('returns null for recovery with no snapshots', () => {
    const recovered = snapMgr.recover('nonexistent', 'nonexistent');
    expect(recovered).toBeNull();
  });

  it('lists snapshots', () => {
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

    snapMgr.createSnapshot(session, 'round_complete', 1, 1);
    snapMgr.createSnapshot(session, 'round_complete', 1, 2);

    const snapshots = snapMgr.listSnapshots(session.session.id, 'p1');
    expect(snapshots).toHaveLength(2);
  });

  it('deep clones session state in snapshot', () => {
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

    const snapshot = snapMgr.createSnapshot(session, 'manual', 1, 1);
    // Modify session after snapshot
    space.submitAnswer(session.session.id, '1.1.1', 'Modified', '1.1.1.a');

    // Snapshot should not be affected
    expect(snapshot.state.answers['1.1.1']).toBeUndefined();
  });
});
