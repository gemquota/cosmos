import { createContext, useContext, useReducer, useEffect } from 'react'

const StoreContext = createContext(null)
const STORAGE_KEY = 'prompt-framework-answers'

function loadPersistedState() {
  try {
    const raw = localStorage.getItem(STORAGE_KEY)
    return raw ? JSON.parse(raw) : null
  } catch { return null }
}

function persistState(state) {
  try {
    localStorage.setItem(STORAGE_KEY, JSON.stringify({
      answers: state.answers,
      completedRounds: [...state.completedRounds],
      activeSeries: state.activeSeries,
      activeRound: state.activeRound,
      view: state.view,
    }))
  } catch { /* ignore */ }
}

const initialPersisted = loadPersistedState()

const initialState = {
  view: initialPersisted?.view || 'welcome',
  activeSeries: initialPersisted?.activeSeries || null,
  activeRound: initialPersisted?.activeRound || 1,
  answers: initialPersisted?.answers || {},
  completedRounds: new Set(initialPersisted?.completedRounds || []),
}

function reducer(state, action) {
  switch (action.type) {
    case 'SET_VIEW':
      return { ...state, view: action.view }

    case 'SELECT_SERIES':
      return {
        ...state,
        view: 'series',
        activeSeries: action.seriesId,
        activeRound: state.activeRound || 1,
      }

    case 'SET_ROUND':
      return { ...state, activeRound: action.round }

    case 'ANSWER_OE': {
      const key = `${action.seriesId}.${action.round}.${action.oeId}`
      return {
        ...state,
        answers: {
          ...state.answers,
          [key]: { ...(state.answers[key] || {}), openEnded: action.text }
        }
      }
    }

    case 'ANSWER_MC': {
      const key = `${action.seriesId}.${action.round}.${action.oeId}`
      return {
        ...state,
        answers: {
          ...state.answers,
          [key]: { ...(state.answers[key] || {}), selectedChoice: action.choiceId }
        }
      }
    }

    case 'COMPLETE_ROUND': {
      const cr = new Set(state.completedRounds)
      cr.add(`${action.seriesId}-${action.round}`)
      return { ...state, completedRounds: cr }
    }

    case 'GO_TO_SUMMARY':
      return { ...state, view: 'summary' }

    case 'RESET':
      return { ...initialState, completedRounds: new Set() }

    default:
      return state
  }
}

export function StoreProvider({ children }) {
  const [state, dispatch] = useReducer(reducer, initialState)

  useEffect(() => {
    const handler = () => persistState(state)
    window.addEventListener('beforeunload', handler)
    return () => window.removeEventListener('beforeunload', handler)
  }, [state])

  useEffect(() => { persistState(state) }, [state])

  return (
    <StoreContext.Provider value={{ state, dispatch }}>
      {children}
    </StoreContext.Provider>
  )
}

export function useStore() {
  const ctx = useContext(StoreContext)
  if (!ctx) throw new Error('useStore must be used within StoreProvider')
  return ctx
}
