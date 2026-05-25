# AGENTS.md

Instructions for future Codex agents working in `internet-product-factory`.

## Execution Mode
1. You are an execution agent, not an advisor.
2. Modify repository files directly when the user asks for execution.
3. Do not stop after writing a plan unless the active collaboration mode requires planning only.
4. Do not create placeholder-only files and claim completion.
5. Do not claim completion without file changes and verification.
6. Do not generate shallow standalone CLI tools unless explicitly requested.
7. Do not push to GitHub unless the user explicitly asks for launch.

## Source Of Truth
Local markdown files are the source of truth.

Resume in this order:
1. `products/_product-index.md`
2. the latest product folder
3. latest `next-stage-brief.md`
4. latest `checkpoint.md`
5. latest `stage-report.md`
6. relevant substage files
7. relevant files in `memory/`

Do not rely on chat memory. Do not rely on Codex memory. Do not rely on implicit context.

## Substage Execution Protocol
- Never complete a major stage as one generic report.
- Every major stage must be decomposed into substages.
- Every substage must write its own Markdown file.
- Every completed substage must contain at least 500 meaningful words.
- Generic filler is failure.
- Every substage must include Objective, Method, Findings, Evidence, Interpretation, Scores, Risks, Output to Next Substage, and Decision.
- Every stage must end with `stage-report.md`, `checkpoint.md`, `decision-log.md`, and `next-stage-brief.md`.
- Next stages must read `next-stage-brief.md` before proceeding.
- Files are memory.
- If evidence is unavailable, write a blocker instead of hallucinating.
- Do not proceed to the next major stage until required substage files and stage handoff files exist.
- Evidence must be collected before analysis.
- Every research, scoring, Q-Gate, discovery, audit, and packaging substage must contain Evidence Pack, Source Log, Analysis, and Decision sections.
- Unsupported claims must be placed under Weak Hypotheses.
- If evidence is unavailable, write exactly: `Evidence unavailable. This is a hypothesis, not a finding.`
- No evidence, no conclusion. No robustness, no ranking. No demo, no public product.
- Do not confuse file existence with workflow completion. A completed product must pass the workflow substance audit or explicitly record why it failed.

## Workflow Substance Audit Protocol

Before claiming a product is workflow-complete, run:

```bash
python scripts/audit_workflow_substance.py --strict product-XXX
```

If the audit finds scaffold residue, many `Status: NOT_STARTED` files, heavy `TBD` text, one-module core risk, shallow tests/fixtures, or no user-ready artifact, do not call the product complete. Return to the relevant stage and repair it.

Product-025 is the current positive benchmark: broad evidence, authority-source moat, method-fit design, modular method architecture, fixture matrix, generated user artifact, confidence labels, risk mitigations, and claim-honest packaging. Future products should copy that execution discipline, not just the file layout.

Before starting a substage:
1. Read the previous substage files in the same stage.
2. Read `checkpoint.md` if it exists.
3. Read `decision-log.md` if it exists.

Before starting a new major stage:
1. Read the previous stage's `next-stage-brief.md`.
2. Read `stage-report.md` if more detail is needed.
3. Read individual substage files only if needed.

## Evidence-First Protocol
Research and analysis must happen in this order:
1. Collect evidence.
2. Fill the Evidence Pack table.
3. Fill the Source Log.
4. Write Analysis that cites evidence IDs.
5. Write Decision or update `decision-log.md`.

Every major claim must reference evidence IDs such as `E3` or `E7`. Model intuition is not evidence. Generic market commentary is not evidence. A long report is not evidence.

Completed research-heavy substages must include source quotas or explain why quotas could not be met. Completed data-heavy substages must include baseline analysis, robustness check, sensitivity check, error/outlier check, interpretation, and decision impact.

A candidate cannot pass Q-Gate mainly on `LOW` or `SPECULATIVE` substages. A candidate cannot become `PUBLIC_PRODUCT` unless demand evidence and demo potential are at least `MEDIUM` confidence.

## Broad Demand Discovery Protocol

Do not preselect the audience. Do not default to developer tools. Do not force non-developer products.

Start from broad market demand discovery, then select the strongest opportunity based on evidence quality, pain intensity, feasibility, distribution, demo potential, and product depth. Developer tools are allowed if they truly win the evidence comparison. If the final shortlist is dominated by developer tools, explain why developer-tool evidence is stronger than other categories.

Stage 1 must inspect multiple demand pools before product ideas are selected:

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

For each pool, collect available pain signals, source references, candidate opportunities, evidence quality, feasibility, distribution path, and likely product format. If evidence is unavailable for a pool, record that clearly instead of inventing signals.

