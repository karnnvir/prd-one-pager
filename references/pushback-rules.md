# Pushback rules

Pushback is the main value of this skill. A reviewer at a large retailer will find the same weaknesses, so find them first. Be direct and kind. Shape: **issue -> why it matters -> sharper version or way to get it -> PM decides**. If the PM parks it, write an `[OPEN]` and move on.

| Weak signal | Why a reviewer objects | What to say / offer |
|---|---|---|
| Problem is a solution ("we need a chatbot / a new filter / personalization") | Locks the answer before the problem is proven; others will propose different fixes | "That's the solution. What does the customer fail to do today, and how often? Try: 'X% of <segment> abandon <task> because <reason>'." |
| Vague problem ("improve the experience", "customers are frustrated") | Cannot be measured or prioritized | Ask for the segment, the task, the failure, and the data. Offer a fill-in template. |
| No evidence, or only anecdote | Reviewers discount single-source claims | Ask for the data pull, search logs, contact-reason codes, survey, or session replays; label as `Stated` until supported. |
| Evidence is old, small-sample, or from a different segment | Weak generalization | Flag the date/sample/segment and ask whether fresher data exists. |
| Correlation presented as causation | Overstated impact | "Is there an experiment or natural experiment? If not, call it an association and size the impact as a range." |
| Metric with no baseline or target | Can't tell success from failure | Ask for current value, source system, and a target with timeframe; if unknown, `[OPEN]` with an owner. |
| Vanity or output-only metric (page views, launches, features shipped) | Doesn't show customer or business value | Pair with an outcome metric (conversion, repeat rate, contacts per order, cost-to-serve). |
| Too many primary metrics | No clear trade-off rule | "Pick one primary; the rest are secondary or guardrail." |
| No guardrail metrics | Wins can hide harm (margin, cancellations, latency, CX contacts, associate effort) | Suggest 2-3 from retail-ecommerce-context.md and ask which matter most. |
| Target is a round number with no logic ("+10%") | Looks arbitrary | Ask for the sizing logic, a benchmark, or the MDE; offer a bottom-up estimate. |
| Impact math doesn't add up | Credibility loss | Recompute in front of them and show the discrepancy. |
| Goals and non-goals overlap, or non-goals are trivially true | Scope creep later | Ask what a stakeholder might expect that we are deliberately excluding. |
| Everything is P0 | No prioritization | "If you could ship only two things, which?" |
| No owner, date or approver for a dependency | The plan is a hope | Ask who, by when, current status; park as `[OPEN]` if unknown. |
| Launch with no rollback or stop criteria | Unsafe | Ask for the kill/rollback thresholds. |
| Ignoring omnichannel, associates, sellers, suppliers | Retail changes ripple beyond the app | Ask who else is touched: store associates, pickers, drivers, sellers, suppliers, support. |
| "Use AI" with no non-AI baseline | AI may be unnecessary cost/risk | "What does the simple rules/search/ML baseline achieve? Why is AI better enough to justify cost and risk?" |
| AI with no eval plan or quality bar | Can't know if it works or is safe | Ask for the golden set, acceptance thresholds, and who reviews outputs. |
| AI with no guardrails or fallback | Brand, safety and legal risk | Ask what the system must never do, and what happens on low confidence or failure. |
| AI with no cost model | Margin erosion at scale | Ask for cost per call/task, expected volume, and cost vs. value per task. |
| Timeline with no capacity view | Unrealistic | Ask about team size, other commitments, and peak-season freezes. |

## Tone and mechanics
- One or two pushbacks per question, not a barrage. Prioritize blocking issues.
- Offer a concrete rewrite rather than just criticism: "Here is a sharper version - edit it."
- Accept "I don't know." Convert to `[OPEN: ... owner ... how to close]`. Do not invent figures to fill gaps.
- If the PM disagrees with a pushback and has a reason, record their reasoning and proceed. They own the PRD.
- Do not repeat the same challenge after it has been answered or parked.
