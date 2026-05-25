# internet-product-factory

`internet-product-factory` is a local, markdown-first workflow for repeatedly discovering, evaluating, building, auditing, packaging, and reflecting on internet products.

The factory no longer optimizes for output count. It optimizes for public GitHub asset value.

The factory is now a file-driven, substage-based workflow state machine.

## Current Operating Rule
A runnable CLI is not automatically a product.

Checklist tools, simple analyzers, README optimizers, config checkers, log summarizers, `.env` sync tools, thin prompt wrappers, simple parsers, and one-file CLIs are `INTERNAL_FACTORY_TOOL` by default. They may be useful, but they do not consume public GitHub release slots unless upgraded into a deeper product.

A product can be small, but it cannot be shallow.

The factory now also blocks a newer low-depth pattern: reused frontend shell plus shallow rule-based backend. Similar products are acceptable only when each product has a meaningfully deep core mechanism, product-specific UI, realistic fixtures, edge-case coverage, and actionable output.

## Source Of Truth
The local markdown files are the source of truth.

If chat context is lost, resume from:

1. `products/_product-index.md`
2. the latest product folder
3. latest `next-stage-brief.md`
4. latest `checkpoint.md`
5. latest `stage-report.md`
6. relevant substage files
7. relevant files in `memory/`

Do not rely on chat memory.
Do not rely on Codex memory.
Do not rely on implicit context.

## File-Driven Workflow
Every major stage is decomposed into concrete substages.

Each substage writes its own Markdown evidence file. A major stage is incomplete until:
- all required substage files exist
- completed substage files meet the 500 meaningful word rule
- `stage-report.md` synthesizes the substage evidence
- `checkpoint.md` records recovery state
- `decision-log.md` records decisions
- `next-stage-brief.md` compresses the handoff for the next stage

The next major stage must read the previous `next-stage-brief.md` first. It should read the full `stage-report.md` or individual substage files only when more detail is needed.

## Workflow Substance Audit

File existence is not enough. A product is not workflow-complete if the stage folders exist but the reasoning is still scaffold text.

Before claiming a product completed the full workflow, run:

```bash
python scripts/audit_workflow_substance.py --strict product-XXX
```

This audit checks for:
- `Status: NOT_STARTED` residue in completed products
- heavy `TBD` scaffold residue
- one-module core implementation risk
- shallow test and fixture matrix
- missing user-ready artifact when the product needs more than a dashboard/report

The Product-025 lesson is now the benchmark: strong products complete evidence, method, modular architecture, fixture matrix, audit, and packaging as one chain. Do not treat validator success as product depth.

```text
Batch Discovery
-> Substage Evidence Files
-> Stage Synthesis
-> Launch Slot Scoring
-> Q-Gate
-> Deep Build
-> Multi-Agent Audit
-> Packaging
-> Feedback
-> Memory Update
```

## 500 Meaningful Word Rule
Every completed substage must contain at least 500 meaningful words.

Word count alone is not enough. Failure modes include:
- generic business-school language
- vague AI trend commentary
- unsupported claims
- repeated statements
- empty lists
- motivational writing
- content that does not affect a decision

If evidence is unavailable, write a blocker instead of fabricating research.

## Evidence-First Rule
The 500-word rule is not enough.

Every research, demand, scoring, Q-Gate, product discovery, audit, and packaging substage must follow this sequence:

```text
Collect evidence
-> Evidence Pack
-> Source Log
-> Analysis
-> Decision
```

No evidence, no conclusion. No robustness, no ranking. No demo, no public product.

Every major claim in Analysis must reference evidence IDs from the Evidence Pack. Unsupported ideas belong under Weak Hypotheses. If evidence is unavailable, write:

```text
Evidence unavailable. This is a hypothesis, not a finding.
```

Completed data-heavy substages must include baseline analysis, robustness check, sensitivity check, error/outlier check, interpretation, and decision impact. If baseline and robustness disagree, the workflow chooses the more conservative classification.

Confidence levels are `HIGH`, `MEDIUM`, `LOW`, and `SPECULATIVE`. A candidate cannot pass Q-Gate mainly on `LOW` or `SPECULATIVE` evidence, and cannot become `PUBLIC_PRODUCT` unless demand evidence and demo potential are at least `MEDIUM`.

