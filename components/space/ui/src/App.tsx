import { useReducer, useEffect } from 'react';
import Sidebar from './components/Sidebar.tsx';
import Dashboard from './views/Dashboard.tsx';
import QuestionView from './views/QuestionView.tsx';
import SummaryView from './views/SummaryView.tsx';
import { FRAMEWORK_DATA } from './data/framework-data.ts';
import './styles.css';

type View = 'dashboard' | 'question' | 'summary';
interface State { view: View; series: number; round: number; answers: Record<string, {oe: string; mc: string}>; completed: Set<string> }
type Action = 
  | {t:'VIEW'; v:View} | {t:'SERIES'; id:number} | {t:'ROUND'; r:number}
  | {t:'OE'; qid:string; text:string} | {t:'MC'; qid:string; cid:string}
  | {t:'DONE'; series:number; round:number} | {t:'RESET'} | {t:'RESTORE'; s:State};

const STORAGE_KEY = 'space-ui-state';

const INIT: State = { view:'dashboard', series:1, round:1, answers:{}, completed:new Set() };

function reducer(s: State, a: Action): State {
  switch(a.t) {
    case 'VIEW': return {...s, view:a.v};
    case 'SERIES': return {...s, view:'question', series:a.id, round:1};
    case 'ROUND': return {...s, round:a.r};
    case 'OE': return {...s, answers:{...s.answers, [a.qid]:{oe:a.text, mc:s.answers[a.qid]?.mc||''}}};
    case 'MC': return {...s, answers:{...s.answers, [a.qid]:{oe:s.answers[a.qid]?.oe||'', mc:a.cid}}};
    case 'DONE': { const c=new Set(s.completed); c.add(`${a.series}-${a.round}`); return {...s, completed:c}; }
    case 'RESTORE': return a.s;
    case 'RESET': { try { localStorage.removeItem(STORAGE_KEY); } catch {} return INIT; }
  }
}

export const SERIES = FRAMEWORK_DATA.map(s => ({ id: s.id, name: s.name, rounds: s.rounds.length, deps: s.deps }));
export const QDATA = Object.fromEntries(FRAMEWORK_DATA.map(s => [s.id, { name: s.name, rounds: s.rounds }]));

export type { State, Action };

const VIEW_LABELS: Record<View, string> = {
  dashboard: 'Dashboard',
  question: 'Question',
  summary: 'Summary',
};

export default function App() {
  const [s, dispatch] = useReducer(reducer, INIT, (init) => {
    // Restore from localStorage on mount
    try {
      const saved = localStorage.getItem(STORAGE_KEY);
      if (saved) {
        const parsed = JSON.parse(saved);
        parsed.completed = new Set(parsed.completed || []);
        return parsed;
      }
    } catch {}
    return init;
  });

  // Save to localStorage on every state change
  useEffect(() => {
    try {
      const toSave = { ...s, completed: Array.from(s.completed) };
      localStorage.setItem(STORAGE_KEY, JSON.stringify(toSave));
    } catch {}
  }, [s]);

  return (
    <div className="app-layout">
      <a href="#main-content" className="skip-link">Skip to main content</a>
      <Sidebar state={s} dispatch={dispatch} />
      <main
        id="main-content"
        className="main-content"
        role="main"
        aria-label={VIEW_LABELS[s.view]}
        aria-live="polite"
      >
        {s.view==='dashboard' && <Dashboard dispatch={dispatch} />}
        {s.view==='question' && <QuestionView state={s} dispatch={dispatch} />}
        {s.view==='summary' && <SummaryView state={s} dispatch={dispatch} />}
      </main>
    </div>
  );
}
