# Stage 2: Launch Slot Scoring

## Purpose
Strictly score candidates, classify every candidate, and decide which single public-product candidate is worth building first.

## Required Input Files
- Stage 1 `next-stage-brief.md`
- Stage 1 `demand_synthesis` substage
- `raw-signal-log.md`
- Stage 1 `demand-bias-check.md`
- `templates/launch-slot-scorecard.md`
- `memory/scoring-calibration.md`

## Required Substages
1. `01_user_pain_scoring.md` - User Pain Scoring
2. `02_demo_pull_scoring.md` - Demo Pull Scoring
3. `03_expected_star_pull_scoring.md` - Expected Star Pull Scoring
4. `04_build_maintenance_cost_scoring.md` - Build / Maintenance Cost Scoring
5. `05_differentiation_copy_risk_scoring.md` - Differentiation / 30-Minute Copy Risk Scoring
6. `06_monetization_distribution_scoring.md` - Monetization / Distribution Scoring
7. `07_final_launch_slot_ranking.md` - Final Launch Slot Ranking

## Required Output Files
- all required substage files
- `demand-scorecard.md`
- `opportunity-ranking.md`
- `batch-shortlist.md`
- `launch-slot-ranking.md`
- `classification-table.md`
- `stage-report.md`
- `checkpoint.md`
- `decision-log.md`
- `next-stage-brief.md`

## Classification Rule
Every candidate must be classified as:
- `PUBLIC_PRODUCT`
- `INTERNAL_FACTORY_TOOL`
- `EXPERIMENT`
- `PARK`
- `KILL`

## Demand Bias Scoring Addendum
Stage 2 must score whether the winning candidate actually earned its rank across demand pools.

Add these fields to every candidate scorecard:
- Evidence Breadth Score: 1-10
- Cross-Audience Strength Score: 1-10
- Source Diversity Score: 1-10
- Demand Specificity Score: 1-10
- Buildability Bias Risk: 1-10
- GitHub Bias Risk: 1-10
- Category Overconcentration Risk: 1-10

Rules:
- A candidate should not win only because it is easier to build.
- A candidate should not win only because it fits GitHub better.
- A candidate should win because it has strong evidence, clear pain, feasible MVP, strong demo, and product depth.
- If Buildability Bias Risk is high, downgrade confidence.
- If GitHub Bias Risk is high, require comparison against non-developer candidates.
- If the final shortlist is dominated by developer tools, explain why the developer-tool evidence is stronger than other categories.
- If a non-developer idea wins, explain why it is not being forced by category preference.

The final selected product must include:
1. Why this audience/problem won
2. What evidence supports it
3. What competing opportunities were rejected
4. Why developer-tool bias or non-developer bias did not decide the outcome
5. Why this is not merely the easiest thing for Codex to build
6. Why this deserves to proceed to Product Discovery

## Preserved Hard Gates
- Demo Pull < 7 cannot be `TOP_10_PUBLISH`.
- Expected Star Pull < 7 cannot be `TOP_10_PUBLISH`.
- Depth Penalty > 6 cannot be `TOP_10_PUBLISH`.
- 30-Minute Copy Risk > 6 cannot be `TOP_10_PUBLISH`.
- checklist/analyzer/parser/config checker defaults to `INTERNAL_FACTORY_TOOL`.

## Substage Quality Rule
Each completed scoring substage must follow `templates/substage-report-template.md`, contain at least 500 meaningful words, include scores with evidence, and name exactly what should move to the next scoring substage.

## Handoff Rule
The stage is incomplete until `next-stage-brief.md` carries the final ranking, classifications, rejected/downgraded candidates, risks, and the exact candidate entering Q-Gate.

## Failure / Blocker Behavior
If no candidate meets public-product gates, do not build. Return to Stage 1 or classify all candidates as internal, parked, experimental, or killed.

## Evidence-First Rule
Scoring conclusions must reference evidence IDs from Stage 1 and this stage. Data-heavy substages must include baseline analysis, robustness check, sensitivity check, error/outlier check, interpretation, and decision impact. No robustness, no ranking. If baseline and robustness disagree, use the more conservative classification.

## Product Depth Scoring Addendum
Add these dimensions to every launch-slot scorecard:
- Core Capability Completeness: 1-10
- Input Automation Depth: 1-10
- User Friction: 1-10
- Real Data Path Strength: 1-10
- Configuration Freshness: 1-10
- Estimation Accuracy: 1-10
- Integration Potential: 1-10
- Frontend Calculator Risk: 1-10