Every Stage 1 run must complete `demand-bias-check.md`:

- If more than 60% of sources are developer sources, flag `DEV_SOURCE_BIAS`.
- If more than 70% of candidates are developer tools, require written justification.
- If the final winner is a developer tool, compare it against the top non-developer candidate.
- If the final winner is a non-developer tool, compare it against the top developer candidate.
- The winner must be justified by evidence, not category preference.

Stage 2 must include Evidence Breadth Score, Cross-Audience Strength Score, Source Diversity Score, Demand Specificity Score, Buildability Bias Risk, GitHub Bias Risk, and Category Overconcentration Risk. A product must not win only because it is easier for Codex to build or easier to package on GitHub.

## Product Classification Rule
Every candidate must be classified before build:

- `PUBLIC_PRODUCT`: external-user product that may become a standalone public GitHub repo.
- `INTERNAL_FACTORY_TOOL`: helps this factory but does not deserve a standalone public repo.
- `EXPERIMENT`: validates a risky mechanism or demand signal without public launch.
- `PARK`: promising but evidence is insufficient.
- `KILL`: weak, risky, undifferentiated, or not worth more work.

## Public Product Minimum Bar
A product can be small, but it cannot be shallow.

A candidate can be `PUBLIC_PRODUCT` only if it has:
- clear user persona
- clear external user pain
- complete user journey
- interactive surface, preferably local web app or strong interactive CLI
- visible demo moment
- sample input and output
- non-trivial core mechanism
- clear GitHub positioning
- strong README first screen
- quickstart
- test or smoke test
- low 30-minute copy risk

## Thin Tool Downgrade Rule
These are `INTERNAL_FACTORY_TOOL` by default:
- checklist tools
- simple analyzers
- README optimizers
- config checkers
- `.env` sync tools
- log summarizers
- thin wrappers around prompts
- small one-file CLI utilities
- simple parsers
- basic scoring scripts

They can become `PUBLIC_PRODUCT` only if upgraded into a deeper product with UI, workflow, demo, sample data, and clear external-user value.

## Build Rule
- Do not build 10 small tools.
- Build only one high-value `PUBLIC_PRODUCT` first unless explicitly instructed otherwise.
- If no candidate passes Q-Gate, do not build.
- If a candidate is `INTERNAL_FACTORY_TOOL`, route it to `internal-tools/` and do not publish it as a standalone repo.
- Record the decision and return to demand discovery when the public-product bar is not met.

## NIM API Secret Rules
The NVIDIA NIM API is a product capability, not a toy wrapper.

Required environment variables:
- `NVIDIA_NIM_API_KEY`
- `NVIDIA_NIM_BASE_URL`
- `NVIDIA_NIM_MODEL`

Never hardcode, log, commit, print, or expose a real API key. Do not put secrets in README, examples, markdown logs, tests, snapshots, frontend code, or GitHub diffs. Use `.env.example` placeholders only.

Any NIM-powered product must include:
- local or server-side API client module
- environment-variable config
- mock mode or sample fixture
- safe error handling for missing key, invalid key, rate limit, timeout, malformed response, empty response, and network failure
- smoke test that passes without a real key

Do not build products that are merely "ask NIM one question." NIM must increase product depth, demo quality, or real-world usefulness.

## Verification Rule
Before final response, always run or attempt:
- `git status`
- `git diff --stat`
- relevant test, lint, build, or smoke command if available

Final response must include:
- files changed
- workflow rules added
- commands run and results
- remaining issues or blockers
- confirmation that the workflow blocks shallow standalone CLI products from being treated as public products

## Product Depth Protocol

Frontend is not depth. Smoke test is not depth. README is not depth. A manual JSON calculator is not depth.

A reused scaffold is allowed. A shallow core is not allowed.

Similarity itself is not failure. Future products may reuse a local web app/backend/report architecture, but the core mechanism must be meaningfully deep for the domain. A product cannot pass as `TOP_10_PUBLISH` merely by changing labels, changing an input file type, adding a few regex rules, and generating a Markdown report.

Before calling any product a strong `PUBLIC_PRODUCT`, explicitly verify:

- Core capability is implemented.
- User data can enter through a real data path, not only hand-written sample JSON.
- Input automation reduces user work.
- User friction is acceptable for the target persona.
- Config, pricing, model lists, API limits, benchmarks, or external assumptions can be updated by users.
- Quantitative output labels what is measured, estimated, manually assumed, uncertain, and decision-impacting.
- README claims map to implemented functionality.