## Broad Demand Discovery Rule

Do not preselect the audience. Do not default to developer tools. Do not force non-developer products.

The factory starts from broad market demand discovery, then lets evidence decide the strongest opportunity. Developer tools are allowed when they truly win the evidence comparison, but they cannot win by default just because Codex works inside code repositories or GitHub rewards developer-facing projects.

Stage 1 must inspect multiple demand pools before selecting product ideas:

- Developer / AI builder / technical workflow users
- Students / international students / applicants
- Job seekers / career planners
- Creators / content workers / solo operators
- Small business / freelancers
- Personal finance / budgeting / decision-making users
- Life admin / family admin / healthcare admin users
- Productivity / AI tool users
- Education / tutoring / learning users
- Emerging niches discovered during search

For each pool, collect pain signals, source references, candidate opportunities, evidence quality, feasibility, distribution path, and likely product format when available. If evidence is unavailable, record the gap instead of fabricating demand.

The workflow now includes `demand-bias-check.md`. If more than 60% of sources are developer sources, flag `DEV_SOURCE_BIAS`. If more than 70% of candidates are developer tools, require written justification. If the winner is a developer tool, compare it against the top non-developer candidate. If the winner is non-developer, compare it against the top developer candidate.

The final selected product must explain why the audience/problem won, what evidence supports it, which competing opportunities were rejected, why category bias did not decide the outcome, and why this is not merely the easiest thing for Codex to build.

## Implementation Depth Rule

Frontend is not product depth. Smoke test is not product depth. README polish is not product depth. A static rule scanner is not automatically a public product.

A reused scaffold is allowed, but a shallow core is not. A product can use a similar architecture only if its core implementation is meaningfully deep enough to justify publication.

Future products must pass these gates:

- `Implementation Depth Gate`: scores Core Logic Depth, Parser/Data Understanding Depth, Edge Case Coverage, Output Actionability, Test Depth, UI Specificity, Integration/Automation Depth, and Non-Trivial Mechanism Depth.
- `UI Specificity Gate`: requires product-specific views and domain-specific visualization, not only a generic upload/report shell.
- `Core Mechanism Requirement`: requires at least one non-trivial mechanism such as AST parser, schema diff engine, dependency graph, permission graph, attack path analysis, timeline reconstruction, auto-fix patching, sensitivity analysis, benchmark suite, SDK/proxy/plugin/GitHub Action, multi-file project analysis, or configurable rule engine.
- `Fixture and Edge Case Depth`: requires multiple realistic examples, edge cases, malformed input, complex input, and no-issue cases when relevant.
- `Output Actionability Gate`: requires precise locations, severity, confidence, explanation, recommended fixes, false-positive notes when relevant, and next actions.

Hard launch rules:

- Core Logic Depth < 5 blocks `PUBLIC_PRODUCT`.
- Core Logic Depth < 7 blocks `TOP_10_PUBLISH`.
- UI Specificity < 5 blocks `TOP_10_PUBLISH`.
- Test Depth < 5 blocks `TOP_10_PUBLISH`.
- Output Actionability < 6 blocks `TOP_10_PUBLISH`.
- Non-Trivial Mechanism Depth < 6 blocks `TOP_10_PUBLISH`.
- Toy Implementation Risk > 6 blocks `TOP_10_PUBLISH`.
- If the product is mainly keyword/regex scanning, it must add depth through AST parsing, graph analysis, auto-fix, benchmark, real imports, confidence scoring, configurable rules, or regression tests over multiple fixtures.

## Real-World Depth Rule

A real core mechanism is not enough if the product only handles toy examples. Future products must prove real-world depth before `TOP_10_PUBLISH`.

The workflow now checks:

