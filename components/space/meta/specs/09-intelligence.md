# 9: Intelligence Layer Specification

**Status:** Draft
**Version:** 1.0.0
**Created:** 2026-07-25
**Depends On:** `05-execution-engine.md`, `06-llm-integration.md`

---

## 1. Purpose

Defines the analytics, adaptive routing, quality intelligence, and cross-session insights that sit on top of the core engine. This is what makes SPACE a "superb" engine rather than just a questionnaire.

## 2. Scope

- Cross-session analytics and insights
- Adaptive question routing (skip irrelevant probes)
- Specification completeness scoring
- Contradiction detection and resolution
- Recommendation engine ("you might also consider...")

---

## 3. Design

### 3.1 Cross-Session Analytics

```typescript
interface AnalyticsEngine {
  // Per-session metrics
  getSessionMetrics(session_id: string): Promise<SessionMetrics>;
  
  // Cross-session insights
  getProjectInsights(project_id: string): Promise<ProjectInsights>;
  
  // Framework-level analytics (across all SPACE users)
  getFrameworkAnalytics(): Promise<FrameworkAnalytics>;
}

interface SessionMetrics {
  session_id: string;
  timing: {
    total_minutes: number;
    per_series: { series_id: number; minutes: number }[];
    per_question: { question_id: string; seconds: number }[];
    fastest_series: number;
    slowest_series: number;
  };
  quality: {
    avg_answer_length: number;
    avg_quality_score: number;
    shortest_answer: string;        // question_id
    longest_answer: string;
    most_edited: string;
  };
  patterns: {
    series_completion_order: number[];
    abandoned_at?: { series_id: number; round: number };
    skip_count: number;
    back_track_count: number;       // times user went back to edit
  };
}

interface ProjectInsights {
  project_id: string;
  total_sessions: number;
  avg_completion_pct: number;
  avg_time_minutes: number;
  specification_drift: {
    question_id: string;
    changes: { from: string; to: string; session_id: string }[];
  }[];
  common_patterns: string[];        // patterns across sessions
}

interface FrameworkAnalytics {
  total_sessions_all_users: number;
  avg_completion_pct: number;
  drop_off_points: {
    series_id: number;
    round: number;
    drop_off_rate: number;          // % of sessions that stop here
  }[];
  most_time_consuming_questions: {
    question_id: string;
    avg_seconds: number;
  }[];
  answer_distribution: {
    question_id: string;
    choice_distribution: Record<string, number>;  // choice_id → count
  }[];
}
```

### 3.2 Adaptive Question Routing

The adaptive router decides which questions to ask and in what order, beyond the default sequential flow:

```typescript
interface AdaptiveRouter {
  analyze(
    session: SessionState,
    artifacts: ArtifactDictionary
  ): Promise<RoutingDecision>;
}

interface RoutingDecision {
  action: 'continue' | 'skip' | 'generate_followup' | 'request_clarification';
  target_question_id?: string;
  generated_probe?: OpenEndedQuestion;
  reason: string;
  confidence: number;
}
```

**Routing rules:**

| Condition | Action | Reason |
|-----------|--------|--------|
| Question is clearly answered | Continue | No intervention needed |
| Answer is vague (<20 chars) | Request clarification | Insufficient detail for artifact |
| Artifact already well-defined | Skip related question | Redundant probe |
| Domain is very simple (<5 entities) | Skip deep ontological rounds | Overkill for simple domains |
| Prior answers suggest high complexity | Generate followup | Need more detail in complex areas |
| Contradiction detected | Request clarification | Resolve before proceeding |

**Skip heuristics:**

```typescript
function shouldSkip(
  question: OpenEndedQuestion,
  session: SessionState,
  artifacts: ArtifactDictionary
): { skip: boolean; reason: string } {
  // Skip heuristic 1: Question about entities when domain is trivially small
  if (question.id.startsWith('2.') && countArtifacts(artifacts, 'entity_list') < 3) {
    return { skip: true, reason: 'Domain has fewer than 3 entities; deep ontological analysis not needed' };
  }
  
  // Skip heuristic 2: Technical specs for non-technical domains
  if (question.id.startsWith('5.1.') && getArtifact(artifacts, 'domain')?.includes('art')) {
    return { skip: true, reason: 'Artistic/creative domain; hardware specs may not apply' };
  }
  
  // Skip heuristic 3: Development methodology for solo projects
  if (question.id.startsWith('6.') && getArtifact(artifacts, 'team_composition')?.value?.includes('solo')) {
    // Don't skip entirely, but simplify choices
    return { skip: false, reason: '' };
  }
  
  return { skip: false, reason: '' };
}
```

### 3.3 Specification Completeness Scoring

