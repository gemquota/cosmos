# RSIS Telemetry Dashboard

Self-contained telemetry dashboard for the RSIS (Recursive Self-Improvement System).
Can be pointed at any RSIS telemetry data directory.

## Quick Start

```bash
# Start the dashboard server (points to ../rack/pulses/ by default)
python server.py

# Point to a specific telemetry directory
python server.py --telemetry-dir /path/to/rack/pulses

# Custom port
python server.py --port 9090
```

Then open http://localhost:8080 in your browser.

## Structure

```
telemetry-dashboard/
├── server.py           # Self-contained HTTP server (Python stdlib, no deps)
├── frontend/           # Static frontend files (HTML, CSS, JS)
│   ├── index.html      # Main dashboard HTML
│   ├── style.css       # Dashboard styling
│   ├── app.js          # All dashboard logic
│   ├── config.js       # Data source configuration
│   └── data.json       # Copy of telemetry data (for standalone file use)
├── backend/            # Original FastAPI backend (from rsis/dashboard/)
│   ├── __init__.py
│   ├── app.py
│   └── templates/
├── requirements.txt    # For the FastAPI backend (optional)
└── README.md
```

## API Endpoints

| Endpoint | Description |
|----------|-------------|
| `/api/data` | Main telemetry data (dashboard-data.json) |
| `/api/pulses` | List all pulse files |
| `/api/pulses/{filename}` | Get specific pulse data |
| `/api/status` | Server + data status |
| `/api/config` | Current server configuration |

## Configuration

Edit `frontend/config.js` to change data sources:

- **USE_API = true**: Fetch data from the server API (default when using server.py)
- **USE_API = false**: Fetch data from a local file path (for standalone HTML opening)

For standalone use without the server:
```js
var USE_API = false;
var DATA_DIR = '';
var DATA_FILE = 'data.json';  // Use the bundled data.json
```

## Origins

This dashboard was extracted from the RSIS project and made self-contained.
- Frontend: extracted from `dashboard/` (Chart.js SPA)
- Backend: extracted from `rsis/dashboard/` (FastAPI/HTMX)
