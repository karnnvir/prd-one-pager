# AI module (use when AI/ML/GenAI/agents are in scope)

AI features at retail scale fail in predictable ways: no clear quality bar, no eval harness, weak guardrails, and costs that scale faster than value. Interview the PM on each block below, push back with pushback-rules.md, and park unknowns as `[OPEN]`. Output goes to Appendix D, and the one-line AI summary goes on page 1.

## D1. Why AI
- What is the task? Classify, rank/recommend, extract, generate, summarize, converse, plan/act (agent), predict/forecast?
- What does the best non-AI baseline (rules, search, classic ML, manual) achieve today? What is the expected lift from AI and what does it cost?
- What happens if the AI is wrong, slow or unavailable? Is the failure cost low (suggestion) or high (price, payment, health/safety, regulated category, order changes)?

## D2. Task, inputs, outputs
Define inputs (query, catalog, order, behavior, images, policy docs), outputs (text, ranking, structured action), autonomy level (suggest / draft / act with approval / act autonomously), and who sees the output (customer, associate, seller, internal).

## D3. Data
Sources and owners, volume, freshness, quality issues, labeling approach and cost, PII/PCI presence, consent and retention, data-sharing constraints (sellers, suppliers, partners), grounding sources (catalog, inventory, price, policy, knowledge base), and how stale data is handled (e.g., price/inventory changes).

## D4. Model and system approach
Build / buy / fine-tune / prompt + retrieval; model options considered; latency budget (p95) and throughput; context/grounding strategy; tool/API access for agents; versioning and rollback; vendor and data-residency constraints. Do not invent internal platform names; mark as "Eng to confirm".

## D5. Evals (the most important block)
- **Quality dimensions** to measure (pick those relevant): correctness/accuracy, relevance, groundedness / hallucination rate, completeness, safety/toxicity, policy compliance, tone/brand, bias/fairness across segments, robustness (typos, multilingual, adversarial), latency, cost.
- **Offline evals**: golden dataset (size, source, who labels, refresh cadence, segment coverage including long tail and seasonal), metrics and thresholds, human review protocol (rubric, rater count, agreement), LLM-as-judge (rubric, calibration vs. humans, known biases), regression suite.
- **Online evals**: A/B design, shadow mode, canary, key online metrics tied to the business goal, guardrail metrics, stop criteria.
- **Ship gates**: explicit thresholds per dimension that must be met to move MVP -> beta -> GA, who signs off.
- **Ongoing**: cadence of re-evaluation, drift detection, feedback loop from customer thumbs/complaints/escalations into the eval set, incident review process.
Push back hard if the PM has no quality bar, no golden set plan, or no owner for evaluation.

## D6. Guardrails
- **Must-never list** (e.g., invent prices/promos/availability, make medical or legal claims, expose PII, take irreversible actions without confirmation, disparage competitors, discuss restricted categories).
- Input guardrails: prompt-injection and jailbreak defense, PII redaction, abuse and rate limits, topic scoping.
- Output guardrails: grounding checks, policy and safety classifiers, structured-output validation, price/inventory verification before display, confidence thresholds with refusal or handoff.
- Action guardrails for agents: permission scopes, human approval for money/orders/account changes, idempotency, audit logs, spend and action caps.
- Operational: kill switch, feature flags, per-segment rollout, monitoring and alerting, incident runbook.

## D7. Human in the loop and fallbacks
Where humans review (associates, CX agents, merchandisers), escalation paths, graceful degradation to the non-AI experience, and the customer-visible behavior when the AI declines.

## D8. Responsible AI and compliance
Fairness across customer segments and regions; transparency and AI disclosure; explainability appropriate to the surface; privacy (data minimization, consent, retention); IP/copyright of generated content; regulatory review (privacy, consumer protection, accessibility, advertising claims); review by legal/privacy/security/RAI forums as applicable.

## D9. Monitoring and drift
Dashboards and alerts for quality, safety incidents, latency, cost, usage, fallback rate, user feedback; retraining or prompt-update cadence; ownership (who gets paged).

## D10. Unit economics
Cost per request/task (inference, retrieval, labeling, human review), expected volume, cost vs. value per task (incremental margin, contacts avoided, labor saved), break-even, and cost levers (caching, smaller models, routing, batching). Flag if projected cost at peak exceeds value.

## Page-1 AI line (template)
"AI does <task> for <user> using <data>; it will not <must-never>; ships when <eval gate>; falls back to <baseline>; cost <$x per task> vs value <$y>."