- Ecosystem compatibility: support real variants, not only the happy path.
- External data integration: security, pricing, vulnerability, market, or risk claims need authoritative data or honest structural/local scope.
- Remediation depth: findings must include affected path, severity, confidence, why it matters, specific fix options, and next command/action.
- Real corpus benchmark: test on realistic, complex, and large cases when relevant; record node count, edge count, runtime, findings count, and false-positive concerns.
- CI / automation readiness: developer tools need CLI/export/CI paths such as `--ci`, JSON, Markdown, SARIF, GitHub Actions, or exit-code thresholds.
- UI domain specificity: dependency products need path explorer, duplicate cluster, hotspot ranking, risk propagation map, or direct dependency blame table.
- README claim honesty: do not call structural analysis vulnerability scanning without advisory data.

Products with only toy fixtures cannot become `TOP_10_PUBLISH`.

## Business Workflow Depth Rule

Non-developer operational products must reduce real operating work. They cannot pass as strong public products just because they import a CSV, calculate a score, show a dashboard, generate a report, or write generic recommendations.

This gate applies to inventory planning, invoice follow-up, budgeting, procurement, scheduling, hiring, applicant planning, sales operations, small business workflows, personal finance workflows, education planning, and similar workflows.

Future business products must pass:

- `Business Workflow Depth Gate`: answer what to do next, what to do first, why, under what constraint, with what risk, and what changes if assumptions change.
- `Data Sufficiency Gate`: prove required data is naturally available, explain required and optional fields, warn on missing fields, and downgrade confidence when data is incomplete.
- `Business Constraint Gate`: model or explicitly handle meaningful constraints such as budget, cash flow, lead time, MOQ, storage, shelf life, time, labor, seasonality, compliance, or priority tradeoffs.
- `Source-System Preset Gate`: do not say "supports CSV" as if all exports are equal; identify source systems, column variants, presets, or flexible mapping needs.
- `Operational Actionability Gate`: produce action, priority, expected impact, risk, required input/resource, and next step.
- `What-if / Constraint Simulation Gate`: test at least one assumption or constraint change for decision-support products.
- `Realistic Business Fixture Gate`: use messy realistic samples with missing fields, malformed values, edge cases, no-action rows, high-priority rows, low-priority rows, and conflicting priorities.

Hard launch rules:

- Spreadsheet Trap Risk > 6 blocks `TOP_10_PUBLISH`.
- Business Constraint Depth < 5 blocks `TOP_10_PUBLISH` for operational products.
- Operational Actionability < 6 blocks `TOP_10_PUBLISH`.
- Data Sufficiency Score < 6 requires `FIX_BEFORE_SHIP` or `NEEDS_V2_BEFORE_LAUNCH`.
- If missing fields silently produce confident output, the product cannot launch as a strong public product.
- A spreadsheet analyzer with a web UI is not enough.

## Disciplinary Method Fit Rule

A strong product should have a natural analytical method core. It should not merely parse input, score a few fields, and generate a report.

The workflow now asks what discipline or analytical tradition fits the problem before build. Decision products may need multi-criteria decision analysis, utility ranking, scenarios, sensitivity, Monte Carlo, devil's advocate review, or multi-perspective synthesis. Inventory products may need reorder points, safety stock, lead-time demand, budget constraints, and supplier-delay sensitivity. Dependency products may need graph traversal, blast radius, path explanation, and advisory data if claiming security. Deadline or return-policy products may need policy rule matching, deadline basis detection, confidence scoring, evidence checklists, and reminders.

The method must fit the problem. Do not force Monte Carlo, multi-agent debate, optimization, graph analysis, or AI classification into products that do not need them. No method theater. No fake complexity.

Future products must pass:

- `Disciplinary Method Fit Gate`: identify the natural discipline, fitting methods, unfitting methods, minimum serious method core, shallow failure mode, and over-engineering failure mode.
- `Method Depth Gate`: score Method Fit, Method Depth, Uncertainty Handling, Assumption Challenge, Cross-Validation, and Decision Impact.
- `Multi-Perspective Reasoning Gate`: for judgment, planning, prioritization, risk, strategy, or tradeoff products, require scenario analysis, user-adjustable assumptions, sensitivity analysis, confidence scoring, assumption review, devil's advocate critique, or synthesis.

Hard launch rules:

