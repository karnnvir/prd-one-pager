# PRD structure

Page 1 is the "one-pager" core. It is dense but scannable: short paragraphs, tables, bold lead-ins. Everything else goes in the appendix with cross-references ("see App. D").

## Header block (metadata table)
Title | Status (Draft vX.Y) | Author (PM) | Eng / Design / Data / Legal partners | Exec sponsor | Last updated | Target launch | Review forum / decision date.

## PAGE 1 - CORE

### 1. TL;DR (3-4 lines)
What we will build, for whom, why now, the expected outcome with a number, and the ask. Written last, placed first.

### 2. Customer problem
Who (segment/persona, size), what they are trying to do, what gets in the way, how often, what it costs them. Backed by at least one data point and one voice-of-customer quote or feedback theme. Describe the problem without describing the solution.

### 3. Business problem and opportunity
The business consequence in P&L / KPI terms: conversion, GMV, margin, cost-to-serve, NPS, retention, cancellations, associate productivity, etc. Include sizing with its math (`affected volume x rate x value = impact`) and the assumptions. Link to the company/org priority this supports and why now (market, competitor move, seasonal window, platform readiness).

### 4. Goals and non-goals
Goals: 3 or fewer, outcome-oriented. Non-goals: real exclusions someone might reasonably expect (and why excluded).

### 5. Proposed solution
What we will build in plain language, the core experience, and the key design choice that makes it work. Mention channels/surfaces (app, web, store, associate app, seller portal). Include 1-2 sentences on alternatives rejected (detail in App. L). If AI is involved: what the AI does, what it does not do, and the human fallback.

### 6. Success metrics (table)
Columns: Type (Primary / Secondary / Guardrail) | Metric and exact definition | Baseline | Target | Timeframe | Data source / owner.
One primary. 2-4 secondary. 2+ guardrails. Add a line on how it will be measured (A/B, holdout, pre/post) and the minimum detectable effect if known.

### 7. Scope and phasing (one-line view)
MVP / V1 / V2 in one line each with the target date. Detail in App. H.

### 8. Top risks and dependencies
Top 3-5 only: risk | likelihood / impact | mitigation | owner. Critical dependencies (teams, platforms, vendors, data).

### 9. Decision / ask
The specific decision, funding, headcount or approval needed, by when, and from whom.

## APPENDIX

- **A. Customers, use cases and user stories** - personas with context; 5-10 prioritized use cases or stories ("As a ..., I want ... so that ..."), each with acceptance criteria; key journeys including edge and failure cases; omnichannel variants (online, pickup, delivery, in-store, associate).
- **B. Research, data analysis and evidence ledger** - summary of each source (what it is, key finding, confidence), data tables, VoC themes, competitive benchmarks, contradictions between sources.
- **C. Functional requirements** - table: ID | Requirement | Priority (P0/P1/P2) | Rationale / story link | Acceptance criteria | Status. Use "must / should / may" wording sparingly and consistently.
- **D. AI module (only if AI in scope)** - D1 AI rationale and non-AI baseline; D2 task definition, inputs/outputs; D3 data (sources, quality, labeling, privacy, freshness); D4 model approach (build/buy/fine-tune, latency and cost budget); D5 **Evals** (offline golden set, online metrics, human review, LLM-judge calibration, thresholds to ship, regression gates, cadence); D6 **Guardrails** (input/output filtering, policy, grounding, refusal behavior, rate limits, PII, prompt-injection defenses, kill switch); D7 human-in-the-loop and fallbacks; D8 responsible AI (fairness, safety, transparency, explainability, customer disclosure); D9 monitoring and drift; D10 unit economics (cost per call/task vs. value).
- **E. Non-functional requirements** - table: Category | Requirement | Target | How verified. Cover performance/latency (p50/p95/p99), scalability and peak events (e.g., holiday, Black Friday-style peaks), availability/SLO, reliability and graceful degradation, security, privacy and compliance (PII, PCI, CCPA/GDPR, accessibility WCAG), observability, localization, cost, maintainability, data retention, backward compatibility.
- **F. Architecture and integrations** - high-level system diagram described as a component list and flow (or an embedded diagram if provided), services and data stores touched, APIs/events, build vs. reuse, data flows, key technical decisions and open design questions (flag as for Eng to confirm; never invent internal system names).
- **G. Experiment and measurement plan** - hypotheses, design (A/B, switchback, geo holdout), unit of randomization, sample size / duration, success and stop criteria, instrumentation and event schema, dashboards.
- **H. Proposed roadmap** - phases (MVP, V1, V2) with scope, milestones, dates, exit criteria, team and dependencies; a Now/Next/Later view if dates are uncertain.
- **I. Launch, rollout and operations** - rollout stages and ramp, comms/GTM (customers, associates, sellers, support), training, support readiness, rollback criteria, on-call and runbook ownership.
- **J. Risks, assumptions and dependencies (full)** - risk register with owners; assumptions to validate with how; cross-team dependencies and status.
- **K. Open questions** - table: # | Question | Why it matters / what it blocks | Owner | Due | Proposed way to close. Every inline `[OPEN]` appears here.
- **L. Alternatives considered** - options with pros, cons, why not chosen (including "do nothing").
- **M. FAQ (optional, Amazon-style)** - customer-facing and internal hard questions with honest answers. Optional press-release paragraph if the PM wants a working-backwards view.
- **N. Glossary, sources and change log** - terms, links to inputs, version history.

## Style rules
- Lead every paragraph with the point. Prefer tables for comparisons, numbers and requirements.
- Define each metric precisely (numerator, denominator, window, segment).
- State confidence next to estimates ("estimate, medium confidence; assumes X").
- Short sentences. No filler ("leverage", "best-in-class", "seamless").
