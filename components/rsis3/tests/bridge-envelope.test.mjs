/**
 * Envelope-level Phase 2 tests (cosmos-envelope/1 hardening).
 *
 * Run: node --test tests/bridge-envelope.test.mjs
 */
import { test } from 'node:test';
import assert from 'node:assert/strict';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import {
  ENVELOPE_SPEC, ENVELOPE_VERSION, TEXT_PREVIEW_MAX, MEDIA_MAX_BYTES,
  TOTAL_MAX_BYTES, mimeOf, isText, isStructured, isAudio, isVideo, isPdf,
  sha256, resolveRef, parseStructured, extractPdfTextFromBuffer,
  buildEnvelope, parseEnvelope, serializeEnvelope,
} from '../rack/bridge/envelope.mjs';

const HERE = path.dirname(fileURLToPath(import.meta.url));
const RSIS3 = path.resolve(HERE, '..');
const REPO = path.resolve(RSIS3, '..', '..');

const allow = {
  roots: [RSIS3, path.resolve(REPO, 'components', 'mykb')],
  deny: ['.git', '.rsis/telemetry', 'rack/bridge/cycles', 'rack/bridge/sessions', '.wiki-daemon/buffers'],
  base: REPO,
};

test('envelope versioning stays additive at spec v1', () => {
  assert.equal(ENVELOPE_SPEC, 'cosmos-envelope/1');
  assert.equal(ENVELOPE_VERSION, '1.1');
});

test('caps are server-side constants', () => {
  assert.equal(TEXT_PREVIEW_MAX, 8 * 1024);
  assert.equal(MEDIA_MAX_BYTES, 4 * 1024 * 1024);
  assert.equal(TOTAL_MAX_BYTES, 6 * 1024 * 1024);
});

test('mime classification', () => {
  assert.equal(mimeOf('README.md'), 'text/markdown');
  assert.ok(isText('text/markdown'));
  assert.ok(isText('text/plain'));
  assert.ok(isStructured('application/json'));
  assert.ok(isStructured('text/yaml'));
  assert.ok(isAudio('audio/wav'));
  assert.ok(isVideo('video/mp4'));
  assert.ok(isPdf('application/pdf'));
});

test('resolveRef enforces roots + deny prefixes', () => {
  assert.equal(resolveRef('../../../../etc/passwd', allow), null);
  assert.equal(resolveRef('/etc/passwd', allow), null);
  assert.equal(resolveRef('C:\\windows\\win.ini', allow), null);
  assert.equal(resolveRef('.rsis/telemetry/000.json', allow), null);   // deny prefix
  assert.equal(resolveRef('rack/bridge/cycles/2026-08-08.jsonl', allow), null);
  assert.equal(resolveRef('README.md', allow), path.join(RSIS3, 'README.md'));
  assert.equal(resolveRef('.rsis/strategies.json', allow), path.join(RSIS3, '.rsis', 'strategies.json'));
});

test('parseStructured builds schema blocks (not raw strings)', () => {
  const j = parseStructured('application/json', '{"a":1,"b":{"c":[1,2]},"d":"x"}');
  assert.equal(j.parsed, true);
  assert.equal(j.schema.keys, 3);
  assert.equal(j.schema.depth, 3);  // object -> nested object -> array
  assert.equal(j.schema.types.b, 'object');
  assert.equal(parseStructured('application/json', '{oops').parsed, false);
  const y = parseStructured('text/yaml', 'a: 1\nb:\n  - x\n');
  assert.equal(y.parsed, true);
  assert.equal(y.schema.keys, 2);
});

test('PDF text extraction with fallback (uncompressed stream)', () => {
  const content = 'BT /F1 12 Tf 72 720 Td (Hello Cosmos Bridge) Tj ET';
  const pdf = Buffer.concat([
    Buffer.from('%PDF-1.4\n4 0 obj << /Length ' + content.length + ' >> stream\n'),
    Buffer.from(content),
    Buffer.from('\nendstream endobj\n%%EOF\n'),
  ]);
  const r = extractPdfTextFromBuffer(pdf);
  assert.equal(r.ok, true);
  assert.match(r.text, /Hello Cosmos Bridge/);
});

test('buildEnvelope round-trips and hides binary data', () => {
  const envObj = buildEnvelope({
    kind: 'chat',
    text: 'hi',
    ctx: { ts: 't', drives: null, kg: { nodes: 1, edges: 2 }, strategies: {}, pulses: 3, syntheses: [] },
    artifacts: [{ kind: 'file', ref: 'a.json', name: 'a.json', mime: 'application/json', size: 4, sha: 'x', inline: true, parsed: true, schema: { keys: 1 } }],
  });
  assert.equal(envObj.spec, ENVELOPE_SPEC);
  const s = serializeEnvelope(envObj);
  const back = parseEnvelope(s);
  assert.equal(back.spec, ENVELOPE_SPEC);
  assert.equal(back.artifacts[0].parsed, true);
  assert.ok(!('data' in back.artifacts[0]));
  assert.equal(parseEnvelope('garbage'), null);
});

test('sha256 stable', () => {
  assert.equal(sha256(Buffer.from('abc')), 'ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad');
});