If the product mainly asks the user to manually enter all important values, runs deterministic formulas, and outputs a formatted report, classify it as `EXPERIMENT`, `INTERNAL_FACTORY_TOOL`, or `NEEDS_V2_BEFORE_LAUNCH`. Do not classify it as `TOP_10_PUBLISH`.

`NEEDS_V2_BEFORE_LAUNCH` means the idea may be good, but the implementation is too shallow to publish. Use it when a product needs real import, automation, configurable data, or deeper core capability before public release.

## Implementation Depth Protocol

Before calling a product `PUBLIC_PRODUCT` or `TOP_10_PUBLISH`, verify implementation depth:

- `Implementation Depth Gate`: score Core Logic Depth, Parser/Data Understanding Depth, Edge Case Coverage, Output Actionability, Test Depth, UI Specificity, Integration/Automation Depth, and Non-Trivial Mechanism Depth.
- `UI Specificity Gate`: the UI must include product-specific views or interactions, not only upload-button-report-output.
- `Core Mechanism Requirement`: every public product needs at least one non-trivial mechanism such as AST parsing, schema diffing, graph analysis, timeline reconstruction, confidence scoring, auto-fix patching, benchmark suite, SDK/proxy/plugin integration, or multi-file project analysis.
- `Fixture and Edge Case Depth`: include at least 3 realistic sample inputs, 5 edge cases, 1 malformed case, 1 complex case, and 1 negative/no-issue case when relevant.
- `Output Actionability Gate`: every finding should include location, severity, confidence, explanation, recommended fix, false-positive note when relevant, and next action.

Hard rules:

- Core Logic Depth < 5 blocks `PUBLIC_PRODUCT`.
- Core Logic Depth < 7 blocks `TOP_10_PUBLISH`.
- UI Specificity < 5 blocks `TOP_10_PUBLISH`.
- Test Depth < 5 blocks `TOP_10_PUBLISH`.
- Output Actionability < 6 blocks `TOP_10_PUBLISH`.
- Non-Trivial Mechanism Depth < 6 blocks `TOP_10_PUBLISH`.
- Toy Implementation Risk > 6 blocks `TOP_10_PUBLISH`.
- If the core is mostly keyword matching, regex matching, or shallow if-statements, it needs additional depth such as AST parsing, graph analysis, auto-fix, benchmark, real imports, configurable rules, confidence scoring, or multi-fixture regression tests.

Stage requirements:

- Stage 4 must create `core-mechanism-design.md`, `ui-specificity-design.md`, and `fixture-plan.md`.
- Stage 5 must block MVPs that can be implemented mostly by changing labels, regex rules, and README text from a previous product.
- Stage 6 must create `core-logic-depth-report.md` and `fixture-test-report.md`.
- Stage 7 must include `09_implementation_depth_reviewer.md`; if that reviewer returns `NEEDS_V2_BEFORE_LAUNCH`, `ship-or-not.md` cannot be `SHIP`.
- Stage 8 must check README depth honesty: do not imply advanced analysis when implementation is static rules; label static rules, sample-only support, and roadmap features clearly.

## Real-World Depth Protocol

A real core mechanism is necessary but not sufficient. A product can parse real files, build a graph, run tests, and still be too shallow if it only handles toy examples and ignores real ecosystem complexity.

Before `TOP_10_PUBLISH`, verify:

- `Real-World Depth Gate`: the product survives realistic ecosystem variants, not only curated samples.
- `Ecosystem Compatibility Gate`: document supported and unsupported variants. For npm tools, check package-lock v1/v2/v3, workspaces, monorepos, dev/prod/optional/peer deps, overrides/resolutions, scoped packages, nested deps, and large lockfiles.
- `External Data Integration Gate`: products claiming security, pricing, vulnerability, market, or risk analysis must use authoritative external data or clearly label output as structural/local/heuristic.
- `Remediation Depth Gate`: findings need affected path, severity, confidence, why it matters, direct dependency or owner action, override/resolution option when relevant, next command/action, and false-positive note.
- `Real Corpus Benchmark Gate`: public products need at least 3 realistic projects or fixtures, 1 complex case, and 1 large case when relevant. Record node count, edge count, runtime, findings count, and false-positive concerns.
- `CI / Automation Readiness Gate`: developer tools need at least one automation path such as CLI `--ci`, JSON export, Markdown export, SARIF export, GitHub Actions example, exit-code threshold, config file, or machine-readable report.
- `README Claim Honesty Gate`: README claims must match implemented depth. Do not call a structural analyzer a vulnerability scanner unless advisory/vulnerability data is integrated.

Hard rules:

