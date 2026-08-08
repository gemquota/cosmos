// Dashboard data configuration
// Change DATA_DIR to point to your telemetry data directory
var DATA_DIR = '../rack/pulses/';
var DATA_FILE = 'dashboard-data.json';
// Full URL is DATA_DIR + DATA_FILE

// COSMOS Bridge (LLM x framework chat) — served by rack/bridge/server.mjs
var BRIDGE_URL = 'http://localhost:8787';
// Active multitiered goal stack (Output > Communicate > Wrap > Bridge)
var GOALS_FILE = '../rack/goals_stack.json';