Hard rules:
- Core Capability Completeness < 7 blocks `TOP_10_PUBLISH`.
- Input Automation Depth < 5 blocks `TOP_10_PUBLISH` unless explicitly justified.
- Real Data Path Strength < 5 blocks `TOP_10_PUBLISH` for analytics, simulator, observability, workflow, log, issue, review, or behavior products.
- User Friction > 7 blocks strong `PUBLIC_PRODUCT` unless the product is explicitly for advanced developers and value is exceptional.
- Frontend Calculator Risk > 6 forces `PIVOT` or `NEEDS_V2_BEFORE_LAUNCH`.
- If baseline ranking says publish but product-depth gates fail, choose the conservative classification.

## Implementation Depth Scoring Addendum
Add these dimensions to every launch-slot scorecard:
- Core Logic Depth: 1-10
- UI Specificity: 1-10
- Parser/Data Depth: 1-10
- Edge Case Coverage: 1-10
- Test Depth: 1-10
- Output Actionability: 1-10
- Non-Trivial Mechanism Depth: 1-10
- Scaffold Reuse Risk: 1-10
- Toy Implementation Risk: 1-10

Hard rules:
- Core Logic Depth < 5 blocks `PUBLIC_PRODUCT`.
- Core Logic Depth < 7 blocks `TOP_10_PUBLISH`.
- UI Specificity < 5 blocks `TOP_10_PUBLISH`.
- Test Depth < 5 blocks `TOP_10_PUBLISH`.
- Output Actionability < 6 blocks `TOP_10_PUBLISH`.
- Non-Trivial Mechanism Depth < 6 blocks `TOP_10_PUBLISH`.
- Toy Implementation Risk > 6 blocks `TOP_10_PUBLISH`.
- Scaffold Reuse Risk > 7 requires stronger core mechanism evidence.
- If a product is mainly keyword/regex scanning, it cannot be `TOP_10_PUBLISH` unless it adds depth such as AST parsing, graph analysis, auto-fix, benchmark, real imports, configurable rules, confidence scoring, or multi-fixture regression tests.

## Real-World Depth Scoring Addendum
Add these dimensions to every launch-slot scorecard:
- Ecosystem Compatibility: 1-10
- External Data Integration: 1-10
- Remediation Depth: 1-10
- Real Corpus Benchmark: 1-10
- CI / Automation Readiness: 1-10
- UI Domain Specificity: 1-10
- README Claim Honesty: 1-10

Hard rules:
- Products with only toy fixtures cannot be `TOP_10_PUBLISH`.
- Products claiming security, vulnerability, pricing, market, or risk analysis must use authoritative external data or label output as structural/local/heuristic.
- Products without remediation guidance cannot be `TOP_10_PUBLISH`.
- Developer tools without CLI/export/CI path lose launch readiness.
- Generic upload-report UI must be penalized.
- README claims must not exceed implementation depth.

## Business Workflow Depth Scoring Addendum
For non-developer operational products, add these dimensions:
- Data Sufficiency Score: 1-10
- Business Constraint Depth: 1-10
- Operational Actionability: 1-10
- Source-System Fit: 1-10
- What-if Depth: 1-10
- Realistic Fixture Depth: 1-10
- Business Workflow Depth: 1-10
- Spreadsheet Trap Risk: 1-10

Hard rules:
- Spreadsheet Trap Risk > 6 blocks `TOP_10_PUBLISH`.
- Business Constraint Depth < 5 blocks `TOP_10_PUBLISH` for operational products.
- Operational Actionability < 6 blocks `TOP_10_PUBLISH`.
- Data Sufficiency Score < 6 requires `FIX_BEFORE_SHIP` or `NEEDS_V2_BEFORE_LAUNCH`.
- A candidate should not win merely because its spreadsheet calculation is easy to implement.

## Disciplinary Method Fit Scoring Addendum
Every analytical product must be scored for whether its method naturally fits the problem.

Add these dimensions to every launch-slot scorecard:
- Disciplinary Method Fit: 1-10
- Method Depth: 1-10
- Analytical Originality: 1-10
- Uncertainty Handling: 1-10
- Assumption Challenge: 1-10
- Multi-Perspective Reasoning: 1-10
- Method Theater Risk: 1-10
- Shallow Scoring Risk: 1-10

Hard rules:
- Method Fit < 6 blocks `TOP_10_PUBLISH`.
- Method Depth < 6 blocks `TOP_10_PUBLISH` for analytical products.
- Shallow Scoring Risk > 6 blocks `TOP_10_PUBLISH`.
- Method Theater Risk > 6 blocks `TOP_10_PUBLISH`.
- If the product only uses simple thresholds and generic scoring, it cannot be a strong `PUBLIC_PRODUCT`.
- If an advanced method is added but does not naturally fit the problem, downgrade Method Fit.
- If uncertainty matters but is ignored, downgrade launch readiness.
- If assumptions drive the conclusion but are never challenged, downgrade launch readiness.
- A candidate should not win because a shallow scorecard makes it look analytical.