- Products with only toy fixtures cannot be `TOP_10_PUBLISH`.
- Products claiming security/risk analysis must either use authoritative external data or label output as structural risk only.
- Products without remediation guidance cannot be `TOP_10_PUBLISH`.
- Developer tools without CLI/export/CI path lose launch readiness.
- Generic upload-report UI must be penalized.
- README claims must not exceed implementation depth.

Stage requirements:

- Stage 4 must create `real-world-depth-design.md`, `ecosystem-compatibility-plan.md`, `external-data-integration-plan.md`, and `real-corpus-benchmark-plan.md`.
- Stage 6 must create `real-corpus-benchmark-report.md`, `ci-automation-readiness-report.md`, and `remediation-depth-report.md`.
- Stage 7 must include `10_real_world_depth_reviewer.md`.

## Disciplinary Method Fit Protocol

A product should have a natural analytical method core. Do not stop at parse input -> score a few fields -> generate report.

Before calling an analytical product `PUBLIC_PRODUCT` or `TOP_10_PUBLISH`, verify:

- `Disciplinary Method Fit Gate`: identify the discipline or analytical tradition, methods that naturally fit, methods that do not fit, the minimum serious method core, shallow failure mode, over-engineering failure mode, and how the method improves user decisions.
- `Method Depth Gate`: score Method Fit, Method Depth, Uncertainty Handling, Assumption Challenge, Cross-Validation, and Decision Impact.
- `Multi-Perspective Reasoning Gate`: for judgment, planning, prioritization, strategy, risk, life decisions, business decisions, or tradeoffs, require at least one of scenario analysis, user-adjustable weights or assumptions, devil's advocate critique, sensitivity analysis, confidence scoring, assumption review, or final synthesis.

Hard rules:

- Method Fit < 6 blocks `TOP_10_PUBLISH`.
- Method Depth < 6 blocks `TOP_10_PUBLISH` for analytical products.
- Shallow Scoring Risk > 6 blocks `TOP_10_PUBLISH`.
- Method Theater Risk > 6 blocks `TOP_10_PUBLISH`.
- If the product only uses simple thresholds and generic scoring, it cannot be a strong `PUBLIC_PRODUCT`.
- If an advanced method is added but does not naturally fit the problem, downgrade Method Fit.
- If uncertainty matters but is ignored, downgrade launch readiness.
- If assumptions drive the conclusion but are never challenged, downgrade launch readiness.
- If the product makes recommendations, it must explain what assumptions would flip the recommendation.

Do not force Monte Carlo into every product. Do not force multi-agent design into every product. The method must fit the problem. No method theater.

Stage requirements:

- Stage 4 must create `method-fit-map.md`, `analytical-core-design.md`, and `uncertainty-and-assumption-map.md`.
- Stage 5 must specify the method core, minimum analytical depth, uncertainty handling, assumption challenge mechanism, method-specific tests, and anti-shallow-scoring rule.
- Stage 6 must create `method-implementation-report.md`.
- Stage 7 must include `13_method_problem_fit_reviewer.md`; if that reviewer fails, `ship-or-not.md` cannot be `SHIP`.
- Stage 8 must explain the implemented method honestly and must not claim `AI-powered`, `Monte Carlo`, `multi-agent`, `optimization`, or advanced analysis unless it exists in code.

## Business Workflow Depth Protocol

A business product must reduce real operating work. It is not enough to import CSV, calculate a score, show a dashboard, generate a report, or write generic recommendations.

This protocol applies to non-developer operational products such as inventory planning, invoice follow-up, budgeting, procurement, scheduling, hiring, applicant planning, sales operations, small business workflows, personal finance workflows, and education planning workflows.

Before `TOP_10_PUBLISH`, verify:

- `Business Workflow Depth Gate`: the product answers what the user should do next, what to do first, why, under what constraint, with what risk, and what changes if assumptions change.
- `Data Sufficiency Gate`: required data is naturally available, required and optional fields are explicit, missing fields trigger warnings, and incomplete data downgrades confidence.
- `Business Constraint Gate`: at least two meaningful constraints are modeled or explicitly handled, such as budget, cash flow, lead time, MOQ, storage, shelf life, time, labor, seasonality, legal/compliance boundary, or priority tradeoff.
- `Source-System Preset Gate`: CSV/XLSX products identify likely source systems, export formats, column variants, and mapping or preset needs.
- `Operational Actionability Gate`: outputs contain what to do, why it matters, priority, expected impact, risk, required input/resource, and next action.
- `What-if / Constraint Simulation Gate`: decision-support products test at least one assumption or constraint change, and recommendation confidence changes when rankings are unstable.
- `Realistic Business Fixture Gate`: samples include realistic messiness, missing fields, malformed values, edge cases, no-action cases, high-priority cases, low-priority cases, and conflicting priorities.

