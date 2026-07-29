#!/usr/bin/env python3
"""Build the telemetry dashboard from pulse data."""

import json, os, sys

PULSES_DIR = os.path.join(os.path.dirname(__file__), 'pulses')
DATA_FILE = os.path.join(PULSES_DIR, 'dashboard-data.json')
DASHBOARD_FILE = os.path.join(os.path.dirname(__file__), 'telemetry-dashboard.html')

def load_data():
    """Load all pulse JSONs and compile into dashboard data."""
    all_pulses = []
    all_goals = []
    score_history = {}
    telemetry_aggregates = {}
    constraint_counts = {}
    total_pass = total_hold = total_fail = total_impl = 0

    for fname in sorted(os.listdir(PULSES_DIR)):
        if not (fname.endswith('.json') and fname.startswith('pulse-')):
            continue
        with open(os.path.join(PULSES_DIR, fname)) as f:
            p = json.load(f)
        
        pid = str(p['pulse'])
        post = p.get('post_state', {}) or {}
        scores = post.get('scores', {})
        score_history[pid] = scores
        pulse_goals = p.get('goals', [])
        rrp_tel = p.get('rrp_telemetry_aggregate', {})
        telemetry_aggregates[pid] = rrp_tel
        
        impl_count = sum(1 for g in pulse_goals if g.get('type', '') == 'implementation' or 
                         g.get('rrp_evaluation', {}).get('trace', {}).get('goal_analysis', {}).get('goal_type') == 'implementation')
        total_impl += impl_count
        
        approved = sum(1 for g in pulse_goals if g.get('rrp_evaluation', {}).get('decision') == 'PASS')
        
        all_pulses.append({
            'id': pid,
            'ts_start': p.get('timestamp_start', ''),
            'ts_end': p.get('timestamp_end', ''),
            'goals_count': len(pulse_goals),
            'approved': approved,
            'duration': p.get('summary', {}).get('duration_seconds', 0),
            'scores': scores,
            'type': p.get('type', 'standard'),
            'num_goals': p.get('summary', {}).get('goals_generated', len(pulse_goals)),
            'implementation_count': impl_count,
            'telemetry': rrp_tel,
            'avg_confidence': rrp_tel.get('avg_quality_index', 0) or 
                round(sum(g.get('rrp_evaluation', {}).get('confidence', 0) for g in pulse_goals) / max(len(pulse_goals), 1), 3),
        })
        
        for g in pulse_goals:
            ev = g.get('rrp_evaluation', {})
            dec = ev.get('decision', 'UNKNOWN')
            if dec == 'PASS':
                total_pass += 1
            elif dec in ('HOLD',):
                total_hold += 1
            elif dec in ('FAIL', 'DISMISS'):
                total_fail += 1
            
            constraints = ev.get('trace', {}).get('constraint_extraction', {}).get('constraints', {})
            for cname, ctype in constraints.items():
                if cname not in constraint_counts:
                    constraint_counts[cname] = {'freq': 0, 'locked': 0}
                constraint_counts[cname]['freq'] += 1
                if ctype in ('LOCKED', 'REQUIRED'):
                    constraint_counts[cname]['locked'] += 1
            
            conversation = ev.get('conversation', [])
            rrp_tel_g = ev.get('rrp_telemetry', {})
            
            all_goals.append({
                'p': pid,
                'd': g.get('description', ''),
                'dec': dec,
                'conf': ev.get('confidence', 0),
                'file': g.get('file', ''),
                'func': g.get('function', ''),
                'type': g.get('type', ev.get('trace', {}).get('goal_analysis', {}).get('goal_type', 'implementation')),
                'conversation': [{'q': c.get('question', ''), 'a': c.get('answer', ''), 'r': c.get('round', 1)} for c in conversation],
                'constraints': constraints,
                'telemetry': rrp_tel_g,
                'contradictions': ev.get('contradictions', []),
            })
    
    summary = {
        'tot': total_pass + total_hold + total_fail,
        'pass': total_pass,
        'hold': total_hold,
        'fail': total_fail,
        'impl_count': total_impl,
        'ca': round(sum(g['conf'] for g in all_goals) / max(len(all_goals), 1), 3),
        'pulse_count': len(all_pulses),
        'cd': constraint_counts,
    }
    
    data = {
        'pulses': all_pulses,
        'goals': all_goals,
        'score_history': score_history,
        'telemetry_aggregates': telemetry_aggregates,
        'summary': summary,
    }
    
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=2)
    
    return data


def generate_html(data):
    """Generate the dashboard HTML from data using template replacement."""
    pulses_json = json.dumps(data['pulses'])
    goals_json = json.dumps(data['goals'])
    scores_json = json.dumps(data['score_history'])
    summary_json = json.dumps(data['summary'])
    tel_agg_json = json.dumps(data.get('telemetry_aggregates', {}))
    
    # Read template from the existing HTML file
    base_dir = os.path.dirname(__file__)
    tpl_path = os.path.join(base_dir, 'telemetry-dashboard.html')
    
    with open(tpl_path) as f:
        html = f.read()
    
    # Replace placeholders with data
    html = html.replace('PULSES_DATA', pulses_json)
    html = html.replace('GOALS_DATA', goals_json)
    html = html.replace('SCORES_DATA', scores_json)
    html = html.replace('SUMMARY_DATA', summary_json)
    html = html.replace('TEL_AGG_DATA', tel_agg_json)
    
    with open(DASHBOARD_FILE, 'w') as f:
        f.write(html)
    
    return len(html)


if __name__ == '__main__':
    print("Loading pulse data...")
    data = load_data()
    print(f"  {len(data['pulses'])} pulses, {len(data['goals'])} goals")
    
    v2 = [p for p in data['pulses'] if p.get('telemetry') and p['telemetry'].get('total_questions')]
    print(f"  {len(v2)} RRP v2 pulses with telemetry")
    for p in v2:
        topics = p.get('telemetry', {}).get('all_topics', [])
        print(f"    #{p['id']}: {p['goals_count']} goals, {len(topics)} topics")
    
    print("Generating dashboard...")
    size = generate_html(data)
    print(f"  Dashboard: {size/1024:.1f} KB")
    print("Done.")