- Method Fit < 6 blocks `TOP_10_PUBLISH`.
- Method Depth < 6 blocks `TOP_10_PUBLISH` for analytical products.
- Shallow Scoring Risk > 6 blocks `TOP_10_PUBLISH`.
- Method Theater Risk > 6 blocks `TOP_10_PUBLISH`.
- If uncertainty matters but is ignored, downgrade launch readiness.
- If assumptions drive recommendations but are never challenged, downgrade launch readiness.
- If the product makes recommendations, it must explain what assumptions would flip the recommendation.

The AI Decision Engine is the reference pattern: it is stronger because it uses a coherent method architecture, not because it adds complexity for its own sake.

## Classification System
Every candidate must be classified before build:

- `PUBLIC_PRODUCT`: external-user product that may become a standalone public GitHub repo.
- `INTERNAL_FACTORY_TOOL`: useful inside this factory, but not a standalone public repo.
- `EXPERIMENT`: validates a mechanism or demand signal.
- `PARK`: promising but not ready.
- `KILL`: weak, risky, shallow, or not worth more work.

Only `PUBLIC_PRODUCT` can become a standalone GitHub repo.

## Public Product Minimum Bar
Public products must have:

- specific external user persona
- strong external user pain
- complete user journey
- interactive surface, such as local web app, dashboard, simulator, report generator, visualizer, or strong multi-step CLI
- sample input and output
- screenshot-worthy demo moment
- non-trivial mechanism
- strong README first screen
- clear GitHub description and topics
- quickstart
- tests or smoke test
- low 30-minute copy risk

If a competent developer can copy 80 percent of the product in 30 minutes, downgrade it to `INTERNAL_FACTORY_TOOL` unless it belongs to a larger product suite.

## Lifecycle
1. Context Setup
2. Demand Discovery
3. Demand Scoring / Launch Slot Ranking
4. Q-Gate / Kill-or-Continue Decision
5. Product Discovery
6. MVP Specification
7. Build Execution
8. Multi-Agent Audit
9. Packaging / Marketing / Launch
10. Post-Launch Feedback
11. Reflection / Memory Update

## Batch Logic
The factory may discover many ideas, but it should build only one high-quality `PUBLIC_PRODUCT` first unless explicitly instructed otherwise.

Daily public GitHub slots are scarce. Stage 2 ranks candidates by launch-slot value, and Stage 3 kills or downgrades weak ideas before build.

## Internal Tools
Internal tools live under `internal-tools/` and are tracked in `internal-tools/_internal-tool-index.md`.

Examples from the failed first batch:
- LaunchLint
- LaunchSlot Ranker
- Repo About Optimizer
- README FirstScreen
- EnvExample Sync
- CI Fail Digest

These are useful factory components, not standalone public products by default.

## Bilingual GitHub Launch

Stage 8 supports bilingual GitHub packaging.

Default launch structure:

- English main/default branch: primary public GitHub asset, optimized for broad discovery. `README.md`, repo description, topics, demo instructions, and launch posts should clearly explain what the product does, which pain it solves, and how to try it quickly.
- Chinese branch, usually `zh-CN`: Chinese GitHub-facing documentation. Only descriptive and promotional materials change. App code, product UI, tests, sample schemas, API routes, environment variables, and commands stay unchanged unless product localization is explicitly requested.

Important GitHub limitation: repo About description and topics are repository-level, not branch-level. The default is to keep repo-level metadata in English and put the Chinese version in the `zh-CN` branch README and Chinese launch materials.

Required Stage 8 bilingual files:
- `readme-final.md`
- `readme-final-zh-CN.md`
- `github-description.md`
- `github-description-zh-CN.md`
- `github-topics.md`
- `launch-posts.md`
- `launch-posts-zh-CN.md`
- `bilingual-github-release-plan.md`

Before push, run the smoke test, workflow validation, and secret scan. Public GitHub upload still requires explicit user approval because it transmits local files to GitHub.

## GitHub Launch Page Gate

Future public repos must read like product pages, not internal technical notes.

Every `PUBLIC_PRODUCT` must include:

- `README.md`: English default README.
- `README.zh-CN.md`: complete natural Chinese README.
- `github-description.md`: short description under 160 characters, longer description, and 3 alternatives.
- `github-topics.md`: 10-20 relevant domain and product-type topics.
- `launch-summary.md`: final packaging decision and launch assets.
- `readme-claim-check.md`: proof that README claims match implemented functionality.

The README first screen must answer within 10 seconds: what this is, who it is for, what pain it solves, what output it creates, why a visitor should care, and how to try it.

Required README structure:

1. Hero Section
2. Problem
3. Why Existing Approaches Are Not Enough
4. What This Project Does
5. Key Features
6. Demo / Screenshots
7. Quick Start
8. Example Input / Output
9. Use Cases
10. How It Works
11. Project Structure
12. Roadmap
13. Limitations
14. License
15. Language link

Every README must include a `Why this is useful` section with concrete differentiation. Generic claims such as "improves productivity" are not enough.

Limitations must be grouped near the end. Do not scatter self-sabotaging caveats through the hero, problem, features, or quickstart. The README should be honest, but it should not weaken the product before the visitor understands its value.

Stage 7 now includes a GitHub README Reviewer. If that reviewer cannot understand the project in 10 seconds, would not keep reading, or finds overclaiming, missing demo evidence, scattered limitations, weak English, or awkward Chinese copy, the product cannot ship.

## NIM API Capability
Future products may use NVIDIA NIM as a real AI/API capability, but secrets must never be written to disk.

Use environment variables:

```bash
NVIDIA_NIM_API_KEY=your_nvidia_nim_api_key_here
NVIDIA_NIM_BASE_URL=your_nvidia_nim_base_url_here
NVIDIA_NIM_MODEL=your_model_name_here
```

NIM-powered products must include mock mode and must run without a real key for normal smoke tests.

## How To Start A New Product
Use the helper:

```bash
python scripts/create_product_folder.py product-011
python scripts/update_product_index.py
```

Then begin at `00_context` and do not build until Stage 2 classification and Stage 3 Q-Gate approve a `PUBLIC_PRODUCT`.

The helper scaffolds all substage files, stage synthesis files, checkpoints, decision logs, and `next-stage-brief.md` handoffs.

## Checkpoints
Every stage has a `checkpoint.md`.

Each checkpoint must answer:
- What was completed?
- What evidence supports completion?
- What files were created or modified?
- What decision was made?
- Can the workflow move to the next stage?
- If not, what is blocking it?

## Validation
Run:

```bash
python scripts/validate_stage_files.py
```

This checks required root files, workflow files, templates, internal-tool index, product stage files, and stage-specific artifacts.

## Product Depth Doctrine

A frontend does not equal product depth. A backend does not equal product depth. A smoke test proves that something runs; it does not prove that the product does meaningful work for a real user.

Manual JSON is acceptable for demo mode, but not as the primary user experience unless the product is explicitly a developer config tool. A strong product reduces user work; it does not ask the user to collect every important value, research prices, estimate token counts, invent failure rates, and then admire a formatted calculator output.

Future products must pass these gates before they can be treated as strong `PUBLIC_PRODUCT` or `TOP_10_PUBLISH` candidates:

- Core Capability Gate: the non-trivial capability must be implemented, not merely implied by README copy.
- Input Automation Gate: real users need an import, parser, integration, SDK, proxy, API, or low-friction data path.
- User Friction Gate: a time-poor target user must reach first useful output without doing most of the product's work manually.
- Configuration Freshness Gate: changing prices, model lists, limits, datasets, or rules must be editable, importable, versioned, or updateable.
- Accuracy / Estimation Quality Gate: quantitative output must separate measured, estimated, assumed, uncertain, and decision-impacting values.
- Real Data Path Gate: sample JSON alone is demo data, not real data support.
- Frontend Calculator Trap Rule: a product with a UI is still shallow if it mainly asks users to enter all important values, runs deterministic formulas, and formats a report.

If a product has frontend + backend + README + sample JSON + smoke test but lacks core capability depth, input automation, real data support, and configurable assumptions, classify it as `EXPERIMENT`, `INTERNAL_FACTORY_TOOL`, `PARK`, or `NEEDS_V2_BEFORE_LAUNCH`.
