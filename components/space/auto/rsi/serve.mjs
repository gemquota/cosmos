import { createServer } from 'http';
import { readFileSync, existsSync } from 'fs';
import { join, extname } from 'path';
import { fileURLToPath } from 'url';
import { dirname } from 'path';

const __dirname = dirname(fileURLToPath(import.meta.url));
const PORT = parseInt(process.argv[2] || '8889');

const MIME = {
  '.html': 'text/html', '.json': 'application/json',
  '.css': 'text/css', '.js': 'text/javascript',
  '.md': 'text/markdown', '.png': 'image/png',
};

const server = createServer((req, res) => {
  let url = req.url.split('?')[0];
  if (url === '/') url = '/viewer.html';
  
  const filePath = join(__dirname, url);
  
  if (!existsSync(filePath)) {
    res.writeHead(404); res.end('Not found'); return;
  }
  
  const ext = extname(filePath);
  res.writeHead(200, {
    'Content-Type': MIME[ext] || 'application/octet-stream',
    'Cache-Control': 'no-cache',
  });
  res.end(readFileSync(filePath));
});

server.listen(PORT, '0.0.0.0', () => {
  console.log(`SPACE RSI Viewer running at http://localhost:${PORT}`);
  console.log(`Serving from: ${__dirname}`);
});
