export interface UIFrameworkQuestion { id: string; text: string; choices: { id: string; text: string }[]; }
export interface UIFrameworkRound { round: number; focus: string; questions: UIFrameworkQuestion[]; }
export interface UIFrameworkSeries { id: number; name: string; description: string; rounds: UIFrameworkRound[]; deps: number[]; }

export const FRAMEWORK_DATA: UIFrameworkSeries[] = [
  { id: 1, name: 'Conceptual Depth', description: 'Domain and audience framing', deps: [], rounds: [
    { round: 1, focus: 'Domain and Audience', questions: [
      { id: '1.1.1', text: 'What is the primary domain or field this prompt addresses?', choices: [{ id: '1.1.1.a', text: 'A single well-established domain' }, { id: '1.1.1.b', text: 'An interdisciplinary space' }, { id: '1.1.1.c', text: 'An emerging or niche area' }] },
      { id: '1.1.2', text: 'Who is the intended audience?', choices: [{ id: '1.1.2.a', text: 'Experts / researchers' }, { id: '1.1.2.b', text: 'Practitioners / professionals' }, { id: '1.1.2.c', text: 'Learners / general audience' }] },
    ]},
    { round: 2, focus: 'Assumptions and Abstraction', questions: [
      { id: '1.2.1', text: 'What foundational concepts can the output take for granted?', choices: [{ id: '1.2.1.a', text: 'Full prerequisites assumed' }, { id: '1.2.1.b', text: 'Core fundamentals assumed' }, { id: '1.2.1.c', text: 'First-principles treatment' }] },
      { id: '1.2.2', text: 'At what level of abstraction should the output operate?', choices: [{ id: '1.2.2.a', text: 'Concrete — specific examples' }, { id: '1.2.2.b', text: 'Mixed — frameworks with examples' }, { id: '1.2.2.c', text: 'Formal — definitions and proofs' }] },
    ]},
    { round: 3, focus: 'Terminology and Scaffolding', questions: [
      { id: '1.3.1', text: 'What vocabulary should be used or avoided?', choices: [{ id: '1.3.1.a', text: 'Standard industry terminology' }, { id: '1.3.1.b', text: 'Plain accessible language' }, { id: '1.3.1.c', text: 'Formal academic register' }] },
      { id: '1.3.2', text: 'How should complexity be distributed?', choices: [{ id: '1.3.2.a', text: 'Progressive — scaffold from simple to advanced' }, { id: '1.3.2.b', text: 'Flat — consistent complexity' }, { id: '1.3.2.c', text: 'Overview-first then deep dives' }] },
    ]},
  ]},
  { id: 2, name: 'Ontological Characteristics', description: 'Entity discovery and modeling', deps: [1], rounds: [
    { round: 1, focus: 'Entity Discovery', questions: [
      { id: '2.1.1', text: 'What are the primary entities in this domain?', choices: [{ id: '2.1.1.a', text: 'Core domain objects' }, { id: '2.1.1.b', text: 'Abstract concepts' }, { id: '2.1.1.c', text: 'Hybrid' }] },
      { id: '2.1.2', text: 'What attributes define each entity?', choices: [{ id: '2.1.2.a', text: 'Properties with types' }, { id: '2.1.2.b', text: 'Behavioral characteristics' }, { id: '2.1.2.c', text: 'Relationships' }] },
      { id: '2.1.3', text: 'How should entities be categorized?', choices: [{ id: '2.1.3.a', text: 'By functional role' }, { id: '2.1.3.b', text: 'By data lifecycle' }, { id: '2.1.3.c', text: 'By interaction pattern' }] },
    ]},
    { round: 2, focus: 'Entity Properties', questions: [
      { id: '2.2.1', text: 'Which entities are core vs peripheral?', choices: [{ id: '2.2.1.a', text: 'Clear distinction' }, { id: '2.2.1.b', text: 'All equal' }, { id: '2.2.1.c', text: 'Context-dependent' }] },
      { id: '2.2.2', text: 'What granularity level for modeling?', choices: [{ id: '2.2.2.a', text: 'Fine-grained' }, { id: '2.2.2.b', text: 'Coarse-grained' }, { id: '2.2.2.c', text: 'Progressive refinement' }] },
      { id: '2.2.3', text: 'How do entities share attributes?', choices: [{ id: '2.2.3.a', text: 'Inheritance' }, { id: '2.2.3.b', text: 'Composition' }, { id: '2.2.3.c', text: 'Mixins' }] },
    ]},
    { round: 3, focus: 'System Boundaries', questions: [
      { id: '2.3.1', text: 'What are the systemic boundaries?', choices: [{ id: '2.3.1.a', text: 'Clear boundary' }, { id: '2.3.1.b', text: 'Blurred' }, { id: '2.3.1.c', text: 'Distributed' }] },
      { id: '2.3.2', text: 'What external actors interact?', choices: [{ id: '2.3.2.a', text: 'Users only' }, { id: '2.3.2.b', text: 'Users + APIs' }, { id: '2.3.2.c', text: 'Users + APIs + systems' }] },
      { id: '2.3.3', text: 'What are the entity lifecycles?', choices: [{ id: '2.3.3.a', text: 'CRUD' }, { id: '2.3.3.b', text: 'Event-sourced' }, { id: '2.3.3.c', text: 'State machine' }] },
    ]},
    { round: 4, focus: 'Edge Cases', questions: [
      { id: '2.4.1', text: 'What entity gaps exist?', choices: [{ id: '2.4.1.a', text: 'Missing temporal' }, { id: '2.4.1.b', text: 'Missing aggregate' }, { id: '2.4.1.c', text: 'Complete' }] },
      { id: '2.4.2', text: 'Should entities be reclassified?', choices: [{ id: '2.4.2.a', text: 'Merge some' }, { id: '2.4.2.b', text: 'Split some' }, { id: '2.4.2.c', text: 'Correct' }] },
      { id: '2.4.3', text: 'What constraints apply?', choices: [{ id: '2.4.3.a', text: 'Cardinality' }, { id: '2.4.3.b', text: 'Temporal' }, { id: '2.4.3.c', text: 'Business rules' }] },
    ]},
    { round: 5, focus: 'Entity Relationships', questions: [
      { id: '2.5.1', text: 'What edge cases for interactions?', choices: [{ id: '2.5.1.a', text: 'Concurrent modification' }, { id: '2.5.1.b', text: 'Cascade deletion' }, { id: '2.5.1.c', text: 'Orphaned references' }] },
      { id: '2.5.2', text: 'How are complex entities composed?', choices: [{ id: '2.5.2.a', text: 'Aggregation' }, { id: '2.5.2.b', text: 'Composition' }, { id: '2.5.2.c', text: 'Both' }] },
      { id: '2.5.3', text: 'What cardinality relationships?', choices: [{ id: '2.5.3.a', text: 'One-to-one' }, { id: '2.5.3.b', text: 'One-to-many' }, { id: '2.5.3.c', text: 'Many-to-many' }] },
    ]},
  ]},
  { id: 3, name: 'Semantic Relationships', description: 'Connection patterns', deps: [2], rounds: [
    { round: 1, focus: 'Direct Associations', questions: [
      { id: '3.1.1', text: 'What direct associations exist?', choices: [{ id: '3.1.1.a', text: 'Transactional' }, { id: '3.1.1.b', text: 'Hierarchical' }, { id: '3.1.1.c', text: 'Peer-to-peer' }] },
      { id: '3.1.2', text: 'How are associations typed?', choices: [{ id: '3.1.2.a', text: 'By verb' }, { id: '3.1.2.b', text: 'By role' }, { id: '3.1.2.c', text: 'By weight' }] },
    ]},
    { round: 2, focus: 'Hierarchy', questions: [
      { id: '3.2.1', text: 'What hierarchy structures?', choices: [{ id: '3.2.1.a', text: 'Tree' }, { id: '3.2.1.b', text: 'DAG' }, { id: '3.2.1.c', text: 'Flat' }] },
      { id: '3.2.2', text: 'What inheritance model?', choices: [{ id: '3.2.2.a', text: 'Classical' }, { id: '3.2.2.b', text: 'Prototype' }, { id: '3.2.2.c', text: 'Composition only' }] },
    ]},
    { round: 3, focus: 'Causal', questions: [
      { id: '3.3.1', text: 'What causal relationships?', choices: [{ id: '3.3.1.a', text: 'Direct causation' }, { id: '3.3.1.b', text: 'Correlation' }, { id: '3.3.1.c', text: 'Feedback loops' }] },
      { id: '3.3.2', text: 'What dependency chains?', choices: [{ id: '3.3.2.a', text: 'Linear' }, { id: '3.3.2.b', text: 'Branching' }, { id: '3.3.2.c', text: 'Complex graphs' }] },
    ]},
    { round: 4, focus: 'Dynamics', questions: [
      { id: '3.4.1', text: 'How mutable are relationships?', choices: [{ id: '3.4.1.a', text: 'Immutable' }, { id: '3.4.1.b', text: 'Versioned' }, { id: '3.4.1.c', text: 'Mutable' }] },
      { id: '3.4.2', text: 'How composed?', choices: [{ id: '3.4.2.a', text: 'References' }, { id: '3.4.2.b', text: 'Junction entities' }, { id: '3.4.2.c', text: 'Embedded' }] },
    ]},
  ]},
  { id: 4, name: 'Procedural Breadth', description: 'Workflow design', deps: [2, 3], rounds: [
    { round: 1, focus: 'Scope', questions: [
      { id: '4.1.1', text: 'Procedural scope?', choices: [{ id: '4.1.1.a', text: 'Core only' }, { id: '4.1.1.b', text: 'All operations' }, { id: '4.1.1.c', text: 'Including edge cases' }] },
      { id: '4.1.2', text: 'How many workflow steps?', choices: [{ id: '4.1.2.a', text: '1-3 (simple)' }, { id: '4.1.2.b', text: '4-8 (moderate)' }, { id: '4.1.2.c', text: '9+ (complex)' }] },
    ]},
    { round: 2, focus: 'Decisions', questions: [
      { id: '4.2.1', text: 'Key decision points?', choices: [{ id: '4.2.1.a', text: 'Entry/exit' }, { id: '4.2.1.b', text: 'Throughout' }, { id: '4.2.1.c', text: 'Critical only' }] },
      { id: '4.2.2', text: 'How decisions made?', choices: [{ id: '4.2.2.a', text: 'Rule-based' }, { id: '4.2.2.b', text: 'ML-based' }, { id: '4.2.2.c', text: 'Human-in-loop' }] },
    ]},
    { round: 3, focus: 'Errors', questions: [
      { id: '4.3.1', text: 'Error handling strategy?', choices: [{ id: '4.3.1.a', text: 'Fail fast' }, { id: '4.3.1.b', text: 'Graceful degradation' }, { id: '4.3.1.c', text: 'Retry' }] },
      { id: '4.3.2', text: 'Recovery mechanisms?', choices: [{ id: '4.3.2.a', text: 'Auto rollback' }, { id: '4.3.2.b', text: 'Manual' }, { id: '4.3.2.c', text: 'Dead letter queue' }] },
    ]},
  ]},
  { id: 5, name: 'Technical Specifications', description: 'Stack and infrastructure', deps: [1, 4], rounds: [
    { round: 1, focus: 'Hardware', questions: [
      { id: '5.1.1', text: 'Hardware requirements?', choices: [{ id: '5.1.1.a', text: 'Low traffic' }, { id: '5.1.1.b', text: 'Medium' }, { id: '5.1.1.c', text: 'High traffic' }] },
      { id: '5.1.2', text: 'Compute profile?', choices: [{ id: '5.1.2.a', text: 'CPU-bound' }, { id: '5.1.2.b', text: 'Memory-bound' }, { id: '5.1.2.c', text: 'I/O-bound' }] },
    ]},
    { round: 2, focus: 'Stack', questions: [
      { id: '5.2.1', text: 'Primary language/framework?', choices: [{ id: '5.2.1.a', text: 'Single language' }, { id: '5.2.1.b', text: 'Primary + secondary' }, { id: '5.2.1.c', text: 'Polyglot' }] },
      { id: '5.2.2', text: 'Database technology?', choices: [{ id: '5.2.2.a', text: 'Relational' }, { id: '5.2.2.b', text: 'Document' }, { id: '5.2.2.c', text: 'Hybrid' }] },
    ]},
    { round: 3, focus: 'Performance', questions: [
      { id: '5.3.1', text: 'Performance targets?', choices: [{ id: '5.3.1.a', text: 'Sub-100ms' }, { id: '5.3.1.b', text: 'Sub-1s' }, { id: '5.3.1.c', text: 'Best effort' }] },
      { id: '5.3.2', text: 'Data volume?', choices: [{ id: '5.3.2.a', text: 'Small' }, { id: '5.3.2.b', text: 'Medium' }, { id: '5.3.2.c', text: 'Large' }] },
      { id: '5.3.3', text: 'Availability targets?', choices: [{ id: '5.3.3.a', text: '99.9%' }, { id: '5.3.3.b', text: '99.99%' }, { id: '5.3.3.c', text: 'Business hours' }] },
      { id: '5.3.4', text: 'Scalability model?', choices: [{ id: '5.3.4.a', text: 'Vertical' }, { id: '5.3.4.b', text: 'Horizontal' }, { id: '5.3.4.c', text: 'Auto-scaling' }] },
      { id: '5.3.5', text: 'Security requirements?', choices: [{ id: '5.3.5.a', text: 'Basic auth' }, { id: '5.3.5.b', text: 'OAuth2/JWT' }, { id: '5.3.5.c', text: 'Full compliance' }] },
    ]},
    { round: 4, focus: 'Integration', questions: [
      { id: '5.4.1', text: 'External integrations?', choices: [{ id: '5.4.1.a', text: 'None' }, { id: '5.4.1.b', text: '1-3 APIs' }, { id: '5.4.1.c', text: 'Many' }] },
      { id: '5.4.2', text: 'Integration protocols?', choices: [{ id: '5.4.2.a', text: 'REST' }, { id: '5.4.2.b', text: 'gRPC/GraphQL' }, { id: '5.4.2.c', text: 'Message queues' }] },
      { id: '5.4.3', text: 'Deployment timeline?', choices: [{ id: '5.4.3.a', text: 'Quick' }, { id: '5.4.3.b', text: 'Standard' }, { id: '5.4.3.c', text: 'Extended' }] },
      { id: '5.4.4', text: 'Deployment strategy?', choices: [{ id: '5.4.4.a', text: 'Blue/green' }, { id: '5.4.4.b', text: 'Canary' }, { id: '5.4.4.c', text: 'Rolling' }] },
      { id: '5.4.5', text: 'Documentation required?', choices: [{ id: '5.4.5.a', text: 'API only' }, { id: '5.4.5.b', text: 'API + architecture' }, { id: '5.4.5.c', text: 'Full suite' }] },
    ]},
  ]},
  { id: 6, name: 'Development Methodologies', description: 'Team process', deps: [4, 5], rounds: [
    { round: 1, focus: 'Team', questions: [
      { id: '6.1.1', text: 'Development cadence?', choices: [{ id: '6.1.1.a', text: 'Continuous' }, { id: '6.1.1.b', text: 'Sprint (Scrum)' }, { id: '6.1.1.c', text: 'Kanban' }] },
      { id: '6.1.2', text: 'Team composition?', choices: [{ id: '6.1.2.a', text: 'Solo' }, { id: '6.1.2.b', text: 'Small (2-5)' }, { id: '6.1.2.c', text: 'Large (5+)' }] },
    ]},
    { round: 2, focus: 'Quality', questions: [
      { id: '6.2.1', text: 'Quality practices?', choices: [{ id: '6.2.1.a', text: 'Unit tests only' }, { id: '6.2.1.b', text: 'Unit + integration' }, { id: '6.2.1.c', text: 'Full pyramid' }] },
      { id: '6.2.2', text: 'Tech debt management?', choices: [{ id: '6.2.2.a', text: 'Refactoring sprints' }, { id: '6.2.2.b', text: 'Boy scout rule' }, { id: '6.2.2.c', text: 'No process' }] },
    ]},
    { round: 3, focus: 'Communication', questions: [
      { id: '6.3.1', text: 'Communication patterns?', choices: [{ id: '6.3.1.a', text: 'Async-first' }, { id: '6.3.1.b', text: 'Sync-first' }, { id: '6.3.1.c', text: 'Hybrid' }] },
      { id: '6.3.2', text: 'Decision making?', choices: [{ id: '6.3.2.a', text: 'RFC/ADR' }, { id: '6.3.2.b', text: 'Lead decides' }, { id: '6.3.2.c', text: 'Consensus' }] },
    ]},
  ]},
  { id: 7, name: 'Operational / Functional', description: 'Deployment and maintenance', deps: [5, 6], rounds: [
    { round: 1, focus: 'Deployment', questions: [
      { id: '7.1.1', text: 'Deployment process?', choices: [{ id: '7.1.1.a', text: 'Manual' }, { id: '7.1.1.b', text: 'CI/CD' }, { id: '7.1.1.c', text: 'GitOps' }] },
      { id: '7.1.2', text: 'Environment management?', choices: [{ id: '7.1.2.a', text: 'Dev+staging+prod' }, { id: '7.1.2.b', text: 'Dev+prod' }, { id: '7.1.2.c', text: 'Ephemeral' }] },
    ]},
    { round: 2, focus: 'Monitoring', questions: [
      { id: '7.2.1', text: 'Monitoring plan?', choices: [{ id: '7.2.1.a', text: 'Basic logging' }, { id: '7.2.1.b', text: 'Logging + metrics' }, { id: '7.2.1.c', text: 'Full observability' }] },
      { id: '7.2.2', text: 'Runtime config?', choices: [{ id: '7.2.2.a', text: 'Env vars' }, { id: '7.2.2.b', text: 'Config files' }, { id: '7.2.2.c', text: 'Feature flags' }] },
    ]},
    { round: 3, focus: 'Maintenance', questions: [
      { id: '7.3.1', text: 'Maintenance policy?', choices: [{ id: '7.3.1.a', text: 'On-call' }, { id: '7.3.1.b', text: 'Business hours' }, { id: '7.3.1.c', text: 'Automated' }] },
      { id: '7.3.2', text: 'Data stewardship?', choices: [{ id: '7.3.2.a', text: 'Manual backups' }, { id: '7.3.2.b', text: 'Automated + retention' }, { id: '7.3.2.c', text: 'Full lifecycle' }] },
    ]},
  ]},
];

export function getSeriesById(id: number): UIFrameworkSeries | undefined {
  return FRAMEWORK_DATA.find(s => s.id === id);
}

export function areDepsMet(seriesId: number, completed: Set<string>): boolean {
  const series = getSeriesById(seriesId);
  if (!series) return false;
  return series.deps.every(depId => {
    const depSeries = getSeriesById(depId);
    if (!depSeries) return false;
    return Array.from({ length: depSeries.rounds.length }, (_, i) => i + 1)
      .every(r => completed.has(`${depId}-${r}`));
  });
}
