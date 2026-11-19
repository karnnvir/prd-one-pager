# Intake checklist

Tier 1 = blocking: the PRD is not credible without it, so push until it is answered or consciously parked as `[OPEN]`. Tier 2 = strongly wanted: ask, but accept "not yet". Tier 3 = nice to have: ask only if the PM seems to have it handy.

## Tier 1 - Blocking
1. **Customer problem**: who exactly (segment, size), what they are trying to do, what blocks them, frequency, consequence.
2. **Business problem**: the KPI/P&L consequence and a size-of-prize estimate with its math.
3. **Evidence**: at least one quantitative signal and one qualitative signal. Where it came from and how recent.
4. **Business goal** and the org/company priority it supports; why now.
5. **Primary metric** with exact definition, baseline, target, timeframe, data source.
6. **Secondary metrics** and **guardrail metrics** (what must not degrade).
7. **Proposed solution** at concept level and the intended scope (MVP).
8. **Non-goals**.
9. **The decision/ask** and the forum/date.
10. If AI is in scope: why AI, the quality bar and how it will be evaluated, the guardrails (see ai-module.md).

## Tier 2 - Strongly wanted
- Personas / segments and top use cases; current-state journey and pain points.
- Competitor or market benchmarks.
- Alternatives considered (including non-AI and do-nothing).
- Stakeholders, partner teams, exec sponsor, approvers (legal, privacy, security, finance, merchandising, store ops, supply chain, seller ops).
- Constraints: timeline, headcount, budget, tech platform, regulatory, peak-season freezes.
- Dependencies and their status.
- Experiment/measurement approach and instrumentation availability.
- Rollout approach and rollback criteria.
- Known risks and what is already de-risked.
- Cost estimate (build + run).

## Tier 3 - Nice to have
- Technical architecture sketch, existing services to reuse, API/event contracts.
- NFR targets (latency, availability, scale, compliance).
- Roadmap beyond MVP; long-term vision.
- Pricing/margin/fee implications; seller or supplier impact.
- GTM and associate/support enablement plan.
- Prior attempts and why they failed; relevant past experiments.
- Press-release / FAQ framing.

## Source-reading prompts (for Phase 1)
For each uploaded or linked item, extract: the claim, number, date, sample size, segment, and caveat. Flag stale data (older than 12 months or pre-major-change), small samples, survivorship or selection bias, and contradictions between documents.

## Questions to ask only when not already answered
- "What is the single number you want to move, and what is it today?"
- "What would make you kill or pause this after launch?"
- "Who is hurt if this goes wrong, and how would we find out?"
- "What are we choosing NOT to do, and who might be disappointed?"
- "Which part of this are you least sure about?"
