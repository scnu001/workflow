# Stage 5: MVP Specification

## Purpose
Make the product implementation-ready so Codex does not need to guess during Build.

## Required Input Files
- Stage 4 `next-stage-brief.md`
- `product-discovery.md`
- `templates/product-build-brief.md`

## Required Substages
1. `01_prd.md` - PRD
2. `02_user_stories.md` - User Stories
3. `03_ux_page_or_cli_structure.md` - UX / Page / CLI Structure
4. `04_data_model.md` - Data Model
5. `05_api_and_nim_integration_plan.md` - API and NIM Integration Plan
6. `06_acceptance_criteria.md` - Acceptance Criteria
7. `07_test_plan.md` - Test Plan

## Required Output Files
- all required substage files
- `mvp-prd.md`
- `technical-spec.md`
- `acceptance-criteria.md`
- `stage-report.md`
- `checkpoint.md`
- `decision-log.md`
- `next-stage-brief.md`

## NIM Rules
If NIM is used, use environment variables only, preserve mock mode, preserve no-key smoke tests, and never expose secrets to frontend code.

## Substage Quality Rule
Each completed specification substage must follow `templates/substage-report-template.md`, contain at least 500 meaningful words, and include concrete implementation requirements, risks, and output to the next substage.

## Handoff Rule
The stage is incomplete until `next-stage-brief.md` provides an implementation-ready build brief, sample input/output, acceptance criteria, test plan, and explicit non-goals.

## Failure / Blocker Behavior
If Codex would need to guess core behavior, stop and complete missing specification substages before Build.

## Evidence-First Rule
Specification decisions must cite source substages, evidence IDs, or local files. If API/NIM behavior is unverified, mark it as a hypothesis and preserve mock mode. No unsupported capability claims may enter Build.

## Product Depth Specification Requirements
The MVP spec must include:
1. Must-have core capability.
2. Real data path requirement.
3. Input automation requirement.
4. Configuration freshness requirement.
5. Accuracy and uncertainty requirement.
6. Minimum acceptable import/export support.
7. Explicit anti-shallow rule.
8. Minimum core mechanism.
9. Parser/data depth requirement.
10. UI specificity requirement.
11. Fixture depth requirement.
12. Edge case test plan.
13. Output actionability requirement.
14. Explicit anti-toy rule.

If the MVP specification allows only manual JSON input for the main workflow, classify it as `EXPERIMENT`, not strong `PUBLIC_PRODUCT`, unless it is explicitly justified as a developer config tool.

If the MVP can be implemented mostly by changing labels, regex rules, and README text from the previous product, it is not a valid `PUBLIC_PRODUCT` MVP.

## Real-World Depth MVP Requirements
The MVP spec must include:
- ecosystem compatibility requirements
- external data integration or honest structural-risk scope
- remediation depth requirement
- real corpus benchmark requirement
- CI/export/automation requirement
- UI domain specificity requirement
- README claim honesty requirement

If the product cannot handle real ecosystem complexity beyond toy fixtures, block `TOP_10_PUBLISH`.

For Agent Budget Lab-type products, require at least custom model price table import, editable pricing config, generic JSONL/CSV trace import, token usage field parsing when present, fallback token estimation when missing, baseline/conservative/sensitivity analysis, sample real-like trace file, and no reliance on hand-written full workflow JSON as the only input path.

## Business Workflow MVP Requirements
For non-developer operational products, the MVP spec must include:
- required fields
- missing field behavior
- business constraints modeled
- source-system presets or flexible mapping
- action-oriented outputs
- what-if/sensitivity
- realistic fixture requirements
- README honesty requirements

If the MVP is only CSV import -> score -> dashboard/report, classify it as `NEEDS_V2_BEFORE_LAUNCH` until it models real constraints and produces operational actions.

## Disciplinary Method MVP Requirements
The MVP spec must include:
- method core specification
- minimum analytical depth
- uncertainty handling
- assumption challenge mechanism
- method-specific tests
- anti-shallow-scoring rule

If the product is a decision, planning, prioritization, risk, strategy, or tradeoff product, the MVP must include:
- scenario analysis or sensitivity analysis
- user-adjustable assumptions, weights, thresholds, or priorities where relevant
- confidence or uncertainty explanation
- recommendation robustness check
- explanation of what would flip the recommendation

If the MVP can be implemented as parse input -> score a few fields -> generate report, it is not a valid strong `PUBLIC_PRODUCT` MVP unless the method-fit map proves that the problem is genuinely that simple and the output is still actionable.