Hard rules:

- Spreadsheet Trap Risk > 6 blocks `TOP_10_PUBLISH`.
- Business Constraint Depth < 5 blocks `TOP_10_PUBLISH` for operational products.
- Operational Actionability < 6 blocks `TOP_10_PUBLISH`.
- Data Sufficiency Score < 6 requires `FIX_BEFORE_SHIP` or `NEEDS_V2_BEFORE_LAUNCH`.
- Missing fields must not silently produce confident output.
- A generic CSV analyzer with a web UI cannot pass as a strong public product.

Stage requirements:

- Stage 1 must record where the user's data lives, what format it naturally exists in, what operational constraints matter, what decision the user needs to make, and what current workaround is used.
- Stage 4 must create `business-workflow-map.md`, `data-sufficiency-map.md`, `constraint-map.md`, and `source-system-map.md`.
- Stage 6 must create `data-quality-report.md`, `missing-field-report.md`, `business-fixture-report.md`, `what-if-simulation-report.md`, and `business-constraint-report.md`.
- Stage 7 must include `12_business_workflow_reviewer.md`; if that reviewer says the product is only a spreadsheet with a web UI, `ship-or-not.md` cannot be `SHIP`.
- Stage 8 must state supported input sources honestly, explain assumptions, show sample output, group limitations near the end, and avoid overclaiming integrations or automation.

## Bilingual GitHub Release Protocol

When a product is approved for GitHub launch, prepare two documentation surfaces:

- English default branch: the primary public asset. `README.md`, GitHub description, release copy, demo instructions, and topics should be optimized for broad GitHub discovery.
- Chinese documentation branch: a `zh-CN` branch or equivalent localized branch where descriptive and promotional materials are Chinese. Product code, app UI, tests, examples, sample data, and behavior must remain the same unless the user explicitly asks for product localization.

Rules:
- Do not change product behavior just to create the Chinese branch.
- Do not translate code identifiers, config keys, sample data schemas, env var names, CLI commands, API routes, or test assertions.
- Chinese branch changes should be limited to README, launch copy, GitHub-facing docs, and explanatory markdown.
- GitHub About description and topics are repo-level, not branch-level. Keep repo metadata English by default for the main asset unless the user explicitly wants a Chinese repo-level description.
- Before public upload, run a secret scan, confirm `.env` is ignored, and verify no API key appears in README, logs, examples, or diffs.
- Public GitHub creation or changing repo visibility/sharing requires explicit action-time confirmation.

## GitHub Launch Page Protocol

GitHub packaging must make a product understandable and star-worthy. Do not publish a technically runnable product with a README that reads like a developer note.

Every `PUBLIC_PRODUCT` must produce:

- `README.md`: English default README.
- `README.zh-CN.md`: complete natural Chinese README.
- `github-description.md`: short description under 160 characters, longer description, and 3 alternatives.
- `github-topics.md`: 10-20 relevant topics.
- `launch-summary.md`: final launch asset summary and decision.
- `readme-claim-check.md`: claim-to-implementation mapping.

README rules:

- The first screen must answer what this is, who it is for, what pain it solves, what output it creates, why it matters, and how to try it.
- Include `English | 中文` in `README.md` and `中文 | English` in `README.zh-CN.md`.
- Both READMEs must share the same structure and claims.
- Chinese copy must read naturally, not like a partial literal translation.
- Include Problem, Why Existing Approaches Are Not Enough, What This Project Does, Key Features, Demo / Screenshots, Quick Start, Example Input / Output, Use Cases, How It Works, Project Structure, Roadmap, Limitations, and License.
- Include a concrete `Why this is useful` section.
- Limitations belong near the end. Do not scatter caveats through the hero, problem, features, or quickstart.
- Do not overclaim. Roadmap features are roadmap, demo-only features are demo, and mock features are mock.

Stage 8 must complete the GitHub Launch Page Gate. Stage 7 must include `11_github_readme_reviewer.md`.

The GitHub README Reviewer must check:

- Would I understand the project in 10 seconds?
- Would I keep reading?
- Would I star it?
- Is the first screen strong?
- Is the README too technical too early?
- Are limitations scattered too much?
- Are product claims honest?
- Are screenshots/GIFs missing?
- Is the Chinese README natural?
- Is the English README professional?

If the GitHub README Reviewer fails the README, `ship-or-not.md` cannot be `SHIP`.
