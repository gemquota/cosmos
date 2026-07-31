#!/usr/bin/env python3
"""PostToolUse hook — captures every agent turn and buffers it for the wiki daemon.
Input: stdin JSON (turn context). Output: stdout JSON.
Must complete in < 2 seconds. Never raises.
"""
import sys, os, json
from datetime import datetime, timezone

BUFFER_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                          '.wiki-daemon', 'buffers')

def main():
    try:
        raw = sys.stdin.read()
        if not raw or not raw.strip():
            sys.stdout.write('{}')
            return
        
        inp = json.loads(raw)
        session_id = inp.get('thread_id') or inp.get('session_id') or inp.get('threadId') or 'default'
        turn_id = inp.get('turn_id') or inp.get('turnId') or str(int(datetime.now(timezone.utc).timestamp() * 1000))
        
        tool_input = inp.get('tool_input') or {}
        tool_response = inp.get('tool_response') or {}
        
        content = (tool_input.get('content') or tool_input.get('new_string') or
                   tool_input.get('file_content') or inp.get('content') or
                   inp.get('file_content') or inp.get('diff') or '')[:10000]
        response = (tool_response.get('content') or tool_response.get('text') or
                    tool_response.get('result') or inp.get('response') or
                    inp.get('result') or '')[:10000]
        
        turn = {
            'ts': int(datetime.now(timezone.utc).timestamp() * 1000),
            'turn_id': turn_id,
            'tool': inp.get('tool_name') or inp.get('tool') or 'unknown',
            'content': content,
            'response': response,
            'has_content': len(content) > 0,
            'has_response': len(response) > 0,
            'tool_input_keys': list(tool_input.keys())[:10],
        }
        
        os.makedirs(BUFFER_DIR, exist_ok=True)
        buffer_path = os.path.join(BUFFER_DIR, f'{session_id}.ndjson')
        with open(buffer_path, 'a') as f:
            f.write(json.dumps(turn) + '\n')
    except Exception:
        pass  # Must never block the agent
    
    sys.stdout.write('{}')

if __name__ == '__main__':
    main()
