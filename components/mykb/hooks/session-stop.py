#!/usr/bin/env python3
"""SessionStop hook — signals the daemon that a session ended.
Input: stdin JSON. Output: stdout JSON.
"""
import sys, os, json
from datetime import datetime, timezone

BUFFER_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                          '.wiki-daemon', 'buffers')
SIGNAL_DIR = os.path.join(BUFFER_DIR, 'signals')

def main():
    try:
        raw = sys.stdin.read()
        inp = json.loads(raw) if raw and raw.strip() else {}
        session_id = inp.get('thread_id') or inp.get('session_id') or 'default'
        
        os.makedirs(SIGNAL_DIR, exist_ok=True)
        signal = {
            'ts': int(datetime.now(timezone.utc).timestamp() * 1000),
            'session_id': session_id,
            'event': 'session_end',
            'thread_name': inp.get('thread_name') or inp.get('threadName') or '',
        }
        with open(os.path.join(SIGNAL_DIR, f'{session_id}.end'), 'w') as f:
            f.write(json.dumps(signal))
    except Exception:
        pass
    
    sys.stdout.write('{}')

if __name__ == '__main__':
    main()
