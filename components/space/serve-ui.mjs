#!/usr/bin/env node
// SPACE Web UI static server
import http from 'http';
import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const PORT = parseInt(process.argv[2] || '8888', 10);
const UI_DIR = path.join(__dirname, 'ui', 'dist');

const MIME = {
  '.html': 'text/html; charset=utf-8',
  '.js': 'application/javascript',
  '.css': 'text/css',
  '.json': 'application/json',
  '.png': 'image/png',
  '.svg': 'image/svg+xml',
};

if (!fs.existsSync(UI_DIR)) {
  console.error(`❌ UI not built at ${UI_DIR}`);
  console.error('   Run: cd ui && npm run build');
  process.exit(1);
}

const server = http.createServer((req, res) => {
  let url = req.url.split('?')[0];
  if (url === '/') url = '/index.html';
  const filePath = path.join(UI_DIR, url);
  const ext = path.extname(filePath);
  if (!filePath.startsWith(UI_DIR) || !fs.existsSync(filePath)) {
    res.writeHead(404);
    res.end('Not found');
    return;
  }
  try {
    const content = fs.readFileSync(filePath);
    res.writeHead(200, { 'Content-Type': MIME[ext] || 'application/octet-stream' });
    res.end(content);
  } catch (e) {
    res.writeHead(500);
    res.end('Server error');
  }
});

server.listen(PORT, () => {
  console.log(`🌐 SPACE Web UI — http://localhost:${PORT}`);
});
