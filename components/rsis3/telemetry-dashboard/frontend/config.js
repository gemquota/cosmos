// Dashboard data configuration
// When served by the telemetry-dashboard server, data is available via the API.
// For standalone file access, set DATA_DIR to '' and DATA_FILE to 'data.json'.
// For the telemetry-dashboard server, set to use the API endpoint.

// If served by the included server.py, use the API:
var DATA_DIR = '';        // Not used when USE_API is true
var DATA_FILE = '';       // Not used when USE_API is true
var USE_API = true;       // true = fetch from /api/data, false = fetch DATA_DIR+DATA_FILE
var API_BASE = '';        // API base path (empty = same origin)
var API_DATA_ENDPOINT = '/api/data';  // Endpoint for dashboard data
