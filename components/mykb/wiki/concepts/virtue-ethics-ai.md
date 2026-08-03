---
type: "concept"
title: "Virtue Ethics for AI"
description: "Evaluating AI by the character it exhibits"
tags: ["virtue-ethics", "ethics", "ai"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Virtue Ethics for AI

## Summary
Virtue-ethical AI asks what dispositions a system should embody: honesty, care, temperance, and reliability. Where deontology asks "what rules must be followed?" and consequentialism asks "what outcomes are best?", virtue ethics asks "what kind of agent is this?" — and for AI, the question becomes whether a system's stable patterns of behavior constitute a good character, and how to train for character rather than only for acts.

## Details
- The core of virtue ethics is the virtues: stable dispositions to perceive, feel, and act well — honesty (telling the truth even when inconvenient), care (attending to others' welfare), temperance (restraint in the face of temptation), courage (acting rightly under risk), and reliability (consistency across contexts). The ethical evaluation targets the agent's character, not individual acts in isolation: a single honest answer is good, but an honest agent is trustworthy, and the trustworthiness is what virtue ethics values. This is a distinctive shift from act-based ethics — the same act can express different characters, and the character is the object of moral assessment.
- It complements rule- and consequence-based ethics by targeting character rather than acts. Rules and consequences both miss something: a rule-follower can obey rules without any disposition to do the right thing when rules are silent, and a consequence-optimizer can produce good outcomes while being manipulable or untrustworthy. Virtue ethics supplies the dispositional layer — the system's stable tendency to act well across novel situations — which is exactly what deployment needs when neither rules nor consequence predictions cover the case at hand.
- The AI translation problem: virtues are dispositions, and dispositions are not directly trainable. You cannot fine-tune "honesty" as a label; you can only train on behavioral instances (honest answers, honest refusals, honest uncertainty) and hope the disposition generalizes. This is why operationalizing virtues is difficult — the training signal is act-level, the target is disposition-level, and the gap between them is where virtue claims fail (a model that is honest in training contexts and evasive elsewhere has not acquired the virtue, only the behavior).
- Increasingly explored: virtue-flavored training objectives — helpful, honest, harmless (HHH) targets, honesty training, and character-oriented evaluation suites that probe dispositions across varied situations rather than scoring individual acts.
- RSIS3 relevance: hha-standards (helpful, honest, harmless) are a virtue list — the bundle's own operating standards are expressed as dispositions the system should exhibit, not just rules it should follow, and the same act-vs-disposition gap applies to its workers.

## Related
- [[wiki/agent-systems/honest-ai|Honest AI]] — a target virtue
- [[wiki/agent-systems/helpful-ai|Helpful AI]] — another virtue
- [[wiki/agent-systems/hha-standards|HHH Standards]] — the virtue bundle
- [[wiki/concepts/deontology-ai|Deontology for AI]] — the rule contrast
- [[wiki/concepts/value-specification|Value Specification]]
- [[wiki/concepts/utility-functions|Utility Functions]]
