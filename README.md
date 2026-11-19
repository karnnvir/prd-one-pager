# PRD One-Pager: a Claude skill for retail / e-commerce product managers

An interactive [Claude](https://claude.com) skill that interviews you, challenges weak inputs, and produces a detailed one-page PRD as a Word (.docx) document, followed by a full appendix. It is modelled on the rigor of big-tech PRDs (Walmart, Amazon, Google style) and tuned for retail, e-commerce and omnichannel products.

> **Disclaimer:** This project is independent and is not affiliated with or endorsed by Walmart, Amazon or Google. "Walmart-style" refers to general retail / e-commerce conventions. The skill never presents company-internal facts, metrics or system names as known. Any company-specific data must come from you or your documents.

## What it does

- **Ingests your material:** research docs, data analyses, customer feedback, strategy docs and draft PRDs (docx, pdf, xlsx, csv, pptx, md, txt), plus Jira, Confluence and Slack when those connectors are authorized.
- **Builds an evidence ledger:** every fact is tagged with its source and confidence (`Verified`, `Stated`, `Inferred`), and contradictions between sources are surfaced.
- **Interviews you** in batches of at most 5 questions, never re-asking what your documents already answer.
- **Pushes back** on weak answers: a solution posing as a problem, metrics with no baseline, missing guardrails, arbitrary targets, AI with no evals or cost model.
- **Finishes anyway:** when inputs are missing, it drafts the PRD and keeps gaps visible as `[OPEN: ...]` items with an owner and how to close them, all collected in an Open Questions appendix.
- **Covers AI features** when in scope: non-AI baseline, evals, ship gates, guardrails, human-in-the-loop, responsible AI, monitoring and unit economics.
- **Outputs a formatted Word document**, versioned (v0.1, v0.2...), which can be rebuilt after each round of answers.

## The PRD it produces

**Page 1 (the core)**
TL;DR - Customer problem - Business problem and sizing - Goals and non-goals - Proposed solution - Success metrics (primary, secondary, guardrail; each with definition, baseline, target, timeframe, source) - Scope and phasing - Top risks and dependencies - Decision / ask

**Appendix**
A. Customers, use cases and user stories
B. Research, data analysis and evidence ledger
C. Functional requirements (IDs, priorities, acceptance criteria)
D. AI module: rationale, data, model approach, **evals**, **guardrails**, human-in-the-loop, responsible AI, monitoring, unit economics (only if AI is in scope)
E. Non-functional requirements
F. Architecture and integrations
G. Experiment and measurement plan
H. Proposed roadmap
I. Launch, rollout and operations
J. Risks, assumptions and dependencies
K. Open questions
L. Alternatives considered
M. FAQ (optional, Amazon-style)
N. Glossary, sources and change log

## Install

Requires [Claude Code](https://claude.com/claude-code) or the Claude desktop app with skills support.

```bash
git clone <your-repo-url> ~/.claude/skills/prd-one-pager
pip3 install python-docx
```

Start a new Claude session so the skill is picked up.

## Use

In a Claude session, say something like:

- "Help me write a PRD for improving substitution acceptance in grocery pickup."
- "Turn these files into a PRD" (attach or point to your research, analysis, feedback and strategy docs).
- "Here is the Jira epic and the Confluence page; draft the PRD and tell me what is missing."

The skill then runs four phases:

1. **Orient:** title, surface, available inputs, whether AI is in scope.
2. **Ingest:** reads everything first and shows you "here is what I understood" to correct.
3. **Interview:** gap analysis, batched questions, pushback, `[OPEN]` items for what is parked.
4. **Draft and review:** checks the draft against a quality bar, builds `PRD - <title> - v0.1.docx`, and reports the open items and any contradictions found in your inputs.

## Connectors (optional)

Jira, Confluence and Slack are read through their Claude connectors. Authorize them via `/mcp` before use. Without them, the skill works from local files and what you tell it.

## Repository layout

```
prd-one-pager/
├── SKILL.md                       # workflow and instructions Claude follows
├── README.md
├── references/
│   ├── prd-template.md            # exact section structure and style rules
│   ├── intake-checklist.md        # blocking vs. nice-to-have inputs
│   ├── pushback-rules.md          # weak-answer patterns and how to challenge them
│   ├── ai-module.md               # AI scoping, evals, guardrails, responsible AI
│   ├── retail-ecommerce-context.md# retail metric vocabulary and domain prompts
│   └── quality-bar.md             # pre-delivery review checklist
└── scripts/
    └── build_prd_docx.py          # JSON spec -> formatted .docx (python-docx)
```

## Build the document directly (optional)

```bash
python3 scripts/build_prd_docx.py spec.json "PRD - My Feature - v0.1.docx"
```

See the header of `scripts/build_prd_docx.py` for the JSON spec format. It supports headings, paragraphs with **bold**, bullets, numbered lists, tables, callouts and page breaks, and highlights `[OPEN: ...]` items.

## Known limitations

- Docx layout (the "core fits on about one page" goal) has not been checked with a visual render in every environment. LibreOffice or Word is needed for that check.
- Architecture detail depends on what you provide; the skill flags it for Engineering to confirm rather than inventing internal systems.
- Jira, Confluence and Slack reading depends on the connectors being installed and authorized.

## Contributing

Issues and pull requests are welcome, especially real-world feedback on the interview flow, pushback rules, domain metrics and PRD layout. Please remove any confidential company data from examples.

## License

TBD. Add a license before publishing, for example MIT.
MIT; see [LICENSE](to be added). Use these however you like.

