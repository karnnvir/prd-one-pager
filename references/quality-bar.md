# Quality bar (run before delivering any draft)

Fix failures before showing the PM. Where the fix needs PM input, add an `[OPEN]` instead.

## Page 1
- [ ] TL;DR states what, for whom, why now, expected outcome (a number), and the ask.
- [ ] Customer problem and business problem are separate, each with evidence and no solution language.
- [ ] Sizing math is shown, assumptions listed, and the arithmetic is right.
- [ ] 3 or fewer goals; non-goals are genuine exclusions.
- [ ] Metrics table has exactly one primary, 2-4 secondary, 2+ guardrails; each with definition, baseline, target, timeframe, source (or an `[OPEN]`).
- [ ] Risks list is top 3-5 with mitigations and owners.
- [ ] The ask names a decision, an approver and a date.
- [ ] Reads in under 5 minutes; no paragraph longer than 4 lines; no jargon undefined.

## Integrity
- [ ] No fabricated numbers, quotes, benchmarks, competitor facts or internal system names. Every figure traces to the evidence ledger or is marked as an estimate/assumption.
- [ ] Confidence is labelled where evidence is `Stated` or `Inferred`.
- [ ] Contradictions among inputs are surfaced, not smoothed over.
- [ ] Every inline `[OPEN]` appears in Appendix K with owner and how to close.

## Completeness
- [ ] Appendix covers A-K (and L, M, N as relevant) as in prd-template.md, with no empty headings (write "Not applicable - <reason>" or `[OPEN]`).
- [ ] Requirements have IDs, priorities and acceptance criteria; not everything is P0.
- [ ] NFRs have measurable targets and verification methods.
- [ ] Roadmap has exit criteria for each phase.
- [ ] If AI is in scope: non-AI baseline, eval plan with ship gates, must-never list and guardrails, fallback, monitoring, cost model are all present.

## Docx
- [ ] Core fits on about one page (up to a tight page and a half); tables render; `[OPEN]` items highlighted; header/footer and page numbers present; file name `PRD - <title> - vX.Y.docx`.
