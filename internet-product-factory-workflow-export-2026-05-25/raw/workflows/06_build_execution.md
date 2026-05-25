# Stage 6: Build Execution

## Purpose
Build only one high-value `PUBLIC_PRODUCT` first unless explicitly instructed otherwise.

## Required Input Files
- Stage 5 `next-stage-brief.md`
- `mvp-prd.md`
- `technical-spec.md`
- `acceptance-criteria.md`

## Required Substages
1. `01_scaffold_log.md` - Scaffold Log
2. `02_core_logic_log.md` - Core Logic Log
3. `03_ui_or_cli_surface_log.md` - UI or CLI Surface Log
4. `04_example_data_log.md` - Example Data Log
5. `05_nim_or_mock_integration_log.md` - NIM or Mock Integration Log
6. `06_smoke_test_log.md` - Smoke Test Log
7. `07_readme_draft_log.md` - README Draft Log

## Required Output Files
- all required substage files
- `build-log.md`
- `run-instructions.md`
- `build-depth-checklist.md`
- `core-logic-depth-report.md`
- `fixture-test-report.md`
- `real-corpus-benchmark-report.md`
- `ci-automation-readiness-report.md`
- `remediation-depth-report.md`
- `stage-report.md`
- `checkpoint.md`
- `decision-log.md`
- `next-stage-brief.md`

## Build Substage Evidence
Each build substage must document:
- what was implemented
- files changed
- why the implementation matches acceptance criteria
- what command was run
- result
- blocker if any

## Substage Quality Rule
Each completed build substage must follow `templates/substage-report-template.md` and contain at least 500 meaningful words of implementation evidence, not essay filler.

## Handoff Rule
The stage is incomplete until `next-stage-brief.md` states what was built, what commands passed or failed, what remains, and what Audit must inspect.

## Failure / Blocker Behavior
Do not generate 10 shallow tools. Do not create placeholder products. Do not produce only README files. Stop launch if secrets are detected.

## Evidence-First Rule
Build substages use implementation evidence rather than market evidence. Record commands, terminal outputs, files changed, smoke-test results, malformed-input behavior where relevant, and blockers. No robustness, no launch readiness.

## Build Depth Checklist
Before marking build launch-ready, create and complete `build-depth-checklist.md`:
- core capability implemented?
- real data path implemented?
- custom config implemented?
- sample data included?
- input validation implemented?
- uncertainty handled?
- robustness/sensitivity implemented?
- smoke test covers real-data path?
- README does not overclaim?
- core logic split into domain modules, or monolith explicitly justified?
- user-ready artifact implemented when the product requires one?

Build logs must distinguish demo-only features, real user features, mock features, and incomplete V2 features. If any critical item is missing, use `NEEDS_V2_BEFORE_LAUNCH`.

Run `python scripts/audit_workflow_substance.py --strict product-XXX` before marking the product workflow-complete. If the audit reports scaffold residue, one-module core risk, shallow tests, shallow fixtures, or no user-ready artifact, repair the workflow or implementation before launch.

## Implementation Depth Build Reports
Before marking build complete, create `core-logic-depth-report.md` and `fixture-test-report.md`.

`core-logic-depth-report.md` must verify:
- core logic is not toy-level
- frontend is not only a relabeled shell
- core logic is not collapsed into one large analyzer file unless the domain is genuinely simple and the monolith is explicitly justified
- core mechanism is more than keyword/regex matching or has added parser, graph, auto-fix, benchmark, confidence, or multi-fixture depth
- final user-ready artifact is implemented, not merely described in README
- output includes specific actionable findings
- README does not overstate depth

`fixture-test-report.md` must verify:
- at least 3 realistic sample inputs exist for public products
- at least 5 edge cases are documented
- malformed input is tested
- empty or missing input is tested where relevant
- complex input is tested
- no-issue / negative case is tested where relevant
- tests do more than prove the app starts

## Real-World Depth Build Reports
Create `real-corpus-benchmark-report.md`, `ci-automation-readiness-report.md`, and `remediation-depth-report.md`.

Before launch readiness:
- record realistic corpus/project names
- record node count, edge count, runtime, findings count, and false-positive concerns
- prove at least one CLI/export/CI path
- prove findings include affected path, severity, confidence, why it matters, direct dependency or owner action, override/resolution option when relevant, and next command/action
- label missing external data as a scope limitation

## Business Workflow Build Reports
For non-developer operational products, create or complete:
- `data-quality-report.md`
- `missing-field-report.md`
- `business-fixture-report.md`
- `what-if-simulation-report.md`
- `business-constraint-report.md`
- `method-implementation-report.md`

Build must include:
- data quality check
- missing field warnings
- realistic sample dataset
- at least one constraint modeled
- action-oriented output
- what-if or sensitivity output
- tests for messy inputs

If missing fields silently produce confident output, or if samples are clean happy-path-only rows, do not mark the build launch-ready.

## Method Implementation Report
Before marking build complete, create `method-implementation-report.md`.

It must explain:
- which analytical method was implemented
- where in code it is implemented
- what assumptions are used
- what sensitivity or robustness checks exist
- how uncertainty is labeled or handled
- how assumptions are challenged
- why this is not just simple threshold scoring
- what remains shallow, incomplete, or roadmap

Do not claim Monte Carlo, multi-agent analysis, optimization, AI-powered reasoning, forecasting, or advanced domain analysis unless that method exists in code and tests.
