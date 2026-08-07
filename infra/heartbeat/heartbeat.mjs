#!/usr/bin/env node

/**
 * SPACE Heartbeat Monitor
 * Reads watches.json for service definitions and checks each one.
 * Usage: node heartbeat.mjs [--interval <seconds>] [--restart]
 *        SPACE_DIR=/path/to/project node heartbeat.mjs   # from anywhere
 */

import http from 'http';
import { spawn } from 'child_process';
import { readFileSync, existsSync } from 'fs';
import { join, dirname } from 'path';
import { fileURLToPath } from 'url';

const __dirname = dirname(fileURLToPath(import.meta.url));

// Resolve project root: SPACE_DIR env var takes precedence, else script dir
const PROJECT_DIR = process.env.SPACE_DIR || __dirname;
const WATCHES_FILE = join(dirname(fileURLToPath(import.meta.url)), "watches.json");

let SERVICES = [];
try {
  if (existsSync(WATCHES_FILE)) {
    SERVICES = JSON.parse(readFileSync(WATCHES_FILE, 'utf-8'));
    SERVICES = SERVICES.map(s => ({
      ...s,
      startCmd: s.startCmd || 'node',
      startArgs: s.startArgs || [],
      cwd: s.cwd || PROJECT_DIR,
    }));
  } else {
    console.error(`⚠️  ${WATCHES_FILE} not found. No services to monitor.`);
  }
} catch (err) {
  console.error(`⚠️  Error reading ${WATCHES_FILE}: ${err.message}`);
}

const args = process.argv.slice(2);
const INTERVAL = parseInt(args[args.indexOf('--interval') + 1] || '30', 10) * 1000;
const SHOULD_RESTART = args.includes('--restart');

const workers = new Map();
const history = {};

function log(service, status, msg) {
  const ts = new Date().toISOString().slice(11, 19);
  const icon = status === 'UP' ? '🟢' : status === 'DOWN' ? '🔴' : status === 'RESTARTED' ? '🔄' : '⚪';
  console.log(`${icon} [${ts}] ${service}: ${msg}`);
}

function checkService(service) {
  return new Promise((resolve) => {
    // Port watch (localhost) or URL watch (e.g. the deployed GitHub Pages
    // site). Both default to HTTP 200 as the up condition.
    const url = service.url || `http://localhost:${service.port}${service.path || '/'}`;
    const req = http.get(url, (res) => {
      resolve(res.statusCode === 200);
      res.resume();
    });
    req.on('error', () => resolve(false));
    req.setTimeout(5000, () => { req.destroy(); resolve(false); });
  });
}

function startService(service) {
  if (workers.has(service.name)) {
    const old = workers.get(service.name);
    old.kill('SIGTERM');
    workers.delete(service.name);
  }

  log(service.name, 'RESTARTED', 'Starting...');
  const child = spawn(service.startCmd, service.startArgs, {
    cwd: service.cwd,
    stdio: 'pipe',
    detached: false,
  });

  child.stdout.on('data', (d) => {
    if (d.toString().includes('listening') || d.toString().includes('http://localhost')) {
      log(service.name, 'UP', d.toString().trim());
    }
  });

  child.stderr.on('data', () => {});

  child.on('exit', (code) => {
    log(service.name, 'DOWN', `Process exited (code: ${code})`);
    workers.delete(service.name);
    if (SHOULD_RESTART) {
      setTimeout(() => startService(service), 2000);
    }
  });

  workers.set(service.name, child);
}

async function heartbeat() {
  if (SERVICES.length === 0) {
    console.log('⚠️  No watches configured. Add services via `sentry add` or edit watches.json');
    return;
  }

  console.log(`\n${'═'.repeat(50)}`);
  console.log(`❤️  SPACE Heartbeat — ${new Date().toLocaleTimeString()}`);
  console.log(`${'═'.repeat(50)}`);

  for (const service of SERVICES) {
    const wasUp = history[service.name];
    const isUp = await checkService(service);

    if (isUp) {
      if (!wasUp) log(service.name, 'UP', 'Responding on port ' + service.port);
      history[service.name] = true;
    } else {
      if (wasUp !== false) log(service.name, 'DOWN', `Port ${service.port} not responding`);
      history[service.name] = false;

      if (SHOULD_RESTART && service.startCmd) {
        startService(service);
      }
    }
  }

  const up = SERVICES.filter(s => history[s.name]).length;
  const total = SERVICES.length;
  const statusChar = up === total ? '✅' : '⚠️';
  console.log(`${statusChar} ${up}/${total} services up`);
}

console.log(`❤️  SPACE Heartbeat Monitor`);
console.log(`   Config: ${WATCHES_FILE}`);
console.log(`   Project: ${PROJECT_DIR}`);
console.log(`   Interval: ${INTERVAL / 1000}s | Auto-restart: ${SHOULD_RESTART ? 'ON' : 'OFF'}`);
console.log(`   Services: ${SERVICES.map(s => s.url ? `${s.name} (${s.url})` : `${s.name} (:${s.port})`).join(', ') || '(none)'}`);
console.log('');

heartbeat();
setInterval(heartbeat, INTERVAL);

process.on('SIGINT', () => {
  console.log('\n❤️  Heartbeat stopped.');
  for (const [name, child] of workers) {
    child.kill('SIGTERM');
    console.log(`  Stopped: ${name}`);
  }
  process.exit(0);
});