```typescript
interface CompletenessScorer {
  score(session: SessionState, artifacts: ArtifactDictionary): Promise<CompletenessReport>;
}

interface CompletenessReport {
  overall_score: number;             // 0-100
  per_dimension: {
    dimension: string;
    score: number;
    status: 'excellent' | 'good' | 'adequate' | 'weak' | 'missing';
    gaps: string[];                   // specific missing artifacts
    suggestions: string[];
  }[];
  readiness_level: 'draft' | 'review' | 'ready';
}

// Dimensions scored:
const DIMENSIONS = [
  {
    id: 'domain_clarity',
    name: 'Domain Clarity',
    required_artifacts: ['domain', 'audience_level', 'terminology_preferences'],
    weight: 0.15,
  },
  {
    id: 'entity_model',
    name: 'Entity Model',
    required_artifacts: ['entity_list', 'entity_attributes', 'entity_categories'],
    weight: 0.20,
  },
  {
    id: 'relationship_map',
    name: 'Relationship Map',
    required_artifacts: ['relationship_graph', 'dependency_chains'],
    weight: 0.15,
  },
  {
    id: 'procedures',
    name: 'Procedural Coverage',
    required_artifacts: ['procedure_steps', 'decision_points', 'branching_complexity'],
    weight: 0.10,
  },
  {
    id: 'technical',
    name: 'Technical Readiness',
    required_artifacts: ['hardware_requirements', 'software_stack', 'performance_targets'],
    weight: 0.20,
  },
  {
    id: 'methodology',
    name: 'Methodology',
    required_artifacts: ['development_cadence', 'quality_practices', 'team_composition'],
    weight: 0.10,
  },
  {
    id: 'operations',
    name: 'Operational Readiness',
    required_artifacts: ['deployment_strategy', 'monitoring_plan', 'maintenance_policy'],
    weight: 0.10,
  },
];
```

### 3.4 Contradiction Detection

```typescript
interface ContradictionDetector {
  detect(
    session: SessionState,
    artifacts: ArtifactDictionary
  ): Promise<Contradiction[]>;
}

interface Contradiction {
  id: string;
  type: 'direct' | 'implied' | 'temporal';
  questions: string[];                // question IDs involved
  description: string;                // human-readable explanation
  severity: 'low' | 'medium' | 'high';
  resolution_suggestions: string[];
}

// Examples:
// - "Q1.1.1 says single domain, but Q2.1.1 lists entities from 3 domains"
// - "Q5.3.1 says <100 req/s but Q5.1.2 says enterprise-scale hardware"
// - "Q6.1.1 says solo developer but Q6.2.1 says pair programming required"
```

### 3.5 Recommendation Engine

```typescript
interface RecommendationEngine {
  getRecommendations(
    session: SessionState,
    artifacts: ArtifactDictionary
  ): Promise<Recommendation[]>;
}

interface Recommendation {
  id: string;
  category: 'gap' | 'enhancement' | 'warning' | 'tip';
  title: string;
  description: string;
  related_questions?: string[];
  related_artifacts?: string[];
  priority: 'low' | 'medium' | 'high';
  actionable: boolean;                // can be addressed immediately?
}
```

**Recommendation patterns:**

| Pattern | Category | Example |
|---------|:--------:|---------|
| Missing critical artifact | gap | "No deployment strategy defined — consider answering 7.1.1" |
| Under-documented area | enhancement | "Entity model has only 2 entities — consider expanding" |
| Conflicting answers | warning | "Team size (solo) conflicts with methodology (Scrum)" |
| Best practice | tip | "For ML projects, consider adding data pipeline as an entity" |
| Completeness milestone | tip | "You're at 80% — just 3 more rounds to complete!" |

---

## 4. Interfaces

```typescript
class IntelligenceLayer {
  constructor(
    analytics: AnalyticsEngine,
    router: AdaptiveRouter,
    scorer: CompletenessScorer,
    detector: ContradictionDetector,
    recommender: RecommendationEngine,
  ) {}
  
  async getInsights(session_id: string): Promise<IntelligenceReport> {
    const session = await this.storage.getSession(session_id);
    const artifacts = await this.engine.getArtifacts(session_id);
    
    return {
      metrics: await this.analytics.getSessionMetrics(session_id),
      completeness: await this.scorer.score(session, artifacts),
      contradictions: await this.detector.detect(session, artifacts),
      recommendations: await this.recommender.getRecommendations(session, artifacts),
      routing_suggestions: await this.router.analyze(session, artifacts),
    };
  }
}

interface IntelligenceReport {
  metrics: SessionMetrics;
  completeness: CompletenessReport;
  contradictions: Contradiction[];
  recommendations: Recommendation[];
  routing_suggestions: RoutingDecision;
}
```

---

## 5. Edge Cases

- **Empty session:** No analytics to compute; return zero-state reports
- **Single answer:** Limited contradiction detection; more recommendations than insights
- **All answers identical across sessions:** Analytics shows high consistency
- **LLM unavailable for scoring:** Fall back to heuristic-based scoring only

---

## 6. Testing Strategy

- Analytics: verify timing calculations and aggregation
- Adaptive routing: mock sessions → verify skip/continue decisions
- Completeness scoring: known-completeness sessions → verify scores
- Contradictions: synthetic contradictions → verify detection
- Recommendations: verify no false positives on clean sessions

---

## 7. Open Questions

- Should analytics be opt-in (privacy)?
- How to handle very large numbers of sessions in framework analytics?
- Should adaptive routing be transparent to the user or hidden?
- Future: can intelligence layer train on user feedback to improve?

---

## 8. Changelog

| Version | Date | Change |
|---------|------|--------|
| 1.0.0 | 2026-07-25 | Initial draft |
