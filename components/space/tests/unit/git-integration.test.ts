import { describe, it, expect, beforeEach, afterEach } from 'vitest';
import { GitIntegration, createGitIntegration } from '../../src/integration/git.js';
import { mkdtempSync, rmSync, writeFileSync } from 'fs';
import { join } from 'path';
import { tmpdir } from 'os';

let tempDir: string;

beforeEach(() => {
  tempDir = mkdtempSync(join(tmpdir(), 'space-git-test-'));
});

afterEach(() => {
  rmSync(tempDir, { recursive: true, force: true });
});

describe('GitIntegration', () => {
  it('creates a new git repo', () => {
    const git = new GitIntegration(tempDir);
    expect(git.isInitialized()).toBe(false);
    const result = git.init();
    expect(result).toBe(true);
    expect(git.isInitialized()).toBe(true);
  });

  it('returns correct status for uninitiated repo', () => {
    const git = new GitIntegration(tempDir);
    const status = git.getStatus();
    expect(status.isRepo).toBe(false);
  });

  it('returns correct status after init', () => {
    const git = createGitIntegration(tempDir);
    const status = git.getStatus();
    expect(status.isRepo).toBe(true);
    expect(status.branch).toBe('main');
  });

  it('detects dirty state', () => {
    const git = createGitIntegration(tempDir);
    writeFileSync(join(tempDir, 'test.txt'), 'hello');
    const status = git.getStatus();
    expect(status.dirty).toBe(true);
  });

  it('commits files', () => {
    const git = createGitIntegration(tempDir);
    writeFileSync(join(tempDir, 'test.txt'), 'hello world');
    const result = git.commit('add test file');
    expect(result).not.toBeNull();
    expect(result!.message).toContain('add test file');
    expect(result!.hash).toBeTruthy();
  });

  it('auto-commits with prefix', () => {
    const git = createGitIntegration(tempDir, { commitMessagePrefix: '[rsi]' });
    writeFileSync(join(tempDir, 'data.json'), '{"key":"value"}');
    const result = git.autoCommit('snapshot', 'session state saved');
    expect(result).not.toBeNull();
    expect(result!.message).toContain('[rsi]');
    expect(result!.message).toContain('snapshot');
  });

  it('respects autoCommit=false', () => {
    const git = createGitIntegration(tempDir, { autoCommit: false });
    writeFileSync(join(tempDir, 'data.json'), '{}');
    const result = git.autoCommit('snapshot', 'test');
    expect(result).toBeNull();
  });

  it('returns clean status after commit', () => {
    const git = createGitIntegration(tempDir);
    writeFileSync(join(tempDir, 'file.txt'), 'content');
    git.commit('initial');
    const status = git.getStatus();
    expect(status.dirty).toBe(false);
  });

  it('gets diff', () => {
    const git = createGitIntegration(tempDir);
    writeFileSync(join(tempDir, 'file.txt'), 'v1');
    git.commit('initial');
    writeFileSync(join(tempDir, 'file.txt'), 'v2');
    const diff = git.diff();
    expect(diff).toContain('v2');
  });

  it('gets log', () => {
    const git = createGitIntegration(tempDir);
    writeFileSync(join(tempDir, 'f.txt'), 'a');
    git.commit('first commit');
    const log = git.log();
    expect(log).toHaveLength(1);
    expect(log[0].message).toContain('first commit');
  });

  it('creates and switches branches', () => {
    const git = createGitIntegration(tempDir);
    writeFileSync(join(tempDir, 'f.txt'), 'a');
    git.commit('init');
    const result = git.createBranch('feature-x');
    expect(result).toBe(true);
    const status = git.getStatus();
    expect(status.branch).toBe('feature-x');
  });

  it('gets and sets config', () => {
    const git = new GitIntegration(tempDir);
    expect(git.getConfig().autoCommit).toBe(true);
    git.setConfig({ autoCommit: false, commitMessagePrefix: '[custom]' });
    const config = git.getConfig();
    expect(config.autoCommit).toBe(false);
    expect(config.commitMessagePrefix).toBe('[custom]');
  });

  it('handles non-existent repo gracefully', () => {
    const git = new GitIntegration('/tmp/nonexistent-repo-12345');
    expect(git.isInitialized()).toBe(false);
    expect(git.getStatus().isRepo).toBe(false);
    expect(git.commit('test')).toBeNull();
  });
});
